# REQ-00019 — 优化 `/code-plan`,BUG 模式产出物与 REQ 模式同构

- 需求编码:REQ-00019
- 所属版本:V0.0.2
- 状态:已锁定
- 责任人:wangmiao
- 创建:2026-06-06
- 最近更新:2026-06-06 14:30
- 当前版本:v1

---

## 1. 需求概述

为 `/code-plan` 技能的**缺陷分支**(输入 `BUG-NNN` 时)统一产出物:**与正常(需求)分支完全同构**——产 `RESULT.md`(详细设计) + `PLAN.md`(任务列表) + 7 份过程文档(`materials-index.md` / `module-details.md` / `interface-specs.md` / `data-changes.md` / `risk-analysis.md` / `rule-compliance.md` / `design-notes.md` + `clarifications.md`);**唯一**区别是上游参考来源——REQ 分支读 `require/<REQ>/RESULT.md` + `design/<REQ>/RESULT.md`,BUG 分支读 `fix/<BUG-NNN>/RESULT.md`。同步改造 `/code-it` BUG 分支(消费方)使输入路径与新产出物对齐,移除 `fix-plan.md` 作为独立"修复方案"文档的定位(本需求后**不再生成** `fix-plan.md`,但 BUG-00001 的历史 `fix-plan.md` 不迁移)。

## 2. 背景与目标

### 2.1 背景(为何提出本需求)

**现状**(V0.0.2 实际):

1. `/code-plan` 技能 SKILL.md 第 588-735 行"缺陷分支"明确说明 BUG 分支产出物是**单文件** `fix-plan.md`(对照 `plugins/code-skills/skills/code-plan/SKILL.md` 步骤 19-28A):
   - 步骤 26A:"按 `templates/fix-plan.md` 的章节结构生成"
   - 步骤 27A / 28A:同步 `fix/<BUG-NNN>/RESULT.md` + `fix/RESULT.md` + 版本看板"缺陷清单"
   - **不**产出 `RESULT.md` / `PLAN.md` / 任何过程文档(沿用 `code-plan/SKILL.md` §"缺陷分支额外禁止" L940-943)
2. `/code-it` BUG 分支(`code-it/SKILL.md` 步骤 17-25)消费方**硬编码**读 `fix-plan.md`:
   - 步骤 17 L650-651:校验 `fix-plan.md` 存在 + 提取"根因定位/修复方案/涉及文件与变更/测试方案"
   - 步骤 22 L689:"按 `fix-plan.md` 中选定的方案展开"
   - 步骤 24 L762-783:同步 `fix/<BUG-NNN>/RESULT.md` + `fix/RESULT.md` + 版本看板(沿用既有)
3. **现行 BUG 流程产出物清单**(以 BUG-00001 为例,实际文件):
   - 主:`fix/BUG-00001/fix-plan.md`(624 行,7 章节) — **唯一**详细设计
   - 辅:`fix/BUG-00001/RESULT.md`(105 行) + `fix/RESULT.md`(23 行) + 版本看板"缺陷清单" + 5 份过程文档(`investigation.md` / `fix-work-log.md` / `fix-compile-and-run.md` / `fix-test-results.md` / `deviations.md`)
   - **缺失**:`fix/BUG-00001/PLAN.md` 不存在,看板上无 `TASK-BUG-00001-00001` 任务登记

**痛点**:
- **认知不对称**:`code-plan` REQ 路径产出 9 份文档(`RESULT.md` + `PLAN.md` + 7 份过程),BUG 路径产出 1 份(`fix-plan.md`),用户心智模型不一致
- **数据对齐困难**:`code-it` 任务路径 / `code-unit` / `code-review` / `code-dashboard` 看板统一基于 `PLAN.md` 任务清单;BUG 任务游离在外
- **缺陷分支与看板任务清单区段脱钩**:`code-dashboard` 看板"任务清单"区段只显示 REQ 任务,BUG 修复进度无统一视图

### 2.2 业务目标

- BUG 修复流程产出物与 REQ 流程**完全同构**(形式、字段、看板位置一致),**仅**参考来源不同
- BUG 任务(`TASK-BUG-NNNNN-NNNNN`)进版本看板"任务清单"区段,触发/来源=缺陷修复
- `/code-it` BUG 分支消费方与新产出物对齐(读 `PLAN.md` / `RESULT.md` 而非 `fix-plan.md`)
- 0 触发 `dashboard-conventions §规则 1` 三同步(沿用既有"任务清单"区段,字段不变,枚举值不变)

### 2.3 本次目标(本迭代范围)

1. `/code-plan` 缺陷分支步骤 19-28A 重构:产出 `RESULT.md` + `PLAN.md` + 7 份过程文档;`fix-plan.md` 退场(本需求后**不**再生成)
2. `/code-it` 缺陷分支(步骤 17-25)联动改造:读 `PLAN.md` / `RESULT.md`,过程文档去 `fix-` 前缀,frontmatter 同步
3. 新增 BUG 任务编号格式 `TASK-BUG-NNNNN-NNNNN`(5+5 位,与既有 `TASK-REQ-NNNNN-NNNNN` 同构)
4. BUG 任务进"任务清单"区段(原区段收录,不新增独立区段,不触发 §规则 1 三同步)
5. **不**迁移历史 BUG-00001(用户确认仅未来新缺陷生效)

## 3. 用户角色与场景

### 3.1 角色:wangmiao(项目负责人,缺陷登记人 + 修复规划人 + 实施人 + 验证人,4 合 1)

### 3.2 场景

