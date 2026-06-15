# 规范遵循记录 — REQ-00033

更新时间:2026-06-15 12:30
版本:V0.0.3

## 1. 本次参考的规范文件

- `./assistants/rules/skill-conventions.md`(SKILL.md frontmatter L1-3 字节级保留)
- `./assistants/rules/module-conventions.md`(资源放 `templates/` / `checklists/` / `guidelines/`)
- `./assistants/rules/doc-conventions.md`(README 中英版本结构对仗;主语言版本完整)
- `./assistants/rules/dashboard-conventions.md`(看板字段三方同步)
- `./assistants/rules/commit-conventions.md`(`chore(<skill>):` 前缀)
- `./assistants/rules/encoding-conventions.md`(需求编号 5 位纯数字;接收端可放宽)
- `./assistants/rules/marketplace-protocol.md`(plugin.json / marketplace.json 引用一致)
- (其他 5 个规范本设计不涉及,沿用既有)

## 2. 规范 vs 现状偏离(本设计 0 偏离)

- 不适用(本设计是 SKILL.md 文字改造,不涉及项目结构变更)

## 3. 规范 vs 设计冲突(本设计 0 冲突)

- 详细设计要求"修改 SKILL.md"vs `skill-conventions.md` 要求"frontmatter 字节级保留"→ **不冲突**(本设计**不**改 frontmatter)
- 详细设计要求"不修改 `templates/requirements.md`"vs `module-conventions.md` → **不冲突**

## 4. 用户授权的偏离(本设计 0 偏离)

- 不适用(本设计严格遵循所有适用规范)

## 5. 规范变更响应(本设计不涉及增量)

- 不适用(本设计是首次设计,无规范变更需响应)
