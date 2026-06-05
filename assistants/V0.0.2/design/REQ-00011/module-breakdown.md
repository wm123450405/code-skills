# 模块拆分 — REQ-00011

更新时间:2026-06-05
版本:V0.0.2

## 模块总览

| 模块名 | 路径 | 状态 | 职责 | 对外接口 | 依赖 |
| --- | --- | --- | --- | --- | --- |
| `code-design` 步骤 0b | `plugins/code-skills/skills/code-design/SKILL.md` | 修改(增量追加) | 设计目标确认 + 写入 `design/.../RESULT.md` | AskUserQuestion × 1-5 | `Read` + `Write` + `AskUserQuestion` |
| `code-design` 模板 | `plugins/code-skills/skills/code-design/templates/design.md` | 修改(顶部预留) | `design/.../RESULT.md` 模板顶部预留"## 设计目标"占位 | (模板) | — |
| `code-plan` 步骤 0b | `plugins/code-skills/skills/code-plan/SKILL.md` | 修改(增量追加) | 读 `design/.../RESULT.md` 的"## 设计目标"小节,沿用 or 退化;据小节调整任务粒度 | AskUserQuestion × 1-5(退化时) | `Read` + `Write` + `AskUserQuestion` |
| `code-plan` 任务粒度调整 | `plugins/code-skills/skills/code-plan/SKILL.md`(同步骤 0b 同一文件) | 修改(增量追加) | 任务拆分时按"## 设计目标"小节判定粒度 | (内部) | — |
| `code-plan` 模板 | `plugins/code-skills/skills/code-plan/templates/plan.md` | 修改(顶部预留) | `plan/.../RESULT.md` 模板顶部预留"## 设计目标"占位 | (模板) | — |

## 新增模块

**无**。本需求不新增任何模块,仅在既有模块上**增量追加**"步骤 0b"小节 + 模板顶部预留位。

## 复用既有模块

| 模块 | 复用方式 | 既有引用位置 |
| --- | --- | --- |
| `code-design` 既有"步骤 0a:git pull"小节(REQ-00005 落地) | 直接复用,本需求在其后追加"步骤 0b" | `plugins/code-skills/skills/code-design/SKILL.md` §步骤 0a |
| `code-plan` 既有"步骤 0a:git pull"小节(REQ-00005 落地) | 直接复用,本需求在其后追加"步骤 0b" | `plugins/code-skills/skills/code-plan/SKILL.md` §步骤 0a |
| `code-design` 既有"## 文档头"模板区段 | 直接复用,本需求在其后加"## 设计目标"占位 | `plugins/code-skills/skills/code-design/templates/design.md` |
| `code-plan` 既有"## 文档头"模板区段 | 直接复用,本需求在其后加"## 设计目标"占位 | `plugins/code-skills/skills/code-plan/templates/plan.md` |
| `code-plan` 既有"任务拆分"步骤 | 直接复用,本需求在其前/后加"按设计目标调整粒度"段 | `plugins/code-skills/skills/code-plan/SKILL.md` §任务拆分 |
| `code-auto` 既有"总选推荐项"行为(REQ-00007 FR-3 / Q-4) | 直接复用,本需求不触发升级 | `plugins/code-skills/skills/code-auto/SKILL.md` |

## 修改既有模块

| 模块 | 变更点 | 变更对既有调用方的影响评估 |
| --- | --- | --- |
| `code-design` SKILL.md 正文 | 步骤 0a 之后**增量追加**"步骤 0b 设计目标确认"小节 | **无影响**:既有"步骤 0-N"流程不变;frontmatter 不变;`code-auto` 调 `code-design` 时**仅**新增"触发 AskUserQuestion"事件,`code-auto` 沿用"总选推荐项" |
| `code-design` 模板 `design.md` | 顶部"## 文档头"区段后 + "## 1. 设计概述"前**预留"## 设计目标"占位** | **无影响**:模板其他章节不变;占位用注释标注"本节由 code-design 步骤 0b 自动生成" |
| `code-plan` SKILL.md 正文 | 步骤 0a 之后**增量追加**"步骤 0b 设计目标确认"小节;**任务拆分**步骤前/后**追加**"按设计目标调整粒度"段 | **无影响**:既有"步骤 0-N"流程不变;frontmatter 不变;`code-auto` 调 `code-plan` 时**仅**新增"读 design" + "触发 AskUserQuestion(若退化)"事件 |
| `code-plan` 模板 `plan.md` | 顶部"## 文档头"区段后 + "## 1. ..."前**预留"## 设计目标"占位** | **无影响**:模板其他章节不变 |

## 关键决策与规范对照

| 决策 | 规范依据 |
| --- | --- |
| 增量追加"步骤 0b"不重写既有章节 | `skill-conventions.md §规则 1`(frontmatter 不变)+ NFR-2 强约束 |
| 资源放技能子目录 `templates/` | `module-conventions.md §规则 1`(已 DEPRECATED,但仍参考) |
| 模板顶部预留位 | `directory-conventions.md`(替代 module-conventions) |
| 零新增依赖 | NFR-1 强约束 |
| 不改 8 个其他技能 | FR-7.AC-7.1 强约束 |
| 不触发 `dashboard-conventions §规则 1` 3 处同步 | NFR-4 强约束(本需求**不**改看板) |
| `code-auto` 沿用"总选推荐项" | NFR-5 强约束;FR-7.AC-7.2 不变 |
| 步骤命名"步骤 0b"沿用"步骤 0a" | NFR-6 强约束(与 REQ-00005 / REQ-00009 / REQ-00010 模式一致) |

## 自检:对照 `module-conventions.md` / `directory-conventions.md` / `skill-conventions.md`

| 规范条款 | 本次涉及 | 满足情况 |
| --- | --- | --- |
| `skill-conventions.md §规则 1`:SKILL.md 必含 name + description,frontmatter 不变 | 2 个技能 SKILL.md frontmatter 不动 | ✅ INV-1 强约束 |
| `module-conventions.md §规则 1`:资源放技能子目录(`templates/` / `checklists/` / `guidelines/`) | 2 个 `templates/*.md` 顶部预留位 | ✅ 已在子目录内,不改位置 |
| `directory-conventions.md §规则 1`:(待添加) | 不涉及 | N/A |
| `dashboard-conventions.md §规则 1`:看板字段扩展需 3 处同步 | 不涉及(本需求**不**改看板) | ✅ NFR-4 强约束 |
| `marketplace-protocol.md §规则 1`:marketplace 与 plugin 协议清单 | 不涉及(本需求**不**改 marketplace.json / plugin.json) | ✅ FR-8.AC-8.1 强约束 |
| `doc-conventions.md §规则 1`:README 多语言对仗 | 不涉及(本需求**不**改 README) | ✅ FR-8.AC-8.4 强约束 |
| `doc-conventions.md §规则 2`:README 完整性 | 不涉及 | N/A |
| `commit-conventions.md §规则 1`:(待添加) | 不涉及(本需求**不**填该规则) | ✅ FR-8.AC-8.3 强约束 |
| `encoding-conventions.md §规则 1-3`:3 类编码权威源 | 不涉及(本需求**不**产生新编码) | N/A |
| `dependency-conventions.md §规则 1`:(待添加);NFR-1 零新增依赖 | 不涉及 | ✅ NFR-1 强约束 |
| `framework-conventions.md §规则 1`:(待添加) | 不涉及 | N/A |
| `coding-style.md §规则 1`:(待添加) | 不涉及 | N/A |
| `naming-conventions.md §规则 1`:(待添加) | 不涉及 | N/A |
