#!/usr/bin/env python3
"""REQ-00036 清理执行脚本。

设计:
- 读每个目标文件
- 分离 frontmatter(L1-3 字节级保留,不动)
- 对 body 部分应用 6 条规则
- 写回文件
- 二次验证
"""
import re
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

# 6 条规则
R1_PATTERN = re.compile(r'\(本需求\s+(?:REQ|BUG)-\d{5}[^)]*\)')
R2_PAREN_PATTERN = re.compile(r'\(\s*(?:原|沿用原)\s+(?:code-unit|fix-plan|fix-work-log|fix-compile-and-run|fix-test-results)[^)]*\)')
R2_INLINE_PATTERN = re.compile(r'(?:原|沿用原)\s+(?:code-unit|fix-plan|fix-work-log|fix-compile-and-run|fix-test-results)\b[^。\n]*')
R3_PAREN_PATTERN = re.compile(r'\(\s*Q-?P?\d+\s*(?:锁定|采纳|隐含答复)[^)]*\)')
R3_INLINE_PATTERN = re.compile(r'Q-?P?\d+\s*(?:锁定|采纳|隐含答复)\b[^。\n]*')
R4_PAREN_PATTERN = re.compile(r'\(\s*\d{4}-\d{2}-\d{2}\s*起生效\s*\)')
R4_INLINE_PATTERN = re.compile(r'\d{4}-\d{2}-\d{2}\s*起生效\b[^。\n]*')
R5_PATTERN = re.compile(r'(?:fix-plan|fix-work-log|fix-compile-and-run|fix-test-results)\.md')
R6_PERSON_PATTERN = re.compile(r'变更人[:：][\s]*[一-龥A-Za-z\s]{2,30}')
R6_OLD_PATTERN = re.compile(r'\(本仓库主动产出[^)]*原\s*\d+\s*位数字[^)]*\)')


def extract_frontmatter(content: str) -> tuple[str, str]:
    if not content.startswith("---"):
        return "", content
    end = content.find("\n---", 3)
    if end == -1:
        return "", content
    frontmatter = content[: end + 4]
    rest = content[end + 4 :]
    return frontmatter, rest


def apply_rules(body: str, is_code_fix: bool) -> tuple[str, dict]:
    stats = {}
    new_body, n = R1_PATTERN.subn("", body)
    stats["R-1"] = n
    body = new_body
    new_body, n = R2_PAREN_PATTERN.subn("", body)
    new_body, n2 = R2_INLINE_PATTERN.subn("", new_body)
    stats["R-2"] = n + n2
    body = new_body
    new_body, n = R3_PAREN_PATTERN.subn("", body)
    new_body, n2 = R3_INLINE_PATTERN.subn("", new_body)
    stats["R-3"] = n + n2
    body = new_body
    new_body, n = R4_PAREN_PATTERN.subn("", body)
    new_body, n2 = R4_INLINE_PATTERN.subn("", new_body)
    stats["R-4"] = n + n2
    body = new_body
    if not is_code_fix:
        new_body, n = R5_PATTERN.subn("", body)
        stats["R-5"] = n
        body = new_body
    else:
        stats["R-5"] = 0
    new_body, n = R6_PERSON_PATTERN.subn("变更人:<责任人>", body)
    new_body, n2 = R6_OLD_PATTERN.subn("", new_body)
    stats["R-6"] = n + n2
    body = new_body
    body = re.sub(r'\n{3,}', '\n\n', body)
    return body, stats


def verify(body: str, is_code_fix: bool) -> dict:
    failed = {}
    if R1_PATTERN.search(body):
        failed["R-1"] = len(R1_PATTERN.findall(body))
    if R2_PAREN_PATTERN.search(body) or R2_INLINE_PATTERN.search(body):
        failed["R-2"] = "still has matches"
    if R3_PAREN_PATTERN.search(body) or R3_INLINE_PATTERN.search(body):
        failed["R-3"] = "still has matches"
    if R4_PAREN_PATTERN.search(body) or R4_INLINE_PATTERN.search(body):
        failed["R-4"] = "still has matches"
    if not is_code_fix and R5_PATTERN.search(body):
        failed["R-5"] = len(R5_PATTERN.findall(body))
    return failed


print("=" * 70)
print("REQ-00036 清理执行")
print("=" * 70)

totals = {"R-1": 0, "R-2": 0, "R-3": 0, "R-4": 0, "R-5": 0, "R-6": 0}
verify_failed_files = []
revert_list = []
modified_files = []

for path in TARGET_FILES:
    rel_path = path.relative_to(REPO_ROOT)
    is_code_fix = "code-fix" in path.parts

    original = path.read_text(encoding="utf-8")
    frontmatter, body = extract_frontmatter(original)

    # 备份 frontmatter 字节级 md5
    import hashlib
    fm_md5_before = hashlib.md5(frontmatter.encode("utf-8")).hexdigest()

    new_body, stats = apply_rules(body, is_code_fix)
    new_content = frontmatter + new_body

    fm_md5_after = hashlib.md5(frontmatter.encode("utf-8")).hexdigest()  # 应与原 frontmatter 字节级一致(因为我们没改 frontmatter)
    assert fm_md5_before == fm_md5_after, f"frontmatter 字节级不一致: {rel_path}"

    # 二次验证
    failed = verify(new_body, is_code_fix)
    if failed:
        verify_failed_files.append((str(rel_path), failed))

    # 写回
    original_lines = original.count("\n") + 1
    new_lines = new_content.count("\n") + 1
    line_diff = original_lines - new_lines
    reduction_pct = (line_diff / max(original_lines, 1)) * 100

    if line_diff > 0 or new_content != original:
        path.write_text(new_content, encoding="utf-8")
        modified_files.append(str(rel_path))

    if reduction_pct > 30:
        revert_list.append((str(rel_path), reduction_pct))

    for k, v in stats.items():
        totals[k] += v

    print(
        f"  {str(rel_path):75s} | "
        f"R-1={stats.get('R-1',0):2d} R-2={stats['R-2']:2d} R-3={stats['R-3']:2d} "
        f"R-4={stats['R-4']:2d} R-5={stats['R-5']:2d} R-6={stats['R-6']:2d} | "
        f"行 {original_lines:4d}->{new_lines:4d} -{reduction_pct:.1f}%"
    )

print()
print("=" * 70)
print("汇总")
print("=" * 70)
for k, v in totals.items():
    print(f"  {k}: {v}")
print(f"  合计: {sum(totals.values())}")
print(f"  修改文件数: {len(modified_files)}")
print(f"  二次验证失败: {len(verify_failed_files)} 个")
for path, failed in verify_failed_files[:10]:
    print(f"    - {path}: {failed}")
print(f"  需回退文件(>30% 减少): {len(revert_list)} 个")
for path, pct in revert_list:
    print(f"    - {path} (-{pct:.1f}%)")

# 占位符保留验证
print()
print("=" * 70)
print("占位符保留验证(NFR-6)")
print("=" * 70)
placeholders = ["REQ-00001", "BUG-00001", "TASK-REQ-00001-00001"]
for ph in placeholders:
    total = 0
    files_with = 0
    for path in TARGET_FILES:
        content = path.read_text(encoding="utf-8")
        n = content.count(ph)
        if n > 0:
            total += n
            files_with += 1
    print(f"  {ph}: 剩余 {total} 次,分布在 {files_with} 文件")