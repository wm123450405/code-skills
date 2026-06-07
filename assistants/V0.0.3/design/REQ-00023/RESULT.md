# 概要设计 — REQ-00023(简化 code-dashboard 总览模式为 4 段输出)

- 需求编码:REQ-00023
- 所属版本:V0.0.3
- 上游需求:./assistants/V0.0.3/require/REQ-00023/RESULT.md
- 遵循规范:./assistants/rules/ 下 13 个文件(dashboard-conventions §规则 1 触发判定:本需求零新增看板字段,**不**触发三同步)
- 创建时间:2026-06-07

## 设计目标

整体设计目标:`--balanced`(code-auto 上下文默认)
维度优先级:
  功能性:中(屏显简化,沿用既有能力;不引入新维度)

## 1. 设计概述

**核心思路**:把 `code-dashboard` 总览模式从"4 段详尽"重定义为"4 段精简",**只**改 `code-dashboard/SKILL.md` 1 个文件,其他 12 个 `code-*` 技能 SKILL.md frontmatter 字节级保留(沿用 NFR-6)。

**关键决策**(D-1 ~ D-6):
- **D-1**:`code-dashboard` 改造**限定在总览模式**(无参数路径);需求模式 `REQ-NNNNN` 输出**完全不变**(沿用既有 5 段)
- **D-2**:总开发进度 = 加权平均(需求 6 步 / 缺陷 5 步,不适用的环节按已完成计入)
- **D-3**:5 类状态(待概要设计 / 待详细设计 / 待代码开发 / 待单元测试 / 待代码评审)从既有看板列**派生**,**不**新增字段
- **D-4**:每类状态 1 条推荐命令(共 ≤ 5 条),**不**超过 5 行上限(沿用既有 AC-4.3)
- **D-5**:高优先级缺陷段(P0 / P1)保留,只列数量,沿用既有 █ / ▓ 标记
- **D-6**:`code-dashboard` 仍是**只读契约**(不调用 `Write` / `Edit` / `Bash`),无副作用,多次执行幂等

## 2. 模块拆分

### 2.1 既有模块(全部保留,零修改)

| 模块 / 路径 | 职责 | 状态 |
| --- | --- | --- |
| `plugins/code-skills/skills/code-dashboard/SKILL.md` | 看板技能定义(总览模式 + 需求模式) | **修改既有**(本需求改造对象) |
| `plugins/code-skills/skills/code-dashboard/guidelines/*.md` | 技能指南 | 复用,零修改 |
| 其他 12 个 `code-*` SKILL.md | 12 个其他技能 | **零修改**(NFR-6 严守) |

### 2.2 新增模块

**无**(本需求只改造 1 个既有 SKILL.md,零新增模块;零新增文件)

### 2.3 修改模块

**`code-dashboard/SKILL.md`** — 改造范围限定:

| 小节 | 改造内容 | 改造量 |
| --- | --- | --- |
| frontmatter L1-3 | 字节级保留 | 0 行(零修改) |
| `## 目标` | 改造 2 段 1 句(沿用既有) | 微调 |
| `## 适用场景` | 沿用,补 1 句"总览模式已精简为 4 段" | +1 行 |
| `## 不适用` | 沿用,零修改 | 0 行 |
| `## 工作目录约定` | 沿用,零修改 | 0 行 |
| `## 输入` | 沿用,零修改 | 0 行 |
| `## 输出` | **核心改造**:总览模式 4 段重定义 | ~30 行 |
| `## 工具使用约定` | 沿用,零修改 | 0 行 |
| `## 工作流程` | **核心改造**:步骤 0/1/2a/3/4 段 1-4 改造 | ~80 行 |
| `## 边界与异常` | 沿用,微调(L1 / L2 / L3 / E-1 ~ E-10) | +5 行 |
| `## 衔接` | 沿用,补 1 句"屏幕输出已简化" | +1 行 |
| `## 不要做的事` | 沿用,零修改 | 0 行 |
| `## 附录 A 任务编号解析` | 沿用,零修改 | 0 行 |
| `## 附录 B ASCII 比例条` | 沿用,零修改 | 0 行 |
| `## 附录 C 建议数据结构` | 沿用,改造 1 段 | ~10 行 |
| `## 变更记录` | 追加 1 条 "2026-06-07 REQ-00023 简化总览模式为 4 段" | +1 行 |

