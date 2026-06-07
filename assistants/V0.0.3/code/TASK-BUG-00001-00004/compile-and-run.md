# 编译与启动验证 — TASK-BUG-00001-00004
版本:V0.0.3
时间:2026-06-07 17:46

## 构建 / 启动
**N/A**

## 静态校验

| 校验项 | 命令 | 时间 | 退出码 | 输出 | 结论 |
| --- | --- | --- | --- | --- | --- |
| INV-13:`code-fix` 含"不修改 SKILL.md"硬约束 | `grep -n "不修改.*SKILL.md" plugins/code-skills/skills/code-fix/SKILL.md` | 2026-06-07 17:46 | 0 | `431:- 不修改 plugins/code-skills/skills/*/SKILL.md 任何文件(...)` (命中 1 行) | ✅ 通过 |
| INV-16:frontmatter 字节级保留 | `git diff plugins/code-skills/skills/code-fix/SKILL.md \| head -15` | 2026-06-07 17:46 | 0 | diff 范围仅 `## 不要做的事` 段;frontmatter 0 变化 | ✅ 通过 |

## 修复记录
**0 修复循环**
