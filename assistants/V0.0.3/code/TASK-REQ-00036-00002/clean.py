#!/usr/bin/env python3
"""
REQ-00036 清理脚本 v2:逐文件 Edit 模式的"清理动作"扫描+统计。

设计:本脚本**不直接写文件**,仅产出 (文件路径, 字面替换列表),由
code-it 阶段通过 Edit 工具逐字面精确替换。
"""
import re
import json
import sys
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

assert len(TARGET_FILES) == 47

# R-1:本需求 REQ-NNNNN / BUG-NNNN (放宽:括号内任意位置)
R1_PATTERN = re.compile(r'\(本需求\s+(?:REQ|BUG)-\d{5}[^)]*\)')
# 例外:本仓库主动产出 / 沿用 V0.0.X / 既有 N 需求 (这些不匹配 R-1 模式,无本需求)
# 跨需求引用 [RESULT.md](./require/REQ-NNNNN/RESULT.md) 不在括号内(在 [] 内),不匹配

# R-2:原/沿用原 + code-unit/fix-plan
R2_PATTERN = re.compile(r'\(\s*(?:原|沿用原)\s+(?:code-unit|fix-plan|fix-work-log|fix-compile-and-run|fix-test-results)[^)]*\)')
# 行内:无括号
R2_INLINE_PATTERN = re.compile(r'(?:原|沿用原)\s+(?:code-unit|fix-plan|fix-work-log|fix-compile-and-run|fix-test-results)\b[^。\n]*')

# R-3:Q-N 锁定/采纳/隐含答复
R3_PATTERN = re.compile(r'\(\s*Q-?P?\d+\s*(?:锁定|采纳|隐含答复)[^)]*\)')
# 行内
R3_INLINE_PATTERN = re.compile(r'Q-?P?\d+\s*(?:锁定|采纳|隐含答复)\b[^。\n]*')

# R-4:YYYY-MM-DD 起生效
R4_PATTERN = re.compile(r'\(\s*\d{4}-\d{2}-\d{2}\s*起生效\s*\)')
# 行内
R4_INLINE_PATTERN = re.compile(r'\d{4}-\d{2}-\d{2}\s*起生效\b[^。\n]*')

# R-5:退场文件名
R5_PATTERN = re.compile(r'(?:fix-plan|fix-work-log|fix-compile-and-run|fix-test-results)\.md')

# R-6:自然人名
R6_PERSON_PATTERN = re.compile(r'变更人[:：][\s]*[一-龥A-Za-z\s]{2,30}')
R6_OLD_PATTERN = re.compile(r'\(本仓库主动产出[^)]*原\s*\d+\s*位数字[^)]*\)')


def find_all(content, pattern, is_code_fix):
    """返回所有匹配 (位置, 匹配文本)"""
    return [(m.start(), m.end(), m.group(0)) for m in pattern.finditer(content)]


def scan_file(path: Path) -> dict:
    """扫描文件,产出所有规则的命中列表"""
    content = path.read_text(encoding="utf-8")
    is_code_fix = "code-fix" in path.parts

    result = {
        "path": str(path.relative_to(REPO_ROOT)),
        "is_code_fix": is_code_fix,
        "matches": {
            "R-1": find_all(content, R1_PATTERN, is_code_fix),
            "R-2-paren": find_all(content, R2_PATTERN, is_code_fix),
            "R-2-inline": find_all(content, R2_INLINE_PATTERN, is_code_fix),
            "R-3-paren": find_all(content, R3_PATTERN, is_code_fix),
            "R-3-inline": find_all(content, R3_INLINE_PATTERN, is_code_fix),
            "R-4-paren": find_all(content, R4_PATTERN, is_code_fix),
            "R-4-inline": find_all(content, R4_INLINE_PATTERN, is_code_fix),
            "R-5": find_all(content, R5_PATTERN, is_code_fix) if not is_code_fix else [],
            "R-6-person": find_all(content, R6_PERSON_PATTERN, is_code_fix),
            "R-6-old": find_all(content, R6_OLD_PATTERN, is_code_fix),
        }
    }
    return result


all_results = [scan_file(p) for p in TARGET_FILES]

# 统计
totals = {"R-1": 0, "R-2": 0, "R-3": 0, "R-4": 0, "R-5": 0, "R-6": 0}
for r in all_results:
    for k, v in r["matches"].items():
        if k.startswith("R-"):
            base = k.split("-")[0] + "-" + k.split("-")[1].split("-")[0]  # R-1, R-2, R-3 ...
            # 简化:把 R-N-paren 和 R-N-inline 都归到 R-N
            base = "-".join(k.split("-")[:2])
            totals[base] = totals.get(base, 0) + len(v)

# 输出汇总
print("=" * 70)
print("REQ-00036 扫描结果 v2 (放宽正则)")
print("=" * 70)
print(f"目标文件: {len(TARGET_FILES)}")
print()
print("--- 命中汇总 ---")
for k, v in totals.items():
    print(f"{k}: {v}")
print(f"总命中: {sum(totals.values())}")
print()

# 每文件命中
print("--- 每文件命中明细 ---")
for r in all_results:
    total = sum(len(v) for v in r["matches"].values())
    if total == 0:
        print(f"  [SKIP] {r['path']} (0 命中)")
        continue
    m = r["matches"]
    print(
        f"  {r['path']:75s} | "
        f"R-1={len(m['R-1']):2d} R-2={len(m['R-2-paren'])+len(m['R-2-inline']):2d} "
        f"R-3={len(m['R-3-paren'])+len(m['R-3-inline']):2d} R-4={len(m['R-4-paren'])+len(m['R-4-inline']):2d} "
        f"R-5={len(m['R-5']):2d} R-6={len(m['R-6-person'])+len(m['R-6-old']):2d} | 合计 {total}"
    )

# 写出 JSON(供后续 Edit 步骤使用)
out_path = REPO_ROOT / "assistants" / "V0.0.3" / "code" / "TASK-REQ-00036-00002" / "scan-results.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump({
        "totals": totals,
        "results": [
            {
                "path": r["path"],
                "is_code_fix": r["is_code_fix"],
                "match_count": sum(len(v) for v in r["matches"].values()),
                "matches": {
                    k: [{"start": s, "end": e, "text": t} for s, e, t in v]
                    for k, v in r["matches"].items()
                }
            }
            for r in all_results
        ]
    }, f, ensure_ascii=False, indent=2)
print(f"\n扫描结果已写入: {out_path}")
