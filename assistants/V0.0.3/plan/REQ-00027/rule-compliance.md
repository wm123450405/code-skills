# 规范遵循记录 — REQ-00027
更新时间:2026-06-08 15:35
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
(共 8 份主要规范)

## 2. 规范 vs 现状偏离
**无**。

## 3. 规范 vs 需求冲突
**无**。

逐条对比:
- `skill-conventions.md` §规则 1 vs FR-1/FR-2:本轮 0 改 frontmatter,0 冲突
- `doc-conventions.md` §规则 1 vs NFR-1:本轮不改 README,0 冲突
- `encoding-conventions.md` §规则 1+2 vs NFR-1:本轮 0 新增编码,0 冲突
- `module-conventions.md` vs FR-2:`code-auto` 模式 C 沿用既有模块边界,0 冲突
- `commit-conventions.md` vs INV-7:本轮 commit 沿用 `chore(code-fix):` / `chore(code-auto):` 前缀,0 冲突
- `marketplace-protocol.md` vs NFR-1:本轮不改 marketplace.json / plugin.json,0 冲突
- `dashboard-conventions.md` vs TASK-003:看板同步沿用 `^## 任务清单$` / `^## 变更记录$` 等锚点,0 冲突

## 4. 用户授权的偏离
**无**。

## 5. 规范变更响应(增量更新时)
N/A(本轮为首次设计)
