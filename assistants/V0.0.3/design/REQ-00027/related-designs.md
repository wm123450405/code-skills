# 关联概要设计 — REQ-00027

## REQ-00022(V0.0.3)`code-review` → `code-check` 重命名
- **关联点**:本需求使用 `code-check` 技能(原 `code-review`)
- **影响**:`code-auto` BUG 路径步骤 4 直接用 `code-check`;不新增 marketplace 词条
- **现状**:本仓库 V0.0.3 实际有 `plugins/code-skills/skills/code-check/SKILL.md` 目录;SKILL.md 改名未完成 100% 覆盖(沿用既有)

## REQ-00005(V0.0.2)`code-require` / `code-design` / `code-plan` 首步拉取 + 末步提交
- **关联点**:本需求中 `code-auto` BUG 路径的子技能(沿用首步拉取 + 末步提交模式)
- **影响**:BUG 路径首尾 commit 由子技能各自负责

## REQ-00009(V0.0.2)`code-unit` 守卫"项目可测性"
- **关联点**:本需求中 `code-auto` BUG 路径 `code-unit` 步骤的条件触发(沿用 `code-plan` §"项目可测性")
- **影响**:BUG 路径在 `code-plan` 阶段产出的 `fix-plan.md` 标记"项目可测性"后,`code-auto` 才调 `code-unit`

## BUG-00001 / BUG-00002 / BUG-00003(V0.0.3)现有 BUG 修复全流程
- **关联点**:本需求为该全流程的自动化编排
- **影响**:本轮仅改 `code-fix` + `code-auto`;既有 BUG 流程不受影响
