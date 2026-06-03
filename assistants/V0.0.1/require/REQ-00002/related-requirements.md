# 关联需求 — REQ-00002

## 扫描范围
- 本版本(V0.0.1):`./assistants/V0.0.1/require/*/RESULT.md`
- 基线版本(V0.0.0):`./assistants/V0.0.0/require/*/RESULT.md`
- 扫描关键词:`REQ-YYYY`、`REQ-NNNN`、`BUG-NNN`、`<任务编码>`、`<任务序号>`、`<需求编号>`、`<缺陷编号>`、`编码`、`编号`

## 扫描结果

### V0.0.1
| 关联需求 | 关联点 | 影响 | 备注 |
| --- | --- | --- | --- |
| REQ-00001(Marketplace 根名称添加 `-marketplace` 后缀,原 REQ-2026-0001) | 本需求 FR-6 部分已提前落地:目录 `REQ-2026-0001/` → `REQ-00001/`、本工作空间引用同步;后续 REQ-00001 的 `code-design`/`code-plan`/`code-it` 阶段将直接使用新编码,不再受"何时重命名"问题困扰 | 强(下游同步) | REQ-00001 当前需求分析阶段已完成,下游(design/plan/it/review)尚未启动 — 现在重命名最廉价;由于重命名已发生,原"先后顺序"顾虑部分消解 |

### V0.0.0(基线)
| 关联需求 | 关联点 | 影响 | 备注 |
| --- | --- | --- | --- |
| EXISTING-001(code-init) | code-init 是产生 EXISTING- 编码的源头;若 EXISTING- 也要重命名,code-init 行为需评估 | 中(取决于 Q-6 决策) | code-init SKILL.md 第 7-8 步显式生成 `require/EXISTING-NNN/` —— 若决定改为 REQ-NNNNN,SKILL.md 需同步 |
| EXISTING-002(code-version) | 不直接维护编码,但版本看板含"需求清单"的需求编码字段 | 弱 | 模板 `version-RESULT.md` 含编码示例,需同步 |
| EXISTING-003(code-rule) | 若新建 `encoding-conventions.md`(Q-8 决策),由 code-rule 维护 | 弱 | 取决于 Q-8 |
| EXISTING-004(code-require) | SKILL.md 含"需求编码"概念、建议 `REQ-YYYY-NNNN` 格式 | 强 | SKILL.md 与 `templates/requirements.md` 均需同步,本需求即由该技能产出 |
| EXISTING-005(code-design) | SKILL.md / templates/design.md 含编码示例 | 中 | 同步 |
| EXISTING-006(code-plan) | SKILL.md / templates/plan.md / templates/task-plan.md 含编码与任务编号生成规则 | 强 | 若 Q-7 决定 TASK 改全局计数,code-plan 的"任务编号分配逻辑"需调整 |
| EXISTING-007(code-it) | SKILL.md 含 regex `^REQ-\d{4}-\d{4}-\d{3}$`、"任务编码 = 需求编码 + -序号"等硬编码 | 强 | regex 与拆分逻辑都要改;若 Q-7 选全局计数,父子拆分逻辑改为"查 PLAN.md 反查所属需求" |
| EXISTING-008(code-unit) | SKILL.md 含"任务编码"格式 `<需求编号>-<任务序号>` | 强 | 同 code-it |
| EXISTING-009(code-fix) | SKILL.md / templates/fix-registry.md 含 BUG-NNN(3 位)格式 | 强 | 需改为 BUG-NNNNN(5 位) |
| EXISTING-010(code-review) | SKILL.md / templates 含派生任务编码(基于父任务) | 中 | 派生任务编码生成规则需重审(取决于 Q-7) |

> 结论:本需求是**横切整个 code-* 技能集**的协议变更,与 V0.0.0 全部 10 条 EXISTING- 需求(对应 10 个技能)均强相关。

## 与 REQ-00001(原 REQ-2026-0001)的实施顺序建议
> 两个需求同时活跃,需明确顺序避免重复工作:

**已发生(2026-06-03 20:20)**:
- ✅ 目录重命名 `REQ-2026-0001/` → `REQ-00001/` 已完成(本工作空间维度)
- ✅ V0.0.1 看板"需求清单"已使用 `REQ-00001`

**当前推荐顺序**:
1. **继续推进 REQ-00001 下游**(design → plan → it → unit → review)— 直接使用新编码 `REQ-00001`
2. **再实施 REQ-00002**(`code-it` 阶段):批量改 SKILL.md / 模板 / README / CLAUDE.md 中的旧编码

**理由(更新)**:
- 重命名已发生,原"先 REQ-2026-0001 跑全下游再重命名"的论证已部分失效(目录已是新名字)
- 现风险:REQ-00001 下游产出物(design/plan/code/test/review)将全程使用新编码 `REQ-00001` 与任务路径 `REQ-00001-NN`(旧格式,因 REQ-00002 的 TASK 格式变更未实施);这些路径在 REQ-00002 `code-it` 阶段清理 SKILL.md 时,可能需要再补一次批量重命名(成本仍可控,因为是局部维度)
- 若仍坚持等 REQ-00002 完整实施后再启动 REQ-00001 下游,会损失本次提前重命名带来的"目录维度清晰"收益

> 最终顺序由用户决定,本结论作为推荐;若选择"等 REQ-00002 完整实施后再启动 REQ-00001 下游",请明示

## 关联规范(强制约束,只读)
| 规范文件 | 关联条款 | 对本需求的影响 |
| --- | --- | --- |
| `./assistants/rules/marketplace-protocol.md §规则 1` | marketplace.json / plugin.json 字段约束 | 不触发(本需求不改协议清单字段) |
| `./assistants/rules/doc-conventions.md §规则 1` | README 中英文必须结构对仗,同次提交同步 | **强触发**:README.md / README.en.md 内所有 REQ-YYYY-NNNN / BUG-NNN 示例必须同步 |
| `./assistants/rules/doc-conventions.md §规则 2` | README 持续维护,所有命令路径与仓库实际一致 | **强触发**:README 中编码格式示例必须反映新规则;不留旧格式残留 |
| `./assistants/rules/dashboard-conventions.md §规则 1` | 看板字段约定扩展需多文件同步(模板 + CLAUDE.md + 本规范) | **可能触发**:若版本看板"需求清单 / 任务清单 / 缺陷清单"模板含编码示例值或字段语义说明,改动需同步三处 |
| `./assistants/rules/skill-conventions.md §规则 1` | SKILL.md frontmatter 必含 `name` + `description` 且 `name` 与目录一致 | 不触发(本需求只改 SKILL.md 正文与示例,不改 frontmatter) |
| `./assistants/rules/module-conventions.md §规则 1` | 技能资源放固定子目录(templates / checklists / guidelines) | 不触发 |

## 派生项(可能产生的新规则)
- 若 Q-8 选 (a),将由 `code-rule` 新建 `./assistants/rules/encoding-conventions.md`(本需求范围:仅记录"将由 code-rule 在实施阶段创建",本需求**不**直接写入 rules/)
