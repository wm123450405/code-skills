<!-- schema: dashboard-v2 -->
# 版本开发进度看板 — V0.0.6

> 本文件是 `V0.0.6` 版本工作空间的**简化版看板**。schema = dashboard-v2,所有动态状态从 `PROCESS.md` / `PLAN.md` / `BUG.md` / `TASK-N.md` 派生,详见 `plugins/code-skills/skills/code/references/_shared/contracts.md` §1。
> 需求/缺陷创建时追加一行,进度通过 `PROCESS.md` 追踪。

## 文档头

- 版本号:`V0.0.6`
- 创建时间:2026-07-20
- 最近更新:2026-07-22
- 创建人:wangmiao
- 负责人:wangmiao
- 状态:活跃
- 描述:V0.0.6 版本 — 新建版本(基线 V0.0.5,已发布);2026-07-22 就地升级到 dashboard-v2

---

## 需求清单

> 写入方:`code-req`(首次创建需求时追加一行)

| 需求编码 | 标题 | 进度文档 |
| --- | --- | --- |
| REQ-00051 | 主 SKILL.md 拆分 + help 子命令化 | [PROCESS.md](req/REQ-00051/PROCESS.md) |
| REQ-OPT-00001 | code-skills 技能能力优化建议报告 P0+P1 全部 14 项整改 | [PROCESS.md](req/REQ-OPT-00001/PROCESS.md) |
| REQ-OPT-00002 | 技能"不要做"事项整治 + 全技能精简单调 | [PROCESS.md](req/REQ-OPT-00002/PROCESS.md) |

---

## 缺陷清单

> 写入方:`code-fix`(首次创建缺陷时追加一行)

| 缺陷编号 | 标题 | 进度文档 |
| --- | --- | --- |
| BUG-00009 | /code ver 切换版本后未在最后阶段提交代码 | [PROCESS.md](fix/BUG-00009/PROCESS.md) |
| BUG-00010 | req/fix CHECK 阶段建议改/可选改自动应用规则不明确 | [PROCESS.md](fix/BUG-00010/PROCESS.md) |
| BUG-00011 | 技能中残余无意义板块清理(如主 SKILL.md "## 不要做的事"为空板块) | [PROCESS.md](fix/BUG-00011/PROCESS.md) |

---

## 变更记录

> 写入方:所有 `code-*` 技能

| 时间 | 变更类型 | 变更摘要 | 关联项 |
| --- | --- | --- | --- |
| 2026-07-20 | 初始化 | 从 V0.0.5 创建 V0.0.6,基线为已发布的 V0.0.5 | — |
| 2026-07-22 | 看板升级 | 就地升级到 dashboard-v2;删除"统计"行(2 处);状态来源已切到 PROCESS 派生 | REQ-OPT-00001 |

> 看板(本 schema-v2)**不存**任何动态状态列(如 状态 / 优先级 / 测试状态 / 完成时间)。所有动态信息通过 `deriveItemStatus()`(详见 `plugins/code-skills/skills/code/references/_shared/contracts.md` §3)从 `PROCESS.md` 等工作产物派生。
