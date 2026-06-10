# 详细设计 — REQ-00029 优化 /code-dashboard 屏显报告(只展示结果 + 去除不必要换行)

- 需求编码:REQ-00029
- 所属版本:V0.0.3
- 状态:已锁定
- 设计目标:`--balanced`(code-auto 上下文检测采纳默认;功能性=高)
- 责任人:用户
- 创建:2026-06-10
- 最近更新:2026-06-10

## 设计目标

| 维度 | 优先级 |
| --- | --- |
| 整体设计目标 | `--balanced` |
| 功能性 | 高(沿用 code-auto 上下文 `--balanced` 默认) |

**说明**:本需求为单文件渲染层改造,功能性=高(用户要求"屏显报告压缩到最小化");架构维度沿用 `--balanced` 默认。

## 1. 设计概述

本需求对 `code-dashboard` 技能的 SKILL.md 做"渲染层瘦身"改造,目标:**总览模式屏显 ≤ 8 行 / 需求模式屏显 ≤ 15 行**;**不**新增/修改任何字段,**不**改算法(算法 1/2/3/4/5 字节级保留),**不**改工具集(仍只 Read/Glob/Grep)。

**上游引用**: `./assistants/V0.0.3/require/REQ-00029/RESULT.md`(8 FR / 8 AC)
**遵循规范**: `./assistants/rules/` 9 个文件(skill-conventions / module-conventions / dashboard-conventions / doc-conventions / encoding-conventions / naming-conventions / coding-style / commit-conventions / directory-conventions)

## 2. 上游引用

| 上游 | 路径 | 关联 |
| --- | --- | --- |
| 需求 | `./assistants/V0.0.3/require/REQ-00029/RESULT.md` | 8 FR / 8 AC 全为本设计依据 |
| 概要设计 | `./assistants/V0.0.3/design/REQ-00029/RESULT.md` | 7 决策 D-1~D-7 / 7 不变量 INV-1~INV-7 |
| 规范 | `./assistants/rules/skill-conventions.md §规则 1` | frontmatter 字节级保留(INV-1) |
| 规范 | `./assistants/rules/dashboard-conventions.md §规则 1` | 看板字段三方同步(本需求不触发) |
| 规范 | `./assistants/rules/encoding-conventions.md §规则 1` | 任务编号正则(算法 4 字节级保留) |
| 既有 SKILL.md | `plugins/code-skills/skills/code-dashboard/SKILL.md` | 当前 4 段屏显契约(本需求改造目标) |

## 3. 模块详细化

### 3.1 改造模块(单一目标)

| 模块 | 路径 | 状态 | 改造范围 |
| --- | --- | --- | --- |
| `code-dashboard/SKILL.md §输出` 段 1(总览契约样例) | `plugins/code-skills/skills/code-dashboard/SKILL.md` | 修改 | L77-99(总览契约样例)+ L101-107(退化 + 总行数说明) |
| `code-dashboard/SKILL.md §输出` 段 2(需求契约样例) | `plugins/code-skills/skills/code-dashboard/SKILL.md` | 修改 | L78(需求模式 5 段) |
| `code-dashboard/SKILL.md §工作流程 > 步骤 4 段 1` | `plugins/code-skills/skills/code-dashboard/SKILL.md` | 修改 | L182-200(总开发进度渲染) |
| `code-dashboard/SKILL.md §工作流程 > 步骤 4 段 2` | `plugins/code-skills/skills/code-dashboard/SKILL.md` | 修改 | L202-228(5 类状态占比渲染) |
| `code-dashboard/SKILL.md §工作流程 > 步骤 4 段 3` | `plugins/code-skills/skills/code-dashboard/SKILL.md` | 修改 | L230-243(高优缺陷渲染) |
| `code-dashboard/SKILL.md §工作流程 > 步骤 4 段 4` | `plugins/code-skills/skills/code-dashboard/SKILL.md` | 修改 | L245-267(后续操作建议渲染) |
| `code-dashboard/SKILL.md §工作流程 > 步骤 4 段 5` | `plugins/code-skills/skills/code-dashboard/SKILL.md` | 修改 | L269-273(需求模式 5 段) |

