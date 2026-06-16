#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""把每个「本需求 REQ-」字面写到 JSON,UTF-8。"""
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

FIND = re.compile(r'本需求\s+(?:REQ|BUG)-\d{5}[^\n]*')

R1_PATTERN = re.compile(
    r'本需求\s+(?:REQ|BUG)-\d{5}'
    r'(?:\s+(?:FR|M|N|Q)[\-‑]\d+)?'
    r'(?:\s*(?:改造|收窄|收紧|新增|撤销|退场|扩展|字节级保留|一步收敛|进一步收敛|改造后|新增边界|屏显瘦身|双正则兼容|新版本?模式|前\d+个|总第\d+个|清空|去重|清退|集中化|原子化|重写|重命名|改写|改造为|收窄至|扩展为|新增为|调整为|进一步收窄为|改造为\s*\d+\s*列|收紧至\s*\d+\s*列)?)*'
    r'(?=\s*[，。、,;；\)）\n]|$)'
)

# 额外模式:后续有 FR-X/Y 形式
R1_PATTERN_V2 = re.compile(
    r'本需求\s+(?:REQ|BUG)-\d{5}'
    r'(?:[^，。、,;；\n]{0,30}?)'   # 0-30 个非收尾字符(非贪婪)
    r'(?=[，。、,;；\)）\n])'
)

results = {"hit": [], "miss": []}
for path in TARGET_FILES:
    content = path.read_text(encoding="utf-8")
    rel = str(path.relative_to(REPO_ROOT))
    for m in FIND.finditer(content):
        literal = m.group(0)
        # 取前 100 字符作为标识
        display = literal[:120]
        hit_v1 = bool(R1_PATTERN.fullmatch(literal))
        hit_v2 = bool(R1_PATTERN_V2.fullmatch(literal))
        item = {"file": rel, "text": display, "v1_hit": hit_v1, "v2_hit": hit_v2}
        if hit_v1 or hit_v2:
            results["hit"].append(item)
        else:
            results["miss"].append(item)

# 写入 JSON,UTF-8
out = Path(r"D:/Workspaces/wm/code-skills/assistants/V0.0.3/code/TASK-REQ-00036-00003/inspect-result.json")
out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"v1/v2 命中: {len(results['hit'])}")
print(f"v1/v2 未命中: {len(results['miss'])}")
print(f"输出: {out}")