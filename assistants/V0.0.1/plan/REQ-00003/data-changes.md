# 数据结构完整变更 — REQ-00003

更新时间:2026-06-04 09:15
版本:V0.0.1

> 本需求**无数据库表/JSON 实体变更**;本文件记录"文件层数据结构"的变更。

## 新增实体:6 个 Type A 规范文件(C-1 ~ C-6)

| 字段 | 类型 | 约束 | 说明 |
| --- | --- | --- | --- |
| 路径 | string | `./assistants/rules/<分类>.md` | 6 个新文件 |
| 文件头 | Markdown | 必须含分类中文名 + 英文名 + 维护声明 + 适用版本 | 复用 `templates/rule.md` 头部 |
| 适用场景 | Markdown H2 | `## 适用场景` | 本文件覆盖范围 |
| 强制级别约定 | Markdown H2 | `## 强制级别约定` | 文件级说明 |
| 规则 1 | Markdown H2 | `## 规则 1: (待添加)` | 占位 |

**关系**:
- 6 个新文件与 4 个保留文件并列(11 个并存)
- 6 个新文件内容在初始化时仅含骨架(占位模式,Q-5=H1)
- `directory-conventions.md` 后续将承载 `module-conventions.md` 的迁移内容(由 `code-it` 阶段完成,本 plan 阶段不迁移)

**存储选型**:Markdown 文件(与现有规范文件一致)

**迁移脚本**:N/A(无数据库)

**依据规范**:`./assistants/rules/skill-conventions.md` §规则 1 + `module-conventions.md`

## 新增实体:CLAUDE.md "## AI 工作约定"小节(Type B)

| 字段 | 类型 | 约束 | 说明 |
| --- | --- | --- | --- |
| 路径 | string | `plugins/code-skills/CLAUDE.md` | 文件级 |
| 小节标题 | Markdown H2 | `## AI 工作约定(由 code-rule 维护)` | 固定字面值 |
| 小节说明 | Markdown 引用块 | 含"本小节由 `code-rule` 技能维护;手动修改可能被 `code-rule` 覆盖" | 首次创建时写入 |
| 指引 N | Markdown H3 | `### 指引 N: <指引简称>` | N 自增 |
| 指引子字段 | Markdown H4 | 描述 / 适用场景 / 期望行为 / 来源(5 字段) | 详见 `interface-specs.md` |

**关系**:
- 与 CLAUDE.md 其他 7 个小节并列
- **仅追加**,不修改其他小节(INV-3)

**存储选型**:Markdown 文件(与现有 CLAUDE.md 一致)

**迁移脚本**:N/A

**依据规范**:`skill-conventions.md` §规则 1(本规则不约束 CLAUDE.md 字段)

## 新增实体:模板末尾"## 提示"小节或内联"### 提示"小节(Type C)

| 字段 | 类型 | 约束 | 说明 |
| --- | --- | --- | --- |
| 路径 | string | `plugins/code-skills/skills/<技能>/templates/<name>.md` | 模板文件 |
| 末尾模式小节 | Markdown H2 | `## 提示: <主题>` | 末尾追加 |
| 内联模式小节 | Markdown H3 | `### 提示: <字段>` | 指定二级小节内 |
| 提示子字段 | Markdown 列表 | 字段 / 必填 / 简明说明 / 错误示例(末尾可选) | 详见 `interface-specs.md` |

**关系**:
- 与模板其他小节并列
- **仅追加**,不修改其他内容(INV-4)
- 本 plan 阶段**不实际修改任何现有模板**(仅扩展 `templates/rule.md` 支持该结构)

**存储选型**:Markdown 文件

**迁移脚本**:N/A

**依据规范**:`module-conventions.md` §规则 1

## 修改实体:`code-rule/SKILL.md`(扩展正文)

| 字段 | 类型 | 约束 | 说明 |
| --- | --- | --- | --- |
| frontmatter | YAML | 不变(本需求改正文,不改 frontmatter) | INV-5 |
| L32-44 工作目录约定 | Markdown 代码块 | 11 个新分类文件名 | INV-8 |
| L117-128 步骤 4 关键词表 | Markdown 列表 | 11 旧 → 6 核心 + 5 专项 | INV-8(向后兼容旧关键词) |
| §步骤 4 整体结构 | Markdown | 扩展为"4.1 拆分 + 4.2 类型识别 + 4.3 初步归类"3 段 | Q-PLAN-2 微调 |
| 新增小节"Type B 子流程" | Markdown | 含触发识别 + 数据结构 + 插入算法 | M-3 |
| 新增小节"Type C 子流程" | Markdown | 含触发识别 + 数据结构 + 插入算法 | M-4 |

**关系**:
- 现有 9 步骤主流程不变(FR-8, INV-1)
- 步骤 4 扩展为 3 段(plan 阶段 Q-PLAN-2 微调)
- 新增 2 个小节(Type B / Type C)文档化

**存储选型**:Markdown 文件

**依据规范**:`skill-conventions.md` §规则 1

## 修改实体:`code-rule/templates/rule.md`(扩展)

| 字段 | 类型 | 约束 | 说明 |
| --- | --- | --- | --- |
| 文件头 | Markdown | 追加"占位模式" + "引导模式"说明 | M-8 |
| 8 字段规则小节 | Markdown H2 | **不变**(向后兼容) | FR-8 |

**依据规范**:`module-conventions.md` §规则 1(资源摆放在 `templates/`)

## 修改实体:`module-conventions.md`(追加 DEPRECATED 标记)

| 字段 | 类型 | 约束 | 说明 |
| --- | --- | --- | --- |
| 文件头 | Markdown | 追加 1 个 `> ⚠️ **DEPRECATED**` 引用块 | M-6 |
| 现有内容 | Markdown | **不修改** | INV-7(回退路径) |

**依据规范**:design Q-8=H2 决策

## 不变更的实体

- `dashboard-conventions.md`(INV-6)
- `doc-conventions.md`(INV-6)
- `marketplace-protocol.md`(INV-6)
- `skill-conventions.md`(INV-6)
- `.claude-plugin/marketplace.json`(INV-5)
- `plugins/code-skills/.claude-plugin/plugin.json`(INV-5)
- 其他 9 个 `code-*` 技能的 SKILL.md frontmatter(INV-5)
- `plugins/code-skills/README.md` / `README.en.md`(本需求不涉及)
- `assistants/V0.0.0/` / `assistants/V0.0.1/` 下的任何工作文件(INV-5)

## 迁移计划总览

| 文件 | 变更类型 | commit 编号 | 验证手段 |
| --- | --- | --- | --- |
| 6 个新规范文件 | 新建 | commit 2 | `Grep "规则 1" 新建文件` 命中占位 |
| `module-conventions.md` | 修改(追加) | commit 3 | `git diff` 仅显示 DEPRECATED 段 |
| `code-rule/SKILL.md` | 修改(扩展) | commit 1 | `git diff` 仅显示扩展段,frontmatter 不变 |
| `code-rule/templates/rule.md` | 修改(扩展) | commit 4 | `git diff` 仅显示头部扩展段 |
| `plugins/code-skills/CLAUDE.md` | 修改(末尾追加) | commit 5 | `git diff` 仅显示"+"行,无"-"行 |
