#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Dry-run:对每个文件 print 修改前后对照(只对含「本需求 REQ-」的文件)。"""
import re
import sys
import io
from pathlib import Path

# 强制 UTF-8 输出
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

REPO_ROOT = Path(r"D:/Workspaces/wm/code-skills")
SKILLS_DIR = REPO_ROOT / "plugins" / "code-skills" / "skills"

SKILL_NAMES = [
    "code-answer", "code-auto", "code-check", "code-dashboard",
    "code-design", "code-fix", "code-init", "code-it", "code-merge",
    "code-plan", "code-publish", "code-require", "code-rule", "code-version",
]

TARGET_FILES = []
for name in SKILL_NAMES:
    skill_md = SKILLS_DIR / name / "SKILL.md"
    if skill_md.exists():
        TARGET_FILES.append(skill_md)
    templates_dir = SKILLS_DIR / name / "templates"
    if templates_dir.exists():
        for f in sorted(templates_dir.glob("*.md")):
            TARGET_FILES.append(f)

ANCHOR_RE = re.compile(r'本需求\s+(?:REQ|BUG)-\d{5}')
FIND = re.compile(r'本需求\s+(?:REQ|BUG)-\d{5}[^\n]*')

TAIL_CHARS = set('。;；:：、,)，)】］]→\\`"\'([{<>*#!')


def is_cjk(ch: str) -> bool:
    if not ch:
        return False
    cp = ord(ch)
    return 0x4E00 <= cp <= 0x9FFF or 0x3400 <= cp <= 0x4DBF


def truncate_after_anchor(literal: str) -> int:
    m = ANCHOR_RE.match(literal)
    if not m:
        return 0
    pos = m.end()
    if pos < len(literal) and literal[pos] == ' ':
        pos += 1
    start = pos
    max_len = 30
    while pos < len(literal) and (pos - start) < max_len:
        ch = literal[pos]
        if ch == '\n':
            break
        if ch in TAIL_CHARS:
            break
        if is_cjk(ch):
            break
        pos += 1
    if pos == start:
        return start
    return pos


# 对每个含 R-1 字面的文件,print 主体+截断后内容
for path in TARGET_FILES:
    content = path.read_text(encoding="utf-8")
    if not FIND.search(content):
        continue
    rel = path.relative_to(REPO_ROOT)
    print(f"\n=== {rel} ===")
    for m in FIND.finditer(content):
        literal = m.group(0)
        # 找主体结束
        m_anchor = ANCHOR_RE.match(literal)
        if not m_anchor:
            continue
        end = truncate_after_anchor(literal)
        if end == 0:
            end = m_anchor.end()
        truncated = literal[:end]
        # print 整字面 + 删除的尾部
        tail = literal[end:end + 20] if end < len(literal) else "(行尾)"
        print(f"  [删]: {truncated!r}")
        if tail and tail != "(行尾)":
            print(f"  [剩]: {tail!r}")
