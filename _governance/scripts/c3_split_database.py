#!/usr/bin/env python3
"""c3_split_database.py — 阶段C3：拆分 ComputerScience/Database.md。

按 4 个 H1：# 数据库（两个 H2 合并）+ # DBF 警告 -> Database/数据库基础.md；
# SQL Server -> Database/SQLServer.md；# MySQL -> Database/MySQL.md。
附带机械修复标题跳级（栈归一：子标题不得高于父级+1）。
"""
import re
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
SRC = VAULT / "ComputerScience" / "Database.md"
OUT_DIR = VAULT / "ComputerScience" / "Database"

FENCE_RE = re.compile(r"^\s*(```|~~~)")
H1_RE = re.compile(r"^# (.*)")
HEAD_RE = re.compile(r"^(#{1,6}) (.*)")


def normalize_headings(lines, label):
    """标题不跳级：若标题层级 > 父级+1，降为父级+1。"""
    stack = []
    out = []
    changes = []
    in_fence = False
    for i, line in enumerate(lines):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        m = HEAD_RE.match(line)
        if m:
            lvl = len(m.group(1))
            while stack and stack[-1] >= lvl:
                stack.pop()
            new = (stack[-1] + 1) if stack else 1
            if new != lvl:
                changes.append((i + 1, lvl, new, m.group(2)))
                line = "#" * new + " " + m.group(2)
            stack.append(new)
        out.append(line)
    for ln, old, new, t in changes:
        print(f"  heading fix [{label}] L{ln}: L{old} -> L{new} {t}")
    return out


def read_sections():
    lines = SRC.read_text(encoding="utf-8").split("\n")
    h1s = []
    in_fence = False
    for i, line in enumerate(lines):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = H1_RE.match(line)
        if m:
            h1s.append((i, m.group(1).strip()))
    secs = {}
    for k, (i, title) in enumerate(h1s):
        end = h1s[k + 1][0] if k + 1 < len(h1s) else len(lines)
        secs[title] = lines[i:end]
    return secs


def clean(body):
    while body and not body[0].strip():
        body.pop(0)
    while body and not body[-1].strip():
        body.pop()
    return body


def main():
    secs = read_sections()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # 数据库基础.md：# 数据库 全章 + # DBF 警告并入末尾
    db = list(secs["数据库"])
    db += ["", "## DBF", ""] + clean(secs["DBF"][1:])  # [1:] 跳过原 # DBF 标题行
    db = normalize_headings(db, "数据库基础")
    (OUT_DIR / "数据库基础.md").write_text(
        "\n".join(db).rstrip() + "\n", encoding="utf-8", newline="\n"
    )

    # SQLServer.md
    ss = normalize_headings(list(secs["SQL Server"]), "SQLServer")
    (OUT_DIR / "SQLServer.md").write_text(
        "\n".join(clean(ss)).rstrip() + "\n", encoding="utf-8", newline="\n"
    )

    # MySQL.md
    my = normalize_headings(list(secs["MySQL"]), "MySQL")
    (OUT_DIR / "MySQL.md").write_text(
        "\n".join(clean(my)).rstrip() + "\n", encoding="utf-8", newline="\n"
    )

    print("written:", sorted(p.name for p in OUT_DIR.glob("*.md")))


if __name__ == "__main__":
    main()
