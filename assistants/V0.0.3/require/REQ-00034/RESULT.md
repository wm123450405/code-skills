# 需求提示词文档 — 移除 /code-unit 技能,能力整合进 /code-it(按需写单测/不适用工程跳过)

- 需求编码:REQ-00034
- 所属版本:V0.0.3
- 文档创建时间:2026-06-15 12:00
- 最近更新:2026-06-15 12:00
- 文档状态:草稿(待 code-design 推进)
- 上游:无(用户口头/文本输入,2026-06-15 11:30,经 1 轮 AskUserQuestion 澄清)
- 遵循规范:`./assistants/rules/` 下 7 个文件(全沿用,无新增)
- 涉及技能:`code-unit`(整体删除) + `code-it`(接管守卫 + 按需写单测)+ `code-plan` / `code-auto` / `code-check`(适配)+ 2 JSON + 4 README + 7 项目级规范 + 11 技能描述段

## 1. 需求概述

**移除** `/code-unit` 技能(整体删除 SKILL.md 635 行 + templates/ 目录);将其能力("编写单元测试 + 执行测试" + "项目可测性守卫 7 项")**整合进** `/code-it` 技能:
- **接管守卫**:`code-it` 步骤 8a(项目可测性守卫)字节级沿用 `code-unit` 步骤 0a 7 项检查
- **按需写单测**:`code-it` 步骤 8.5 在守卫通过后,按"项目可测 + 任务性质"自动判定(纯函数/工具方法/业务逻辑 → 写;配置/类型定义/文档 → 不写)
- **不适用工程跳过**:守卫不通过 → 跳过单测,屏幕输出守卫详情,任务"测试状态"列 = `不适用`,exit 0(沿用原 `code-unit` E-2 行为)

涉及 5 SKILL.md / 2 JSON / 4 README / CLAUDE.md / 7 项目级规范 / 11 技能描述段 / 1 目录删除,共约 ~30 个文件,净变化约 -600 ~ -800 行(技能合并)。

## 2. 背景与目标

### 2.1 背景

V0.0.3 期间(2026-06-12)通过 REQ-00031 已将 `code-unit` 声明为"**独立、可选**"的技能,但**没**真正删除:

| 维度 | REQ-00031 落地后(本需求前) | 本需求 |
| --- | --- | --- |
| `code-plan` 任务规划 | 不含"测试"类任务(已收窄) | 沿用 |
| `code-it` 职责 | 编码 + 编译/运行(声明"不含"单测) | 编码 + 编译/运行 + **含**单测(按需) |
| `code-unit` 职责 | 独立、可选(声明) | **退场** |
| `code-unit` 技能本体 | 仍存在(635 行) | **删除** |
| `code-auto` 步骤 4.b | 恒等跳过(屏幕日志冗余) | **整段删除** |
| 任务"测试状态" | `已运行-通过` / `不适用` 2 枚举(已收窄) | 沿用(`code-it` 内部使用) |

**用户原始输入(verbatim)**:
> 移除技能 `/code-unit`,将技能能力整合进 `/code-it` 技能中,功能代码编写完成根据需要直接编写单元测试或针对不适用的工程跳过单元测试编写。

### 2.2 业务目标

- 显式合并 `code-unit` 进 `code-it`,消除 11 vs 12 技能数量的"半分离"状态
- `code-it` 接管 7 项守卫(字节级沿用 `code-unit` 步骤 0a)
- `code-it` 接管"按需写单测"逻辑(自动判定,无新增用户问路)
- `code-auto` 屏幕日志减少 1 行/任务(删除 `code-unit` 跳过日志)
- 2 JSON + 4 README + 7 项目级规范 + 11 技能描述段全部去 `code-unit` 引用
- 历史 V0.0.2 / V0.0.3 既有 `test/<TASK-...>/RESULT.md` + `code/<TASK-...>/test-results.md` 字节级保留(NFR-2 沿用 REQ-00031)

### 2.3 本次目标

- 范围:**移除** `code-unit` 整体 + **改造** `code-it` / `code-plan` / `code-auto` / `code-check` 4 SKILL.md + **改写** 2 JSON + 4 README + CLAUDE.md + 7 项目级规范 + 11 技能描述段
- 不涉及:`code-require` / `code-design` / `code-fix` / `code-init` / `code-version` / `code-rule` / `code-merge` / `code-answer` / `code-dashboard` / `code-publish` 10 个 SKILL.md 核心工作流(仅描述段去 `code-unit` 引用,前 N 行不动)
- 不涉及:历史 V0.0.2 / V0.0.3 既有 `test/` 目录 + `code/<TASK-...>/test-results.md`(字节级保留)
- 不涉及:BUG-00001 "不修改 SKILL.md"硬约束(本需求不冲突 Q-5)
- 触发 1 次看板同步:`assistants/V0.0.3/RESULT.md` §需求清单 追加 1 行 + §变更记录 追加 1 条

## 3. 用户角色与场景

### 3.1 角色

