# 关联需求 — REQ-00007

更新时间:2026-06-04 13:58

## 扫描范围
- 同版本:`./assistants/V0.0.2/require/`
  - REQ-00004 / REQ-00005 / REQ-00006
- 跨版本:`./assistants/V0.0.1/require/`、`./assistants/V0.0.0/`

## 关联需求清单

### REQ-00005(版本:V0.0.2)— 优化 3 技能,加首步拉取与末步提交
- **关联点**:
  - **被调用的子技能**:`code-require` / `code-design` / `code-plan` 是 `code-auto` 的"前 3 步",均被 REQ-00005 改写
  - **执行次数**:`code-auto` 内部至少会调 `code-require` 1 次 + `code-design` 1 次 + `code-plan` 1 次;**`code-review` 可能产生派生任务 → 触发 `code-it` / `code-unit` 多次执行**
  - **末步提交被重复触发**:每次子技能完成都会触发"末尾兜底提交",即 `code-auto` 一次完整执行可能产生 5~20+ 个 commit
- **对本需求的影响**:
  - **设计侧必决**:`code-auto` 是否在调子技能时**关闭**末步提交(让所有提交由 `code-auto` 末尾统一)?见 clarifications.md Q-5
  - **拉取重复**:每个子技能首步 `git pull`,`code-auto` 一次跑完可能 20+ 次 `git pull`
  - **建议**:本需求落地时,应**复用** REQ-00005 的边界(子技能仍按 REQ-00005 工作);不要求子技能新增"批量模式"
- **来源**:`./assistants/V0.0.2/require/REQ-00005/RESULT.md` §FR-1 / §FR-3

### REQ-00006(版本:V0.0.2)— `/code-publish` 发布部署技能
- **关联点**:
  - **下游衔接**:`code-auto` 是"开发周期自动跑通",`code-publish` 是"开发完成后发布"
  - **本需求完成时,本版本**应**已通过** `code-publish` 的前置检查(需求/任务/缺陷全部"解决")
- **对本需求的影响**:
  - **衔接提示**:`code-auto` 完成时,应**提示**用户调 `code-publish`(Q-6 采纳默认)
  - **不触发** `code-publish`:`code-auto` 自身**不**调 `code-publish`(职责分离)
  - **结果检查**:`code-auto` 完成后,可**建议**用户调 `code-dashboard` 验证状态(同源)
- **来源**:`./assistants/V0.0.2/require/REQ-00006/RESULT.md` §FR-1 / §9 边界

### REQ-00004(版本:V0.0.2)— `/code-dashboard` 开发看板技能
- **关联点**:
  - **本需求产出的"完成"事件**应能被 `code-dashboard` 看到(看板"任务清单"区段更新)
  - **跨需求一致性**:`code-auto` 跑完时,`code-dashboard` 输出的"全版本已完成"应**精确匹配** `code-auto` 报告的"完成"状态
- **对本需求的影响**:
  - **状态同步**:`code-auto` 完成时,看板"任务清单" / "需求清单" 区段必须已被各子技能同步更新
  - **FR-4 的优先级策略**:`code-dashboard` 现有"全完成 → 建议调 `code-version <新版本号>`";本需求落地后,中间应加一步"建议调 `code-publish`"
- **来源**:`./assistants/V0.0.2/require/REQ-00004/RESULT.md` §FR-4 + §NFR-8

### REQ-00003(版本:V0.0.1)— 优化 `code-rule` 技能
- **关联点**:
  - **`code-rule` 维护项目级规范**:本需求**不**创建 `auto-conventions.md`(留作 follow-up)
  - **CLAUDE.md "AI 工作约定"小节**:本需求不追加(留作 follow-up)
- **对本需求的影响**:
  - **不直接写规范**:本需求不创建新规范
  - **建议派生**:本需求评审时可派生"用 `code-rule` 沉淀 `auto-conventions.md`(自动化边界/终止条件/中止开关)"
- **来源**:`./assistants/V0.0.1/require/REQ-00003/RESULT.md` + `commit-conventions.md`(占位)

