#!/usr/bin/env python3
"""fixlinks.py — 重算 vault 内所有 Markdown 相对链接。

规则：
- 扫描所有 .md（跳过 .git/.obsidian/_governance/scripts 自身）。
- 对 ](path) 形式链接（图片与笔记），若 path 不含 scheme（http/https/mailto/#），
  视为 vault 相对路径处理：
  1. 以“链接书写时所在文件”的旧深度解析出的 attachments 绝对位置为锚，
     或更稳健地：直接尝试多种候选解释，找到在 vault 中真实存在的目标文件。
  2. 重写为“从该文件当前所在目录到目标”的正确相对路径。
- URL 编码统一：目标文件名含空格时使用 %20。

本脚本是幂等的：链接已正确时输出不变。
"""
import os
import re
import sys
import urllib.parse
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]  # _governance/scripts/fixlinks.py -> vault root
SKIP_DIRS = {".git", ".obsidian", ".claude", "node_modules"}

# 收集 vault 内全部文件（相对路径，正斜杠）
all_files = {}
for p in VAULT.rglob("*"):
    if p.is_file():
        rel = p.relative_to(VAULT).as_posix()
        if rel.split("/")[0] in SKIP_DIRS:
            continue
        all_files[rel.lower()] = rel

LINK_RE = re.compile(r"(!?)\[([^\]]*)\]\(([^)]+)\)")

def decode(seg: str) -> str:
    return urllib.parse.unquote(seg)

def find_target(cur_file: str, raw_path: str):
    """返回 vault 相对目标路径（或 None）。容忍历史错误深度。"""
    if raw_path.startswith(("http://", "https://", "mailto:", "#", "data:")):
        return None
    path_part = raw_path.split("#")[0]
    if not path_part:
        return None
    if path_part.startswith("/"):  # vault 绝对路径
        cand = path_part.lstrip("/")
        if cand.lower() in all_files:
            return all_files[cand.lower()]
        return None
    cur_dir = os.path.dirname(cur_file)
    # 候选1：按字面相对路径解析（正确情况）
    joined = os.path.normpath(os.path.join(cur_dir, decode(path_part))).replace("\\", "/")
    if joined.lower() in all_files:
        return all_files[joined.lower()]
    # 候选2：文件名在 attachments/ 下（处理历史多一级/少一级 ../ 的错误）
    base = decode(path_part).split("/")[-1]
    hits = [v for k, v in all_files.items() if v.lower().endswith("/" + base.lower()) or v.lower() == base.lower()]
    if len(hits) == 1:
        return hits[0]
    # 候选3：任意位置唯一同名文件
    if len(hits) > 1:
        # 优先 attachments/ 下的
        att = [h for h in hits if h.startswith("attachments/")]
        if len(att) == 1:
            return att[0]
    return None

def rel_link(cur_file: str, target: str) -> str:
    cur_dir = os.path.dirname(cur_file)
    rel = os.path.relpath(target, cur_dir or ".").replace("\\", "/")
    # URL 编码空格与特殊字符（保守：仅空格和括号）
    rel = rel.replace(" ", "%20").replace("(", "%28").replace(")", "%29")
    return rel

def fix_file(md: Path):
    text = md.read_text(encoding="utf-8")
    cur = md.relative_to(VAULT).as_posix()
    out = []
    changes = []
    # 逐行处理，跳过代码围栏
    in_fence = False
    for line in text.split("\n"):
        stripped = line.lstrip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        def repl(m):
            bang, label, raw = m.group(1), m.group(2), m.group(3)
            frag = ""
            rp = raw
            if "#" in raw:
                rp, frag = raw.split("#", 1)
                frag = "#" + frag
            if rp.startswith(("http://", "https://", "mailto:")):
                return m.group(0)
            if not rp:
                return m.group(0)
            tgt = find_target(cur, rp)
            if tgt is None:
                return m.group(0)
            new_rel = rel_link(cur, tgt)
            if new_rel == rp:
                return m.group(0)
            changes.append((raw.split("#")[0], new_rel))
            return f"{bang}[{label}]({new_rel}{frag})"
        out.append(LINK_RE.sub(repl, line))
    new_text = "\n".join(out)
    if new_text != text:
        md.write_text(new_text, encoding="utf-8", newline="\n")
    return changes

def main():
    total = 0
    for p in sorted(VAULT.rglob("*.md")):
        rel = p.relative_to(VAULT).as_posix()
        if rel.split("/")[0] in SKIP_DIRS or rel.startswith("_governance"):
            continue
        ch = fix_file(p)
        if ch:
            total += len(ch)
            for old, new in ch[:5]:
                print(f"{rel}: {old} -> {new}")
            if len(ch) > 5:
                print(f"{rel}: ... {len(ch)-5} more")
    print(f"DONE: {total} links fixed")

if __name__ == "__main__":
    main()
