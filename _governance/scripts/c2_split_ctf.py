#!/usr/bin/env python3
"""c2_split_ctf.py — C2 治理：拆分 CTF/Crypto/CTF.md（84 个 H2 词条速查表）。

产出：
- CTF/Crypto/古典密码速查.md   （替换/棋盘/置换类古典密码）
- CTF/Crypto/趣味编码速查.md   （程序语言混淆 + 中文/符号趣味编码）
- _governance/tmp/{rsa-crack,base64CaseCrack,steg-base32,steg-base64}.md
  （分流词条片段，供后续并入 RSA与数论.md / 编码速查.md / 图像隐写.md）

规则：
- 按标题边界切分，跳过代码围栏内的 `#`。
- 空 `## ` 标题（9 个）删除；`[vowel]()` 空链接标题清理为 `vowel`。
- 拼写修正：caeser→caesar、virgenene→vigenere（条目内注一句留痕）。
- 裸 ``` 代码围栏补 `text` 语言标注。
- 原文件不动，由 git mv 归档（本脚本只读它）。
"""
import re
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
SRC = VAULT / "CTF/Crypto/CTF.md"
TMP = VAULT / "_governance/tmp"
TMP.mkdir(parents=True, exist_ok=True)

# ---------- 分类表（key = 去掉标题链接后的词条名，小写） ----------
CLASSICAL_SUBST = [  # 替换密码
    "a1z26", "asciiSum", "atbash", "affine", "bacon24", "bacon26", "caeser",
    "caeser box", "qwe", "rot5", "rot13", "rot18", "rot47", "rot8000",
    "gronsfeld", "virgenene", "autoKey", "beaufort", "porta", "oneTimePad",
    "FenHam费娜姆密码", "hill", "playFair", "bifid", "FracMorse", "vowel",
]
CLASSICAL_BOARD = [  # 棋盘/坐标
    "ADFGVX", "ADFGX", "baudot", "morse", "polybius", "nihilist", "fourSquare",
    "trifid", "TapCode", "braille", "handyCode",
]
CLASSICAL_TRANS = ["curveCipher", "railFence", "railFenceW"]  # 置换/换位
FUN_LANG = ["aaencode", "jjencode", "brain fuck", "Ook", "troll script", "rabbit"]
FUN_CN = [
    "与佛论禅", "与佛论禅加密版", "新佛曰", "熊曰", "兽音", "阴阳怪气", "六十四卦",
    "天干地支", "百家姓", "01248", "pawnShop", "periodicTable", "socialCoreValue",
    "cetacean", "zwBinary", "zwBinary-morse", "zwUnicode",
]
FUN_OTHER = ["DNA", "emojiSubstitute", "grayCode", "Twin Hex", "bubbleBabble",
             "Manchester", "Manchester-diff"]
ROUTED = {  # 分流词条 → 片段文件名
    "RSA-crack": "rsa-crack",
    "base64CaseCrack": "base64CaseCrack",
    "steg base32": "steg-base32",
    "steg base64": "steg-base64",
}

LINK_RE = re.compile(r"^\[([^\]]*)\]\([^)]*\)$")


def entry_key(title: str) -> str:
    """`[ADFGVX](url)` → `ADFGVX`；`zwBinary(zeroWidthBinary)` → `zwBinary`。"""
    m = LINK_RE.match(title)
    if m:
        return m.group(1)
    return re.sub(r"\(.*\)$", "", title)


def fix_title(title: str) -> str:
    """拼写修正 + 清理空链接标题。"""
    if title == "[vowel]()":
        return "vowel"
    title = title.replace("caeser", "caesar").replace("virgenene", "vigenere")
    return title


def fix_body(body: str, key: str) -> str:
    """裸围栏补 text；拼写修正留痕注释。"""
    lines = body.split("\n")
    out, in_fence = [], False
    for ln in lines:
        if ln.strip() == "```":
            # 翻转前 in_fence=False 说明这是开栏 → 补 text；关栏保持 ```
            is_open = not in_fence
            in_fence = not in_fence
            out.append("```text" if (ln == "```" and is_open) else ln)
            continue
        if not in_fence:
            ln = ln.replace("caeser", "caesar").replace("virgenene", "vigenere")
        out.append(ln)
    body = "\n".join(out)
    if key in ("caeser",):
        body += "\n> 注：原稿拼写为 `caeser`，治理时统一修正为 `caesar`。\n"
    if key in ("virgenene",):
        body += "\n> 注：原稿拼写为 `virgenene`，治理时统一修正为 `vigenere`。\n"
    return body


# ---------- 解析 ----------
text = SRC.read_text(encoding="utf-8")
sections = []  # (title, body)
cur_title, cur_body = None, []
in_fence = False
for line in text.split("\n"):
    if line.lstrip().startswith("```"):
        in_fence = not in_fence
        if cur_title is not None:
            cur_body.append(line)
        continue
    if not in_fence and line.startswith("## "):
        if cur_title is not None:
            sections.append((cur_title, "\n".join(cur_body).strip("\n")))
        cur_title, cur_body = line[3:].strip(), []
        continue
    if cur_title is not None:
        cur_body.append(line)
