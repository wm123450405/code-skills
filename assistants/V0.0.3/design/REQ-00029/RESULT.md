# 概要设计 — REQ-00029 优化 /code-dashboard 屏显报告(只展示结果 + 去除不必要换行)

- 需求编码:REQ-00029
- 所属版本:V0.0.3
- 状态:已锁定
- 设计目标:`--balanced`(功能性=高,code-auto 上下文检测采纳默认)
- 责任人:用户
- 创建:2026-06-10
- 最近更新:2026-06-10

## 设计目标

| 维度 | 优先级 |
| --- | --- |
| 整体设计目标 | `--balanced` |
| 功能性 | 高(沿用 code-auto 上下文 `--balanced` 默认) |

**说明**:本需求为单文件渲染层改造,架构维度(扩展性/健壮性/可维护性/封装性/可复用性/可读性)沿用 `--balanced` 默认值;功能性=高(用户要求"屏显报告压缩到最小化")。

## 1. 设计概述

本需求对 `code-dashboard` 技能的 SKILL.md 做"渲染层瘦身"改造,**严格限定**在 §输出段 + §工作流程 步骤 4 各段描述(纯 SKILL.md 文档改造);**不动**算法 1/2/3/4/5(沿用 V0.0.2 REQ-00023 既有)、**不动**工具集(仍只 Read/Glob/Grep)、**不动**看板字段、**不动**其他 10 个 `code-*` 技能 SKILL.md、**不动** `./assistants/rules/` 与 `CLAUDE.md` 与 `marketplace.json`。

**上游引用**: `./assistants/V0.0.3/require/REQ-00029/RESULT.md`(8 FR / 8 AC / 3 待澄清沿用既有)
**遵循规范**: `./assistants/rules/` 9 个文件(skill-conventions / module-conventions / dashboard-conventions / doc-conventions / encoding-conventions / naming-conventions / coding-style / commit-conventions / directory-conventions)
**架构图** (ASCII):
```
用户输入 `/code-dashboard [REQ-NNNNN]`
        │
        ▼
   步骤 0:版本上下文检测(Read .current-version)
        │
        ▼
   步骤 1:参数解析(算法 0)
        │
        ▼
   步骤 2:数据加载(Read/Glob)─────────────┐
        │                                  │
        ▼                                  ▼
   步骤 3:区段解析(算法 1,字节级保留)   需求模式:3 文件并行 Read
        │                                  │
        └──────────────┬───────────────────┘
                       ▼
            步骤 4:聚合 + 渲染 ★ 本需求改造锚点
                       │
                       ▼
            步骤 5:建议生成(算法 3/4,字节级保留)
                       │
                       ▼
            步骤 6:屏幕打印(无文件副作用)
                       │
                       ▼
                  stdout(≤ 8 / ≤ 15 行)
```

## 2. 上游引用

| 上游 | 路径 | 关联 |
| --- | --- | --- |
| 需求 | `./assistants/V0.0.3/require/REQ-00029/RESULT.md` | 8 FR / 8 AC 全为本设计依据 |
| 规范 | `./assistants/rules/skill-conventions.md` | frontmatter 字节级保留(INV-1) |
| 规范 | `./assistants/rules/dashboard-conventions.md §规则 1` | 看板字段三方同步(本需求不触发) |
| 规范 | `./assistants/rules/encoding-conventions.md` | 任务编号正则(算法 4 沿用) |
| 既有设计 | `./assistants/V0.0.2/design/REQ-00023/RESULT.md` | code-dashboard 当前 4 段屏显契约 |

## 3. 模块拆分

**单一目标**: 修改 `plugins/code-skills/skills/code-dashboard/SKILL.md` 渲染层。

| 模块 | 状态 | 职责 | 路径 |
| --- | --- | --- | --- |
| code-dashboard 屏显渲染层 | 修改既有 | 步骤 4 各段渲染输出 + §输出 契约样例 | `plugins/code-skills/skills/code-dashboard/SKILL.md` |
| 其他 10 个 `code-*` 技能 | 0 改 | — | — |
| `code-dashboard/SKILL.md` 算法层(附录 A/B/C) | 0 改(INV-2/3) | 字节级保留 | — |
| `code-dashboard/SKILL.md` frontmatter | 0 改(INV-1) | 字节级保留 | L1-3 |
| `code-dashboard/SKILL.md` 工具使用约定 | 0 改(INV-7) | 仍只 Read/Glob/Grep | L109-121 |

详见 `module-breakdown.md`。

## 4. 接口概要

### 4.1 屏显契约(总览模式)

| 区段 | 改后格式 |
| --- | --- |
| 段 1:总开发进度 | `[███████████░] 92%` |
| 段 2:5 类状态占比 | `状态: 待代码开发 0 / 待代码评审 0` |
| 段 3:高优缺陷 | `P0 待修复: █ 2 \| P1 待修复: ░ 0` |
| 段 4:建议 | `> /code-fix BUG-00001 [高] (依据: P0 待修复 2 个)`(每条 1 行,≤ 5 条) |

**满负载合计 ≤ 8 行**(从既有 ≤ 12 行收紧)。

### 4.2 屏显契约(需求模式)

