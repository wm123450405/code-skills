# 缺陷详情 — BUG-00001

- 缺陷编号:BUG-00001
- 缺陷标题:code-require/code-design/code-plan/code-fix 不能实际修改代码(职责混淆)
- 严重度:**P0**(架构职责分离违反,影响主流程"谁可以改代码"的核心契约)
- 状态:**修复编码中**(本轮 code-it 实施 TASK-BUG-00001-00001,从"修复规划中"推进)
- 报告人:wangmiao
- 报告时间:2026-06-06 22:41
- 当前负责人:wangmiao
- 所属版本:V0.0.3
- 关联技能:`code-require` / `code-design` / `code-plan` / `code-fix` / `code-it` / `code-unit`

---

## 1. 缺陷描述

### 1.1 用户原始报告(2026-06-06 22:41)

> 当前 `/code-require` 技能执行时就已经对代码进行实际的修改了,这是错误的,`/code-require`、`/code-design`、`/code-plan`、`/code-fix` 这些技能不能实际修改代码,只能分析需求和缺陷、安排开发方案和计划,只有 `/code-it` 可以修改实际的工程代码,`/code-unit` 可以编写实际的单元测试。

### 1.2 期望行为

按 `CLAUDE.md` 与本仓库工作流约定,主流程管道应严格分离"分析 / 计划 / 实施"三种职责:

| 技能 | 职责 | 可修改的目录 |
| --- | --- | --- |
| `code-require` | 需求分析 | `./assistants/<version>/require/<REQ>/` 下的文档 + 看板"需求清单"区段 |
| `code-design` | 概要设计 | `./assistants/<version>/design/<REQ>/` 下的文档 + 看板"概要设计清单"区段 |
| `code-plan` | 详细设计 + 任务计划 | `./assistants/<version>/plan/<REQ>/` 下的文档 + 看板"详细设计与任务计划汇总"区段 |
| `code-fix` | 缺陷登记 + 跟踪 | `./assistants/<version>/fix/` 下的文档 + 看板"缺陷清单"区段 |
| **`code-it`** | **实施开发** | **CWD 下的项目源码**(唯一允许的生产代码改动场景) |
| `code-unit` | 单元测试 | CWD 下的测试文件 |

### 1.3 实际行为(本仓库 5 个历史 commit 违反职责分离)

`code-require` / `code-design` / `code-plan` 在历史上**实际修改了 3 个 SKILL.md**(即"工程代码"):

| 提交哈希 | 提交类型 | 修改的工程代码 | 修改行数 |
| --- | --- | --- | --- |
| `e69a58a` | `chore(code-require): REQ-00020 ...` | `code-design/SKILL.md` + `code-plan/SKILL.md` + `code-it/SKILL.md` | 12 + 131 + 74 行 |
| `6dee813` | `chore(code-require): REQ-00021 ...` | `code-design/SKILL.md` + `code-plan/SKILL.md` + `code-require/SKILL.md` | 3 SKILL.md 全部 |
| `3e1573e` | `chore(code-design): REQ-00005 ...` | `code-design/SKILL.md` | 47 行(步骤 0a + 步骤 N) |
| `e568328` | `chore(code-plan): REQ-00005 ...` | `code-plan/SKILL.md` | 47 行(步骤 0a + 步骤 N) |

**这 4 个 commit 全部"应该由 `code-it` 实施"**(本应是 `code-plan <REQ>` 拆分任务后,`code-it <TASK-...>` 实施修改 SKILL.md 的任务)。

**潜在风险**:
- **审计追溯断裂**:commit `e69a58a` 的 6 个 TASK 全部被登记为"开发=已完成",但实际它们在 `code-require` 阶段一次性提交,违反 INV-7(0 派生"更新看板"任务)和 INV-8(0 修改其他 `code-*` SKILL.md)的隐含约束(本应通过拆分任务,逐个 `code-it` 实施)
- **职责边界失守**:用户已显式报告"`code-require` ... 这些技能不能实际修改代码"
- **可观察影响**:从 git log 角度看,`code-require` 类型的 commit 含 SKILL.md 变更,使职责不可分
- **修复成本**:低(纯 SKILL.md 文档 + 流程约束;无运行时影响)

