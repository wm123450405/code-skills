---
name: code-req
description: `/code req` 需求开发 _gated_ 7 阶段流程。模型在用户发起"开新需求 / 续跑 REQ-NNNNN / 一句话描述要做什么"时调用。INIT→REQUIRE→DESIGN→PLAN→CODING→CHECK→DONE,每阶段 _traced_(追加 PROCESS.md),仅 CODING 阶段可改 CWD 源码;支持 `--confirm`(每阶段重读确认)/ `--auto`(静默全跑)。
---

# `/code req` — 需求开发

> 流程细节: [`common.md`](common.md) / [`require.md`](require.md) / [`design.md`](design.md) / [`plan.md`](plan.md) / [`coding.md`](coding.md) / [`check.md`](check.md) / [`runtime-environment.md`](../runtime-environment.md) / [`languages/<lang>.md`](languages/)。

## 启动检查

进入本技能后,先确认 §0 不变式(主 SKILL.md)。然后:

1. 读 `./assistants/.current-version` — 不存在则停,提示先调 `/code ver`
2. 解析用户输入: 自然语言 → 新分配 `REQ-NNNNN`(最大编号+1);`REQ-NNNNN` → 直接用
3. `req/<REQ-NNNNN>/PROCESS.md` 不存在 → 建目录 + 初始化 PROCESS.md
4. 从 PROCESS.md 最后一行确定当前阶段,从中断处继续

## 7 阶段(_gated_ + _traced_)

| 阶段 | 强制产出 | 关键约束 |
| --- | --- | --- |
| **INIT** | PROCESS.md 起始行 | 分配编号 |
| **REQUIRE** | `REQUIRE.md`(FR/NFR/AC) | 不做技术选型(关键词过滤 20 个,延迟到 DESIGN);需求冲突必须 `AskUserQuestion`,不可标"设计推断" |
| **DESIGN** | `DESIGN.md`(模块/接口/数据/流程/选型) | 4 类用户确认(扩展性/方案选型/改修方案/**危险操作**);危险操作 `--auto` 也需停 |
| **PLAN** | `PLAN.md`(任务列表 + Mermaid 依赖图) | 任务编号 `TASK-<REQ-NNNNN>-<序号>` |
| **CODING** | `TASK-N.md` × N + CWD 代码变更 | **唯一允许改源码阶段**;环境缺失走 §5 确认机制;评审-编码循环 ≤5 轮 |
| **CHECK** | `CHECK.md`(9 维度) | 正确性/需求一致性/设计一致性 + 代码行数阈值(总 500 / 新增 200);"必须改"→ 生成改修任务 → 重 CHECK |
| **DONE** | 完成报告 + 兜底 commit | `chore(code req): <编号> <标题>` 格式 |

## 工作目录

```
./assistants/<版本号>/
└── req/<REQ-NNNNN>/
    ├── REQUIRE.md / DESIGN.md / PLAN.md
    ├── TASK-<序号>.md × N
    ├── CHECK.md
    ├── PROCESS.md          追加式,_traced_ 全流程
    ├── clarifications.md   REQUIRE 阶段问答(可选)
    └── LOG.md              非必要不记
```

## 三态确认

| 模式 | 阶段边界 | 阶段内内容确认 |
| --- | --- | --- |
| `--confirm` | 增强(路径提示+重读+继续/中止) | 正常触发 |
| `--auto` | 自动继续(前缀输出) | 自动选推荐项 |
| 默认 | 自动继续(无输出) | 正常触发 |

`--confirm` 与 `--auto` 互斥,同传报错。

## 强制约束

- **禁 `EnterPlanMode`**(PLAN 阶段已替代)
- **非 CODING 阶段禁改 CWD 源码**
- 代码注释不引用 `REQ-NNNNN` / `BUG-NNNNN` / `TASK-*` 追踪编号(用功能描述替代)
- 不修改 `./assistants/rules/`(`/code rule` 职责)
- 不修改 RESULT.md 中非本技能负责的区段
- REQUIRE 阶段每轮最多 1-3 个最阻塞的问题
- 评审-编码循环 ≤5 轮后必须询问用户
- CODING 阶段编译/单测前先尝试执行一次,**不**先询问是否装运行时;环境缺失(已实际运行失败)才走确认机制
- 运行时路径不入文档、不存 MEMORY
- 编译/单测缺运行时:`--auto` 自动安装;默认模式弹 A/B/C/D

## 衔接

- 下游: `/code ver --publish` 发版
- 上游: `/code ver`(必,提供激活版本);`/code rule`(项目级规范)
- 横向: `/code fix`(复用 DESIGN/PLAN/CODING/CHECK 子流程);`/code faq`(查询导出)