# 概要设计 — REQ-00034 移除 /code-unit 技能,能力整合进 /code-it(按需写单测/不适用工程跳过)

- 需求编码:REQ-00034
- 所属版本:V0.0.3
- 文档创建时间:2026-06-15 13:30
- 最近更新:2026-06-15 13:30
- 文档状态:已完成
- 上游:`./assistants/V0.0.3/require/REQ-00034/RESULT.md`
- 遵循规范:`./assistants/rules/` 下 12 个文件(全沿用,无新增)
- 涉及技能:`code-unit`(整体删除) + `code-it`(接管守卫 + 按需写单测)+ `code-plan` / `code-auto` / `code-check`(适配)+ 2 JSON + 4 README + CLAUDE.md + 7 项目级规范 + 11 技能描述段

## 1. 设计目标

- **整体设计目标**:`--extensible`(触发条件 2:模块拆分预评估涉及模块数 ≥ 3 = 29 个文件)
- **维度优先级**:功能性 = 中(技能合并涉及"按需写单测"功能接管)
- **设计目标确认路径**:`code-auto` 上下文检测到,采纳 `--extensible` 默认 0 问(沿用 REQ-00030 FR-2 收敛:大需求 + 扩展性触发 → 1 个 `AskUserQuestion` 整体,但 `code-auto` 上下文 0 问)

## 2. 设计概述

**核心决策**:**移除** `code-unit` 技能(整体删除 SKILL.md 635 行 + templates/ 目录),将其能力("编写单元测试 + 执行测试" + "项目可测性守卫 7 项")**整合进** `code-it`。涉及 5 SKILL.md / 2 JSON / 4 README / CLAUDE.md / 7 项目级规范 / 11 技能描述段 / 1 目录删除,共约 30 个文件,净变化约 -600 ~ -800 行(技能合并)。

**关键边界**:
- `code-unit` 步骤 0a 7 项守卫**字节级沿用**至 `code-it` 步骤 8a
- `code-unit` 步骤 4 测试状态判定**简化**为 2 状态(`已运行-通过` / `不适用`,沿用 REQ-00031 FR-3)
- `code-unit` 步骤 7 屏幕输出模板**沿用**至 `code-it` 步骤 8.5
- `code-unit` 步骤 11 错误修复循环**沿用**至 `code-it` 步骤 12(最连续失败 5 次停下)
- `code-unit` 步骤 12 详细覆盖率分析**不**接管(避免 `code-it` 净增过多行;覆盖率由 `code-check` 评审时按需补)
- 历史 V0.0.2 / V0.0.3 既有 `test/<TASK-...>/RESULT.md` + `code/<TASK-...>/test-results.md` **字节级保留**(NFR-2 沿用 REQ-00031)

## 3. 关键设计决策(15 项,详见 `design-notes.md`)

### 决策 D-1:`code-unit` 整体删除(无字节级保留)

**理由**:用户原始输入"**移除**技能 `/code-unit`"+ 候选方案(占位 / 改名)均与字面冲突,激进删除是唯一契合方案(FR-1 锁定)

### 决策 D-2:`code-it` 步骤 8a 字节级沿用 `code-unit` 步骤 0a 7 项守卫

**理由**:守卫逻辑是已落地的产品需求(REQ-00009),字节级沿用保证行为 0 漂移;`code-it` 步骤 8a 锚点 = "## 步骤 8"之后,"## 步骤 9"之前(FR-2 锁定)

### 决策 D-3:`code-it` 步骤 8.5 自动判定 3 类任务(无用户问路)

**理由**:用户原始输入"**根据需要**直接编写单元测试"隐含**不**问;Q-4 隐含答复 C(自动判定);3 大类(函数级 → 写;文档/配置/类型定义 → 不写;不适用 → 跳过)(FR-3 锁定)

### 决策 D-4:任务"测试状态"简化至 2 状态(沿用 REQ-00031 FR-3)