- **元技能维护者**(本需求主要受益方):希望 `code-*` 技能数量收敛,职责清晰无歧义
- **项目开发者**:在 `code-it` 完成后,期望"该写的单测自动写上,该跳过的自动跳过",**不**需要单独调 `code-unit`
- **`code-auto` 编排者**:任务循环步骤 4 中,**不**再需要"code-unit 跳过"日志(整体清爽 1 行)
- **`code-check` 评审者**:在 `code-it` 完成后,直接读 `code/<TASK-...>/test-results.md`,**不**需要找 `test/<TASK-...>/RESULT.md`

### 3.2 场景

| 场景 | 现状体验 | 改造后体验 |
| --- | --- | --- |
| 用户调 `code-unit TASK-XXX` | 可用,但 12 技能并存,有"半分离"感 | 不可用(`/code-unit` 退场);改为 `code-it TASK-XXX` 内化 |
| `code-it` 写完代码 | 屏幕输出"请调 code-unit 写单测" | 屏幕输出"项目可测 → 写 5 个单测 ✓"或"项目不可测 → 跳过单测" |
| `code-auto` 跑循环 | 每条任务循环额外 1 行 `code-unit ... ✓ (跳过,无需测试)` | 删除该行;屏幕日志减少 1 行/任务 |
| `code-check` 评审 | 需读 `code/<TASK-...>/test-results.md` + `test/<TASK-...>/RESULT.md` | 仅读 `code/<TASK-...>/test-results.md`(由 `code-it` 自含) |
| README 写"12 个 code-* 技能" | 1 处描述 | 改为"11 个 code-* 技能" |

## 4. 功能需求(FR)

### FR-1:`code-unit` 技能整体删除

- **删除范围**(硬删除,无字节级保留):
  - `plugins/code-skills/skills/code-unit/SKILL.md`(635 行)
  - `plugins/code-skills/skills/code-unit/templates/RESULT.md`
  - `plugins/code-skills/skills/code-unit/templates/` 整体目录
- **不涉及**:
  - `plugins/code-skills/skills/code-merge/SKILL.md`(独立技能,不动)
  - V0.0.2 / V0.0.3 既有 `test/<TASK-...>/RESULT.md`(历史档案保留)
  - 既有 11 个 `code-*` 技能描述段对 `code-unit` 的引用(由 FR-10 单独改写)
- **commit message 候选**:
  - `chore(code-unit): REQ-00034 移除 code-unit 技能整体(SKILL.md + templates/ 目录)`
  - 或:`chore(code-it): REQ-00034 接管 code-unit 能力`(按接管方命名)
  - 锁定:`chore(code-unit): REQ-00034 移除 code-unit 技能整体`(以被删除技能命名,更直观)

### FR-2:`code-it` 接管项目可测性守卫 7 项

- **位置**:`plugins/code-skills/skills/code-it/SKILL.md` 在既有"## 步骤 8"之后新增"## 步骤 8a — 项目可测性守卫"
- **字节级沿用 `code-unit` 步骤 0a 7 项检查**:
  1. `package.json` 含 `scripts.test`
  2. `pyproject.toml` 含 `[tool.pytest]` / `[tool.pytest.ini_options]` / `[tool.tox]` / `[tool.nox]` 任一
  3. `Cargo.toml` 存在
  4. `go.mod` 存在
  5. `pom.xml` 存在
  6. `build.gradle` / `build.gradle.kts` 任一
  7. `test/` 目录存在
- **判定逻辑**(沿用 `code-unit` 步骤 0a.2):
  - 命中任一 → testable = True → 屏幕输出"✓ code-it 守卫通过"→ 进入步骤 8.5
  - 全部不命中 → testable = False → 屏幕输出"⏭ code-it 跳过单测(项目不可测)" + 守卫检查详情 → 跳过步骤 8.5 → 任务"测试状态"列 = `不适用`(看板)→ exit 0
- **不修改**:`code-it` 步骤 0a 既有"git pull + current-version 读取"逻辑(沿用 REQ-0009 既有)

### FR-3:`code-it` 接管"按需写单测"步骤

- **位置**:`plugins/code-skills/skills/code-it/SKILL.md` 在"## 步骤 8a"之后新增"## 步骤 8.5 — 按需写单测"(仅在 testable = True 时执行)
- **自动判定逻辑**(Q-4 隐含答复 C):
  - **写单测**(`code-it` 自含):任务涉及"纯函数 / 工具方法 / 业务逻辑"
    - 读取 `plan/<需求>/PLAN.md` 中本任务详情,识别任务类型 = `新增` / `修改` / `重构` / `修复` + 涉及"函数级"改动
    - 写单测到 CWD 下的项目测试目录
    - 跑通(`Bash` 跑项目测试命令)
    - 写 `code/<TASK-...>/unit-test-results.md`(新模板,见 FR-4)
  - **不写单测**(跳过):任务涉及"配置 / 类型定义 / 文档 / 模板"
    - 任务类型 = `文档`
    - 写 `code/<TASK-...>/unit-test-results.md`,内容 = "本任务不涉及单元测试(任务类型 = 文档)"
  - **不写单测**(跳过,沿用原 `code-unit` 步骤 4 `不适用` 语义):任务"测试状态"已为 `不适用`