### 3.2 不改模块(INV 锁定)

| 模块 | 状态 | 不改理由 |
| --- | --- | --- |
| `code-dashboard/SKILL.md` frontmatter(L1-3) | 0 改 | INV-1 `skill-conventions §规则 1` 字节级保留 |
| `code-dashboard/SKILL.md` §工具使用约定(L109-121) | 0 改 | INV-7 工具集不变(仍只 Read/Glob/Grep) |
| `code-dashboard/SKILL.md` §附录 A 算法 4(L402-420) | 0 改 | INV-2 算法 4 字节级保留 |
| `code-dashboard/SKILL.md` §附录 B 算法 5(L422-435) | 0 改 | INV-3 ASCII 比例条字节级保留 |
| `code-dashboard/SKILL.md` §附录 C 建议数据结构(L437-453) | 0 改 | 沿用既有 |
| 其他 10 个 `code-*` 技能 SKILL.md | 0 改 | INV-5 |
| `./assistants/V<版本号>/RESULT.md` 字段 | 0 改 | INV-4(避免触发 dashboard-conventions §规则 1 三方同步) |
| `./assistants/rules/` 13 份 | 0 改 | INV-6 |
| `plugins/code-skills/CLAUDE.md` | 0 改 | INV-6 |
| `marketplace.json` / `plugin.json` | 0 改 | INV-6 |

## 4. 算法与逻辑

### 4.1 总览模式段 1 渲染(FR-4 + 屏显 ≤ 8 行)

**改前**(3 行):
```
总开发进度
──────────
[████████░░░░] 67%
```

**改后**(1 行):
```
[███████████░] 92%
```

**算法逻辑**(伪代码):
```
renderOverviewSection1(progress):
  if progress.total == 0:
    return "— / 无需求无缺陷,无需进度"
  return renderBar(progress.filled, progress.total)  # 算法 5,字节级保留
```

### 4.2 总览模式段 2 渲染(FR-2 + 5 类状态压缩为 1 行)

**改前**(N 行):
```
各状态数量占比
──────────────
待概要设计: 需求 2 / 缺陷 0(占比 50.0%)
待代码开发: 需求 1 / 缺陷 0(占比 25.0%)
待代码评审: 需求 1 / 缺陷 0(占比 25.0%)
```

**改后**(1 行):
```
状态: 待代码开发 0 / 待代码评审 0
```

**算法逻辑**(伪代码):
```
renderOverviewSection2(breakdown):
  parts = []
  for each row in breakdown.filter(r => r.total > 0):
    parts.append("待" + row.state + " " + row.total)
  if parts.isEmpty():
    return "状态: (无)"
  return "状态: " + parts.join(" / ")
```

### 4.3 总览模式段 3 渲染(FR-1 + P0/P1 合并 1 行)

**改前**(4 行):
```
高优先级缺陷
───────────
P0 待修复: █ 1
P1 待修复: ░ 0
```

**改后**(1 行):
```
P0 待修复: █ 2 | P1 待修复: ░ 0
```

**算法逻辑**(伪代码):
```
renderOverviewSection3(bugs):
  p0 = bugs.filter(b => b.severity == "P0" && b.status != "已修复").length
  p1 = bugs.filter(b => b.severity == "P1" && b.status != "已修复").length
  return "P0 待修复: " + marker(p0) + " " + p0 + " | P1 待修复: " + marker(p1) + " " + p1
```

### 4.4 总览模式段 4 渲染(FR-3 + 建议单行格式)

**改前**(每条 3 行,共 ≤ 15 行):
```
> 建议: /code-design REQ-00023
> 依据: REQ-00023 在"待概要设计"状态
> 优先级: 中
```

