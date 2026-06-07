# 模块拆分 — REQ-00024
更新时间:2026-06-07
版本:V0.0.3

## 模块清单

| 模块 | 路径 | 状态 | 职责 | 对外暴露 | 依赖 |
| --- | --- | --- | --- | --- | --- |
| **code-auto** | `plugins/code-skills/skills/code-auto/SKILL.md` | **修改** | 6 步状态机 + 路径感知判定 | (无 API;内部技能) | code-require / code-design / code-plan / code-it / code-unit / code-check |
| code-fix | `plugins/code-skills/skills/code-fix/SKILL.md` | 不修改 | (本需求边界外) | — | — |
| code-init / code-version / code-rule / code-publish | 4 个 | 不修改 | (与编号格式无关) | — | — |
| code-require / code-design / code-plan / code-it / code-unit / code-check / code-dashboard | 7 个 | 不修改 | (NFR 强约束) | — | — |

## 自检(沿用 module-conventions §规则 1)

- **命名**:所有 14 个 `code-*` 模块均符合 `kebab-case` 命名规范
- **目录位置**:均在 `plugins/code-skills/skills/<name>/` 下
- **依赖方向**:`code-auto` 依赖 6 个子技能;子技能之间无相互依赖
- **禁止模式**:**0 违反**(无循环依赖,无跨层调用)
