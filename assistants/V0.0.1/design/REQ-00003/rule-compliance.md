# 规范遵循记录 — REQ-00003
更新时间:2026-06-03 21:00
版本:V0.0.1

## 1. 本次参考的规范文件(5 个,全 Glob 命中)

| 规范文件 | 类别 | 关键约束摘要 | 本次如何遵循 |
| --- | --- | --- | --- |
| `dashboard-conventions.md` | 看板 | 看板字段约定 | INV-6 0 变更 |
| `doc-conventions.md` §规则 1 | 文档 | README 多语言对仗 | 本需求不修改 README ✅ |
| `doc-conventions.md` §规则 2 | 文档 | README 与代码现状一致 | 本需求不修改 README ✅ |
| `marketplace-protocol.md` | marketplace | `marketplace.json` + `plugin.json` 引用一致性 | INV-5 0 变更(FR-9 边界) |
| `skill-conventions.md` §规则 1 | 技能 | SKILL.md frontmatter 必含 `name`+`description` 且与目录名一致 | INV-5 0 变更(本需求改 SKILL.md 正文,不改 frontmatter) |
| `module-conventions.md` | 模块 | **本需求 H2 决策:迁移到 `directory-conventions.md`,旧文件追加 DEPRECATED 标记** | INV-7 仅追加标记 |

## 2. 规范 vs 现状偏离

| # | 规范条款 | 项目现状 | 本次处理 |
| --- | --- | --- | --- |
| 1 | `skill-conventions §规则 1` frontmatter 一致性 | `code-rule/SKILL.md` frontmatter 完好 | 本需求**只改正文**,不改 frontmatter(INV-5) |
| 2 | `module-conventions.md` 现行 | 内容已存在 | 本需求**追加 DEPRECATED 标记**(INV-7),不删除内容 |
| 3 | `marketplace-protocol.md` 引用一致性 | `marketplace.json` + `plugin.json` 已对齐 | 本需求**0 变更**(INV-5) |

## 3. 规范 vs 需求冲突(无)

本需求**无规范 vs 需求冲突**。所有 FR / NFR 与既有规范兼容。

## 4. 用户授权的偏离(本设计无)

本设计**无用户授权的偏离**。所有变更均在 FR 范围内,且 FR 边界清晰(FR-9 不得修改清单 + FR-10 严禁重写)。

## 5. 规范变更响应(无)

本设计阶段**无规范侧变更**(`code-rule` 自身被扩展,但不修改 `rules/` 下的规范文件;`code-rule` 是规范的"消费者",不是"生产者"——除非用户主动调 `code-rule` 添加新规范)。

## 6. 本次设计新增的"硬性边界"

### 边界 B-1:Type B 仅追加
- 依据:REQU FR-5 + FR-10
- 含义:`code-rule` 处理 Type B 时,只**追加**到 CLAUDE.md 末尾的"AI 工作约定"小节
- 不允许:修改 CLAUDE.md 其他任何小节(包括"仓库用途"/"仓库结构"/"如何编写技能"等)

### 边界 B-2:Type C 仅追加
- 依据:REQU FR-6 + FR-10
- 含义:`code-rule` 处理 Type C 时,只**追加**到模板末尾或内联位置
- 不允许:修改模板的现有字段/示例/小节

### 边界 B-3:9 个其他 SKILL.md 零变更
- 依据:REQU FR-9
- 含义:`code-rule` 不得修改其他 9 个 `code-*` 技能的 SKILL.md(包括 `name` / `description` frontmatter)
- 允许:读取(只读)

### 边界 B-4:marketplace.json / plugin.json 零变更
- 依据:REQU FR-9
- 含义:`code-rule` 不得修改 `.claude-plugin/marketplace.json` 与 `plugins/code-skills/.claude-plugin/plugin.json`

### 边界 B-5:工作文件零变更
- 依据:REQU FR-9
- 含义:`code-rule` 不得修改 `assistants/V0.0.0/` 与 `assistants/V0.0.1/` 下的任何工作文件

### 边界 B-6:`module-conventions.md` 仅追加 DEPRECATED 标记
- 依据:Q-8=H2
- 含义:`module-conventions.md` 文件**不删除**,只追加 1 个 DEPRECATED 标记;其内容可作为历史参考
- 允许:未来调用 `code-rule` 添加"目录与模块"规范时,优先追加到 `directory-conventions.md`

## 7. 自检表

| # | 规范条款 | 自检结果 |
| --- | --- | --- |
| 1 | doc-conventions §规则 1(中英对仗) | 本需求不修改 README,N/A |
| 2 | doc-conventions §规则 2(与代码现状一致) | 本需求不修改 README,N/A |
| 3 | skill-conventions §规则 1(frontmatter 一致) | INV-5 仅改正文,不改 frontmatter ✅ |
| 4 | marketplace-protocol(marketplace 与 plugin 引用一致) | INV-5 0 变更 ✅ |
| 5 | dashboard-conventions(看板字段) | INV-6 0 变更 ✅ |
| 6 | module-conventions(模块结构) | INV-7 仅追加 DEPRECATED 标记 ✅ |
| 7 | (新建)framework-conventions(C-1) | 由本需求 M-5 创建,Q-5=H1(全空占位) ✅ |
| 8 | (新建)dependency-conventions(C-2) | 由本需求 M-5 创建,Q-5=H1 ✅ |
| 9 | (新建)naming-conventions(C-3) | 由本需求 M-5 创建,Q-5=H1 ✅ |
| 10 | (新建)directory-conventions(C-4) | 由本需求 M-5 创建,Q-5=H1;承载原 module-conventions 内容 ✅ |
| 11 | (新建)coding-style(C-5) | 由本需求 M-5 创建,Q-5=H1 ✅ |
| 12 | (新建)commit-conventions(C-6) | 由本需求 M-5 创建,Q-5=H1 ✅ |
| 13 | doc-conventions(marketplace 协议) | INV-6 0 变更 ✅ |
| 14 | skill-conventions(SKILL.md frontmatter) | INV-5 0 变更 ✅ |