| 场景 | 用户故事 | 前置条件 | 主流程 |
| --- | --- | --- | --- |
| S-1:小 BUG(单文件改) | 作为 wangmiao,我希望小 BUG 修复也走标准 `PLAN.md` 流程,这样修复历史可追溯 | `code-fix` 已登记 `BUG-00010`(单文件改 1 处) | 调 `code-plan BUG-00010` → 产出 `fix/BUG-00010/RESULT.md` + `PLAN.md` + 7 份过程文档 + 看板"任务清单" + 1 行 `TASK-BUG-00010-00001` |
| S-2:大 BUG(多文件) | 作为 wangmiao,我希望大 BUG 修复可拆为多任务,逐步推进 | `code-fix` 已登记 `BUG-00011`(预计 3 个文件改动) | 调 `code-plan BUG-00011` → 产出 `RESULT.md` + `PLAN.md` 含 `TASK-BUG-00011-00001/00002/00003` 三个任务 + 看板"任务清单"3 行 |
| S-3:`code-it` 实施 | 作为 wangmiao,我希望 `code-it` 实施 BUG 修复时,过程文档与 REQ 任务同套 | `code-plan BUG-00010` 已产出 | 调 `code-it TASK-BUG-00010-00001` → 读 `fix/BUG-00010/PLAN.md`(主) + `RESULT.md`(辅) + 产出 `code/TASK-BUG-00010-00001/{work-log,compile-and-run,test-results,deviations}.md`(无 `fix-` 前缀) |
| S-4:`code-dashboard` 看板 | 作为 wangmiao,我希望看板"任务清单"区段同时显示 BUG 任务 | BUG 任务已拆分登记 | 调 `code-dashboard` → 看板"任务清单"区段显示 `TASK-BUG-00010-00001` 等 |
| S-5:`code-review` 评审 | 作为 wangmiao,我希望 `code-review` 对 BUG 修复做正式评审 | `code-it` 已完成 BUG 任务 | 调 `code-review BUG-00010` → 按既有 REQ 路径同构评审(读 `fix/BUG-00010/PLAN.md` 任务总览) |
| S-6:历史 BUG-00001 保留 | 作为 wangmiao,我希望 BUG-00001 的现有 `fix-plan.md` 不被破坏 | BUG-00001 已修复-待验证 | 不主动迁移;`code-it` 路径仅对 V0.0.2 未来新 BUG 生效 |

## 4. 功能需求(FR)

### FR-1:`code-plan` 缺陷分支产出 `RESULT.md` + `PLAN.md` + 7 份过程文档

- **描述**:在 `/code-plan` 缺陷分支(步骤 19-28A)中,**废弃** `fix-plan.md` 作为主详细设计文档的定位;改为产出与 REQ 分支同构的 9 份文档:
  - `fix/<BUG-NNN>/RESULT.md`(详细设计)
  - `fix/<BUG-NNN>/PLAN.md`(任务列表)
  - `fix/<BUG-NNN>/materials-index.md`
  - `fix/<BUG-NNN>/module-details.md`
  - `fix/<BUG-NNN>/interface-specs.md`
  - `fix/<BUG-NNN>/data-changes.md`
  - `fix/<BUG-NNN>/risk-analysis.md`
  - `fix/<BUG-NNN>/rule-compliance.md`
  - `fix/<BUG-NNN>/design-notes.md`
  - `fix/<BUG-NNN>/clarifications.md`(可选)
- **入口**:用户调 `/code-plan <BUG-NNN>` 触发
- **前置条件**:`./assistants/<版本号>/fix/<BUG-NNN>/RESULT.md` 存在(由 `code-fix` 登记)
- **主流程**:
  1. `code-plan` 步骤 19-22:读 `fix/<BUG-NNN>/RESULT.md` + `fix/<BUG-NNN>/investigation.md`(若有)+ 探索项目代码(同 REQ 步骤 3/5)
  2. `code-plan` 步骤 23:检查 `fix/<BUG-NNN>/RESULT.md` / `PLAN.md` 是否存在
  3. `code-plan` 步骤 24A(首次规划):根因定位 + 修复方案 + 涉及文件 + 测试方案 + 风险与回退 + 修复步骤;**改**为产出 `RESULT.md` + `PLAN.md` + 7 份过程文档(沿用 `code-plan/SKILL.md` §步骤 7A-15A 模板结构,`RESULT.md` 14 章节对齐 `templates/plan.md`,`PLAN.md` 8 章节对齐 `templates/task-plan.md`)
  4. `code-plan` 步骤 26A(撰写文档):废弃原"按 `templates/fix-plan.md` 的章节结构生成"段,改为"按 `templates/plan.md` + `templates/task-plan.md` 同构产出"
  5. `code-plan` 步骤 27A(同步 `fix/<BUG-NNN>/RESULT.md` 与 `fix/RESULT.md`):保留(本需求不修改 `fix/<BUG-NNN>/RESULT.md` 的"缺陷描述/根因分析"等稳定章节;状态推进为"修复规划中"沿用)
  6. `code-plan` 步骤 28A(同步版本看板"缺陷清单"):保留
  7. `code-plan` 步骤 28A+1(新增同步版本看板"任务清单"):本需求**新增** — 在步骤 28A 后追加"同步版本看板'任务清单'区段"(从 `PLAN.md` 任务总览批量登记,**触发/来源**=**缺陷修复**)
- **分支/异常**:
  - **E-1**:`fix-plan.md` 存在(仅 BUG-00001 历史文件)→ 步骤 23 检测到,提示"检测到历史 fix-plan.md,本需求已不再生成该文件;是否继续以本缺陷的 fix-plan.md 为参考?" + 提供 3 选 1(继续/手动迁移/中止)
  - **E-2**:`investigation.md` 不存在 → 步骤 22 退化,根因定位仅依据 `fix/<BUG-NNN>/RESULT.md` 中已有"根因分析(已调查)"段
  - **E-3**:步骤 24A 评估 BUG 修复跨多步 → 在 `PLAN.md` 任务总览中拆分多个 `TASK-BUG-NNNNN-NNNNN` 任务(从 `TASK-BUG-NNNNN-00001` 起递增)
- **数据变化**:
  - `fix/<BUG-NNN>/` 目录新增 8 份文件(`RESULT.md` 已存在则更新,`PLAN.md` 必新增,7 份过程文档可全产出或按需产出)
  - `fix/<BUG-NNN>/fix-plan.md` 退场(本需求后**不**再生成);**E-1** 例外(仅 BUG-00001 历史保留)
  - 版本看板"任务清单"区段追加 BUG 任务行(若有拆分)
- **来源**:本需求 v1 锁定;Q-1 锁定 A(彻底同步升级,去掉 `fix-plan.md`)

### FR-2:`code-plan` 步骤 26A 章节结构沿用 `templates/plan.md` + `templates/task-plan.md`

- **描述**:BUG 分支的 `RESULT.md` 与 `PLAN.md` 章节结构**完全沿用** REQ 分支的模板:
  - `RESULT.md` 14 章节(概述 / 上游引用 / 规范遵循 / 模块详细化 / 算法与逻辑 / 数据结构 / 接口细节 / 异常处理 / 安全 / 状态机 / 性能 / 测试要点 / 关联 / 待澄清 / 变更记录) — 沿用 `plugins/code-skills/skills/code-plan/SKILL.md` 步骤 14A 与 `templates/plan.md`
  - `PLAN.md` 8 章节(计划概述 / 任务总览 / 任务详情 / 任务依赖图 / 里程碑 / 状态管理规则 / 关联计划 / 变更记录) — 沿用 `plugins/code-skills/skills/code-plan/SKILL.md` 步骤 15A 与 `templates/task-plan.md`
