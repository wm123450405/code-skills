# 现有功能需求 — EXISTING-010:代码评审(code-review)

> 本文档由 `code-init` 技能基于项目现有代码生成。
> 描述的是"**代码中已实现**"的功能,而非待开发的功能。
> 未来对该功能的**修改**应通过 `code-require`(增量更新本文件)进行。
> 最后更新:2026-06-03 18:10
> 适用版本:基线版本 `V0.0.0`

## 需求概述
`code-review` 是主流程的**最后一步**(版本感知):接收"需求编码"(`REQ-YYYY-NNNN`),读 `plan/<需求>/PLAN.md` 中本需求所有任务,逐任务按 `./assistants/rules/`(项目级评审清单) + `checklists/review-checklist.md` 评审,产出整体 `REVIEW-REPORT.md` 与派生的"审查改修"任务(每个任务的改修要求保存到 `review/<任务编码>/RESULT.md`,作为 `code-it` 的输入)。同时把派生任务追加到 `PLAN.md` 的"任务总览"(触发/来源=**审查改修**,关联任务=被修正原任务)。

## 现有实现位置

| 维度 | 位置 |
| --- | --- |
| 主要文件 | `plugins/code-skills/skills/code-review/SKILL.md`(425 行) |
| 关键函数/类 | (N/A) |
| 涉及文件数 | 4(SKILL.md + checklists/ + 3 个模板) |
| 大致代码量 | 约 520 行 |

### 关键代码位置(可选)
- `plugins/code-skills/skills/code-review/SKILL.md` — 工作流(读 .current-version → 校验需求 → 读 PLAN.md + code/ + test/ + rules/ + checklist → 逐任务评审 → 写 REVIEW-REPORT.md → 派生改修任务 → 更新 PLAN.md + 看板)
- `plugins/code-skills/skills/code-review/checklists/review-checklist.md` — 强制校验清单
- `plugins/code-skills/skills/code-review/templates/REVIEW-REPORT.md` — 整体评审报告模板
- `plugins/code-skills/skills/code-review/templates/REVIEW-FIX.md` — 单个改修任务模板
- `plugins/code-skills/skills/code-review/templates/assistants-layout.md`

## 用户角色与场景

### 角色
- **架构师 / 高级开发**:整需求代码评审,派生改修任务

### 场景
- 一组相关任务(同一需求)完成后做整体评审
- 派生"审查改修"任务让 `code-it` 跟进
- 收尾某需求的代码质量

## 功能点(FR)

- **FR-1**:读 `.current-version` 确认激活版本
- **FR-2**:校验 `plan/<需求>/PLAN.md` 存在,且本需求所有任务的开发/测试状态符合"可评审"条件
- **FR-3**:读 `./assistants/rules/`(项目级评审清单)+ `checklists/review-checklist.md`
- **FR-4**:逐任务按规则 + 清单评审,产出整体 `review/<需求>/REVIEW-REPORT.md`
- **FR-5**:派生"审查改修"任务:每个任务的改修要求保存到 `review/<任务编码>/RESULT.md`
- **FR-6**:把派生任务追加到 `PLAN.md` 的"任务总览"(触发/来源=**审查改修**,关联任务=被修正原任务)
- **FR-7**:同步更新看板的"评审发现汇总" / "派生任务记录" / "缺陷清单" / "变更记录"
- **FR-8**:可独立重跑(也可在 `code-it` 完成后、`code-unit` 缺失时直接调用 —— 评审会标注"测试缺失")

## 关键接口

### CLI
```
/code-skills:code-review REQ-2026-0001
```

### 输入
- `./assistants/<版本号>/plan/<需求>/PLAN.md`(所有任务)
- `./assistants/<版本号>/code/<任务>/RESULT.md`(代码改修正文)
- `./assistants/<版本号>/test/<任务>/RESULT.md`(测试结果)
- `./assistants/rules/`(项目级评审清单,只读)
- `./assistants/rules/` + `checklists/review-checklist.md`(本技能自带清单)

### 输出
- `./assistants/<版本号>/review/<需求>/REVIEW-REPORT.md`
- 派生"审查改修"任务:`./assistants/<版本号>/review/<任务编码>/RESULT.md`
- 同步更新 `<版本号>/RESULT.md` 看板

## 数据模型(若适用)

| 实体 | 字段 | 约束 |
| --- | --- | --- |
| 评审发现 ID | `F-NNN` | 3 位数序号,本需求内唯一 |
| 评审级别 | 必须改/建议改/可选 | 看板字段 |
| 评审维度 | 安全/性能/可读性/可维护性/... | 自由扩展 |
| 派生任务 | `REQ-YYYY-NNNN-NNN`(新) | 触发/来源=**审查改修**,关联任务=被修正原任务 |
| 整体报告 | `REVIEW-REPORT.md` | 字段:评审时间/参与任务/通过项/发现问题清单/派生改修任务/总结 |
| 单个改修 | `REVIEW-FIX.md` | 字段:问题描述/严重度/建议方案/验收标准 |

## 验收标准(AC)

- **AC-1**:无 `.current-version` 时立即中止
- **AC-2**:`plan/<需求>/PLAN.md` 不存在时立即中止
- **AC-3**:产出 `review/<需求>/REVIEW-REPORT.md`,含本需求所有任务的评审结果
- **AC-4**:有需要改修的项时,派生"审查改修"任务到 `review/<任务编码>/RESULT.md`
- **AC-5**:派生任务的"触发/来源"= **审查改修**,关联任务=被修正原任务
- **AC-6**:同步更新 PLAN.md 的"任务总览"(追加派生任务)
- **AC-7**:同步更新看板"评审发现汇总" / "派生任务记录" / "缺陷清单" / "变更记录"
- **AC-8**:`code-unit` 缺失时评审会标注"测试缺失",但不会强制要求先补测试

## 关联功能

| 关联编码 | 关联点 | 影响 |
| --- | --- | --- |
| EXISTING-006 | 读 `plan/<需求>/PLAN.md` 作为输入 | 主流程上游 |
| EXISTING-007 | 读 `code/<任务>/RESULT.md` 作为输入 | 主流程上游(代码) |
| EXISTING-008 | 读 `test/<任务>/RESULT.md` 作为输入 | 主流程上游(测试) |
| EXISTING-007 (派生) | 派生任务的"触发/来源"=**审查改修** → `code-it` 读 `review/<任务>/RESULT.md` | 回路 |
| EXISTING-003 | 读 `rules/` + `checklists/review-checklist.md` 作为约束 | 双源 |
| EXISTING-002 | `code-version` 是前置门 | 必须先有激活版本 |

## 已知限制/技术债

- 评审维度(安全/性能/...)完全由 AI 自主决定,缺少项目级评审 checklist 模板
- "派生改修任务"是新任务(不修改原任务),可能导致任务编号膨胀
- 评审发现与缺陷清单的边界模糊 —— 评审发现是否会自动登记为 `BUG-NNN` 不明确
- "code-unit 缺失时评审会标注"是有用的回退,但不强制要求先补测试,可能放过"测试不充分"的代码
- 派生任务可能跨多个原任务(如"重构 A 与 B 共用的 X 模块"),SKILL.md 未规定如何处理跨任务派生

## 变更记录

| 时间 | 变更类型 | 变更摘要 | 关联项 |
| --- | --- | --- | --- |
| 2026-06-03 18:10 | 需求登记 | code-init 识别并登记现有功能 EXISTING-010 | EXISTING-010 |
