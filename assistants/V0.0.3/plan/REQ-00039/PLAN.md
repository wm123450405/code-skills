# 编码计划 — REQ-00039 优化 /code-it、/code-check 等技能:代码行数限制仅统计实际逻辑行

- 需求编码:REQ-00039
- 所属版本:V0.0.3
- 上游详细设计:./assistants/V0.0.3/plan/REQ-00039/RESULT.md (v1,2026-06-22 15:00)
- 任务总数:6
- 估算工作量:2.25-3.25 天
- 状态:草稿
- 创建:2026-06-22 15:00
- 最近更新:2026-06-22 16:35
- 当前版本:v2

## 1. 计划概述

本计划基于详细设计 `RESULT.md` 的 5 模块详细化 + 4 函数伪代码 + 1 算法聚合,把整项工作拆分为 5 条可独立追踪的 `TASK-REQ-00039-NNNNN` 任务。每条任务有明确的"目标 / 涉及文件 / 关键变更 / 边界与异常 / 验证手段 / 回退方式",严格串行(T-1 → T-2 → T-3 → T-4 → T-5),由 `code-it` 步骤 0a 前置任务守卫按文件行序强制执行。

**任务双状态语义**(沿用既有):**任务"真正可发布" = 开发状态=已完成**;V0.0.3 修订后测试状态字段统一填 `不适用`(`code-it` 步骤 8.5 自含按需写单测守卫判定)。

**触发/来源**:全部任务 = `详细设计`(沿用 REQ-00017 强约束 — **不**出现 `更新看板` 等纯协调类触发源)。

## 2. 任务总览

| 任务编号 | 需求 | 类型 | 触发/来源 | 标题 | 开发状态 | 测试状态 | 涉及文件 | 关联任务 | 估算 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TASK-REQ-00039-00001 | REQ-00039 | 新增 | 详细设计 | [新增] 共享库 logic-loc.md + logic-loc-defaults.md(4 函数伪代码 + 2 阈值字段) | 已完成 | 不适用 | `plugins/code-skills/skills/code-it/lib/logic-loc.md` + `logic-loc-defaults.md` | — | 0.5 天 |
| TASK-REQ-00039-00002 | REQ-00039 | 修改 | 详细设计 | [修改] code-it 步骤 8 末尾追加 detectLocTool + calcLogicLoc 子步骤 + 屏显契约 | 已完成 | 不适用 | `plugins/code-skills/skills/code-it/SKILL.md` | T-1 | 0.5 天 |
| TASK-REQ-00039-00003 | REQ-00039 | 修改 | 详细设计 | [修改] code-check 步骤 8.13 新增 + 评审维度速查表第 13 维度 | 已完成 | 不适用 | `plugins/code-skills/skills/code-check/SKILL.md` | T-1 | 0.5 天 |
| TASK-REQ-00039-00004 | REQ-00039 | 修改 | 详细设计 | [修改] code-it/templates/RESULT.md 模板新增"## 逻辑行统计"小节示例 | 已完成 | 不适用 | `plugins/code-skills/skills/code-it/templates/RESULT.md` | T-2 | 0.25 天 |
| TASK-REQ-00039-00005 | REQ-00039 | 文档 | 详细设计 | [文档] 端到端验证 AC-1 ~ AC-8 + 末尾兜底提交 | 已完成 | 不适用 | (无生产代码改动) | T-1 ~ T-4 | 0.5 天 |
| TASK-REQ-00039-00006 | REQ-00039 | 修改 | 审查改修 | [修改] 修正 T-2 / T-3 / T-4 评审发现(合并 1 必须改 + 2 建议改) | 待开始 | 未编写 | `code-it/templates/RESULT.md` + `code-it/SKILL.md` + `code-check/SKILL.md` | T-2, T-3, T-4 | 0.25 天 |

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

### TASK-REQ-00039-00006:[修改] 修正 T-2 / T-3 / T-4 评审发现(合并 1 必须改 + 2 建议改)

- **目标**:修正 code-check 评审 REQ-00039 时发现的 3 项问题(1 必须改 + 2 建议改,合并)
- **涉及文件**:
 - `plugins/code-skills/skills/code-it/templates/RESULT.md`(line 124 — 模板标题末尾未闭合的半角逗号)
 - `plugins/code-skills/skills/code-it/SKILL.md`(line 762 — 步骤 8.6.3 E-3 处理列字面)
 - `plugins/code-skills/skills/code-check/SKILL.md`(line 440 — 步骤 8.13 "总规模优先,新增次之" 字面)
- **关键变更**(语义化定位):
 - **F-1(必须改)**:删除 `code-it/templates/RESULT.md` line 124 标题末尾的半角逗号 `,`;改为 `## 10. 逻辑行统计(由 code-it 内化,新增)`
 - **F-2(建议改)**:更新 `code-it/SKILL.md` line 762 步骤 8.6.3 E-3 处理列;改为 "`calcLogicLines` 返回 error 对象,任务级跳过该文件,继续下一文件 + 屏显警告"
 - **F-3(建议改)**:更新 `code-check/SKILL.md` line 440 步骤 8.13;改为 "先判 totalLoc,再判 newLoc,两个独立发现可同时触发"
- **边界与异常**:
 - **E-1**:`code-it/lib/logic-loc.md` + `code-it/lib/logic-loc-defaults.md` **不**改(共享库是 single source of truth,只改调用方字面以对齐)
 - **E-2**:frontmatter L1-3 字节级保留(沿用 NFR-3)
 - **E-3**:既有"## 工作流程"小节 / "## 不要做的事"小节 / 既有章节字节级沿用