**理由**:既有 `code-unit` 步骤 4 5 状态(`已编写` / `已运行-通过` / `已运行-失败` / `不适用` / `阻塞`)中 3 个中间态(`已编写` / `已运行-失败` / `阻塞`)由 `code-it` 步骤 8.5 内部处理(直接重新跑测试,不细化到 5 状态);看板只显示 2 状态(FR-5 / Q-7 锁定)

### 决策 D-5:`code-it` 接管 `code-unit` 步骤 11 错误修复循环

**理由**:错误修复循环是"写单测 + 跑通"的固有环节,接管保证连续性;E-8 沿用"最连续失败 5 次后停下询问用户"语义(FR-3 / E-8 锁定)

### 决策 D-6:`code-it` **不**接管 `code-unit` 步骤 12 详细覆盖率分析

**理由**:覆盖率分析是"评审阶段"职责,非"开发阶段"职责;`code-check` 评审时按需补可避免 `code-it` 净增过多行;Q-4 锁定

### 决策 D-7:`code-it` 步骤 8.5 产出 `code/<TASK-...>/unit-test-results.md`(新模板,非沿用 `test-results.md`)

**理由**:既有 `code-it/templates/RESULT.md` 的 `test-results.md` 语义是"项目自身的集成/冒烟测试结果";`code-it` 接管后,**新增** `unit-test-results.md` 模板,语义是"守卫判定 + 写单测 + 跑通"(FR-4 锁定;Q-6 细化)

### 决策 D-8:`code-plan` 测试状态字段语义收窄为"`code-it` 内化"

**理由**:原"由 `code-unit` 另起流程"语义已过时(本需求后 `code-unit` 退场);沿用既有"由 `code-it` 内化"语义,5 处字面改写(FR-5 锁定)

### 决策 D-9:`code-auto` 步骤 4.b 整段删除

**理由**:`code-plan` 不再产出测试任务 + `code-unit` 退场 → 步骤 4.b 整体删除;屏幕日志减少 1 行/任务(原"code-unit 跳过"日志删除);为后续若 `code-plan` 重新启用测试规划时**字节级**还原本步骤 4.b 预留(FR-6 锁定)

### 决策 D-10:`code-check` `test/<TASK-...>/` 引用收窄

**理由**:评审时不再需要找 `test/<TASK-...>/RESULT.md`;直接读 `code/<TASK-...>/unit-test-results.md`(由 `code-it` 自含);10 处字面改写(FR-7 锁定)

### 决策 D-11:plugin.json + marketplace.json 注册项删除

**理由**:技能物理删除后,注册项必须同步删除(否则残留死引用);3 处字面删除(FR-8 锁定)

### 决策 D-12:4 README + CLAUDE.md 字面改写

**理由**:`doc-conventions.md` 规则 2 要求主语言版本完整 + 规则 1 要求中英版本结构对仗;字面改写"12 → 11" + 删除 `code-unit` 行(FR-9 锁定)

### 决策 D-13:7 项目级规范字面改写(只改字面,核心约束保留)

**理由**:本需求不引入新规范,只改 7 份既有规范的字面量以去 `code-unit` 引用(FR-10 锁定)

### 决策 D-14:11 技能描述段字面改写(frontmatter 字节级保留)

**理由**:各 SKILL.md 描述段引用 `code-unit` 是历史背景,本需求后**不再**有 `code-unit` 技能 → 描述段必须同步;frontmatter L1-3 字节级保留(FR-11 锁定)

### 决策 D-15:不修改其他 8 个 `code-*` 技能核心工作流

**理由**:`code-require` / `code-design` / `code-fix` / `code-init` / `code-publish` / `code-version` / `code-rule` / `code-merge` / `code-answer` / `code-dashboard` 10 个 SKILL.md 的核心工作流**0**改;只动描述段;FR-12 锁定

## 4. 模块拆分(本设计 0 新增,3 状态汇总)

