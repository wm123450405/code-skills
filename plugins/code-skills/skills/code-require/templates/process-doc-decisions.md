# 过程文档决策记录模板 — code-require

> 本文件是 `code-require` 技能"过程文档自适应生成"的决策记录文件模板。
> **仅当本轮有"不生成"判定时才生成本文件**(沿用 FR-2 强约束,避免反向增加 token)。
> 本仓库中本文件不直接被复制;`code-require` 启动时按本模板的章节结构动态生成。
> 实际生成的文件位于 `./assistants/<版本号>/require/<需求编码>/process-doc-decisions.md`。

---

# 过程文档决策记录 — <需求编码> · code-require

- 需求编码:<REQ-NNNNN>
- 所属版本:<版本号>
- 时间:YYYY-MM-DD HH:mm
- 技能:code-require

## 决策结果

| 过程文档 | 决策 | 理由(引用 §6.1 准则) |
| --- | --- | --- |
| `materials-index.md` | 生成 / 不生成 | <判定理由> |
| `clarifications.md` | 生成 / 不生成 | <判定理由> |
| `related-requirements.md` | 生成 / 不生成 | <判定理由> |
| `analysis-notes.md` | 生成 / 不生成 | <判定理由> |
| 看板"变更记录" | 生成 / 不生成 | <判定理由> |

## 已生成的过程文档清单

- `RESULT.md`(主产出物,本需求 1 个)
- `materials-index.md`(若判定为生成)
- `analysis-notes.md`(若判定为生成)
- ...(其他生成的过程文档)

## 变更记录

| 时间 | 事件 | 摘要 |
| --- | --- | --- |
| YYYY-MM-DD HH:mm | 创建 | <需求编码> 过程文档决策记录(共 N 个不生成判定) |
