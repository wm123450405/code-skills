# TASK-BUG-00004-00004 — [文档] 其他 6 个技能旁路验证(grep 判定表 + 静态校验,**不修改**)

- 任务编码:TASK-BUG-00004-00004
- 缺陷编号:BUG-00004
- 所属版本:V0.0.3
- 任务类型:文档
- 触发/来源:缺陷修复
- 任务来源:./assistants/V0.0.3/fix/BUG-00004/PLAN.md §3 TASK-BUG-00004-00004
- 详细设计:./assistants/V0.0.3/fix/BUG-00004/RESULT.md §4 模块 3 + §6 末"其他技能旁路验证结论"
- 状态:已完成
- 责任人:wangmiao
- 创建:2026-06-22 22:05
- 完成:2026-06-22 23:00
- 当前版本:v1

## 1. 任务概述

本任务是 BUG-00004 修复方案的最后一个任务:对 7 个其他技能(`code-require` / `code-design` / `code-check` / `code-plan` / `code-fix` / `code-init` / `code-rule`)做静态校验,确认它们是否也存在 `code-it` 同类"判定表 ↔ 工作流"脱节问题。**不动修改任何 SKILL.md**;仅产出 `side-skill-verification.md` 报告 + 末尾兜底提交累积 T-001 ~ T-004 一起 commit。

## 2. 改修内容总览

### 2.1 文件变更

| 变更类型 | 文件路径 | 说明 |
| --- | --- | --- |
| 新增 | `assistants/V0.0.3/fix/BUG-00004/side-skill-verification.md` | **本任务核心产出**:7 技能旁路验证报告(4 个有判定表 / 3 个无判定表) |
| 状态推进 | `assistants/V0.0.3/code/TASK-BUG-00004-00004/{work-log,deviations,RESULT,process-doc-decisions}.md` | 4 份过程文档(守卫正确跳过 `compile-and-run.md` / `test-results.md`) |
| 状态推进 | `assistants/V0.0.3/fix/BUG-00004/{PLAN.md,RESULT.md}` | 任务完成 + BUG 状态推进 `修复编码中` → `待审查` |
| 状态推进 | `assistants/V0.0.3/fix/RESULT.md` | 缺陷清单同步 |
| 状态推进 | `assistants/V0.0.3/RESULT.md` | 任务清单 + 统计 + 变更记录 |
| 末尾兜底提交 | (累积 T-001 + T-002 + T-003 + T-004 一起 commit)| `git add` + `git commit` 一次提交全部 4 任务产出 |

### 2.2 提交记录

- 分支:本仓库 `main`
- 提交哈希:(本任务末尾 `git commit` 产出,见步骤 24/25 末尾兜底)
- 提交信息:`chore(code-it): BUG-00004 code-it 步骤 8.7 + 9/10/11 守卫 + 步骤 13/16 改造 + 模板 §8 + 端到端验证 + 6 技能旁路验证`

## 3. 详细改动

### 3.1 旁路验证报告(`assistants/V0.0.3/fix/BUG-00004/side-skill-verification.md`)

**核心数据**(7 技能):

| 技能 | 判定表存在? | 始终生成 | 条件生成 | ≥ 2 项"不生成" 触发 | 实际过度生成风险 | 是否修复? |
| --- | --- | --- | --- | --- | --- | --- |
| `code-require` | ✓ | 2 | 3 | 是(3 项) | 低 | 不修复 |
| `code-design` | ✓ | 2 | 6 | 是(5 项) | 中(当前 0 触发) | 不修复 |
| `code-check` | ✓ | 2 | 2 | 是(2 项) | 极低 | 不修复 |
| `code-plan` | ✓ | 2 | 7 | 是(5 项) | 中(当前 0 触发) | 不修复 |
| `code-fix` | ✗ | 2(硬写) | 0 | 不适用 | 无 | 不修复 |
| `code-init` | ✗ | 1(基线) | 0 | 不适用 | 无 | 不修复 |
| `code-rule` | ✗ | 0 | 0 | 不适用 | 无 | 不修复 |

**核心结论**:
- **7 个技能全部"实际过度生成风险" = 低 / 中(0 触发) / 极低 / 无**
- **均不修复**(修复成本/收益不匹配)
- 与 BUG-00004 详细设计 §6 末"其他技能旁路验证结论" 字面 100% 一致
- **关键决策**:仅修复 `code-it`(由 T-001 + T-002 完成);其他 6 个技能旁路验证**仅**记录结论,作为 BUG-00004 修复完整性的旁证

### 3.2 静态校验方法