- **屏幕输出**(字节级沿用 `code-unit` 步骤 7):
  ```
  === code-it 按需写单测(守卫通过)===
  任务:TASK-REQ-...-...
  判定:写单测 / 跳过单测
  测试框架:<Jest / Pytest / ...>(沿用原 code-unit 步骤 8 检测)
  新增/修改的测试文件:<file1.test.ts, file2.test.ts>
  ```
- **不引入用户问路**:**不**弹 `AskUserQuestion`(用户原始输入"根据需要"隐含**不**问)

### FR-4:`code-it` 模板新增"## 单元测试"小节

- **位置**:`plugins/code-skills/skills/code-it/templates/RESULT.md` 在既有章节中新增"## 单元测试"小节
- **小节内容**:
  ```
  ## 单元测试(由 code-it 内化)
  - 守卫判定:可测 / 不可测
  - 测试框架:<Jest / Pytest / ...>
  - 新增/修改的测试文件:<...>
  - 跑通情况:<通过 N 个 / 失败 M 个>
  - 覆盖率(若可获得):<...>
  - 跳过的子任务:<...>(若有)
  - 发现的代码 bug:<...>(若有,转交 code-it 修复)
  ```
- **不修改**:`code-it/templates/RESULT.md` 既有章节(字节级保留)

### FR-5:`code-plan` 测试状态字段语义改写

- **位置**:`plugins/code-skills/skills/code-plan/SKILL.md` L368 / L431 / L445 / L454 / L1105 共 5 处
- **改写**:
  - 既有"由 `code-unit` 另起流程" → 改为"由 `code-it` 内化(`code-it` 步骤 8a 守卫 + 步骤 8.5 按需写单测)"
  - 既有"code-unit 阶段记录到 `code/<任务>/test-results.md`" → 改为"由 `code-it` 步骤 8.5 产出 `code/<任务>/unit-test-results.md`"
- **不修改**:
  - 任务"测试状态"2 枚举(`已运行-通过` / `不适用`)(沿用 REQ-00031 FR-3)
  - 任务"双状态"语义 = 开发状态 = 已完成(沿用 REQ-00031 FR-3)

### FR-6:`code-auto` 步骤 4.b 整段删除

- **位置**:`plugins/code-skills/skills/code-auto/SKILL.md` L388-411 + L432-433 + L449 + L624-625 + L672 + L692 + L711 + L741 + L797 + L806 + L834
- **删除**:
  - 步骤 4.b "code-unit 步骤"整段(FR-6.1,字节级删除)
  - 子技能调用表 4 行(`code-unit` 任务路径 + 派生任务路径 + BUG 路径 + 条件触发)(FR-6.2)
  - 派生任务循环 L432-433 `code-unit` 引用(FR-6.3)
  - 屏幕日志 + 报告段 L624-625 / L672 / L692 / L711 / L741 `code-unit` 字面(FR-6.4)
  - 衔接 L797 / L806 `code-unit` 字面(FR-6.5)
  - "不要做的事" L834 中"`code-unit`"字面删除(FR-6.6)
- **不修改**:`code-auto` 步骤 4.a 任务循环 + 步骤 5-7 既有逻辑
- **副作用**:`code-auto` 任务循环屏幕日志**减少** 1 行/任务(原"code-unit ... ✓ (跳过,无需测试)"删除)

### FR-7:`code-check` `test/<TASK-...>/` 引用收窄

- **位置**:`plugins/code-skills/skills/code-check/SKILL.md` L3 / L21 / L40-41 / L56 / L72 / L96 / L151 / L281 / L608 / L615 共 10 处
- **改写**:
  - 既有"`./assistants/<版本号>/test/<任务编码>/RESULT.md`" → 改为"`./assistants/<版本号>/code/<任务编码>/unit-test-results.md`(由 `code-it` 步骤 8.5 自含)"
  - 既有"`code-unit` 产出(只读,作为评审上下文)" → 改为"`code-it` 自含的 `unit-test-results.md`"
- **不修改**:`code-check` 评审清单 12 维度(8.1-8.12)字节级保留;`code-check` 工作流步骤 0-6 字节级保留

### FR-8:plugin.json + marketplace.json 注册项删除

- **位置**:
  - `plugins/code-skills/.claude-plugin/plugin.json` L15
  - `.claude-plugin/marketplace.json` L24 / L39
- **删除**:
  - plugin.json `keywords[]` 数组中的 `"code-unit"`(1 项)
  - marketplace.json `plugins[0].keywords[]` 数组中的 `"code-unit"`(1 项)
  - marketplace.json `plugins[0].skills[]` 数组中的 `"./skills/code-unit"`(1 项)
- **不修改**:2 JSON 文件的 `$schema` / `name` / `version` / `description` / `author` / `owner` / `source` 等其他字段

### FR-9:4 README + CLAUDE.md 去 `code-unit` 引用

- **位置**:
  - `README.md`(仓库根)
  - `README.en.md`(仓库根)
  - `plugins/code-skills/README.md`
  - `plugins/code-skills/README.en.md`
  - `CLAUDE.md`(仓库根)
- **改写**:
  - 技能表 / 工作流总览描述段:删除 `code-unit` 行
  - 字面量`12 个 code-* 技能` → `11 个 code-* 技能`
  - 主流程图:`code-it → code-unit → code-check` → `code-it → code-check`