| 类别 | 数量 | 文件 |
| --- | --- | --- |
| **硬删除** | 1 技能 + 1 模板目录 | `code-unit/SKILL.md` (635) + `code-unit/templates/` 整体 |
| **改造既有(扩展)** | 5 SKILL.md | `code-it`(净增 +150~+250)+ `code-plan`(-10~+20)+ `code-auto`(-50~+80)+ `code-check`(-10~+20)+ `code-it/templates/RESULT.md`(+20~+40) |
| **字面改写** | 2 JSON + 4 README + CLAUDE.md + 7 规范 + 11 描述段 | 详见 `materials-index.md` §3.1.3 ~ §3.1.6 |
| **保留** | V0.0.2 / V0.0.3 既有历史档案 | `test/<TASK-...>/RESULT.md` + `code/<TASK-...>/test-results.md` + `auto-report.md` |
| **净变化** | **约 -600 ~ -800 行**(技能合并;删除多于新增) | |

## 5. 接口(本设计 0 新增,1 类修改)

| 接口 | 形式 | 状态 | 职责 |
| --- | --- | --- | --- |
| `code-it` 步骤 8a | 函数 | 新增 | 项目可测性守卫 7 项检查 |
| `code-it` 步骤 8.5 | 函数 | 新增 | 按需写单测(自动判定) |
| `code-it/templates/RESULT.md` 模板 | Markdown | 修改(追加 1 小节) | 新增"## 单元测试"小节 |
| `code-it/产出物:unit-test-results.md` | Markdown | 新增 | 守卫判定 + 写单测 + 跑通结果 |
| 既有 `code-unit/接口` | 全部 | 退场 | (随 `code-unit` 删除) |

## 6. 数据结构(本设计 0 新增,0 修改)

## 7. 三方依赖(本设计 0 新增,0 修改)

| 依赖名 | 用途 | 必要性 | 替代评估 |
| --- | --- | --- | --- |
| — | — | — | (NFR-5 0 新增) |

## 8. 修改文件定位(语义化锚点,本设计 29 个文件)

| 路径 | 锚点 | 改造内容 |
| --- | --- | --- |
| `code-unit/SKILL.md` | 整体 | 硬删除 |
| `code-unit/templates/` | 整体目录 | 硬删除 |
| `code-it/SKILL.md` | 文档头 ## 目标 | 删除 L14 反向声明 + 改写为"含按需写单测" |
| `code-it/SKILL.md` | § 步骤 8 之后 | 新增"## 步骤 8a — 项目可测性守卫" |
| `code-it/SKILL.md` | § 步骤 8a 之后 | 新增"## 步骤 8.5 — 按需写单测" |
| `code-it/SKILL.md` | L18, L795, L907-908 | 删除 `code-unit` 引用 |
| `code-it/SKILL.md` | L54, L83, L531, L632, L735-736 | `test-results.md` 收窄语义 |
| `code-it/templates/RESULT.md` | 既有章节 | 追加"## 单元测试"小节 |
| `code-plan/SKILL.md` | L368, L431, L445, L454, L1105 | "由 `code-unit` 另起流程" → "由 `code-it` 内化" |
| `code-auto/SKILL.md` | L45, L213-227, L388-411, L432-433, L449, L624-625, L672, L692, L711, L741, L797, L806, L834 | 删除 `code-unit` 字面 |
| `code-check/SKILL.md` | L3, L21, L40-41, L56, L72, L96, L151, L281, L608, L615 | `test/<TASK-...>/` → `code/<TASK-...>/unit-test-results.md` |
| `plugin.json` | L15 | 删除 `"code-unit"` keyword |
| `marketplace.json` | L24, L39 | 删除 `"code-unit"` keyword + skill |
| 4 README + CLAUDE.md | 描述段 | 字面改写 |
| 7 项目级规范 | 描述段 | 字面改写 |
| 11 技能描述段 | frontmatter description | 字面改写 |

## 9. 不变量(共 12 条,INV-1 ~ INV-12)

