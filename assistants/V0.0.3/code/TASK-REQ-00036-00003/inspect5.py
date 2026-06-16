#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""v5 R-1:不要求收尾字符,直接匹配主体 + 后续 0-50 任意字符。"""
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

# v5:在 FIND 找到的「本需求 REQ-NNNNN」字面上,直接截取主体 + 后续 0-50 字符
# 思路:我们关心"如何把这个字面删除/替换成什么",而 FIND 拿到的字面是「本需求 REQ-NNNNN」开头的整段
# 简化:直接用 FIND 找到的字面,再"从主体向后扩展到第一个中文段尾字符前"

# 主体锚点
ANCHOR = re.compile(r'本需求\s+(?:REQ|BUG)-\d{5}')

# 字符集:后续可以包含空格/字母/数字/标点/连字符/反引号/斜杠/中文逗号/中文括号,但**不**含中文段尾字符「，」「。」「；」「、」「:」等
# 进一步:遇到中文段尾字符(不是空格/字母/数字/标点/反引号/斜杠/连字符)就停止
# 关键:中文字符(U+4E00 - U+9FFF) 范围之外的都可
# 简化判断:0-50 字符,字符集 = [^\n] (即不跨行),遇到"本仓库"/"本技能"/"本需求"边界停止

# v5:截断到第一个中文段尾字符(，。；、)之前,或者 50 字符上限
R1_TRUNC = re.compile(
    r'本需求\s+(?:REQ|BUG)-\d{5}'   # 主体
    r'[^\n一-鿿。;；:：、]?'           # 至少 1 字符(吞掉 FR- 前的空格)
    r'(?:[^\n一-鿿。;；:：、]*[A-Za-z0-9\)\-/`])?'  # 后续字符(直到中文段尾或行尾)
)

# 测试 v5
FIND = re.compile(r'本需求\s+(?:REQ|BUG)-\d{5}[^\n]*')

results = {"v5_hit": [], "v5_miss": [], "v5_samples": []}

for path in TARGET_FILES:
    content = path.read_text(encoding="utf-8")
    rel = str(path.relative_to(REPO_ROOT))
    for m in FIND.finditer(content):
        literal = m.group(0)
        display = literal[:120]

        # v5:从主体起截取
        anchor_match = ANCHOR.match(literal)
        if not anchor_match:
            results["v5_miss"].append({"file": rel, "text": display})
            continue
        rest = literal[anchor_match.end():]
        # 在 rest 中找"段尾边界"(中文字符 / ;:/ 等)
        # 简化:取首个中文字符(不含「RE」/「FR」/「Q」字母)的索引
        cut = None
        for i, ch in enumerate(rest):
            # 中文字符
            if '一' <= ch <= '鿿':
                # 排除"后续"的"本仓库"/"本技能"等 - 但这些是后续描述,通常在"收尾字符"之后
                cut = i
                break
            # 段尾中文标点
            if ch in '。;；:：、':
                cut = i
                break
        if cut is None:
            cut = min(len(rest), 50)
        # 截断到 cut 之前的"功能短语尾" - 通常 cut 处就是"中文段尾字符"或中文"本..."
        # 实际策略:把 cut 处的中文字符一并删除
        truncated = literal[:anchor_match.end() + cut + 1] if cut < len(rest) else literal
        # 二次验证:用正则匹配 truncated
        if R1_TRUNC.fullmatch(truncated):
            results["v5_hit"].append({"file": rel, "text": display})
        else:
            results["v5_miss"].append({"file": rel, "text": display, "truncated": truncated[:120]})

out = Path(r"D:/Workspaces/wm/code-skills/assistants/V0.0.3/code/TASK-REQ-00036-00003/inspect-v5.json")
out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"v5 命中: {len(results['v5_hit'])}")
print(f"v5 未命中: {len(results['v5_miss'])}")
if results['v5_miss']:
    print("未命中样本(前 5):")
    for m in results['v5_miss'][:5]:
        print(f"  {m['file']}: {m['text']}")
print(f"输出: {out}")