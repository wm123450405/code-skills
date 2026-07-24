<!-- schema: dashboard-v2 -->
# 版本开发进度看板 — <V>

> 本文件是 `<V>` 版本工作空间的**简化版看板**。schema = dashboard-v2,所有动态状态从 `PROCESS.md` / `PLAN.md` / `BUG.md` / `TASK-N.md` 派生,详见 `references/_shared/contracts.md`「RESULT.md schema(`dashboard-v2`)」。
> 需求/缺陷创建时追加一行,进度通过 `PROCESS.md` 追踪。

## 文档头

- 版本号:`<V>`
- 创建时间:YYYY-MM-DD HH:mm
- 最近更新:YYYY-MM-DD HH:mm
- 创建人:<name>
- 负责人:<name>
- 状态:活跃
- 描述:<一行描述>

---

## 需求清单

> 写入方:`code-req`(首次创建需求时追加一行)

| 需求编码 | 标题 | 进度文档 |
| --- | --- | --- |
| REQ-NNNNN | <标题> | [PROCESS.md](req/REQ-NNNNN/PROCESS.md) |

---

## 缺陷清单

> 写入方:`code-fix`(首次创建缺陷时追加一行)

| 缺陷编号 | 标题 | 进度文档 |
| --- | --- | --- |
| BUG-NNNNN | <标题> | [PROCESS.md](fix/BUG-NNNNN/PROCESS.md) |

---

## 变更记录

> 写入方:所有 `code-*` 技能

| 时间 | 变更类型 | 变更摘要 | 关联项 |
| --- | --- | --- | --- |
| YYYY-MM-DD HH:mm | 初始化 | 从基线版本创建 <V> | — |

> 看板(本 schema-v2)**不存**任何动态状态列(如 状态 / 优先级 / 测试状态 / 完成时间)。所有动态信息通过 `deriveItemStatus()`(详见 `references/_shared/contracts.md`「看板派生接口」)从 `PROCESS.md` 等工作产物派生。
