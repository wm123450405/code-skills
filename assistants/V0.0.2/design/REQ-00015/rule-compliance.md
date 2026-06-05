# 规范遵循记录 — REQ-00015
更新时间:2026-06-06 09:00
版本:V0.0.2

## 1. 本次参考的规范文件(13 份,全部)
- ./assistants/rules/skill-conventions.md
- ./assistants/rules/module-conventions.md
- ./assistants/rules/dashboard-conventions.md
- ./assistants/rules/marketplace-protocol.md
- ./assistants/rules/encoding-conventions.md
- ./assistants/rules/commit-conventions.md
- ./assistants/rules/directory-conventions.md
- ./assistants/rules/framework-conventions.md
- ./assistants/rules/naming-conventions.md
- ./assistants/rules/doc-conventions.md
- ./assistants/rules/dependency-conventions.md
- ./assistants/rules/migration-mapping.md
- ./assistants/rules/coding-style.md

## 2. 规范 vs 现状偏离
**0 项偏离**:
- 本需求是纯新增技能,**不**改既有 11 个 `code-*` SKILL.md / `assistants/rules/` / `marketplace.json` 既有字段

## 3. 规范 vs 需求冲突
**0 项冲突**:
- `marketplace-protocol.md §规则 1` vs FR-NFR-6:`marketplace.json` 需追加 `./skills/code-merge` → **一致**(本设计 INV-2 保证)
- `skill-conventions.md §规则 1` vs FR-NFR-1:新 SKILL.md frontmatter 必含 name + description → **一致**(本设计模块拆分保证)
- `encoding-conventions.md §规则 3` vs FR-6 看板自检:任务编码解析 → **一致**(本设计复用既有解析)

## 4. 用户授权的偏离
**0 项用户授权的偏离**(本设计严守所有规范)

## 5. 规范变更响应(增量更新时填写)
**不适用**(本需求是首次设计,非增量更新)

## 6. 自检清单(本设计严守)
- [x] SKILL.md frontmatter 必含 `name: code-merge` + `description: <完整描述>`(skill-conventions §规则 1)
- [x] SKILL.md 放在 `plugins/code-skills/skills/code-merge/SKILL.md`(module-conventions §规则 1)
- [x] 不新增 templates/ checklists/ guidelines/ 子目录(本需求无新增资源)
- [x] `marketplace.json` 追加 `./skills/code-merge`,**不**触碰其他字段(marketplace-protocol §规则 1)
- [x] `plugin.json` **不**修改(marketplace-protocol §规则 1)
- [x] 看板字段**不**扩展 → 不触发 dashboard-conventions §规则 1 的 3 文件同步
- [x] 任务编号解析复用 encoding-conventions §规则 1+3(FR-6 看板自检)
- [x] commit 格式沿用 V0.0.2 既有 `chore(<scope>): <description>` 模式

## 7. 与 REQ-00013 的协同
- REQ-00013 INV-1(8 个 SKILL.md 既有 frontmatter / 章节字节级保留)→ 本设计严守(NFR-5 + INV-1,**不**修改既有 11 个 SKILL.md)
- REQ-00013 INV-5(0 触发 `dashboard-conventions §规则 1` 3 处同步)→ 本设计严守(看板字段**不**扩展,FR-6 复用既有 5 区段)
- REQ-00013 INV-6(0 修改 `marketplace.json` / `plugin.json` / `assistants/rules/`)→ 本设计严守(仅追加 `marketplace.json` 的 `./skills/code-merge` 项,**不**触碰其他字段,符合 NFR-6)