**预估总改造量**:`code-dashboard/SKILL.md` 净变化 +20~+30 行(沿用 REQ-00021 NFR-5.1 经验值)

### 2.4 关键设计原则

- **零新增模块**:不引入新 `code-*` 技能,不复用 V0.0.1 / V0.0.2 历史文件
- **零新增文件**:不引入新模板 / 指南 / 清单
- **零新增依赖**:不引入新 NPM / Python 包
- **零新增看板字段**(沿用 dashboard-conventions §规则 1 触发判定:**不**触发三同步)

## 3. 接口概要

### 3.1 总览模式 4 段屏显接口(FR-1 / FR-2 / FR-3 / FR-6)

**段 1:总开发进度**(新增)

```
总开发进度
──────────
[████████░░░░] 67%
```

- 12 字符 ASCII 比例条 + 1 行百分比
- 公式:`总进度 = (Σ 需求已完步 + Σ 缺陷已完步) / ((需求数 × 6) + (缺陷数 × 5)) × 100%`
- 退化(分母=0):`— / 无需求无缺陷,无需进度`

**段 2:各状态数量占比**(改造既有"任务进度"段)

```
各状态数量占比
──────────────
待概要设计: 需求 2 / 缺陷 0(占比 50.0%)
待详细设计: 需求 0 / 缺陷 0
待代码开发: 需求 1 / 缺陷 0(占比 25.0%)
待单元测试: 需求 0 / 缺陷 0
待代码评审: 需求 1 / 缺陷 0(占比 25.0%)
```

- 5 类状态各 1 行
- 0/0 行不展示(AC-3.3)
- 占比分母 = 本版本"需求+缺陷"总数

**段 3:高优先级缺陷**(沿用既有)

```
高优先级缺陷
───────────
P0 待修复: █ 1
P1 待修复: ▓ 0
```

- 沿用既有 █/▓ 标记
- 只列 P0 / P1 数量(沿用既有)

**段 4:后续操作建议**(改造既有"下一步建议"段)

```
后续操作建议
────────────
> 建议: /code-design REQ-00023
> 依据: 1 项需求在"待概要设计"状态
> 优先级: 中

> 建议: /code-it TASK-REQ-00023-00001
> 依据: 1 项需求在"待代码开发"状态
> 优先级: 中

> 建议: /code-check REQ-00023
> 依据: 1 项需求在"待代码评审"状态
> 优先级: 中
```

- 每类状态 1 条命令(共 ≤ 5 条)
- 严格按既有 10 个 `code-*` SKILL.md frontmatter 真实语法
- 状态无触发 → 该行不展示

### 3.2 需求模式接口(完全沿用,零修改)

既有 5 段输出(元信息 / 任务清单 / 关联缺陷 / 任务进度 / 建议)**不**简化,沿用 V0.0.2 实现。

### 3.3 错误模式接口(完全沿用,零修改)

既有 E-4(参数格式错)+ E-1(无激活版本)+ E-2(版本不存在)+ E-3(需求不存在)+ E-5(看板缺失)**不**简化,沿用 V0.0.2 实现。

## 4. 数据结构(派生自既有看板列,**不**新增字段)

### 4.1 既有看板列(全部沿用,零新增)

| 看板区段 | 既有列 | 本需求用途 |
| --- | --- | --- |
| **需求清单** | 需求编码 / 标题 / 状态 / 创建时间 / 完成时间 / **需求文档 / 概要设计 / 详细设计** | 判定 5 类状态中的"待概要设计 / 待详细设计" |
| **缺陷清单** | 缺陷编号 / 严重度 / 标题 / **状态** / 报告时间 / 修复时间 / 关联任务 / 修复提交 | 判定 5 类状态中缺陷归属 |
| **任务清单** | 任务编号 / 需求 / 类型 / 触发/来源 / 标题 / **开发状态 / 测试状态** / 涉及文件 / 完成时间 / 提交哈希 / 关联任务 | 判定"待代码开发 / 待单元测试 / 待代码评审" |
| **评审发现汇总** | 评审 ID / 需求 / 任务 / 维度 / **级别 / 状态** / 描述 / 派生改修任务 | 判定"待代码评审"(是否有"必须改"未处理) |

