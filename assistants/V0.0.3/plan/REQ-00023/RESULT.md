# 详细设计 — REQ-00023(简化 /code-dashboard 总览模式 4 段输出)

- 需求编码:REQ-00023
- 所属版本:V0.0.3
- 上游需求:./assistants/V0.0.3/require/REQ-00023/RESULT.md
- 上游概要设计:./assistants/V0.0.3/design/REQ-00023/RESULT.md
- 遵循规范:./assistants/rules/ 下 13 个文件(零触发 dashboard-conventions §规则 1,零触发 skill-conventions §规则 1)
- 创建时间:2026-06-07

## 1. 概述

本详细设计把概要设计"4 段精简输出"落地为可直接编码的算法(算法 1 ~ 4)+ 接口契约 + 数据结构 + 边界处理 + 任务拆分。

**核心范围**:**只**改 `plugins/code-skills/skills/code-dashboard/SKILL.md` 1 个文件,其他 12 个 `code-*` 技能 SKILL.md frontmatter 字节级保留(沿用 NFR-6)。零新增模块,零新增文件,零新增依赖,零新增看板字段(沿用 INV-1 ~ INV-9)。

**预估净变化**:`code-dashboard/SKILL.md` +20~+30 行(沿用 REQ-00021 NFR-5.1 经验值)。

## 2. 上游引用

### 2.1 需求引用
- 来源:./assistants/V0.0.3/require/REQ-00023/RESULT.md
- 6 FR / 9 NFR / 8 AC / 9 INV / 3 待澄清 Q
- 关键 FR:
  - FR-1:总览模式 4 段精简
  - FR-2:总开发进度计算公式
  - FR-3:5 类状态判定规则
  - FR-4:各状态数量占比
  - FR-5:每状态 1 条推荐
  - FR-6:高优先级缺陷段保留

### 2.2 概要设计引用
- 来源:./assistants/V0.0.3/design/REQ-00023/RESULT.md
- 6 决策 D-1 ~ D-6
- 关键决策:总览模式限定改造 / 加权平均 / 5 类状态派生 / 每状态 1 条 / 保留 P0/P1 / 仍只读

### 2.3 规范遵循
- 13 份规范全部沿用,零触发三同步(INV-1 ~ INV-9 锁定)

## 3. 模块详细化

### 3.1 唯一改造对象:`code-dashboard/SKILL.md`

| 小节 | 改造 | 备注 |
| --- | --- | --- |
| frontmatter L1-3 | 字节级保留 | INV-1 |
| `## 目标` | 微调 1 段 1 句 | 补充"总览模式已精简" |
| `## 适用场景` | +1 行 | 标注总览已简化 |
| `## 不适用` | 沿用 | 0 改 |
| `## 工作目录约定` | 沿用 | 0 改 |
| `## 输入` | 沿用 | 0 改 |
| `## 输出` | **核心改造** | 总览模式 4 段重定义 |
| `## 工具使用约定` | 沿用 | 0 改 |
| `## 工作流程` | **核心改造** | 步骤 4 段 1-4 改造 |
| `## 边界与异常` | 微调 | L1 / L2 / L3 / E-1 ~ E-10 |
| `## 衔接` | +1 行 | 标注已简化 |
| `## 不要做的事` | 沿用 | 0 改 |
| `## 附录 A 任务编号解析` | 沿用 | 0 改 |
| `## 附录 B ASCII 比例条` | 沿用 | 0 改 |
| `## 附录 C 建议数据结构` | 微调 | Suggestion 字段不变,补 1 段 |
| `## 变更记录` | +1 行 | 追加本次变更 |

## 4. 算法与逻辑(算法 1 ~ 4)

### 4.1 算法 1:总开发进度计算(沿用概要设计 §5.1)

