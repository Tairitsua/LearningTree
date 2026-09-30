#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lint the CTF domain markdown files for format governance.

Checks (gate criteria):
  1. Exactly one H1 (0 or >1 is an error; H1 != filename stem is only a note).
  2. No heading level skips (H2 -> H4 directly etc.).
  3. All fenced code blocks closed.
  4. All fenced code blocks carry a language tag (text counts).
  5. No '*'-prefixed headings like the CIRCLED PLUS heading marker.
  6. No bare autolinks <https://...> or plain-text URLs outside code fences.

Outputs a PASS/FAIL list per file, plus a detail section for failures.
"""
import io
import os
import re
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
CTF_DIR = os.path.join(ROOT, "CTF")

H_RE = re.compile(r"^(#{1,6})\s+(.*)$")
AUTOLINK_RE = re.compile(r"<https?://[^>]+>")

def lint_file(path):
    rel = os.path.relpath(path, ROOT).replace("\\", "/")
    errors = []
    notes = []
    with io.open(path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    h1_count = 0
    prev_level = 0  # 0 = document start / H1 zone
    in_fence = False
    fence_lines = []
    fence_start = 0
    fences = []
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if in_fence:
            if stripped.startswith("```"):
                in_fence = False
                fences.append((fence_start, i, fence_lines))
            else:
                fence_lines.append(line)
            continue
        if stripped.startswith("```"):
            in_fence = True
            fence_start = i
            fence_lines = []
            continue
        m = H_RE.match(stripped)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            if level == 1:
                h1_count += 1
                if h1_count > 1:
                    errors.append("L%d: multiple H1 (this is #%d): '%s'" % (i, h1_count, title[:30]))
                elif title != os.path.splitext(os.path.basename(path))[0]:
                    notes.append("H1 '%s' != filename stem (accepted)" % title)
            if level - prev_level > 1:
                errors.append("L%d: heading skip H%d->H%d at '%s'" % (i, prev_level, level, title[:30]))
            prev_level = level
            if title.startswith("※"):
                errors.append("L%d: star-prefixed heading '%s'" % (i, title[:30]))
    if in_fence:
        errors.append("L%d: unclosed code fence" % fence_start)

    for (start, end, body) in fences:
        first = lines[start - 1].strip()
        lang = first[3:].strip()
        if not lang:
            errors.append("L%d: code fence without language" % start)

    # Bare autolinks / plain-text URLs outside fences
    fence_spans = [(s - 1, e) for (s, e, _) in fences]
    def in_any_fence(idx):
        return any(a <= idx < b for (a, b) in fence_spans)
    for i, line in enumerate(lines):
        if in_any_fence(i):
            continue
        for m in AUTOLINK_RE.finditer(line):
            prefix = line[: m.start()]
            if prefix.count("`") % 2 == 1:
                continue
            errors.append("L%d: bare autolink %s" % (i + 1, m.group(0)[:40]))
        for m in re.finditer(r"https?://[^\s)\]>]+", line):
            seg = line[m.start(): m.end()]
            before = line[: m.start()]
            if before.endswith("](") or before.endswith("<") or before.endswith("="):
                continue
            if AUTOLINK_RE.search(line[m.start():]):
                continue
            if before.count("`") % 2 == 1:
                continue
            errors.append("L%d: plain-text URL %s" % (i + 1, seg[:40]))

    if h1_count == 0:
        errors.append("no H1 found")

    return rel, errors, notes

def main():
    results = []
    for dirpath, dirnames, filenames in os.walk(CTF_DIR):
        dirnames[:] = [d for d in dirnames if d not in (".git", "attachments")]
        for name in sorted(filenames):
            if name.endswith(".md"):
                results.append(lint_file(os.path.join(dirpath, name)))
    results.sort()
    fail = 0
    for rel, errors, notes in results:
        if errors:
            fail += 1
            print("FAIL %s" % rel)
            for e in errors:
                print("     - %s" % e)
        else:
            print("PASS %s" % rel)
            for n in notes:
                print("     note: %s" % n)
    print("")
    print("TOTAL %d files, %d FAIL, %d PASS" % (len(results), fail, len(results) - fail))
    return 1 if fail else 0

if __name__ == "__main__":
    sys.exit(main())
