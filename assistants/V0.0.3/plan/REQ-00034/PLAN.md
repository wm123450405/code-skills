# 编码计划 — REQ-00034 移除 /code-unit 技能,能力整合进 /code-it(按需写单测/不适用工程跳过)

- 需求编码:REQ-00034
- 所属版本:V0.0.3
- 文档创建时间:2026-06-15 14:00
- 最近更新:2026-06-15 14:00
- 文档状态:已完成
- 计划标题:移除 /code-unit 技能,能力整合进 /code-it
- 整体设计目标:`--extensible`(功能性 = 中)
- 任务总数:**10**(候选 14 合并)
- 任务类型:修改(主) + 新增(2 个"code-it 步骤 8a / 8.5" 行为接管) + 删除(1 个 `code-unit` 硬删除)

---

## 1. 计划概述

**核心改造**:`code-unit` 技能整体删除 + `code-it` 接管项目可测性守卫 7 项 + 按需写单测。涉及 29 个文件,净变化约 -600 ~ -800 行。

**任务合并策略**(候选 14 → 实际 10):
- T-001 + T-002 合并(都是 code-it 改造):T-001 `code-it` 步骤 8a + 8.5 + 文档头 + L18/L795/L907-908 字面
- T-003 + T-004 + T-005 合并(都是 `code-it` 模板改造):T-002 `code-it` 模板新增"## 单元测试"小节
- T-006 `code-plan` 字面改写(单任务)
- T-007 + T-008 合并(都是 `code-auto` 改造):T-003 `code-auto` 步骤 4.b 删除 + 10 处字面
- T-009 `code-check` 10 处字面改写(单任务)
- T-010 2 JSON 注册项删除(单任务)
- T-011 4 README + CLAUDE.md 字面改写(单任务)
- T-012 7 项目级规范字面改写(单任务)
- T-013 11 技能描述段字面改写(单任务)
- T-014 看板同步(单任务)

## 2. 任务总览

| 任务编号 | 类型 | 触发/来源 | 标题 | 开发状态 | 测试状态 | 涉及文件 | 关联任务 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TASK-REQ-00034-00001 | 修改 | 详细设计 | [修改] code-it 步骤 8a 守卫 + 步骤 8.5 按需写单测接管 + 文档头/L18/L795/L907-908 字面改写 | 已完成 | 不适用 | `plugins/code-skills/skills/code-it/SKILL.md` §"## 步骤 8"之后新增"## 步骤 8a / 8.5" + 文档头 + L18 + L795 + L907-908 | — |
| TASK-REQ-00034-00002 | 修改 | 详细设计 | [修改] code-it 模板新增"## 单元测试"小节 | 已完成 | 不适用 | `plugins/code-skills/skills/code-it/templates/RESULT.md` 既有章节追加 1 小节 | — |
| TASK-REQ-00034-00003 | 修改 | 详细设计 | [修改] code-plan/SKILL.md L368/431/445/454/1105 字面改写(由 `code-unit` 另起流程 → 由 `code-it` 内化) | 已完成 | 不适用 | `plugins/code-skills/skills/code-plan/SKILL.md` § L368 / L431 / L445 / L454 / L1105 | — |
| TASK-REQ-00034-00004 | 修改 | 详细设计 | [修改] code-auto/SKILL.md 步骤 4.b 整段删除 + 10 处字面改写 | 已完成 | 不适用 | `plugins/code-skills/skills/code-auto/SKILL.md` L45 + L213-227 + L388-411 + L432-433 + L449 + L624-625 + L672 + L692 + L711 + L741 + L797 + L806 + L834 | — |
| TASK-REQ-00034-00005 | 修改 | 详细设计 | [修改] code-check/SKILL.md 10 处 test/<TASK-...>/ 引用改写 | 已完成 | 不适用 | `plugins/code-skills/skills/code-check/SKILL.md` L3 + L21 + L40-41 + L56 + L72 + L96 + L151 + L281 + L608 + L615 | — |
| TASK-REQ-00034-00006 | 修改 | 详细设计 | [修改] plugin.json + marketplace.json 注册项删除(3 处字面) | 已完成 | 不适用 | `plugins/code-skills/.claude-plugin/plugin.json` L15 + `.claude-plugin/marketplace.json` L24 / L39 | — |
| TASK-REQ-00034-00007 | 修改 | 详细设计 | [修改] 4 README + CLAUDE.md 字面改写(去 `code-unit` 引用) | 已完成 | 不适用 | `README.md` + `README.en.md` + `plugins/code-skills/README.md` + `plugins/code-skills/README.en.md` + `CLAUDE.md` 描述段 | — |
| TASK-REQ-00034-00008 | 修改 | 详细设计 | [修改] 7 项目级规范字面改写(去 `code-unit` 引用) | 已完成 | 不适用 | `assistants/rules/encoding-conventions.md` + `review-checklist.md` + `skill-conventions.md` + `module-conventions.md` + `dashboard-conventions.md` + `plugin-conventions.md` + `migration-mapping.md` 描述段 | — |
| TASK-REQ-00034-00009 | 修改 | 详细设计 | [修改] 11 技能 SKILL.md 描述段去 `code-unit` 引用(`code-it` 改写为"含按需写单测") | 已完成 | 不适用 | `plugins/code-skills/skills/{code-require, code-design, code-plan, code-fix, code-init, code-publish, code-version, code-rule, code-merge, code-answer, code-dashboard, code-auto, code-it}/SKILL.md` frontmatter description 字段 | — |
| TASK-REQ-00034-00010 | 删除 | 详细设计 | [删除] code-unit 整体(SKILL.md 635 行 + templates/ 目录) | 已完成 | 不适用 | `plugins/code-skills/skills/code-unit/SKILL.md` 整体 + `plugins/code-skills/skills/code-unit/templates/` 整体 | — |