---

## 2. 涉及文件 / 模块

- `plugins/code-skills/skills/code-require/SKILL.md`(流程约束修订,不动)
- `plugins/code-skills/skills/code-design/SKILL.md`(流程约束修订,不动)
- `plugins/code-skills/skills/code-plan/SKILL.md`(流程约束修订,不动)
- `plugins/code-skills/skills/code-fix/SKILL.md`(流程约束修订,不动)
- `plugins/code-skills/skills/code-it/SKILL.md`(边界明确为"唯一可改代码")
- `plugins/code-skills/skills/code-unit/SKILL.md`(边界明确为"可改测试代码")
- `./assistants/rules/`(可能需要补充"技能职责分离"规范)

---

## 3. 根因分析

**初步假设**(本轮 2026-06-07 调查补充):
1. **历史惯例**:V0.0.1 / V0.0.2 时代,SKILL.md 改造"少而集中",`code-require` 阶段直接修改效率高,形成历史惯例
2. **流程约束弱化**:现 SKILL.md 中,`code-require` / `code-design` / `code-plan` 步骤虽提到"实施 / 编码"是 `code-it` 的事,但**没有显式的"禁止修改 CWD 项目源码"硬约束**
3. **未受审查**:本仓库历史 PR 未严格按"主流程 vs 实施"职责分离审查
4. **(本轮补充)Commit 模式特征**:4 个违规 commit(e69a58a / 6dee813 / 3e1573e / e568328)全部为 `chore(code-require):` / `chore(code-design):` / `chore(code-plan):` 前缀,**未走 `code-plan` 拆分任务 → `code-it <TASK-...>` 实施的标准链路**,即 INV-7(0 派生"更新看板"任务)的隐含约束(本应"code-require 分析 → code-plan 拆任务 → code-it 逐任务实施")未被强制
5. **(本轮补充)审计可观察性**:违规 commit 与任务清单的"开发=已完成"行**不一一对应**(如 e69a58a 一次性 commit 6 任务的工作,任务清单只能登记 1 个 commit 哈希),任务颗粒度与 commit 颗粒度失配

**根因正式定稿**(本轮 code-plan 确认):
- **主因(假设 2)**:SKILL.md 流程约束弱化 — 4 个技能"## 不要做的事"段虽有"不修改 X"等条款,但**无**"禁止修改 CWD 项目源码"的**显式硬约束**(本仓库工程代码 = `plugins/code-skills/skills/*/SKILL.md`)
- **辅助(假设 1+3)**:历史惯例 + 未受审查(本修复不追溯历史 commit)
- **辅助(假设 4)**:4 个违规 commit 全部跳过"code-plan 拆任务 → code-it 实施"标准链路,INV-7 隐含约束未被强制
- **辅助(假设 5)**:审计可观察性失配(本修复不解决此问题,只通过后续强制"code-it 实施"间接改善)

---

## 4. 修复方案

> 本节由 `code-plan BUG-00001` 产出 RESULT.md 14 章节后回写链接(本需求 REQ-00019 起,BUG 路径不生成 `fix-plan.md`,沿用 `plan/.../RESULT.md` 同构)

- **当前**:已确认 5 项修复方向,5 个任务拆分完成
- **方案 5 项**(本轮细化):
  1. SKILL.md 改造:在 `code-require` / `code-design` / `code-plan` / `code-fix` SKILL.md 中显式追加"禁止修改 CWD 项目源码"硬约束
  2. SKILL.md 改造:在 `code-it` SKILL.md 中显式追加"唯一允许的生产代码改动场景"声明
  3. SKILL.md 改造:在 `code-unit` SKILL.md 中显式追加"可改测试代码"声明
  4. 规范补充(可选):在 `./assistants/rules/` 下新增 `skill-responsibility.md`,固化"技能 → 目录映射"约束(本轮**不**实施,留作后续可能需求)
  5. 历史 commit 处理:无需回滚(`e69a58a` / `6dee813` / `3e1573e` / `e568328` 4 个 commit 的实际改造是有价值的;只是流程需约束;本缺陷修复**仅约束未来**,不追溯)