- **不修改**:README / CLAUDE.md 中其他技能描述

### FR-10:7 项目级规范去 `code-unit` 引用

- **位置**:`./assistants/rules/*.md`(本仓库当前 13 个 .md,本需求**仅**触及 7 个)
- **改写**:
  - `encoding-conventions.md` 任务"双状态"测试状态字段语义:沿用 REQ-00031 + 本需求 FR-5
  - `review-checklist.md` §8.7 测试质量维度:`code-unit` 引用 → `code-it` 内化
  - `skill-conventions.md`:`code-unit` 引用 → `code-it` 内化
  - `module-conventions.md`:`code-unit/templates/` 引用删除
  - `dashboard-conventions.md`:看板字段"code-unit 跳过"日志描述改写
  - `plugin-conventions.md`:plugin.json / marketplace.json `code-unit` 引用删除
  - `migration-mapping.md`(若引用 `code-unit`):`code-unit` 引用 → `code-it` 内化
- **不修改**:7 规范的核心约束字节级保留(只改字面量)

### FR-11:11 个 `code-*` 技能 SKILL.md 描述段去 `code-unit` 引用

- **位置**:`plugins/code-skills/skills/{code-require, code-design, code-plan, code-fix, code-init, code-publish, code-version, code-rule, code-merge, code-answer, code-dashboard, code-auto}/SKILL.md` 中 frontmatter `description` 字段或文档头概述段
- **改写**:删除 `code-unit` 引用(具体位置由 `code-plan` 阶段精确扫描)
- **不修改**:
  - 各 SKILL.md 的 frontmatter L1-3 字节级保留(INV-1 沿用)
  - 各 SKILL.md 的核心工作流字节级保留
- **例外**:`code-it` 描述段**改写**为"含按需写单测"(本需求 FR-2 / FR-3)
- **例外**:`code-auto` 描述段**改写**为"不调 `code-unit`(本需求 FR-6)"

### FR-12:不修改其他 8 个 `code-*` 技能核心工作流

- **不修改**:
  - `code-require` / `code-design` / `code-fix` / `code-init` / `code-publish` / `code-version` / `code-rule` / `code-merge` / `code-answer` / `code-dashboard` 10 个 SKILL.md 的核心工作流(INV-4 字节级保留)
  - 既有 12 个 REQ 的 `code/<TASK-...>/RESULT.md` + `test/<TASK-...>/RESULT.md` 字节级保留(INV-7 字节级保留)
  - 既有 V0.0.2 / V0.0.3 看板 RESULT.md 字节级保留(只追加 REQ-00034 行,不改既有)

## 5. 非功能需求 / 约束(NFR)

- **NFR-1 字节级保留**:`code-it` / `code-plan` / `code-auto` / `code-check` 4 个被改 SKILL.md 的 frontmatter L1-3 字节级保留(INV-1 沿用);既有"## 不要做的事"小节 0 改(INV-2 沿用)
- **NFR-2 历史档案保留**:V0.0.2 / V0.0.3 既有 `test/<TASK-...>/RESULT.md` + `code/<TASK-...>/test-results.md` 字节级保留;既有 12 个 REQ 的 `PLAN.md` 任务"测试状态"列保留原值(不追溯重写,沿用 REQ-00031 NFR-2)
- **NFR-3 净变化**:本需求涉及 ~30 个文件,净变化约 -600 ~ -800 行(技能合并;删除多于新增)
- **NFR-4 幂等性**:`code-it` 步骤 8a 守卫 + 步骤 8.5 按需写单测,多次执行行为**不**累积
- **NFR-5 不引入新三方依赖**:0 新增依赖(本需求**仅**文档改动 + 1 目录删除)
- **NFR-6 与 REQ-00031 协同**:沿用 REQ-00031 落地的 5 任务提交 + 任务"测试状态"2 枚举 + `code-it` 不调 `code-unit` 编排逻辑;**不**回滚 REQ-00031 任何字节级变更
- **NFR-7 与 BUG-00001 协同**:本需求**不**修改工程代码(SKILL.md 之外的生产代码),**不**冲突 BUG-00001(Q-5 锁定);本需求修改的 5 SKILL.md 是经用户授权的元技能改
- **NFR-8 不引入新用户问路**:`code-it` 步骤 8.5 **不**弹 `AskUserQuestion`(用户原始输入"根据需要"隐含**不**问,FR-3 锁定)
- **NFR-9 看板三同步**:`V0.0.3/RESULT.md` §"需求清单" 追加 1 行(REQ-00034) + §"变更记录" 追加 1 条;统计数字刷新
- **NFR-10 模板零规范变更**:`plugins/code-skills/skills/code-plan/templates/plan.md` 测试状态字段 0 改(沿用 REQ-00031 FR-7);`plugins/code-skills/skills/code-it/templates/RESULT.md` 仅追加"## 单元测试"小节(FR-4)
- **NFR-11 不引入新任务类型 / 新测试类型**:沿用 REQ-00031 FR-2;本需求不涉及任务类型变更
- **NFR-12 不变更状态机**:`code-fix` 5 候选状态机 0 改(沿用 REQ-00027)