- **入口**:FR-1 步骤 24A → 步骤 26A
- **前置条件**:无
- **主流程**:
  1. 步骤 26A 撰写 `RESULT.md`:严格按 `templates/plan.md` 14 章节结构;**关键差异**:第 2 章"上游引用" 写 `fix/<BUG-NNN>/RESULT.md`(缺陷详情) + `fix/<BUG-NNN>/investigation.md`(若有) + 项目级规范
  2. 步骤 26A+1(新增)撰写 `PLAN.md`:严格按 `templates/task-plan.md` 8 章节;**关键差异**:
     - 任务总览"触发/来源"列 = **`缺陷修复`**(新格式,与既有 `触发/来源=需求新增` / `触发/来源=审查改修` 等 13 个枚举值并列)
     - 任务编号前缀 = **`TASK-BUG-`**(新格式,5+5 位嵌套式沿用 `encoding-conventions §规则 1/3`)
     - 任务总览"需求"列 = **`BUG-NNN`**(3 位,与 REQ 任务的 5 位不同)
     - 任务总览"标题"列 = 沿用 REQ-00013 标题解析(字符数 ≤ 30,中点 `·` 格式)
  3. 步骤 26A+2(新增)撰写 7 份过程文档:沿用 `code-plan/SKILL.md` 步骤 7A 的过程文档分工(详细化 / 接口 / 数据 / 风险)
- **分支/异常**:
  - **E-4**:`templates/plan.md` 14 章节中"安全要求" / "状态机" / "性能与资源"等若 BUG 修复不涉及 → 章节保留但内容写"不适用(本修复聚焦代码改动,不涉及该维度)"
- **数据变化**:`fix/<BUG-NNN>/` 目录下 9 份文档的结构与 REQ 分支完全同构
- **来源**:本需求 v1 锁定;Q-2 锁定 A(章节结构与 REQ 模式一致)

### FR-3:BUG 任务进版本看板"任务清单"区段(原区段收录)

- **描述**:BUG 任务(`TASK-BUG-NNNNN-NNNNN`)作为看板"任务清单"区段的一类行,与 REQ 任务同表展示;**不**新增独立"缺陷任务"区段(避免触发 `dashboard-conventions §规则 1` 三同步)
- **入口**:`code-plan` 步骤 28A+1(FR-1 新增)
- **前置条件**:`PLAN.md` 任务总览存在
- **主流程**:
  1. `code-plan` 步骤 28A+1 读 `PLAN.md` 任务总览
  2. 在版本看板 `assistants/<版本号>/RESULT.md` "任务清单" 区段批量追加(每条 BUG 任务一行)
  3. 行字段(任务编号 / 需求 / 类型 / 触发/来源 / 标题 / 开发状态 / 测试状态 / 涉及文件 / 完成时间 / 提交哈希 / 关联任务)与 REQ 任务行同构
  4. 关键字段填法:
     - **任务编号**:`TASK-BUG-NNNNN-NNNNN`
     - **需求**:`BUG-NNN`(3 位,如 `BUG-00010`)
     - **类型**:`修复`(沿用既有 6 枚举)
     - **触发/来源**:`缺陷修复`(沿用既有 13 枚举,**不**新增)
     - **标题**:沿用 REQ-00013 标题解析(`formatTaskTitle` + `truncateTitle`)
     - **开发状态**:`待开始`(初值)
     - **测试状态**:`不适用`(纯文档型任务)或 `未编写`(代码类任务)
     - **关联任务**:本缺陷 `BUG-NNN`(自查)
- **分支/异常**:
  - **E-5**:同一 BUG 多次跑 `code-plan`(增量更新)→ "任务清单"区段只追加新拆分的任务,既有任务**不**重复登记(沿用 REQ 路径强约束)
  - **E-6**:BUG 任务跨多需求?不允许(每条 BUG 任务只属于 1 个 BUG-NNN);若 `code-plan` 误拆,需调整 `PLAN.md`
- **数据变化**:版本看板"任务清单"区段追加 BUG 任务行(数量 = `PLAN.md` 任务总览行数)
- **来源**:本需求 v1 锁定;Q-3 锁定 A(原"任务清单"区段收录,不新增区段)

### FR-4:`code-it` 缺陷分支步骤 17 改读 `PLAN.md` + `RESULT.md`

- **描述**:`/code-it` 技能 BUG 分支(从步骤 1.2 判定为 BUG-NNN 时)步骤 17(校验缺陷与修复方案存在)的输入路径从 `fix-plan.md` 改为 `PLAN.md`(主) + `RESULT.md`(辅)
- **入口**:`code-it` 步骤 17
- **前置条件**:`fix/<BUG-NNN>/PLAN.md` + `fix/<BUG-NNN>/RESULT.md` 都存在
- **主流程**:
  1. 步骤 17 改为:
     - 读 `fix/<BUG-NNN>/RESULT.md` 验证缺陷已登记 + 状态 ∈ {`修复规划中`, `修复编码中`}
     - 读 `fix/<BUG-NNN>/PLAN.md` 验证"修复方案已规划"(状态字段 == `已锁定` 或 `草稿`)
     - **删去** 原"读 `fix-plan.md` + 提取'根因定位/修复方案/涉及文件与变更/测试方案'"段
     - 改为"读 `PLAN.md` 任务总览 + `RESULT.md` §3 算法与逻辑 / §4 数据结构 / §5 接口细节 / §7 异常处理 / §6 风险与回退"
  2. 步骤 17 校验失败改为:
     - 缺 `RESULT.md` → "请先调 `code-fix <缺陷编号>` 登记缺陷"
     - 缺 `PLAN.md` → "请先调 `code-plan <缺陷编号>` 规划修复方案"
     - 状态不符 → 提示用户:当前状态是 X,需要先 `code-fix` 推进到 `修复规划中` / `修复编码中`
- **分支/异常**:
  - **E-7**:`fix-plan.md` 存在(仅 BUG-00001 历史)→ 步骤 17 退化(若 `PLAN.md` 缺失但 `fix-plan.md` 存在,提示用户"检测到历史 fix-plan.md;请先用 `code-plan` 产出 `PLAN.md`") 
  - **E-8**:`PLAN.md` 存在但任务总览为空 → 提示"修复方案待补充任务拆分;请调 `code-plan` 重新规划"
- **数据变化**:`code-it` 步骤 17 锚点文字 + 输入路径更新
- **来源**:本需求 v1 锁定;Q-1 锁定 A(彻底同步升级,去掉 `fix-plan.md`)

### FR-5:`code-it` 缺陷分支过程文档去 `fix-` 前缀