详细设计见 §7 详细设计 14 章节;任务拆分见 `PLAN.md`。

---

## 5. 修复实施

> 本节由 `code-it BUG-00001` 阶段产出 `code/TASK-BUG-00001-NNNNN/RESULT.md` 等后回写链接

- **当前**:无(`code-it` 尚未执行)
- **下一步**:调 `/code-skills:code-it BUG-00001` 实施 SKILL.md 改造(在 `code-plan` 已拆分 5 任务后,逐任务实施,本缺陷自身正是要"修复的行为模式")

---

## 6. 验证结果

> 本节由 `code-it BUG-00001` 阶段产出 `test/TASK-BUG-00001-NNNNN/RESULT.md` 后回写链接(纯文档任务,实际不生成此文件)

- **当前**:无
- **验证方式**:本仓库 0 测试框架,验证手段为**静态校验**(详 §7.12 测试要点):
  - INV-10~16 自检(7 项):grep 各 SKILL.md 关键字 + frontmatter 字节级保留
  - 回归校验:对历史 4 个 commit 的实际 SKILL.md 改造**不**回滚(那是"流程违反但功能正确")

---

## 7. 详细设计(本轮 code-plan 追加,2026-06-07)

> 本节是 code-plan 阶段的详细设计;§1~§6 是 code-fix 登记时的"缺陷上下文",保留不动。本轮不重写 §1~§6 任何字段。

### 7.1 概述

**本详细设计的目标**:把缺陷 `code-require/code-design/code-plan/code-fix 实际修改了 SKILL.md` 修复为"`code-require/design/plan/fix` 严格只写工作空间文档,`code-it` 是唯一允许修改 `plugins/code-skills/skills/*/SKILL.md` 的技能"。

**修复范围**(本轮确认):
- 6 个目标 SKILL.md:`code-require` / `code-design` / `code-plan` / `code-fix` / `code-it` / `code-unit`
- 0 个目录新增 / 0 个文件新增 / 0 个文件删除
- 0 个依赖新增 / 0 个字段新增 / 0 触发 `dashboard-conventions §规则 1` 三同步
- 0 触发 `code-rule`(新增 `rules/skill-responsibility.md` **不**在本轮修复范围,留作后续可能的需求)

**与概要设计的关系**:本缺陷没有走 `code-design` 阶段;§4 即"概要设计草案",本详细设计将其从"5 项方向"细化为"5 个任务的精确锚点"。

### 7.2 上游引用

| 来源 | 路径 | 提取内容 |
| --- | --- | --- |
| 缺陷详情 | `fix/BUG-00001/RESULT.md §1-§6` | 缺陷描述 / 涉及文件 / 5 条根因 / 5 项修复方向 / 验证方式 |
| 项目级规范 | `./assistants/rules/*.md` × 13 | 强约束:`skill-conventions §规则 1` / `encoding-conventions §规则 1-4` / `dashboard-conventions §规则 1`;其余 10 份对本修复**不**产生约束(占位待填或 0 触发) |
| 历史违规 commit | `e69a58a` / `6dee813` / `3e1573e` / `e568328` | 4 个 commit 模式特征(根因假设 4) — **不**回滚,仅作修复依据 |

### 7.3 规范遵循(13 份规范自检)

