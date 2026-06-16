#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""REQ-00036 清理补丁 v2 - dry-run 扫描(不写回)。"""
import re
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

R1_PATTERN = re.compile(
    r'本需求\s+(?:REQ|BUG)-\d{5}'
    r'(?:\s+(?:FR|M|N|Q)[\-‑]\d+)?'
    r'(?:\s*(?:改造|收窄|收紧|新增|撤销|退场|扩展|字节级保留|一步收敛|进一步收敛|改造后|新增边界|屏显瘦身|双正则兼容|新版本?模式|前\d+个|总第\d+个|清空|去重|清退|集中化|原子化|重写|重命名|改写|改造为|收窄至|扩展为|新增为|调整为|进一步收窄为|改造为\s*\d+\s*列|收紧至\s*\d+\s*列)?)*'
    r'(?=\s*[，。、,;；\)）\n]|$)'
)

print("=" * 70)
print("R-1 扩展 dry-run 扫描")
print("=" * 70)
total = 0
for path in TARGET_FILES:
    content = path.read_text(encoding="utf-8")
    matches = R1_PATTERN.findall(content)
    if matches:
        rel = path.relative_to(REPO_ROOT)
        total += len(matches)
        print(f"\n  {rel} ({len(matches)} matches):")
        for m in matches[:3]:
            print(f"    - {m!r}")
        if len(matches) > 3:
            print(f"    ... ({len(matches) - 3} more)")
print()
print(f"总计: {total} 命中,跨 {sum(1 for p in TARGET_FILES if R1_PATTERN.search(p.read_text(encoding='utf-8')))} 文件")
