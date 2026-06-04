# 关联需求 — REQ-00008

更新时间:2026-06-04 14:06

## 扫描范围
- 同版本:`./assistants/V0.0.2/require/`
  - REQ-00004 / REQ-00005 / REQ-00006 / REQ-00007
- 跨版本:`./assistants/V0.0.1/require/`(含 V0.0.1 真实 `code-review` 评审产物,可作为"现有行为"参考)
- 直接相关:`./assistants/V0.0.1/review/REVIEW-REPORT.md`(原模式产物)

## 关联需求清单

### REQ-00007(版本:V0.0.2)— `/code-auto` 自动开发技能
- **关联点**:
  - **被高频调用的子技能**:`code-review` 是 `code-auto` 评审循环的"主角"
  - **`code-auto` 的 FR-5 评审循环**只消费"必须改列表"字段(从 `REVIEW-REPORT.md` 解析)
  - **本需求落地的"整版本模式"**会让 `code-auto` 内部出现"模式选择"问题:`code-review` (无参) vs `code-review REQ-NNNNN`
- **对本需求的影响**:
  - **`code-auto` 内部需识别**:`code-review` 整版本模式产生的 REPORT 格式 vs 单需求模式产生的 REPORT 格式必须**对 `code-auto` 友好**(即都能解析"必须改列表")
  - **设计侧建议**:**REPORT 顶层结构完全一致**,仅数据项聚合方式不同(整版本 = N 个单需求的并集)
  - **派生任务影响**:整版本模式若支持派生任务,需在 `PLAN.md` 任务总览中追加任务(可能跨多个 `REQ-NNNNN` 的 `PLAN.md`);考虑复杂度,Q-3 锁定 A 优先
- **来源**:`./assistants/V0.0.2/require/REQ-00007/RESULT.md` §FR-5 / §NFR-4

### REQ-00006(版本:V0.0.2)— `/code-publish` 发布部署技能
- **关联点**:
  - **`code-publish` 的前置检查**是"全版本需求/任务/缺陷全部解决"
  - **`code-review` 整版本模式**可作为"发布前最后一次全量评审"的工具
  - **`code-publish` 完成后**不再调 `code-review`(评审应在发布前)
- **对本需求的影响**:
  - **衔接提示**:`code-review` 整版本模式完成时,若"无必须改",可提示"建议调 `code-publish`"
  - **不修改** `code-publish` 边界
- **来源**:`./assistants/V0.0.2/require/REQ-00006/RESULT.md` §FR-1 / §9 边界

### REQ-00005(版本:V0.0.2)— 优化 3 技能,加首步拉取与末步提交
- **关联点**:
  - **修改范围不含 `code-review`**:REQ-00005 只改 3 个技能,`code-review` 不在其列
  - **本需求**仅扩展 `code-review` 的"无参数模式",不改 `code-review` 的"单需求模式"
- **对本需求的影响**:
  - **遵循既有边界**:本需求**不**触发 REQ-00005 的"首步拉取+末步提交"扩展到 `code-review`
  - **若 `code-auto` 调用本模式**,会按 `code-review` 原有行为运行(无首步拉取/无末步提交)
  - **建议派生**:在 `code-review REQ-00008` 阶段,可派生"把 `code-review` 也加入 REQ-00005 的'首步拉取+末步提交'"任务(由用户决定)
- **来源**:`./assistants/V0.0.2/require/REQ-00005/RESULT.md` §NFR-4 / §NFR-9

### REQ-00004(版本:V0.0.2)— `/code-dashboard` 开发看板技能
- **关联点**:
  - **同一看板 3 区段数据源**:`code-review` 整版本模式与 `code-dashboard` 同样消费"整个版本的状态"
  - **`code-dashboard` 现有"全完成"建议**是"调 `code-version`",本需求落地后中间可加一步"建议调 `code-review`(整版本模式)"
- **对本需求的影响**:
  - **不修改 `code-dashboard`**:本需求不触发 `code-dashboard` 升级
  - **数据格式兼容**:`code-review` 整版本模式输出应能被 `code-dashboard` 解析(若 dashboard 后续升级支持)
- **来源**:`./assistants/V0.0.2/require/REQ-00004/RESULT.md` §FR-4 / §NFR-8

### REQ-00001(版本:V0.0.1)— `code-review` 单需求模式的历史产物
- **关联点**(直接):
  - **现有 `code-review` 单需求模式的产物**:`./assistants/V0.0.1/review/REQ-00001/REVIEW-REPORT.md`(存在),`./assistants/V0.0.1/review/REQ-00001-005/RESULT.md`(派生任务的修改要求)
  - **本需求是"扩展"而非"替代"**:用户原文"增加不传入参数的模式" — 明确为"模式扩展",现有"传入 `REQ-NNNNN`"模式保留