| INV | 约束 | 范围 |
| --- | --- | --- |
| INV-1 | frontmatter L1-3 字节级保留 | `code-it` / `code-plan` / `code-auto` / `code-check` + 11 描述段 |
| INV-2 | "## 不要做的事" 既有小节 0 改 | 4 个被改 SKILL.md |
| INV-3 | "## 工作流程" 既有步骤字节级保留 | `code-it` 步骤 0a/0-8/9-16(8a / 8.5 是**纯新增**);`code-auto` 步骤 0a-3/5-7(4.b 整段删除) |
| INV-4 | 10 个其他 `code-*` 技能 SKILL.md 核心工作流 0 改 | `code-require` / `code-design` / `code-fix` / `code-init` / `code-publish` / `code-version` / `code-rule` / `code-merge` / `code-answer` / `code-dashboard` |
| INV-5 | 12 个项目级规范 0 改核心约束(只改字面) | `./assistants/rules/*.md` |
| INV-6 | 4 README + CLAUDE.md 0 改非描述段 | 顶层配置 |
| INV-7 | 既有 12 个 REQ 的 `code/<TASK-...>/RESULT.md` + `plan/<需求>/PLAN.md` 0 改 | 历史档案 |
| INV-8 | 0 新增三方依赖 | NFR-5 锁定 |
| INV-9 | 0 触发 dashboard-conventions 字段扩展 | 看板只追加既有区段内的行 |
| INV-10 | 历史 `test/<TASK-...>/RESULT.md` 字节级保留 | V0.0.2 / V0.0.3 全部历史档案 |
| INV-11 | `code-fix` 5 候选状态机 0 改 | 沿用 REQ-00027 |
| INV-12 | `code-dashboard` 12 维度屏显契约 0 改 | 沿用既有 |

## 10. 边界与异常

- **E-1**(本仓库无项目级规范):沿用 `code-require` 既有 `AskUserQuestion`(本需求不介入)
- **E-2**(项目不可测,7 项守卫不命中):`code-it` 步骤 8a 守卫不通过 → 跳过步骤 8.5 → 看板"测试状态"= `不适用` → exit 0(沿用原 `code-unit` E-2 行为)
- **E-3**(任务类型 = `文档`):`code-it` 步骤 8.5 跳过写单测 → 写 `unit-test-results.md` = "本任务不涉及单元测试"(FR-3 锁定)
- **E-4**(`code-unit` 步骤 1 重入 / 老用户手动调):不可用,屏幕输出"⛔ code-unit 已退场,能力整合进 code-it"(FR-1 锁定)
- **E-5**(历史 V0.0.2 / V0.0.3 `test/<TASK-...>/RESULT.md` 存在):字节级保留(NFR-2 沿用);`code-check` 评审时**仍**读 `test/<TASK-...>/RESULT.md` 作为历史参考(FR-7 字面改写**不**影响历史路径)
- **E-6**(`code-auto` 历史 `auto-report.md` 中含 `code-unit 跳过` 日志):字节级保留(NFR-2 沿用);**不**追溯重写
- **E-7**(`code-it` 步骤 8.5 自动判定失败):`code-it` 沿用既有"失败 → 屏显 → 中断"逻辑(本需求不介入)
- **E-8**(`code-it` 步骤 8.5 写单测跑通失败):沿用原 `code-unit` 步骤 11 错误修复循环;最连续失败 5 次后必须停下询问用户(FR-3 锁定)

## 11. 衔接

- **下游**:`code-plan` 消费本设计做实施计划(候选 14 任务;实际由 `code-plan` 阶段细化)
- **上游**:`code-require` 的 `RESULT.md`(本设计只读)
- **横向**:
  - 与 REQ-00031(任务粒度 + 元技能改)协同
  - 与 REQ-00009(`code-unit` 守卫 7 项)协同
  - 与 BUG-00001("不修改 SKILL.md")协同(NFR-7 锁定)
  - 与 REQ-00026(最小化变更)协同
  - 与 REQ-00030(INV 字节级保留)协同
  - 与 REQ-00032(屏显契约)协同
  - 与 REQ-00033(不涉及技术选型)协同

## 12. 变更记录

```
2026-06-15 13:30  设计新增  REQ-00034 概要设计完成(15 决策 / 12 不变量 / 0 新增模块 / 1 新增接口类 / 0 数据结构 / 0 依赖);整体=--extensible,功能性=中(触发条件 2:29 个文件 ≥ 3);0 触发扩展性问路(code-auto 上下文 0 问);0 冲突;候选 14 任务(由 code-plan 阶段细化)  REQ-00034
```
