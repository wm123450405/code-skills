# 设计笔记 — REQ-00010

更新时间:2026-06-06 12:10
版本:V0.0.2
需求编码:REQ-00010

## 任务拆分讨论(本阶段)

### DQ-1:本需求应拆为几个任务?
- **候选**:
  - **A**:1 个任务(单一 SKILL.md 增量追加)
  - **B**:2 个任务(T-001 改 SKILL.md + T-002 收尾 INV 自检 + 看板同步)
  - **C**:3 个任务(T-001 锚点 A / T-002 锚点 B / T-003 收尾)
- **选定**:**B**(沿用 REQ-00009 既有实践)
- **理由**:
  1. REQ-00009 同是 SKILL.md 步骤 0a 守卫追加,已用 2 任务结构 + 2 里程碑并通过评审(0 必须改)
  2. REQ-00014 强约束"按功能点拆分" — T-001 = "步骤 0a 守卫落地"功能点,T-002 = "INV 自检收尾"功能点
  3. REQ-00017 强约束"不拆更新看板任务" — 看板推进由 `code-it` 末尾兜底 P-1 承担,T-002 收尾只动"任务清单"行
  4. C(3 任务)粒度过细:本需求"步骤 0a 守卫"是单一功能点,不应再拆锚点 A/B/C(与 REQ-00009 不同:REQ-00009 步骤 0a 守卫 + 边界 E-2 + 边界 E-8 = 3 个独立子节,本需求只 1 个)
  5. A(1 任务)粒度过粗:把"实施 + 自检 + 看板"合为 1 任务,违反 REQ-00009 同类实践,且失去"实施/自检分两道闸"的双重保险
- **回退路径**:v2 评估是否需要更细粒度

### DQ-2:测试状态应该是什么?
- **候选**:
  - **A**:`不适用`(纯文档型,沿用 REQ-00009)
  - **B**:`未编写` → 后续补
- **选定**:**A**(沿用 REQ-00009 既有实践)
- **理由**:
  1. 本需求 = `code-it/SKILL.md` 增量追加,纯文档,无可测代码载体
  2. 仓库**不**含可测载体(无 `package.json` / `pyproject.toml` / `Cargo.toml` / `go.mod` / `pom.xml` / `build.gradle` / `test/` 目录) → 沿用 REQ-00009 "项目不可测 → 不适用"判定
  3. `code-unit` 守卫(Q-1 锁定)也会判定为不可测 → 测试状态 = `不适用`
- **回退路径**:v2 若仓库引入可测载体,可补单元测试

### DQ-3:INV 自检应包含几项?
- **候选**:
  - **A**:9 项(沿用 `design/.../RESULT.md §3.2` INV-1~9)
  - **B**:13 项(沿用 REQ-00009 实践:9 项 + 4 项"看板/收尾"扩展)
- **选定**:**B**(沿用 REQ-00009 实践)
- **理由**:
  1. T-002 收尾职责:对设计 9 项 INV 全部复核 + 看板 5 处同步(任务清单 2 行 + 文档头 + 详细设计汇总 + 变更记录)+ 整体收尾
  2. REQ-00009 INV-1~13 = 9 设计 INV + 4 收尾 INV(看板"测试状态"列不新增枚举值 / 整体收尾 / 13 项自检等)
  3. 4 项扩展 INV = INV-10 看板"测试状态"列不新增枚举值 / INV-11 其他 11 技能 0 改动 / INV-12 收尾过程文档齐全 / INV-13 整体收尾

### DQ-4:任务编号如何分配?
- **选定**:`TASK-REQ-00010-00001` + `TASK-REQ-00010-00002`(沿用 REQ-00009 同结构)
- **理由**:沿用 5+5 位嵌套式(`encoding-conventions §规则 3`)

## 关键决策(本计划,4 项)

| # | 决策 | 依据 | 替代方案(被否决) |
| --- | --- | --- | --- |
| DQ-1 | 2 任务结构(T-001 实施 + T-002 收尾) | REQ-00009 同结构(0 必须改评审通过) | 1 任务粒度过粗 / 3 任务粒度过细 |
| DQ-2 | 测试状态 = `不适用`(纯文档型) | REQ-00009 实践 + 仓库无可测载体 | `未编写`(后续补) |
| DQ-3 | INV 13 项(9 设计 + 4 收尾) | REQ-00009 实践 | 9 项(无收尾扩展) |
| DQ-4 | 任务编号 `TASK-REQ-00010-00001` + `TASK-REQ-00010-00002` | `encoding-conventions §规则 3` | 3 位序号(已淘汰) |

## 沿用上游设计决策(9 项,详 `design/.../RESULT.md §3.1`)

1. 守卫插入"步骤 0"前,名为"步骤 0a"
2. 前置信息源 = `PLAN.md` 任务总览**文件行序**
3. "未完成"判定 = 开发状态 ∈ {`待开始`,`进行中`,`阻塞`}
4. 中止时退出码 = `1`(非 0)
5. `PLAN.md` 缺失 / 解析失败 → 守卫**通过**(退化)
6. 不修改既有"步骤 7 显式前置任务检查"
7. 不引入新依赖
8. 不修改 frontmatter
9. 不引入新参数(`--skip-precondition`)

## 沿用上游不变量(9 项,详 `design/.../RESULT.md §3.2`)

