# 模块详细化 — REQ-00013
更新时间:2026-06-05 21:30
版本:V0.0.2

## 模块:M-1 `code-require/SKILL.md` 增量追加
- **路径**:`plugins/code-skills/skills/code-require/SKILL.md`
- **关键类/函数**:
  - `truncateTitle(title: string, maxLen: number = 30): string` — 共享工具函数
  - `formatReqTitle(reqNum: string, title: string): string` — 需求标题格式化
  - 内部:在"## 工作流程"前的"## 工具使用约定"段后追加"## 标题解析(REQ-00013 新增)"小节
- **调用顺序**:
  1. `code-require` 启动 → 调 `formatReqTitle(REQ-NNNNN, parseResultTitle())`
  2. 屏幕输出:`正在处理: REQ-NNNNN · <需求标题>`
  3. 各步骤屏幕输出复用 `formatReqTitle`
  4. 完成时屏幕输出:`完成: REQ-NNNNN · <需求标题>`
- **状态归属**:N/A(本模块无状态变更,仅屏幕输出格式升级)
- **与概要设计的对应**:design §3 M-1
- **符合的规范**:`skill-conventions §规则 1` (frontmatter 字节级保留)+ `dashboard-conventions §规则 1` (字段不扩展)

## 模块:M-2 `code-plan/SKILL.md` 增量追加
- **路径**:`plugins/code-skills/skills/code-plan/SKILL.md`
- **关键类/函数**:
  - `truncateTitle` (共享)
  - `formatReqTitle` (共享,用于需求标题)
  - `formatTaskTitle(taskNum: string, title: string): string` — 任务标题格式化
  - 内部:在"## 工作流程"前追加"## 标题解析(REQ-00013 新增)"小节
- **调用顺序**:
  1. `code-plan` 启动 → 调 `formatReqTitle(REQ-NNNNN, parseResultTitle())`
  2. 屏幕输出:`正在处理: REQ-NNNNN · <需求标题>`
  3. 拆分每个任务时 → 调 `formatTaskTitle(TASK-..., parsePlanTaskTitle())`
  4. 屏幕输出:`拆分: TASK-... · <任务标题>`
  5. 完成时屏幕输出:`完成: REQ-NNNNN · <需求标题>(拆 N 个任务)`
- **状态归属**:N/A
- **与概要设计的对应**:design §3 M-2
- **符合的规范**:同 M-1

## 模块:M-3 `code-fix/SKILL.md` 增量追加
- **路径**:`plugins/code-skills/skills/code-fix/SKILL.md`
- **关键类/函数**:
  - `truncateTitle` (共享)
  - `formatBugTitle(bugNum: string, title: string): string` — 缺陷标题格式化
  - 内部:在"## 工作流程"前追加"## 标题解析(REQ-00013 新增)"小节 + 步骤 1 末尾追加"## 缺陷标题生成(REQ-00013 新增)"小节
- **调用顺序**:
  1. `code-fix` 启动 → 调 `formatBugTitle(BUG-NNNNN, parseFixTitle())`
  2. 屏幕输出:`正在处理: BUG-NNNNN · <缺陷标题>`
  3. **新登记时**:用户输入缺陷描述 → 调 `truncateTitle(描述, 30)` → 写入 `fix/<BUG-NNN>/RESULT.md` 顶部"## 缺陷标题"小节
  4. 完成时屏幕输出:`已修复: BUG-NNNNN · <缺陷标题>`
- **状态归属**:`fix/<BUG-NNN>/RESULT.md` 内部新增"## 缺陷标题"小节(本轮唯一新增字段,但**不**写入看板"缺陷清单"区段)
- **与概要设计的对应**:design §3 M-3
- **符合的规范**:同 M-1

## 模块:M-4 `code-it/SKILL.md` 增量追加
- **路径**:`plugins/code-skills/skills/code-it/SKILL.md`
- **关键类/函数**:
  - `truncateTitle` (共享)
  - `formatTaskTitle` (共享)
  - 内部:在"## 工作流程"前追加"## 标题解析(REQ-00013 新增)"小节
- **调用顺序**:
  1. `code-it` 启动 → 调 `formatTaskTitle(TASK-..., parsePlanTaskTitle())`
  2. 屏幕输出:`正在处理: TASK-... · <任务标题>`
  3. 中止时(REQ-00010 守卫)屏幕输出含标题:
     ```
     ⛔ code-it 中止(存在未完成的前置任务)
     正在处理: REQ-NNNNN · <需求标题>(任务 TASK-... · <任务标题>)
     前置任务状态:...
     ```
  4. 完成时屏幕输出:`已完成: TASK-... · <任务标题>`
