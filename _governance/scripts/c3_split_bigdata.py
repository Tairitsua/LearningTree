#!/usr/bin/env python3
"""c3_split_bigdata.py — 阶段C3：拆分 ComputerScience/BigData.md。

## 概念 + ## Hadoop框架 -> BigData/Hadoop生态.md；## 云数据中心 -> BigData/云数据中心.md。
"""
import re
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
SRC = VAULT / "ComputerScience" / "BigData.md"
OUT_DIR = VAULT / "ComputerScience" / "BigData"

FENCE_RE = re.compile(r"^\s*(```|~~~)")
H2_RE = re.compile(r"^## (.*)")


def split_h2(lines):
    in_fence = False
    bounds = []
    for i, line in enumerate(lines):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = H2_RE.match(line)
        if m:
            bounds.append((i, m.group(1).strip()))
    secs = {}
    for k, (i, title) in enumerate(bounds):
        end = bounds[k + 1][0] if k + 1 < len(bounds) else len(lines)
        secs[title] = lines[i + 1 : end]
    return secs


def clean(body):
    while body and not body[0].strip():
        body.pop(0)
    while body and not body[-1].strip():
        body.pop()
    return body


def main():
    lines = SRC.read_text(encoding="utf-8").split("\n")
    secs = split_h2(lines)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    hadoop = ["# 大数据与 Hadoop 生态", "", "## 概念", ""] + clean(secs["概念"])
    hadoop += ["", "## Hadoop框架", ""] + clean(secs["`Hadoop`框架"])
    (OUT_DIR / "Hadoop生态.md").write_text(
        "\n".join(hadoop).rstrip() + "\n", encoding="utf-8", newline="\n"
    )

    cloud = ["# 云数据中心", ""] + clean(secs["云数据中心"])
    (OUT_DIR / "云数据中心.md").write_text(
        "\n".join(cloud).rstrip() + "\n", encoding="utf-8", newline="\n"
    )

    print("written:", sorted(p.name for p in OUT_DIR.glob("*.md")))


if __name__ == "__main__":
    main()
