#!/usr/bin/env python3
"""checklinks.py — 校验 vault 内 Markdown 相对链接完整性。

输出：
- DEAD：链接目标不存在（按当前文件位置解析；再做全库唯一文件名兜底）
- ORPHAN：attachments/ 下未被任何 md 引用的文件
- 退出码：有 DEAD 链接时为 1，否则 0。
"""
import os
import re
import sys
import urllib.parse
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
SKIP_DIRS = {".git", ".obsidian", ".claude", "node_modules"}
IGNORED_PREFIXES = ("http://", "https://", "mailto:", "#", "data:")

LINK_RE = re.compile(r"(!?)\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")

md_files = []
for p in VAULT.rglob("*.md"):
    rel = p.relative_to(VAULT).as_posix()
    if rel.split("/")[0] in SKIP_DIRS or rel.startswith("_governance"):
        continue
    md_files.append(p)

referenced = set()
dead = []
for md in md_files:
    cur = md.relative_to(VAULT).as_posix()
    text = md.read_text(encoding="utf-8")
    in_fence = False
    for i, line in enumerate(text.split("\n"), 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        # 行内代码段（`...`）内的链接不校验（占位示例）
        segs = line.split("`")
        scan_line = "".join(segs[0::2]) if len(segs) % 2 == 1 else line
        for m in LINK_RE.finditer(scan_line):
            raw = m.group(3)
            if raw.startswith(IGNORED_PREFIXES):
                continue
            rp = raw.split("#")[0]
            if not rp:
                continue
            dec = urllib.parse.unquote(rp)
            target = os.path.normpath(os.path.join(os.path.dirname(cur), dec)).replace("\\", "/")
            if (VAULT / target).exists():
                referenced.add(target.lower())
            else:
                # 全库唯一文件名兜底（历史坏深度）
                base = dec.split("/")[-1]
                hits = [
                    q.relative_to(VAULT).as_posix()
                    for q in md_files + list(VAULT.rglob("*.png")) + list(VAULT.rglob("*.jpeg")) + list(VAULT.rglob("*.gif")) + list(VAULT.rglob("*.jpg"))
                    if q.name.lower() == base.lower()
                ]
                if len(hits) == 1:
                    referenced.add(hits[0].lower())
                    dead.append((cur, i, raw, f"BAD-DEPTH (resolvable -> {hits[0]})"))
                else:
                    dead.append((cur, i, raw, "DEAD"))

orphans = []
if (VAULT / "attachments").is_dir():
    for p in (VAULT / "attachments").rglob("*"):
        if "_orphan" in p.parts:
            continue
        if p.is_file() and p.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}:
            rel = p.relative_to(VAULT).as_posix()
            if rel.lower() not in referenced:
                orphans.append(rel)

print(f"== {len(md_files)} md files scanned ==")
if dead:
    print(f"\n!! {len(dead)} broken/bad-depth links:")
    for cur, i, raw, why in dead:
        print(f"  [{why}] {cur}:{i} -> {raw}")
else:
    print("all links OK")
if orphans:
    print(f"\n?? {len(orphans)} orphan images in attachments/ (not referenced):")
    for o in orphans:
        print(f"  {o}")

sys.exit(1 if any(d[3] == "DEAD" for d in dead) else 0)