- **步骤 A**:对每个技能,定位"## 过程文档自适应判定"或等效章节
- **步骤 B**:数判定表中"始终生成" / "条件生成或不适用" / "不生成" 3 类条目的数量
- **步骤 C**:判定是否有 ≥ 2 个"条件生成"分支同时触发"不生成"的可能性
- **步骤 D**:给出"实际过度生成风险"等级
- **步骤 E**:本任务**不修改任何 SKILL.md**(沿用详细设计 §4 模块 3 字面)

### 3.3 末尾兜底提交

按 V0.0.3 REQ-00037 模式,本任务末尾执行 1 次 `git commit`,累积 T-001 + T-002 + T-003 + T-004 全部产出:
- `plugins/code-skills/skills/code-it/SKILL.md`(T-001 + T-002 改造)
- `plugins/code-skills/skills/code-it/templates/RESULT.md`(T-002 改造)
- `assistants/V0.0.3/fix/BUG-00004/{RESULT,PLAN,side-skill-verification}.md`(T-004 产出)
- `assistants/V0.0.3/fix/RESULT.md`(总览同步)
- `assistants/V0.0.3/RESULT.md`(看板同步)
- `assistants/V0.0.3/code/TASK-BUG-00004-0000{1,2,3,4}/{work-log,deviations,RESULT,process-doc-decisions}.md`(4 任务过程文档)

## 4. 关键决策与权衡

1. **PLAN.md 字面歧义处理**:标题"6 个技能" vs 涉及文件模块"7 个" → 沿用"涉及文件模块"字面(plan-conventions §规则 1 强约束:文件级而非数字级),遍历 7 个技能
2. **不修复决策**:7 技能全部"实际过度生成风险"低/中(0 触发)/极低/无 → 修复成本/收益不匹配 → 仅修复 `code-it`
3. **末尾兜底提交**:沿用 V0.0.3 REQ-00037 模式,T-001 ~ T-004 累积 1 次 commit(避免多次小 commit 噪声)

## 5. 偏离设计/规范的地方

指向 `deviations.md`:
- **§偏离 1**:PLAN.md 标题字面"6 个技能"与"涉及文件模块"字面"7 个"歧义,本任务按"涉及文件模块"字面遍历 7 个技能
- **§偏离 0**:无偏离(NFR-3 零规范变更)

## 6. 验证结果

### 6.1 编译

- 命令:(无 — 本任务为静态校验 + 末尾兜底提交,无生产代码改动,无可执行构建命令)
- 结论:✅ 不适用
- 详情:**步骤 8.7 守卫跳过**(`decisions.compileAndRun = '不生成'`,因 changedFiles 全部为 `.md`),本任务**不**生成 `compile-and-run.md`

### 6.2 启动

- 命令:(无)
- 结论:✅ 不适用(沿用 §6.1)

### 6.3 测试(若适用)

- 命令:(无)
- 结论:✅ 不适用(本任务为静态校验,非代码任务;任务测试状态 = `不适用`)
- 静态校验(本任务):全部通过
 - 7 个技能 SKILL.md 字面位置全部正确(line 80 / 83 / 104 / 92 / 376 / 无 / 426)
 - 4 个有判定表的技能判定表字面收集完整
 - 3 个无判定表的技能过程文档逻辑字面确认
 - `side-skill-verification.md` 报告 7 行数据 + 与 BUG-00004 详细设计 §6 末字面 100% 一致 ✓
- 详情:**步骤 8.7 守卫跳过**(`decisions.testResults = '不生成'`,因任务测试状态 = `不适用`),本任务**不**生成 `test-results.md`

## 7. 已知问题 / 未完成项

本任务范围内无未完成项。

- BUG-00004 状态推进:`修复编码中` → `待审查`(由 `itEndStateRollback` 子步骤执行,doneCount=4/totalCount=4)
- 末尾兜底提交:本任务末尾执行 1 次 `git commit`
- 下一步:`code-check BUG-00004`(评审修复成果) + `code-fix BUG-00004`(推进状态到 `已修复-已验证` → `已关闭`)

## 8. 过程文档清单(由 code-it 内化,BUG-00004 新增)

> 本节由 `code-it` 步骤 13 接管 BUG-00004 详细设计 §5 算法 3 产出,沿用步骤 8.7 物化的 `decisions` 字典;详见 `code-it/SKILL.md` 步骤 13 末"本步骤产物"指引。

### 8.1 工作流上下文