### REQ-00001(版本:V0.0.1)— Marketplace 改名落地(REVIEW 派生任务样板)
- **关联点**:
  - **`code-review` 派生任务模式**:REQ-00001-005 / REQ-00002-009 是 `code-review` 派生的 2 个任务,展示了"派生 + 关联原任务 + review 来源"模式
  - **`code-auto` 循环中的"派生任务"**会**反复**触发此模式
- **对本需求的影响**:
  - **派生任务可执行性**:`code-auto` 调 `code-it` / `code-unit` 完成派生任务时,需要识别"派生任务"标识(看 PLAN.md 任务总览的"触发/来源"列)
  - **派生任务的 commit**:`code-it` 内部 commit 的 commit message 应包含"审查派生"标识(避免与"需求新增"任务混淆)
- **来源**:`./assistants/V0.0.1/RESULT.md` "派生任务记录"段

### REQ-00002(版本:V0.0.1)— 编码格式统一
- **关联点**(间接):
  - **3 类编码权威源**:`code-auto` 内部会**生成**新 REQ 编码 / 新 TASK 编码,必须遵循 `encoding-conventions.md`
- **对本需求的影响**:
  - **新 REQ 编码生成**:`code-auto` 调 `code-require` 时,需传递"待生成 REQ 编码"作为子技能输入(或由子技能按 §规则 4 流程自取)
  - **新 TASK 编码生成**:`code-plan` 拆分任务时按 §规则 4 自取
  - **新 BUG 编码生成**(由 `code-review` 派生):由 `code-fix` / `code-review` 按规范自取
- **来源**:`./assistants/V0.0.1/require/REQ-00002/RESULT.md` + `./assistants/rules/encoding-conventions.md`

## 跨需求聚合(供 `code-design` 阶段权衡)

| 维度 | 涉及需求 | 共性 | 处理建议 |
| --- | --- | --- | --- |
| 子技能边界 | REQ-00005 | 子技能被 N 次调用,触发重复拉取/重复提交 | `code-auto` 设计"批量模式"开关(Q-5 待定) |
| 上下游衔接 | REQ-00006 / REQ-00004 | `code-auto` 完成 → 建议调 `code-publish` / `code-dashboard` | 在本需求末尾报告阶段加 2 条"后续建议" |
| 派生任务模式 | REQ-00001-005 / REQ-00002-009 | `code-review` 派生任务会反复触发 | 子技能按既有模式处理;`code-auto` 循环中识别 |
| 编码生成 | REQ-00002 | `code-auto` 内部会**生成**新编码 | 严格遵循 `encoding-conventions.md §规则 4` |
| 规范沉淀 | REQ-00003 | 项目级规范由 `code-rule` 维护 | 本需求不直接写规范,留作 follow-up |

## V0.0.0 EXISTING-* 任务
- 项目级 `auto-conventions.md` 在 V0.0.0 不存在(无 EXISTING 任务)
- 本需求是 V0.0.2 中**首次引入** `code-auto` 自动化编排需求
- 与 7 个 `code-*` 技能的关系:`code-auto` 是**编排者**,其他 7 个(及未来的 `code-dashboard` / `code-publish`)**是被调用方**
- 与 Claude Code 自身能力的关系:本需求落地需要 `Skill` 工具的"嵌套调用"支持 — 应在 `code-design` 阶段验证可行性

## 关键事实扫描结果(供 clarifications.md 引用)
- 当前 9 个 `code-*` 技能:`code-version` / `code-require` / `code-design` / `code-plan` / `code-it` / `code-unit` / `code-review` / `code-dashboard` / `code-publish`
- 本需求将引入第 10 个:`code-auto`
- `code-auto` 与其他 9 个的**关系**:**"驱动者"(code-auto) vs "被驱动"(其余 9 个)**
- `code-auto` 与 `code-version` 的关系:`code-auto` 启动时**不**切版本(沿用当前 `.current-version`);与 `code-publish` 关系同上
- 看板"任务清单"区段有"真正可发布"概念(V0.0.1 看板末行)— 是 `code-auto` 完成判定的现成锚点
