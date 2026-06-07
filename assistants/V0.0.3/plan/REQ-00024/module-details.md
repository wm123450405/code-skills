# 模块详细化 — REQ-00024
更新时间:2026-06-07
版本:V0.0.3

> 本文档是 `code-plan BUG-00001` 阶段的辅助过程文档。详细内容已并入 `plan/REQ-00024/RESULT.md §模块详细化`。本文档作为索引与速查表。

## 模块清单(单一模块)

| 模块 | 路径 | 状态 | 职责 | 对外暴露 | 依赖 |
| --- | --- | --- | --- | --- | --- |
| **code-auto** | `plugins/code_skills/skills/code-auto/SKILL.md` | **修改** | 6 步状态机 + 路径感知判定 | (无 API;内部技能) | 6 子技能 |

## 自检
- 命名:`code-auto` 与目录名 kebab-case 一致
- 目录位置:`plugins/code_skills/skills/code-auto/` ✓
- 依赖方向:仅依赖 6 个子技能(无循环依赖)
- 0 违反 `module-conventions §规则 1`
