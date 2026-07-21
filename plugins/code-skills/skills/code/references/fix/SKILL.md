---
name: code-fix
description: `/code fix` 缺陷修复 _gated_ 6 阶段流程。模型在用户报告 bug / 续跑 BUG-NNNNN 时调用。INIT→DESIGN→PLAN→CODING→CHECK→DONE,DESIGN/PLAN/CODING/CHECK 复用 req 的 4 阶段子流程,INIT 阶段产出 BUG.md 含严重度 P0-P3。_traced_(PROCESS.md 追加);仅 CODING 阶段可改 CWD 源码;支持 `--confirm` / `--auto`。
---

# `/code fix` — 缺陷修复

> 流程细节复用 [`references/req/`](../req/) 下文件(`common.md` / `design.md` / `plan.md` / `coding.md` / `check.md` / `runtime-environment.md`),fix 专用资料见 [`fix-register.md`](fix-register.md)。

## 与 req 的差异

| 方面 | req | fix |
| --- | --- | --- |
| 第 1 阶段 | REQUIRE(REQUIRE.md) | INIT(BUG.md + 严重度 P0-P3) |
| 后续 4 阶段 | DESIGN/PLAN/CODING/CHECK | 复用 `../req/` 下的同名子流程 |
| 输出目录 | `req/<REQ-NNNNN>/` | `fix/<BUG-NNNNN>/` |
| 看板区段 | 需求清单 | 缺陷清单 |

## 启动检查

进入本技能后,先确认 §0 不变式(主 SKILL.md)。然后:

1. 读 `./assistants/.current-version` — 不存在则停,提示先调 `/code ver`
2. 解析用户输入: 自然语言 → 新分配 `BUG-NNNNN`;`BUG-NNNNN` → 直接用
3. `fix/<BUG-NNNNN>/PROCESS.md` 不存在 → 建目录 + 初始化 PROCESS.md
4. 从 PROCESS.md 最后一行确定当前阶段,从中断处继续

## 6 阶段(_gated_ + _traced_)

| 阶段 | 强制产出 | 关键约束 |
| --- | --- | --- |
| **INIT** | `BUG.md`(缺陷描述/触发条件/可能成因/影响范围/严重度) | 不做修复方案;默认严重度 P2 |
| **DESIGN** | `DESIGN.md` | 同 req;危险操作不可跳 |
| **PLAN** | `PLAN.md` | 任务编号 `TASK-<BUG-NNNNN>-<序号>` |
| **CODING** | `TASK-N.md` × N + CWD 代码变更 | 同 req |
| **CHECK** | `CHECK.md`(9 维度) | 审查维度含"缺陷修复一致性" |
| **DONE** | 完成报告 + 兜底 commit | `chore(code fix): <编号> <标题>` 格式 |

## 三态确认

同 req。`--confirm` 与 `--auto` 互斥。

## 强制约束

- **禁 `EnterPlanMode`**
- **非 CODING 阶段禁改 CWD 源码**
- 代码注释不引用追踪编号
- 不修改 `./assistants/rules/`
- 不修改 RESULT.md 中非本技能负责的区段
- INIT 阶段不做修复方案(归 DESIGN)
- 评审-编码循环 ≤5 轮
- 运行时缺失按 req 同款机制处理;**不**先询问是否装

## 衔接

- 下游: `/code ver --publish`
- 上游: `/code ver`(必);`/code rule`
- 横向: `/code req`(共用 4 阶段子流程);`/code faq`