## 6. 页面与界面

不适用(本需求无 UI 变更)。

## 7. 交互逻辑(状态机、关键流程)

### 7.1 `code-it` 步骤 8a + 步骤 8.5 状态机

```
[code-it 步骤 8 探索项目代码]
  ↓
[code-it 步骤 8a 项目可测性守卫]
  ├─ 命中 7 项任一 → testable = True → 屏幕输出"✓ 守卫通过" → 进入步骤 8.5
  └─ 全部不命中 → testable = False → 屏幕输出"⏭ 守卫不通过" → 跳过步骤 8.5
                                                                     ↓
                                                              看板"测试状态"= 不适用
                                                                     ↓
                                                                  exit 0
  ↓
[code-it 步骤 8.5 按需写单测](testable = True 时)
  ├─ 任务类型 = 文档 → 写 unit-test-results.md = "本任务不涉及单元测试"
  ├─ 任务类型 = 新增/修改/重构/修复 + 涉及"函数级"改动 → 写单测 + 跑通 + 写 unit-test-results.md
  └─ 任务类型 = 配置/类型定义 → 写 unit-test-results.md = "本任务不涉及单元测试"
  ↓
[code-it 步骤 9 编译/运行 + 步骤 10 跑测试 + 步骤 11 错误修复 + 步骤 12 覆盖率 + 步骤 13 RESULT.md]
```

### 7.2 `code-auto` 任务循环简化

```
code-auto 步骤 4 任务循环(简化后):
  for each TASK-REQ-...-... in PLAN.md:
    → 1/N:code-it TASK-REQ-...-... ✓  (本需求后不再有"code-unit 跳过"日志)
```

### 7.3 技能数量变迁(本需求前 vs 本需求后)

```
[本需求前 12 个 code-* 技能]:
  code-require, code-design, code-plan, code-it, code-unit, code-check,
  code-fix, code-version, code-init, code-rule, code-auto, code-merge,
  code-answer, code-dashboard, code-publish
  (实际 15 个,含 code-merge/code-answer/code-dashboard/code-publish)

[本需求后 11 个 code-* 技能]:
  code-require, code-design, code-plan, code-it, code-check,
  code-fix, code-version, code-init, code-rule, code-auto, code-merge,
  code-answer, code-dashboard, code-publish
  (实际 14 个,移除 code-unit)
```

## 8. 数据与状态

### 8.1 内部变量(非文档字段)

无新增内部变量(本需求是"技能合并",无状态机变更)。

### 8.2 文档结构变更(本需求产出)

| 文档 | 变更类型 | 位置 | 行数变化 |
| --- | --- | --- | --- |
| `plugins/code-skills/skills/code-unit/SKILL.md` | **删除** | 整体 | -635 |
| `plugins/code-skills/skills/code-unit/templates/RESULT.md` | **删除** | 整体 | (待扫描) |
| `plugins/code-skills/skills/code-unit/templates/` | **删除** | 整体目录 | (整体) |
| `plugins/code-skills/skills/code-it/SKILL.md` | 净增守卫 + 按需写单测 | 步骤 8a + 步骤 8.5 + 文档头 | +150 ~ +250 |
| `plugins/code-skills/skills/code-plan/SKILL.md` | 字面改写 | L368/431/445/454/1105 | -10 ~ -20 |
| `plugins/code-skills/skills/code-auto/SKILL.md` | 整段删除 + 字面改写 | L213-227 / L388-411 / L432-433 / L449 / L624-625 / L672 / L692 / L711 / L741 / L797 / L806 / L834 | -50 ~ -80 |
| `plugins/code-skills/skills/code-check/SKILL.md` | 字面改写 | L3/21/40-41/56/72/96/151/281/608/615 | -10 ~ -20 |
| `plugins/code-skills/.claude-plugin/plugin.json` | 字面删除 | L15 | -1 |
| `.claude-plugin/marketplace.json` | 字面删除 | L24 / L39 | -2 |
| `plugins/code-skills/skills/code-it/templates/RESULT.md` | 追加 1 小节 | "## 单元测试" | +20 ~ +40 |
| 4 README + CLAUDE.md | 字面改写 | 描述段 | -10 ~ -30 |
| 7 项目级规范 | 字面改写 | 描述段 | -5 ~ -15 |
| 11 技能描述段 | 字面改写 | frontmatter description | -10 ~ -30 |
| `assistants/V0.0.3/RESULT.md` | 追加 1 行 + 1 条 | §"需求清单" + §"变更记录" | +2 |

## 9. 边界与异常

