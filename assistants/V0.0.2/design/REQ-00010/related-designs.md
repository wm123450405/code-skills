# 关联概要设计 — REQ-00010

更新时间:2026-06-06 12:00
版本:V0.0.2
需求编码:REQ-00010

## 同版本关联设计(`./assistants/V0.0.2/design/*/RESULT.md`)

| 关联设计 | 关联点 | 对本设计的影响 |
| --- | --- | --- |
| **REQ-00005** `code-require` / `code-design` / `code-plan` 首步拉取 | "首步拉取"位置 = 各技能步骤 0 之前 | 本设计沿用:守卫作为 `code-it` 步骤 0a(在版本上下文检测之前) |
| **REQ-00007** `code-auto` 任务循环 | `code-auto` 按"任务总览区段行序"调 `code-it` | NFR-4:本需求守卫作为"双保险";`code-auto` 调用下守卫**总是通过** |
| **REQ-00009** `code-unit` 守卫 | `code-unit` 守卫 = "步骤 0a"模式 | NFR-2:本需求守卫与 `code-unit` 守卫结构一致(同是"步骤 0a"模式) |
| **REQ-00013** `code-it` 标题解析 | `code-it` §"标题解析"工具函数(标题解析 / 格式化 / 截断) | 本设计**复用** REQ-00013 的 `parsePlanTaskTitle()` / `formatTaskTitle()` / `truncateTitle()` |
| **REQ-00017** `code-it` 步骤 14.5 推进看板 | `code-it` 步骤 14.5 把"推进看板"职责显式化 | 锚点参照:本设计不修改步骤 14.5 既有逻辑;本设计新追加的"步骤 0a"在更前面 |

## 跨版本关联设计(可选,`./assistants/*/design/*/RESULT.md`)

| 关联设计 | 关联点 | 影响 |
| --- | --- | --- |
| **REQ-00003**(V0.0.1)`code-rule` 维护项目级规范 | `code-rule` 维护 `rules/` 目录 | 本需求**不**直接调用 `code-rule`;FR-5.AC-5.4/5.5 明确不修改 `dashboard-conventions.md` 与 `commit-conventions.md` 规则 1 |

## 关联点详细分析

### 与 REQ-00013(标题解析)协同
- **复用点**:`parsePlanTaskTitle()` 解析任务标题
- **复用点**:`formatTaskTitle()` 格式化"任务编码 · 标题"
- **复用点**:`truncateTitle()` 截断 > 30 字符标题
- **本设计新增**:`code-it` 中止报告中的"前置任务状态清单"使用 `formatTaskTitle()` 格式化
- **本设计新增**:守卫算法中调用 `parsePlanTaskTitle()` 取当前任务与前置任务标题
- **协同约束**:**不**修改 REQ-00013 既有小节(本设计新增小节在 REQ-00013 小节**之后**追加,见"插入位置"段)

### 与 REQ-00007(`code-auto` 任务循环)协同
- **现状**:`code-auto` 按"任务总览区段行序"调 `code-it`(FR-4.AC-4.3)
- **本设计引入**:`code-it` 步骤 0a 守卫按相同行序判定前置
- **协同**:`code-auto` 按序调 `code-it` → 步骤 0a 守卫**总是通过**(前置任务已完成);`code-auto` 调用下守卫**不**触发中止
- **不冲突**:`code-auto` 现行 FR-4.AC-4.3 的"按序"逻辑**不**变(FR-4.AC-4.2)
- **价值**:本需求守卫作为"双保险"—— 用户手动乱序调 `code-it` 时仍被守卫拦截

### 与 REQ-00009(`code-unit` 守卫)协同
- **现状**:`code-unit` 也有"步骤 0a"守卫(本设计未读其细节,沿用"步骤 0a 模式"惯例)
- **本设计引入**:`code-it` 也用"步骤 0a"守卫
- **协同**:`code-it` 与 `code-unit` 同构,符合 NFR-2 强约束

## 关联设计无冲突确认
- ✅ 不修改任何已发布设计的章节
- ✅ 不修改 `code-it` 既有"步骤 0 ~ 16"与"缺陷分支 17 ~ 25"
- ✅ 不修改 `code-auto` 现行"按序调 code-it"逻辑
- ✅ 不修改 `code-unit` / `code-publish` / `code-dashboard` / `code-review` 现有逻辑