| 规范 | 触发? | 结论 |
| --- | --- | --- |
| `skill-conventions.md §规则 1` | ✅ 强 | SKILL.md frontmatter(`name` + `description`)字节级保留 — INV 严守 |
| `module-conventions.md` | ❌ | DEPRECATED,本修复不引用 |
| `directory-conventions.md` | ❌ | 占位待填,本修复不触发 |
| `encoding-conventions.md §规则 1-4` | ✅ 强 | BUG 任务编号 5+5 位嵌套式 `TASK-BUG-00001-NNNNN` |
| `dashboard-conventions.md §规则 1` | ❌ | 0 字段扩展,0 三同步 |
| `doc-conventions.md §规则 1-2` | ❌ | 本修复不涉及 README |
| `coding-style.md` | ❌ | 占位,SKILL.md 是自然语言不涉及代码风格 |
| `commit-conventions.md` | ⚠️ 软 | 本修复产物为 6 段 SKILL.md 文本追加,commit message 沿用 `chore(code-it): BUG-00001 ...` |
| `dependency-conventions.md` | ❌ | 0 新依赖 |
| `framework-conventions.md` | ❌ | 0 架构变更 |
| `naming-conventions.md` | ❌ | 0 新增命名实体 |
| `migration-mapping.md` | ❌ | 0 编码重命名 |
| `marketplace-protocol.md` | ❌ | 0 JSON 字段变更 |

**自检结论**:0 违反强约束,2 项软约束已通过(frontmatter 保留 + 任务编号新格式),0 需 `code-rule` 介入。

### 7.4 模块详细化(6 个 SKILL.md 各加 1 段)

> 沿用"修改文件定位的语义化约定" — 每段追加用语义化锚点,不写行号。

#### 7.4.1 `code-require/SKILL.md`

- **追加位置**:`## 不要做的事` 段,作为新条目插在该段**最前面**(在 NFR-7 的"不调用 Write/Edit"条目之前)
- **追加内容**(原文,约 80 字符):
  > 不修改 `plugins/code-skills/skills/*/SKILL.md` 任何文件(工程代码改动由 `code-it` 实施,本技能只写 `require/<REQ>/RESULT.md` 等工作空间文档)
- **影响范围**:0 个下游任务(本段追加不触发其他技能改动)
- **触发来源**:BUG-00001 §4 方向 1

#### 7.4.2 `code-design/SKILL.md`

- **追加位置**:`## 不要做的事` 段,作为新条目插在该段**最前面**
- **追加内容**(原文):
  > 不修改 `plugins/code-skills/skills/*/SKILL.md` 任何文件(工程代码改动由 `code-it` 实施,本技能只写 `design/<REQ>/RESULT.md` 等工作空间文档)
- **影响范围**:0 个下游任务
- **触发来源**:BUG-00001 §4 方向 1

#### 7.4.3 `code-plan/SKILL.md`

- **追加位置**:`## 不要做的事` 段,作为新条目插在该段**最前面**
- **追加内容**(原文):
  > 不修改 `plugins/code-skills/skills/*/SKILL.md` 任何文件(工程代码改动由 `code-it` 实施,本技能只写 `plan/<REQ>/RESULT.md` / `PLAN.md` 等工作空间文档)
- **影响范围**:0 个下游任务
- **触发来源**:BUG-00001 §4 方向 1

#### 7.4.4 `code-fix/SKILL.md`

- **追加位置**:`## 不要做的事` 段,作为新条目插在该段**最前面**
- **追加内容**(原文):
  > 不修改 `plugins/code-skills/skills/*/SKILL.md` 任何文件(工程代码改动由 `code-it` 实施,本技能只写 `fix/<BUG-NNN>/RESULT.md` 等工作空间文档)
- **影响范围**:0 个下游任务
- **触发来源**:BUG-00001 §4 方向 1

#### 7.4.5 `code-it/SKILL.md`

- **追加位置**:在 `## 目标` 段后**新增** `## 唯一允许的生产代码改动场景` 小节(锚点:§目标 段)
- **追加内容**(原文,约 150 字符):
  > 本技能是 `code-skills` 体系中**唯一**被允许修改 `plugins/code-skills/skills/*/SKILL.md` 的技能。`code-require` / `code-design` / `code-plan` / `code-fix` 不得修改这些工程代码;`code-unit` 不得修改生产代码(只能写测试代码)。本技能读 `<版本号>/code/<TASK-...>/` 工作空间文档与 `plan/<REQ>/PLAN.md` 任务清单,逐任务产出 `code/<TASK-...>/RESULT.md` 实施记录。
- **影响范围**:0 个下游任务(纯声明)
- **触发来源**:BUG-00001 §4 方向 2