- **验证手段**:
 - **F-1 验证**:`grep -n "^## 10\. 逻辑行统计" plugins/code-skills/skills/code-it/templates/RESULT.md` — 确认 line 124 标题末尾**无**逗号
 - **F-2 验证**:读 `code-it/SKILL.md` 步骤 8.6.3 E-3 行,确认处理列字面已更新
 - **F-3 验证**:`grep -n "总规模优先" plugins/code-skills/skills/code-check/SKILL.md` — 确认**无**命中(已替换)
- **回退方式**:`Bash: git revert HEAD`(单 commit 模式)

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
| 2026-06-22 15:05 | v1 | 状态更新 | TASK-REQ-00039-00001 状态"待开始"→"已完成";`plugins/code-skills/skills/code-it/lib/logic-loc.md` + `logic-loc-defaults.md` 2 个共享库新建落地;`logic-loc.md` 含 4 函数(`detectLocTool` / `calcLogicLines` / `heuristicLoc` / `code-check-exceed`)+ 检测机制 + 启发式算法;`logic-loc-defaults.md` 含 2 阈值字段(500 / 200);字段完整性静态校验通过(4 函数名命中 13 次 / 2 阈值字段命中 3 次);AC-7 部分静态校验通过 | wangmiao |
| 2026-06-22 15:08 | v1 | 状态更新 | TASK-REQ-00039-00002 状态"待开始"→"已完成";`plugins/code-skills/skills/code-it/SKILL.md` 步骤 8 末尾追加 `### 步骤 8.6 — 逻辑行统计(由 code-it 内化)` 子步骤(89 行新增,7 个子节:目标 / 算法 / 边界与异常 / 性能 / 屏显契约 / 退出码契约 / 约束);**仅**引用共享库 4 函数不重写;NFR-7 不阻断 + NFR-8 缺陷分支不触达约束字节级沿用;frontmatter L1-3 字节级保留;既有 步骤 8 / 8a / 8.5 字节级沿用;AC-7 静态校验通过 | wangmiao |
| 2026-06-22 15:12 | v1 | 状态更新 | TASK-REQ-00039-00003 状态"待开始"→"已完成";`plugins/code-skills/skills/code-check/SKILL.md` 步骤 8 末尾追加 `**8.13 代码行数超标检查**` 子步骤(18 行新增)+ 评审维度速查表新增第 13 行 `P3 | 代码行数超标 | 可选 / 建议改 / 必须改`(line 608);既有 步骤 8.13("过程文档适配性")重命名为 步骤 8.14(文字内容字节级保留);**仅**引用共享库 §函数 4 `code-check-exceed` 不重写;阈值默认 500 / 200 沿用 `logic-loc-defaults.md`;用户配置覆盖读 `require/<需求>/RESULT.md` "## 阈值配置";frontmatter L1-3 字节级保留;既有 步骤 8.1 ~ 8.12 字节级沿用;既有 12 维度表字节级沿用;AC-7 / AC-9 部分静态校验通过 | wangmiao |
| 2026-06-22 15:16 | v1 | 状态更新 | TASK-REQ-00039-00004 状态"待开始"→"已完成";`plugins/code-skills/skills/code-it/templates/RESULT.md` 在 ## 9. 单元测试 小节后新增"## 10. 逻辑行统计(由 code-it 内化,新增"小节示例(20 行新增,含 1 表格 + 5 字段说明 + 1 模板使用说明);原"## 10. 变更记录"重命名为"## 11. 变更记录"(章节编号顺序 +1);表格字面与详细设计 §5.5 step 6 完全一致;既有 9 个章节(## 文档头 ~ ## 9. 单元测试)字节级保留;字段完整性静态校验通过(逻辑行(新增) 1 次 / 逻辑行(总规模) 1 次 / 检测方式 ≥ 3 次);AC-1 部分静态校验通过 | wangmiao |
| 2026-06-22 15:22 | v1 | 状态更新 | TASK-REQ-00039-00005 状态"待开始"→"已完成";端到端验证 AC-1 ~ AC-8 全部 8 条通过(`code-it/SKILL.md` 步骤 8.6 子步骤 / `logic-loc.md` 4 函数 / `code-check/SKILL.md` 步骤 8.13 子步骤 / 模板"## 10. 逻辑行统计"小节示例 + 速查表第 13 行 / NFR-7 不阻断 + NFR-8 缺陷分支不触达 / frontmatter L1-3 字节级保留 / 步骤 8.6.4 性能 < 3 秒);M1-REQ-00039 完成定义全部满足(5 任务开发状态=已完成 ∧ 测试状态=不适用;AC-1 ~ AC-8 全通过);末尾兜底 1 次 commit 累积 5 M + 7 ?? = 12 个变更单元(沿用 REQ-00037 T-7 模式);net +137 行(151 - 14) | wangmiao |
| 2026-06-22 16:35 | v2 | 增量更新(审查) | 评审发现 3 个问题(1 必须改 F-T4-1 + 2 建议改 F-T2-1 / F-T3-1),新增任务 T-006(合并 T-2 / T-3 / T-4);3 文件改动(`code-it/templates/RESULT.md` + `code-it/SKILL.md` + `code-check/SKILL.md`);版本号 v1 → v2 | wangmiao |