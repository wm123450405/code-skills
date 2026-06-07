# 模块拆分 — REQ-00022
更新时间:2026-06-07
版本:V0.0.3

## 模块总览

| 模块 | 路径 | 状态 | 职责 | 处理 |
| --- | --- | --- | --- | --- |
| `code-review/SKILL.md` | plugins/code-skills/skills/code-review/SKILL.md | **重命名 + 字面量改** | 技能入口 | `git mv` → `code-check/` + 改 frontmatter + 改 H1 + 改全文 |
| 10 个其他 SKILL.md description | plugins/code-skills/skills/{code-auto,code-design,code-require,code-plan,code-it,code-unit,code-fix,code-publish,code-dashboard,code-version,code-rule}/SKILL.md | **字面量改** | 下游引用 | 改 description 字段 |
| `.claude-plugin/marketplace.json` | .claude-plugin/marketplace.json | **字面量改** | marketplace 清单 | 改 `skills[]` + `keywords[]` + `description` |
| `plugin.json` | plugins/code-skills/.claude-plugin/plugin.json | **字面量改** | plugin 清单 | 改 `keywords[]` + `description` |
| 4 个 README | README.md / README.en.md / plugins/code-skills/README.md / plugins/code-skills/README.en.md | **字面量改** | 仓库级 README | 改全文字面量 |
| CLAUDE.md | CLAUDE.md | **字面量改** | 项目级规则 | 改全文字面量 |
| 13 份项目级规范 | assistants/rules/*.md | **字面量改** | 规范文件 | 改引用字面量 |
| 6 个技能模板 | plugins/code-skills/skills/*/templates/*.md | **字面量改** | 技能模板 | 改引用字面量 |
| V0.0.3 当前激活看板 | assistants/V0.0.3/RESULT.md | **字面量改** | 规范引用 | 改 6 处 |

## 字面量替换矩阵

| 位置 | 数量 |
| --- | --- |
| 技能入口(目录重命名 + SKILL.md 全文) | 1 目录 + 1 文件(~20 处) |
| 10 个其他 SKILL.md description | 10 |
| marketplace.json | ~3 |
| plugin.json | ~2 |
| 4 个 README + 1 个 CLAUDE.md | ~10-20 |
| 13 份项目级规范 | ~5-10 |
| 6 个技能模板 | ~5-10 |
| V0.0.3 当前激活看板 | 6 |
| **总计** | **约 60-90 处字面量** |

## 不追溯模块(本需求 0 改)

- V0.0.0 / V0.0.1 / V0.0.2 全部历史版本内容
- V0.0.3 历史 review 产物 `review/REQ-NNNN/*`
- `migration-mapping.md` L156 "`EXISTING-010` → 代码评审(`code-review`)" 行
- 其他 9 个其他 `code-*` 技能的"## 工作流程" / "## 衔接" / "## 不要做的事" 段
- 11 个 SKILL.md(除 `code-check` 自身)的 frontmatter `name` 字段
