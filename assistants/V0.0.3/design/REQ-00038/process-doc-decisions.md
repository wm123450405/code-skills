# 过程文档决策记录 — REQ-00038

更新时间:2026-06-22 13:30
版本:V0.0.3

> 本文件由 `code-design` 步骤 0 末尾"过程文档自适应判定"段产出;按 `## 适用过程文档清单` 字面执行。

## 决策汇总(7 项)

| 序号 | 过程文档 | 决策 | 理由 |
| --- | --- | --- | --- |
| 1 | `materials-index.md` | 生成 | 项目级规范登记是核心;本需求消费 8 个规范文件 |
| 2 | `design-notes.md` | 生成 | 设计权衡笔记是核心;本需求 8 决策 + 8 问题清单 |
| 3 | `module-breakdown.md` | 生成 | 模块数 = 1 主改造 + 1 模板改造 + 1 文档字面改写 = 3 项 ≥ 2 阈值 |
| 4 | `dependencies.md` | **不生成** | 0 新增三方依赖(只读 monorepo 声明文件,无新增 npm / pip / cargo 等依赖) |
| 5 | `related-designs.md` | 生成 | 关联 REQ-00034(7 项守卫字节级沿用)≥ 1 |
| 6 | `rule-compliance.md` | 生成 | `./assistants/rules/` 存在且有内容(13 个规范文件) |
| 7 | `clarifications.md` | 生成 | 本轮 1 个 `AskUserQuestion` 问路 |
| 8 | 看板"变更记录" | 生成 | 本轮有追加(概要设计清单新增 1 行 + 变更记录新增 1 条) |

## 不生成原因详述

### `dependencies.md`(决策 4)

- 本需求**不**引入新三方依赖:
 - 模块识别 = 只读 monorepo 声明文件(pnpm-workspace.yaml / package.json#workspaces / pom.xml#modules / Cargo.toml#workspace.members / go.mod / lerna.json / nx.json / turbo.json)→ 0 新增 IO 库依赖
 - 7 项守卫 = 沿用既有 `Glob` + `Read` 工具调用 → 0 新增工具依赖
 - 模板追加小节 = 0 模板新增 / 0 工具新增
- 沿用 `code-design` 适用清单判定:"依赖其他模块/服务/中间件 ≥ 1 个 → 生成;无外部依赖(自含/单文件)→ 不生成"

## 决策触发器

- 本文件**仅**在 `decisions` 存在"不生成"时生成
- 本轮触发原因:决策 4(`dependencies.md`)= 不生成 → 写本文件记录"为何不生成"