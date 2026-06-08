# 规范遵循记录 — REQ-00027
更新时间:2026-06-08 15:30
版本:V0.0.3

## 1. 本次参考的规范文件
- ./assistants/rules/skill-conventions.md
- ./assistants/rules/doc-conventions.md
- ./assistants/rules/encoding-conventions.md
- ./assistants/rules/module-conventions.md
- ./assistants/rules/marketplace-protocol.md
- ./assistants/rules/commit-conventions.md
- ./assistants/rules/dependency-conventions.md
- ./assistants/rules/dashboard-conventions.md
(共 8 份主要规范,其他 5 份为占位/辅助)

## 2. 规范 vs 现状偏离

| 规范条款 | 项目现状 | 本设计处理 |
| --- | --- | --- |
| `skill-conventions.md` §规则 1:SKILL.md frontmatter `name` 与目录名一致 | 本仓库 V0.0.3 现状有 `code-check/SKILL.md` + `code-review/SKILL.md` 两个目录,内容不 100% 一致 | 本需求不修复(留待后续) |
| `module-conventions.md`:模块边界 / 目录结构 | 本轮重写 `code-fix` + `code-auto` 不影响其他 12 个子技能 | 严守 |

## 3. 规范 vs 需求冲突

**无**。

逐条对比:
- `skill-conventions.md` §规则 1 vs FR-1:本需求 0 改 frontmatter,0 冲突
- `doc-conventions.md` §规则 1 vs NFR-1:本需求不改 README,0 冲突
- `module-conventions.md` vs FR-2:本需求 `code-auto` 模式 C 沿用既有模块边界,0 冲突
- `commit-conventions.md` vs INV-7:本需求 commit 沿用 `chore(code-fix):` / `chore(code-auto):` 前缀,0 冲突
- `marketplace-protocol.md` vs NFR-1:本需求不改 marketplace.json / plugin.json,0 冲突

## 4. 用户授权的偏离

**无**。

## 5. 规范变更响应(增量更新时填写)

N/A(本轮为首次设计)
