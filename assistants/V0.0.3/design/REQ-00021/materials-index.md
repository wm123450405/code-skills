# 材料登记 — REQ-00021
更新时间:2026-06-06 17:45
版本:V0.0.3

## 项目级规范(本次扫描)

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| skill-conventions.md | 技能规范 | §规则 1:frontmatter `name` 字节级保留 |
| dashboard-conventions.md | 看板规范 | §规则 1:三同步(本需求 0 触发) |
| encoding-conventions.md | 编号规范 | §规则 1/3:5+5 位嵌套式(本需求 0 触发) |
| marketplace-protocol.md | 市场协议 | 0 改 marketplace/plugin |
| module-conventions.md(DEPRECATED) | 模块规范 | §规则 1:过程文档摆放 |
| commit-conventions.md | 提交规范 | chore(<scope>) 格式 |
| doc-conventions.md | 文档规范 | 中英 README 同步 |
| naming-conventions.md | 命名规范 | 0 新增文件名前缀 |
| dependency-conventions.md | 依赖规范 | 0 新增依赖 |
| directory-conventions.md | 目录规范 | 子目录命名 |
| framework-conventions.md | 框架规范 | (本需求 N/A) |
| coding-style.md | 编码风格 | (本需求 N/A) |
| migration-mapping.md | 迁移映射 | (本需求 N/A) |

## 上游需求

- 来源:`./assistants/V0.0.3/require/REQ-00021/RESULT.md`
- 版本:v1(2026-06-06 17:00)
- 提取的 FR / NFR / AC 数量:7 FR / 6 NFR / ~30 AC / 9 INV

## 项目现状(本次扫描)

### 项目类型
- meta-skills 工具集(Claude Code marketplace)
- 仓库根:marketplace
- 子插件:`plugins/code-skills/`
- 无源代码 / 无构建 / 无包管理(沿用 CLAUDE.md 强约束)

### 目录结构(本需求关注)
```
plugins/code-skills/skills/
├── code-require/         # 本需求改造 — SKILL.md + templates/requirements.md
├── code-design/          # 本需求改造 — SKILL.md + templates/design.md
├── code-plan/            # 本需求改造 — SKILL.md + templates/plan.md
├── code-auto/            # 本需求 0 改 — SKILL.md(沿用 Q-4)
├── code-fix/             # 本需求 0 改
├── code-unit/            # 本需求 0 改
├── code-review/          # 本需求 0 改
├── code-version/         # 本需求 0 改
├── code-init/            # 本需求 0 改
├── code-rule/            # 本需求 0 改
├── code-dashboard/       # 本需求 0 改
└── code-publish/         # 本需求 0 改
```

### 已有 SKILL.md(本需求关注)
- `code-require/SKILL.md`:532 行,**已含** "## 命令行参数解析"(L127-153)+ "## 模板填充步骤"(L452-516)
- `code-design/SKILL.md`:已含 "## 命令行参数解析"(L104-130)+ "## 模板填充步骤"(L541-582)
- `code-plan/SKILL.md`:已含 "## 命令行参数解析"(L183-211)+ "## 模板填充步骤"(L1022+)
- `code-auto/SKILL.md`:本需求 0 改(沿用 Q-4 `code-auto` 不传)

### 已有模板
- `code-require/templates/requirements.md`:RESULT.md 章节结构模板(本需求占位符映射来源 §1-12)
- `code-design/templates/design.md`:本技能 RESULT.md 章节结构模板(本需求占位符映射来源 §1-16)
- `code-plan/templates/plan.md`:本技能 RESULT.md 章节结构模板(本需求占位符映射来源)
- `code-plan/templates/task-plan.md`:PLAN.md 模板(本需求 `{{任务列表}}` / `{{依赖图}}` / `{{里程碑}}` 来源)

### 编码与构建约定
- 沿用既有:本仓库 0 改 CLAUDE.md / README / 模板
- 提交格式:`chore(<scope>): <subject>`
- 版本:沿用 V0.0.3(本需求在 V0.0.3 工作空间)

### 本需求实际状态(关键发现)
- **2026-06-06 17:05**:REQ-00021 需求分析完成(看板有记录)
- **2026-06-06 17:05~17:15**:3 个 SKILL.md **已落地修改**(本概设"读 SKILL.md"验证通过)
- **本概要设计**(2026-06-06 17:15+):**回填式**概设,实际代码已落地;概设任务是"事后归档"系统设计意图
- **看板影响**:本需求在 V0.0.3/RESULT.md"概要设计清单"**尚未追加**(看板当前 17:30 变更记录只到 REQ-00020),本概设完成时需要补"概要设计清单" + "变更记录"

## 关联需求(同版本 + 跨版本)
详 `related-designs.md`

## 命令行参数解析(本需求新增)

### `code-require --result <模板文件>`
- 模板文件示例:`./templates/requirement-template.docx` / `./tmpl.md` / `./org-requirement.html`
- 输出文件:`./assistants/V0.0.3/require/REQ-00021/REQUIRE.<ext>`
- 状态:**已实现**(SKILL.md L127-153)

### `code-design --result <模板文件>`
- 模板文件示例:`./templates/design-template.docx`
- 输出文件:`./assistants/V0.0.3/design/REQ-00021/DESGIN.<ext>`(用户原文拼写)
- 状态:**已实现**(SKILL.md L104-130)

### `code-plan --result <模板文件> --plan <模板文件>`
- `--result` 输出:`./assistants/V0.0.3/plan/REQ-00021/DESGIN.<ext>`
- `--plan` 输出:`./assistants/V0.0.3/plan/REQ-00021/PLAN.<ext>`
- 状态:**已实现**(SKILL.md L183-211)

## 模板填充结果(本概设**不**实际填充,仅回填设计意图)

- 本概设**不**实际执行模板填充(本需求 REQ-00021 的实际执行是用户后续调 3 技能时)
- 本概设的"模板填充"由用户在后续 `code-require / code-design / code-plan` 调用时触发
- 模板填充屏显格式见 `interface-specs.md` §1.2
