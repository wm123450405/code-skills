# 关联设计 — REQ-00022
更新时间:2026-06-07
版本:V0.0.3

## 本版本(V0.0.3)
- **REQ-00020**:架构设计目标重新归位 + 3 新维度(本需求 0 涉及)
- **REQ-00021**:优化 3 技能 --result / --plan 模板参数(本需求 0 涉及)

## 跨版本(V0.0.2)
- **REQ-00007**:`code-auto` 自动开发 — `code-auto/SKILL.md` 同步改(FR-3)
- **REQ-00013**:屏显"编号+标题" — 屏显格式契约沿用
- **REQ-00017**:0 派生"更新看板"任务 — INV-6 沿用
- **REQ-00019**:BUG 模式同构 — BUG 路径评审仍走 `review/` 目录

## 关键引用方(本需求必须同步改)

| 引用方 | 路径 | 字面量出现位置 | 处理 |
| --- | --- | --- | --- |
| `code-review/SKILL.md` | plugins/code-skills/skills/code-review/SKILL.md | 全文(frontmatter + H1 + 引用) | **git mv** + 改 frontmatter + 改 H1 + 改全文 |
| 10 个其他 SKILL.md | plugins/code-skills/skills/{auto,design,require,plan,it,unit,fix,publish,dashboard,version,rule}/SKILL.md | description 字段 | 改字面量 |
| marketplace.json | .claude-plugin/marketplace.json | L17 + L25 + L40 | 改字面量 |
| plugin.json | plugins/code-skills/.claude-plugin/plugin.json | L17 + description | 改字面量 |
| 4 个 README + CLAUDE.md | README*.md + plugins/code-skills/README*.md + CLAUDE.md | 全文 | 改字面量 |
| 13 份项目级规范 | assistants/rules/*.md | 引用字面量 | 改字面量 |
| 6 个技能模板 | plugins/code-skills/skills/*/templates/*.md | 引用字面量 | 改字面量 |
| V0.0.3 当前激活看板 | assistants/V0.0.3/RESULT.md | L98 / L122 / L136 / L166 / L217 / L218 | 改字面量 |

## 不追溯(本需求 0 改)
- V0.0.0 / V0.0.1 / V0.0.2 全部历史版本内容
- V0.0.3 历史 review 产物 `review/REQ-NNNN/*`
- `migration-mapping.md` L156"`EXISTING-010` → 代码评审(`code-review`)"行
