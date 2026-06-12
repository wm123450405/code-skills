# 数据结构完整变更 — REQ-00030

更新时间:2026-06-12 14:31
版本:V0.0.3

> **本节是 `code-plan` 详设阶段产出**——把 `code-design` §9 4 项实体**详细化**为完整字段(类型/约束/索引/迁移)。
> 本需求**不**涉及持久化数据结构变更,本节为"逻辑实体"详细化(锚点 / INV 字节级保留的"伪结构")。

## 新增实体:`check-validation-point`(逻辑实体,无持久化)

### 字段表

| 字段 | 类型 | 约束 | 索引 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | PK, `vp<N>`(vp1 / vp2 / vp3) | — | 校验点唯一标识 |
| name | string | NOT NULL, ≤ 50 字符 | — | 校验点名称(详设完整性 / 概设越界 / 行数比例) |
| trigger | enum('planIntegrity' \| 'designBoundary' \| 'lineRatio') | NOT NULL | — | 校验点类型 |
| action | enum('deriveTask' \| 'warning') | NOT NULL | — | 触发动作(派生任务 / 警告) |
| taskType | enum('重构') | (action=deriveTask 时 NOT NULL) | — | 派生任务类型 |
| triggerSource | enum('设计变更') | (action=deriveTask 时 NOT NULL) | — | 派生任务触发/来源 |
| relatedTask | string | (action=deriveTask 时 NOT NULL) | — | 关联任务(被修正原任务) |
| warningThreshold | number | (action=warning 时 NOT NULL, 默认 1.2) | — | 警告阈值(行数比例) |
| createdAt | datetime | NOT NULL | — | 创建时间(由 code-check 写入) |
| updatedAt | datetime | NOT NULL | — | 更新时间 |

### 关系

- 与"## 任务清单"区段:**一对多**(1 个校验点可派生 0 ~ N 个任务)
- 与"## 评审发现汇总"区段:**一对多**(1 个校验点可触发 0 ~ N 条评审发现)

### 存储选型

- **不适用**(逻辑实体,无持久化存储)
- 校验点的"创建"是 `code-check` 评审清单的纯文本追加,**不**写入数据库

### 迁移脚本

- **不适用**(无数据库)

### 依据规范

- `commit-conventions`(派生任务按"重构"类型登记)
- `dashboard-conventions §规则 1`(派生任务同步到"任务清单"区段)

## 修改实体:`design-template-chapter`(逻辑实体,无持久化)

### 字段变更

| 字段 | 类型 | 约束变更 |
| --- | --- | --- |
| `§7.1 模块总览表` | markdown 表格 | 列数:7 → 5(移除"对外接口" / "理由" / "符合的规范条款") |
| `§7.2 新增模块` | markdown 表格 | 列数:7 → 5(移除"关键设计点" / "对外接口" / "依赖" / "理由") |
| `§7.5 设计边界` | markdown 小节 | **新增**(原本不存在) |
| `§8 接口概要` | markdown 表格 | 列数:6 → 4(移除"数据格式" / "错误码" / "鉴权" / "版本策略") |
| `§8.5 设计边界` | markdown 小节 | **新增** |
| `§9 数据结构` | markdown 表格 | 列数:6 → 4(移除"字段类型" / "约束" / "索引" / "存储选型") |
| `§9.5 设计边界` | markdown 小节 | **新增** |
| `§10 三方依赖` | markdown 表格 | 列数:7 → 4(移除"版本" / "来源" / "许可" / "活跃度") |
| 模板顶部注释 | markdown 注释 | **追加** 1 行 `> 本模板只覆盖概要设计...` |

### 索引变更

- **不适用**

### 兼容策略

- 模板章节变更**不**影响**既有** 9 个 REQ 的 `design/<REQ>/RESULT.md`(已锁定,**不**追溯)
- 模板章节变更**仅**影响**未来**新 REQ 的 `code-design` 步骤 9A/10A/11A 产出

### 迁移需求

- **不适用**(无数据库 / 无数据迁移)

### 依据规范

- `module-conventions §规则 1`(资源文件放 `templates/`)

## 修改实体:`plan-process-doc-status`(逻辑实体,无持久化)

### 字段变更

| 字段 | 类型 | 约束变更 |
| --- | --- | --- |
| `module-details.md` | enum('可选' \| '必选') | 可选 → **必选** |
| `interface-specs.md` | enum('可选' \| '必选') | 可选 → **必选** |
| `data-changes.md` | enum('可选' \| '必选') | 可选 → **必选** |
| `risk-analysis.md` | enum('可选' \| '必选') | 可选 → **必选** |

### 索引变更

- **不适用**

### 兼容策略

- 既有 9 个 REQ 的 `plan/<REQ>/{module-details,interface-specs,data-changes,risk-analysis}.md` 状态**不**变(已锁定,**不**追溯)
- 本变更**仅**影响**未来**新 REQ 的 `code-plan` 步骤 7A 产出

### 迁移需求

- **不适用**

### 依据规范

- `encoding-conventions §规则 1/3`(任务编号)

## 新增实体:`plan-template-chapter-required-flag`(逻辑实体,无持久化)

### 字段表

| 字段 | 类型 | 约束 | 索引 | 说明 |
| --- | --- | --- | --- | --- |
| chapter | string | PK, `§<N>` | — | 章节编号(§4 ~ §12) |
| required | boolean | NOT NULL, 默认 true | — | 是否必填(本需求前=建议填;本需求后=必填) |
| minContent | string | (required=true 时 NOT NULL) | — | 必填最小内容(如"至少 1 个伪代码块") |
| fallbackText | string | NOT NULL, 默认 "本需求不涉及" | — | 缺省文本(若章节无内容) |

### 关系

- 与 `templates/plan.md` 章节:**一对一**

### 存储选型

- **不适用**

### 迁移脚本

- **不适用**

### 依据规范

- `module-conventions §规则 1`

## 数据生命周期

### 留存期限

- 逻辑实体**不**适用(无持久化)

### 清理/归档策略

- 既有 9 个 REQ 的 design / plan**不**清理(已锁定,作为历史保留)
- 新 REQ 的 design / plan 按既有:`code-publish` 部署后保留;`code-version` 切换后保留

### 备份与恢复策略

- 沿用既有:git 仓库**不**做额外备份(已锁定 git 仓库的备份策略)

## 整体变更摘要

| 实体 | 状态 | 影响范围 |
| --- | --- | --- |
| `check-validation-point` | 新增 | `code-check/SKILL.md` 评审清单追加 3 行 |
| `design-template-chapter` | 修改 | `templates/design.md` 5 个章节 + 1 个注释 |
| `plan-process-doc-status` | 修改 | `code-plan/SKILL.md` 步骤 7A 强约束 |
| `plan-template-chapter-required-flag` | 新增 | `templates/plan.md` §4-§12 9 个章节 |
