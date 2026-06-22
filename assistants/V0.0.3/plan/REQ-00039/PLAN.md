# 编码计划 — REQ-00039 优化 /code-it、/code-check 等技能:代码行数限制仅统计实际逻辑行

- 需求编码:REQ-00039
- 所属版本:V0.0.3
- 上游详细设计:./assistants/V0.0.3/plan/REQ-00039/RESULT.md (v1,2026-06-22 15:00)
- 任务总数:5
- 估算工作量:2-3 天
- 状态:草稿
- 创建:2026-06-22 15:00
- 最近更新:2026-06-22 15:00
- 当前版本:v1

## 1. 计划概述

本计划基于详细设计 `RESULT.md` 的 5 模块详细化 + 4 函数伪代码 + 1 算法聚合,把整项工作拆分为 5 条可独立追踪的 `TASK-REQ-00039-NNNNN` 任务。每条任务有明确的"目标 / 涉及文件 / 关键变更 / 边界与异常 / 验证手段 / 回退方式",严格串行(T-1 → T-2 → T-3 → T-4 → T-5),由 `code-it` 步骤 0a 前置任务守卫按文件行序强制执行。

**任务双状态语义**(沿用既有):**任务"真正可发布" = 开发状态=已完成**;V0.0.3 修订后测试状态字段统一填 `不适用`(`code-it` 步骤 8.5 自含按需写单测守卫判定)。

**触发/来源**:全部任务 = `详细设计`(沿用 REQ-00017 强约束 — **不**出现 `更新看板` 等纯协调类触发源)。

## 2. 任务总览

| 任务编号 | 需求 | 类型 | 触发/来源 | 标题 | 开发状态 | 测试状态 | 涉及文件 | 关联任务 | 估算 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TASK-REQ-00039-00001 | REQ-00039 | 新增 | 详细设计 | [新增] 共享库 logic-loc.md + logic-loc-defaults.md(4 函数伪代码 + 2 阈值字段) | 待开始 | 不适用 | `plugins/code-skills/skills/code-it/lib/logic-loc.md` + `logic-loc-defaults.md` | — | 0.5 天 |
| TASK-REQ-00039-00002 | REQ-00039 | 修改 | 详细设计 | [修改] code-it 步骤 8 末尾追加 detectLocTool + calcLogicLoc 子步骤 + 屏显契约 | 待开始 | 不适用 | `plugins/code-skills/skills/code-it/SKILL.md` | T-1 | 0.5 天 |
| TASK-REQ-00039-00003 | REQ-00039 | 修改 | 详细设计 | [修改] code-check 步骤 8.13 新增 + 评审维度速查表第 13 维度 | 待开始 | 不适用 | `plugins/code-skills/skills/code-check/SKILL.md` | T-1 | 0.5 天 |
| TASK-REQ-00039-00004 | REQ-00039 | 修改 | 详细设计 | [修改] code-it/templates/RESULT.md 模板新增"## 逻辑行统计"小节示例 | 待开始 | 不适用 | `plugins/code-skills/skills/code-it/templates/RESULT.md` | T-2 | 0.25 天 |
| TASK-REQ-00039-00005 | REQ-00039 | 文档 | 详细设计 | [文档] 端到端验证 AC-1 ~ AC-8 + 末尾兜底提交 | 待开始 | 不适用 | (无生产代码改动) | T-1 ~ T-4 | 0.5 天 |

> **任务双状态字段解释**:
> - **开发状态**:6 枚举(`待开始` / `进行中` / `已完成` / `已取消` / `阻塞` / `待重新评估`)
> - **测试状态**:沿用 V0.0.3 修订 — 2 选 1(`已运行-通过` / `不适用`);本需求 5 任务统一填 `不适用`(纯文档 / 配置变更任务,**不**写单测;由 `code-it` 步骤 8.5 自含按需写单测判定)

## 3. 任务详情

### TASK-REQ-00039-00001:[新增] 共享库 logic-loc.md + logic-loc-defaults.md

