# 过程文档判定 — TASK-REQ-00038-00003

任务编码:TASK-REQ-00038-00003
任务标题:[修改] 模板追加"## 各模块单测结果"小节 + code-plan 任务粒度描述字面改写 + 端到端验证
版本:V0.0.3
判定时间:2026-06-22 14:15

## decisions 字典

| 字段 | 决策 | 判定理由 |
| --- | --- | --- |
| `workLog.md` | 生成 | 任务实施日志是核心(始终生成) |
| `compileAndRun.md` | 不生成 | 纯 Markdown 改造,涉及文件 = `code-it/templates/RESULT.md` + `code-plan/SKILL.md`(2 文件,均 .md),无 .ts / .json / .toml / .yaml / .config 编译动作 |
| `deviations.md` | 生成 | 评审要查(始终生成) |
| `testResults.md` | 不生成 | 任务测试状态 = 不适用(纯文档任务) |
| `unitTestResults.md` | 不生成 | 任务类型 = 修改(代码类),但项目不可测(本仓库 7 项守卫全不命中) |
| `kanbanChangeLog` | 生成 | 本轮有追加(任务状态推进 + 完成时间填入 + 提交哈希回填) |
| `processDocDecisions` | 生成 | 其他任一不生成 → 本节生成 |

## 引用源

- 判定准则沿用 `code-it/SKILL.md` "## 过程文档自适应判定"(line 101-138)表格的"判定准则"列
- 物化算法沿用 `code-it/SKILL.md` 步骤 8.7.2(line 819-857)

## 涉及文件(本任务)

- `plugins/code-skills/skills/code-it/templates/RESULT.md`(L153 之后 / L155 之前追加 1 小节"## 各模块单测结果",7 字段)
- `plugins/code-skills/skills/code-plan/SKILL.md`(L473 / L496 各字面改写 1 句)
- 端到端校验:既有 8 个章节(L28-L106)字节级保留 + 既有"## 9. 单元测试"小节(L138-L153)字节级保留 + "## 10. 逻辑行统计"小节(L155-L174)章节顺序 +1 + "## 11. 变更记录"章节顺序 +1
- 关键:既有 9 个章节字节级保留(NFR-4 + INV-4 锁定)
