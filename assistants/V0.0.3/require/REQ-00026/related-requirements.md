# 关联需求 — REQ-00026

## 排查结论

通过 `Grep` 扫描 `./assistants/V0.0.3/require/*/RESULT.md`,**未发现**既有需求与"技能通用化"强关联:

| 旧需求 | 与本需求的关系 | 处理 |
| --- | --- | --- |
| REQ-00020(看板 ASCII 化)| 无关 | 不引用 |
| REQ-00021(REQ/BUG 双格式)| 无关 | 不引用 |
| REQ-00022(`code-review` → `code-check` 重命名)| 仅历史引用过 `plugins/code-skills/...` 路径(在"不变量"章节中,属正确用法)| 不引用;旧需求 RESULT.md 保留具体路径是可追溯证据 |
| REQ-00023(看板算法 4 兼容)| 无关 | 不引用 |
| REQ-00024(`code-auto` 移除 `from`)| 仅历史引用过 `plugins/code-skills/...` 路径(在"不变量" + "验收步骤"中)| 不引用;同上 |
| REQ-00025(无值字面校正)| 仅历史引用过 `plugins/code-skills/...` 路径(在"验收步骤"中)| 不引用;同上 |

## 旧需求中"看起来强关联但实际是正确用法"的引用范式

旧需求在以下场景使用 `plugins/code-skills/...` 路径,**均属正确用法,本需求不波及**:

1. **不变量章节**(如"不修改 `plugins/code-skills/.claude-plugin/plugin.json`")—— 这是项目级硬约束,字面路径是证据,必须保留。
2. **验收步骤的 `git diff` 命令**(如 `git diff plugins/code-skills/skills/*/SKILL.md`)—— 这是具体的可执行 shell 命令,字面路径是命令的一部分,必须保留。
3. **历史变更记录** —— 任何已 commit 的需求档案,字面都不可改(改了反而破坏可追溯)。

## 待澄清的边界

本需求关注"10 个 SKILL.md 的描述性文字",与"需求档案(旧 RESULT.md)"**不应混为一谈**。具体边界见 `clarifications.md` 的 Q1 / Q2。
