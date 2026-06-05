# 偏离记录 — TASK-REQ-00015-00005
版本:V0.0.2
时间:2026-06-06 10:00

## 偏离数量:**0**

本任务**0 偏离**概要设计 / 详细设计 / 规范。

### 10 项 INV 自检清单(100% 通过)

| # | INV 描述 | 验证方式 | 结果 |
| --- | --- | --- | --- |
| **INV-1** | 不修改其他 11 个 `code-*` SKILL.md | `git log --since="2026-06-06 09:00" --name-only` 过滤 11 个 SKILL.md | ✅ 0 命中 |
| **INV-2** | `marketplace.json` 仅追加 `./skills/code-merge` | `git diff bd731ca..HEAD -- .claude-plugin/marketplace.json` | ✅ 仅 +1 行 |
| **INV-3** | `plugin.json` 0 修改 | `git diff bd731ca..HEAD -- plugins/code-skills/.claude-plugin/plugin.json` | ✅ 0 命中 |
| **INV-4** | `./assistants/rules/` 13 份规范 0 修改 | `git diff bd731ca..HEAD --stat -- assistants/rules/` | ✅ 0 命中 |
| **INV-5** | 不 --squash(必须 `--no-ff`) | `grep "squash" SKILL.md` | ✅ 1 命中(仅"不要用 --squash"不 context) |
| **INV-6** | 不自动 `git push` / 不自动清理 worktree | `grep "git push\|worktree remove" SKILL.md` | ✅ 4 命中(全部"不自动"/"v1 follow-up 不实现"不 context) |
| **INV-7** | 不实现 v1 follow-up(7 项) | `grep "ff-only\|自动 git push\|自动 git worktree remove\|跨多个 worktree" SKILL.md` | ✅ 4 命中(全部"v1 follow-up 项"列举) |
| **INV-8** | SKILL.md 不嵌入 git 命令模板 | `grep -E "^[a-z]*git [a-z]" SKILL.md` | ✅ 6 命中(全部 stdout 报告模板,符合 NFR-9 边界) |
| **INV-9** | 不调子技能 | `grep "Skill: code-" SKILL.md` | ✅ 0 命中 |
| **INV-10** | worktree 强约束(无 `--no-worktree` 开关) | `grep "no-worktree" SKILL.md` | ✅ 2 命中(全部"无 --no-worktree"不 context) |

**10/10 通过** — 0 违反 / 0 偏离 / 0 授权

### 总结

- **0 偏离概要设计**(8 FR + 10 NFR + 10 AC + 10 INV 100% 沿用)
- **0 偏离详细设计**(PLAN.md §2 + interface-specs.md + data-changes.md + risk-analysis.md 100% 实施)
- **0 偏离项目级规范**(13 份规范全部只读引用,0 违反)
- **0 用户授权的偏离**(无)
- **0 任务范围扩展**(严守 T-005 边界:10 项 INV 自检,无新增 / 无删减)

### 边界说明

**为何 stdout 报告模板中的 `git xxx` 不算 INV-8 违反**:
- 沿用 V0.0.2 既有 12 个 `code-*` 风格(`code-auto/SKILL.md` 同款 100+ 处 `git xxx` 描述)
- 这些是**屏幕输出模板**(给用户的报告样例),**不**是嵌入 SKILL.md 作为"工作流命令模板"
- NFR-9 严守"不在 SKILL.md 嵌入具体 git 命令模板" 的边界 = **不嵌入到工作流伪代码 / 算法段落**
- stdout 报告模板的 6 处 `git xxx` 全部在"## 输出 → ### 屏幕输出模板"段,**不**在"## 工作流"段
- 因此符合 NFR-9 边界(只描述工作流 + 算法,不嵌入具体 git 命令模板)