- **目标**:新建 2 个共享库文档,定义逻辑行计算的 4 个核心函数 + 2 个阈值默认值
- **涉及文件**:
 - `plugins/code-skills/skills/code-it/lib/logic-loc.md`(新建)
 - `plugins/code-skills/skills/code-it/lib/logic-loc-defaults.md`(新建)
- **关键变更**(语义化定位):
 - C-lib-1:`logic-loc.md` 包含 4 个函数伪代码(`detectLocTool` / `calcLogicLines` / `heuristicLoc` / `code-check-exceed`)+ 检测机制 + 启发式算法
 - C-lib-2:`logic-loc-defaults.md` 包含 2 个阈值字段(单文件总规模 ≤ 500 / 新增 ≤ 200)
- **边界与异常**:
 - **E-1**:新建在 `code-it/lib/` 而非 `code-it/templates/`(沿用 `module-conventions §规则 1`)
 - **E-2**:本任务**不**触发 `dashboard-conventions §规则 1` 三同步(无看板列变更)
- **验证手段**:
 - **AC-7**:`code-it` / `code-check` frontmatter 字节级保留(本任务**不**改 SKILL.md,**不**触发该校验,但任务完成时统一校验)
 - 文件存在性:`Bash: test -f plugins/code-skills/skills/code-it/lib/logic-loc.md`
 - 字段完整性:grep `detectLocTool` / `calcLogicLines` / `heuristicLoc` / `code-check-exceed` 4 个函数名均命中
- **回退方式**:`Bash: rm -f plugins/code-skills/skills/code-it/lib/logic-loc.md plugins/code-skills/skills/code-it/lib/logic-loc-defaults.md`

### TASK-REQ-00039-00002:[修改] code-it 步骤 8 末尾追加 detectLocTool + calcLogicLoc 子步骤 + 屏显契约

- **目标**:在 `code-it/SKILL.md` §"## 步骤 8 实施开发"末尾追加 2 个子步骤
- **涉及文件**:
 - `plugins/code-skills/skills/code-it/SKILL.md`
- **关键变更**(语义化定位):
 - C-it-1:`code-it/SKILL.md` §"## 步骤 8 实施开发"末尾追加 `### 步骤 8.X — 逻辑行统计(由 code-it 内化)`(沿用库 §函数 1 + §函数 2)+ 屏显契约
 - C-it-2:步骤 8 末尾子步骤**不**修改既有步骤 8 子步骤结构(字节级沿用)
 - C-it-3:缺陷分支(`^TASK-BUG-...`)**不**触达(NFR-8)子步骤触发条件
- **边界与异常**:
 - **E-1**:既有 `code-it/SKILL.md` frontmatter L1-3 字节级保留(`skill-conventions §规则 1`)
 - **E-2**:既有"## 工作流程"小节 / "## 不要做的事"小节字节级保留
 - **E-3**:既有 `code-it/SKILL.md` 步骤 8a / 8.5(REQ-00034 + REQ-00038 改造)字节级保留
- **验证手段**:
 - **AC-1**:调 `code-it TASK-REQ-NNNNN-NNNNN` → `code/<TASK-...>/RESULT.md` 新增"## 逻辑行统计"小节
 - **AC-6**:调 `code-it TASK-BUG-NNNNN-NNNNN` → 缺陷分支完全跳过 `calcLogicLoc`
 - **AC-7**:`code-it/SKILL.md` frontmatter L1-3 字节级保留
- **回退方式**:`Bash: git revert HEAD`(单 commit 模式);若发现步骤 8 末尾子步骤误改其他位置,人工还原 line 1167+ 末尾的字面

### TASK-REQ-00039-00003:[修改] code-check 步骤 8.13 新增 + 评审维度速查表第 13 维度

- **目标**:在 `code-check/SKILL.md` §"## 步骤 8 逐任务评审"末尾追加 1 个子步骤 + 评审维度速查表新增 1 维度
- **涉及文件**:
 - `plugins/code-skills/skills/code-check/SKILL.md`
