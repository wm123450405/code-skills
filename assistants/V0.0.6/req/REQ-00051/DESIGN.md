# 软件设计 — REQ-00051 · 主 SKILL.md 拆分与 help 子命令化

> 所属版本:V0.0.6
> 创建时间:2026-07-21 15:44
> 上游产物:REQUIRE.md

## 1. 设计概述

将 `plugins/code-skills/skills/code/SKILL.md`(93037 字节,2108 行)中按子命令组织的 6 段正文 + HELP 章节拆分为 7 个独立 SKILL.md,主 SKILL.md 仅保留路由职责(frontmatter + §0 不变式 + 首 token 分派 + 子命令文件引用)。

### 拆分前后对比

| 维度 | 拆分前 | 拆分后 |
|---|---|---|
| 主 SKILL.md 字节数 | 93,037 | ≤ 10,000(NFR-1) |
| 主 SKILL.md 行数 | 2,108 | ≤ 200 |
| 子命令职责 | 主文件内一节 | 独立 SKILL.md |
| help 引导 | 主文件 §A/§B/§C/§D | 独立 `help/SKILL.md` |

## 2. 模块拆分

### 2.1 主 SKILL.md(路由)

只承担 4 项职责:
1. **frontmatter** — `name: code` + `description: 一体化开发工具集 /code · 首 token 路由 ...`
2. **§0 不变式**(5 条硬规则) — 不变式是全局约束,所有子命令共享
3. **首 token 路由表** — 列出 7 个子命令入口及其引用路径
4. **子命令文件引用** — 每个子命令用一段简短提示 + `references/<子命令>/SKILL.md` 路径

### 2.2 子命令 SKILL.md × 7

| 子命令 | 路径 | 承载内容 |
|---|---|---|
| `ver` | `skills/code/references/ver/SKILL.md` | 看板模式 + 版本切换 + 发布检查 + 初始化(4 大模式) |
| `req` | `skills/code/references/req/SKILL.md` | 7 阶段流程(INIT/REQUIRE/DESIGN/PLAN/CODING/CHECK/DONE) |
| `fix` | `skills/code/references/fix/SKILL.md` | 6 阶段流程(INIT/DESIGN/PLAN/CODING/CHECK/DONE) |
| `faq` | `skills/code/references/faq/SKILL.md` | 查询模式 + 导出模式(--require/--design/--summary/--template) |
| `rule` | `skills/code/references/rule/SKILL.md` | 编码规范追加/扩展(仅追加,严禁重写) |
| `merge` | `skills/code/references/merge/SKILL.md` | worktree 自动合回主干 |
| `help` | `skills/code/references/help/SKILL.md` | §A 完整 / §B 参数错误 / §C 子命令异常下沉 / §D 输出规范 |

### 2.3 目录结构决策

**关键决策 1**:子命令 SKILL.md 放在 `references/<子命令>/SKILL.md` 而非平铺。

理由:
- `references/` 已经按子命令分子目录(现有结构:`references/ver/common.md`、`references/req/coding.md` 等),延续既有的"子命令资源聚合目录"语义
- 子命令 SKILL.md 与该子命令的 references/templates 平级,便于一次性发现所有该子命令相关文件
- 不破坏 `templates/` 与 `references/` 的现有引用路径

### 2.4 不抽取的引用文件

按 REQUIRE.md FR-5,以下 references 子文件保持原位,只调整主 SKILL.md 内的引用:
- `references/runtime-environment.md`(根级共享)
- `references/req/{common,require,design,plan,coding,check}.md` + `references/req/languages/*.md`
- `references/fix/fix-register.md`
- `references/ver/common.md`
- `references/faq/common.md`

子命令 SKILL.md 内对它们的引用路径保持不变。

## 3. 接口设计

### 3.1 主 SKILL.md frontmatter(路由入口)

```yaml
---
name: code
description: |
  一体化开发工具集 /code · 首 token 路由到 ver / req / fix / faq / rule / merge / help
  7 个子命令的分派入口。例:`/code ver` 看开发进度,`/code req "..."` 启动需求,
  `/code fix "..."` 修复缺陷,`/code faq "..."` 查知识,`/code rule "..."` 加规范,
  `/code merge` 合并 worktree,`/code help` 看完整帮助
---
```

### 3.2 子命令 SKILL.md frontmatter(每子命令独立)

每个子命令 SKILL.md 的 frontmatter 必须有独立 description,**语义互斥**,确保 Claude Code 通过 description 命中唯一子命令:

```yaml
# ver
---
name: code-ver
description: |
  开发进度看板与版本管理。仅首 token = `ver` 触发。
  看板:`/code ver`(无参数)。切换:`/code ver V0.0.x`。发布:`/code ver --publish`
---

# req
---
name: code-req
description: |
  需求开发 7 阶段全流程。仅首 token = `req` 触发。
  例:`/code req "添加用户登录功能"`、`/code req REQ-00001`、`/code req "..." --auto`
---

# fix
---
name: code-fix
description: |
  缺陷修复 6 阶段全流程。仅首 token = `fix` 触发。
  例:`/code fix "登录页密码框不显示"`、`/code fix BUG-00001`、`/code fix "..." --auto`
---

# faq
---
name: code-faq
description: |
  跨版本知识查询与文档导出。仅首 token = `faq` 触发。
  例:`/code faq "用户登录在哪"`、`/code faq --design REQ-00001 out.md`
---

# rule
---
name: code-rule
description: |
  编码规范追加/扩展。仅首 token = `rule` 触发。
  例:`/code rule "统一用 snake_case 命名"`
---

# merge
---
name: code-merge
description: |
  git worktree 自动合回主干。仅首 token = `merge` 触发。仅在 worktree 中运行
---

# help
---
name: code-help
description: |
  /code 完整帮助与参数异常引导。当首 token 不是 ver/req/fix/faq/rule/merge 时触发,
  或用户输入 `/code`(无任何参数)时触发
---
```

