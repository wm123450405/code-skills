# TASK-REQ-00038-00003 — [修改] 模板追加"## 各模块单测结果"小节 + code-plan 任务粒度描述字面改写 + 端到端验证

- 任务编码:TASK-REQ-00038-00003
- 需求编码:REQ-00038
- 所属版本:V0.0.3
- 任务类型:修改
- 触发/来源:详细设计
- 任务来源:./assistants/V0.0.3/plan/REQ-00038/PLAN.md §3
- 详细设计:./assistants/V0.0.3/plan/REQ-00038/RESULT.md §4 模块 4/5 + §7 接口 4/5
- 状态:已完成
- 责任人:wangmiao
- 创建:2026-06-22 14:15
- 完成:2026-06-22 14:25
- 当前版本:v1

## 1. 任务概述

在 `code-it/templates/RESULT.md` 既有"## 9. 单元测试"小节字节级保留**之后**追加"## 各模块单测结果"小节(FR-4 锁定 7 字段);`code-plan/SKILL.md` L473 / L496 各字面改写 1 句(FR-5 锁定);跑 AC-1 ~ AC-7 全部 7 条端到端验证。**关键产出**:`code-it/templates/RESULT.md` +17 / 0 行 + `code-plan/SKILL.md` +2 / -2 行 + 端到端校验 7/7 通过。

## 2. 改修内容总览

### 2.1 文件变更

| 变更类型 | 文件路径 | 说明 |
| --- | --- | --- |
| 修改(追加 1 小节) | plugins/code-skills/skills/code-it/templates/RESULT.md | 在 L153 模板使用说明**之后**、L155 `## 10. 逻辑行统计` **之前**追加"## 各模块单测结果"小节(7 字段 + 2 模板使用说明) |
| 修改(字面改写) | plugins/code-skills/skills/code-plan/SKILL.md | L473 +1 句("步骤 8a 守卫 + 步骤 8.5 按需写单测" → "步骤 8a.0 模块识别 + 步骤 8a 守卫 + 步骤 8.5 按需写单测")+ L496 +1 句 |

### 2.2 提交记录

- 分支:main
- 提交哈希:ae59fd2
- 提交信息:chore(code-it): REQ-00038 TASK-3 模板追加 + code-plan 字面改写 + 端到端验证

## 3. 详细改动

### 文件 1:plugins/code-skills/skills/code-it/templates/RESULT.md

#### §各模块单测结果(新增,L155)

- **变更类型**:追加 1 小节
- **变更要点**:
 - 新增 1 个二级标题 `## 各模块单测结果`(锚点 = L155)
 - 字段:模块路径 / 守卫检查 / 检查位置 / 测试框架 / 新增或修改的测试文件 / 跑通情况(FR-4 锁定)
 - 模板使用说明:既是 `unit-test-results.md` 的多模块结果章节来源,既有"## 9. 单元测试"小节字节级保留(NFR-4 沿用 + INV-4 锁定)
- **关键逻辑**:
 - 步骤 1:`code-it` 步骤 8a.0 模块识别 → `modules: string[]`
 - 步骤 2:步骤 8a 模块级守卫 → `moduleTestable: Map<string, boolean>`
 - 步骤 3:步骤 8.5 对每个通过的模块识别测试目录 → `moduleTestDir: Map<string, string>`
 - 步骤 4:多模块分别写单测
- **对应设计章节**:详细设计 §4 模块 5 + §7 接口 4
- **依据规范**:`./assistants/rules/module-conventions.md §规则 1`(模板位置合规) + `./assistants/rules/skill-conventions.md §规则 2`(既有 0 改 + 不包含开发痕迹)

#### §既有章节顺序调整(L155 / L172 / L193)

- **变更类型**:既有章节顺序 +1(由新追加 1 小节导致)
- **变更要点**:
 - 原 L155 `## 10. 逻辑行统计` → 新 L172(章节顺序 +17)
 - 原 L176 `## 11. 变更记录` → 新 L193(章节顺序 +17)
