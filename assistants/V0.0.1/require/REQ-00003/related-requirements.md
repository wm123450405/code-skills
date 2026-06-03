# 关联需求 — REQ-00003
更新时间:2026-06-03 20:45
版本:V0.0.1

## 扫描范围
- 本版本(V0.0.1):`./assistants/V0.0.1/require/*/RESULT.md`
- 跨版本:`./assistants/*/require/*/RESULT.md`
- 扫描关键词:`code-rule`、`规则`、`规范`、`CLAUDE.md`、`templates/`、`指引`、`占位`、`Type A`、`Type B`、`Type C`

## 扫描结果

### V0.0.1(本版本)
| 关联需求 | 关联点 | 影响 | 备注 |
| --- | --- | --- | --- |
| **REQ-00001**(Marketplace 改名) | 弱 — REQ-00001 涉及 `marketplace.json` 根 `name` 字段;本需求不修改该字段 | 无 | 两需求作用域不重叠 |
| **REQ-00002**(编码格式统一) | 中 — REQ-00002 涉及 `SKILL.md` / `templates/*.md` 的编码格式字面量(REQ-NNNNN 等);本需求**修改** `code-rule` SKILL.md 和 `templates/rule.md`,因此也会触及编码格式 | **建议**:`code-rule` SKILL.md 扩展时,使用 REQ-00002 v2 锁定的新格式(若已落地);本需求的 FR/AC 编号也用 `REQ-00003-NN` 5 位格式 | 详见 V0.0.1/require/REQ-00002/RESULT.md |

### 跨版本
| 关联需求 | 关联点 | 影响 | 备注 |
| --- | --- | --- | --- |
| **V0.0.0 EXISTING-003**(`code-rule` 技能) | 强 — 本需求**扩展** EXISTING-003 定义的 `code-rule` 基线能力;不重写 | 本需求继承 EXISTING-003 的"自然语言 → 结构化规范"核心,扩展为"自然语言 → 3 种目标类型" | EXISTING-003 位于 `assistants/V0.0.0/require/EXISTING-003/RESULT.md` |
| **V0.0.0 EXISTING-NNN**(其它) | 弱 — V0.0.0 的 10 个 `EXISTING-NNN` 中,EXISTING-003 是直接相关;其它 9 个(`code-init` / `code-version` / `code-require` / `code-design` / `code-plan` / `code-it` / `code-unit` / `code-fix` / `code-review`)是 `code-rule` 的"消费方" | 本需求新增的 Type B(CLAUDE.md)与 Type C(模板)会间接影响这 9 个技能的"读"行为;但本需求**不修改**这 9 个技能的 SKILL.md | 需在 `code-rule` 扩展时,确保"消费方"的读路径仍兼容(只是多了"AI 工作约定"与"模板提示"内容,不影响原有结构) |

## 横向关联需求(影响本需求的下游需求)

| 关联需求 | 关联点 | 对本需求的影响 |
| --- | --- | --- |
| **未来的规范填充需求** | 本需求只建 6 个 Type A 分类的脚手架(可能含部分示例);具体规则内容由后续 `code-rule` 调用逐条添加 | 本需求不假设任何具体规范内容;`code-rule` 扩展后,用户在 V0.0.x 任意版本都能调 `code-rule` 填充 |
| **未来 `code-rule` 升级** | 本需求扩展 `code-rule` SKILL.md;未来如需再加 Type D / E / ...,只需追加"类型定义"文件 | 本需求为 NFR-2(可扩展性)留下接口 |

## 关联规范(在 `code-design` 阶段详细分析)

| 关联规范 | 关联 |
| --- | --- |
| `skill-conventions.md §规则 1`(SKILL.md frontmatter 必含 `name` + `description`) | 本需求修改 `code-rule` SKILL.md 时,必须保留 frontmatter;只改正文 |
| `module-conventions.md §规则 1`(资源放固定子目录) | 本需求新增 Type A 分类文件时,必须放 `./assistants/rules/`;Type C 模板提示必须放 `plugins/code-skills/skills/<技能>/templates/` |
| `dashboard-conventions.md §规则 1`(看板字段约定扩展需三处同步) | 本需求不触发(本需求不改看板字段) |
| `doc-conventions.md §规则 1`(中英同次提交) | 本需求修改 `code-rule` SKILL.md 时,若加英文版,需中英同步;但本仓库当前无 `code-rule` 英文 SKILL.md,本需求不强制新建 |
| `marketplace-protocol.md §规则 1` | 本需求不修改 `marketplace.json` / `plugin.json` |

## 无关联确认
- 本需求**不涉及任何应用代码模块**(本仓库无应用代码)
- 本需求**不涉及任何对外 API / 数据模型 / 部署形态**
