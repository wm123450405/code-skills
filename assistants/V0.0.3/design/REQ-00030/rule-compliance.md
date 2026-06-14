# 规范遵循记录 — REQ-00030

更新时间:2026-06-12 14:25
版本:V0.0.3

## 1. 本次参考的规范文件

- `./assistants/rules/skill-conventions.md`
- `./assistants/rules/module-conventions.md`(DEPRECATED,沿用历史)
- `./assistants/rules/directory-conventions.md`
- `./assistants/rules/doc-conventions.md`
- `./assistants/rules/dashboard-conventions.md`
- `./assistants/rules/encoding-conventions.md`
- `./assistants/rules/naming-conventions.md`
- `./assistants/rules/coding-style.md`
- `./assistants/rules/commit-conventions.md`
- `./assistants/rules/framework-conventions.md`
- `./assistants/rules/dependency-conventions.md`

## 2. 规范 vs 现状偏离(本节为完整性列出,本需求**无**新偏离)

- **无新偏离**:
  - 既有 11 个 `code-*` 技能的 `SKILL.md` 命名 = 目录名(全部满足 `skill-conventions §规则 1`)
  - 既有 5 个 `templates/` 资源文件均位于 `plugins/code-skills/skills/<skill>/templates/`(满足 `module-conventions §规则 1`)
  - 既有 `README.md` / `README.en.md` 结构对仗(满足 `doc-conventions §规则 1`)
  - 既有看板字段(任务编号正则 / 6 类型 / 13 触发/来源)满足 `dashboard-conventions §规则 1`

## 3. 规范 vs 需求冲突

- **无冲突**:
  - 本需求**不**修改任何项目级规范
  - 本需求**不**触发看板字段扩展
  - 本需求**不**触发 README 结构变化
  - 本需求**不**引入新三方依赖

## 4. 用户授权的偏离

- **无授权偏离**:
  - 本需求完全沿用既有规范
  - 所有约束均通过修改 SKILL.md 步骤定义 + templates 章节硬切,**不**需要偏离规范

## 5. 规范变更响应(增量更新时填写,本节首次设计为空)

- 本节首次设计,无规范变更
- 未来若 `code-rule` 修订任一规范,本设计应**不**触发回流(本设计**不**引用具体规范条款,只引用规范**类别**)