### 4.2 派生状态对象(本需求在 SKILL.md 内定义的**纯解析**对象,**不**落盘)

```ts
type DashboardState =
  | "待概要设计"
  | "待详细设计"
  | "待代码开发"
  | "待单元测试"
  | "待代码评审"
  | "已完成"  // 隐含(不再单列)
  | "已取消"  // 隐含(不再单列)
  | "阻塞"    // 隐含(不再单列)

type Item = {
  type: "requirement" | "bug"
  id: string  // REQ-NNNNN 或 BUG-NNN
  currentState: DashboardState
}

type Summary = {
  totalProgress: number  // 0-100
  bar: string  // "[████████░░░░] 67%"
  stateBreakdown: { state: DashboardState, reqCount: number, bugCount: number, pct: number }[]
  p0Count: number
  p1Count: number
  suggestions: Suggestion[]  // 最多 5 条
}
```

- **不**落盘到 `<版本号>/RESULT.md`(**不**触发 dashboard-conventions §规则 1 三同步)
- **不**落盘到任何 JSON / YAML 文件
- 仅作为 `code-dashboard/SKILL.md` §工作流程 段 4 内的临时解析对象

## 5. 算法与逻辑

### 5.1 总开发进度计算(算法 1)

```ts
function calcTotalProgress(requirements, bugs, tasks, reviews): { progress: number, bar: string } {
  let totalDone = 0
  let totalExpected = 0

  // 需求类(6 步)
  for (const req of requirements) {
    totalExpected += 6
    if (req.hasRequireDoc)  totalDone += 1  // 需求分析
    if (req.hasDesignDoc)   totalDone += 1  // 概要设计
    if (req.hasPlanDoc)     totalDone += 1  // 详细设计
    if (req.allTasksDevDone) totalDone += 1  // 编码
    if (req.allTasksTestPassed || req.allTasksTestN_A) totalDone += 1  // 单元测试
    if (req.reviewPassed)   totalDone += 1  // 代码评审
  }

  // 缺陷类(5 步)
  for (const bug of bugs) {
    totalExpected += 5
    if (bug.isReported)  totalDone += 1  // 缺陷登记
    if (bug.hasFixPlan)  totalDone += 1  // 详细设计
    if (bug.allTasksDevDone) totalDone += 1  // 编码
    if (bug.allTasksTestPassed || bug.allTasksTestN_A) totalDone += 1  // 单元测试
    if (bug.reviewPassed) totalDone += 1  // 代码评审
  }

  if (totalExpected === 0) {
    return { progress: null, bar: "— / 无需求无缺陷,无需进度" }
  }

  const pct = Math.round(totalDone / totalExpected * 100)
  return { progress: pct, bar: renderBar(pct) }
}
```

**关键约束**:
- "不适用的环节按已完成计入":AC-1.3 明确说明(如纯文档任务,单元测试=不适用,**算**已完成 1 步)
- 计算结果**严格**在内存中,不写任何文件

### 5.2 5 类状态判定(算法 2)

```ts
function classifyState(item, allTasks, reviews): DashboardState {
  // 需求类判定
  if (item.type === "requirement") {
    if (!item.hasDesignDoc) return "待概要设计"  // 概要设计列 = — 或空
    if (!item.hasPlanDoc)   return "待详细设计"  // 概要设计已链接,详细设计未开始
    if (!item.allTasksDevDone) return "待代码开发"  // 有任务开发状态≠已完成
    if (item.hasTaskWithoutTest) return "待单元测试"  // 开发已完成,测试未通过
    if (item.hasMustFix) return "待代码评审"  // 评审发现"必须改"未处理
    return "已完成"  // 隐含,不单列
  }

  // 缺陷类判定(类比)
  if (item.type === "bug") {
    if (!item.hasFixPlan)  return "待详细设计"  // 缺陷跳过"待概要设计",直接进修复方案
    if (!item.allTasksDevDone) return "待代码开发"
    if (item.hasTaskWithoutTest) return "待单元测试"
    if (item.hasMustFix) return "待代码评审"
    return "已完成"
  }
}
```

**关键约束**:
- 缺陷不进入"待概要设计"状态(缺陷从登记直接进入修复方案)
- E-7 边界:某需求同时属"待代码开发"+"待单元测试" → 归入"待代码开发"(更早阶段优先)