**统计**:
- 任务总数:10
- 开发=已完成:10
- 测试=不适用:10
- 完成定义:任务开发=已完成 ∧ 测试∈{已运行-通过, 不适用}(沿用 REQ-00031 FR-3)
- 里程碑:M1-REQ-00034(10 任务全部开发=已完成 ∧ 测试=不适用)

## 3. 任务详情

### TASK-REQ-00034-00001:[修改] code-it 步骤 8a 守卫 + 步骤 8.5 按需写单测接管

- **目标**:`code-it` 接管 `code-unit` 项目可测性守卫 7 项 + 按需写单测
- **涉及文件**:`plugins/code-skills/skills/code-it/SKILL.md`
- **关键变更**:
  1. 文档头 ## 目标段:删除"`code-it` 不含'编写单元测试'或'执行单元测试'(那属于 `code-unit` 职责)"反向声明;**改写**为"含按需写单测(项目可测性守卫 7 项 + 写单测 + 跑通);**不**弹 `AskUserQuestion`"
  2. L18 "`code-unit` 不得修改生产代码" → 删除
  3. L795 "(可选)调 code-unit 补/验证单测" 步骤 3 → 删除
  4. L907-908 "`code-unit` 与 `code-check` 在本任务完成后对本次变更展开" → 改写为"`code-check` 在本任务完成后对本次变更展开"
  5. **新增**"## 步骤 8a — 项目可测性守卫"(字节级沿用 `code-unit` 步骤 0a 7 项检查)
  6. **新增**"## 步骤 8.5 — 按需写单测"(自动判定 3 类,无 `AskUserQuestion`)
- **边界与异常**:
  - 既有 9 步(步骤 0a / 0 / 1-16)**0**改(8a / 8.5 是**纯新增**)
  - 步骤 12 错误修复循环**沿用**(最连续失败 5 次停下)
  - 步骤 13 撰写 `code/<任务>/RESULT.md` **沿用**;`unit-test-results.md` 独立产出
- **验证手段**:
  - `git diff` 校验 frontmatter L1-3 字节级保留
  - `git diff` 校验 L18 / L795 / L907-908 字面改写
  - `git diff` 校验 8a / 8.5 是**纯新增**段
  - `git diff --stat` 校验净增行数在 +150 ~ +250 范围内
  - 9 项 AC-2.x / AC-3.x 校验点全过