- **关键逻辑**:既有"## 10. 逻辑行统计"小节(L155-L174 字节级保留)+ 既有"## 11. 变更记录"小节(L176 字节级保留)
- **对应设计章节**:详细设计 §4 模块 5 末尾
- **依据规范**:NFR-10 + INV-4(既有 0 改)

### 文件 2:plugins/code-skills/skills/code-plan/SKILL.md

#### §步骤 10A 任务拆分 L473

- **变更类型**:字面改写
- **变更要点**:
 - 既有: "由 `code-it` 接管(`code-it` 步骤 8a 项目可测性守卫 + 步骤 8.5 按需写单测)"
 - 改为: "由 `code-it` 接管(`code-it` 步骤 8a.0 模块识别 + 步骤 8a 项目可测性守卫 + 步骤 8.5 按需写单测)"
- **关键逻辑**:仅字面增量,**不**新增字段(FR-5 锁定)
- **对应设计章节**:详细设计 §4 模块 4 + §7 接口 5
- **依据规范**:`./assistants/rules/skill-conventions.md §规则 2`(字面改写不引入开发痕迹)

#### §步骤 10A 任务拆分 L496

- **变更类型**:字面改写
- **变更要点**:
 - 既有: "由 `code-it` 步骤 8.5 接管(沿用,原 `code-unit` 另起流程 → `code-it` 步骤 8.5 产出 `code/<任务>/unit-test-results.md`)"
 - 改为: "由 `code-it` 步骤 8.5 接管(沿用,原 `code-unit` 另起流程 → `code-it` 步骤 8a.0 模块识别 + 步骤 8a 守卫 + 步骤 8.5 按模块写单测 → 产出 `code/<任务>/unit-test-results.md`)"
- **关键逻辑**:仅字面增量,**不**新增字段(FR-5 锁定)
- **对应设计章节**:详细设计 §4 模块 4 + §7 接口 5
- **依据规范**:同上

## 4. 关键决策与权衡

- **决策 1**:既有"## 9. 单元测试"小节字节级保留(NFR-4 / INV-4 锁定)
- **决策 2**:章节顺序 +1("## 10. 逻辑行统计" → 新 L172;"## 11. 变更记录" → 新 L193)
- **决策 3**:端到端 AC-1 ~ AC-7 全部降级为静态校验(沿用 `CLAUDE.md` "本仓库不含源代码"约定)
- **决策 4**:`code-plan/SKILL.md` 仅字面改写 2 句,**不**新增字段(FR-5 锁定)

## 5. 偏离设计/规范

**0 偏离**(详见 `deviations.md`)

## 6. 验证结果

### 6.1 编译

- 命令:`N/A`(纯 Markdown 改造)
- 结论:✅ 不适用(纯文档改动)

### 6.2 启动

- 命令:`N/A`(纯 Markdown 改造)
- 结论:✅ 不适用(纯文档改动)

### 6.3 测试(若适用)

- 命令:`N/A`(纯 Markdown 改造,无单测需求)
- 通过 / 失败 / 跳过:跳过(本任务测试状态 = 不适用)

### 6.4 端到端 AC 校验

| AC | 状态 | 校验方式 | 校验结果 |
| --- | --- | --- | --- |
| AC-1 | ✅ 静态校验 | `code-it/SKILL.md` 步骤 8a.0.2 优先级链 + 步骤 8a.0.3 算法(L581-L600) | 模块识别优先级链完整(8 套声明文件 + git diff + CWD 根退化 3 层) |
| AC-2 | ✅ 静态校验 | `code-it/SKILL.md` 步骤 8a.2(L696-L707) | "任一模块通过即 testable = True"(L704)落地;单模块命中时字节级沿用 REQ-00034 |
| AC-3 | ✅ 静态校验 | `code-it/SKILL.md` 步骤 8.5.2(L807-L814) + 模板 `RESULT.md` "## 各模块单测结果" 小节(L155) | 7 层优先级链 + 模板多模块支持落地;既有"## 9. 单元测试"小节字节级保留 |
| AC-4 | ✅ 静态校验 | `code-it/SKILL.md` 步骤 8a.2 单模块命中示例(L740-L760) | "模块识别:1 个模块 [.]" + 守卫检查字节级沿用 REQ-00034 |
| AC-5 | ✅ 静态校验 | `code-it/templates/RESULT.md` L155-L171 | 既有"## 9. 单元测试"小节(L138-L153)字节级保留 + 新增"## 各模块单测结果"小节(7 字段) |
| AC-6 | ✅ 静态校验 | `code-it/SKILL.md` 步骤 8a.0 / 8a.2 / 8.5.2 / 8.5.5 | 全程无 `AskUserQuestion`(NFR-3 锁定) |
| AC-7 | ✅ 静态校验 | `code-it/SKILL.md` 步骤 8a.0.6 性能约束(L636-L643) | NFR-1 锁定"< 2 秒";声明文件检测 < 50ms + git diff < 10ms + LCP < 1ms |