```ts
function calcTotalProgress(
  requirements: RequirementRow[],
  bugs: BugRow[],
  tasks: TaskRow[],
  reviews: ReviewRow[]
): { progress: number | null; bar: string } {
  let totalDone = 0
  let totalExpected = 0

  // 需求类(6 步)
  for (const req of requirements) {
    totalExpected += 6
    if (req.requireDocLink)        totalDone += 1  // 需求分析
    if (req.designDocLink)         totalDone += 1  // 概要设计
    if (req.planDocLink)           totalDone += 1  // 详细设计
    if (req.allTasksDevDone)       totalDone += 1  // 编码
    if (req.allTasksTestOkOrNA)    totalDone += 1  // 单元测试
    if (req.reviewPassed)          totalDone += 1  // 代码评审
  }

  // 缺陷类(5 步)
  for (const bug of bugs) {
    totalExpected += 5
    if (bug.isReported)            totalDone += 1  // 缺陷登记
    if (bug.fixPlanLink)           totalDone += 1  // 详细设计
    if (bug.allTasksDevDone)       totalDone += 1  // 编码
    if (bug.allTasksTestOkOrNA)    totalDone += 1  // 单元测试
    if (bug.reviewPassed)          totalDone += 1  // 代码评审
  }

  if (totalExpected === 0) {
    return { progress: null, bar: "— / 无需求无缺陷,无需进度" }
  }

  const pct = Math.round((totalDone / totalExpected) * 100)
  return { progress: pct, bar: renderBar(pct) }  // 沿用附录 B 算法 5
}
```

**约束**:
- 退化:分母 = 0 → 屏显 `— / 无需求无缺陷,无需进度`
- "不适用"环节按已完成计入(AC-1.3 锁定)

### 4.2 算法 2:5 类状态判定(沿用概要设计 §5.2)

```ts
type DashboardState =
  | "待概要设计"
  | "待详细设计"
  | "待代码开发"
  | "待单元测试"
  | "待代码评审"
  | "已完成"  // 隐含
  | "已取消"  // 隐含
  | "阻塞"    // 隐含

function classifyState(item: Item, allTasks: TaskRow[], reviews: ReviewRow[]): DashboardState {
  if (item.type === "requirement") {
    if (!item.designDocLink) return "待概要设计"
    if (!item.planDocLink)   return "待详细设计"
    if (!allTasksDevDone(item)) return "待代码开发"
    if (hasTaskWithoutTest(item)) return "待单元测试"
    if (hasMustFixUnprocessed(item, reviews)) return "待代码评审"
    return "已完成"
  }
  // 缺陷类(不进入"待概要设计")
  if (item.type === "bug") {
    if (!item.fixPlanLink) return "待详细设计"
    if (!allTasksDevDone(item)) return "待代码开发"
    if (hasTaskWithoutTest(item)) return "待单元测试"
    if (hasMustFixUnprocessed(item, reviews)) return "待代码评审"
    return "已完成"
  }
  return "已完成"
}
```

**约束**:
- E-7:同需求同时属"待代码开发"+"待单元测试" → 归入"待代码开发"
- 缺陷跳过"待概要设计"(从登记直接进入"修复方案")

### 4.3 算法 3:5 类状态计数(沿用概要设计 §5.3)

```ts
function buildBreakdown(items: Item[]): BreakdownRow[] {
  const total = items.length
  const stateOrder: DashboardState[] = [
    "待概要设计", "待详细设计", "待代码开发", "待单元测试", "待代码评审"
  ]
  const result: BreakdownRow[] = []
  for (const s of stateOrder) {
    const reqCount = items.filter(i => i.type === "requirement" && i.state === s).length
    const bugCount = items.filter(i => i.type === "bug" && i.state === s).length
    if (reqCount + bugCount === 0) continue  // AC-3.3
    const pct = total === 0 ? 0 : Math.round((reqCount + bugCount) / total * 1000) / 10
    result.push({ state: s, reqCount, bugCount, pct })
  }
  return result
}
```

