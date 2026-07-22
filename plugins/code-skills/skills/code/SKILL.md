---
name: code
description: 一体化开发工具集 /code · 首 token 路由入口。包含 7 个子命令:ver(版本管理与开发看板——无参数看进度,带版本号切换,`--publish` 发版)/ req(需求开发 7 阶段全流程)/ fix(缺陷修复 6 阶段全流程)/ faq(跨版本知识查询与文档导出)/ rule(编码规范追加/扩展)/ merge(worktree 自动合回主干)/ help(命令错误时显示帮助引导)。req/fix 必须严格走 7/6 阶段流程,先建 req/<REQ>/ 或 fix/<BUG>/ 工作产物目录再动代码,严禁 EnterPlanMode 或在 PROCESS.md 最后阶段 ≠ CODING 时修改 CWD 源码。
---

# `/code` — 一体化开发工具集

> **首 token = 子命令**。在用户输入 `/code <子命令>` 时,先识别首 token,再路由到对应子命令 SKILL.md。

---

## ⛔ 执行不变式 — 调用本技能前的第一关(强制)

> **本节优先级高于一切其他指令**。进入本技能后,在做任何动作之前,先看下方 5 条不变式,**逐条核对**。
>
> **任一违反 = 立即停手 + 处置**。本节位于 frontmatter 后第一段,不会被任何子命令段落覆盖。

### §0 不变式(5 条硬规则)

| # | 不变式 | 触发条件 |
| --- | --- | --- |
| **I-1** | **子命令首 token 路由**:首 token ∈ {`ver`, `req`, `fix`, `faq`, `rule`, `merge`} 才进子命令;否则进入 help 子命令 | 用户输入 `/code <子命令>` |
| **I-2** | **绝不使用 `EnterPlanMode`**:`req` / `fix` 的 PLAN 阶段已经取代 plan 模式功能 | 用户描述复杂 / 需要详细方案 / 任何场景 |
| **I-3** | **`req` / `fix` 在 `PROCESS.md` 最后阶段 = `CODING` 之前,严禁 `Edit`/`Write` 任何 CWD 源代码** | 阶段 = INIT / REQUIRE / DESIGN / PLAN / CHECK / DONE |
| **I-4** | **先建工作产物,再动代码**:第一次动作必须是 `mkdir req/<REQ-NNNNN>/` + 写 `PROCESS.md` 起始行 | 用户调 `/code req "<description>"` 或 `/code fix "<description>"` |
| **I-5** | **`/code rule` 严禁 `Edit` 既有规则文件**:只允许 `Edit` 在末尾追加;新建分类用 `Write` 首次 | 任何 7 阶段流程外的规则变更 |

**检测信号**(看到这些信号立即停):
- 已经调用或即将调 `EnterPlanMode` → 违反 I-2
- 已经用 `Edit`/`Write` 改过 CWD 代码但 `req/<REQ>/PROCESS.md` 不存在 → 违反 I-3 + I-4
- 准备用 `Edit` 全量覆盖 `./assistants/rules/<分类>.md` → 违反 I-5

### §0 违反后的处置流程(强制,不可降级)

```
step 1: 立即停止后续动作(不继续修改源代码、不进入下一阶段)
step 2: git checkout -- <files> 回退已修改的 CWD 文件
step 3: mkdir -p req/<REQ-NNNNN>/  (或 fix/<BUG-NNNNN>/)
        echo "| $(date '+%Y-%m-%d %H:%M') | INIT | 失败 | 违反不变式 §<N>: <具体说明> |" >> req/<REQ>/PROCESS.md
step 4: 重新从 §0 不变式开始核对,逐条 ✓ 后再进入正常流程
```

> **反向用例**:用户描述"为 /code 加 HELP 功能"是技术性元任务,不是面向某个产品需求。**这种"自身技能改进"任务**也必须走 `req` 流程 → 在 `req/REQ-00050/REQUIRE.md` 里写"为 /code 加 HELP,FR-1 是..."

### §0 验证:本 §0 是否生效

每次进入本技能时,**用 AskUserQuestion 自检一次**(即使是非 `--auto` 也走):

```
请确认已读完 §0 不变式 5 条:
- I-1(子命令路由)明白了吗?
- I-2(禁 plan 模式)明白了吗?
- I-3(非 CODING 禁改源码)明白了吗?
- I-4(先建工作产物)明白了吗?
- I-5(rule 不重写)明白了吗?
A. 全部明白,继续执行
B. 某条不清楚,先解释
```

> `--auto` 模式:跳过此问询,直接默认"全部明白"

---

## 子命令路由表

> 用户输入 `/code <子命令>` 后,按首 token 路由到对应 SKILL.md。

| 子命令 | 入口 | SKILL.md 路径 | 触发场景 |
| --- | --- | --- | --- |
| `ver` | `/code ver` | [`references/ver/SKILL.md`](references/ver/SKILL.md) | 版本管理 + 开发看板 + 发布检查 |
| `req` | `/code req` | [`references/req/SKILL.md`](references/req/SKILL.md) | 需求开发 7 阶段全流程 |
| `fix` | `/code fix` | [`references/fix/SKILL.md`](references/fix/SKILL.md) | 缺陷修复 6 阶段全流程 |
| `faq` | `/code faq` | [`references/faq/SKILL.md`](references/faq/SKILL.md) | 跨版本知识查询 + 文档导出 |
| `rule` | `/code rule` | [`references/rule/SKILL.md`](references/rule/SKILL.md) | 编码规范追加/扩展 |
| `merge` | `/code merge` | [`references/merge/SKILL.md`](references/merge/SKILL.md) | worktree 自动合回主干 |
| `help` | (首 token 不可识别 / 无参数时) | [`references/help/SKILL.md`](references/help/SKILL.md) | 显示完整帮助 + 6 选项引导 |

### 路由规则

1. 首 token ∈ {`ver`, `req`, `fix`, `faq`, `rule`, `merge`} → 加载对应子命令 SKILL.md
2. 首 token 缺失 / 无法识别 → 加载 `references/help/SKILL.md`,显示 §A 完整 HELP + AskUserQuestion 6 选项引导
3. 用户输入 `/code help` / `/code --help` / `/code -h` → 直接加载 `references/help/SKILL.md` §A

> **本技能定位**:路由 + §0 不变式 + 全局纪律。子命令的具体流程、参数、边界、不做的事,均在各子命令 SKILL.md 内。

---

## 衔接

- **下游**:`/code ver` / `/code req` / `/code fix` / `/code faq` / `/code rule` / `/code merge` / `/code help`
- **上游**:用户直接发起
- **横向**: `./assistants/rules/` 跨所有版本共享,被所有子命令只读消费

---

## 必须做事项清单

> 以下事项为强制要求,违反即视为本技能执行失败。

- 进入本技能时**必须**完整执行 §0 不变式验证(I-1 ~ I-5)
- 新增/修改子命令 `description` 时**必须**验证与已注册 description 无显著语义重叠(参考 `references/help/SKILL.md` 命令矩阵)
- 子命令的详细流程**必须**写在 `references/<子命令>/SKILL.md` 内,主 SKILL.md 仅做路由

---

## 不要做的事

- (本节保留位置;具体约束见上文"必须做事项清单")