### 5.3 5 类状态计数(算法 3)

```ts
function buildBreakdown(items): { state: DashboardState, reqCount: number, bugCount: number, pct: number }[] {
  const total = items.length
  const states: DashboardState[] = ["待概要设计", "待详细设计", "待代码开发", "待单元测试", "待代码评审"]
  const result = []

  for (const s of states) {
    const reqCount = items.filter(i => i.type === "requirement" && i.currentState === s).length
    const bugCount = items.filter(i => i.type === "bug" && i.currentState === s).length
    if (reqCount + bugCount === 0) continue  // 0/0 行不展示
    const pct = total === 0 ? 0 : Math.round((reqCount + bugCount) / total * 1000) / 10  // 保留 1 位小数
    result.push({ state: s, reqCount, bugCount, pct })
  }

  return result
}
```

**关键约束**:
- AC-3.3:0/0 行不展示
- AC-3.5:5 行占比加和 = 100%(允许 0.1% 四舍五入误差)

### 5.4 后续操作建议生成(算法 4,改造既有算法 3)

```ts
function buildSuggestions(items): Suggestion[] {
  const suggestions: Suggestion[] = []

  // 1. 待概要设计(只走需求路径)
  const pendingDesign = items.find(i => i.type === "requirement" && i.currentState === "待概要设计")
  if (pendingDesign) {
    suggestions.push({
      command: `/code-design ${pendingDesign.id}`,
      reason: `${pendingDesign.id} 在"待概要设计"状态`,
      priority: "中"
    })
  }

  // 2. 待详细设计
  const pendingPlan = items.find(i => i.currentState === "待详细设计")
  if (pendingPlan) {
    const cmd = pendingPlan.type === "requirement" ? `/code-plan ${pendingPlan.id}` : `/code-plan ${pendingPlan.id}`
    suggestions.push({
      command: cmd,
      reason: `${pendingPlan.id} 在"待详细设计"状态`,
      priority: "中"
    })
  }

  // 3. 待代码开发
  const pendingDev = items.find(i => i.currentState === "待代码开发")
  if (pendingDev) {
    const firstTask = firstUndoneTask(pendingPlan)  // 沿用既有算法
    const cmd = pendingDev.type === "requirement" ? `/code-it ${firstTask.id}` : `/code-it ${firstTask.id}`
    suggestions.push({
      command: cmd,
      reason: `${pendingDev.id} 在"待代码开发"状态,首个未完成任务 ${firstTask.id}`,
      priority: "中"
    })
  }

  // 4. 待单元测试
  const pendingUnit = items.find(i => i.currentState === "待单元测试")
  if (pendingUnit) {
    const firstTestTask = firstTaskWithoutTest(pendingUnit)
    const cmd = `/code-unit ${firstTestTask.id}`
    suggestions.push({
      command: cmd,
      reason: `${firstTestTask.id} 开发完成,测试未通过`,
      priority: "中"
    })
  }

  // 5. 待代码评审
  const pendingReview = items.find(i => i.currentState === "待代码评审")
  if (pendingReview) {
    const cmd = `/code-check ${pendingReview.id}`  // 沿用 code-check 现有契约(只接 REQ)
    suggestions.push({
      command: cmd,
      reason: `${pendingReview.id} 任务全部完成,评审发现"必须改"未处理`,
      priority: "中"
    })
  }

  return suggestions.slice(0, 5)  // AC-4.3 严格 5 行上限
}
```

**关键约束**:
- AC-4.2:同状态需求 + 缺陷并存 → 1 条(需求路径优先)
- AC-4.5:每条命令**严格**按既有 10 个 `code-*` SKILL.md frontmatter 真实语法

## 6. 异常处理(沿用既有 + 本需求新增 E-1 ~ E-10)