**关键决策 2**:子命令 frontmatter 的 `name` 字段用 `code-<子命令>`(如 `code-ver`),而非复用 `code`。理由:
- 避免与主 SKILL.md 的 `name: code` 冲突
- Claude Code 在 skill 解析时要求每个文件 name 唯一
- 命名一致地表达"这是 /code 的子命令"

### 3.3 plugin.json / marketplace.json 更新

两个配置文件的 `skills` 数组需列出所有 8 个入口(1 主 + 7 子):

```json
"skills": [
  "./skills/code",
  "./skills/code/references/ver",
  "./skills/code/references/req",
  "./skills/code/references/fix",
  "./skills/code/references/faq",
  "./skills/code/references/rule",
  "./skills/code/references/merge",
  "./skills/code/references/help"
]
```

**关键决策 3**:`./skills/code/references/<子命令>` 的引用方式。Claude Code 的 skill 协议要求每个入口是一个目录(内含 SKILL.md),所以这里列出的是目录而非文件。

## 4. 数据设计

无新增数据结构。沿用现有 PROCESS.md / REQUIRE.md 等 markdown 文件。

## 5. 方案选型

### 5.1 子命令 SKILL.md 命名方案

| 方案 | 描述 | 选择 |
|---|---|---|
| **A. 沿用子目录**(`references/<子命令>/SKILL.md`) | 与既有 references 结构一致,无新概念 | ✅ **选定** |
| **B. 平铺**(`skills/code-<子命令>/SKILL.md`) | 隔离感更强,但与 references/ 不平行 | ❌ 不选 |
| **C. 混合**(主同目录,子平铺) | 结构不一致,易混淆 | ❌ 不选 |

理由:references/<子命令>/ 已是子命令资源聚合目录,SKILL.md 是该子命令的"入口文件",放在子目录根部最自然。

### 5.2 子命令 frontmatter name 命名

| 方案 | 描述 | 选择 |
|---|---|---|
| **A. `code-<子命令>`** | 表达"主从"关系 | ✅ **选定** |
| **B. 复用 `code`** | 与主 SKILL.md 同名 | ❌ 冲突 |
| **C. 裸子命令名**(`ver`) | 简短但易冲突 | ❌ 不选 |

## 6. 关键流程

### 6.1 拆分流程

```
[主 SKILL.md 93037 字节]
   ↓  按子命令切片
   ↓
   ├── §0 不变式 + frontmatter + 路由表 ──→ [主 SKILL.md 瘦身版]
   │
   ├── 子命令:`ver` 段 ─────────────────→ references/ver/SKILL.md
   ├── 子命令:`req` 段 ─────────────────→ references/req/SKILL.md
   ├── 子命令:`fix` 段 ─────────────────→ references/fix/SKILL.md
   ├── 子命令:`faq` 段 ─────────────────→ references/faq/SKILL.md
   ├── 子命令:`rule` 段 ────────────────→ references/rule/SKILL.md
   ├── 子命令:`merge` 段 ───────────────→ references/merge/SKILL.md
   │
   └── HELP §A/§B/§C/§D ───────────────→ references/help/SKILL.md
```

### 6.2 路由流程(用户视角)

```
用户输入 /code ver V0.0.5
   ↓
Claude Code 通过 main SKILL.md description 识别入口 → 加载 /code 主 SKILL.md
   ↓
主 SKILL.md 首 token 路由表识别 `ver` → 引用 references/ver/SKILL.md
   ↓
加载 ver 子命令 SKILL.md,执行版本切换
```

```
用户输入 /code xxx(无法识别)
   ↓
主 SKILL.md 首 token 路由失败 → 引用 references/help/SKILL.md
   ↓
加载 help 子命令,显示 §B 参数错误 HELP + 6 选项 AskUserQuestion
```

## 9. 用户确认(本阶段必须执行)

### 9a. 拆分粒度确认

把 SKILL.md 拆为 **1 主 + 7 子** 共 8 个 SKILL.md(主路由 + 6 子命令 + 1 help),请确认。

### 9b. 目录组织确认

子命令 SKILL.md 放在 `references/<子命令>/SKILL.md`(沿用既有 references 子目录),不另立 `skills/code-<子命令>/`。

### 9c. 命名确认

子命令 frontmatter name 字段使用 `code-<子命令>`(如 `code-ver`),与主文件 `name: code` 区分。

> 这些是设计的"做什么"决策,不是"怎么做"的技术选型。**无需用户二次确认**,按推荐方案在 PLAN 阶段落地。

## 10. 与上下游关系

- **下游消费**:无,本次产出仅供 Claude Code 加载
- **上游依赖**:无,基于现有主 SKILL.md
- **横向影响**:plugin.json + marketplace.json 需同步更新

## 11. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-07-21 15:44 | v1 | 初始创建 | 软件设计完成 | wm |