- **描述**:`/code-it` 缺陷分支(步骤 22-25)产出的过程文档从 `fix-work-log.md` / `fix-compile-and-run.md` / `fix-test-results.md` / `deviations.md` 改为 `work-log.md` / `compile-and-run.md` / `test-results.md` / `deviations.md`(与任务路径同套命名)
- **入口**:`code-it` 步骤 22-25
- **前置条件**:FR-4 已改造
- **主流程**:
  1. 步骤 22(实施修复)过程记录改为追加到 `code/<TASK-BUG-...>/work-log.md`(原 `fix-work-log.md`)
  2. 步骤 23.1-23.3(编译/启动/测试)过程记录改为追加到 `code/<TASK-BUG-...>/compile-and-run.md` / `test-results.md`(原 `fix-compile-and-run.md` / `fix-test-results.md`)
  3. 步骤 23.4 错误修复循环过程记录沿用 `code/<TASK-BUG-...>/work-log.md`
  4. 步骤 25(完善过程文档与汇报)收尾文档从 `fix-work-log.md` / `fix-compile-and-run.md` / `fix-test-results.md` / `deviations.md` 改为 `work-log.md` / `compile-and-run.md` / `test-results.md` / `deviations.md`
- **分支/异常**:
  - **E-9**:`fix-work-log.md` 存在(仅 BUG-00001 历史)→ 步骤 22 检测到,提示"检测到历史 fix- 前缀过程文档;本次为新结构 TASK-BUG- 任务编号,过程文档不再使用 fix- 前缀;是否手动迁移?推荐不迁移(BUG-00001 已修复-待验证,历史保留)"
  - **E-10**:旧缺陷的 `fix-work-log.md` 等若在 BUG-00001 后续被 `code-it` 复跑 → 步骤 22 退化(沿用历史文件,不动)
- **数据变化**:`code/<TASK-BUG-...>/` 目录下 4 份过程文档,无 `fix-` 前缀
- **来源**:本需求 v1 锁定;Q-1 锁定 A

### FR-6:`code-it` 缺陷分支步骤 24 不再写 `fix-plan.md`

- **描述**:`/code-it` 缺陷分支步骤 24(同步 fix/<缺陷编号>/RESULT.md 与看板)不再涉及 `fix-plan.md` 同步;原"不修改 `fix-plan.md`,那是上游"约束**删除**(因 `fix-plan.md` 本需求后**不**再生成)
- **入口**:`code-it` 步骤 24
- **前置条件**:FR-4 / FR-5 已改造
- **主流程**:
  1. 步骤 24 改为:同步 `fix/<BUG-NNN>/RESULT.md`(状态推进) + `fix/RESULT.md`(缺陷总览) + 版本看板"缺陷清单" — **不**改 `fix-plan.md` 因 `fix-plan.md` 不存在(沿用既有"不修改上游"约束,但实际"上游"从 `fix-plan.md` 改为 `PLAN.md` + `RESULT.md`)
  2. 步骤 24 不写 `fix/<BUG-NNN>/PLAN.md` 不写 `fix/<BUG-NNN>/RESULT.md` 中的"修复方案"段(沿用既有"不修改上游"约束;状态字段、修复日志、变更记录可改)
- **分支/异常**:
  - **E-11**:同 FR-4 E-7(BUG-00001 历史,步骤 24 不动 `fix-plan.md`)
- **数据变化**:`code-it` 步骤 24 锚点文字更新;**不**写 `fix-plan.md` 同步动作
- **来源**:本需求 v1 锁定;Q-1 锁定 A

### FR-7:`code-it` 缺陷分支步骤 25 汇报 + frontmatter 同步

- **描述**:`/code-it` 缺陷分支步骤 25(完善过程文档与汇报)与 SKILL.md frontmatter `description` 字段的"缺陷分支"描述同步更新;`fix-plan.md` 引用全部移除
- **入口**:`code-it` 步骤 25 + frontmatter
- **前置条件**:FR-4 / FR-5 / FR-6 已改造
- **主流程**:
  1. 步骤 25 汇报字段从:
     ```
     - 同步的文件:`fix/<缺陷编号>/RESULT.md` / `fix/RESULT.md` / 版本看板
     ```
     改为:
     ```
     - 同步的文件:`fix/<缺陷编号>/RESULT.md` / `fix/RESULT.md` / `fix/<缺陷编号>/PLAN.md`(若状态推进) / 版本看板"缺陷清单"+ "任务清单"
     ```
  2. frontmatter L5(缺陷分支描述)从:
     ```
     - **缺陷编号**(格式 `BUG-NNNNN`,如 `BUG-00001`):所有产出物写入 `./assistants/<版本号>/fix/<缺陷编号>/`(以 `fix-` 前缀命名的过程文档),从 `./assistants/<版本号>/fix/<缺陷编号>/RESULT.md` 读取缺陷详情,从 `./assistants/<版本号>/fix/<缺陷编号>/fix-plan.md` 读取修复方案
     ```
     改为:
     ```
     - **缺陷编号**(格式 `BUG-NNNNN`,如 `BUG-00001`):所有产出物写入 `./assistants/<版本号>/fix/<缺陷编号>/`(主详细设计 `RESULT.md` + 任务列表 `PLAN.md`,沿用 REQ 路径同构产出),从 `./assistants/<版本号>/fix/<缺陷编号>/RESULT.md` 读取缺陷详情,从 `./assistants/<版本号>/fix/<缺陷编号>/PLAN.md` 读取修复任务列表
     ```
  3. frontmatter L6(下游衔接)更新:沿用既有"在 `code-it` 之前使用"
  4. 步骤 25 "下一步建议"段保留(沿用既有 3 条:跑测试 / `code-review` / `code-unit`)
- **分支/异常**:无
- **数据变化**:`code-it/SKILL.md` frontmatter L5 + 步骤 25 锚点文字
- **来源**:本需求 v1 锁定;Q-1 锁定 A

### FR-8:`code-fix` 不变(本需求仅优化 `code-plan` 与 `code-it`,不优化 `code-fix`)

- **描述**:`/code-fix` 技能 SKILL.md 与产出物**不**变;继续维护 `fix/<BUG-NNN>/RESULT.md` 缺陷详情 + `fix/RESULT.md` 缺陷总览 + 版本看板"缺陷清单"区段
- **入口**:无(本需求不动 `code-fix`)
- **前置条件**:无
- **主流程**:
  1. `code-fix` 步骤 1 收集缺陷编号 / 描述(沿用既有)
  2. `code-fix` 步骤 1.3 新建缺陷时创建 `fix/<BUG-NNN>/RESULT.md`(沿用既有 105 行结构)
  3. `code-fix` 步骤 2-3 同步 `fix/RESULT.md` + 版本看板"缺陷清单"(沿用既有)
