# 模块拆分 — REQ-00025
更新时间:2026-06-07
版本:V0.0.3

## 模块清单(9 文件改动)

| 模块 | 路径 | 状态 | 改动类型 |
| --- | --- | --- | --- |
| **encoding-conventions.md** | `./assistants/rules/encoding-conventions.md` | **修改** | §规则 1/2/4 软化 + 新增 §规则 1.5 |
| code-require/SKILL.md | `plugins/code-skills/skills/code-require/SKILL.md` | 修改 | 步骤 1 编码格式 + 工具使用约定 |
| code-design/SKILL.md | `plugins/code-skills/skills/code-design/SKILL.md` | 修改 | 步骤 2 + 步骤 3 校验放宽 |
| code-plan/SKILL.md | `plugins/code-skills/skills/code-plan/SKILL.md` | 修改 | 步骤 2 / 步骤 9B / §步骤 10A |
| code-it/SKILL.md | `plugins/code-skills/skills/code-it/SKILL.md` | 修改 | 步骤 1 / 步骤 7 |
| code-unit/SKILL.md | `plugins/code-skills/skills/code-unit/SKILL.md` | 修改 | 步骤 2 校验放宽 |
| code-check/SKILL.md | `plugins/code-skills/skills/code-check/SKILL.md` | 修改 | 步骤 2 解析放宽 |
| code-fix/SKILL.md | `plugins/code-skills/skills/code-fix/SKILL.md` | 修改 | 步骤 1 解析放宽 |
| code-dashboard/SKILL.md | `plugins/code-skills/skills/code-dashboard/SKILL.md` | 修改 | 算法 4 解析放宽 |

## 不修改清单(5 文件)
- code-init/SKILL.md / code-version/SKILL.md / code-rule/SKILL.md / code-publish/SKILL.md / code-auto/SKILL.md
- **理由**:与编号格式无关(已识别 BUG-00001 修复完后 `code-auto` SKILL.md 仍是 v2 模式 B + 退出码 5,本需求 0 触发其改造)

## 自检(沿用 module-conventions §规则 1)
- 命名:所有 9 个文件均符合 kebab-case
- 目录位置:均在 `plugins/code-skills/skills/<name>/` 或 `./assistants/rules/`
- 依赖方向:8 个 SKILL.md 之间无相互依赖
- 0 违反