| ID | 场景 | 处理 | 退化 |
| --- | --- | --- | --- |
| **E-1** | 某需求"概要设计"列异常(非 `—`/非空/非链接) | 视为"未开始",归入"待概要设计" | 屏显 `?` 标记 |
| **E-2** | `plan/<REQ>/RESULT.md` 缺失 | 视为"待详细设计" | 屏显 `?` 标记 |
| **E-3** | `plan/<REQ>/PLAN.md` 缺失 | 视为"待代码开发"(无任务可读) | 屏显 `?` 标记 |
| **E-4** | 任务"开发状态"字段为空 | 视为"待开始",归入"待代码开发" | 屏显 `?` 标记 |
| **E-5** | 评审发现汇总"必须改"未链接原任务 | 视为"待代码评审" | 屏显 `?` 标记 |
| **E-6** | `RESULT.md` 完全缺失 | 沿用既有 E-5:退出 + 引导调 `code-version` | 不渲染 |
| **E-7** | 某需求同时属于"待代码开发"和"待单元测试" | 归入"待代码开发"(更早阶段优先) | 屏显注释 |
| **E-8** | 5 类状态全部无触发 | 显示"无后续动作" 1 行 | 不展示建议段 |
| **E-9** | 推荐命令对应的目标文件不存在 | 沿用既有 E-5(只读契约) | 不报错,屏显 `?` 标记 |
| **E-10** | 缺陷"修复方案"(`fix/<BUG>/PLAN.md`)缺失 | 视为"待详细设计" | 屏显 `?` 标记 |

**所有异常均不阻塞**(`code-dashboard` 沿用 L2 / L3 退化原则)

## 7. 安全 / 性能

- **安全**:本需求零新增外部输入(只读 `RESULT.md`),无注入风险
- **性能**:单遍扫描主看板文本(沿用既有算法 1),NFR-1 强约束屏显 ≤ 12 行

## 8. 测试要点(本需求**不适用**单元测试)

- 沿用 REQ-00021 / REQ-00022 同模式:`code-dashboard` 是**文档 / 配置 / 屏显**类技能,无源码改动,**不**触发单元测试
- 验证手段:人工在 REPL 中调 `/code-dashboard` 对比屏显
- 验证用例:见 `require/REQ-00023/RESULT.md` §6 验收标准(AC-1 ~ AC-8 共 8 类)

## 9. 规范遵循与冲突解决

### 9.1 触发的规范

| 规范文件 | 触发判定 | 处理 |
| --- | --- | --- |
| **dashboard-conventions §规则 1** | 零新增看板字段(INV-8 锁定) | **不**触发三同步;**不**改 `version-RESULT.md` / `CLAUDE.md` |
| **skill-conventions §规则 1** | 改造既有 SKILL.md 1 个 | frontmatter L1-3 字节级保留(INV-1);**不**触发 skill 同步 |
| **module-conventions §规则 1** | 不新增模块 | 零修改 |
| **encoding-conventions §规则 1+3** | 沿用任务编号双格式 | 零修改 |
| **doc-conventions** | 文档措辞 | 沿用现有 |

### 9.2 现状偏离

**无**(本需求零改动其他 12 个 `code-*` 技能)

### 9.3 冲突解决

**无**(INV-1 ~ INV-9 全部锁定 0 偏离)

### 9.4 用户授权的偏离

**无**

## 10. 待澄清 / 未决项(继承上游 §10)

- **Q-1**:5 类状态判定时,同状态需求 + 缺陷并存,推荐命令选需求路径还是缺陷路径?
  - 本设计选择:**需求路径优先**(沿用 FR-5 同表注释;AC-4.2 锁定)
  - 沿用 INV-6 零新增原则
- **Q-2**:`code-check` 技能本身**不**接收 BUG 编号;缺陷的"待代码评审"推荐命令如何生成?
  - 本设计选择:**缺陷走 `code-check <REQ>` 路径**(评审关联的"原需求",非直接评审缺陷)
  - 备选方案不采纳(沿用 `code-check` 既有契约)
- **Q-3**:V0.0.2 引入的"已完成(需求分析)"子状态在本需求中如何归类?
  - 本设计选择:**归入"待概要设计"**(NFR-3 + INV-9 锁定的"不归一化")
  - 屏显原状保留

## 11. 变更记录

| 时间 | 变更类型 | 摘要 | 关联项 |
| --- | --- | --- | --- |
| 2026-06-07 | 设计新增 | REQ-00023 概要设计完成(6 决策 D-1~D-6 + 9 不变量 INV-1~INV-9,沿用上游;0 模块新增,0 依赖新增,0 字段新增,0 看板三同步触发);整体=--balanced(code-auto 上下文默认);0 派生"更新看板"任务;Q-1/Q-2/Q-3 沿用上游当前假设锁定 | REQ-00023 |