- **关键变更**(语义化定位):
 - C-check-1:`code-check/SKILL.md` §"## 步骤 8 逐任务评审"末尾(line 524 后)追加 `### 步骤 8.13 — 代码行数超标检查`(沿用库 §函数 4)+ 派生发现格式
 - C-check-2:`code-check/SKILL.md` §"## 评审维度速查表"(line 588 后,既有 12 维度表后)新增第 13 行 `P3 | 代码行数超标 | 可选 / 建议改 / 必须改`
 - C-check-3:既有 `code-check/SKILL.md` 步骤 8.1 ~ 8.12 字节级保留(沿用 `code-check` 8.12 行数比例警告格式)
- **边界与异常**:
 - **E-1**:既有 `code-check/SKILL.md` frontmatter L1-3 字节级保留
 - **E-2**:既有"## 工作流程"小节 / "## 不要做的事"小节字节级保留
- **验证手段**:
 - **AC-4**:调 `code-check` 评审 1 个 600 行单文件 → 派生"代码行数超标"发现(P3,级别"建议改")
 - **AC-5**:用户配置阈值 300 → 400 行单文件触发"建议改"
 - **AC-7**:`code-check/SKILL.md` frontmatter L1-3 字节级保留
 - **AC-9**:`code-check REQ-NNNNN` 既有行为字节级不变(步骤 8.1 ~ 8.12 字节级沿用)
- **回退方式**:`Bash: git revert HEAD`(单 commit 模式);若发现步骤 8.13 误改其他位置,人工还原 line 524 后追加的字面

### TASK-REQ-00039-00004:[修改] code-it/templates/RESULT.md 模板新增"## 逻辑行统计"小节示例

- **目标**:在 `code-it/templates/RESULT.md` 既有章节中新增"## 逻辑行统计(由 code-it 内化)"小节示例
- **涉及文件**:
 - `plugins/code-skills/skills/code-it/templates/RESULT.md`
- **关键变更**(语义化定位):
 - C-tpl-1:`code-it/templates/RESULT.md` §"## 单元测试(由 code-it 内化)"小节后(line N+1)新增"## 逻辑行统计(由 code-it 内化)"小节示例
 - C-tpl-2:既有"## 单元测试"小节字节级保留;既有其他章节字节级保留
- **边界与异常**:
 - **E-1**:既有模板其他章节字节级保留(沿用 `skill-conventions §规则 1`)
 - **E-2**:不触发 `dashboard-conventions §规则 1` 三同步(无看板列变更)
- **验证手段**:
 - **AC-1**(部分):模板示例展示 `## 逻辑行统计` 小节格式 + 屏显契约
 - 文件存在性:`Bash: test -f plugins/code-skills/skills/code-it/templates/RESULT.md`
 - 字段完整性:`grep "逻辑行(新增)"` + `grep "逻辑行(总规模)"` + `grep "检测方式"` 均命中
- **回退方式**:`Bash: git revert HEAD`(单 commit 模式)

### TASK-REQ-00039-00005:[文档] 端到端验证 AC-1 ~ AC-8 + 末尾兜底提交

- **目标**:验证 4 个修改任务(T-1 ~ T-4)落地后满足 AC-1 ~ AC-8 全部验收标准;末尾兜底提交
- **涉及文件**:
 - (无生产代码改动;仅验证)
- **关键变更**:
 - **不**修改任何 SKILL.md / templates/
 - 验证步骤:
 1. 静态 AC 校验(对照 §5 伪代码 + §6 关键变更字面)
 2. 调 `/code-dashboard` 看段 3 屏显(确认未被本需求影响)
 3. 跑 AC-1 ~ AC-8 全部 8 条验收
- **边界与异常**:
 - **E-1**:AC-1 ~ AC-8 任一条不通过 → 不提交,修复后重跑
 - **E-2**:历史 BUG 状态保留 — 验证完不修改 `BUG-00001 / 02 / 03` 的文件内容(沿用 NFR-3)
- **验证手段**:沿用 `risk-analysis.md` §"测试要点" AC-1 ~ AC-8 全部 8 条
- **回退方式**:若 1 个或多个 AC 不通过,**不**提交;回到对应任务(T-1 ~ T-4)修复

## 4. 任务依赖图

