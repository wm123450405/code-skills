# 材料登记 — REQ-00013
更新时间:2026-06-05 21:30
版本:V0.0.2

## 项目级规范
(沿用 `design/REQ-00013/materials-index.md` §项目级规范,本计划阶段无新增/修改)

## 上游需求
- 来源:./assistants/V0.0.2/require/REQ-00013/RESULT.md
- 版本:v1(2026-06-04 15:25)
- 提取的 FR / NFR / AC 数量:11 FR / 10 NFR / ~30 AC / 9 边界场景
- 关键交叉点(每条 FR 对应的设计章节):
  - FR-1 → design §1.4 D-1 多源派生(标题已存在)
  - FR-2 → design §1.1 D-2 6 技能统一格式
  - FR-3 → design §3 M-1 `code-require` 增量追加
  - FR-4 → design §3 M-2 `code-plan` 增量追加
  - FR-5 → design §3 M-3 `code-fix` 增量追加(本轮新增"## 缺陷标题"小节)
  - FR-6 → design §3 M-4 `code-it` 增量追加
  - FR-7 → design §3 M-5 `code-unit` 增量追加
  - FR-8 → design §3 M-6 `code-review` 增量追加(派生任务标题截断)
  - FR-9 → design §3 M-7 `code-auto` 增量追加
  - FR-10 → design §3 M-8 `code-publish` 协同 + `code-dashboard` 不改
  - FR-11 → design §1.2 范围(0 修改 marketplace / plugin / rules / templates)

## 上游概要设计
- 来源:./assistants/V0.0.2/design/REQ-00013/RESULT.md
- 版本:v1(2026-06-05 21:00)
- 提取的模块拆分 / 接口概要 / 数据结构 / 决策:
  - **模块拆分**:M-1~M-8 共 8 个 SKILL.md 增量追加(7 技能 + 1 协同),锚点统一为"## 工作流程"前 / 步骤 1 末尾 / PreflightChecker 末尾
  - **接口概要**:`truncateTitle(title, maxLen=30)` + `formatReqTitle(reqNum, title)` + `formatTaskTitle(taskNum, title)` + `formatBugTitle(bugNum, title)` 4 个共享工具函数;6 技能调用
  - **数据结构**:NFR-2 0 新增字段;`code-fix` "## 缺陷标题"小节在 `fix/.../RESULT.md` 内部
  - **决策**:8 项设计决策 D-1~D-8 全部锁定,详 `design/.../design-notes.md`

## 项目现状(实现细节)

### 命名风格
- SKILL.md 章节标题:`##` 一级 + `###` 二级
- 锚点:行号禁用,使用章节标题或子节标题(详 SKILL.md 中 `## 工作流程` / `## 工具使用约定` / `## 输入` / `## 输出`)
- 函数命名:沿用既有 JavaScript camelCase(如 `truncateTitle`)

### 错误模型
- 屏幕输出风格:`⛔` (中止)/ `✗` (失败)/ `✓` (成功)/ `⚠` (警告)
- 退出码:`code-*` 技能统一 0(成功)或非 0(失败/中止)
- `code-auto` 子技能零修改契约(D-8 选定 A):不向子技能传任何参数

### 既有相似功能
- REQ-00005:`code-require` / `code-design` / `code-plan` 步骤 0a + 步骤 N 末尾兜底提交(本设计沿用增量追加模式)
- REQ-00008:`code-review` 步骤 1.5 模式选择 + 步骤 2 整版本模式 + 步骤 3 退化报告(本设计沿用增量追加模式)
- REQ-00009:`code-unit` 步骤 0a 项目可测性检查守卫(本设计沿用增量追加模式)
- REQ-00010:`code-it` 步骤 0a 前置任务检查守卫(本设计沿用增量追加模式)
- REQ-00011:`code-design` / `code-plan` 步骤 0b 设计目标确认(本设计沿用增量追加模式)
- REQ-00014:`code-plan` §10A 改写"按功能点拆分" + 架构任务 + 生效范围(本设计沿用拆分准则)
- REQ-00017:`code-plan` 步骤 10A 拆任务约束(实际产出候选集 6 项,看板更新不在内)+ `code-it` 末尾兜底后 P-1 推进看板(本设计严守拆任务约束)

### 既有测试用例
- 0(本仓库无构建/测试文件,`code-unit` 守卫判定"不可测")

### 可复用的工具函数/中间件
- `truncateTitle` / `formatReqTitle` / `formatTaskTitle` / `formatBugTitle`:本设计新增,各 SKILL.md 内伪代码完整化
- 沿用:`code-review` 派生任务追加锚点(本设计派生任务"标题"列截断)
- 沿用:`code-auto` 屏幕日志格式(本设计 M-7 沿用 `[code-auto] 步骤 N/M:` 格式)
- 沿用:`code-publish` PreflightChecker 解析逻辑(本设计 M-8 复用既有解析,新增 1 次文件 I/O)

## 本次变更源(增量更新时)
N/A(本计划为首次规划)