**改后**(每条 1 行,共 ≤ 5 行):
```
> /code-design REQ-00023 [中] (依据: REQ-00023 在"待概要设计"状态)
```

**算法逻辑**(伪代码):
```
renderOverviewSection4(suggestions):
  if suggestions.isEmpty():
    return "> 无后续动作"
  return suggestions.map(s =>
    "> " + s.command + " [" + s.priority + "] (依据: " + s.reason + ")"
  ).join("\n")
```

### 4.5 需求模式 5 段渲染(FR-5 + 段内压)

**改后屏显样例**(5 段结构保留,段内单行):
```
REQ-00028 · 新增 code-answer 技能 [已完成] 概要: ✓ 详细: ✓
任务: TASK-REQ-00028-00001 × 1(已完成 1 / 不适用 1)
缺陷: (无)
进度: 1/1 (100%)
> /code-dashboard REQ-00028 [低] (依据: 查看需求详情)
> /code-publish V0.0.3 [中] (依据: 所有需求已完成)
```

**段 1 元信息**(单行合并):
- 格式:`<REQ> · <标题> [<状态>] 概要: <✓/—> 详细: <✓/—>`
- 来源:`require/<REQ>/RESULT.md` + `plan/<REQ>/RESULT.md` 存在性

**段 2 任务清单**(单行摘要):
- 格式:`任务: <TASK-...> × <N>(已完成 <N1> / 不适用 <N2>)`
- 来源:`plan/<REQ>/PLAN.md` "任务总览" 表格
- 退化:任务空 → `任务: (无)`

**段 3 关联缺陷**(沿用既有范式,1 行):
- 格式:`缺陷: (无)` 或 `缺陷: F-NNN [<状态>]`
- 来源:主看板"缺陷清单"区段,筛 `relatedTask.startsWith(reqNum + "-")`

**段 4 任务进度**(单行):
- 格式:`进度: <已完成>/<总数> (<比例>%)`
- 来源:从段 2 任务清单聚合

**段 5 建议**(FR-3 单行格式,沿用):
- 沿用 4.4 单行格式

## 5. 数据结构完整变更

**本需求 0 改数据结构**(INV-4 锁定)。

屏显契约中所有字段(`已完成` / `概要: ✓` / `1/1` / `优先级` 等)均派生自既有看板 `RESULT.md` 字段,未新增字段。

## 6. 接口细节

**本需求 0 改对外接口**(本技能为只读型 CLI,无外部 API)。

**屏显契约变更**(本节为本需求唯一对外契约):

| 契约 ID | 改前 | 改后 | 行数变化 |
| --- | --- | --- | --- |
| 总览段 1 | 3 行(标题+分隔+ASCII) | 1 行(只 ASCII) | -2 |
| 总览段 2 | 1 + 1 + N 行(标题+分隔+N 状态) | 1 行(单行摘要) | -1-N |
| 总览段 3 | 1 + 1 + 2 行(标题+分隔+P0+P1) | 1 行(单行合并) | -3 |
| 总览段 4 | 每条 3 行(建议/依据/优先级) | 每条 1 行(单行合并) | -2*N(N ≤ 5) |
| 需求段 1 | 1 + 1 + 4 行(标题+分隔+4 元信息) | 1 行(单行合并) | -5 |
| 需求段 2 | 1 + 1 + N 行(标题+分隔+N 任务) | 1 行(单行摘要) | -1-N |
| 需求段 3 | 1 + 1 + N 行(标题+分隔+N 缺陷) | 1 行(单行合并) | -1-N |
| 需求段 4 | 1 + 1 + 1 行(标题+分隔+进度) | 1 行(单行合并) | -2 |
| 需求段 5 | 沿用总览段 4 | 同总览段 4 | — |
| **总览满负载** | 12 行 | **8 行** | -4 |
| **需求满负载** | 18 行 | **9 行** | -9 |

## 7. 异常处理

**本需求 0 改异常处理**(沿用 L1/L2/L3 三层退化)。

退化场景屏显(FR-5 退化路径):

