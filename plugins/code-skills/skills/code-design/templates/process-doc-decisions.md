# 过程文档决策记录模板 — code-design

> 本文件是 `code-design` 技能"过程文档自适应生成"的决策记录文件模板。
> **仅当本轮有"不生成"判定时才生成本文件**(沿用 FR-2 强约束)。
> 实际生成的文件位于 `./assistants/<版本号>/design/<需求编码>/process-doc-decisions.md`。

---

# 过程文档决策记录 — <需求编码> · code-design

- 需求编码:<REQ-NNNNN>
- 所属版本:<版本号>
- 时间:YYYY-MM-DD HH:mm
- 技能:code-design

## 设计目标(沿用 --balanced / 沿用上游 / code-auto 默认)

- 整体设计目标:`--minimal` / `--balanced` / `--extensible`
- 维度优先级:
 - 功能性:<高/中/低>
- code-auto 上下文:0 问路

## 决策结果

| 过程文档 | 决策 | 理由(引用 §6.2 准则) |
| --- | --- | --- |
| `materials-index.md` | 生成 / 不生成 | <判定理由> |
| `design-notes.md` | 生成 / 不生成 | <判定理由> |
| `module-breakdown.md` | 生成 / 不生成 | <判定理由> |
| `dependencies.md` | 生成 / 不生成 | <判定理由> |
| `related-designs.md` | 生成 / 不生成 | <判定理由> |
| `rule-compliance.md` | 生成 / 不生成 | <判定理由> |
| `clarifications.md` | 生成 / 不生成 | <判定理由> |
| 看板"变更记录" | 生成 / 不生成 | <判定理由> |

## 已生成的过程文档清单

- `RESULT.md`(主产出物,本设计 1 个)
- ...(其他生成的过程文档)

## 变更记录

| 时间 | 事件 | 摘要 |
| --- | --- | --- |
| YYYY-MM-DD HH:mm | 创建 | <需求编码> 过程文档决策记录(共 N 个不生成判定) |
