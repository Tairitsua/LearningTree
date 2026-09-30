#!/usr/bin/env python3
"""c3_verify_split.py — 阶段C3 门禁：核对原稿各章节标题均能在拆分产物中找到。

对每个拆分：提取原稿全部标题（跳过代码围栏），与目标目录全部产物文件的
标题集合+正文比对（归一化：去反引号/空白/层级号），报告缺失项。
"""
import re
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
FENCE_RE = re.compile(r"^\s*(```|~~~)")


def headings(path):
    out = []
    in_fence = False
    for line in Path(path).read_text(encoding="utf-8").split("\n"):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = re.match(r"^(#{1,6})\s+(.*?)\s*$", line)
        if m:
            out.append(m.group(2))
    return out


def norm(s):
    s = s.replace("`", "").replace("（", "(").replace("）", ")")
    s = re.sub(r"^\d+[\.、]\s*", "", s)  # 序号差异
    return re.sub(r"\s+", "", s).lower()


CHECKS = [
    (
        "_archive/ComputerScience/Linux-原稿.md",
        ["ComputerScience/Linux"],
        {
            "命令": "# Linux 命令速查(文件H1,原H1)",
            "Vim": "# Vim(文件H1,原H2)",
            "快捷键": "## 快捷键",
            "运行级别runlevel": "## 运行级别runlevel",
            "Shell": "# Shell(文件H1,原H1)",
            "Shell脚本": "## Shell脚本",
            "目录结构": "## 目录结构",
            "种类": "## 种类",
            "文件权限": "## 文件权限",
            "用户": "## 用户",
            "组": "## 组",
            "进程": "## 进程",
            "硬盘管理": "## 硬盘管理",
            "SSH": "# SSH(文件H1,原H1)",
            "网络设置": "# 网络配置(文件H1,原H1)",
            "WSL": "仅含跳转链接→SoftwareManual/WSL.md,无需覆盖",
        },
    ),
    (
        "_archive/ComputerScience/Database-原稿.md",
        ["ComputerScience/Database"],
        {
            "数据库": "# 数据库(文件H1,原H1)",
            "SQL Server": "# SQL Server(文件H1,原H1)",
            "MySQL": "# MySQL(文件H1,原H1)",
            "DBF": "## DBF(并入数据库基础.md末尾)",
        },
    ),
    (
        "_archive/ComputerScience/BigData-原稿.md",
        ["ComputerScience/BigData"],
        {
            "大数据": "# 大数据与 Hadoop 生态(文件H1,原H1)",
            "概念": "## 概念",
            "`Hadoop`框架": "## Hadoop框架",
            "云数据中心": "# 云数据中心(文件H1,原H2)",
        },
    ),
]

ok = True
# 有意改名的标题（任务书指定文件名/标题），视为已覆盖
RETITLED = {"网络设置": "网络配置（有意改名，对应文件 07-网络配置.md）"}
for src, dirs, h12 in CHECKS:
    orig = headings(src)
    prod = []
    for d in dirs:
        for p in sorted((VAULT / d).rglob("*.md")):
            prod += headings(p)
            prod.append(p.read_text(encoding="utf-8"))  # 正文兜底
    prod_norm = {norm(h) for h in prod if isinstance(h, str)}
    prod_text = "\n".join(x for x in prod if isinstance(x, str))
    print(f"== {src} ==")
    missing = []
    for h in orig:
        n = norm(h)
        if n in prod_norm or n in re.sub(r"`", "", prod_text).replace(" ", "").lower() or n in prod_text.replace("`", "").replace(" ", "").lower():
            continue
        missing.append(h)
    # 逐个 H1/H2 对照去向说明
    for h, dest in h12.items():
        covered = norm(h) not in [norm(m) for m in missing] or "WSL" in dest or h in RETITLED
        print(f"  [{'OK' if covered else 'MISS'}] {h} -> {dest}" + (f" [{RETITLED[h]}]" if h in RETITLED else ""))
    if missing:
        for m in missing:
            if m in RETITLED:
                continue
        real_missing = [m for m in missing if m not in RETITLED]
        if real_missing:
            ok = False
            for m in real_missing:
                print(f"  !! MISSING: {m}")
    print()

print("RESULT:", "ALL HEADINGS COVERED" if ok else "SOME HEADINGS MISSING")
