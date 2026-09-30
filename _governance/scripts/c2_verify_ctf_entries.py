#!/usr/bin/env python3
"""c2_verify_ctf_entries.py — 验收门禁 2：CTF.md 84 个 H2 词条在拆分产物中的完整性。

从 _archive/CTF/CTF速查-原稿.md 读取全部 H2（含空标题），逐条在预期产物文件中
查找对应标题（`### 词条名`），报告：总数/实际词条数/空标题数/命中数/未命中清单。
"""
import re
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
SRC = VAULT / "_archive/CTF/CTF速查-原稿.md"
LINK_RE = re.compile(r"^\[([^\]]*)\]\([^)]*\)$")

TARGETS = {
    "古典": VAULT / "CTF/Crypto/古典密码速查.md",
    "趣味": VAULT / "CTF/Crypto/趣味编码速查.md",
    "RSA与数论": VAULT / "CTF/Crypto/RSA与数论.md",
    "编码速查": VAULT / "CTF/Crypto/编码速查.md",
    "图像隐写": VAULT / "CTF/Misc/图像隐写/图像隐写.md",
}
CACHE = {k: v.read_text(encoding="utf-8") for k, v in TARGETS.items()}

# 词条 key（去链接、去括号后缀）→ 预期产物
KEY_TO_TARGET = {}
for k in [
    "a1z26", "asciiSum", "atbash", "affine", "bacon24", "bacon26", "caeser", "caeser box",
    "qwe", "rot5", "rot13", "rot18", "rot47", "rot8000", "gronsfeld", "virgenene",
    "autoKey", "beaufort", "porta", "oneTimePad", "FenHam费娜姆密码", "hill", "playFair",
    "bifid", "FracMorse", "vowel", "ADFGVX", "ADFGX", "baudot", "morse", "polybius",
    "nihilist", "fourSquare", "trifid", "TapCode", "braille", "handyCode", "curveCipher",
    "railFence", "railFenceW", "参考",
]:
    KEY_TO_TARGET[k] = "古典"
for k in [
    "aaencode", "jjencode", "brain fuck", "Ook", "troll script", "rabbit",
    "与佛论禅", "与佛论禅加密版", "新佛曰", "熊曰", "兽音", "阴阳怪气", "六十四卦", "天干地支",
    "百家姓", "01248", "pawnShop", "periodicTable", "socialCoreValue", "cetacean",
    "zwBinary", "zwBinary-morse", "zwUnicode", "DNA", "emojiSubstitute", "grayCode",
    "Twin Hex", "bubbleBabble", "Manchester", "Manchester-diff",
]:
    KEY_TO_TARGET[k] = "趣味"
KEY_TO_TARGET.update({
    "RSA-crack": "RSA与数论",
    "base64CaseCrack": "编码速查",
    "steg base32": "图像隐写",
    "steg base64": "图像隐写",
})

SPELLFIX = {"caeser": "caesar", "virgenene": "vigenere"}


def norm_title(title: str) -> str:
    m = LINK_RE.match(title)
    if m:
        title = m.group(1)
    title = re.sub(r"\(.*\)$", "", title).strip()
    for bad, good in SPELLFIX.items():
        title = title.replace(bad, good)
    return title


def entry_key(title: str) -> str:
    return re.sub(r"\(.*\)$", "", LINK_RE.match(title).group(1) if LINK_RE.match(title) else title).strip()


# 解析归档原稿 H2（跳过围栏与引用块）
h2 = []
in_fence = False
for line in SRC.read_text(encoding="utf-8").split("\n"):
    if line.lstrip().startswith("```"):
        in_fence = not in_fence
        continue
    if not in_fence and line.startswith("## "):
        h2.append(line[3:].strip())

empty = [t for t in h2 if not t]
real = [t for t in h2 if t]
misses = []
hits = 0
for t in real:
    key = entry_key(t)
    target = KEY_TO_TARGET.get(key)
    if target is None:
        misses.append((t, "NO-TARGET-MAPPING"))
        continue
    want = norm_title(t)
    # 在产物中找标题行（任意级别）或原 key 文本
    pat = re.compile(r"^#{2,5}.*" + re.escape(want.split("(")[0].strip()) + r".*$", re.M | re.I)
    if pat.search(CACHE[target]):
        hits += 1
    else:
        misses.append((t, target))

print(f"原稿 H2 总数: {len(h2)}（实际词条+参考: {len(real)}，空标题: {len(empty)}）")
print(f"产物命中: {hits}/{len(real)}")
if misses:
    print("未命中清单:")
    for t, why in misses:
        print(f"  {t!r} -> {why}")
    sys.exit(1)
print("all entries present")
