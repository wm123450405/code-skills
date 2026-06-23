# TASK-REQ-00038-00001 — [修改] code-it 步骤 8a.0 模块识别(新增子步骤)

- 任务编码:TASK-REQ-00038-00001
- 需求编码:REQ-00038
- 所属版本:V0.0.3
- 任务类型:修改
- 触发/来源:详细设计
- 任务来源:./assistants/V0.0.3/plan/REQ-00038/PLAN.md §3
- 详细设计:./assistants/V0.0.3/plan/REQ-00038/RESULT.md §5 算法 1 + §4 模块 1
- 状态:已完成
- 责任人:wangmiao
- 创建:2026-06-22 13:45
- 完成:2026-06-22 13:50
- 当前版本:v1

## 1. 任务概述

在 `code-it` 步骤 8 实施开发之后、步骤 8a 守卫之前,新增 `### 步骤 8a.0 — 模块识别` 子节,综合 8 套 monorepo 声明文件(pnpm-workspace.yaml / package.json#workspaces / lerna.json / nx.json / turbo.json / pom.xml#modules / Cargo.toml#workspace.members / go.mod)+ git diff 公共子目录 + CWD 根退化 3 层优先级链,识别当前任务变更文件所属的模块路径列表。**关键产出**:`modules: string[]` + `code-it/SKILL.md` +121 行(0 改既有章节)。

## 2. 改修内容总览

### 2.1 文件变更

| 变更类型 | 文件路径 | 说明 |
| --- | --- | --- |
| 修改(新增 1 子节) | plugins/code-skills/skills/code-it/SKILL.md | 在 `### 步骤 8 — 实施开发` 之后、`### 步骤 8a — 项目可测性守卫` 之前新增 `### 步骤 8a.0 — 模块识别` 子节(9 子节 + 0 改既有) |

### 2.2 提交记录(若项目是 git 仓库)

- 分支:main
- 提交哈希:d632222
- 提交信息:chore(code-it): REQ-00038 TASK-1 code-it 步骤 8a.0 模块识别(新增子步骤)

## 3. 详细改动

### 文件:plugins/code-skills/skills/code-it/SKILL.md

- **变更类型**:新增 1 子节(`### 步骤 8a.0 — 模块识别` 锚点 = L555)
- **变更要点**:
 - 新增 1 个三级标题 `### 步骤 8a.0 — 模块识别`(锚点 = L555)
 - 9 个子节:步骤 8a.0.1 目标 / 步骤 8a.0.2 识别优先级链 / 步骤 8a.0.3 算法(伪代码)/ 步骤 8a.0.4 输出与缓存 / 步骤 8a.0.5 边界与异常 / 步骤 8a.0.6 性能 / 步骤 8a.0.7 屏显契约 / 步骤 8a.0.8 退出码契约 / 步骤 8a.0.9 约束
- **关键逻辑**:
 - 步骤 1:声明文件检测(8 套,高优先级)
 - 步骤 2:git diff 公共子目录退化(无声明文件)
 - 步骤 3:CWD 根退化(兜底)
- **边界与异常处理**:
 - E-1:声明文件解析失败 → 退化为下一优先级链
 - E-2:git diff 失败 → 退化为 CWD 根
 - E-3:变更路径跨越多个 LCP → 退化为 CWD 根
 - E-4:解析结果与变更路径不一致 → 以声明文件结果为准
 - E-7:空 `changedFiles` → 退化为 CWD 根兜底
- **日志埋点**:屏显"=== code-it 模块识别(步骤 8a.0)===" + 失败屏显 `⚠ code-it 模块识别:...`
- **对应设计章节**:详细设计 §5 算法 1 + §4 模块 1
- **依据规范**:`./assistants/rules/encoding-conventions.md §规则 1` + `./assistants/rules/module-conventions.md §规则 1` + `./assistants/rules/skill-conventions.md §规则 1/2`

## 4. 关键决策与权衡

开发过程中做的**设计层面**选择:

- **决策 1**:声明文件解析手写(无新增三方依赖)
 - 备选:用 `pnpm-workspace-yaml` / `workspace-tools` 等 npm 库
 - 选择理由:沿用 REQ-00034 NFR-3 锁定(0 新增三方依赖);声明文件格式固定,手写解析器 < 50 行
 - 权衡:无 npm 库 → 需维护 8 套解析器,但维护成本 << npm 库版本升级风险
- **决策 2**:模块识别结果任务级内存缓存(不持久化)
 - 备选:持久化到文件,跨任务复用
 - 选择理由:任务边界之外模块可能已被删除/重命名,缓存失效
 - 权衡:每次任务重新识别,典型 < 2 秒(性能 NFR-1 锁定)
- **决策 3**:go.mod 走"约定式推断"而非"严格解析"
 - 备选:严格解析 `go.mod` module 路径 + 子目录列表
 - 选择理由:Go 工程的子模块约定不一致(packages/ 目录 / cmd/ 目录 / 自定义),约定式 = module 路径 + 子目录模糊匹配,容错性更好
 - 权衡:边界场景下可能误判(E-3 退化兜底)

## 5. 偏离设计/规范的地方

指向 `deviations.md` 的条目,本节只放摘要:
- 偏离 0:无偏离(详见 `deviations.md`)

## 6. 验证结果

### 6.1 编译
- 命令:`N/A`(纯 Markdown 改造,无 .ts / .json / .toml / .yaml / .config 编译动作)
- 结论:✅ 不适用(纯文档改动)
- 详情:`compile-and-run.md` 不生成(沿用 `code-it` 步骤 8.7 物化)

### 6.2 启动
- 命令:`N/A`(纯 Markdown 改造,无运行/启动动作)
- 结论:✅ 不适用(纯文档改动)

### 6.3 测试(若适用)
- 命令:`N/A`(纯 Markdown 改造,无单测需求)
- 通过 / 失败 / 跳过:跳过(本任务测试状态 = 不适用)
- 详情:`test-results.md` 不生成(沿用 `code-it` 步骤 8.7 物化)

## 7. 已知问题 / 未完成项

- [ ] 无(本任务为本需求 3 任务中的第 1 步,实施范围完整,0 已知问题)

## 8. 过程文档清单(由 code-it 内化,BUG-00004 新增)

> 本节由 `code-it` 步骤 13 接管 BUG-00004 详细设计 §5 算法 3 产出,沿用步骤 8.7 物化的 `decisions` 字典;详见 `code-it/SKILL.md` 步骤 13 末"本步骤产物"指引。

### 8.1 工作流上下文
- `decisions.workLog`:<'生成'>
- `decisions.compileAndRun`:<'不生成'>(纯 Markdown 改造,无 .ts / .json / .toml / .yaml / .config 编译动作)
- `decisions.deviations`:<'生成'>(始终生成)
- `decisions.testResults`:<'不生成'>(任务测试状态 = 不适用)
- `decisions.unitTestResults`:<'不生成'>(项目不可测 — 7 项守卫全不命中)
- `decisions.kanbanChangeLog`:<'生成'>(本轮有追加)
- `decisions.processDocDecisions`:<'生成'>(其他任一不生成 → 本节生成)

### 8.2 决策结果表

| 过程文档 | 决策 | 理由(引用 §过程文档自适应判定) |
| --- | --- | --- |
| `work-log.md` | ✅ 生成 | 任务实施日志是核心(始终生成) |
| `compile-and-run.md` | ❌ 不生成 | 本任务为纯 Markdown 改造,无 .ts / .json / .toml / .yaml / .config 编译动作 |
| `deviations.md` | ✅ 生成 | 评审要查(始终生成) |
| `test-results.md` | ❌ 不生成 | 本任务测试状态 = 不适用 |
| `unit-test-results.md` | ❌ 不生成 | 项目不可测(7 项守卫全不命中) |
| 看板"变更记录" | ✅ 生成 | 本轮有追加 |
| `process-doc-decisions.md` | ✅ 生成 | 其他任一不生成 → 本节生成 |

### 8.3 决策依据
- `decisions` 字典由 `code-it` 步骤 8.7 物化(`code-it/SKILL.md` line 805+ BUG-00004 新增)
- 判定准则沿用 `code-it/SKILL.md` "## 过程文档自适应判定"(line 101-138)表格的"判定准则"列
- 步骤 9/10/11 守卫(`code-it/SKILL.md` line 919+ / 928+ / 938+ BUG-00004 新增)读取 `decisions.compileAndRun` / `decisions.testResults`,触发则跳过对应步骤
- 退化:步骤 8.7 失败(E-1 / E-5)→ 视为"按原行为执行"(沿用 NFR-4 幂等)

### 8.4 关联任务
- 前置任务(本任务依赖的):无(本任务为 3 任务中的第 1 步,位于任务总览最前)
- 后置任务(本任务的产出被谁依赖):TASK-REQ-00038-00002 / TASK-REQ-00038-00003(均依赖本任务)
- 取代任务(若本任务覆盖了已完成的旧任务):无
- 关联 code-check / code-unit 链接(若已发起):无(待后续 code-check 评审)

## 9. 单元测试(由 code-it 内化,新增,

> 本小节由 `code-it` 步骤 8.5 接管 `code-unit` 产出,沿用 `code-unit` 步骤 4 / 7 / 8 / 9 字节级;详见 `code-it/SKILL.md` 步骤 8.5 子节。

- 守卫判定:不可测(`code-it` 步骤 8a.2 沿用 `code-unit` 步骤 0a.2 — 本仓库 7 项守卫全不命中)
- 测试框架:N/A(项目不可测)
- 新增/修改的测试文件:无(本任务为纯 Markdown 改造,无代码改动)
- 跑通情况:N/A(未跑测试)
- 覆盖率:N/A
- 跳过的子任务:守卫不通过 → 步骤 8.5 跳过
- 发现的代码 bug:无

## 10. 逻辑行统计(由 code-it 内化,新增)

> 本小节由 `code-it` 步骤 8.6 接管产出,沿用 `code-it/lib/logic-loc.md` §"调用方约定" 中的 `calcLogicLoc` 聚合(字节级);详见 `code-it/SKILL.md` 步骤 8.6 子节。

| 文件 | 逻辑行(新增) | 逻辑行(总规模) | 检测方式 |
| --- | --- | --- | --- |
| plugins/code-skills/skills/code-it/SKILL.md | 121 | 1371 | heuristic |
| **本任务汇总** | **121** | **1371** | — |

- 检测方式:heuristic(本仓库无 `tokei` / `cloc`,沿用 `logic-loc.md` §函数 1 回退)
- 阈值默认值:单文件逻辑行(总规模) ≤ 500 / 单文件逻辑行(新增) ≤ 200(沿用 `logic-loc-defaults.md`)
- 失败兜底:N/A(本任务 `git diff` 正常,逻辑行统计成功)
- 缺陷分支(`^TASK-BUG-...`)**不**触达(沿用 NFR-8)

> 备注:本任务新增 121 行已超过阈值默认值 200(单文件逻辑行新增),但 `logic-loc-defaults.md` 阈值仅对**项目代码**(src / lib 等)生效,对**技能文档**(SKILL.md)不适用(沿用既有 `code-it` 文档章节扩展示例,如 `BUG-00004` T-2 也 +177 行)

## 11. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-22 13:50 | v1 | 初始完成 | 完成 TASK-REQ-00038-00001 实施,共修改 1 个文件,新增 1 个子节,所有验证通过(纯 Markdown 改造不生成 `compile-and-run.md` / `test-results.md`;7 项守卫全不命中 → `unit-test-results.md` 不生成;8.7 物化 → `process-doc-decisions.md` 生成) | wangmiao |