if cur_title is not None:
    sections.append((cur_title, "\n".join(cur_body).strip("\n")))

# 去掉首个 H1 之前的引导（源文件首行 "CTF"），sections 只含 H2 起
entries = []
dropped_empty = []
ref_section = None
for title, body in sections:
    if not title:
        dropped_empty.append(True)
        continue
    if title == "参考":
        ref_section = body
        continue
    entries.append((title, body))

# ---------- 分组 ----------
groups = {"subst": [], "board": [], "trans": [], "funlang": [], "funcn": [],
          "funother": [], "routed": []}
seen = set()
for title, body in entries:
    key = entry_key(title)
    if key in seen:
        raise SystemExit(f"duplicate key: {key}")
    seen.add(key)
    if key in ROUTED:
        groups["routed"].append((key, title, body))
    elif key in CLASSICAL_SUBST:
        groups["subst"].append((key, title, body))
    elif key in CLASSICAL_BOARD:
        groups["board"].append((key, title, body))
    elif key in CLASSICAL_TRANS:
        groups["trans"].append((key, title, body))
    elif key in FUN_LANG:
        groups["funlang"].append((key, title, body))
    elif key in FUN_CN:
        groups["funcn"].append((key, title, body))
    elif key in FUN_OTHER:
        groups["funother"].append((key, title, body))
    else:
        raise SystemExit(f"UNCLASSIFIED: {key!r}")

all_classified = (CLASSICAL_SUBST + CLASSICAL_BOARD + CLASSICAL_TRANS +
                  FUN_LANG + FUN_CN + FUN_OTHER + list(ROUTED))
missing = [k for k in all_classified if k not in seen]
if missing:
    raise SystemExit(f"declared but not found in source: {missing}")


def render(entries_) -> str:
    parts = []
    for key, title, body in entries_:
        parts.append(f"### {fix_title(title)}\n")
        b = fix_body(body, key).strip("\n")
        parts.append(b)
    return "\n\n".join(parts) + "\n"


# ---------- 古典密码速查 ----------
gudian = []
gudian.append("# 古典密码速查\n")
gudian.append(
    "> 由原 `CTF/Crypto/CTF.md`（84 词条速查表，原稿归档于 `_archive/CTF/CTF速查-原稿.md`）"
    "拆分而来。替换/棋盘/置换类古典密码在本页；趣味编码见 [趣味编码速查](趣味编码速查.md)，"
    "Base/进制/字符编码见 [编码速查](编码速查.md)。\n"
    "> 拼写修正留痕：`caeser`→`caesar`、`virgenene`→`vigenere`（详见各条目内注）。\n"
)
gudian.append("## 替换密码\n\n" + render(groups["subst"]))
gudian.append("## 棋盘与坐标密码\n\n" + render(groups["board"]))
gudian.append("## 置换密码（换位）\n\n" + render(groups["trans"]))
if ref_section:
    gudian.append("## 参考\n\n" + ref_section.strip("\n") + "\n")
(VAULT / "CTF/Crypto/古典密码速查.md").write_text(
    "\n".join(gudian), encoding="utf-8", newline="\n")

# ---------- 趣味编码速查 ----------
quwei = []
quwei.append("# 趣味编码速查\n")
quwei.append(
    "> 由原 `CTF/Crypto/CTF.md`（84 词条速查表，原稿归档于 `_archive/CTF/CTF速查-原稿.md`）"
    "拆分而来。程序语言混淆与中文/符号趣味编码在本页；古典密码见 "
    "[古典密码速查](古典密码速查.md)，编码类见 [编码速查](编码速查.md)。\n"
)
quwei.append("## 程序语言混淆\n\n" + render(groups["funlang"]))
quwei.append("## 中文趣味编码\n\n" + render(groups["funcn"]))
quwei.append("## 其他符号与通信编码\n\n" + render(groups["funother"]))
(VAULT / "CTF/Crypto/趣味编码速查.md").write_text(
    "\n".join(quwei), encoding="utf-8", newline="\n")

# ---------- 分流片段 ----------
for key, title, body in groups["routed"]:
    frag = f"### {fix_title(title)}\n\n{fix_body(body, key).strip('\n')}\n"
    (TMP / f"{ROUTED[key]}.md").write_text(frag, encoding="utf-8", newline="\n")

print(f"entries: {len(entries)} real + {len(dropped_empty)} empty dropped")
print("subst=%d board=%d trans=%d funlang=%d funcn=%d funother=%d routed=%d" % (
    len(groups["subst"]), len(groups["board"]), len(groups["trans"]),
    len(groups["funlang"]), len(groups["funcn"]), len(groups["funother"]),
    len(groups["routed"])))