**约束**:
- 0/0 行不展示
- 占比保留 1 位小数
- 5 行占比加和 ≈ 100%(允许 0.1% 四舍五入)

### 4.4 算法 4:后续操作建议生成(沿用概要设计 §5.4)

```ts
function buildSuggestions(items: Item[], allTasks: TaskRow[]): Suggestion[] {
  const suggestions: Suggestion[] = []
  const push = (state: DashboardState, command: string, reason: string) => {
    suggestions.push({ command, reason, priority: "中" })
  }

  // 1. 待概要设计(只走需求路径)
  const r1 = items.find(i => i.type === "requirement" && i.state === "待概要设计")
  if (r1) push("待概要设计", `/code-design ${r1.id}`, `${r1.id} 在"待概要设计"状态`)

  // 2. 待详细设计
  const r2 = items.find(i => i.state === "待详细设计")
  if (r2) push("待详细设计", `/code-plan ${r2.id}`, `${r2.id} 在"待详细设计"状态`)

  // 3. 待代码开发
  const r3 = items.find(i => i.state === "待代码开发")
  if (r3) {
    const firstTask = firstUndoneTask(r3)  // 沿用既有算法 4 解析
    push("待代码开发", `/code-it ${firstTask.id}`, `${r3.id} 在"待代码开发"状态,首个未完成任务 ${firstTask.id}`)
  }

  // 4. 待单元测试
  const r4 = items.find(i => i.state === "待单元测试")
  if (r4) {
    const firstTestTask = firstTaskWithoutTest(r4)
    push("待单元测试", `/code-unit ${firstTestTask.id}`, `${firstTestTask.id} 开发完成,测试未通过`)
  }

  // 5. 待代码评审
  const r5 = items.find(i => i.state === "待代码评审")
  if (r5) {
    // 缺陷走 code-check <REQ>(code-check 现有契约只接 REQ)
    const reqId = r5.type === "bug" ? r5.relatedReq : r5.id
    push("待代码评审", `/code-check ${reqId}`, `${reqId} 任务全部完成,评审发现"必须改"未处理`)
  }

  return suggestions.slice(0, 5)  // AC-4.3 严格 5 行上限
}
```

**约束**:
- AC-4.2:同状态需求 + 缺陷并存 → 1 条(需求路径优先)
- AC-4.5:每条命令**严格**按既有 10 个 `code-*` SKILL.md frontmatter 真实语法

## 5. 数据结构(派生,**不**落盘,**不**新增字段)

| 字段 | 既有位置 | 本需求用途 |
| --- | --- | --- |
| 需求清单."概要设计"列 | 看板(沿用) | 判定"待概要设计" |
| 需求清单."详细设计"列 | 看板(沿用) | 判定"待详细设计" |
| 任务清单."开发状态"列 | 看板(沿用) | 判定"待代码开发 / 单元测试" |
| 任务清单."测试状态"列 | 看板(沿用) | 判定"待代码评审" |
| 缺陷清单."状态"列 | 看板(沿用) | 判定缺陷分类 |
| 评审发现汇总."级别" + "状态"列 | 看板(沿用) | 判定"待代码评审"(是否有"必须改"未处理) |

**新增派生类型**(内存中,**不**落盘):
```ts
type Item = { type: "requirement" | "bug"; id: string; state: DashboardState }
type BreakdownRow = { state: DashboardState; reqCount: number; bugCount: number; pct: number }
type Summary = {
  totalProgress: number | null
  bar: string
  stateBreakdown: BreakdownRow[]
  p0Count: number
  p1Count: number
  suggestions: Suggestion[]
}
```

## 6. 接口细节(沿用概要设计 §3,**不**新增 CLI flag)

### 6.1 总览模式 4 段输出契约

