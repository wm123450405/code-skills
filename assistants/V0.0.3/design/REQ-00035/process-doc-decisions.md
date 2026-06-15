# 过程文档决策记录 — REQ-00035 · code-design

版本:V0.0.3
时间:2026-06-15 19:05
技能:code-design
上游:code-require(REQ-00035 需求分析完成,8 FR / 9 NFR / 22 AC)

## 设计目标(沿用 code-auto 默认 --balanced)

- 整体设计目标:`--balanced`
- 功能性:中(本需求为"过程文档生成逻辑改造",属元技能改类,与"功能正确性"直接相关度低)
- 扩展性:不触发(`./assistants/V0.0.3/require/REQ-00035/process-doc-decisions.md` 不存在"待评估三方依赖"清单;模块数 ≥ 3 但本需求**不**改"对外暴露的接口",仅改"过程文档生成约定")
- 0 问路(code-auto 上下文 0 问,沿用 REQ-00020 步骤 0b.0)

## 决策结果

| 过程文档 | 决策 | 理由(引用 §6.2 准则) |
| --- | --- | --- |
| `materials-index.md` | 生成 | 始终生成(§6.2 强制) |
| `design-notes.md` | 生成 | 始终生成(§6.2 强制) |
| `module-breakdown.md` | 生成 | 模块数 ≥ 2(本设计涉及 5 主流程技能 + 1 编排 + 1 dashboard,共 7 个改写模块)— §6.2 准则 |
| `dependencies.md` | 不生成 | 无外部依赖(改既有 SKILL.md / 模板 / 规范引用,无新增三方依赖)— §6.2 准则 |
| `related-designs.md` | 生成 | 5 个关联设计(REQ-00020 / REQ-00030 / REQ-00031 / REQ-00032 / REQ-00034)≥ 1 — §6.2 准则 |
| `rule-compliance.md` | 生成 | `./assistants/rules/` 存在且有内容(7 个规范文件)— §6.2 准则 |
| `clarifications.md` | 不生成 | 本轮无用户问路(§6.2 准则) |
| 看板"变更记录" | 生成 | 本轮有 `RESULT.md` 写入 + 概要设计清单追加(§6.2 看板) |

## 已生成的过程文档清单

- `RESULT.md`(主产出物,本设计 1 个)
- `materials-index.md`
- `design-notes.md`
- `module-breakdown.md`
- `related-designs.md`
- `rule-compliance.md`

## 变更记录

| 时间 | 事件 | 摘要 |
| --- | --- | --- |
| 2026-06-15 19:05 | 创建 | REQ-00035 过程文档决策记录(共 2 个不生成判定:`dependencies.md` / `clarifications.md`) |
