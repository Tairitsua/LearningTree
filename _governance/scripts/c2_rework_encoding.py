#!/usr/bin/env python3
"""c2_rework_encoding.py — C2 治理：CTF/Crypto/Encoding.md → 编码速查.md 结构重排。

- 唯一 H1（原 4 个 H1：Base家族/进制表示/其他/字符编码 → H2 分组）。
- 词条 H2→H3，字符集教程小节顺延降级（H3→H4、H4→H5）。
- 裸 ``` 围栏补 text。
- 头部加来源说明。
"""
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
F = VAULT / "CTF/Crypto/编码速查.md"

lines = F.read_text(encoding="utf-8").split("\n")
out = []
in_fence = False
seen_h1 = False
for ln in lines:
    if ln.lstrip().startswith("```"):
        # 翻转前 in_fence=False 说明这是开栏 → 补 text；关栏保持 ```
        is_open = not in_fence
        in_fence = not in_fence
        out.append("```text" if (ln == "```" and is_open) else ln)
        continue
    if not in_fence and ln.startswith("#"):
        level = len(ln) - len(ln.lstrip("#"))
        rest = ln.lstrip("#")[1:] if len(ln) > level else ""
        if level == 1 and not seen_h1:
            seen_h1 = True
            out.append("# 编码速查")
            out.append("")
            out.append(
                "> 原名 `Encoding.md`，2026-09 治理改名并重排标题结构；"
                "`base64CaseCrack` 词条（原 `CTF.md`）与 Base64 介绍（原 `Misc/编码类.md`）已并入。")
            out.append("")
            out.append("## Base家族")
            continue
        new_level = level + 1
        out.append("#" * new_level + " " + rest.strip() if rest.strip() else "#" * new_level)
        continue
    out.append(ln)

# 去掉开头多余空行
while out and out[0] == "":
    out.pop(0)
text = "\n".join(out)
# 压缩 3 连以上空行为 2
import re
text = re.sub(r"\n{4,}", "\n\n\n", text)
F.write_text(text, encoding="utf-8", newline="\n")
print("done")
