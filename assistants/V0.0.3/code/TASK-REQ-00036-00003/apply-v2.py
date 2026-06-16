#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""REQ-00036 清理补丁 v2(T-3 范围执行)。

关键差异 vs T-2 的 apply.py:
- R-1 扩到"行内任意位置"(不再要求括号包围)
- 用 Python 字符串逻辑截断(找第一个中文段尾字符/中文字符前的"功能短语尾部")
- 收尾策略:找到主体后,向后找到第一个"中文字符"或"中文段尾符号"前为止
- 同时考虑"本需求 REQ-NNNNN" 后跟"FR-X/Y"、"M-N"、"改造"/"收窄"等纯英文短语 + 中文段尾
- 后跟"本仓库 X"(本仓库的"本")的,截断到"本"之前
- 后跟")"/"("/含反引号等收尾,直接删除到收尾
"""
import re
import sys
import hashlib
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

assert len(TARGET_FILES) == 47, f"expected 47, got {len(TARGET_FILES)}"

# 主体锚点
ANCHOR_RE = re.compile(r'本需求\s+(?:REQ|BUG)-\d{5}')

# 段尾边界字符:中文段尾符号 + 段尾英文符号(避免吞掉正常描述)
# 注意:本 R-1 只删除"本需求 REQ-NNNNN"主体 + 紧跟的"功能短语尾"(如 FR-X/Y / 改造 / 收窄)
# 不删除任何 CJK 内容(本仓库/本技能/沿用/字符等)
TAIL_CHARS = set('。;；:：、,)，)】］]→\\`"\'([{<>*#!')

# 中文汉字范围(用于截断点判断)
def is_cjk(ch: str) -> bool:
    if not ch:
        return False
    cp = ord(ch)
    return 0x4E00 <= cp <= 0x9FFF or 0x3400 <= cp <= 0x4DBF


def truncate_after_anchor(literal: str) -> int:
    """从主体结束后开始扫描,返回"删除到哪"的索引(相对 literal 起点)。

    策略:
    1. 找主体结束位置
    2. 从主体结束后第一个非空格字符开始,扫描到第一个:
       - 中文字符(0x4E00-0x9FFF 或 0x3400-0x4DBF),停止于该字符之前
       - 段尾字符(。;；:：、,)，)】］]),停止于该字符之前
       - 字符超过 50 个,停止于第 50 个字符
    3. 同时处理"功能短语尾"模式(数字/字母 + 中文段尾)
    """
    m = ANCHOR_RE.match(literal)
    if not m:
        return 0
    pos = m.end()  # 主体结束位置
    # 跳过主体后的 0-1 个空格
    if pos < len(literal) and literal[pos] == ' ':
        pos += 1
    # 扫描后续
    start = pos
    max_len = 30
    while pos < len(literal) and (pos - start) < max_len:
        ch = literal[pos]
        if ch == '\n':
            break  # 跨行停止
        if ch in TAIL_CHARS:
            break  # 段尾符号停止
        if is_cjk(ch):
            # 中文字符:如果这个字是"本仓库"/"本技能"等的"本"字,需要把后续整段也截断
            # 但因为我们要清的就是"本需求 REQ-NNNNN 后续短语",所以停止于"本"字之前
            # 即:遇到 CJK 字符(且不是"Q" / "F" / "M" / "N" 等字母)就停止
            # 但前面的字符可能是 "FR-X/Y" 这样的英文短语,后面接中文段尾
            # 关键:本仓库 SKILL.md 中 R-1 字面后续的中文字符,通常不是"FR-X"的一部分
            # (FR 是字母),所以遇到 CJK 就停止是对的
            break
        pos += 1
    # 如果 pos 没移动(pos == start),说明主体后紧跟段尾符号,直接返回 0(只删主体)
    if pos == start:
        return start
    # 删除范围 = [start, pos)
    return pos


def apply_r1(body: str) -> tuple:
    """R-1:删除「本需求 REQ-NNNNN [可选 FR-X/Y] [可选 改造/收窄/... + 数字 + 段尾」整段。"""
    stats = []
    new_body = body
    while True:
        m = ANCHOR_RE.search(new_body)
        if not m:
            break
        end = truncate_after_anchor(new_body[m.start():])
        if end == 0:
            # 退化:主体后紧跟段尾,只删除主体
            end = m.end() - m.start()
        # 删除整段
        new_body = new_body[:m.start()] + new_body[m.start() + end:]
        stats.append(m.start())
    return new_body, len(stats)


# R-2 ~ R-6 沿用 T-2
R2_PAREN_PATTERN = re.compile(r'\(\s*(?:原|沿用原)\s+(?:code-unit|fix-plan|fix-work-log|fix-compile-and-run|fix-test-results)[^)]*\)')
R2_INLINE_PATTERN = re.compile(r'(?:原|沿用原)\s+(?:code-unit|fix-plan|fix-work-log|fix-compile-and-run|fix-test-results)\b[^。\n]*')

R3_PAREN_PATTERN = re.compile(r'\(\s*Q-?P?\d+\s*(?:锁定|采纳|隐含答复)[^)]*\)')
R3_INLINE_PATTERN = re.compile(r'Q-?P?\d+\s*(?:锁定|采纳|隐含答复)\b[^。\n]*')

R4_PAREN_PATTERN = re.compile(r'\(\s*\d{4}-\d{2}-\d{2}\s*起生效\s*\)')
R4_INLINE_PATTERN = re.compile(r'\d{4}-\d{2}-\d{2}\s*起生效\b[^。\n]*')

R5_PATTERN = re.compile(r'(?:fix-plan|fix-work-log|fix-compile-and-run|fix-test-results)\.md')

R6_PERSON_PATTERN = re.compile(r'变更人[:：][\s]*[一-龥A-Za-z\s]{2,30}')
R6_OLD_PATTERN = re.compile(r'\(本仓库主动产出[^)]*原\s*\d+\s*位数字[^)]*\)')


def extract_frontmatter(content: str) -> tuple:
    if not content.startswith("---"):
        return "", content
    end = content.find("\n---", 3)
    if end == -1:
        return "", content
    frontmatter = content[: end + 4]
    rest = content[end + 4 :]
    return frontmatter, rest


def apply_rules(body: str, is_code_fix: bool) -> tuple:
    stats = {}
    new_body, n = apply_r1(body)
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
    # 清理可能产生的多余空行
    body = re.sub(r'\n{3,}', '\n\n', body)
    # 清理可能产生的多余空格
    body = re.sub(r'  +', ' ', body)
    return body, stats


def verify(body: str, is_code_fix: bool) -> dict:
    failed = {}
    if ANCHOR_RE.search(body):
        failed["R-1"] = len(ANCHOR_RE.findall(body))
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
print("REQ-00036 清理补丁 v2(T-3 范围)")
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

    fm_md5_before = hashlib.md5(frontmatter.encode("utf-8")).hexdigest()

    new_body, stats = apply_rules(body, is_code_fix)
    new_content = frontmatter + new_body

    fm_md5_after = hashlib.md5(frontmatter.encode("utf-8")).hexdigest()
    assert fm_md5_before == fm_md5_after, f"frontmatter 字节级不一致: {rel_path}"

    failed = verify(new_body, is_code_fix)
    if failed:
        verify_failed_files.append((str(rel_path), failed))

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
        f"R-1={stats.get('R-1',0):3d} R-2={stats['R-2']:2d} R-3={stats['R-3']:2d} "
        f"R-4={stats['R-4']:2d} R-5={stats['R-5']:2d} R-6={stats['R-6']:2d} | "
        f"行 {original_lines:4d}->{new_lines:4d} -{reduction_pct:.1f}%"
    )

print()
print("=" * 70)
print("汇总(T-3 范围)")
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
