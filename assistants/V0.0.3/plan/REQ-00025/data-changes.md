# 数据结构完整变更 — REQ-00025
版本:V0.0.3

## 修改实体:id-prefix × id-suffix → 完整编号

| 字段 | 类型 | 旧约束 | 新约束 | 索引 | 说明 |
| --- | --- | --- | --- | --- | --- |
| `id-prefix` | enum | 4 类(`REQ-` / `BUG-` / `TASK-REQ-` / `TASK-BUG-`)| **不**变 | N/A | 前缀部分,本需求**不**变 |
| `id-suffix` | string | 5 位纯数字 `\d{5}` | 1+ 位字符集 `[A-Za-z0-9.\-_]+` | N/A | 后缀部分,本需求**放宽** |

- 关系:`id-prefix` × `id-suffix` → `完整编号`
- 存储选型:Markdown 目录(本仓库纯文档)
- 迁移脚本:**无**;新正则超集旧正则,既有 `REQ-00020` / `BUG-00001` / `TASK-REQ-00020-00001` 继续可用
- 兼容策略:超集(新 ⊇ 旧)
- 依据规范:`encoding-conventions.md §规则 1`(本需求修订后)

## 新增实体:§规则 1.5 第三方平台前缀登记表

| 字段 | 类型 | 约束 | 索引 | 说明 |
| --- | --- | --- | --- | --- |
| 前缀 | string | 必填,如 `JIRA-` | — | 第三方平台编号前缀 |
| 等价类别 | enum | `REQ` / `BUG` / `TASK-REQ` / `TASK-BUG` 之一 | — | 视为何种类型 |
| 登记时间 | date | ISO 8601 | — | 登记时间戳 |
| 登记人 | string | 必填 | — | 登记人员 |
| 备注 | string | 可选 | — | 补充说明 |

- 关系:N/A(纯文档表)
- 存储选型:Markdown 表格(本仓库纯文档)
- 迁移脚本:N/A
- 依据规范:`encoding-conventions.md §规则 1.5`(本需求新增)
- **初始状态**:空表(由用户按需登记)

## 修改实体:encoding-conventions.md §规则 1 §条款 表(3 行)

- 字段变更:正则列(3 行)+ 容量列(3 行)+ 备注列(3 行)
- 索引变更:N/A
- 迁移需求:**无**;新正则超集旧正则
- 兼容策略:超集
- 依据规范:`encoding-conventions.md §规则 1`(本需求修订后)

## 不修改实体(沿用既有)

- 13 份项目级规范中除 `encoding-conventions.md` 外的 12 份
- 6 个不修改的 SKILL.md(`code-init` / `code-version` / `code-rule` / `code-publish` / `code-auto` / `code-merge`)
- 既有 V0.0.3 看板结构(§任务清单 12 列字段不变)