- **回退方式**:`git revert <commit-hash>`(单 commit 回退)
- **完成定义**:
  - 文档头字面改写与 L18 / L795 / L907-908 字面删除
  - 8a 守卫 7 项字节级沿用
  - 8.5 自动判定 3 类 + 不弹 `AskUserQuestion` + 产出 `unit-test-results.md`
  - 既有 9 步 0 改
  - frontmatter 字节级保留

### TASK-REQ-00034-00002:[修改] code-it 模板新增"## 单元测试"小节

- **目标**:`code-it/templates/RESULT.md` 追加 1 小节
- **涉及文件**:`plugins/code-skills/skills/code-it/templates/RESULT.md`
- **关键变更**:
  - 在既有章节中**追加** 1 小节"## 单元测试(由 code-it 内化)"
  - 小节包含 7 字段:守卫判定 / 测试框架 / 测试文件 / 跑通情况 / 覆盖率 / 跳过的子任务 / 发现的代码 bug
- **边界与异常**:既有章节 0 改(NFR-10 沿用)
- **验证手段**:`git diff` 校验既有章节字节级保留
- **回退方式**:`git revert <commit-hash>`
- **完成定义**:
  - 既有章节 0 改
  - 新增 1 小节含 7 字段
  - 净增 +20 ~ +40 行

### TASK-REQ-00034-00003:[修改] code-plan/SKILL.md L368/431/445/454/1105 字面改写

- **目标**:`code-plan` 测试状态字段语义改写
- **涉及文件**:`plugins/code-skills/skills/code-plan/SKILL.md`
- **关键变更**:
  - 5 处"由 `code-unit` 另起流程" → "由 `code-it` 内化(`code-it` 步骤 8a 守卫 + 步骤 8.5 按需写单测)"
  - 5 处"code-unit 阶段记录到 `code/<任务>/test-results.md`" → "由 `code-it` 步骤 8.5 产出 `code/<任务>/unit-test-results.md`"
- **边界与异常**:
  - 任务"测试状态"2 枚举(`已运行-通过` / `不适用`)**0**改(沿用 REQ-00031 FR-3)
  - 任务"双状态"语义 = 开发状态 = 已完成**0**改
- **验证手段**:`git diff` 校验 5 处字面改写
- **回退方式**:`git revert <commit-hash>`
- **完成定义**:5 处字面改写与 2 枚举 0 改

### TASK-REQ-00034-00004:[修改] code-auto/SKILL.md 步骤 4.b 整段删除 + 10 处字面

- **目标**:`code-auto` 步骤 4.b 整段删除 + 10 处 `code-unit` 字面删除
- **涉及文件**:`plugins/code-skills/skills/code-auto/SKILL.md`
- **关键变更**:
  1. L45 `test/<任务编码>/` 目录引用 → 删除
  2. L213-227 子技能调用表 4 行(`code-unit`) → 删除
  3. L388-411 步骤 4.b "code-unit 步骤"整段 → 删除
  4. L432-433 / L449 派生任务循环段 → 删除
  5. L624-625 / L672 / L692 / L711 / L741 屏幕日志 + 报告段 → 删除
  6. L797 / L806 衔接 → 删除
  7. L834 "不要做的事"段"不要修改 `code-unit`" → 删除
- **边界与异常**:
  - 步骤 4.a 任务循环 + 步骤 5-7 既有逻辑**0**改
  - 屏幕日志减少 1 行/任务
- **验证手段**:
  - `git diff` 校验步骤 4.b 整段删除
  - `git diff` 校验 10 处字面删除
  - 步骤 4.a 字节级保留
- **回退方式**:`git revert <commit-hash>`
- **完成定义**:
  - 步骤 4.b 整段删除
  - 10 处 `code-unit` 字面删除
  - 步骤 4.a + 步骤 5-7 0 改

### TASK-REQ-00034-00005:[修改] code-check/SKILL.md 10 处 test/<TASK-...>/ 引用改写

