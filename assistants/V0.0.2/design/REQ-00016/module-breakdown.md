# 模块拆分 — REQ-00016
更新时间:2026-06-05 16:10
版本:V0.0.2
需求编码:REQ-00016
设计标题:`code-design` / `code-plan` 增加"快模式"+ 末尾提交无需确认

---

## 1. 拆分总览

| 类别 | 数量 | 模块数 | 字节级修改 |
| --- | --- | --- | --- |
| **新增** | 0 个 | — | — |
| **修改既有** | 2 个 | 2 | `plugins/code-skills/skills/code-design/SKILL.md` + `plugins/code-skills/skills/code-plan/SKILL.md`(各自增量追加"步骤 0.5 模式选择" + 快模式分支 + 末尾兜底 3 选 1 跳过条件) |
| **复用既有** | 5 个 | 5 | (不修改,运行时引用) |
| **总计** | 7 个 | 7 | 2 个修改 + 0 个新增 + 5 个复用 |

> 本设计严格遵循 FR-5(完整模式字节级不变)+ FR-6(0 修改其他 9 个 `code-*`)+ NFR-6(0 修改 marketplace.json / plugin.json / rules/)

---

## 2. 模块清单

### 2.1 修改既有模块

#### M-1:`plugins/code-skills/skills/code-design/SKILL.md`

| 字段 | 值 |
| --- | --- |
| 状态 | **修改既有** |
| 职责 | 既有 `code-design` 技能入口 — 完整模式(15 步骤 + 7 过程文档) + 快模式(跳过 4 步骤 + 仅 3 过程文档 + 末尾跳过 3 选 1) |
| 对外暴露的接口 | (SKILL.md 入口,无 API;由 Claude Code 平台解析) |
| 依赖(对内其他模块) | 既有 `templates/design.md` / `templates/assistants-layout.md` |
| 依赖(对外三方) | 0 |
| 关键决策 | **增量追加**(DQ-1.E),**不**重写既有章节;frontmatter **不**变 |
| 涉及修改范围 | 在既有"步骤 0 版本上下文检测"节末尾 + 空行 + 追加"### 步骤 0.5 模式选择";在既有"步骤 7A-15A"中各步骤的条件分支(快模式跳过 / 完整模式执行)用 `if (mode == FAST)` 包裹(由代码分支而非字面替换);在既有"步骤 N 末尾兜底提交"中步骤 4 之前增加"步骤 3.5 模式分支"(快模式跳过步骤 4 / 完整模式执行步骤 4) |
| 字节级修改原则 | Edit 工具严格按锚点;**不**改 frontmatter;**不**改既有 1-15 步骤的字面;**不**删任何既有章节;**不**改既有 `## 目标` / `## 适用场景` / `## 不适用` / `## 工作目录约定` / `## 输入` / `## 输出` / `## 工具使用约定` / `## 模板格式` 字面 |

#### 关键决策的规范依据

| 决策 | 依据 |
| --- | --- |
| 增量追加 vs 整体重写 | `skill-conventions §规则 1`(frontmatter 不变)+ FR-5.AC-5.1 / AC-5.4 / AC-5.5 + INV-1 / INV-4 / INV-5 |
| 不在 `code-design/` 下新增子目录 | `module-conventions §规则 1`(本设计**不**新增资源,只改 SKILL.md 正文) |
| 不在 SKILL.md 嵌入具体 git / bash 命令模板 | NFR 沿用 V0.0.2 既有 11 个 `code-*` SKILL.md 风格(描述工作流而非命令) |
| frontmatter 字节级不变 | `skill-conventions §规则 1` + FR-5.AC-5.4 + INV-4 |
| 末尾兜底 3 选 1 跳过条件(快模式) | FR-4 + NFR-2 + NFR-7 + 用户原文"提交过程无需用户确认,直接提交" |

#### 自检结果(对照 `module-conventions §规则 1`)

