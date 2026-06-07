# 测试结果 — TASK-BUG-00001-00005
版本:V0.0.3
时间:2026-06-07 17:53

## 测试命令
**不适用**

## 静态校验(2 个文件)

| 测试 ID | 描述 | 命令 | 期望 | 实际 | 结论 |
| --- | --- | --- | --- | --- | --- |
| INV-14 | `code-it` 含"唯一允许的生产代码改动"声明 | `grep -n "唯一.*生产代码改动" plugins/code-skills/skills/code-it/SKILL.md` | 命中 ≥ 1 行 | 命中 2 行(line 14 + 58) | ✅ 通过 |
| INV-15 | `code-unit` 含"可改测试代码"边界声明 | `grep -n "可改测试代码" plugins/code-skills/skills/code-unit/SKILL.md` | 命中 ≥ 1 行 | 命中 1 行(line 11) | ✅ 通过 |
| INV-16 | 2 个 SKILL.md frontmatter 字节级保留 | `git diff ... code-it/SKILL.md code-unit/SKILL.md` | 仅新增小节处有 diff,frontmatter 0 diff | diff 范围仅 `## 目标` 段后,frontmatter 0 变化 | ✅ 通过 |

## 失败用例详情
**0 失败**

## 备注
- 累计已覆盖:T-1(INV-10) + T-2(INV-11) + T-3(INV-12) + T-4(INV-13) + T-5(INV-14 + INV-15)= 6 项 INV
- INV-16 累计验证 5 次(每个 SKILL.md 1 次;本任务 2 个文件 1 次)
- **全部 7 项 INV + INV-16 静态校验 5/5 全通过 = 8/8 项验收清单(本任务实现,8 项全通过)**
- 仅剩"回归校验(e69a58a / 6dee813 / 3e1573e / e568328 4 commit 保留)"由 code-fix 推进阶段统一验证
