---
name: code
description: 集成开发入口 `/code`,首 token 路由到 6 个子命令(ver / req / fix / faq / rule / merge);用户调 `/code`(无参)或首 token 不可识别时回落到 `/code help`。req/fix 是 _gated_ 7/6 阶段流程(REQUIRE→DESIGN→PLAN→CODING→CHECK→DONE),每阶段必须先建 req/<REQ>/ 或 fix/<BUG>/ 工作目录并追加 PROCESS.md,_traced_ 全流程;只有 CODING 阶段允许改 CWD 源码;严禁 EnterPlanMode。
---

# `/code` — 集成开发入口

> 首 token = 子命令。本文件只做路由 + _gated_ 不变式;子命令流程见各自 `references/<name>/SKILL.md`。

---

## §0 _gated_ 不变式(进入本技能后第一关)

逐条核对。任一违反 = 立即停手 + 回退 + 写失败行 + 退到 INIT。

| # | 不变式 | 触发条件 |
| --- | --- | --- |
| **I-1** | 首 token ∈ {`ver`,`req`,`fix`,`faq`,`rule`,`merge`} → 加载对应子命令 SKILL.md;否则 → 加载 `references/help/SKILL.md` | 任何 `/code` 调用 |
| **I-2** | **绝不使用 `EnterPlanMode`** — req/fix 的 PLAN 阶段已取代它 | 任何复杂任务 |
| **I-3** | **PROCESS.md 最后阶段 ≠ `CODING` 时,严禁 `Edit`/`Write` CWD 源码** | INIT/REQUIRE/DESIGN/PLAN/CHECK/DONE 阶段 |
| **I-4** | **先建工作产物再动代码** — 第一次动作必须是建 `req/<REQ-NNNNN>/` 或 `fix/<BUG-NNNNN>/` + 初始化 PROCESS.md | 调 `/code req` 或 `/code fix` |
| **I-5** | **`/code rule` 只追加不重写** — 既有的 `./assistants/rules/<分类>.md` 用 `Edit` 末尾追加,新建分类用 `Write` 首次 | 任何规则变更 |

**违反处置**: `git checkout -- <files>` 回退 → 建目录 + 写 `| <时间> | INIT | 失败 | 违反 §<N>: <说明> |` → 重新核对 §0。

> "为 /code 加自身功能"也是元任务 → 走 `/code req`,在 `req/REQ-00050/REQUIRE.md` 里写需求。

---

## 子命令路由

| 首 token | 加载文件 | 何时触发 |
| --- | --- | --- |
| `ver` | `references/ver/SKILL.md` | 版本切换 / 看开发进度 / 发布检查 |
| `req` | `references/req/SKILL.md` | 需求开发 7 阶段 |
| `fix` | `references/fix/SKILL.md` | 缺陷修复 6 阶段 |
| `faq` | `references/faq/SKILL.md` | 跨版本知识查询 / 文档导出 |
| `rule` | `references/rule/SKILL.md` | 编码规范追加 |
| `merge` | `references/merge/SKILL.md` | git worktree 合回主干 |
| 其他 / 无参数 | `references/help/SKILL.md` | 完整 HELP + 7 选项引导 |

> 路由后,子命令 SKILL.md 接管全部流程。本技能定位 = 路由 + 不变式,不做任何阶段逻辑。

---

## 衔接

- 下游: 6 个子命令 + help
- 上游: 用户直接发起
- 横向: `./assistants/rules/` 跨版本共享,被子命令只读消费