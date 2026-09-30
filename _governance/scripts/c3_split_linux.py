#!/usr/bin/env python3
"""c3_split_linux.py — 阶段C3：将 ComputerScience/Linux.md 巨石按 H1/H2 机械拆分。

- 按标题边界切分（跳过代码围栏内的 # 行）。
- 逐片做最小格式修复（标题降级、去重行、裸链接、空表格行、孤立字符）。
- 产物写入 ComputerScience/Linux/；原稿由 git mv 归档（脚本外执行）。
- 附带把 Koubot/Linux命令.md 的条目并入 01-命令速查.md 的"命令补遗"节。
"""
import re
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
SRC = VAULT / "ComputerScience" / "Linux.md"
OUT_DIR = VAULT / "ComputerScience" / "Linux"
KOUBOT = VAULT / "Koubot" / "Linux命令.md"

FENCE_RE = re.compile(r"^\s*(```|~~~)")
HEAD_RE = re.compile(r"^(#{1,6}) (.*)")
EMPTY_ROW_RE = re.compile(r"^\|(\s*\|)+\s*$")


def split_sections(lines):
    in_fence = False
    bounds = []
    for i, line in enumerate(lines):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEAD_RE.match(line)
        if m and m.group(1) in ("#", "##"):
            bounds.append(i)
    secs = {}
    for k, start in enumerate(bounds):
        end = bounds[k + 1] if k + 1 < len(bounds) else len(lines)
        m = HEAD_RE.match(lines[start])
        secs[m.group(2).strip()] = lines[start + 1 : end]
    return secs


def clean(body):
    """去首尾空行 + 清理纯空表格行。"""
    body = [l for l in body if not EMPTY_ROW_RE.match(l.strip())]
    while body and not body[0].strip():
        body.pop(0)
    while body and not body[-1].strip():
        body.pop()
    return body


def drop_line(body, predicate, note):
    kept = []
    dropped = 0
    for l in body:
        if predicate(l):
            dropped += 1
            continue
        kept.append(l)
    if dropped:
        print(f"  fix: {note} (x{dropped})")
    return kept