#### 7.4.6 `code-unit/SKILL.md`

- **追加位置**:在 `## 目标` 段后**新增** `## 可改测试代码边界` 小节(锚点:§目标 段)
- **追加内容**(原文,约 130 字符):
  > 本技能被允许**仅**修改 CWD 下的测试文件(如 `tests/` / `__tests__/` / `*.test.*` / `*.spec.*`)。**不得**修改 `plugins/code-skills/skills/*/SKILL.md` 或其他生产代码文件;生产代码改动由 `code-it` 唯一实施。本技能产出 `test/<TASK-...>/RESULT.md` 测试记录。
- **影响范围**:0 个下游任务(纯声明)
- **触发来源**:BUG-00001 §4 方向 3

### 7.5 算法与逻辑

本修复**不**涉及算法或运行时逻辑;**不**涉及数据结构、接口、状态机变更。详见 §7.4 各 SKILL.md 追加内容(纯文档静态文本,无函数/方法新增)。

### 7.6 数据结构

**0 变更**。本修复不新增 / 修改 / 删除任何数据结构。

### 7.7 接口细节

**0 变更**。本修复不新增 / 修改 / 删除任何接口。

### 7.8 异常处理

**0 运行时异常路径**(纯文档修复)。code-it 实施时若发现"目标锚点(段标题)已变更"或"该段被删除",应通过 `code-fix BUG-00001` 走派生任务,而不是直接重写 6 段文本。

### 7.9 安全

**0 安全影响**。本修复仅追加 6 段 SKILL.md 文本,无权限/凭据/输入校验变化。

### 7.10 状态机

**0 状态机变更**。

### 7.11 性能

**0 性能影响**(纯文本追加,文档长度变化 < 1 KB / 6 文件)。

### 7.12 测试要点

本仓库 0 测试框架,验证手段为**静态校验**(详 §6 验证结果):

| 校验项 | 命令 | 通过条件 |
| --- | --- | --- |
| INV-10:`code-require` 含"不修改 SKILL.md"硬约束 | `grep -n "不修改.*SKILL.md" plugins/code-skills/skills/code-require/SKILL.md` | 命中 ≥ 1 行 |
| INV-11:`code-design` 含"不修改 SKILL.md"硬约束 | 同上,目标 `code-design` | 命中 ≥ 1 行 |
| INV-12:`code-plan` 含"不修改 SKILL.md"硬约束 | 同上,目标 `code-plan` | 命中 ≥ 1 行 |
| INV-13:`code-fix` 含"不修改 SKILL.md"硬约束 | 同上,目标 `code-fix` | 命中 ≥ 1 行 |
| INV-14:`code-it` 含"唯一允许的生产代码改动"声明 | `grep -n "唯一.*生产代码改动" plugins/code-skills/skills/code-it/SKILL.md` | 命中 ≥ 1 行 |
| INV-15:`code-unit` 含"可改测试代码边界"声明 | `grep -n "可改测试代码" plugins/code-skills/skills/code-unit/SKILL.md` | 命中 ≥ 1 行 |
| INV-16:6 个 SKILL.md 的 frontmatter 字节级保留 | `git diff plugins/code-skills/skills/{code-require,code-design,code-plan,code-fix,code-it,code-unit}/SKILL.md` 头部 3 行 | 仅"## 不要做的事" / "## 目标" 段后有 diff,frontmatter 0 diff |
| 回归校验 | `git log --oneline \| head -10` | e69a58a / 6dee813 / 3e1573e / e568328 4 个 commit 仍存在(**不**回滚) |

**验收清单**(code-check 阶段):7 项 INV 全部通过 + 1 项回归校验通过 → 缺陷可关闭。

### 7.13 关联