| 区段 | 改后格式 |
| --- | --- |
| 段 1:元信息 | `REQ-00028 · 新增 code-answer 技能 [已完成] 概要: ✓ 详细: ✓` |
| 段 2:任务清单 | `任务: TASK-REQ-00028-00001 × 1(已完成 1 / 不适用 1)` |
| 段 3:关联缺陷 | `缺陷: (无)` |
| 段 4:任务进度 | `进度: 1/1 (100%)` |
| 段 5:建议 | `> /code-dashboard REQ-00028 [低] (依据: 查看需求详情)`(每条 1 行) |

**满负载合计 ≤ 15 行**(从既有"5 段独立多行"收紧)。

详见 `dependencies.md §2`。

## 5. 数据结构

**本需求 0 改数据结构**。

屏显契约中所有字段(`已完成` / `概要: ✓` / `1/1` / `优先级` 等)均派生自既有看板 `RESULT.md` 字段,未新增字段(沿用 INV-4)。

## 6. 规范遵循

| 规范条款 | 本设计遵循 | 依据 |
| --- | --- | --- |
| `skill-conventions.md §规则 1` frontmatter 字节级保留 | ✅ INV-1 | L1-3 不动 |
| `module-conventions.md §规则 1` 技能资源摆放 | ✅ | 无新增 templates/guidelines/checklists |
| `dashboard-conventions.md §规则 1` 三方同步 | ✅ 不触发 | INV-4 字段 0 改 |
| `encoding-conventions.md §规则 1` 任务编号正则 | ✅ INV-2 | 算法 4 字节级保留 |
| NFR-1 算法 1/2/3/4/5 字节级保留 | ✅ INV-2/3 | 附录 A/B 不动 |
| NFR-2 其他 10 个技能 0 改 | ✅ INV-5 | — |
| NFR-7 工具集不变 | ✅ INV-7 | 仍只 Read/Glob/Grep |

详见 `rule-compliance.md`。

## 7. 待澄清/未决项

| 编号 | 问题 | 影响范围 | 阻塞方 | 期望回复时间 |
| --- | --- | --- | --- | --- |
| Q-1 | 总览模式的"5 类状态"若全 0,是否显示"(无)"? | FR-2 退化路径 | 无 | (已沿用既有) |
| Q-2 | 需求模式任务清单/关联缺陷为空时,是否显示"(无)"? | FR-5 退化路径 | 无 | (已沿用既有) |
| Q-3 | 屏显是否保留 ASCII 比例条(12 字符固定)? | FR-4 | 无 | (已沿用既有算法 5) |

> Q-1 ~ Q-3 全部沿用既有退化行为,不构成新约束。

## 8. 边界与异常(继承 REQ-00023)

| ID | 场景 | 处理 | 退化 |
| --- | --- | --- | --- |
| E-1 | 无 `.current-version` | 屏显错误 + 引导调 `code-version` + 退出 | — |
| E-2 | 版本工作空间不存在 | 屏显错误 + 引导 | — |
| E-3 | 需求模式 + `require/<REQ>/` 不在列表 | 屏显错误 + 列出本版本所有需求 + 退出 | — |
| E-4 | 参数格式错 | 屏显用法 + 退出 | — |
| E-5 | 看板文件缺失 | 屏显错误 + 引导调 `code-version` + 退出 | — |
| E-6 | 区段缺失 | 屏显 `(无)`(沿用既有) | — |
| E-7 | 表格列错位 | 退化到原始 markdown 块原样输出 | — |
| E-8 | 内部异常 | 屏显 `✗ 内部错误: <msg>` + 退出 | — |

## 9. 关键决策(D-1 ~ D-7)

| 编号 | 决策 | 依据 |
| --- | --- | --- |
| D-1 | 仅改 code-dashboard/SKILL.md 渲染层 | NFR-1 字节级保留算法 1-5 |
| D-2 | 总览 + 需求两种模式都压 | 用户澄清 2026-06-10 §问题 1 |
| D-3 | 5 类状态占比段从 N 行压缩为 1 行摘要(不删除) | 用户澄清 2026-06-10 §问题 2 |
| D-4 | 建议单行格式 `> <cmd> [<prio>] (依据: <reason>)` | 用户澄清 2026-06-10 §问题 3 |
| D-5 | 进度条 3 行 → 1 行(只保留 ASCII 比例条) | FR-4 |
| D-6 | 总览模式 ≤ 8 行 / 需求模式 ≤ 15 行(从既有 ≤ 12 收紧) | FR-6 |
| D-7 | 工具集 0 改(仍只 Read/Glob/Grep) | NFR-7 |

## 10. 不变量(INV)

| 编号 | 不变量 |
| --- | --- |
| INV-1 | code-dashboard/SKILL.md frontmatter 0 修改 |
| INV-2 | 算法 1/2/3/4 字节级保留 |
| INV-3 | 算法 5(ASCII 比例条)字节级保留 |
| INV-4 | 看板 RESULT.md 字段 0 修改 |
| INV-5 | 其他 10 个 `code-*` 技能 SKILL.md 0 修改 |
| INV-6 | `marketplace.json` / `plugin.json` / `CLAUDE.md` / `./assistants/rules/` 0 修改 |
| INV-7 | code-dashboard 工具集不变 |

## 11. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-10 11:30 | v1 | 初始创建 | 概要设计完成;7 项决策 + 7 条不变量 + 1 个改造模块;code-auto 上下文采纳 `--balanced` 默认 | 用户 |