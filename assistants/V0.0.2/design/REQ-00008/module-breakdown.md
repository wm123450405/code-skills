# 模块拆分 — REQ-00008
更新时间:2026-06-05 15:55
版本:V0.0.2
需求编码:REQ-00008
设计标题:`/code-review` 整版本模式(无参评审)

---

## 1. 拆分总览

| 类别 | 数量 | 模块数 | 字节级修改 |
| --- | --- | --- | --- |
| **新增** | 0 个 | — | — |
| **修改既有** | 1 个 | 1 | `plugins/code-skills/skills/code-review/SKILL.md`(增量追加"步骤 1.5 模式选择" + "步骤 2 整版本模式" 章节) |
| **复用既有** | 4 个 | 4 | (不修改,运行时引用) |
| **总计** | 5 个 | 5 | 1 个修改 + 0 个新增 + 4 个复用 |

> 本设计严格遵循 NFR-2(增量修改 SKILL.md)+ FR-8.AC-8.1(0 修改其他 9 个 `code-*`)+ FR-8.AC-8.3(0 修改 `assistants/rules/`)

---

## 2. 模块清单

### 2.1 修改既有模块

#### M-1:`plugins/code-skills/skills/code-review/SKILL.md`

| 字段 | 值 |
| --- | --- |
| 状态 | **修改既有** |
| 职责 | 既有 `code-review` 技能入口 — 模式 1(单需求评审)+ 模式 2(整版本评审)双模式 |
| 对外暴露的接口 | (SKILL.md 入口,无 API;由 Claude Code 平台解析) |
| 依赖(对内其他模块) | 既有 `templates/REVIEW-REPORT.md` / `templates/REVIEW-FIX.md` / `checklists/review-checklist.md` |
| 依赖(对外三方) | 0 |
| 关键决策 | **增量追加**(DQ-1.B),**不**重写既有章节;frontmatter **不**变 |
| 涉及修改范围 | 在既有"步骤 1 解析参数"后插入"步骤 1.5 模式选择" + 新增"步骤 2 整版本模式" + 在"步骤 N — 末尾兜底提交"前插入"步骤 N-1 整版本模式 附加流程" |
| 字节级修改原则 | Edit 工具严格按锚点;**不**改 frontmatter;**不**改既有 1-15 步骤的字面;**不**删任何既有章节;**不**改既有 `## 目标` / `## 适用场景` / `## 不适用` / `## 工作目录约定` / `## 输入` / `## 输出` / `## 工具使用约定` / `## 评审维度速查` / `## 过程文档格式` / `## 衔接` / `## 不要做的事` 字面 |

#### 关键决策的规范依据

| 决策 | 依据 |
| --- | --- |
| 增量追加 vs 整体重写 | `skill-conventions §规则 1`(frontmatter 不变)+ FR-7.AC-7.2 + FR-7.AC-7.4 + NFR-2 |
| 不在 `code-review/` 下新增子目录 | `module-conventions §规则 1`(本设计**不**新增资源,只改 SKILL.md 正文) |
| 不在 SKILL.md 嵌入具体 git / bash 命令模板 | NFR-9 沿用 V0.0.2 既有 11 个 `code-*` SKILL.md 风格(描述工作流而非命令) |
| frontmatter 字节级不变 | `skill-conventions §规则 1` + FR-7.AC-7.2 |

#### 自检结果(对照 `module-conventions §规则 1`)

- ✅ 命名:技能目录名 `code-review` 与既有 SKILL.md frontmatter `name: code-review` 一致
- ✅ 目录位置:技能根目录 + 既有 3 子目录(templates/ + checklists/ + assistants-layout.md 在 templates/)与既有对齐
- ✅ 依赖方向:本设计不引入新模块依赖;既有依赖(`templates/REVIEW-REPORT.md` 等)字节级不变
- ✅ 被禁止的模式:无(无循环依赖 / 无新模块根目录散落 / 无违反固定子目录约束)

---

### 2.2 复用既有模块(运行时引用,**不**修改)

#### M-2:`plugins/code-skills/skills/code-review/templates/REVIEW-REPORT.md`

| 字段 | 值 |
| --- | --- |
| 状态 | **复用既有** |
| 职责 | 模式 1 整体评审报告模板(8 章节) |
| 整版本模式用法 | 整版本模式对每个被评审需求生成 1 份 `REVIEW-REPORT.md`,**完全复用**此模板(FR-3.AC-3.1 + FR-6.AC-6.1 强约束) |
| 字节级修改 | **不修改**(0 字节变更) |