- **目标**:`code-check` `test/<TASK-...>/` 引用改写为 `code/<TASK-...>/unit-test-results.md`
- **涉及文件**:`plugins/code-skills/skills/code-check/SKILL.md`
- **关键变更**:
  - 10 处"`./assistants/<版本号>/test/<任务编码>/RESULT.md`" → "`./assistants/<版本号>/code/<任务编码>/unit-test-results.md`(由 `code-it` 步骤 8.5 自含)"
  - 10 处"`code-unit` 产出(只读,作为评审上下文)" → "`code-it` 自含的 `unit-test-results.md`"
- **边界与异常**:
  - 评审清单 12 维度(8.1-8.12)**0**改
  - 工作流步骤 0-6**0**改
- **验证手段**:`git diff` 校验 10 处字面改写 + 12 维度 0 改
- **回退方式**:`git revert <commit-hash>`
- **完成定义**:
  - 10 处字面改写
  - 12 维度 0 改
  - 工作流 0 改

### TASK-REQ-00034-00006:[修改] plugin.json + marketplace.json 注册项删除(3 处字面)

- **目标**:2 JSON 文件注册项同步删除
- **涉及文件**:`plugins/code-skills/.claude-plugin/plugin.json` + `.claude-plugin/marketplace.json`
- **关键变更**:
  - plugin.json L15 `keywords[]` 数组**删除** `"code-unit"`
  - marketplace.json L24 `plugins[0].keywords[]` 数组**删除** `"code-unit"`
  - marketplace.json L39 `plugins[0].skills[]` 数组**删除** `"./skills/code-unit"`
- **边界与异常**:
  - 2 JSON 的 `$schema` / `name` / `version` / `description` / `author` / `owner` / `source` **0**改
- **验证手段**:
  - `git diff` 校验 3 处字面删除
  - `python -m json.tool < plugin.json` 校验 JSON 合法性
  - `python -m json.tool < marketplace.json` 校验 JSON 合法性
- **回退方式**:`git revert <commit-hash>`
- **完成定义**:
  - 3 处字面删除
  - 2 JSON 合法性
  - 其他字段 0 改

### TASK-REQ-00034-00007:[修改] 4 README + CLAUDE.md 字面改写

- **目标**:顶层文档去 `code-unit` 引用
- **涉及文件**:5 个文件(README.md + README.en.md + plugins/code-skills/README.md + plugins/code-skills/README.en.md + CLAUDE.md)
- **关键变更**:
  - 技能表 / 工作流总览描述段:删除 `code-unit` 行
  - 字面量"12 个 code-* 技能" → "11 个 code-* 技能"
  - 主流程图:`code-it → code-unit → code-check` → `code-it → code-check`
- **边界与异常**:其他技能描述 0 改
- **验证手段**:
  - `git diff` 校验 5 个文件字面改写
  - 字面量计数:实际 "N 个" 与 grep 一致
- **回退方式**:`git revert <commit-hash>`
- **完成定义**:
  - 5 个文件字面改写
  - "12 → 11" 字面量一致
  - 其他描述 0 改

### TASK-REQ-00034-00008:[修改] 7 项目级规范字面改写

- **目标**:7 份项目级规范去 `code-unit` 引用
- **涉及文件**:7 个文件(本仓库当前 12 个,本需求**仅**触及 7 个)
- **关键变更**:`code-unit` 字面**全部删除**或改写为"`code-it` 内化";核心约束字节级保留
- **边界与异常**:7 规范核心约束 0 改
- **验证手段**:`git diff` 校验 7 个文件字面改写 + 核心约束保留
- **回退方式**:`git revert <commit-hash>`
- **完成定义**:
  - 7 个文件字面改写
  - 核心约束 0 改

### TASK-REQ-00034-00009:[修改] 11 技能 SKILL.md 描述段去 `code-unit` 引用

- **目标**:11 技能描述段去 `code-unit` 引用
- **涉及文件**:11 个 SKILL.md 的 frontmatter `description` 字段
- **关键变更**:
  - 11 个 description 字段删除 `code-unit` 字面
  - `code-it` 描述段**改写**为"含按需写单测"
  - `code-auto` 描述段**改写**为"不调 `code-unit`"
- **边界与异常**:
  - 各 SKILL.md frontmatter L1-3 字节级保留
  - 各 SKILL.md 核心工作流字节级保留