- INV-1:frontmatter L1-3 字节级保留
- INV-2:§"工作流程"步骤 0~16 内容不变
- INV-3:§"缺陷分支"步骤 17~25 内容不变
- INV-4:§"标题解析(REQ-00013 新增)"小节不变
- INV-5:`PLAN.md` 模板 / 看板"任务清单"区段 / `dashboard-conventions.md` 不变
- INV-6:`marketplace.json` / `plugin.json` 不变
- INV-7:9 个其他 `code-*` 技能 SKILL.md 不变
- INV-8:`code-auto` FR-4.AC-4.3 "按任务总览行序"逻辑不变
- INV-9:`code-unit` / `code-publish` / `code-dashboard` / `code-review` 现有逻辑不变

## 本计划新增 INV(4 项,扩展上游 9 项)

- **INV-10**:SKILL.md 锚点 A 后的"步骤 0a"小节必须含完整 5 子节(目标 / 触发条件 / 算法 / 通过条件 / 不通过处理 / 退化条件)
- **INV-11**:9 个其他 `code-*` 技能 SKILL.md 行数**不**变化(用于精确验证 INV-7)
- **INV-12**:`/code-plan` / `/code-unit` 既有"## 工作流程"步骤 0a 守卫(REQ-00009 / REQ-00005)与本需求守卫**并存**,职责正交,无重复
- **INV-13**:整体收尾:2 任务开发状态 = `已完成` + 测试状态 = `不适用`

## 守卫算法(沿用概要设计 §4,本计划补充细节)

```ts
// 步骤 0a 前置任务守卫(详细化版,语义化锚点已锁定)
function preTaskGuard(taskNum: string, version: string, reqNum: string): void {
  // 1. 反推所属需求(taskNum 第 3 段为 reqNum 数字)
  //    格式: TASK-REQ-NNNNN-NNNNN → reqNum = NNNNN
  //    格式: TASK-BUG-NNNNN-NNNNN → 不属于"任务"路径(缺陷),守卫不触达
  if (!taskNum.startsWith('TASK-REQ-')) return
  // 2. 读 PLAN.md(NFR-6 退化)
  const planPath = `./assistants/${version}/plan/${reqNum}/PLAN.md`
  if (!fileExists(planPath)) {
    log('⚠ PLAN.md 不存在,守卫通过(退化)')
    return
  }
  // 3. 解析任务总览区段
  //    锚点: ^## 任务总览$
  //    行匹配: ^\| .* \|$  (表格行)
  //    列锚点: 第 1 列 = 任务编号 / 第 6 列 = 开发状态(沿用 REQ-00013 `parsePlanTaskTitle` 列号)
  const tasks = parsePlanOverview(planPath)
  // 4. 找到当前任务位置
  const idx = tasks.findIndex(t => t.num === taskNum)
  if (idx === -1) return  // 由原 code-it 步骤 2 报错
  // 5. 前置任务 = 当前任务之前的所有任务
  const preTasks = tasks.slice(0, idx)
  if (preTasks.length === 0) {
    log('✓ 前置任务守卫通过(无前置任务)')
    return
  }
  // 6. 判定每个前置任务的开发状态
  //    "未完成"定义(沿用 Q-2 锁定 A):开发状态 ∈ {待开始, 进行中, 阻塞}
  //    "已完成"定义:开发状态 = 已完成
  const unfinished = preTasks.filter(t => t.devStatus !== '已完成')
  if (unfinished.length === 0) {
    log('✓ 前置任务守卫通过(全部已完成)')
    return
  }
  // 7. 中止 + 打印推荐命令
  logAbortReport(reqNum, taskNum, tasks, unfinished)
  exit(1)
}

function logAbortReport(reqNum, taskNum, allTasks, unfinished) {
  // 沿用概要设计 §5.2 模板
  // 含"REQ-NNNNN · 标题" + "TASK-... · 标题"格式(沿用 REQ-00013 升级版)
  // 推荐命令只指向第一个未完成前置
}
```

## 边界与异常(本计划补充实施细节,沿用概要设计 §7)

| ID | 场景 | 处理 | 实施时验证 |
| --- | --- | --- | --- |
| E-1 | 无 `.current-version` | 原 `code-it` 步骤 0 处理 | 既有行为 |
| E-2 | 守卫不通过(存在未完成前置) | 打印中止报告 + 推荐命令 + `exit 1` | T-001 验证:模拟 TASK-002 待开始,调 `code-it TASK-003` |
| E-3 | `PLAN.md` 不存在 | 守卫**通过**(NFR-6 退化) | T-001 验证:`rm` PLAN.md 后调 `code-it` |
| E-4 | 当前任务不在 `PLAN.md` 任务总览中 | 原步骤 2 报错(守卫不重复) | T-001 验证:故意调不存在的 TASK-999 |
| E-5 | `PLAN.md` 任务总览区段格式错乱 | 守卫**通过**(软失败) | T-001 验证:故意改 PLAN.md 表格 |
| E-6 | `code-auto` 调 `code-it` 时守卫不通过 | `exit 1` → `code-auto` 中断 | 由 `code-auto` 流程验证 |
| E-7 | 多个未完成前置 | 打印所有未完成前置,推荐命令**只**指向第一个 | T-001 验证:TASK-002 + TASK-003 都待开始 |
| E-8 | 任务编码格式不匹配 | 原 `code-it` 步骤 1 报错 | 既有行为 |
| E-9 | 任务属于缺陷分支(`TASK-BUG-...`) | 守卫不触达 | T-001 验证:故意调 `TASK-BUG-...` |
| E-10 | 标题解析失败 | 退化"编号+(无标题)" | 沿用 REQ-00013 E-3 |