```
T-1 ──────┬─────────┬─────────┐
          ↓         ↓         ↓
         T-2       T-3       T-4
          ↓         ↓
          └────→ T-5(端到端验证 + 末尾兜底)
```

**依赖关系表**:

| 任务 | 依赖 | 备注 |
| --- | --- | --- |
| T-1 | — | 入口任务;定义共享库 4 函数 + 2 阈值字段 |
| T-2 | T-1 | `code-it` 步骤 8 末尾调用 `logic-loc.md` §函数 1 + §函数 2 |
| T-3 | T-1 | `code-check` 步骤 8.13 调用 `logic-loc.md` §函数 4 |
| T-4 | T-2 | 模板新增"## 逻辑行统计"小节示例,引用 T-2 子步骤约定 |
| T-5 | T-1 ~ T-4 | 端到端验证依赖前 4 任务的代码落地 |

**并行性**:T-2 / T-3 之间**无依赖**(可并行);T-4 依赖 T-2;T-5 依赖 T-1 ~ T-4。本计划按串行执行(`code-it` 步骤 0a 前置任务守卫按文件行序强制执行)。

## 5. 里程碑

| 里程碑 | 包含任务 | 完成定义 | 状态 | 计划时间 | 实际完成 |
| --- | --- | --- | --- | --- | --- |
| M1-REQ-00039 | T-1 ~ T-5(全部 5 任务) | 5 任务开发状态=已完成 ∧ 测试状态=不适用;AC-1 ~ AC-8 全通过;1 次末尾兜底提交落地 | 待开始 | 2026-06-22(2-3 天) | — |

## 6. 状态管理规则

### 6.1 双状态字段语义(沿用既有)

- **开发状态**:6 枚举(`待开始` / `进行中` / `已完成` / `已取消` / `阻塞` / `待重新评估`)
- **测试状态**:沿用 V0.0.3 修订 — 2 选 1(`已运行-通过` / `不适用`);本需求 5 任务统一填 `不适用`(纯文档 / 配置变更任务,**不**写单测;由 `code-it` 步骤 8.5 自含按需写单测守卫判定)
- **任务"真正可发布" = 开发状态=已完成**

### 6.2 状态变更规则(沿用既有)

- **任务初始状态**:开发状态=`待开始`;测试状态=`不适用`
- **任务完成流程**:开发状态 `待开始` → `进行中` → `已完成`;测试状态维持 `不适用`
- **任务取消**:用户主动调 `code-plan` 增量更新 → 任务标 `已取消`(开发状态)
- **任务阻塞**:用户报告阻塞原因 → 任务标 `阻塞`(开发状态);解除后回 `进行中`

### 6.3 触发/来源字段(沿用既有 13 枚举)

- 本需求 5 任务全部填 `详细设计`(沿用 REQ-00017 强约束 — **不**出现 `更新看板` 等纯协调类)

## 7. 关联计划

| 关联计划 | 关联点 | 影响 |
| --- | --- | --- |
| REQ-00034 | `code-unit` 整合进 `code-it`(步骤 8a / 8.5) | 本计划**不**修改(沿用既有);新增逻辑行 metadata 与单测 metadata 协同(同 `code/<task>/RESULT.md`) |
| REQ-00037 | 缺陷修复流程的状态推进(`code-fix` / `code-plan` / `code-it` / `code-check` 5 处 `*StateRollback`) | 本计划**不**涉及缺陷路径(沿用既有 `code-it` §缺陷分支 17-25);缺陷分支不触达 `calcLogicLoc`(NFR-8) |
| REQ-00038 | `code-it` 步骤 8a / 8.5 模块级单测 | 本计划**不**修改(沿用既有);与本计划"步骤 8 末尾新增 `calcLogicLoc`"协同(步骤 8a → 8.5 → 步骤 8 末尾) |
| REQ-00022 | `code-review` → `code-check` 重命名 | 本计划沿用既有 `code-check` SKILL.md |

## 8. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-22 15:00 | v1 | 初始创建 | 完成首次编码计划;5 任务严格串行;AC-1 ~ AC-8 全部纳入 T-5 验证;`--balanced` + 功能性=高 + 健壮性=高 + 可维护性=高 | 用户 |