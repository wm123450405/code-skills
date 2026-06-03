# 材料登记 — REQ-00003
更新时间:2026-06-03 21:00
版本:V0.0.1

## 项目级规范(5 个)

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `./assistants/rules/dashboard-conventions.md` | 看板 | 看板字段约定、状态机(本需求"Type A 看板"基线) |
| `./assistants/rules/doc-conventions.md` | 文档 | README 多语言对仗(规则 1)+ 仓库级使用说明文档(规则 2) |
| `./assistants/rules/marketplace-protocol.md` | marketplace | `marketplace.json` + `plugin.json` 协议约束(本需求严禁修改边界) |
| `./assistants/rules/module-conventions.md` | 模块 | **本需求 H2 决策:迁移到 `directory-conventions.md`,旧文件标记 DEPRECATED** |
| `./assistants/rules/skill-conventions.md` | 技能 | SKILL.md frontmatter 必含 `name` + `description` 且与目录名一致(规则 1) |

> 注:本需求涉及 6 类核心规范新建 + 1 个迁移(原 `module-conventions.md` → `directory-conventions.md`),详见 `design-notes.md` §决策 1。

## 上游需求

- 来源:`./assistants/V0.0.1/require/REQ-00003/RESULT.md`
- 版本:v1(2026-06-03 20:45,已锁定)
- 提取:10 FR / 6 NFR / 10 AC
- 3 项已锁定(Q-1/Q-2/Q-3)+ 5 项本设计阶段确认(Q-4/Q-5/Q-6/Q-7/Q-8)
- 关键交叉点:

| FR | 摘要 | 本设计章节 |
| --- | --- | --- |
| FR-1 | 3 种目标类型(Type A 规则 / Type B CLAUDE.md / Type C 模板) | §3.1 核心架构 |
| FR-2 | Type A 6 类核心规范 | §3.2 Type A 模块 |
| FR-3 | Type A 条件性分类的"占位"模式 | §3.2.2 占位流程 |
| FR-4 | Type A 默认分类的"引导"模式 | §3.2.3 引导流程 |
| FR-5 | Type B(AI 工作指引)标准结构与插入位置 | §3.3 Type B 模块 |
| FR-6 | Type C(模板内容提示)两种插入位置 | §3.4 Type C 模块 |
| FR-7 | 类型识别(自动 + 显式) | §3.5 类型识别引擎 |
| FR-8 | 现有 Type A 流程不变 | §3.2.1 现有流程继承 |
| FR-9 | 不得修改的边界(FR-9 边界清单) | §5 不变量 INV-7 |
| FR-10 | Type B/C 严禁重写既有内容 | §5 不变量 INV-5 / INV-6 |

## 上游概要设计

- **本需求无上游概要设计**(本设计是 REQ-00003 的概要设计阶段本身)

## 项目现状(本次扫描)

### 项目类型
- 语言:Markdown(技能描述文件)
- 框架:Claude Code plugin / marketplace 协议
- 关键依赖:无(本仓库为纯文档/SKILL 集合,无运行时依赖)

### 目录结构(本需求相关)
- `plugins/code-skills/skills/`(10 个技能,各含 `SKILL.md` + `templates/`)
- `plugins/code-skills/CLAUDE.md`(1 个文件,本需求 Type B 目标)
- `assistants/rules/`(5 个现有文件,本需求扩展点)

### 已有模块(`code-rule` 技能)
- `plugins/code-skills/skills/code-rule/SKILL.md`(272 行,9 步骤工作流,Type A 单一类型)
- `plugins/code-skills/skills/code-rule/templates/rule.md`(52 行,规则小节标准结构)

### 已有接口
- 现有 9 步骤工作流(步骤 0-9)
- `AskUserQuestion` 用于分类确认
- 重复检测 + 冲突检测 + 跨分类引用机制

### 已有数据模型
- 规则条目结构(8 字段):条款 / 强制级别 / 适用范围 / 正面示例 / 反面示例 / 例外 / 关联规范 / 来源

### 关键观察
1. **现有 SKILL.md 与实际 `rules/` 不一致**:
   - SKILL.md 步骤 0 列出 11 个预期分类文件,但 `./assistants/rules/` 实际只有 5 个
   - 本需求是 6 个新分类的"占位",与 SKILL.md 中的预期分类需要保持映射
2. **`code-rule` SKILL.md 工作目录约定**(L32-44)已列出 11 个预期文件名,本需求 H2 决策需要**部分重命名**:`module-conventions.md` → `directory-conventions.md`,其他不变
3. **CLAUDE.md 已有 7 个小节**,但无"## AI 工作约定(由 code-rule 维护)"小节(FR-5 需要)
4. **模板文件**(`templates/rule.md`)结构清晰,可作为 Type A 模板基础

## 关键澄清记录(本设计阶段)

| Q 编号 | 问题 | 阶段回答 | 影响章节 |
| --- | --- | --- | --- |
| Q-4 | C-4 分类(C-4 目录与模块规范)文件名 | **沿用 `directory-conventions.md`**(新建独立文件) | §3.2.4 分类映射表 |
| Q-5 | 6 个新分类文件的初始内容 | **H1 全部建空占位**(纯脚手架) | §3.2.2 占位流程 |
| Q-6 | Type B 是否需要"示例"字段 | **不增加**示例字段(本设计决策) | §3.3 Type B 数据结构 |
| Q-7 | Type C 内容提示格式 | **末尾追加**:`## 提示: <主题>` / **内联**:`### 提示: <字段>` | §3.4 Type C 数据结构 |
| Q-8 | 现有 5 个规范文件处理 | **H2 迁移部分重叠**:`module-conventions.md` → `directory-conventions.md`(旧文件标记 DEPRECATED) | §3.2.4 分类映射表 + §4 实施计划 |

> 详细问答记录见 `clarifications.md`。

## 本次变更源

| 变更源 | 检测方式 | 变化列表 |
| --- | --- | --- |
| 需求侧 | 上游 REQU v1(已锁定) | 10 FR / 6 NFR / 10 AC,3 Q 锁定,5 Q 待本设计 |
| 概要设计侧 | (无上游) | — |
| 规范侧 | `./assistants/rules/` 对比 | 5 个文件保持 + 1 个文件迁移(module → directory) |
| 代码侧 | 重跑项目探索 | 已发现 1 个 `code-rule/SKILL.md` + 1 个 `code-rule/templates/rule.md` + 1 个 `plugins/code-skills/CLAUDE.md` |

## 预检冲突

| 冲突源 | 描述 | 本设计处理 |
| --- | --- | --- |
| SKILL.md vs 现状 | SKILL.md 步骤 0 列出 11 个预期分类文件,实际只有 5 个 | 本需求在 SKILL.md 步骤 0 列表中**更新为 11 个新分类**(部分名称变更),并**重写**步骤 4 的分类识别表(从 11 个旧分类 → 6 个新核心分类 + 5 个保留专项分类) |
| `code-rule` 边界 vs 本需求 | 既有"不要重写既有规范文件"与本需求 FR-9 边界 | 本需求**遵守**既有约束:`module-conventions.md` 不重写,只追加 DEPRECATED 标记;`directory-conventions.md` 全新建 |
| `code-rule` 不写 `assistants/<版本号>/` | 本需求 Type A 全部在 `assistants/rules/` 下,不触及版本目录 | **不冲突** |
