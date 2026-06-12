# 模块拆分 — REQ-00031

更新时间:2026-06-12 15:25
版本:V0.0.3

## 模块总览

| 模块 | 路径 | 状态 | 职责 | 依赖 |
| --- | --- | --- | --- | --- |
| code-plan | `plugins/code-skills/skills/code-plan/SKILL.md` | 修改 | 修订任务粒度原则:内化编译/运行 + 移除测试类型 + 收窄测试状态枚举 | — |
| code-it | `plugins/code-skills/skills/code-it/SKILL.md` | 修改 | 文档头追加"不含单元测试"职责声明 | — |
| code-unit | `plugins/code-skills/skills/code-unit/SKILL.md` | 修改 | 文档头追加"独立、可选"职责声明 | — |
| code-auto | `plugins/code-skills/skills/code-auto/SKILL.md` | 修改 | 步骤 4.b 由"按需调用"改为"恒等跳过" | — |
| templates-plan | `plugins/code-skills/skills/code-plan/templates/plan.md` | 修改 | 任务类型移除 `测试`,测试状态字段收窄为 2 个 | code-plan |

## 复用既有模块

| 模块/路径 | 复用方式 | 复用内容 |
| --- | --- | --- |
| `code-plan §步骤 10A "任务拆分原则"` | 扩展(追加 1 句) | 既有"可独立验证"小节 |
| `code-plan §步骤 10A "任务类型"` | 修改(移除 1 项) | 既有 6 类任务类型列表 |
| `code-plan §步骤 10A "任务双状态字段"` | 修改(收窄 2 处) | 既有"测试状态"枚举 + "双状态语义" |
| `code-it ## 目标` | 扩展(追加 1 行) | 既有 2-3 段职责描述 |
| `code-unit ## 目标` | 扩展(追加 1 行) | 既有 1-2 段职责描述 |
| `code-auto §步骤 4 任务循环 步骤 4.b` | 修改(改写) | 既有"按需调用 code-unit"逻辑 |
| `templates/plan.md` 任务类型 + 测试状态 | 修改(收窄) | 既有字段表 |

## 新增模块

| 模块/路径 | 职责 | 关键决策 |
| --- | --- | --- |
| (无) | — | — |

## 修改既有模块

| 模块/路径 | 修改内容 | INV 约束 |
| --- | --- | --- |
| `code-plan/SKILL.md` §步骤 10A | 任务粒度原则修订(追加 1 句 + 移除 1 项 + 收窄 2 处) | INV-1 / INV-2 / INV-3 |
| `code-it/SKILL.md` ## 目标 | 追加 1 行 | INV-1 / INV-2 / INV-3 |
| `code-unit/SKILL.md` ## 目标 | 追加 1 行 | INV-1 / INV-2 / INV-3 |
| `code-auto/SKILL.md` §步骤 4 | 步骤 4.b 改写 | INV-1 / INV-2 / INV-3 / INV-10 |
| `templates/plan.md` | 任务类型 + 测试状态字段收窄 | INV-3 |

## 自检(对照 module-conventions.md)

- [x] 命名符合规范(kebab-case 目录 / 中英混排标题)
- [x] 目录位置符合规范(`plugins/<plugin>/skills/<skill>/` 沿用)
- [x] 依赖方向未违反规范(均为单向 `code-plan` → `code-it` / `code-unit` / `code-auto`,无循环)
- [x] 无被禁止的模式(本仓库无"禁止"列表)
- [x] 资源文件放 templates/ 子目录(`templates/plan.md` 沿用)
