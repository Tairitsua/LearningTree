# -*- coding: utf-8 -*-
"""C4 残留治理 lint：唯一 H1 / 无跳级 / 围栏闭合 / 围栏语言"""
import io, os, re, sys

ROOTS = [
    r"D:\Code\LearningTree\CloudNative",
    r"D:\Code\LearningTree\Programming",
    r"D:\Code\LearningTree\SoftwareManual",
    r"D:\Code\LearningTree\Frontend",
    r"D:\Code\LearningTree\English",
]

HEADING_RE = re.compile(r'^(#{1,6})\s+(.*)$')
FENCE_RE = re.compile(r'^\s*(```+|~~~+)')

def lint(path):
    issues = []
    try:
        with io.open(path, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
    except UnicodeDecodeError:
        with io.open(path, 'r', encoding='utf-8', errors='replace') as f:
            lines = f.read().splitlines()

    h1_count = 0
    h1_first = None
    prev_level = None
    in_fence = False
    fence_marker = ''
    fence_start = 0
    fence_no_lang = []
    fence_unclosed = []

    for i, line in enumerate(lines, 1):
        if not in_fence:
            m = FENCE_RE.match(line)
            if m:
                in_fence = True
                fence_marker = m.group(1)[:3]
                fence_start = i
                rest = line.strip()[3:].strip()
                if not rest:
                    fence_no_lang.append(i)
                continue
            hm = HEADING_RE.match(line)
            if hm:
                level = len(hm.group(1))
                text = hm.group(2).strip()
                if level == 1:
                    h1_count += 1
                    if h1_first is None:
                        h1_first = (i, text)
                if prev_level is not None and level > prev_level + 1:
                    issues.append("L%d: 跳级 H%d->H%d (%s)" % (i, prev_level, level, text[:30]))
                prev_level = level
        else:
            m = FENCE_RE.match(line)
            if m and m.group(1)[:3] == fence_marker:
                in_fence = False
    if in_fence:
        fence_unclosed.append(fence_start)

    base = os.path.basename(path)
    if h1_count == 0:
        issues.append("无 H1")
    elif h1_count > 1:
        issues.append("H1 x%d (首个 L%d: %s)" % (h1_count, h1_first[0], h1_first[1][:30]))
    else:
        # H1 与文件名一致性
        stem = os.path.splitext(base)[0]
        if h1_first and h1_first[1].strip() != stem:
            issues.append("H1(%r) != 文件名(%r)" % (h1_first[1][:40], stem))
    for ln in fence_no_lang:
        issues.append("L%d: 围栏无语言" % ln)
    for ln in fence_unclosed:
        issues.append("L%d: 围栏未闭合" % ln)
    return issues

def main():
    total = 0
    fail = 0
    for root in ROOTS:
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in ('.obsidian',)]
            for fn in sorted(filenames):
                if not fn.endswith('.md'):
                    continue
                p = os.path.join(dirpath, fn)
                total += 1
                issues = lint(p)
                rel = os.path.relpath(p, r"D:\Code\LearningTree")
                if issues:
                    fail += 1
                    print("FAIL %s" % rel)
                    for it in issues:
                        print("     - %s" % it)
                else:
                    print("PASS %s" % rel)
    print("\n=== %d files, %d FAIL, %d PASS ===" % (total, fail, total - fail))

if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