- ✅ 命名:技能目录名 `code-design` 与既有 SKILL.md frontmatter `name: code-design` 一致
- ✅ 目录位置:技能根目录 + 既有 2 子目录(`templates/`)与既有对齐
- ✅ 依赖方向:本设计不引入新模块依赖;既有依赖(`templates/design.md` 等)字节级不变
- ✅ 被禁止的模式:无(无循环依赖 / 无新模块根目录散落 / 无违反固定子目录约束)

---

#### M-2:`plugins/code-skills/skills/code-plan/SKILL.md`

| 字段 | 值 |
| --- | --- |
| 状态 | **修改既有** |
| 职责 | 既有 `code-plan` 技能入口 — 完整模式(18 步骤 + 8 过程文档) + 快模式(跳过 5 步骤 + 仅 4 过程文档 + 末尾跳过 3 选 1) |
| 对外暴露的接口 | (SKILL.md 入口) |
| 依赖(对内其他模块) | 既有 `templates/plan.md` / `templates/task-plan.md` / `templates/assistants-layout.md` |
| 依赖(对外三方) | 0 |
| 关键决策 | **增量追加**,**不**重写既有章节;frontmatter **不**变 |
| 涉及修改范围 | 同 M-1,但锚点不同(在 `code-plan` SKILL.md 步骤 0 后插入"步骤 0.5 模式选择";在快模式分支跳 7A-8A + 12A-13A + 14A/15A 仅核心 + 16A 仅 1 行;末尾兜底 3 选 1 跳过条件) |
| 字节级修改原则 | 同 M-1(本设计**不**改 frontmatter / **不**改既有 1-18 步骤字面 / **不**改既有 5 章节字面) |

#### 自检结果(对照 `module-conventions §规则 1`)

- ✅ 命名:技能目录名 `code-plan` 与既有 SKILL.md frontmatter `name: code-plan` 一致
- ✅ 目录位置:技能根目录 + 既有 3 子目录(`templates/`)与既有对齐
- ✅ 依赖方向:本设计不引入新模块依赖
- ✅ 被禁止的模式:无

---

### 2.2 复用既有模块(运行时引用,**不**修改)

#### M-3:`plugins/code-skills/skills/code-design/templates/design.md`

| 字段 | 值 |
| --- | --- |
| 状态 | **复用既有** |
| 职责 | 完整模式 RESULT.md 章节结构(14 章节)模板 |
| 快模式用法 | 快模式**不**使用本模板(快模式 RESULT.md 仅 4 章节,直接 Write 字面) |
| 完整模式用法 | 完整模式**完全复用**本模板 |
| 字节级修改 | **不修改**(0 字节变更) |

#### M-4:`plugins/code-skills/skills/code-design/templates/assistants-layout.md`

| 字段 | 值 |
| --- | --- |
| 状态 | **复用既有** |
| 职责 | 目录布局参考 |
| 快模式 + 完整模式用法 | 两者都**完全复用** |
| 字节级修改 | **不修改** |

#### M-5:`plugins/code-skills/skills/code-plan/templates/plan.md`

| 字段 | 值 |
| --- | --- |
| 状态 | **复用既有** |
| 职责 | 完整模式 plan/RESULT.md 章节结构(14 章节)模板 |
| 快模式用法 | 快模式**不**使用本模板(快模式 RESULT.md 仅 4 章节) |
| 完整模式用法 | 完整模式**完全复用** |
| 字节级修改 | **不修改** |

#### M-6:`plugins/code-skills/skills/code-plan/templates/task-plan.md`

| 字段 | 值 |
| --- | --- |
| 状态 | **复用既有** |
| 职责 | 完整模式 PLAN.md 章节结构(8 章节)模板 |
| 快模式用法 | 快模式**不**使用本模板(快模式 PLAN.md 仅 5 章节) |
| 完整模式用法 | 完整模式**完全复用** |
| 字节级修改 | **不修改** |

#### M-7:`assistants/V0.0.2/RESULT.md`(主看板)