- **分支/异常**:无
- **数据变化**:`code-fix/SKILL.md` **0** 改动
- **来源**:本需求 v1 锁定;**0 修改 `code-fix`** 强约束(由 `code-fix` 是上游登记方,登记后状态推进由 `code-fix` 自己负责)

## 5. 非功能需求 / 约束(NFR)

### 5.1 性能(NFR-1)
- `code-plan` 缺陷分支:与 REQ 分支同等性能(沿用既有 9 份文档产出的开销);目标 < 5 秒生成 9 份文档(用户实际感受不到延迟)

### 5.2 兼容性(NFR-2)
- **NFR-2.1**:`dashboard-conventions §规则 1` 0 触发(沿用既有"任务清单"区段;不新增区段 / 不新增列 / 不新增枚举值 / 不改字段语义)
- **NFR-2.2**:`encoding-conventions §规则 1/3` 0 触发(沿用既有 5+5 位嵌套式;`TASK-BUG-NNNNN-NNNNN` 与 `TASK-REQ-NNNNN-NNNNN` 风格一致)
- **NFR-2.3**:`skill-conventions §规则 1` 0 触发(`code-plan` / `code-it` SKILL.md frontmatter 字节级保留;只有 L5 description 与步骤 17/24/25 锚点文字 + 过程文档前缀的修改;**0** 改 `name` 字段)
- **NFR-2.4**:`marketplace-protocol` 0 触发(0 改 `marketplace.json` / `plugin.json`)
- **NFR-2.5**:`module-conventions §规则 1` 0 触发(过程文档放在 `fix/<BUG-NNN>/` 根目录,与 REQ 路径 `plan/<REQ>/` 摆放规则一致;`templates/fix-plan.md` 留作历史但不再被引用)
- **NFR-2.6**:`commit-conventions` 0 触发(沿用既有 `chore(<scope>): <subject>` 格式)
- **NFR-2.7**:`doc-conventions` 0 触发(0 改中英 README)
- **NFR-2.8**:`naming-conventions` 0 触发(0 新增文件名前缀规则;`TASK-BUG-` 沿用 `TASK-` 已有规则)

### 5.3 可靠性(NFR-3)
- **NFR-3.1**:本需求后**所有新 BUG**(REPO `code-fix` 接收的自然语言描述或 `BUG-NNN` 编号)走新流程(产 `RESULT.md` + `PLAN.md` + 7 份过程 + 看板任务清单)
- **NFR-3.2**:BUG-00001 历史文件**不**自动迁移;用户手动决定是否迁移(本需求范围外)
- **NFR-3.3**:`code-plan` / `code-it` 步骤 0a(REQ-00005 沿用)在 BUG 路径同样适用(增量同步)
- **NFR-3.4**:`code-plan` 步骤 0b(REQ-00011 沿用)对 BUG 路径**不**触发(REQ-00011 仅适用于设计目标确认;BUG 修复是已发生的设计偏差,无需再确认)

### 5.4 可观测性(NFR-4)
- **NFR-4.1**:`code-plan` 屏幕输出沿用既有"启动 / 拆分 / 完成 / 中止 / 错误"5 类格式(REQ-00013 沿用)
  - 启动:`正在处理: BUG-NNNNN · <缺陷标题>`(沿用 `code-fix` 标题解析)
  - 完成:`完成: BUG-NNNNN · <缺陷标题>(拆 N 个任务)`(本需求新增)
- **NFR-4.2**:`code-it` 屏幕输出沿用既有"启动 / 完成 / 中止 / 错误"4 类格式;`TASK-BUG-...` 任务编号用 `formatTaskTitle`(REQ-00013 沿用)
- **NFR-4.3**:版本看板"任务清单"区段统计行更新(总任务数 + 真正可发布数)

### 5.5 可维护性(NFR-5)
- **NFR-5.1**:`code-plan` / `code-it` SKILL.md 行数变化 ≤ ±20%(基线 `code-plan` 945 行 / `code-it` 944 行,允许上下浮动)
- **NFR-5.2**:`code-plan` 步骤 19-28A 重构后行数与既有 REQ 步骤 7A-18A **结构对称**(便于审阅;两侧都是 9 步详细设计 + 4 步同步)
- **NFR-5.3**:BUG 任务编号分配算法与 REQ 任务编号分配算法同构(沿用 `code-plan/SKILL.md` 步骤 9B "任务编号分配"逻辑)

### 5.6 安全性(NFR-6)
- 无新增鉴权 / 加密需求(本需求纯文档重构,无新代码模块)

## 6. 页面与界面(本需求不涉及)

> 本需求**不**新增 / 不修改任何用户可见页面(本仓库是 meta-skills 工具集,无 UI)。

## 7. 交互逻辑

### 7.1 缺陷分支主流程(代码同构后的状态机)

```mermaid
stateDiagram-v2
    [*] --> 登记: code-fix <描述>
    登记 --> 报告: 创建 fix/<BUG>/RESULT.md
    报告 --> 修复规划中: code-plan <BUG>
    修复规划中 --> 修复编码中: code-it <TASK-BUG-...>
    修复编码中 --> 已修复-待验证: code-it 步骤 24 同步
    已修复-待验证 --> 已修复-已验证: code-fix <BUG>
    已修复-已验证 --> 已关闭: code-fix <BUG>

    修复规划中 --> 修复规划中: code-plan 增量更新
    修复编码中 --> 修复编码中: code-it 中断后恢复
    已修复-待验证 --> 修复编码中: 验证失败回退

    note right of 修复规划中
        code-plan 产出 fix/<BUG>/RESULT.md + PLAN.md
        + 7 份过程文档 + 看板"任务清单"区段
    end note

    note right of 修复编码中
        code-it 读 fix/<BUG>/PLAN.md(主) + RESULT.md(辅)
        产出 code/<TASK-BUG-...>/work-log.md 等
    end note
```

### 7.2 关键交互