#### M-3:`plugins/code-skills/skills/code-review/templates/REVIEW-FIX.md`

| 字段 | 值 |
| --- | --- |
| 状态 | **复用既有** |
| 职责 | 派生改修要求模板(给 `code-it` 消费) |
| 整版本模式用法 | 整版本模式的派生任务**完全复用**此模板 |
| 字节级修改 | **不修改** |

#### M-4:`plugins/code-skills/skills/code-review/checklists/review-checklist.md`

| 字段 | 值 |
| --- | --- |
| 状态 | **复用既有** |
| 职责 | 内置评审清单(9 维度 + 评审结论判定) |
| 整版本模式用法 | 整版本模式对每个被评审需求逐项应用此清单(步骤 7 加载清单) |
| 字节级修改 | **不修改** |

#### M-5:`assistants/V0.0.2/RESULT.md`(主看板)

| 字段 | 值 |
| --- | --- |
| 状态 | **复用既有**(只读数据源) |
| 职责 | 需求清单(整版本模式过滤"已完成"需求的数据源) |
| 整版本模式用法 | 步骤 1.5 模式选择后,步骤 2 过滤"已完成"需求 — Grep `^## 需求清单` + 解析 `^\| REQ-\d{5} \|` 行 |
| 字节级修改 | **不修改**(整版本模式只读;`code-review` 模式 1 既有同步逻辑覆盖所有看板区段) |

---

## 3. 物理文件路径清单(本设计会触碰的)

| 路径 | 修改类型 | 修改字节 | 触发/来源 |
| --- | --- | --- | --- |
| `plugins/code-skills/skills/code-review/SKILL.md` | Edit 增量追加 | +N 行(预计 +60 ~ +120 行,含模式选择 + 整版本模式 8 步骤 + 附加流程) | 需求新增 |
| `plugins/code-skills/skills/code-review/templates/REVIEW-REPORT.md` | 0 | 0 | 复用 |
| `plugins/code-skills/skills/code-review/templates/REVIEW-FIX.md` | 0 | 0 | 复用 |
| `plugins/code-skills/skills/code-review/checklists/review-checklist.md` | 0 | 0 | 复用 |
| `assistants/V0.0.2/RESULT.md`(本设计阶段**不**写;`code-plan` 阶段由 T-003 文档任务写) | 0(本设计阶段) | 0(本设计阶段) | (留 `code-plan` 阶段) |

> 注:本设计阶段**不**触碰 `RESULT.md` — 看板同步在 `code-plan` 阶段由独立的"文档"任务(T-003 预估)完成。本设计阶段结束时,看板"概要设计清单"由 `code-design` 步骤 14A 追加 1 行。

---

## 4. 不修改的文件清单(本设计 0 触碰)

| 路径 | 原因 |
| --- | --- |
| `.claude-plugin/marketplace.json` | FR-8.AC-8.1 + `marketplace-protocol §规则 1` |
| `plugins/code-skills/.claude-plugin/plugin.json` | 同上 |
| 其他 9 个 `code-*/SKILL.md`(`code-init` / `code-version` / `code-rule` / `code-require` / `code-design` / `code-plan` / `code-it` / `code-unit` / `code-fix` / `code-publish` / `code-auto` / `code-dashboard`) | FR-8.AC-8.2 |
| `assistants/rules/` 下 13 个规范文件 | FR-8.AC-8.3 |
| `plugins/code-skills/README.md` + `README.en.md` | FR-8.AC-8.4 + `doc-conventions §规则 1` (Q-7 采纳默认不主动写) |
| `plugins/code-skills/CLAUDE.md` | Q-7 采纳默认(留作 `code-rule` 沉淀) |
| `code-review/SKILL.md` frontmatter | FR-7.AC-7.2 + `skill-conventions §规则 1` |
| 既有 `code-review/SKILL.md` 步骤 0-15 字面 | FR-7.AC-7.4 + NFR-2 |

---

## 5. 模块拆分自检结论

- ✅ 命名合规:`code-review` 目录 + frontmatter name 一致;既有不变
- ✅ 目录位置合规:`code-review/` 下既有 3 固定子目录不变(`module-conventions §规则 1`)
- ✅ 依赖方向合规:无循环依赖;既有 3 模板 + 1 清单沿用
- ✅ 字节级修改边界:1 个修改(SKILL.md 增量追加) + 0 个新增 + 4 个复用 = 5 个模块
- ✅ 100% 合规(`rule-compliance.md` 详)
- ✅ 0 风险 vs 既有规范
