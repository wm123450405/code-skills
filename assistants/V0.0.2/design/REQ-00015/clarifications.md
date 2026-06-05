# 待澄清与已决项 — REQ-00015
更新时间:2026-06-06 09:00
版本:V0.0.2

> 本需求上游 `code-require` 阶段已完成 7 项已锁定 + 2 项采纳默认(详 `require/REQ-00015/RESULT.md`)。
> 本设计阶段**无新澄清项** —— 上游已锁定项直接沿用,v1 follow-up 项不实现。

## 上游已锁定项(直接沿用,无新澄清)
1. 默认主干分支 = `origin/main`(用户在 clarifications.md 第 2 轮问题 5 锁定)
2. 冲突解决用 LLM 智能合并,**不**用脚本/工具批量(用户在 clarifications.md 第 1 轮问题 1 锁定)
3. `git merge <target> --no-ff`(用户在 clarifications.md 第 1 轮问题 2 锁定,**不**用 `--squash`)
4. 看板自检**不**修复统计行,只打印(用户在 clarifications.md 第 3 轮问题 6 锁定)
5. 看板自检是核心执行步骤,非可选(用户在 clarifications.md 第 3 轮问题 6 锁定)
6. 整个技能执行过程**不**产生任何过程文件 / 结果文件(SKILL.md 必产)(用户在 clarifications.md 第 2 轮问题 4 锁定)
7. merge commit 消息走 git 默认格式(用户在 clarifications.md 第 3 轮问题 7 锁定)

## 上游采纳默认项
- `code-merge` 不自动调 `code-publish`(采纳默认:职责分离)
- `code-auto` 不自动调 `code-merge`(采纳默认:用户手动决策)

## v1 follow-up 项(本设计**不**实现,留作 v2)
- `--ff-only` 开关
- `--target <branch>` 显式主分支参数(仅环境变量 `CODE_MERGE_TARGET`)
- 自动 `git push` 到 origin
- 自动 `git worktree remove` 清理
- 跨多个 worktree 同时合并
- 看板自检"自动修复统计行"
- `code-auto` 在自动循环完成后**自动**调用 `code-merge`(本设计 INV-9 严守)

## 本设计阶段新发现的问题
**0** —— 上游需求 + 规范已提供足够信息,无需新增澄清
