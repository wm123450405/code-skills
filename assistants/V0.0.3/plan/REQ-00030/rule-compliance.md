# 规范遵循记录 — REQ-00030(详设阶段)

更新时间:2026-06-12 14:31
版本:V0.0.3

## 1. 本次参考的规范文件

(同概设,见 `design/REQ-00030/rule-compliance.md` §1)

## 2. 规范 vs 现状偏离

- **无新偏离**:
  - INV-1 ~ INV-9 全部满足
  - 既有 11 个 `code-*` 技能的 `SKILL.md` 命名 = 目录名(全部满足)
  - 既有 `templates/` 资源文件均位于 `plugins/code-skills/skills/<skill>/templates/`(满足)
  - 既有 `README.md` / `README.en.md` 结构对仗(满足)
  - 既有看板字段(任务编号正则 / 6 类型 / 13 触发/来源)满足

## 3. 规范 vs 需求冲突

- **无冲突**(同概设)

## 4. 用户授权的偏离

- **无授权偏离**(同概设)

## 5. 规范变更响应(增量更新时填写,本节首次详设为空)

- 本节首次详设,无规范变更

## 6. 详设阶段新增的自检结论(本节为详设独有)

### 6.1 接口契约自检(`api-standards.md` 等)

- **不适用**(本仓库无对外 API)

### 6.2 数据建模自检(`data-modeling.md` 等)

- **不适用**(本仓库无持久化数据模型)

### 6.3 安全自检(`security-standards.md` 等)

- **不适用**(本仓库无安全相关)
- 沿用既有:`commit-conventions` 提交审计

### 6.4 性能自检(`performance-standards.md` 等)

- **不适用**(本仓库无性能相关)

### 6.5 测试自检(`testing-standards.md` 等)

- **不适用**(本仓库无测试框架)
- 沿用既有:人工评审(`code-check`)+ `git diff` 验证

### 6.6 可观测性自检(`observability-standards.md` 等)

- **不适用**(本仓库无可观测性相关)
- 沿用既有:`commit-conventions` 提交审计

## 7. 详设阶段的"## 不要做的事"补充

- **不**修改 `templates/design.md` §1-§6 / §11-§16 既有章节(INV-3)
- **不**修改 `templates/plan.md` §1-§3 / §13-§15 既有章节(INV-3)
- **不**修改 `code-design/SKILL.md` frontmatter L1-3(INV-1)
- **不**修改 `code-plan/SKILL.md` frontmatter L1-3(INV-1)
- **不**修改 `code-check/SKILL.md` frontmatter L1-3(INV-1)
- **不**修改其他 11 个 `code-*` 技能 SKILL.md(INV-4)
- **不**修改 `./assistants/rules/*.md`(INV-5)
- **不**修改 `marketplace.json` / `plugin.json` / `CLAUDE.md` / `README*.md`(INV-6)
- **不**修改既有 9 个 REQ 的 design / plan(INV-7)
- **不**新增三方依赖(INV-8)
- **不**触发 `dashboard-conventions §规则 1` 三方同步(INV-9)