| 关联项 | 关联方式 |
| --- | --- |
| `CLAUDE.md §版本感知工作空间约定` | 上游权威源(定义 `code-*` 技能 → 工作空间目录映射) |
| `plugins/code-skills/skills/code-fix/SKILL.md §工作目录约定` | 缺陷路径工作空间约定(本修复同构) |
| `plugins/code-skills/skills/code-it/SKILL.md §目标` | 唯一可改代码边界声明的"反向引用源" |
| `plugins/code-skills/skills/code-unit/SKILL.md §目标` | 可改测试代码边界声明的"反向引用源" |
| `plugins/code-skills/CLAUDE.md` "## 如何编写技能" 段 | 技能编写的整体规范(本修复不触发三同步) |
| V0.0.3 RESULT.md §缺陷清单 | 本修复完成后由 code-check 同步更新 BUG-00001 状态 |

### 7.14 待澄清 / 未决项

| 编号 | 问题 | 默认决策(本轮锁定) | 后续触发条件 |
| --- | --- | --- | --- |
| Q-1 | 是否新增 `rules/skill-responsibility.md` 规范文件固化"技能 → 目录映射"约束?(§4 方向 4) | **否**(本轮 0 触发 `code-rule`,避免修复范围蔓延) | 未来若第 2 次出现"职责混淆"问题 → 调 `code-rule` 加规范 |
| Q-2 | 是否回滚 4 个历史违规 commit(e69a58a 等)? | **否**(本轮修复仅约束未来,沿用 §3 "修复成本:低,无运行时影响"判定) | 永不回滚(沿用既有 `migration-mapping §规则 4` "不追溯重命名"精神) |
| Q-3 | 6 个 SKILL.md 的硬约束文案是否要"完全统一"措辞? | **否**(每段文案略不同,因各技能后续流程描述略异;统一为"不修改 SKILL.md" 短句即可) | 后续若发现"自由裁量"导致不一致 → 调 `code-rule` 加 `skill-responsibility.md` 锁定模板 |
| Q-4 | 是否在 `code-fix/SKILL.md` 中加"修复流程示例 1 个"演示 `from REQ-NNNNN` / `from BUG-NNNNN` 双模式? | **否**(本轮修复不涉及,沿用既有) | 未来若有 `code-fix` 重构需求再追加 |

---

## 8. 修复日志

| 时间 | 操作 | 摘要 |
| --- | --- | --- |
| 2026-06-06 22:41 | 登记 | wangmiao 报告缺陷:code-require/code-design/code-plan/code-fix 不能实际修改代码(职责混淆) |
| 2026-06-07 | 状态推进 | 状态"报告"→"调查中":补充根因假设 4 / 5(commit 模式特征 + 审计可观察性);确认涉及文件 = `code-require` / `code-design` / `code-plan` / `code-fix` / `code-it` / `code-unit` 6 个 SKILL.md + `./assistants/rules/`(可选新增 skill-responsibility.md);确认根因正式定稿留待 `code-plan BUG-00001` 阶段 |
| 2026-06-07 | 修复规划 | code-plan 完成详细设计 + 5 任务拆分(RESULT.md 14 章节 + PLAN.md 任务总览 + 7 份过程文档);状态推进"调查中"→"修复规划中";5 任务全部为纯文档型(测试状态=不适用) |
| 2026-06-07 | 修复开始 | code-it 开始实施 TASK-BUG-00001-00001(`code-require` 加硬约束);状态推进"修复规划中"→"修复编码中" |

---

## 9. 变更记录

| 时间 | 变更类型 | 变更摘要 | 关联项 |
| --- | --- | --- | --- |
| 2026-06-06 22:41 | 缺陷登记 | code-fix 创建缺陷 BUG-00001(严重度 P0,状态 报告) | BUG-00001 |
| 2026-06-07 | 状态推进 | BUG-00001 状态"报告"→"调查中"(补充根因假设 4/5,确认根因正式定稿留待 code-plan) | BUG-00001 |
| 2026-06-07 | 计划完成 | code-plan 完成 BUG-00001 详细设计 + 5 个任务拆分(整体=--balanced, 可维护性=高, 封装性/可读性=不适用);产出 9 份文档(RESULT.md / PLAN.md / 7 份过程文档) | BUG-00001 |
| 2026-06-07 | 状态推进 | BUG-00001 状态"修复规划中"→"修复编码中"(code-it 开始实施 TASK-BUG-00001-00001) | BUG-00001 |
