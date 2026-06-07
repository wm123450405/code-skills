# 规范遵循记录 — REQ-00023
更新时间:2026-06-07
版本:V0.0.3

## 1. 本次参考的规范文件
- ./assistants/rules/dashboard-conventions.md
- ./assistants/rules/skill-conventions.md
- ./assistants/rules/module-conventions.md
- ./assistants/rules/encoding-conventions.md
- ./assistants/rules/doc-conventions.md
- ./assistants/rules/naming-conventions.md
- ./assistants/rules/directory-conventions.md
- ./assistants/rules/framework-conventions.md
- ./assistants/rules/dependency-conventions.md
- ./assistants/rules/commit-conventions.md
- ./assistants/rules/coding-style.md
- ./assistants/rules/marketplace-protocol.md
- ./assistants/rules/migration-mapping.md

## 2. 规范 vs 现状偏离
**无**(本需求零改动其他 12 个 `code-*` 技能,零新增看板字段,零新增模块)

## 3. 规范 vs 需求冲突
**无**(INV-1 ~ INV-9 全部锁定 0 偏离)

## 4. 用户授权的偏离
**无**

## 5. 规范变更响应(增量更新时填写)
- 本需求**不**触发任何规范变更
- 零新增字段 → 零触发 `dashboard-conventions §规则 1` 三同步
- 零修改 frontmatter → 零触发 `skill-conventions §规则 1` 同步

## 6. 关键判定
- **dashboard-conventions §规则 1 触发判定**:本需求零新增看板字段(INV-8 锁定),**不**触发三同步。`version-RESULT.md` / `CLAUDE.md` / 本规范均**不**修改。
- **NFR-6 触发判定**:本需求仅改 `code-dashboard/SKILL.md` 1 个文件,其他 12 个 `code-*` 技能 frontmatter 字节级保留(INV-2 锁定)。