```
总开发进度
──────────
[████████░░░░] 67%

各状态数量占比
──────────────
待概要设计: 需求 2 / 缺陷 0(占比 50.0%)
待代码开发: 需求 1 / 缺陷 0(占比 25.0%)
待代码评审: 需求 1 / 缺陷 0(占比 25.0%)

高优先级缺陷
───────────
P0 待修复: █ 1
P1 待修复: ▓ 0

后续操作建议
────────────
> 建议: /code-design REQ-00023
> 依据: REQ-00023 在"待概要设计"状态
> 优先级: 中
```

### 6.2 屏显宽字符

- `█` (U+2588) / `░` (U+2591) / `▓` (U+2593)— 沿用既有 ASCII 比例条算法 5
- 12 字符固定宽度

## 7. 异常处理(沿用概要设计 §6 + 既有 §边界与异常 段)

详见概要设计 §6(本节不重复列出 10 条 E-1 ~ E-10,沿用)。

## 8. 安全要求

- 零新增外部输入(只读 `RESULT.md`),无注入风险
- 屏显只读,无文件副作用
- `git status --porcelain` 退出后应保持 clean(沿用 FR-7 AC-7.1)

## 9. 状态机/流程

```
启动 → 步骤 0 读 .current-version
  → 步骤 1 解析参数(无参=总览模式)
  → 步骤 2 Read <版本号>/RESULT.md
  → 步骤 3 区段解析(算法 1)
  → 步骤 4 聚合 + 渲染
    ├── 段 1 总开发进度(算法 1 calcTotalProgress)
    ├── 段 2 5 类状态数量占比(算法 2 classifyState + 算法 3 buildBreakdown)
    ├── 段 3 高优先级缺陷(沿用既有)
    └── 段 4 后续操作建议(算法 4 buildSuggestions)
  → 步骤 5 屏显 → 退出
```

## 10. 性能与资源

- 屏显总行数 ≤ 12 行(NFR-1 强约束;退化场景 ≤ 6 行)
- 单遍扫描主看板文本(沿用既有 §工作流程 步骤 3)
- NFR-1 验收:有需求有缺陷 + 5 类状态全部触发 → ≤ 12 行

## 11. 测试要点

- 单元测试:**不适用**(纯文档/屏显类技能,无源码改动)
- 集成测试:**不适用**(沿用 REQ-00021 / REQ-00022 既有模式)
- 端到端:人工在 REPL 中调 `/code-dashboard` 对比屏显
- 验证用例:见上游需求 §6 AC-1 ~ AC-8(8 类 30+ 验收点)

## 12. 规范遵循

- dashboard-conventions §规则 1:**不**触发(零新增看板字段)
- skill-conventions §规则 1:**不**触发(frontmatter 字节级保留)
- module-conventions §规则 1:**不**触发(零新增模块)
- encoding-conventions §规则 1+3:沿用(任务编号双格式透传)

## 13. 待澄清 / 未决项(继承上游)

| 编号 | 描述 | 选定方案 |
| --- | --- | --- |
| Q-1 | 5 类状态判定时,同状态需求 + 缺陷并存,推荐命令选需求路径还是缺陷路径? | **需求路径优先**(AC-4.2 锁定) |
| Q-2 | 缺陷的"待代码评审"推荐命令如何生成? | **缺陷走 `code-check <REQ>`**(code-check 现有契约只接 REQ) |
| Q-3 | V0.0.2 引入的"已完成(需求分析)"子状态归类? | **不归一化**,归入"待概要设计"(NFR-3 + INV-9) |

## 14. 变更记录

| 时间 | 变更类型 | 摘要 | 关联项 |
| --- | --- | --- | --- |
| 2026-06-07 | 详细设计新增 | REQ-00023 详细设计与编码计划完成(6 任务 T-1 ~ T-6,沿用概要设计 D-1~D-6 + 9 不变量 INV-1~INV-9;算法 1~4 完整伪代码;零新增模块 / 0 依赖 / 0 字段 / 0 看板三同步);整体=--balanced;功能性=中 | REQ-00023 |