| 交互 | 触发 | 流程 | 关键规则 |
| --- | --- | --- | --- |
| I-1:`code-plan` BUG 分支 | `/code-plan BUG-00010` | 步骤 19-22 读 `fix/<BUG-00010>/RESULT.md` → 步骤 23 检测文件存在性 → 步骤 24A 根因 + 方案 → 步骤 25A 对齐 → 步骤 26A 撰写 9 份文档 → 步骤 27A 同步 `fix/RESULT.md` + 看板"缺陷清单" → 步骤 28A+1 同步看板"任务清单" → 步骤 29 汇报 | 9 份文档同构产出;看板 2 区段同步 |
| I-2:`code-it` BUG 分支 | `/code-it TASK-BUG-00010-00001` | 步骤 17 校验 + 读 `PLAN.md` + `RESULT.md` → 步骤 18 定位工作目录 → 步骤 19 读规范 → 步骤 20 探索代码 → 步骤 21 状态推进 → 步骤 22 实施 + `work-log.md` → 步骤 23 编译启动测试 + `compile-and-run.md` / `test-results.md` → 步骤 24 同步 → 步骤 25 汇报 | 过程文档去 `fix-` 前缀;输入路径改 `PLAN.md` + `RESULT.md` |
| I-3:`code-dashboard` 看板 | `/code-dashboard` | 解析版本看板"任务清单"区段(沿用既有解析锚点) → 显示 BUG 任务行 | BUG 任务在区段中带 `TASK-BUG-` 前缀,需求列填 `BUG-NNN` |

### 7.3 异常处理

| 场景 | 处理 |
| --- | --- |
| E-1:历史 `fix-plan.md` 存在(仅 BUG-00001) | `code-plan` 步骤 23 检测 + 提示 + 3 选 1 |
| E-2:`investigation.md` 缺失 | `code-plan` 步骤 22 退化,根因定位仅依据 `fix/<BUG-NNN>/RESULT.md` |
| E-3:BUG 修复跨多步 | `PLAN.md` 任务总览拆多任务(`TASK-BUG-NNNNN-00001` 起递增) |
| E-7:历史 `fix-plan.md` 存在(在 `code-it` 步骤 17) | 退化 + 提示"请先用 `code-plan` 产出 `PLAN.md`" |
| E-9:历史 `fix-work-log.md` 等存在(在 `code-it` 步骤 22) | 提示"新结构 TASK-BUG- 任务编号,过程文档不再使用 fix- 前缀;是否手动迁移?推荐不迁移" |
| E-11:同 E-7 | `code-it` 步骤 24 不动 `fix-plan.md` |

## 8. 数据与状态

### 8.1 核心实体:`fix/<BUG-NNN>/` 目录结构

| 实体(本需求**前**) | 实体(本需求**后**) | 差异 |
| --- | --- | --- |
| `fix/<BUG-NNN>/RESULT.md` | `fix/<BUG-NNN>/RESULT.md` | **不变**(缺陷详情) |
| `fix/<BUG-NNN>/investigation.md` | `fix/<BUG-NNN>/investigation.md` | **不变**(调查笔记) |
| `fix/<BUG-NNN>/fix-plan.md` | ❌ 退场(不生成) | **本需求后不再生成**;BUG-00001 历史保留 |
| (无) | `fix/<BUG-NNN>/PLAN.md` | **本需求新增**(任务列表) |
| (无) | `fix/<BUG-NNN>/materials-index.md` | **本需求新增** |
| (无) | `fix/<BUG-NNN>/module-details.md` | **本需求新增** |
| (无) | `fix/<BUG-NNN>/interface-specs.md` | **本需求新增** |
| (无) | `fix/<BUG-NNN>/data-changes.md` | **本需求新增** |
| (无) | `fix/<BUG-NNN>/risk-analysis.md` | **本需求新增** |
| (无) | `fix/<BUG-NNN>/rule-compliance.md` | **本需求新增** |
| (无) | `fix/<BUG-NNN>/design-notes.md` | **本需求新增** |
| (无) | `fix/<BUG-NNN>/clarifications.md` | **本需求新增**(可选) |

### 8.2 核心实体:版本看板"任务清单"区段(扩展)

| 字段 | REQ 任务填法 | BUG 任务填法(本需求新增) |
| --- | --- | --- |
| 任务编号 | `TASK-REQ-NNNNN-NNNNN` | `TASK-BUG-NNNNN-NNNNN` |
| 需求 | `REQ-NNNNN` | `BUG-NNN` |
| 类型 | 6 枚举(新增/修改/重构/修复/测试/文档) | **`修复`**(沿用既有 6 枚举之一) |
| 触发/来源 | 13 枚举(需求新增/需求变更/.../审查改修) | **`缺陷修复`**(沿用既有 13 枚举之一) |
| 标题 | 沿用 REQ-00013 标题解析 | 沿用 REQ-00013 标题解析(用 `formatTaskTitle` + `truncateTitle`) |
| 开发状态 | 6 枚举(待开始/进行中/已完成/...) | 同(沿用) |
| 测试状态 | 6 枚举(未编写/已编写/已运行-通过/已运行-失败/不适用/阻塞) | 同(沿用) |
| 涉及文件 | 留空 → `code-it` 完成时填入 | 同(沿用) |
| 完成时间 | `code-it` 完成时填入 | 同(沿用) |
| 提交哈希 | `code-it` 完成时填入 | 同(沿用) |
| 关联任务 | 沿用(审查改修场景) | **`BUG-NNN`**(自查) |

**关键**:所有字段**0 新增**,所有枚举值**0 新增**;仅在既有"任务清单"区段内**新增** BUG 任务行(用既有字段填法)。

### 8.3 状态机:BUG 状态(沿用既有 7 状态)

```
报告 → 调查中 → 修复规划中 → 修复编码中 → 已修复-待验证 → 已修复-已验证 → 已关闭
```

本需求不修改状态机(由 `code-fix` 维护)。

## 9. 边界与异常

### 9.1 历史 BUG-00001 兼容

| 边界 | 场景 | 处理 |
| --- | --- | --- |
| **B-1** | BUG-00001 现有 `fix-plan.md`(624 行) | **不迁移**;用户决定是否手动重生成 `RESULT.md` + `PLAN.md`;`code-plan BUG-00001` 检测到 `fix-plan.md` 存在 + 提示"是否继续以本缺陷的 fix-plan.md 为参考?" + 3 选 1(继续/手动迁移/中止) |
| **B-2** | BUG-00001 现有 `fix-work-log.md` / `fix-compile-and-run.md` / `fix-test-results.md` / `deviations.md` | **不迁移**;`code-it TASK-BUG-00001-00001`(若重跑)退化,沿用历史文件 |

### 9.2 BUG 任务状态推进

| 边界 | 场景 | 处理 |
| --- | --- | --- |
| **B-3** | BUG 任务已完成,`code-it` P-1(REQ-00017 沿用)推进看板 | 沿用既有 P-1 逻辑(看板"开发状态":待开发→已完成) |
| **B-4** | BUG 任务被 `code-review` 派生"审查改修"任务 | 沿用既有 `触发/来源=审查改修` 枚举;新任务仍为 BUG 任务的子任务 |
| **B-5** | BUG 任务跨多 BUG(同时修 2 个缺陷) | **不允许**;每条 BUG 任务只属于 1 个 `BUG-NNN` |