- **对本需求的影响**:
  - **本需求是 V0.0.1 起 `code-review` 的第 2 种调用模式**:
    - 模式 1(已有):`code-review REQ-NNNNN` → 评审单需求
    - 模式 2(本需求):`code-review`(无参) → 评审整版本
  - **REVIEW-REPORT.md 路径**:
    - 模式 1:`./assistants/<版本号>/review/REQ-NNNNN/REVIEW-REPORT.md`
    - 模式 2:待定(Q-3 锁定);候选 A:同单需求模式路径,但 N 份分别生成;候选 B:`./assistants/<版本号>/review/ALL/REVIEW-REPORT.md`(聚合)
- **来源**:`./assistants/V0.0.1/review/REQ-00001/REVIEW-REPORT.md`(直接扫描)

### REQ-00003(版本:V0.0.1)— 优化 `code-rule` 技能
- **关联点**(间接):
  - **`code-rule` 维护项目级规范**:`code-review` 评审清单的权威源是 `./assistants/rules/`(项目级共享)
  - **本需求**不主动写新规范
- **对本需求的影响**:
  - **不直接写规范**:本需求不创建 `review-conventions.md`(留作 follow-up)
  - **建议**:本需求评审时,可派生"用 `code-rule` 沉淀 `review-conventions.md`(整版本模式的检查清单)"任务
- **来源**:`./assistants/V0.0.1/require/REQ-00003/RESULT.md`

### REQ-00002(版本:V0.0.1)— 编码格式统一
- **关联点**(间接):
  - **`encoding-conventions.md`**:派生任务的 `TASK-...` 编码遵循规范
- **对本需求的影响**:
  - **不强相关**:本需求不直接产生新编码
  - **派生任务场景**:若 Q-3 锁定 A 后整版本模式支持派生任务,新 `TASK-` 编码按规范生成
- **来源**:`./assistants/V0.0.1/require/REQ-00002/RESULT.md`

## 跨需求聚合(供 `code-design` 阶段权衡)

| 维度 | 涉及需求 | 共性 | 处理建议 |
| --- | --- | --- | --- |
| 模式共存 | REQ-00001 | 现有单需求模式 + 本需求整版本模式 | REPORT 顶层结构完全一致(Q-3 锁定 A),仅数据项聚合方式不同 |
| 编排协同 | REQ-00007 | `code-auto` 评审循环的高频调用 | 整版本模式输出对 `code-auto` 友好(可解析"必须改列表") |
| 上游衔接 | REQ-00006 | `code-publish` 前置检查 | 完成时提示"建议调 `code-publish`" |
| 边界继承 | REQ-00005 | `code-review` 不在改写范围 | 本需求**不**触发 REQ-00005 扩展到 `code-review`(留作 follow-up) |
| 状态可视化 | REQ-00004 | 同一看板 3 区段数据源 | 整版本模式输出应能被 dashboard 解析 |
| 规范沉淀 | REQ-00003 | 项目级规范由 `code-rule` 维护 | 本需求不直接写 `review-conventions.md`(留作 follow-up) |

## V0.0.0 EXISTING-* 任务
- `code-review` 技能在 V0.0.0 已存在(7 个 `code-*` 之一),本需求是 V0.0.1 起"REVIEW-REPORT.md"模式基础上的"模式扩展"
- 历史上 **`code-review` 只支持单需求模式**;V0.0.0 ~ V0.0.1 中所有评审产物(REQ-00001 / REQ-00002 / REQ-00003)都是"单需求模式"产物
- 本需求是**首次**在 V0.0.2 中引入"整版本模式"扩展

## 关键事实扫描结果(供 clarifications.md 引用)
- 现有 `code-review` 评审产物(2026-06-04 14:06 扫描):
  - `./assistants/V0.0.1/review/REQ-00001/REVIEW-REPORT.md` — 2 条发现(F-1/F-2)
  - `./assistants/V0.0.1/review/REQ-00002/REVIEW-REPORT.md` — 3 条发现(F-3/F-4/F-5)
  - `./assistants/V0.0.1/review/REQ-00003/REVIEW-REPORT.md` — 1 条发现(F-6)
  - `./assistants/V0.0.1/review/REQ-00001-005/RESULT.md` — 派生任务 1 的修改要求
  - `./assistants/V0.0.1/review/REQ-00002-009/RESULT.md` — 派生任务 2 的修改要求
- 模式 1(单需求)产物路径已固定;模式 2(整版本)产物路径需在本需求中**新定**
- V0.0.2 当前已有 4 个需求(REQ-00004/00005/00006/00007),均处于"需求分析"阶段,**尚无任何 `code/` 目录下的代码改修正文**
- 整版本模式在 V0.0.2 当前**没有可评审的代码**(无任务完成),需要明确"无代码可评审"的退化行为