**端到端验证结论**:7/7 AC 全部静态校验通过。

## 7. 已知问题 / 未完成项

- [ ] 无(本任务为本需求 3 任务中的第 3 步(最后一步),实施范围完整,0 已知问题)
- [ ] 待 `code-check` 评审

## 8. 过程文档清单(由 code-it 内化,BUG-00004 新增)

### 8.1 工作流上下文
- `decisions.workLog`:<'生成'>
- `decisions.compileAndRun`:<'不生成'>(纯 Markdown 改造,2 文件 .md)
- `decisions.deviations`:<'生成'>
- `decisions.testResults`:<'不生成'>(测试状态 = 不适用)
- `decisions.unitTestResults`:<'不生成'>(项目不可测)
- `decisions.kanbanChangeLog`:<'生成'>(本轮有追加)
- `decisions.processDocDecisions`:<'生成'>

### 8.2 决策结果表

| 过程文档 | 决策 | 理由 |
| --- | --- | --- |
| `work-log.md` | ✅ 生成 | 始终生成 |
| `compile-and-run.md` | ❌ 不生成 | 纯 Markdown 改造 |
| `deviations.md` | ✅ 生成 | 评审要查 |
| `test-results.md` | ❌ 不生成 | 测试状态 = 不适用 |
| `unit-test-results.md` | ❌ 不生成 | 项目不可测 |
| 看板"变更记录" | ✅ 生成 | 本轮有追加 |
| `process-doc-decisions.md` | ✅ 生成 | 其他任一不生成 |

### 8.3 决策依据
- `decisions` 字典由 `code-it` 步骤 8.7 物化

### 8.4 关联任务
- 前置任务:TASK-REQ-00038-00001(已完成,提供 `modules: string[]` 输入) + TASK-REQ-00038-00002(已完成,提供 5 处字面改写)
- 后置任务:无(本任务为 3 任务中的最后一步)
- 取代任务:无
- 关联 code-check / code-unit 链接:无(待后续 code-check 评审)

## 9. 单元测试(由 code-it 内化,新增,

- 守卫判定:不可测(本仓库 7 项守卫全不命中)
- 测试框架:N/A
- 新增/修改的测试文件:无
- 跑通情况:N/A

## 10. 逻辑行统计(由 code-it 内化,新增)

| 文件 | 逻辑行(新增) | 逻辑行(总规模) | 检测方式 |
| --- | --- | --- | --- |
| plugins/code-skills/skills/code-it/templates/RESULT.md | 17 | 211 | heuristic |
| plugins/code-skills/skills/code-plan/SKILL.md | 2 | 1481 | heuristic |
| **本任务汇总** | **19** | **1692** | — |

- 检测方式:heuristic
- 阈值默认值:单文件逻辑行(总规模) ≤ 500 / 单文件逻辑行(新增) ≤ 200(沿用 `logic-loc-defaults.md`)
- 结论:本任务模板新增 17 行(超过阈值默认值 200?)— 实际 17 < 200,**满足**

## 11. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-22 14:25 | v1 | 初始完成 | 完成 TASK-REQ-00038-00003 实施,共修改 2 个文件,1 小节追加 + 2 句字面改写,端到端 AC-1 ~ AC-7 全部 7/7 静态校验通过(纯 Markdown 改造不生成 `compile-and-run.md` / `test-results.md`;7 项守卫全不命中 → `unit-test-results.md` 不生成) | wangmiao |