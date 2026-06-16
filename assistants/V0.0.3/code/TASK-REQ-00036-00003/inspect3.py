#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""更激进的 R-1:匹配「本需求 REQ-NNNNN」+ 后续 0-25 字符 + 收尾于非汉字。"""
import re
import json
from pathlib import Path

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

# v3 R-1:激进匹配「本需求 REQ-NNNNN」+ 后续 0-25 字符(非汉字 / 非段尾)
# 后续字符含:数字/字母/`/`/空格/-/点/括号/特殊符号,但不进入中文段尾
R1_PATTERN_V3 = re.compile(
    r'本需求\s+(?:REQ|BUG)-\d{5}'           # 主体
    r'(?:[^\n。一-鿿]{0,30})?'     # 0-30 字符(非句号/非中文段尾),非贪婪
    r'(?=[\n。一-鿿]|$)'            # 收尾:段尾/中文/行尾
)

# v4 R-1:更激进,任意非换行非汉字字符 0-25 字符
R1_PATTERN_V4 = re.compile(
    r'本需求\s+(?:REQ|BUG)-\d{5}'
    r'(?:[^\n一-鿿]{0,25})?'       # 0-25 字符(非中文/非换行)
    r'(?=[\n一-鿿]|$)'              # 收尾
)

FIND = re.compile(r'本需求\s+(?:REQ|BUG)-\d{5}[^\n]*')

results = {"hit_v3": [], "miss_v3": [], "hit_v4": [], "miss_v4": []}

for path in TARGET_FILES:
    content = path.read_text(encoding="utf-8")
    rel = str(path.relative_to(REPO_ROOT))
    for m in FIND.finditer(content):
        literal = m.group(0)
        display = literal[:120]

        hit_v3 = bool(R1_PATTERN_V3.fullmatch(literal))
        if hit_v3:
            results["hit_v3"].append({"file": rel, "text": display})
        else:
            results["miss_v3"].append({"file": rel, "text": display})

        hit_v4 = bool(R1_PATTERN_V4.fullmatch(literal))
        if hit_v4:
            results["hit_v4"].append({"file": rel, "text": display})
        else:
            results["miss_v4"].append({"file": rel, "text": display})

out = Path(r"D:/Workspaces/wm/code-skills/assistants/V0.0.3/code/TASK-REQ-00036-00003/inspect-v3.json")
out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"v3 命中: {len(results['hit_v3'])}, 未命中: {len(results['miss_v3'])}")
print(f"v4 命中: {len(results['hit_v4'])}, 未命中: {len(results['miss_v4'])}")
print(f"输出: {out}")