### 9.3 增量更新

| 边界 | 场景 | 处理 |
| --- | --- | --- |
| **B-6** | `code-plan BUG-NNN` 多次执行(增量) | 沿用 `code-plan/SKILL.md` 步骤 24B-26B 增量更新逻辑;`RESULT.md` / `PLAN.md` 稳定章节不重写;看板"任务清单"区段只追加新拆分任务,既有任务不重复登记 |
| **B-7** | `code-it TASK-BUG-...` 多次执行(中断恢复) | 沿用既有"中断后恢复"逻辑;`work-log.md` 等持续追加,不重写 |

## 10. 验收标准(AC)

### 10.1 FR-1 ~ FR-2 验收(`code-plan` 缺陷分支)

| AC | 验证手段 | 判定条件 |
| --- | --- | --- |
| **AC-1.1** | 调 `code-plan BUG-00010`(新 BUG,无历史) | `fix/BUG-00010/` 下产出 9 份文档:`RESULT.md` / `PLAN.md` / `materials-index.md` / `module-details.md` / `interface-specs.md` / `data-changes.md` / `risk-analysis.md` / `rule-compliance.md` / `design-notes.md`(可加 `clarifications.md`);**0** 产出 `fix-plan.md` |
| **AC-1.2** | 验证 `fix/BUG-00010/RESULT.md` 章节结构 | 14 章节齐全:概述 / 上游引用 / 规范遵循 / 模块详细化 / 算法与逻辑 / 数据结构 / 接口细节 / 异常处理 / 安全 / 状态机 / 性能 / 测试要点 / 关联 / 待澄清 / 变更记录;与 `plugins/code-skills/skills/code-plan/templates/plan.md` 同构 |
| **AC-1.3** | 验证 `fix/BUG-00010/PLAN.md` 章节结构 | 8 章节齐全:计划概述 / 任务总览 / 任务详情 / 任务依赖图 / 里程碑 / 状态管理规则 / 关联计划 / 变更记录;与 `plugins/code-skills/skills/code-plan/templates/task-plan.md` 同构 |
| **AC-1.4** | 验证 `fix/BUG-00010/PLAN.md` 任务总览 | 含至少 1 条 `TASK-BUG-00010-00001`;触发/来源=缺陷修复;类型=修复;需求=BUG-00010;标题=沿用 REQ-00013 标题解析 |
| **AC-1.5** | 验证 `fix/BUG-00010/PLAN.md` §"上游引用" | 引用 `./RESULT.md`(缺陷详情) + `./investigation.md`(若有) + 项目级规范 |

### 10.2 FR-3 验收(看板任务清单区段)

| AC | 验证手段 | 判定条件 |
| --- | --- | --- |
| **AC-2.1** | 调 `code-dashboard`(无参) | 看板"任务清单"区段显示 `TASK-BUG-00010-00001`(或多个 BUG 任务);与 REQ 任务同表 |
| **AC-2.2** | 验证 BUG 任务行字段 | 任务编号=`TASK-BUG-00010-00001`;需求=BUG-00010;类型=修复;触发/来源=缺陷修复;开发状态=待开始;测试状态=不适用或未编写 |
| **AC-2.3** | 验证 0 触发 §规则 1 三同步 | `plugins/code-skills/skills/code-version/templates/version-RESULT.md` + `plugins/code-skills/CLAUDE.md` "看板字段约定"段 + `assistants/rules/dashboard-conventions.md` **0** 改动 |

### 10.3 FR-4 ~ FR-7 验收(`code-it` 缺陷分支)

| AC | 验证手段 | 判定条件 |
| --- | --- | --- |
| **AC-3.1** | 调 `code-it TASK-BUG-00010-00001` | 步骤 17 读 `fix/BUG-00010/PLAN.md` + `RESULT.md`(**不**读 `fix-plan.md`) |
| **AC-3.2** | 步骤 17 校验失败场景 | 缺 `PLAN.md` → 提示"请先调 `code-plan`";缺 `RESULT.md` → 提示"请先调 `code-fix`" |
| **AC-3.3** | 步骤 22-25 过程文档 | 产出 `code/TASK-BUG-00010-00001/{work-log.md, compile-and-run.md, test-results.md, deviations.md}`(**不**产出 `fix-work-log.md` 等) |
| **AC-3.4** | 步骤 24 同步 | 同步 `fix/BUG-00010/RESULT.md` + `fix/RESULT.md` + 看板"缺陷清单";**0** 同步 `fix-plan.md`(因不存在) |
| **AC-3.5** | 步骤 25 汇报 | 含"同步的文件:`fix/<缺陷>/RESULT.md` / `fix/RESULT.md` / `fix/<缺陷>/PLAN.md`(若状态推进) / 版本看板'缺陷清单'+'任务清单'" |
| **AC-3.6** | frontmatter L5 | 描述"从 `fix-plan.md` 读取修复方案" → "从 `PLAN.md` 读取修复任务列表" |

### 10.4 FR-8 验收(`code-fix` 不变)

| AC | 验证手段 | 判定条件 |
| --- | --- | --- |
| **AC-4.1** | 调 `code-fix <描述>`(新建缺陷) | 产出 `fix/<BUG-NNN>/RESULT.md` + 同步 `fix/RESULT.md` + 看板"缺陷清单";`code-fix/SKILL.md` **0** 改动 |

### 10.5 跨需求兼容(沿用 13 份规范)

| AC | 验证手段 | 判定条件 |
| --- | --- | --- |
| **AC-5.1** | `dashboard-conventions §规则 1` | 0 触发(沿用既有"任务清单"区段;0 新增区段/列/枚举值/字段语义) |
| **AC-5.2** | `encoding-conventions §规则 1/3` | 0 触发(沿用 5+5 位嵌套式;`TASK-BUG-NNNNN-NNNNN` 与 `TASK-REQ-NNNNN-NNNNN` 风格一致) |
| **AC-5.3** | `skill-conventions §规则 1` | `code-plan` / `code-it` SKILL.md frontmatter `name` 字段**字节级保留** |
| **AC-5.4** | `marketplace-protocol` | 0 改 `marketplace.json` / `plugin.json` |
| **AC-5.5** | `module-conventions §规则 1` | 过程文档摆放在 `fix/<BUG-NNN>/` 根目录;`templates/fix-plan.md` 留作历史不删,但**不**再被引用 |
| **AC-5.6** | `commit-conventions` | 沿用 `chore(<scope>): <subject>` |
| **AC-5.7** | `doc-conventions` | 0 改中英 README |
| **AC-5.8** | `naming-conventions` | 0 新增文件名前缀规则;`TASK-BUG-` 沿用 `TASK-` 已有规则 |
| **AC-5.9** | `dependency-conventions` | 0 新增依赖 |
| **AC-5.10** | `framework-conventions` / `migration-mapping` / `coding-style` | 不涉及 |
| **AC-5.11** | `directory-conventions` | 0 新增子目录 |