| 场景 | 屏显(改后) |
| --- | --- |
| 无需求无缺陷 | `— / 无需求无缺陷,无需进度`(单行) + 段 2 = `(无)` + 段 4 = `> 无后续动作` |
| 5 类状态全 0 | 段 2 = `状态: (无)`(单行) |
| 高优缺陷全 0 | 段 3 = `P0 待修复: ░ 0 \| P1 待修复: ░ 0`(1 行) |
| 5 条建议无触发 | 段 4 = `> 无后续动作`(1 行) |
| 命中 > 5 条建议 | 屏显前 5 条 + `> 另有 N 条相关建议,可通过执行 /code-require 补录` 触发 |

## 8. 安全要求

**本需求 0 改安全要求**(只读型 CLI,无外部 API)。

## 9. 状态机/流程

**本需求 0 改状态机**:`code-dashboard` 既有状态机(步骤 0 → 1 → 2 → 3 → 4 → 5 → 6)0 改。

**本需求只改**:步骤 4 渲染输出 + 步骤 6 屏显打印的字符格式。

## 10. 性能与资源

**本需求 0 改性能与资源**(纯屏显渲染层改造,无 IO 变化)。

## 11. 测试要点

**本需求 0 引入新测试**(NFR-7 工具集不变,沿用既有验证):

### 单元测试
- 沿用既有:不需要为屏显字符串写单元测试(屏显契约以 SKILL.md 文档样例为准)

### 手工验证(AC-1 ~ AC-8)
- AC-1:`git status` 验证无副作用
- AC-2:数屏显行数(总览 ≤ 8)
- AC-3:检查段 2 单行
- AC-4:检查建议单行格式
- AC-5:检查进度条无解释行
- AC-6:数屏显行数(需求 ≤ 15)
- AC-7:grep 元描述关键词 0 匹配
- AC-8:5 类状态映射仍正确触发

## 12. 规范遵循

| 规范条款 | 本设计遵循 | 依据 |
| --- | --- | --- |
| `skill-conventions.md §规则 1` frontmatter 字节级保留 | ✅ INV-1 | L1-3 不动 |
| `module-conventions.md §规则 1` 技能资源摆放 | ✅ | 无新增 templates/guidelines/checklists |
| `dashboard-conventions.md §规则 1` 三方同步 | ✅ 不触发 | INV-4 字段 0 改 |
| `encoding-conventions.md §规则 1` 任务编号正则 | ✅ INV-2 | 算法 4 字节级保留 |
| NFR-1 算法 1/2/3/4/5 字节级保留 | ✅ INV-2/3 | 附录 A/B 不动 |
| NFR-2 其他 10 个技能 0 改 | ✅ INV-5 | — |
| NFR-7 工具集不变 | ✅ INV-7 | 仍只 Read/Glob/Grep |

## 13. 待澄清/未决项

| 编号 | 问题 | 影响范围 | 阻塞方 | 期望回复时间 |
| --- | --- | --- | --- | --- |
| Q-1 | 总览模式的"5 类状态"若全 0,是否显示"(无)"? | FR-2 退化路径 | 无 | (已沿用既有) |
| Q-2 | 需求模式任务清单/关联缺陷为空时,是否显示"(无)"? | FR-5 退化路径 | 无 | (已沿用既有) |
| Q-3 | 屏显是否保留 ASCII 比例条(12 字符固定)? | FR-4 | 无 | (已沿用既有算法 5) |

> Q-1 ~ Q-3 全部沿用既有退化行为,不构成新约束。

## 14. 关联编码计划

- 同版本关联:`./assistants/V0.0.3/plan/REQ-00029/PLAN.md`(本技能产出,详 §"详细设计 步骤 7A" → 拆分 1 个任务)

## 15. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-10 12:00 | v1 | 初始创建 | 详细设计完成;5 段渲染算法 + 6 不改模块 + 1 个改造模块;code-auto 上下文采纳 `--balanced` 默认 | 用户 |