- **状态归属**:N/A
- **与概要设计的对应**:design §3 M-4
- **符合的规范**:同 M-1

## 模块:M-5 `code-unit/SKILL.md` 增量追加
- **路径**:`plugins/code-skills/skills/code-unit/SKILL.md`
- **关键类/函数**:
  - `truncateTitle` (共享)
  - `formatTaskTitle` (共享)
  - 内部:在"## 工作流程"前追加"## 标题解析(REQ-00013 新增)"小节
- **调用顺序**:
  1. `code-unit` 启动 → 调 `formatTaskTitle(TASK-..., parsePlanTaskTitle())`
  2. 屏幕输出:`正在处理: TASK-... · <任务标题>`
  3. 守卫跳过时(REQ-00009)屏幕输出:`⏭ code-unit 跳过: TASK-... · <任务标题>(项目不可测)`
  4. 完成时屏幕输出:`已运行-通过/失败: TASK-... · <任务标题>`
- **状态归属**:N/A
- **与概要设计的对应**:design §3 M-5
- **符合的规范**:同 M-1

## 模块:M-6 `code-review/SKILL.md` 增量追加
- **路径**:`plugins/code-skills/skills/code-review/SKILL.md`
- **关键类/函数**:
  - `truncateTitle` (共享)
  - `formatReqTitle` (共享)
  - `formatTaskTitle` (共享)
  - 内部:在"## 工作流程"前追加"## 标题解析(REQ-00013 新增)"小节
- **调用顺序**:
  1. `code-review` 启动 → 调 `formatReqTitle(REQ-NNNNN, parseResultTitle())`
  2. 屏幕输出:`正在处理: REQ-NNNNN · <需求标题>`
  3. 派生任务时:写入 `PLAN.md` 任务总览"标题"列 ≤ 30 字(D-5 选定 A)
  4. 完成时屏幕输出:`已评审: REQ-NNNNN · <需求标题>(N 条发现)`
- **状态归属**:N/A(派生任务的"标题"列由 `code-review` 写入时即截断,下游消费方零感知)
- **与概要设计的对应**:design §3 M-6
- **符合的规范**:同 M-1

## 模块:M-7 `code-auto/SKILL.md` 增量追加
- **路径**:`plugins/code-skills/skills/code-auto/SKILL.md`
- **关键类/函数**:
  - `truncateTitle` (共享)
  - `formatReqTitle` (共享,需求场景)
  - `formatTaskTitle` (共享,任务场景)
  - `formatBugTitle` (共享,缺陷场景)
  - 内部:在"## 屏幕报告格式"前追加"## 标题预读(REQ-00013 新增)"小节
- **调用顺序**:
  1. `code-auto` 步骤 1/2/3/5:调子技能前 → 读 `require/<REQ-NNNNN>/RESULT.md` 第 1 行 → 调 `formatReqTitle(REQ-NNNNN, parseResultTitle())`
  2. `code-auto` 步骤 4/6:调子技能前 → 读 `plan/<REQ-NNNNN>/PLAN.md` 任务总览"标题"列 → 调 `formatTaskTitle(TASK-..., parsePlanTaskTitle())`
  3. `code-auto` 步骤 6 派生:调子技能前 → 读 `fix/<BUG-NNNNN>/RESULT.md` "## 缺陷标题" → 调 `formatBugTitle(BUG-NNNNN, parseFixTitle())`
  4. 屏幕输出:`[code-auto] 步骤 N/M:code-require REQ-NNNNN · <需求标题>`
- **状态归属**:N/A
- **与概要设计的对应**:design §3 M-7
- **符合的规范**:同 M-1
- **关键契约**:子技能零修改契约保持(D-8 选定 A)— `code-auto` 自读"标题"源,不向子技能传任何参数

## 模块:M-8 `code-publish/SKILL.md` 增量追加
- **路径**:`plugins/code-skills/skills/code-publish/SKILL.md`
- **关键类/函数**:
  - `truncateTitle` (共享)
  - `formatReqTitle` / `formatTaskTitle` / `formatBugTitle` (共享)
  - 内部:在 "PreflightChecker" 章节末尾追加"## 报告格式升级(REQ-00013 新增)"小节
- **调用顺序**:
  1. `code-publish` PreflightChecker 检测"未完成项"时 → 调 `parseResultTitle()` / `parsePlanTaskTitle()` / `parseFixTitle()`
  2. 拼接"编号+标题"到"未完成项"行:
     - 原:`REQ-NNNNN 状态=...`
     - 新:`REQ-NNNNN · <需求标题> 状态=...`
- **状态归属**:N/A
- **与概要设计的对应**:design §3 M-8
- **符合的规范**:NFR-5;FR-10.AC-10.2