- **E-1**(本仓库无项目级规范):沿用 `code-require` 既有 `AskUserQuestion`(本需求不介入)
- **E-2**(项目不可测,7 项守卫不命中):`code-it` 步骤 8a 守卫不通过 → 跳过步骤 8.5 → 看板"测试状态"= `不适用` → exit 0(沿用原 `code-unit` E-2 行为)
- **E-3**(任务类型 = `文档`):`code-it` 步骤 8.5 跳过写单测 → 写 `unit-test-results.md` = "本任务不涉及单元测试"(FR-3 锁定)
- **E-4**(`code-unit` 步骤 1 重入 / 老用户手动调):不可用,屏幕输出"⛔ code-unit 已退场,能力整合进 code-it"(FR-1 锁定)
- **E-5**(历史 V0.0.2 / V0.0.3 `test/<TASK-...>/RESULT.md` 存在):字节级保留(NFR-2 沿用);`code-check` 评审时**仍**读 `test/<TASK-...>/RESULT.md` 作为历史参考(FR-7 字面改写**不**影响历史路径)
- **E-6**(`code-auto` 历史 `auto-report.md` 中含 `code-unit 跳过` 日志):字节级保留(NFR-2 沿用);**不**追溯重写
- **E-7**(`code-it` 步骤 8.5 自动判定失败):`code-it` 沿用既有"失败 → 屏显 → 中断"逻辑(本需求不介入)
- **E-8**(`code-it` 步骤 8.5 写单测跑通失败):沿用原 `code-unit` 步骤 11 错误修复循环;最连续失败 5 次后必须停下询问用户

## 10. 验收标准(AC)

### AC-1:`code-unit` 硬删除

- **AC-1.1** `plugins/code-skills/skills/code-unit/SKILL.md` 文件**不存在**(经 `Bash: test -f ... && echo EXISTS || echo NOT_EXISTS` 校验,NOT_EXISTS)
- **AC-1.2** `plugins/code-skills/skills/code-unit/templates/` 目录**不存在**(经 `Bash: test -d ... && echo EXISTS || echo NOT_EXISTS` 校验,NOT_EXISTS)
- **AC-1.3** `plugins/code-skills/skills/code-unit/templates/RESULT.md` 文件**不存在**(经 `Bash: test -f ...` 校验,NOT_EXISTS)
- **AC-1.4** commit message = `chore(code-unit): REQ-00034 移除 code-unit 技能整体`(FR-1 锁定)

### AC-2:`code-it` 接管守卫 7 项

- **AC-2.1** `plugins/code-skills/skills/code-it/SKILL.md` 既有"## 步骤 8"之后**新增**"## 步骤 8a — 项目可测性守卫"
- **AC-2.2** 守卫检查项 7 项**字节级沿用** `code-unit` 步骤 0a.1(逐条命中校验)
- **AC-2.3** 守卫判定逻辑**字节级沿用** `code-unit` 步骤 0a.2(testable = True / False + 屏显模板)
- **AC-2.4** 守卫不通过时,屏幕输出**字节级沿用** `code-unit` 步骤 0a.4 模板("⏭ code-it 跳过单测(项目不可测)")

### AC-3:`code-it` 接管按需写单测

- **AC-3.1** `plugins/code-skills/skills/code-it/SKILL.md` "## 步骤 8a"之后**新增**"## 步骤 8.5 — 按需写单测"
- **AC-3.2** 自动判定逻辑**覆盖** 3 类任务类型(新增/修改/重构/修复 涉及函数级 → 写;文档/配置/类型定义 → 不写;任务"测试状态"= `不适用` → 跳过)
- **AC-3.3** 屏幕输出模板**字节级沿用** `code-unit` 步骤 7("=== code-it 按需写单测(守卫通过)===" + 判定结果)
- **AC-3.4** **不**弹 `AskUserQuestion`(NFR-8 锁定)
- **AC-3.5** 产出物路径 = `code/<TASK-...>/unit-test-results.md`(FR-4 锁定)

### AC-4:`code-it` 模板新增"## 单元测试"小节

- **AC-4.1** `plugins/code-skills/skills/code-it/templates/RESULT.md` **新增**"## 单元测试"小节
- **AC-4.2** 小节内容**包含** 7 个字段(守卫判定 / 测试框架 / 测试文件 / 跑通情况 / 覆盖率 / 跳过的子任务 / 发现的代码 bug)(FR-4 锁定)
- **AC-4.3** 既有章节**不**改(NFR-10 沿用)

### AC-5:`code-plan` 测试状态字段语义改写

- **AC-5.1** `plugins/code-skills/skills/code-plan/SKILL.md` L368 / L431 / L445 / L454 / L1105 共 5 处"由 `code-unit` 另起流程" → "由 `code-it` 内化"
- **AC-5.2** 任务"测试状态"2 枚举(`已运行-通过` / `不适用`)**不**改(沿用 REQ-00031 FR-3)
- **AC-5.3** 任务"双状态"语义 = 开发状态 = 已完成**不**改(沿用 REQ-00031 FR-3)

### AC-6:`code-auto` 步骤 4.b 整段删除

- **AC-6.1** `plugins/code-skills/skills/code-auto/SKILL.md` L388-411 整段**删除**
- **AC-6.2** L213-227 子技能调用表 4 行(`code-unit`)**删除**
- **AC-6.3** L432-433 / L449 / L624-625 / L672 / L692 / L711 / L741 / L797 / L806 / L834 `code-unit` 字面**删除**
- **AC-6.4** `code-auto` 任务循环屏幕日志**减少** 1 行/任务(原"code-unit ... ✓ (跳过,无需测试)"删除)
- **AC-6.5** 步骤 4.a 任务循环 + 步骤 5-7 既有逻辑**0**改