| 字段 | 值 |
| --- | --- |
| 状态 | **复用既有**(只读 + 写) |
| 职责 | "概要设计清单" / "详细设计与任务计划汇总" / "任务清单" / "里程碑" 区段 |
| 快模式用法 | 步骤 14A / 16A 同步 — 写 1 行(带"-快模式"后缀)到"概要设计清单"或"详细设计与任务计划汇总";**不**写"变更记录";**不**更新"最近更新"时间戳 |
| 完整模式用法 | 步骤 14A / 16A 同步 — 既有行为**完全不变** |
| 字节级修改 | 快模式**写** 1 行 + 时间戳 0 修改;完整模式**写**多行 + 时间戳更新 |

---

## 3. 物理文件路径清单(本设计会触碰的)

| 路径 | 修改类型 | 修改字节 | 触发/来源 |
| --- | --- | --- | --- |
| `plugins/code-skills/skills/code-design/SKILL.md` | Edit 增量追加 | +N 行(预计 +80 ~ +150 行,含"步骤 0.5 模式选择" + 快模式分支 + 末尾兜底 3 选 1 跳过条件) | 需求新增 |
| `plugins/code-skills/skills/code-plan/SKILL.md` | Edit 增量追加 | +N 行(预计 +100 ~ +180 行,含"步骤 0.5 模式选择" + 快模式分支 + 末尾兜底 3 选 1 跳过条件) | 需求新增 |
| `assistants/V0.0.2/RESULT.md` | 0(本设计阶段) | 0(本设计阶段) | (留 `code-plan` 阶段由 T-003 写) |

> 注:本设计阶段**不**触碰 `RESULT.md` — 看板同步在 `code-plan` 阶段由独立的"文档"任务(T-003 预估)完成。本设计阶段结束时,看板"概要设计清单"由 `code-design` 步骤 14A 追加 1 行。

---

## 4. 不修改的文件清单(本设计 0 触碰)

| 路径 | 原因 |
| --- | --- |
| `.claude-plugin/marketplace.json` | FR-6.AC-6.2 + `marketplace-protocol §规则 1` |
| `plugins/code-skills/.claude-plugin/plugin.json` | 同上 |
| 其他 9 个 `code-*/SKILL.md`(`code-init` / `code-version` / `code-rule` / `code-require` / `code-it` / `code-unit` / `code-fix` / `code-publish` / `code-auto` / `code-dashboard` / `code-review`) | FR-6.AC-6.1 + NFR-4 + NFR-5 |
| `assistants/rules/` 下 13 个规范文件 | NFR-6 |
| `plugins/code-skills/README.md` + `README.en.md` | NFR-6 |
| `plugins/code-skills/CLAUDE.md` | NFR-6 |
| `code-design/SKILL.md` frontmatter | FR-5.AC-5.4 + `skill-conventions §规则 1` + INV-4 |
| 既有 `code-design/SKILL.md` 步骤 0-15 字面 | FR-5.AC-5.5 + INV-1 + INV-5 |
| 既有 `code-design/templates/{design,assistants-layout}.md` | INV-2 |
| 既有 `code-plan/SKILL.md` 步骤 0-18 字面 | FR-5.AC-5.5 + INV-1 + INV-5 |
| 既有 `code-plan/templates/{plan,task-plan,fix-plan,assistants-layout}.md` | INV-2 |

---

## 5. 模块拆分自检结论

- ✅ 命名合规:`code-design` / `code-plan` 目录 + frontmatter name 一致;既有不变
- ✅ 目录位置合规:`code-design/` / `code-plan/` 下既有 2-3 固定子目录不变(`module-conventions §规则 1`)
- ✅ 依赖方向合规:无循环依赖;既有模板沿用
- ✅ 字节级修改边界:2 个修改(M-1 + M-2)+ 0 个新增 + 5 个复用 = 7 个模块
- ✅ 100% 合规(`rule-compliance.md` 详)
- ✅ 0 风险 vs 既有规范
