# 规范遵循记录 — REQ-00035

更新时间:2026-06-15 19:15
版本:V0.0.3

## 1. 本次参考的规范文件

- ./assistants/rules/encoding-conventions.md
- ./assistants/rules/dashboard-conventions.md
- ./assistants/rules/skill-conventions.md
- ./assistants/rules/module-conventions.md
- ./assistants/rules/doc-conventions.md
- ./assistants/rules/marketplace-protocol.md
- ./assistants/rules/migration-mapping.md

## 2. 规范 vs 现状偏离

- **无显著偏离**:本设计不修改项目结构 / 模块边界 / 依赖方向;仅在 5 主流程技能 SKILL.md 中追加 1 个新小节(在"## 工具使用约定" 段后 + "## 工作流程" 段前);在 1 个编排 + 1 个 dashboard 各追加 1 段说明
- 自检:每个 SKILL.md 改写严格遵循"锚点"约定(`skill-conventions.md`),**不**修改 frontmatter / 既有章节

## 3. 规范 vs 需求冲突

- 无冲突(NFR-5 强约束:不修改 `./assistants/rules/`)

## 4. 用户授权的偏离

- 无偏离

## 5. 规范变更响应(增量更新时填写)

- 不适用(本设计为首次,无规范侧变化)