- **验证手段**:
  - `git diff` 校验 11 个 SKILL.md frontmatter 字面改写
  - md5sum 校验各 SKILL.md frontmatter L1-3
- **回退方式**:`git revert <commit-hash>`
- **完成定义**:
  - 11 个描述段字面改写
  - frontmatter L1-3 字节级保留
  - 核心工作流 0 改

### TASK-REQ-00034-00010:[删除] code-unit 整体(SKILL.md 635 行 + templates/ 目录)

- **目标**:`code-unit` 技能整体删除
- **涉及文件**:
  - `plugins/code-skills/skills/code-unit/SKILL.md`(整体,635 行)
  - `plugins/code-skills/skills/code-unit/templates/RESULT.md`(整体)
  - `plugins/code-skills/skills/code-unit/templates/` 整体目录
- **关键变更**:
  - `git rm -r plugins/code-skills/skills/code-unit/` 整段删除
- **边界与异常**:
  - **不**影响 `plugins/code-skills/skills/code-merge/SKILL.md`(独立技能)
  - **不**影响 V0.0.2 / V0.0.3 既有 `test/<TASK-...>/RESULT.md`(历史档案保留)
- **验证手段**:
  - `git status` 校验 `code-unit/SKILL.md` 不存在
  - `git status` 校验 `code-unit/templates/` 不存在
  - `git status` 校验 `code-unit/templates/RESULT.md` 不存在
- **回退方式**:`git revert <commit-hash>`(单 commit 回退,可恢复)
- **完成定义**:
  - `code-unit/SKILL.md` 不存在
  - `code-unit/templates/` 不存在
  - `code-unit/templates/RESULT.md` 不存在
  - commit message = `chore(code-unit): REQ-00034 移除 code-unit 技能整体`

## 4. 任务依赖图

不适用(本计划拆 10 任务,均**无前置依赖**;沿用 `code-it` 末尾兜底 P-1 推进看板的"按 PLAN.md 任务总览行序"路径)

## 5. 里程碑

| 里程碑 | 包含任务范围 | 完成定义 | 状态 | 计划时间 | 实际完成 |
| --- | --- | --- | --- | --- | --- |
| M1-REQ-00034 | TASK-REQ-00034-00001 ~ 00010(10 任务,29 个文件) | 10 任务开发=已完成 ∧ 测试=不适用;净变化约 -600 ~ -800 行;INV-1 ~ INV-12 全部严守;AC-1 ~ AC-14 全过 | 待开始 | 2026-06-15 | — |

## 6. 状态管理规则

- **开发状态**:初值 = `待开始`;`code-it` 完成后 → `已完成`
- **测试状态**:初值 = `不适用`(沿用 REQ-00031 FR-3 收窄,本设计是元技能改造,无单元测试)
- **不**重写已分配的任务编号
- **不**修改已完成任务的描述或状态(只能追加"修改类"任务)

## 7. 关联计划

| 计划 | 关联点 |
| --- | --- |
| REQ-00031 | "外移单元测试"+"任务粒度收窄"(5 任务已落地)— **前置依赖** |
| REQ-00009 | `code-unit` 守卫 7 项 — **强继承** |
| BUG-00001 | 5 技能加"不修改 SKILL.md"硬约束 — **兼容性** |
| REQ-00026 | SKILL.md 描述通用化扫除 — 最小化变更原则 |
| REQ-00030 | 元技能改 + 12 维度评审 + INV 字节级保留 — 沿用 INV-1 ~ INV-12 |
| REQ-00032 | `code-require` 屏显契约 |
| REQ-00033 | `code-require` 不涉及技术选型 |
| REQ-00020 | 元技能改首条需求 |

## 8. 变更记录

| 时间 | 变更类型 | 变更摘要 | 关联项 |
| --- | --- | --- | --- |
| 2026-06-15 14:00 | 计划新增 | REQ-00034 详细设计与编码计划完成(共 10 任务,候选 14 合并;5 SKILL.md 改造 + 2 JSON 字面 + 4 README 字面 + 7 规范字面 + 11 描述段字面 + 1 目录删除;净变化约 -600 ~ -800 行) | REQ-00034 |
