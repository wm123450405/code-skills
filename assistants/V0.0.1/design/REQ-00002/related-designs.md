# 关联设计 — REQ-00002
更新时间:2026-06-03 20:25
版本:V0.0.1

## 扫描范围
- 本版本(V0.0.1):`./assistants/V0.0.1/design/*/RESULT.md`
- 跨版本(可选):`./assistants/*/design/*/RESULT.md`
- 扫描关键词:`marketplace`、`name`、`install`、`plugin`、`REQ-`、`TASK-`、`BUG-`、`编码`、`格式`

## 扫描结果

### V0.0.1(本版本)
| 关联设计 | 关联点 | 影响 | 备注 |
| --- | --- | --- | --- |
| [design/REQ-00001/RESULT.md](REQ-00001/RESULT.md)(Marketplace 根名称添加 `-marketplace` 后缀) | 弱耦合 — 两个需求的"修改文件集"无重叠;REQ-00001 改 marketplace.json + 2 README + CLAUDE.md(本需求);REQ-00002 改 10 SKILL.md + 20+ 模板 + 3 文档 + 1 看板模板。**仅在 README 与 CLAUDE.md 处有交集**:REQ-00001 改 marketplace name 引用,REQ-00002 改编码格式引用;两个需求的修改可能在同一文件不同行,需协调 `code-it` 阶段的子任务边界 | 弱(只读) | 已在 V0.0.1/RESULT.md 看板同步,均为"已完成"状态;本设计不重复 |

### 跨版本
| 关联设计 | 关联点 | 影响 | 备注 |
| --- | --- | --- | --- |
| (无 V0.0.0 概要设计) | — | — | V0.0.0 仅 `require/EXISTING-NNN/`,无 `design/` 子目录 |

## 横向关联需求(影响本设计的下游需求)

| 关联需求 | 关联点 | 对本设计的影响 |
| --- | --- | --- |
| **REQ-00001**(Marketplace 改名,原 REQ-2026-0001) | 本需求 FR-6 部分已提前落地(目录 + 本工作空间引用);两需求实施顺序见 `require/REQ-00002/related-requirements.md` | **中**:两个需求都改 `plugins/code-skills/README.md` + `README.en.md` + `CLAUDE.md`,但**改的内容维度不同**(REQ-00001 = install 命令中的 marketplace name;REQ-00002 = 编码格式);若两需求均在 `code-it` 阶段实施,需协调子任务边界 |
| **EXISTING-001 ~ EXISTING-010**(V0.0.0) | 10 个技能的"现有功能"基线;本需求横切影响这 10 个技能的 SKILL.md(本仓库内全部 10 个技能) | **强**(若 Q-6 = H2);**零**(若 Q-6 = H1) |

## 关联规范(已在 `rule-compliance.md` 中详细分析)

| 规范 | 关联 |
| --- | --- |
| `doc-conventions.md §规则 1` | README 中英结构对仗 + 同次提交同步(本需求强触发) |
| `doc-conventions.md §规则 2` | README 中命令/路径必须反映仓库实际状态(本需求强触发) |
| `dashboard-conventions.md §规则 1` | 看板字段约定扩展需多文件同步(本需求**条件不触发** — 仅改示例值,不改字段语义) |
| `skill-conventions.md §规则 1` | SKILL.md frontmatter 必含 `name` + `description` 且 `name` 与目录一致(本需求不改 frontmatter) |
| `module-conventions.md §规则 1` | 技能资源放固定子目录(本需求不创建新资源) |
| `marketplace-protocol.md §规则 1` | marketplace.json / plugin.json 字段约束(本需求不触发) |

## 无关联确认

- 本设计不涉及任何**应用代码模块** → 无 `module-breakdown.md` 维度的"复用既有模块 / 扩展既有模块"
- 本设计不涉及任何**对外 API** → 无 `api-standards` 维度的契约变更
- 本设计不涉及任何**数据模型** → 无 `data-modeling` 维度的实体变更
- 本设计不涉及任何**部署形态** → 本仓库是"纯文档/清单/SKILL.md 集合",无部署概念
