# 评审清单 — REQ-00022
版本:V0.0.3
时间:2026-06-07

## 来源
- 项目级:./assistants/rules/review-conventions.md(待 `code-rule` 沉淀,本版本 N/A)
- 内置:`plugins/code-skills/skills/code-check/checklists/review-checklist.md`(沿用)

## 本次应用的检查项

### 正确性
- [x] 实现了任务所声明的功能(10 任务全部完成)
- [x] 边界条件(本需求为字面量重命名,边界 N/A)
- [x] 异常路径(`git mv` / `Edit` / `jq` 失败处理)
- [x] `git mv` 保留 git 历史(可 `git log --follow` 追踪)

### 规范
- [x] 命名规范:`code-check` 与目录名一致
- [x] 目录结构与模块边界:过程文档摆放在子目录根
- [x] 错误处理范式:本需求 N/A
- [x] API 风格:CLI 入口名变化,无 API 行为变化
- [x] 数据建模:N/A
- [x] 安全:`git mv` / `Edit` 失败透传 stderr
- [x] 性能:本地操作 < 5 秒

### 设计符合度
- [x] T-001 符合 FR-1
- [x] T-002 ~ T-003 符合 FR-2
- [x] T-004 符合 FR-3
- [x] T-005 ~ T-009 符合 FR-4
- [x] T-010 符合 AC 校验

### 测试
- [x] 纯文档改动,无源代码改动
- [x] 0 任务涉及"测试需要=Y"

### 一致性
- [x] 11 SKILL.md(除 code-check)的 `name` 字段字节级保留
- [x] 11 SKILL.md 工作流程 / 衔接 / 不要做的事 字节级保留
- [x] V0.0.3 看板"任务清单"区段字段 0 新增
- [x] 中英 README 对仗