### AC-7:`code-check` `test/<TASK-...>/` 引用收窄

- **AC-7.1** `plugins/code-skills/skills/code-check/SKILL.md` L3 / L21 / L40-41 / L56 / L72 / L96 / L151 / L281 / L608 / L615 共 10 处"test/<任务编码>/" → "code/<任务编码>/unit-test-results.md"
- **AC-7.2** 评审清单 12 维度(8.1-8.12)**0**改
- **AC-7.3** 工作流步骤 0-6**0**改

### AC-8:plugin.json + marketplace.json 注册项删除

- **AC-8.1** `plugins/code-skills/.claude-plugin/plugin.json` L15 `keywords[]` 数组**删除** `"code-unit"`
- **AC-8.2** `.claude-plugin/marketplace.json` L24 `plugins[0].keywords[]` 数组**删除** `"code-unit"`
- **AC-8.3** `.claude-plugin/marketplace.json` L39 `plugins[0].skills[]` 数组**删除** `"./skills/code-unit"`
- **AC-8.4** 2 JSON 文件的 `$schema` / `name` / `version` / `description` 等其他字段**0**改

### AC-9:4 README + CLAUDE.md 字面改写

- **AC-9.1** `README.md`(仓库根)技能表 / 工作流总览:删除 `code-unit` 行
- **AC-9.2** `README.en.md`(仓库根)同 AC-9.1(英文)
- **AC-9.3** `plugins/code-skills/README.md` 同 AC-9.1
- **AC-9.4** `plugins/code-skills/README.en.md` 同 AC-9.1(英文)
- **AC-9.5** `CLAUDE.md`(仓库根)字面量删除 `code-unit` 引用
- **AC-9.6** 字面量"12 个 code-* 技能" → "11 个 code-* 技能"(具体计数由 `code-plan` 阶段重新扫描)

### AC-10:7 项目级规范字面改写

- **AC-10.1** `assistants/rules/encoding-conventions.md` 任务"双状态"测试状态字段语义:沿用 REQ-00031 + 本需求 FR-5
- **AC-10.2** `assistants/rules/review-checklist.md` §8.7 测试质量维度:`code-unit` 引用 → `code-it` 内化
- **AC-10.3** `assistants/rules/skill-conventions.md`:`code-unit` 引用 → `code-it` 内化
- **AC-10.4** `assistants/rules/module-conventions.md`:`code-unit/templates/` 引用删除
- **AC-10.5** `assistants/rules/dashboard-conventions.md`:看板字段"code-unit 跳过"日志描述改写
- **AC-10.6** `assistants/rules/plugin-conventions.md`:plugin.json / marketplace.json `code-unit` 引用删除
- **AC-10.7** `assistants/rules/migration-mapping.md`(若引用 `code-unit`):`code-unit` 引用 → `code-it` 内化
- **AC-10.8** 7 规范核心约束字节级保留(只改字面量)

### AC-11:11 技能描述段字面改写

- **AC-11.1** 11 SKILL.md frontmatter description 字段 / 文档头概述段:删除 `code-unit` 引用
- **AC-11.2** 11 SKILL.md frontmatter L1-3 字节级保留(NFR-1 沿用)
- **AC-11.3** 11 SKILL.md 核心工作流字节级保留
- **AC-11.4** `code-it` 描述段**改写**为"含按需写单测"
- **AC-11.5** `code-auto` 描述段**改写**为"不调 `code-unit`"

### AC-12:零变更校验

- **AC-12.1** V0.0.2 / V0.0.3 既有 `test/<TASK-...>/RESULT.md` 0 改(NFR-2 沿用)
- **AC-12.2** V0.0.2 / V0.0.3 既有 `code/<TASK-...>/test-results.md` 0 改(NFR-2 沿用)
- **AC-12.3** V0.0.2 / V0.0.3 既有 `auto-report.md` 0 改(NFR-2 沿用)
- **AC-12.4** 既有 12 个 REQ 的 `code/<TASK-...>/RESULT.md` 0 改
- **AC-12.5** 既有 12 个 REQ 的 `plan/<需求>/PLAN.md` 0 改(任务"测试状态"列保留原值)
- **AC-12.6** `code-fix` 5 候选状态机 0 改(NFR-12 沿用)
- **AC-12.7** `code-dashboard` 12 维度屏显契约 0 改

### AC-13:看板同步

- **AC-13.1** `assistants/V0.0.3/RESULT.md` §"需求清单" 追加 1 行:需求编码 = REQ-00034,标题 = "移除 /code-unit 技能,能力整合进 /code-it(按需写单测/不适用工程跳过)",状态 = "草稿"
- **AC-13.2** `assistants/V0.0.3/RESULT.md` §"变更记录" 追加 1 条:`2026-06-15 12:00  需求新增  REQ-00034 需求分析完成(...)  REQ-00034`
- **AC-13.3** `assistants/V0.0.3/RESULT.md` 统计区段"总数 + 1"(NFR-9)
- **AC-13.4** 看板其他区段(概要设计清单 / 详细设计 / 任务清单 / 缺陷清单 / 评审发现 / 派生任务)0 改(本需求尚未推进到 design / plan / it / check)

