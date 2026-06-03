# 关联需求 — REQ-00001
(2026-06-03 20:20 标题同步;原 REQ-2026-0001,已重命名;正文未含旧编码)

## 扫描范围
- 本版本(V0.0.1):`./assistants/V0.0.1/require/*/RESULT.md` — 当前为空(本需求是 V0.0.1 首个需求)
- 基线版本(V0.0.0):`./assistants/V0.0.0/require/EXISTING-001 ~ EXISTING-010/RESULT.md`
- 扫描关键词:`marketplace`、`marketplace.json`、`plugin.json`、`code-skills`、`插件名`、`仓库名`

## 扫描结果

### V0.0.1
| 关联需求 | 关联点 | 影响 |
| --- | --- | --- |
| — | 无其它需求 | — |

### V0.0.0(基线)
| 关联需求 | 关联点 | 影响 | 备注 |
| --- | --- | --- | --- |
| EXISTING-001(code-init) | code-init 在生成基线时会读 / 引用仓库结构,但不直接写入 marketplace.json | 无 | code-init 不维护 marketplace 协议清单,本需求不影响其行为 |
| EXISTING-002(code-version) | 创建 `./assistants/<版本号>/`,与 marketplace 协议清单解耦 | 无 | 版本工作空间与插件市场清单是两条互不影响的轨道 |
| EXISTING-003(code-rule) | `code-rule` 维护 `./assistants/rules/marketplace-protocol.md`,但规则文件本身不引用具体 marketplace name | 弱(规则未硬编码 name 值,改名后规则示例可继续使用 `code-skills` 仅作示例) | 若用户希望规则示例同步使用新名,后续可单独发起新需求(本次范围之外) |

> 结论:本需求与 V0.0.0 基线全部 EXISTING-NNN 均**无强耦合**,无需在本次实施中变更任何 EXISTING-NNN 的 RESULT.md。

## 关联规范(强制约束,只读)
| 规范文件 | 关联条款 | 对本需求的影响 |
| --- | --- | --- |
| `./assistants/rules/marketplace-protocol.md §规则 1` | `$schema/name/version` 必填;`plugins[].name` 必须与子插件 `plugin.json` 的 `name` 一致;不允许未知字段 | 改根 `name` 后,**禁止**顺手改 `plugins[].name`,否则会与 `plugin.json` 失配,触发规则违规;`$schema`/`version` 保持原值 |
| `./assistants/rules/doc-conventions.md §规则 1` | README 多语言版本必须保持结构对仗,改一边同步另一边 | README.md 与 README.en.md 必须**同次提交**完成 install 命令同步,任何漂移触发规则违规 |
| `./assistants/rules/doc-conventions.md §规则 2` | README 中命令/路径必须与仓库实际状态一致 | 改名后老 install 命令在 README 中会"指向不存在的 marketplace name",必须同步更新 |
| `./assistants/rules/dashboard-conventions.md §规则 1` | 看板字段约定扩展需多文件同步(模板 + CLAUDE.md + 本规范) | 本需求不修改看板字段约定,**不触发**本规则 |
| `./assistants/rules/skill-conventions.md §规则 1` | SKILL.md 的 `name` 与目录名一致 | 本需求不修改任何 SKILL.md,**不触发**本规则 |
| `./assistants/rules/module-conventions.md §规则 1` | 技能资源放在固定子目录 | 本需求不修改技能资源,**不触发**本规则 |