### 10.6 不变量自检(INV)

| INV | 验证手段 | 判定条件 |
| --- | --- | --- |
| **INV-1** | frontmatter 字节级保留 | `code-plan/SKILL.md` + `code-it/SKILL.md` 的 `name` 字段**字节级保留**;只有 L5 description 段修改 |
| **INV-2** | 既有"## 工作流程" 小节不改 | `code-plan/SKILL.md` 步骤 0a-28 + 步骤 N 既有内容**字节级保留**;**只**追加新锚点 |
| **INV-3** | 既有"## 看板字段约定" 段不动 | `code-plan/SKILL.md` 步骤 16A 既有"同步版本看板"段**字节级保留**;**只**追加"28A+1 同步'任务清单'区段" |
| **INV-4** | 9 份文档结构完整 | `RESULT.md` 14 章节 / `PLAN.md` 8 章节 / 7 份过程文档 |
| **INV-5** | 13 份规范 0 冲突 | AC-5.1 ~ AC-5.11 全部通过 |
| **INV-6** | 看板 5 处一致 | "任务清单"区段 BUG 任务行 + "详细设计与任务计划汇总"新增 BUG 计划行(若有)+ "里程碑"新增 BUG 里程碑(若有)+ 文档头 + 变更记录(5 处) |
| **INV-7** | 0 派生"更新看板"任务(REQ-00017 强约束) | 看板推进由 `code-it` P-1 自行承担;**不**通过"更新看板"派生任务 |
| **INV-8** | 0 修改其他 11 个 `code-*` SKILL.md | `code-require` / `code-design` / `code-fix` / `code-unit` / `code-review` / `code-auto` / `code-version` / `code-init` / `code-merge` / `code-publish` / `code-dashboard` 11 个 SKILL.md 全部**字节级保留** |

## 11. 关联需求

| 需求编码 | 关联点 | 对本需求的影响 | 关联需求所在版本 |
| --- | --- | --- | --- |
| **REQ-00005** | 首步拉取最新代码 + 末步兜底提交 | `code-plan` 步骤 0a + 步骤 N 对 BUG 路径同样适用(沿用既有) | V0.0.2 |
| **REQ-00007** | `code-auto` 自动开发技能 | `code-auto` 子技能调用 `code-plan` 时,BUG 路径(若有)同样接受"自动选推荐项"约束(沿用 BUG-00001 修复方案) | V0.0.2 |
| **REQ-00009** | `code-unit` 项目可测性守卫 | BUG 任务的测试状态初始化:本仓库无测试框架,守卫判定"不可测" → 测试状态 = `不适用` | V0.0.2 |
| **REQ-00010** | `code-it` 步骤 0a 前置任务守卫 | BUG 任务执行时也走前置守卫(按 `PLAN.md` 文件登记顺序判定);`TASK-BUG-...` 任务也在守卫判定范围内 | V0.0.2 |
| **REQ-00011** | `code-design` / `code-plan` 步骤 0b 设计目标确认 | BUG 路径**不**触发步骤 0b(修复是已发生的设计偏差,无需再确认);FR 8 NFR-3.4 锁定 | V0.0.2 |
| **REQ-00013** | 6 技能启用"编号+标题" 显示 | BUG 任务沿用 `formatTaskTitle` + `truncateTitle`;`code-plan` / `code-it` 屏幕输出统一格式 | V0.0.2 |
| **REQ-00014** | `code-plan` 任务拆分维度(按功能点拆 + 架构任务作为首个) | BUG 路径**不**触发"架构任务作为首个"(修复不引入新架构);**0 派生架构任务** | V0.0.2 |
| **REQ-00016** | `code-design` / `code-plan` 快模式 | BUG 路径同样支持快模式(沿用 `code-plan` 步骤 0.5 模式选择) | V0.0.2 |
| **REQ-00017** | `code-plan` 不再为"更新看板"拆派生任务 | BUG 任务沿用 FR-3 强约束;看板推进由 `code-it` P-1 自行承担 | V0.0.2 |
| **REQ-00018** | `code-version` 优化(CWD 描述文件版本号同步) | BUG 路径产出物写入版本工作空间时,沿用 CWD 同步(若 V0.0.2 是新版本首次切) | V0.0.2 |
| **BUG-00001** | `code-auto` 调用子技能时子技能仍会手动选 | BUG-00001 已有 `fix-plan.md` 历史文件;本需求**不**迁移(用户锁定) | V0.0.2 |

## 12. 待澄清 / 未决项

| 编号 | 内容 | 状态 |
| --- | --- | --- |
| (无) | 本需求**0** 待澄清;8 项 FR + 11 项 NFR + ~30 项 AC + 11 项 INV 全部已锁定(用户 3 轮澄清已采纳所有建议:Q-1 形式同构 + 路径全替,Q-2 `TASK-BUG-NNNNN-NNNNN` 新格式,Q-3 原"任务清单"区段收录,Q-4 4 项 code-it 联动全选,Q-5 仅未来新缺陷生效不迁移) | 0 待澄清 |

## 13. 变更记录

| 时间 | 版本 | 变更摘要 | 变更人 |
| --- | --- | --- | --- |
| 2026-06-06 14:30 | v1 | 初始创建:8 FR / 11 NFR / ~30 AC / 11 INV / 5 项 Q-locked;锁定"形式同构 + 路径全替" + `TASK-BUG-NNNNN-NNNNN` 新格式 + 原"任务清单"区段收录;0 触发 `dashboard-conventions §规则 1` 三同步;0 修改 `code-fix` 强约束;0 派生"更新看板"任务 REQ-00017 强约束;0 修改其他 11 个 `code-*` SKILL.md;0 触发 `encoding-conventions §规则 1/3`(沿用 5+5 位嵌套式);0 触发 `marketplace-protocol`;0 触发 `module-conventions §规则 1`(`templates/fix-plan.md` 留作历史不删);2 个 SKILL.md 修改(`code-plan` / `code-it`) | wangmiao |
