# 版本开发进度看板 — V0.0.5

> 本文件是 `V0.0.5` 版本工作空间的**简化版看板**。
> 需求/缺陷创建时追加一行,进度通过 `PROCESS.md` 追踪。

## 文档头
- 版本号:`V0.0.5`
- 创建时间:2026-06-30 19:00
- 最近更新:2026-06-30 20:13
- 创建人:wangmiao
- 负责人:wangmiao
- 状态:活跃
- 描述:V0.0.5 版本 — 使用 v2 新目录结构(req/+fix/)

---

## 需求清单

> 写入方:`code-req`(首次创建需求时追加一行)

| 需求编码 | 标题 | 进度文档 |
| --- | --- | --- |
| REQ-00045 | 补充 REQ-00044 重构后丢失的旧技能能力 | [PROCESS.md](req/REQ-00045/PROCESS.md) |
| REQ-00046 | 恢复旧技能中与用户确认的交互方式 | [PROCESS.md](req/REQ-00046/PROCESS.md) |
| REQ-00047 | 优化 REQUIRE.md 和 BUG.md 保留用户原始输入 | [PROCESS.md](req/REQ-00047/PROCESS.md) |
| REQ-00048 | 优化 code-dashboard 技能:输出模板化、移除需求模式、简化 | [PROCESS.md](req/REQ-00048/PROCESS.md) |
| REQ-00049 | 为 code-req、code-fix 增加 --confirm 模式 | [PROCESS.md](req/REQ-00049/PROCESS.md) |

**统计**:3

---

## 缺陷清单

> 写入方:`code-fix`(首次创建缺陷时追加一行)

| 缺陷编号 | 标题 | 进度文档 |
| --- | --- | --- |
| BUG-00001 | code-req 未按阶段顺序执行,跳过需求/设计/排期直接修改代码 | [PROCESS.md](fix/BUG-00001/PROCESS.md) |
| BUG-00002 | REQ-00044 重构后项目使用说明文档未更新,编码规范缺失同步规则 | [PROCESS.md](fix/BUG-00002/PROCESS.md) |
| BUG-00003 | code-req 工作流强制指令位置不够靠前,AI 跳过工作流直接修改代码 | [PROCESS.md](fix/BUG-00003/PROCESS.md) |
| BUG-00004 | code-req DONE 阶段兜底提交未触发,指令不够显式 | [PROCESS.md](fix/BUG-00004/PROCESS.md) |
| BUG-00007 | REQ-00049 执行中遗漏用户确认环节 | [PROCESS.md](fix/BUG-00007/PROCESS.md) |

**统计**:5

---

## 变更记录

> 写入方:所有 `code-*` 技能

| 时间 | 变更类型 | 变更摘要 | 关联项 |
| --- | --- | --- | --- |
| 2026-06-30 19:00 | 初始化 | 创建版本 V0.0.5 工作空间(v2 简化版看板) | — |
| 2026-06-30 19:35 | 需求创建 | 创建 REQ-00045:补充 REQ-00044 重构后丢失的旧技能能力 | REQ-00045 |
| 2026-06-30 20:13 | 需求完成 | 完成 REQ-00045:8 任务/0 发现/审查通过 | REQ-00045 |
| 2026-06-30 20:41 | 缺陷修复 | 完成 BUG-00001:code-req 阶段门控机制 | BUG-00001 |
| 2026-06-30 21:26 | 缺陷修复 | 完成 BUG-00002:README 更新+规范补充+技能规范读取 | BUG-00002 |