# 待澄清与已决项 — REQ-00015
更新时间:2026-06-06 09:10
版本:V0.0.2

> 本需求上游 `code-require` 阶段已完成 7 项已锁定 + 2 项采纳默认(详 `require/REQ-00015/RESULT.md`)。
> 本需求 `code-design` 阶段确认 0 项新澄清(详 `design/REQ-00015/clarifications.md`)。
> 本 `code-plan` 阶段**无新澄清项** —— 上游 + 设计已锁定项直接沿用,5 任务拆分明确无歧义。

## 上游 + 设计已锁定项(直接沿用)
1. 默认主干分支 = `origin/main`
2. 冲突解决用 LLM 智能合并,**不**用脚本/工具批量
3. `git merge <target> --no-ff`,**不**用 `--squash`
4. 看板自检**不**修复统计行,只打印
5. 看板自检是核心执行步骤,非可选
6. 整个技能执行过程**不**产生任何过程文件 / 结果文件(SKILL.md 必产)
7. merge commit 消息走 git 默认格式
8. worktree 模式强约束
9. 不自动 push / 不自动 `worktree remove`
10. SKILL.md 不嵌入 git 命令模板
11. 0 派生 / 0 调其他子技能
12. 10 项 INV 全部通过自检

## 本计划阶段 5 任务拆分明确(0 歧义)
- T-001 写 SKILL.md(主文件)
- T-002 改 marketplace.json(协议清单)
- T-003 改中英 README(用户入口)
- T-004 同步看板 4 处(版本一致性)
- T-005 10 项 INV 自检 + 收尾(质量门)

## v1 follow-up 项(本计划**不**实现,留作 v2)
- `--ff-only` 开关
- `--target <branch>` 显式主分支参数(仅环境变量 `CODE_MERGE_TARGET`)
- 自动 `git push` 到 origin
- 自动 `git worktree remove` 清理
- 跨多个 worktree 同时合并
- 看板自检"自动修复统计行"
- `code-auto` 在自动循环完成后**自动**调用 `code-merge`

## 本计划阶段新发现的问题
**0** —— 上游需求 + 概要设计 + 规范已提供足够信息,无需新增澄清
