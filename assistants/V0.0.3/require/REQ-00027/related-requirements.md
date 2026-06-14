# 关联需求 — REQ-00027

## REQ-00009(V0.0.2)
- **关联点**:`code-unit` 守卫"项目可测性",决定 BUG 路径是否调 `code-unit`
- **影响**:本需求 §7.3 步骤 3 条件触发逻辑沿用 REQ-00009 约定

## REQ-00022(V0.0.3)
- **关联点**:`code-review` → `code-check` 重命名
- **影响**:本需求 §7.3 步骤 4 直接使用 `code-check`(无需新增 marketplace 词条)

## REQ-00005(V0.0.2)
- **关联点**:`code-require` / `code-design` / `code-plan` "首步拉取 + 末步提交"模式
- **影响**:BUG 路径(`code-plan` → `code-it` → `code-unit` → `code-check`)沿用此模式

## BUG-00001 / BUG-00002 / BUG-00003(V0.0.3)
- **关联点**:现有 BUG 修复全流程
- **影响**:本需求为该全流程的自动化编排(`code-auto` 模式 C)
