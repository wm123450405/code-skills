# 关联设计 — REQ-00008
更新时间:2026-06-05 15:55
版本:V0.0.2
需求编码:REQ-00008
设计标题:`/code-review` 整版本模式(无参评审)

---

## 1. 扫描范围

- 同版本 `./assistants/V0.0.2/design/`:REQ-00004 / REQ-00005 / REQ-00006 / REQ-00007 / REQ-00014(共 5 个既有 design 文档)
- 跨版本 `./assistants/V0.0.1/design/`:REQ-00001 / REQ-00002 / REQ-00003(共 3 个历史 design 文档)
- 直接相关:历史 `code-review` 产物 `./assistants/V0.0.1/review/REQ-0000{1,2,3}/REVIEW-REPORT.md`

## 2. 关联设计清单(模块交集 / 接口约定)

| 关联 design | 版本 | 关联点 | 对本设计的影响 |
| --- | --- | --- | --- |
| **REQ-00004 design**(`code-dashboard`) | V0.0.2 | 整版本模式过滤"已完成"需求 → 数据源 = `RESULT.md` 需求清单;解析锚点 = `^## 需求清单` + `^\| REQ-\d{5} \|`;**完全复用** `code-dashboard` 算法 1 区段解析 | 整版本模式**沿用** `code-dashboard` 解析口径,与看板 3 区段数据源严格一致(NFR-8) |
| **REQ-00006 design**(`code-publish`) | V0.0.2 | `code-publish` 前置检查 = "全版本已解决"是看板层判定;**不**触发代码层全版本评审;整版本模式**不**被 `code-publish` 调用 | 整版本模式是"发布前最后一次评审"的工具(用户角色 R-1),但**不**嵌入 `code-publish` 流程(沿用既有边界) |
| **REQ-00007 design**(`code-auto`) | V0.0.2 | `code-auto` 评审循环**继续**用模式 1;整版本模式由用户手动调 | **NFR-4 强约束**:`code-auto` 内部消费模式 1 的 `REVIEW-REPORT.md` 解析逻辑(FR-6.AC-6.2 强保证);整版本模式**不**被 `code-auto` 调用 |
| **REQ-00005 design**(首步拉取+末步提交) | V0.0.2 | 改写范围**不**含 `code-review`;`code-review` **不**引入"首步拉取+末步提交" | **NFR-5 强约束**:本设计**不**触发 REQ-00005 扩展到 `code-review`(留作 follow-up,Q-8 派生任务预警) |
| **REQ-00014 design**(`code-plan` 任务拆分维度) | V0.0.2 | `code-plan` 拆任务时已扩展为"按功能点拆" + 架构任务;`code-review` 派生任务的"必须改"可触发 `code-plan` 重跑 | 整版本模式的派生任务追加到 `PLAN.md` 任务总览(沿用既有逻辑,无新增关联) |
| **REQ-00001 design**(V0.0.1) | V0.0.1 | 模式 1 既有行为 + V0.0.1 `code-review` 评审产物(`review/REQ-00001/REVIEW-REPORT.md`) | **INV-1 / INV-2** 自检用(整版本模式生成的 `REVIEW-REPORT.md` 与模式 1 既有产物字面 100% 一致) |
| **REQ-00002 design**(V0.0.1) | V0.0.1 | `encoding-conventions.md` 编码规范 + 3 类编码权威源 | `code-review` 派生任务追加 `TASK-` 编码沿用规范(本设计**不**重新定义) |
| **REQ-00003 design**(`code-rule` 优化) | V0.0.1 | `code-rule` 维护项目级规范;`code-review` 评审清单的权威源是 `./assistants/rules/` | 本设计**不**主动写 `review-conventions.md`(留作 follow-up,Q-8 派生任务预警) |

## 3. 关键结论

1. **0 修改其他 design**:本设计**不**影响上述 8 个 design 的章节与决策
2. **0 依赖反向影响**:本设计的"完全复用模式 1"决策**不**触发其他 design 的更新
3. **整版本模式是 `code-auto` 的"伴生技能"**:两者正交 — `code-auto` 内部继续用模式 1,模式 2 由用户手动调(整版本"全版本最后一次评审"场景)
4. **看板解析口径严格沿用 `code-dashboard`**:与既有 V0.0.2 看板 3 区段(需求清单 / 任务清单 / 缺陷清单)数据源严格一致,无新解析口径
5. **REVIEW.md 聚合文件**位于版本顶层(与 `RESULT.md` 同级),**不**进 `review/` 子目录(NFR-6)— 与 `code-dashboard` "顶层看板"风格一致

## 4. 待澄清项(本设计阶段)

**无新增待澄清**。所有设计决策均由既有需求(REQ-00008) + 既有规范 + 既有 8 个 design 提供充分依据。