def main():
    lines = SRC.read_text(encoding="utf-8").split("\n")
    secs = split_sections(lines)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    def take(*names):
        out = []
        for n in names:
            out.append("## " + n)
            out.append("")
            out.extend(clean(secs[n]))
            out.append("")
        return out

    # ---------- 01 命令速查 ----------
    body = clean(secs["命令"])
    # 修复盘点：wc 命令重复两行，删去第二行（无全称、描述更弱的那行）
    body = drop_line(
        body,
        lambda l: l.startswith("| wc ") and "word count" not in l,
        "删除重复的 wc 行（保留含 word count 全称的首行）",
    )
    # 表格内裸 URL 改链接
    n_url = 0
    def fix_row_url(l):
        nonlocal n_url
        if "<https://" in l:
            new = l.replace(
                "<https://www.jianshu.com/p/676353506f0b>",
                "[xargs 用法参考 - 简书](https://www.jianshu.com/p/676353506f0b)",
            ).replace(
                "<https://zhuanlan.zhihu.com/p/74812069>",
                "[tcpdump 抓包用法参考 - 知乎](https://zhuanlan.zhihu.com/p/74812069)",
            )
            if new != l:
                n_url += 1
            return new
        return l
    body = [fix_row_url(l) for l in body]
    print(f"  fix: 表格内裸 URL 转链接 x{n_url}")

    kb = ["## 命令补遗", ""]
    if KOUBOT.exists():
        kb += [
            "> 以下条目并入自 `Koubot/Linux命令.md`（2026-09 阶段C3 治理；原文空的「介绍」「备注」占位节已清理）。",
            "",
            "### 查看当前操作系统信息",
            "",
            "```shell",
            "cat /etc/os-release",
            "```",
            "",
            "### 查看历史命令",
            "",
            "`fc -l`",
            "",
            "The command \"fc -l\" is a command used in the command line interface of a computer. \"fc\" stands for \"fix command\" and is used to edit and re-execute previously entered commands. The \"-l\" option is used to list the last executed commands. Therefore, \"fc -l\" will display a list of the most recent commands that have been executed in the command line interface.",
            "",
            "### 学习资源",
            "",
            "- [GitHub - jlevy/the-art-of-command-line: Master the command line, in one page](https://github.com/jlevy/the-art-of-command-line)",
            "",
        ]
    body += ["", "## 快捷键", ""]
    # 修复盘点：L246 孤立字符 "f"
    sk = clean(secs["快捷键"])
    sk = drop_line(sk, lambda l: l.strip() == "f", "删除孤立字符行 'f'")
    body += sk + ["", "## 运行级别runlevel", ""] + clean(secs["运行级别runlevel"])
    if KOUBOT.exists():
        body += [""] + kb
    (OUT_DIR / "01-命令速查.md").write_text(
        "# Linux 命令速查\n\n" + "\n".join(body).rstrip() + "\n", encoding="utf-8", newline="\n"
    )

    # ---------- 02 Vim ----------
    (OUT_DIR / "02-Vim.md").write_text(
        "# Vim\n\n" + "\n".join(clean(secs["Vim"])).rstrip() + "\n", encoding="utf-8", newline="\n"
    )

    # ---------- 03 Shell ----------
    body = clean(secs["Shell"])  # # Shell 章首简介（保留为文件引言）
    body += ["", "## Shell脚本", ""]
    script = clean(secs["Shell脚本"])
    # 标题跳级修复：#### 变量 -> ### 变量
    script = [
        l.replace("#### 变量", "### 变量", 1) if l.startswith("#### 变量") else l for l in script
    ]
    body += script + ["", "## 目录结构", ""] + clean(secs["目录结构"])
    body += ["", "## 种类", ""] + clean(secs["种类"])
    (OUT_DIR / "03-Shell脚本.md").write_text(
        "# Shell\n\n" + "\n".join(body).rstrip() + "\n", encoding="utf-8", newline="\n"
    )

    # ---------- 04 用户与权限 ----------
    body = ["## 文件权限", ""]
    perm = clean(secs["文件权限"])
    perm = [l.replace("#### 特殊权限", "### 特殊权限", 1) if l.startswith("#### 特殊权限") else l for l in perm]
    body += perm + ["", "## 用户", ""] + clean(secs["用户"])
    body += ["", "## 组", ""] + clean(secs["组"])
    (OUT_DIR / "04-用户与权限.md").write_text(
        "# 用户与权限\n\n" + "\n".join(body).rstrip() + "\n", encoding="utf-8", newline="\n"
    )

    # ---------- 05 进程与磁盘 ----------
    body = ["## 进程", ""] + clean(secs["进程"])
    body += ["", "## 硬盘管理", ""] + clean(secs["硬盘管理"])
    (OUT_DIR / "05-进程与磁盘.md").write_text(
        "# 进程与磁盘\n\n" + "\n".join(body).rstrip() + "\n", encoding="utf-8", newline="\n"
    )

    # ---------- 06 SSH ----------
    ssh = clean(secs["SSH"])
    ssh = [
        l.replace(
            "<https://www.cnblogs.com/276815076/p/10449354.html>",
            "[SSH 连接失败排查参考 - 博客园](https://www.cnblogs.com/276815076/p/10449354.html)",
        )
        for l in ssh
    ]
    ssh = [l.replace("1、权限问题", "1. 权限问题", 1) if l.strip() == "1、权限问题" else l for l in ssh]
    ssh = [l.replace("2、StrictModes问题", "2. StrictModes 问题", 1) if l.strip() == "2、StrictModes问题" else l for l in ssh]
    (OUT_DIR / "06-SSH.md").write_text(
        "# SSH\n\n" + "\n".join(ssh).rstrip() + "\n", encoding="utf-8", newline="\n"
    )

    # ---------- 07 网络配置 ----------
    net = clean(secs["网络设置"])
    net = [
        l.replace("##### 出现莫名奇妙无法连接其他子节点时", "## 出现莫名奇妙无法连接其他子节点时", 1)
        if l.startswith("##### 出现莫名奇妙")
        else l
        for l in net
    ]
    net = [l.replace("1.关闭SELinux，但是这样会不太安全，不是很推荐", "1. 关闭 SELinux，但是这样会不太安全，不是很推荐", 1) if l.startswith("1.关闭SELinux") else l for l in net]
    net = [l.replace("2.开放通讯端口(推荐)", "2. 开放通讯端口（推荐）", 1) if l.startswith("2.开放通讯端口") else l for l in net]
    (OUT_DIR / "07-网络配置.md").write_text(
        "# 网络配置\n\n" + "\n".join(net).rstrip() + "\n", encoding="utf-8", newline="\n"
    )

    print("written:", sorted(p.name for p in OUT_DIR.glob("*.md")))


if __name__ == "__main__":
    main()
