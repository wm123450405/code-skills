# 模块详细化 — REQ-00010

更新时间:2026-06-06 12:10
版本:V0.0.2
需求编码:REQ-00010

## 模块:`code-it` 步骤 0a 前置任务守卫(对应概要设计 §2.1)

- **路径**:`plugins/code-skills/skills/code-it/SKILL.md`
- **关键函数**(本计划新增):
  - `preTaskGuard(taskNum: string, version: string, reqNum: string): void` — 守卫主入口
  - `parsePlanOverview(planPath: string): TaskOverview[]` — 解析 `PLAN.md` 任务总览
  - `logAbortReport(reqNum, taskNum, allTasks, unfinished): void` — 打印中止报告
- **关键工具函数**(沿用 REQ-00013 沉淀,**不**重写):
  - `truncateTitle(title, maxLen=30)` — 标题截断
  - `formatTaskTitle(taskNum, title)` — 任务编号 + 标题
  - `formatReqTitle(reqNum, title)` — 需求编号 + 标题
  - `parsePlanTaskTitle(planPath, taskNum)` — 解析 PLAN.md 任务标题
- **内部状态**:**无**(纯函数式守卫,无内部状态)
- **关键调用顺序**:
  1. 用户输入 `code-it TASK-...` → `code-it` 步骤 0a 入口
  2. `preTaskGuard(taskNum, version, reqNum)` 被调用
  3. 反推 reqNum → 读 `plan/REQ-NNNNN/PLAN.md`
  4. `parsePlanOverview(planPath)` 解析任务列表
  5. 找到当前任务位置 → 取前置任务 → 判定
  6. 通过 → 步骤 0 入口;不通过 → `logAbortReport` + `exit(1)`
- **并发模型**:**无**(单次执行,无并发)
- **资源管理**:**无**(无文件/网络/连接)
- **错误处理范式**:
  - 文件不存在 → 软失败(守卫通过)
  - 解析失败 → 软失败(守卫通过)
  - 守卫不通过 → 硬失败(`exit 1`)
- **日志埋点**:
  - 守卫通过:`✓ code-it 前置任务守卫通过(<原因>)`
  - 守卫不通过:完整中止报告(沿用概要设计 §5.2)
  - 退化:`⚠ code-it 前置任务守卫:PLAN.md 不存在,守卫通过(退化)`
- **依据规范**:
  - `skill-conventions.md §规则 1` — frontmatter 字节级保留(INV-1)
  - `encoding-conventions.md §规则 1+3` — 任务编号正则(INV-2/3)
  - `dashboard-conventions.md §规则 1` — 不触发(INV-5)

## 模块与概要设计的对应

| 概要设计章节 | 本计划对应 |
| --- | --- |
| §2.1 修改文件清单 | 本计划 T-001 |
| §2.2 架构图 | 本计划 §状态机 / 流程 |
| §2.3 关键流程(S-1 守卫不通过) | 本计划 T-001 锚点 A 实施内容 |
| §2.4 关键流程(S-2 守卫通过) | 本计划 T-001 锚点 A 实施内容 |
| §3 关键设计 | 本计划 §"设计笔记"(沿用) |
| §4 守卫算法 | 本计划 §"设计笔记"详细化版 |
| §5 屏幕输出契约 | 本计划 T-001 锚点 A 实施内容 |
| §6 接口与数据结构 | **不适用**(无新增接口/数据结构) |
| §7 边界与异常 | 本计划 §"设计笔记"边界与异常(本计划补充实施细节) |