- `decisions.workLog`:`生成`(本任务有 `work-log.md`)
- `decisions.compileAndRun`:**`不生成`**(静态校验 + 末尾兜底提交,无构建/运行命令,changedFiles 全部为 `.md`;步骤 8.7 守卫触发,步骤 9/10 跳过)
- `decisions.deviations`:`生成`(本任务有 `deviations.md`)
- `decisions.testResults`:**`不生成`**(任务测试状态 = `不适用`,本仓库无可测工程代码;步骤 8.7 守卫触发,步骤 11 跳过)
- `decisions.unitTestResults`:`不生成`(缺陷分支 → 步骤 8a 守卫不触达 → 退化 `testable = False` 沿用 E-4 边界)
- `decisions.kanbanChangeLog`:`生成`(本轮有追加 — 任务完成 + 缺陷状态推进 `修复编码中` → `待审查` + 看板变更记录)
- `decisions.processDocDecisions`:`生成`(存在 3 项"不生成"决策:compileAndRun + testResults + unitTestResults;触发"其他任一'不生成' → 本节生成"规则)

### 8.2 决策结果表

| 过程文档 | 决策 | 理由 |
| --- | --- | --- |
| `work-log.md` | ✅ 生成 | 任务实施日志是核心(始终生成) |
| `compile-and-run.md` | ❌ 不生成 | 本任务为静态校验 + 末尾兜底提交,无构建/运行(changedFiles 全部为 `.md`) |
| `deviations.md` | ✅ 生成 | 评审要查(始终生成);T-004 §偏离 1(PLAN.md 字面歧义)需要记录 |
| `test-results.md` | ❌ 不生成 | 本任务测试状态=不适用(本仓库无可测工程代码) |
| `unit-test-results.md` | ❌ 不生成 | 缺陷分支 → 步骤 8a 守卫不触达 → 退化 `testable = False` 沿用 E-4 边界 |
| 看板"变更记录" | ✅ 生成 | 本轮有追加(任务完成 + 缺陷状态推进) |
| `process-doc-decisions.md` | ✅ 生成 | 存在 3 项"不生成"决策,触发"其他任一'不生成' → 本文件生成"规则 |

### 8.3 决策依据

- `decisions` 字典由 `code-it` 步骤 8.7 物化(`code-it/SKILL.md` line 805+ BUG-00004 T-001 新增)
- 判定准则沿用 `code-it/SKILL.md` "## 过程文档自适应判定"(line 101-138)表格的"判定准则"列
- 步骤 9/10/11 守卫(`code-it/SKILL.md` line 919+ / 928+ / 938+ BUG-00004 T-001 新增)读取 `decisions.compileAndRun` / `decisions.testResults`,触发则跳过对应步骤
- **T-002 / T-003 / T-004 三次执行,守卫均正确跳过**(守卫已稳定生效)
- 退化:步骤 8.7 失败(E-1 / E-5)→ 视为"按原行为执行"(沿用 NFR-4 幂等)

### 8.4 关联任务

- 前置任务(本任务依赖的):TASK-BUG-00004-00001, TASK-BUG-00004-00002, TASK-BUG-00004-00003
- 后置任务(本任务的产出被谁依赖):—
- 取代任务:无
- 关联 code-check / code-unit 链接(若已发起):—

## 9. 单元测试

- 守卫判定:**不可测**(本仓库无可测工程代码;沿用 `code-it` 步骤 8a 守卫)
- 测试框架:N/A
- 新增/修改的测试文件:N/A
- 跑通情况:N/A
- 覆盖率:N/A
- 跳过的子任务:N/A
- 发现的代码 bug:N/A

## 10. 逻辑行统计

> 缺陷分支(`^TASK-BUG-...`)**不**触达步骤 8.6(沿用 NFR-8 强约束)。本字段填"工具检测失败,跳过" + 其他字段为 N/A(沿用模板使用说明)。

- 检测方式:不适用(缺陷分支)
- 阈值默认值:不适用(缺陷分支)
- 用户配置覆盖:不适用(缺陷分支)
- 失败兜底:不适用(缺陷分支)

## 11. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-22 23:00 | v1 | 初始完成 | 完成本任务:7 个技能旁路验证报告(4 个有判定表 / 3 个无判定表;全部"实际过度生成风险" = 低 / 中(0 触发) / 极低 / 无;**均不修复**);与 BUG-00004 详细设计 §6 末字面 100% 一致;**末尾兜底提交累积 T-001 + T-002 + T-003 + T-004 一起 commit**;**BUG-00004 状态推进**:`修复编码中` → `待审查`(由 `itEndStateRollback` 子步骤执行,doneCount=4/totalCount=4);§偏离 1(PLAN.md 字面歧义)+ §偏离 0;**步骤 8.7 守卫 4 任务连续生效** | wangmiao |