### AC-14:与既有规则协同

- **AC-14.1** 沿用 REQ-00031 元技能改规则(本需求不重做 REQ-00031 5 任务)
- **AC-14.2** 沿用 REQ-00026 最小化变更原则
- **AC-14.3** 沿用 REQ-00030 INV 字节级保留约束
- **AC-14.4** 沿用 REQ-00009 `code-unit` 守卫 7 项检查(由 `code-it` 接管)
- **AC-14.5** 与 BUG-00001 不冲突(NFR-7 锁定)
- **AC-14.6** 沿用 REQ-00032 屏显契约

## 11. 关联需求

| 需求 | 版本 | 关联点 | 影响 |
| --- | --- | --- | --- |
| REQ-00031 | V0.0.3 | "外移单元测试"+"任务粒度收窄"(5 任务已落地) | **前置依赖**;本需求是其"实际删除"补完 |
| REQ-00009 | V0.0.2 | `code-unit` 守卫"项目可测性"(7 项检查) | **强继承**;由 `code-it` 接管,字节级沿用 |
| BUG-00001 | V0.0.3 | 5 技能加"不修改 SKILL.md"硬约束 | **兼容性**;本需求不冲突(NFR-7 锁定) |
| REQ-00026 | V0.0.3 | SKILL.md 描述通用化扫除(10 SKILL.md) | 沿用最小化变更原则 |
| REQ-00030 | V0.0.3 | 元技能改 + 12 维度评审 + INV 字节级保留 | 沿用 INV 校验 |
| REQ-00032 | V0.0.3 | `code-require` 屏显契约 | 沿用 |
| REQ-00033 | V0.0.3 | `code-require` 不涉及技术选型 | 沿用(本需求不涉及) |
| REQ-00007 | V0.0.3 | `code-auto` 整版本自动流水线 | 部分影响:步骤 4.b 删除后,`code-auto` 屏幕日志减少 1 行/任务 |
| REQ-00017 | V0.0.2 | `code-plan` 拆任务约束 | 沿用 |
| REQ-00025 | V0.0.3 | 软化编号正则约束 | 沿用 |

## 12. 待澄清 / 未决项

- **Q-1**(本需求下游 `code-plan` 是否自动接管 `code-auto` 步骤 4 屏幕日志格式修订):本需求**不**实现(`code-auto` 描述段字面改写已涵盖,见 FR-11.5);留作 follow-up
- **Q-2**(`code-rule` 是否沉淀 `testing-conventions.md` 单测规范):本需求**不**实现(避免越界 `code-rule` 改造);留作 follow-up
- **Q-3**(`code-it` 步骤 8.5 自动判定的"任务性质"判据表是否需要细化):本需求 FR-3 锁定 3 大类(函数级 / 文档 / 配置);具体判据由 `code-plan` 阶段细化
- **Q-4**(`code-it` 步骤 8.5 是否接管 `code-unit` 步骤 12 覆盖率分析):本需求**包含**(FR-3 锁定接管守卫 7 项 + 按需写单测 + 跑通 + 写 `unit-test-results.md`);**不**接管 `code-unit` 步骤 12 详细覆盖率分析(避免 `code-it` 净增过多行;覆盖率分析由 `code-check` 评审时按需补)
- **Q-5**(本需求是否在 `code-check` 评审清单 §8.7 测试质量维度**新增**"按需写单测"校验点):本需求**不**实现(避免越过本需求边界到 `code-check` 评审清单扩展);留作 follow-up
- **Q-6**(`code-it` 接管守卫后,既有 `code-unit` 步骤 0a.3 守卫不通过时"不写 `test/<任务编码>/RESULT.md`"语义如何处理):本需求**统一**改为"不写 `code/<任务编码>/unit-test-results.md`(或写 '不适用' 占位)";由 `code-plan` 阶段细化
- **Q-7**(历史 `code-unit` 步骤 4 行为(已编写/已运行-通过/已运行-失败/不适用/阻塞 5 测试状态判定)如何映射到 `code-it` 步骤 8.5):本需求**简化**为 2 状态(已运行-通过 / 不适用,与 REQ-00031 FR-3 一致);既有 5 状态中"已编写 / 已运行-失败 / 阻塞"3 个状态**不**继承(由 `code-it` 步骤 8.5 内部处理)
- **Q-8**(`code-it` 步骤 8.5 是否承担 `code-unit` 步骤 9 错误修复循环(最连续失败 5 次后必须停下询问用户)):本需求**包含**(FR-3 锁定接管;E-8 沿用原 `code-unit` 步骤 11 行为)

## 13. 变更记录

```
2026-06-15 12:00  需求新增  REQ-00034 需求分析完成(共 12 FR / 12 NFR / 8 大类共 50+ AC);本需求唯一硬删除对象 = code-unit/SKILL.md(635 行) + code-unit/templates/ 整体;code-it 接管守卫 7 项 + 按需写单测;code-plan/auto/check 适配;0 改既有 12 个 REQ + 0 改 frontmatter / 0 改工程代码  REQ-00034
```
