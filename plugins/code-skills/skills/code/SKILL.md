---
name: code
description: 一体化开发工具集合并入口。包含 6 个子命令:ver(版本管理与开发看板——新项目初始化、版本切换、发布检查、无参数显示看板)/ req(需求开发——从需求分析到代码审查全流程)/ fix(缺陷修复——从缺陷登记到修复审查全流程)/ faq(知识查询——跨版本需求与缺陷检索,支持文档导出)/ rule(编码规范——用自然语言描述规则,自动整理为结构化条款)/ merge(分支合并——worktree 自动合回主干,智能解决冲突)。各子命令效果与原独立技能完全一致。
---

# `/code` — 一体化开发工具集

> 本技能合并不久:`/code-ver` → `/code ver`、`/code-req` → `/code req`、以此类推。
> 6 个子命令的输入参数、阶段流程、产出物、错误处理与原独立技能一一对应,**功能完全一致**。

### 关键执行纪律(全局约束)

> 此节是**全局**纪律,**优先于**一切子命令内部的具体规则。任何子命令被调用时,都先看下面 4 条:

1. **子命令识别第一**:每次进入本技能,先看首 token(详见下方"参数提示"小节)
2. **`req` / `fix` 严禁走 `EnterPlanMode`**:它们的 PLAN 阶段已经取代 plan 模式的功能;走 plan 模式 = 直接绕过 7 阶段流程
3. **`req` / `fix` 在 `PROCESS.md` 最后阶段 = `CODING` 之前不得修改 CWD 源代码**:CWD 源码修改唯一合法窗口是 `CODING` 阶段
4. **`/code rule` 也严禁直接 `Edit` 既有规范文件**:`rule` 是"追加 / 扩展",不是"重写"

**违反任一条** = 本技能执行失败,后续必须:
- 立即停手
- 在 `req/<REQ>/PROCESS.md` 或 `fix/<BUG>/PROCESS.md` 追加一行 `| <时间> | <阶段> | 失败 | 违反全局执行纪律 §<N>: <说明> |`
- 回退到 INIT 阶段重新开始(已修改的 CWD 文件用 `git checkout -- <files>` 回退)

---

## 参数提示(后续参数感知)

> Claude Code 在用户输入 `/code ` 后会自动展示本技能的 description(见 frontmatter)。
> 当用户输入 `/code` 后无 token,Claude Code 会进入本技能,本节作为"参数说明"。

### 用法速查

```
/code ver                       → 开发看板(无参数)
/code ver <版本号>               → 切换或创建版本(如 V0.0.5)
/code ver --publish             → 发布检查

/code req <需求描述|REQ-NNNNN>  → 需求开发(可加 --confirm / --auto)
/code fix <缺陷描述|BUG-NNNNN>  → 缺陷修复(可加 --confirm / --auto)

/code faq [查询词]                → 跨版本知识查询
/code faq --require <REQ> <out> → 导出需求文档
/code faq --design <REQ> <out>  → 导出设计文档
/code faq --summary ...         → 设计概要(--design 时可用)
/code faq --template <tpl> ...  → 模板填充(配合 --require / --design)

/code rule <规范描述>           → 添加或扩展编码规范

/code merge [branch]            → worktree 合回主干(默认 origin/main)
```

### 子命令路由

- 首 token ∈ {`ver`, `req`, `fix`, `faq`, `rule`, `merge`} → 触发对应子命令
- 首 token 缺失 / 无法识别 → 输出"可用子命令"列表 + AskUserQuestion 引导

---

## HELPs(帮助)

> 本节定义"在什么情况下显示什么帮助文档"。Claude Code 进入本技能后应先看本节,**先决定行为,再走子命令**。
>
> 与"参数提示"的差别:参数提示是"正常调用时的提示",HELPs 是"参数异常时的引导"。

### 帮助触发条件

| 用户输入形态 | 行为 |
| --- | --- |
| `/code`(无任何参数) | 显示 §A 完整 HELP,然后 `AskUserQuestion` 6 选项引导 |
| `/code ` 加一个空 token | 同上 |
| `/code <未知子命令>` (首 token 不在 `{ver, req, fix, faq, rule, merge}`) | 显示 §B 参数错误 HELP,然后 `AskUserQuestion` 6 选项引导 |
| `/code help` / `/code --help` / `/code -h` | 显示 §A 完整 HELP |
| `/code <子命令>` 子命令已识别,但参数异常(例如 `/code req` 无描述) | 子命令自身处理,见 §C |
| `/code <子命令> <合法参数>` | **跳过帮助**,直接进入子命令 |

### §A — 完整 HELP(`/code` 默认展示)

```
╔══════════════════════════════════════════════════════════════════════════╗
║                          /code  · 一体化开发工具集                         ║
╚══════════════════════════════════════════════════════════════════════════╝

  /code 是合并 6 个原 code-* 技能的单一入口。首 token = 子命令。

┌─────────────────────────────────────────────────────────────────────────┐
│  ver   版本管理与开发看板                                                 │
│    /code ver                       开发进度看板(无参数,推荐先用)         │
│    /code ver <版本号>               切换或创建版本(如 V0.0.5)            │
│    /code ver --publish             发布检查(不切换版本)                  │
│    版本号禁用字符:  /  \  :  *  ?  "  <  >  |  空格                       │
└─────────────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────────────┐
│  req   需求开发 7 阶段全流程                                            │
│    /code req <需求描述>             新建需求(自然语言)                   │
│    /code req REQ-NNNNN              续跑某条已有需求                      │
│    /code req <...> --confirm        每阶段完成后强制确认                  │
│    /code req <...> --auto          静默自动全跑通                        │
│    ⚠ --confirm 与 --auto 互斥,只能选其一                                │
└─────────────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────────────┐
│  fix   缺陷修复 6 阶段全流程                                            │
│    /code fix <缺陷描述>             新建缺陷(自然语言)                   │
│    /code fix BUG-NNNNN              续跑某条已有缺陷                      │
│    /code fix <...> --confirm        每阶段完成后强制确认                  │
│    /code fix <...> --auto          静默自动全跑通                        │
│    ⚠ --confirm 与 --auto 互斥,只能选其一                                │
└─────────────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────────────┐
│  faq   跨版本知识查询与文档导出                                          │
│    /code faq [查询词]                知识查询(可留空)                      │
│    /code faq --require <REQ> <out>  导出需求文档到 <out>                 │
│    /code faq --design <REQ> <out>   导出设计文档到 <out>                 │
│    /code faq --summary             仅与 --design 配合,提取概要           │
│    /code faq --template <tpl>      占位符 {{...}} 模板导出                │
└─────────────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────────────┐
│  rule  编码规范管理                                                     │
│    /code rule "<规范描述>"           用自然语言描述规则,自动归类入库        │
│    规范描述可多行/多条,逐条处理                                         │
└─────────────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────────────┐
│  merge   worktree 自动合回主干                                          │
│    /code merge                     合 origin/main(默认)                  │
│    /code merge <branch>             合 origin/<branch>(自动补全前缀)      │
│    环境变量:                                                            │
│      CODE_MERGE_SCOPE=<scope>      commit message 的 scope                │
│      CODE_MERGE_TARGET=<branch>    合并目标主干                          │
│    ⚠ 仅限 git worktree 内执行                                          │
└─────────────────────────────────────────────────────────────────────────┘

  提示:
    · 首 token 缺失或不是上述 6 个 → 会自动弹出 6 选项
    · 任何阶段都可以补 --confirm 或 --auto(--req/--fix 互斥)
    · 参数不全时,我会先显示本页 HELP 再请你选择
```

#### AskUserQuestion 引导(无参数或参数不全时弹)

```
你想做什么?

A. /code ver          ← 看开发进度(推荐先调)
B. /code req "<需求>" ← 开发新需求
C. /code fix "<缺陷>" ← 修复缺陷
D. /code faq "<关键词>" ← 查需求/缺陷
E. /code rule "<规范>" ← 加编码规范
F. /code merge        ← 合并 worktree

(其他选项可写: 自由输入命令 / 再看一次完整帮助 / 退出)
```

### §B — 参数错误 HELP(首 token 不可识别)

当首 token 不在 `{ver, req, fix, faq, rule, merge}` 时显示:

```
⚠ /code <第一个参数> 不是已识别的子命令。

已识别的 6 个子命令:
  · ver   — 版本管理与开发看板
  · req   — 需求开发
  · fix   — 缺陷修复
  · faq   — 知识查询
  · rule  — 编码规范
  · merge — worktree 合并

常见误用对照:
  /code-req "xxx"     →  /code req "xxx"     (用空格,不再用中横线)
  /code --ver         →  /code ver            (不要给子命令加 --)
  /code help          →  /code                (help 直接调 /code 看完整帮助)
```

随后 `AskUserQuestion` 列出 6 个已识别子命令供选择。

### §C — 子命令内部"参数异常"处理(责任下沉)

子命令已识别但参数异常时,具体错误处理**由各子命令自身承担**,不在 HELPs 集中处理:

| 子命令 | 异常场景 | 处理方式 |
| --- | --- | --- |
| `ver` | 版本号含非法字符、未知 flag | 提示错误 + 退出,沿用原有逻辑 |
| `req` | 无需求描述、`--auto` 与 `--confirm` 同时指定 | 提示"需求描述必填"或 flag 互斥校验 |
| `fix` | 同 req | 同 req |
| `faq` | 未知 flag / `--require` 的 REQ 不存在 / `--summary` 单用 | 各 flag 单独提示与互斥提示 |
| `rule` | 无规范描述 | 主动询问"请用一两句话描述" |
| `merge` | ≥2 个非空参 | 报错退出(E-M8) |

### §D — 输出规范(本 HELP 文档约束)

- HELP 只屏幕输出,**不**落盘任何文件
- HELP 不调用 `Write` / `Edit` / `Bash`,只用 `Read` / `Glob`
- 用户在任意阶段问"怎么用"或"参数是什么"时,直接输出 §A,不重复读取本 SKILL.md
- 显示本 HELP 后立即 `AskUserQuestion`,而不是等待用户重新输入

---

## 子命令索引

| 子命令 | 入口 | 原技能 | 关键能力 |
| --- | --- | --- | --- |
| `ver` | `/code ver` | `code-ver` | 版本管理 + 开发看板 |
| `req` | `/code req` | `code-req` | 需求开发 7 阶段全流程 |
| `fix` | `/code fix` | `code-fix` | 缺陷修复 6 阶段全流程 |
| `faq` | `/code faq` | `code-faq` | 知识查询 + 文档导出 |
| `rule` | `/code rule` | `code-rule` | 编码规范管理 |
| `merge` | `/code merge` | `code-merge` | worktree 自动合并 |

---

## 子命令:`ver` — 版本管理与开发看板

> 替代原 `/code-ver`。所有行为一致。
> 工作流细节见 `references/ver/common.md`。

### 目标

提供版本工作空间的**全生命周期管理**与**开发进度看板**:
- **开发看板**(无参数):一行命令查看当前版本的开发进度、高优先级缺陷、下一步建议
- **新项目**:扫描现有代码,登记基线,建立版本工作空间
- **版本切换**:在多个版本之间切换,可选先发布当前版本
- **发布检查**:检查版本是否可发布,生成部署手册

### 适用场景

- 会话开头总览:调一次 `/code ver` 看到"还差什么"
- 长会话中"接下来做什么":多次 `code-*` 调用之间,获得下一步建议
- 新项目首次接入 `code-skills` 体系
- 启动一个全新版本(如产品发版、独立功能包、季度迭代)
- 在多个并行版本之间切换
- 开发周期末,准备发布到生产环境
- 任何 `/code req` / `/code fix` 调用前,先确认/切换当前工作空间

### 不适用

- 已有激活版本且用户想继续在该版本工作(直接调用其他 `/code *` 子命令即可)
- 项目级规范相关操作(规范在 `./assistants/rules/`,调用 `/code rule`)
- 想修改看板字段/区段 → 看板是只读的,扩展走 `/code rule`
- 想自动登记缺陷/推进任务 → 本技能不写任何文件(除版本管理操作外)

### 工作目录约定(强制)

```
./assistants/
├── rules/                  # 项目级规范(跨版本共享,本技能只读)
├── .current-version        # 当前激活版本标记文件(本技能读写)
└── <版本号>/               # 版本工作空间
    ├── RESULT.md           # 版本开发进度看板(简化版)
    ├── req/<REQ-NNNNN>/
    │   └── PROCESS.md      # 需求执行进度
    └── fix/<BUG-NNNNN>/
        └── PROCESS.md      # 缺陷修复进度
```

- 路径以**当前工作目录(CWD)**为基准
- `rules/` **不**在版本下,跨版本共享
- `.current-version` 是纯文本标记,内容只有版本号字符串
- 本技能**不**修改 `./assistants/rules/` 下的任何内容(只读)
- 本技能**不**修改 `<本仓库>` 中除了 `./assistants` 目录中的其他代码文件
- 看板模式**只读**,不修改任何文件

### 输入

- **0 个参数** → 开发看板模式(版本粒度,显示当前版本进度)
- **版本号**(可选):格式不强求,推荐 `vMAJOR.MINOR.PATCH`(如 `v1.0.0`);不允许包含路径分隔符(`/`、`\`)
- **--publish**(可选):仅执行发布检查,不切换版本

### 输出

- 看板模式:屏幕输出(ASCII 进度条 + 状态分布 + 高优缺陷 + 建议,≤6 行)
- 切换:`./assistants/.current-version` 被覆写为新版本号
- 新建:`./assistants/<版本号>/` 目录 + `./assistants/<版本号>/RESULT.md` 看板
- 初始化:`./assistants/<版本号>/INIT-REPORT.md` + `require/EXISTING-NNN/` 基线需求
- 发布:`./assistants/<版本号>/publish/DEPLOY.md` + `UPDATE.md` + `FAQ.md`

### 工具使用约定

| 模式 | 可用工具 |
| --- | --- |
| 看板模式 | `Read`、`Glob`、`Grep`(只读,不调用 `Write`/`Edit`/`Bash`) |
| 版本管理模式 | `Read`、`Glob`、`Bash`、`Write`、`Edit` |

- 读目录:`Glob` / `Bash: ls`
- 读标记文件:`Read "./assistants/.current-version"`
- 读规范:`Glob "./assistants/rules/**/*"` + `Read`(发布检查时读取编码规范)
- 写标记文件:`Write "./assistants/.current-version"`
- 建目录:`Bash: mkdir -p`
- 写文档:`Write`(首次)/ `Edit`(增量)
- 与用户澄清:优先 `AskUserQuestion`;自然语言兜底

### 工作流程

#### 步骤 0 — 场景检测(强制前置)

> 详见 references/ver/common.md §1

1. 检测 `assistants/` 目录是否存在
2. 检测 `.current-version` 是否存在
3. 解析用户输入(版本号 / --publish / 无参数)
4. 判定场景:
   - 用户传 `--publish` → **发布检查**(步骤 1C-5C)
   - 用户传版本号 → **版本切换**(步骤 1B-6B)
   - 无参数 + (`assistants/` 不存在 或 无 `.current-version`) → **新项目初始化**(步骤 1A-8A)
   - 无参数 + `.current-version` 存在 → **开发看板**(步骤 1D-5D)

---

#### 看板模式(无参数,已初始化项目)

##### 看板输出格式模板

> 以下为屏幕输出的**固定格式模板**,每次执行必须严格按此结构输出。

##### 段 1:总开发进度(单行 ASCII 比例条)

```
[███████████░] 92%
```

- 固定 12 字符宽度,`█`(U+2588)实心 / `░`(U+2591)空心
- 公式:`总进度 = round((Σ需求已完成阶段数 + Σ缺陷已完成阶段数) / (需求数×6 + 缺陷数×5) × 100)%`
- 需求 6 阶段推进(INIT→REQUIRE→DESIGN→PLAN→CODING→CHECK→DONE)
- 缺陷 5 阶段推进(INIT→DESIGN→PLAN→CODING→CHECK→DONE)
- PROCESS.md 不存在 → 视为 0 阶段完成;DONE → 视为全部完成
- 退化(分母=0):`— / 无需求无缺陷,无需进度`

##### 段 2:各状态数量占比(单行)

```
状态: 待编码 0 / 待审查 0
```

- 5 类状态(基于 PROCESS.md 最后阶段判定):

| 状态 | 需求判定 | 缺陷判定 |
| --- | --- | --- |
| 待需求分析 | PROCESS.md 不存在或最后阶段=INIT | (缺陷不经过此状态) |
| 待设计 | 最后阶段=REQUIRE | PROCESS.md 不存在或最后阶段=INIT |
| 待排期 | 最后阶段=DESIGN | 最后阶段=DESIGN |
| 待编码 | 最后阶段=PLAN | 最后阶段=PLAN |
| 待审查 | 最后阶段=CODING | 最后阶段=CODING |

- PROCESS.md 解析失败 → 归入"待需求分析"
- 只展示 N>0 的状态;全 0 时显示 `状态: (无)`

##### 段 3:高优先级缺陷(单行)

```
P0 待修复: █ 2 | P1 待修复: ░ 0
```

- 标记:█(P0 有)/▓(P1 有)/░(无)
- 统计:非已完成/已修复-已验证/已关闭 的 P0/P1 缺陷(字面匹配,不归一化)
- 不展示 P2/P3,不展示具体标题

##### 段 4:后续操作建议(最多 5 行)

```
> /code fix BUG-00001 [高] (依据: P0 待修复 2 个)
> /code req REQ-00020 [中] (依据: 2 个需求待续跑)
> 无后续动作
```

- 单行格式:`> <命令> [<优先级>] (依据: <依据>)`
- 优先级:高/中/低/—
- 每类状态 1 条建议,共 ≤5 条;同状态需求+缺陷并存 → 需求路径优先
- 无触发时显示 `> 无后续动作`

##### 完整输出示例

**正常场景**(有需求有缺陷):
```
[███████████░] 92%
状态: 待编码 0 / 待审查 0
P0 待修复: █ 2 | P1 待修复: ░ 0
> /code fix BUG-00001 [高] (依据: P0 待修复 2 个)
> /code req REQ-00020 [中] (依据: 2 个需求待续跑)
```

**退化场景**(无需求无缺陷):
```
— / 无需求无缺陷,无需进度
状态: (无)
P0 待修复: ░ 0 | P1 待修复: ░ 0
> 无后续动作
```

- 总行数:正常 ≤6 行,退化 ≤4 行

#### 步骤 1D — 版本上下文检测

1. `Read "./assistants/.current-version"`
2. 不存在 → `✗ 未检测到激活的版本工作空间` + 引导 `/code ver <版本号>` + 退出
3. 读取内容记为 `<版本号>`,验证目录存在
4. 目录缺失 → `✗ 版本 <X> 工作空间不存在` + 引导 + 退出

#### 步骤 2D — 数据加载

1. `Read "./assistants/<版本号>/RESULT.md"`(主看板)
2. 缺失 → `✗ 看板文件不存在,请先初始化版本` + 退出
3. `Glob "./assistants/<版本号>/req/REQ-*"` 列出所有需求
4. `Glob "./assistants/<版本号>/fix/BUG-*"` 列出所有缺陷
5. 并行读取所有 `req/<REQ>/PROCESS.md` 和 `fix/<BUG>/PROCESS.md`

#### 步骤 3D — 区段解析

单遍扫描主看板文本:

1. 按 `^## (.+)$` 匹配所有区段标题 + 行号 → `anchors{}`
2. 提取目标区段行区间:
   - 需求清单(总览)
   - 缺陷清单(总览)
3. 在每个区间内,匹配 `^\| .* \|$` 收集表格行(过滤 `^\| ---`)
4. 按 `|` 切分列 → `RequirementRow[]`/`BugRow[]`
5. 任务编号按**算法 4**解析(双正则兼容,详见附录 A)

**L2 退化**:
- 区段缺失 → 返回 `[]`(显示 `(无)`)
- 表格列错位 → 退化到原始 markdown 块原样输出
- 字段值缺失 → 显示 `?` 占位
- 变更记录区段空表(无 `^\| .* \|$` 表格行)→ 屏显 "无变更记录",不报错

#### 步骤 4D — 聚合计算与建议生成

按输出格式模板的 4 段结构,逐段计算:

| 段 | 计算逻辑 |
| --- | --- |
| 段 1 | 遍历所有 PROCESS.md,统计已完成阶段数:需求 6 阶段推进,缺陷 5 阶段推进;PROCESS.md 不存在=0;DONE=全部完成 |
| 段 2 | 按最后阶段归类到 5 类状态,计数;PROCESS.md 解析失败→归入"待需求分析" |
| 段 3 | 从缺陷清单筛 P0/P1 且状态非已完成/已修复-已验证/已关闭,计数 |
| 段 4 | 按建议算法生成建议,取前 5 条 |

**建议算法(5 类优先级)**:

1. **高**:P0 待修复 → `/code fix <BUG>`;需求最后阶段=INIT → `/code req <REQ>`
2. **中**:需求最后阶段=DESIGN → `/code req <REQ>`;缺陷最后阶段=INIT → `/code fix <BUG>`
3. **低**:需求最后阶段=CODING → `/code req <REQ>`
4. **特殊**:全版本已完成(所有 DONE ∧ 无 P0/P1 待修复)→ `/code ver V0.0.x`

**建议命令映射**(严格按既有 `code-*` SKILL.md frontmatter 真实语法):

| 状态 | 需求路径命令 | 缺陷路径命令 |
| --- | --- | --- |
| 待需求分析 | `/code req <REQ>` | — |
| 待设计 | `/code req <REQ>`(续跑) | `/code fix <BUG>`(续跑) |
| 待排期 | `/code req <REQ>`(续跑) | `/code fix <BUG>`(续跑) |
| 待编码 | `/code req <REQ>`(续跑) | `/code fix <BUG>`(续跑) |
| 待审查 | `/code req <REQ>`(续跑) | `/code fix <BUG>`(续跑) |

- 同状态需求+缺陷并存 → 只展示 1 条(需求路径优先)
- 状态无触发 → 不展示该行
- 全部无触发 → `> 无后续动作`

#### 步骤 5D — 屏幕打印

按模板的段 1→段 2→段 3→段 4 顺序打印,退出(无状态保留)。

---

#### 边界与异常(看板模式)

##### L1 启动错误(致命,必须退出)

| 场景 | 触发条件 | 屏幕输出 |
| --- | --- | --- |
| E-1 无激活版本 | `.current-version` 不存在 | `✗ 未检测到激活的版本工作空间` + 引导 `/code ver <版本号>` |
| E-2 版本工作空间不存在 | 目录缺失 | `✗ 版本 <X> 工作空间不存在` + 引导 |
| E-3 看板文件缺失 | `RESULT.md` 不存在 | `✗ 看板文件不存在,请先初始化版本` |

##### L2 数据错误(可降级,继续渲染)

| 场景 | 触发条件 | 处理 |
| --- | --- | --- |
| 区段缺失 | 看板不含目标区段 | 该段显示 `(无)` |
| 表格列错位 | 列数≠期望 | 退化到原始 markdown 块 |
| 字段值缺失 | 单元格为空 | 显示 `?` |
| PROCESS.md 缺失 | 文件不存在 | 视为 0 阶段完成 |
| PROCESS.md 解析失败 | 阶段字段异常 | 归入"待需求分析" |
| 全版本无需求 | 初始化态 | 建议 `/code req`(高) |
| 全版本已完成 | 所有 DONE + 无 P0/P1 待修复 | 建议 `/code ver V0.0.x`(高) |
| 旧格式任务编号 | `REQ-NNNNN-NNNNN` 字面 | 字面透传,不解析路径 |

##### L3 异常兜底

| 场景 | 处理 |
| --- | --- |
| 任何未预期异常 | `✗ 内部错误: <msg>` + 退出 |

---

#### 版本管理模式

##### 步骤 1A — 收集初始版本号

> 详见 references/ver/common.md §2.1

- 默认:`V0.0.0`
- 校验:非空,不含 `/` `\` `:` `*` `?` `"` `<` `>` `|`
- 不与已有版本重名

##### 步骤 2A — 创建 assistants/ 骨架

> 详见 references/ver/common.md §2.2

- 创建 `assistants/`、`assistants/rules/`、`assistants/<版本号>/` 目录
- 不覆盖已存在文件

##### 步骤 3A — 写入 .current-version

> 详见 references/ver/common.md §2.3

- `Write "./assistants/.current-version"`,内容 = `<版本号>\n`

##### 步骤 4A — 写入版本看板 RESULT.md

> 详见 references/ver/common.md §2.4

- 基于简化版 RESULT.md 模板(仅需求清单 + 缺陷清单)
- 填写版本信息、里程碑、变更记录

##### 步骤 5A — 分析现有代码

> 详见 references/ver/common.md §2.5

- 识别项目类型、目录结构、入口与主流程
- 识别已有模块、数据模型、第三方依赖
- 识别编码与构建约定

##### 步骤 6A — 生成 INIT-REPORT.md

> 详见 references/ver/common.md §2.6

- 项目概述、技术栈、目录结构、核心模块、入口与主流程
- 外部接口、数据模型、构建与运行、测试情况
- 可复用资产、已知问题/技术债

##### 步骤 7A — 生成现有功能需求清单

> 详见 references/ver/common.md §2.7

- 按功能拆分(M 个 `EXISTING-NNN`)
- 编号:`EXISTING-NNN`,从 `EXISTING-001` 开始
- 每份 `RESULT.md` 描述功能的现有实现

##### 步骤 8A — 引导用户补齐编码规范

> 详见 references/ver/common.md §2.8

- 检查 `rules/` 是否为空
- 若空,建议调 `/code rule`

---

#### 步骤 1B — 版本切换:读当前版本

> 详见 references/ver/common.md §3.1

1. `Read "./assistants/.current-version"` → 当前激活版本
2. 校验目标版本号合法性
3. 四种情形:
   - **A. 目标版本不存在 + 当前也无激活版本** → 首次创建
   - **B. 目标版本不存在 + 当前已有激活版本** → 创建新版本
   - **C. 目标版本已存在 + 与当前激活版本不同** → 切换
   - **D. 目标版本已存在 + 与当前激活版本相同** → 同版本再确认

#### 步骤 2B — 检查是否需要发布

> 详见 references/ver/common.md §3.2

- 若当前版本有活跃内容(需求清单非空 / 任务清单非空)
- 询问用户:是否先发布当前版本?
  - A. 先发布当前版本,再切换
  - B. 直接切换(不发布)
  - C. 取消

#### 步骤 3B — 执行发布(若用户选择)

> 详见 references/ver/common.md §4

- 走发布检查流程(步骤 1C-5C)
- 若发布不通过,询问是否仍要切换

#### 步骤 4B — 创建/切换到目标版本

> 详见 references/ver/common.md §3.3

- 情形 A/B:创建新版本工作空间,写入 .current-version
- 情形 C:只更新 .current-version
- 情形 D:不做任何文件操作

#### 步骤 5B — CWD 描述文件版本号同步

> 详见 references/ver/common.md §5

#### 步骤 6B — 验证与汇报

> 详见 references/ver/common.md §3.4

---

#### 步骤 1C — 发布前置检查

> 详见 references/ver/common.md §4.1

- 解析 RESULT.md 的需求清单 / 任务清单 / 缺陷清单
- 判定:需求=已完成, 任务=可发布, 缺陷=已修复
- 通过 → 进入步骤 2C
- 不通过 → 输出未完成项明细,退出

#### 步骤 2C — 基线识别

> 详见 references/ver/common.md §4.2

- 列出所有版本,字典序排序
- 本版本 = 最小 → 基线(跳过 UPDATE.md)

#### 步骤 3C — 生成部署手册

> 详见 references/ver/common.md §4.3

- 始终生成:DEPLOY.md
- 非基线:UPDATE.md
- 始终生成:FAQ.md(聚合 `faq/` 目录)

#### 步骤 4C — 创建 faq/ 骨架

> 详见 references/ver/common.md §4.4

- 若 `assistants/faq/` 不存在 → 创建 + README.md

#### 步骤 5C — 报告

> 详见 references/ver/common.md §4.5

---

### 衔接

- **下游**:`/code req`(需求开发)、`/code fix`(缺陷修复)、`/code rule`(编码规范)
- **上游**:无,通常由用户直接发起
- **横向**:`./assistants/rules/` 跨所有版本共享

### 不要做的事(ver)

- 不要在 `./assistants/rules/` 下创建版本子目录
- 不要在版本号中使用 `/` `\` 空格
- 不要在用户没确认的情况下覆盖现有 `RESULT.md`
- 不要在切版本时删除其他版本的目录
- 不要修改项目源代码(初始化时只读分析)
- 不要把分析结果写进 CWD 根目录
- 不要给"现有功能"捏造未实现的细节
- 不要在发布检查通过前生成部署手册
- 不要在**看板模式**下调用 `Write`/`Edit`/`Bash`(只读)
- 不修改 `.current-version`(看板模式只读)
- 不修改 `<版本号>/RESULT.md`(那是 `/code req`/`/code fix` 责任)
- 不归一化状态字面(严格按字面匹配)
- 不把旧格式任务编号改写为新格式(双格式兼容,旧字面透传)

### 附录 A:任务编号解析(算法 4,双正则兼容)

```
parseTaskId(raw):
  // 新格式优先
  m = match(/^TASK-(REQ|BUG)-([A-Za-z0-9.\-_]+)-([A-Za-z0-9.\-_]+)$/, raw)
  if m: return { format: "new", type: m[1], parentNum: m[2], taskNum: m[3], displayId: raw }
  // 旧格式透传
  m = match(/^(REQ|BUG)-([A-Za-z0-9.\-_]+)-([A-Za-z0-9.\-_]+)$/, raw)
  if m: return { format: "old", type: m[1], parentNum: m[2], taskNum: m[3], displayId: raw }
  return null
```

- 新格式:`TASK-REQ-00001-00001`;旧格式:`REQ-00001-00001`
- 解析失败 → `null` → 调用方按字面显示

### 附录 B:ASCII 比例条(算法 5)

```
renderBar(filled, total):
  if total === 0:
    return "[" + "░" × 12 + "] 0%"
  pct = round(filled / total × 100)
  blocks = round(pct / 100 × 12)
  return "[" + "█" × blocks + "░" × (12 - blocks) + "] " + pct + "%"
```

- 固定 12 字符;`█`实心/`░`空心/`▓`P1 标记

### 附录 C:建议数据结构

```
Suggestion:
  command:  string  // 如 "/code req REQ-00004"
  reason:   string  // 如 "需求待续跑 DESIGN 阶段"
  priority: "高" | "中" | "低" | "—"
```

- 严格匹配既有 SKILL.md frontmatter 真实语法
- 最多 5 条;无触发时显示 `> 无后续动作`

---

## 子命令:`req` — 需求开发

> 替代原 `/code-req`。所有行为一致。
> 流程细节见 `references/req/common.md` / `require.md` / `design.md` / `plan.md` / `coding.md` / `check.md` / `runtime-environment.md`(根级)/ `languages/<lang>.md`。

### 启动检查(读取本节后立即执行)

> ⛔ **关键执行纪律(优先于一切其他考虑)**:
>
> 1. `req` 的产物路径**已严格固定**:`./assistants/<版本>/req/REQ-NNNNN/`。在 `INIT` 阶段完成"创建目录 + 初始化 PROCESS.md"**之前**,任何对 CWD 源代码的 `Edit`/`Write` 操作都是绕道。
> 2. **不得**调 `EnterPlanMode`。`req` 的"先 REQUIRE → DESIGN → PLAN(写 `PLAN.md`)"就是本技能内置的计划机制,代替了 Claude 工具层的 `EnterPlanMode`。
> 3. **不得**因为"用户描述比较复杂 / 需要详细方案"而跳过 7 阶段:`INIT → REQUIRE → DESIGN → PLAN → CODING → CHECK → DONE` 7 个阶段每一阶段都必须有 `PROCESS.md` 记录。
> 4. **不得**直接通过 `Edit`/`Write` 修改 CWD 源代码,除非 `PROCESS.md` 最后阶段 = `CODING`。这是本节 §强制阶段门控 的硬约束。
>
> **违反任一条 = 本技能执行失败**。识别到违反后:
> - 立即停止后续动作
> - 在 `req/<当前 REQ>/PROCESS.md` 追加一行 `| <时间> | <阶段> | 失败 | 违反启动检查: <具体条款> |`
> - 退出,不推进任何阶段

1. 读取 `./assistants/.current-version`,不存在 → 停止,提示用户先调 `/code ver`
2. 解析用户输入,分配需求编号(新需求取最大编号+1;已存在则直接使用)
3. 检查 `req/<REQ-NNNNN>/PROCESS.md` 是否存在,不存在则创建目录 + 初始化 PROCESS.md,**然后立即进入步骤 1 REQUIRE 阶段**
4. 从 PROCESS.md 确定当前阶段,开始执行

### 目标

提供需求开发的**全生命周期管理**,将 5 段式主流程合并为单一入口:
- **需求分析**:将用户输入转化为结构化 REQUIRE.md
- **软件设计**:结合项目现状,产出可被评审的 DESIGN.md
- **任务排期**:将设计拆分为可独立执行的任务 PLAN.md
- **编码执行**:逐任务编码,产出 TASK-N.md 与代码变更
- **代码审查**:系统化审查,发现并修复缺陷,产出 CHECK.md

### 适用场景

- 从零开始开发一个新需求
- 需求已登记,续跑后续阶段(从 PROCESS.md 恢复)
- 任何需要"从需求到代码审查"全流程的场景
- `--auto` 模式:CI/批量场景,无人值守全自动跑通

### 不适用

- 当前**没有激活的版本工作空间**(请先调 `/code ver`)
- 缺陷修复(请调 `/code fix`)
- 仅需单个阶段(如仅需需求分析)→ 也可用,但本技能会询问是否继续下一阶段
- 版本管理/项目初始化(请调 `/code ver`)

### 工作目录约定(强制)

```
./assistants/
├── rules/                  # 项目级规范(跨版本共享,只读)
├── .current-version        # 当前激活版本标记(只读)
└── <版本号>/
    ├── RESULT.md           # 版本看板(本技能在首次创建需求时追加一行)
    └── req/<REQ-NNNNN>/    # 本技能产出
        ├── REQUIRE.md      # 需求分析结果
        ├── DESIGN.md       # 软件设计
        ├── PLAN.md         # 任务排期
        ├── TASK-<序号>.md  # 任务完成结果(每任务一份)
        ├── CHECK.md        # 代码审查结果
        ├── PROCESS.md      # 执行进程(追加式,用于断点续跑)
        └── LOG.md          # 过程记录(可选,非必要不记录)
```

- 路径以**当前工作目录(CWD)**为基准
- `rules/` **不**在版本下,跨版本共享,本技能只读
- 本技能**不**修改 `./assistants/rules/` 下的任何内容
- 本技能是**唯一**被允许修改 `<本仓库>` 中除了 `./assistants` 目录中的其他代码文件的技能(在 CODING 阶段)

### 输入

- **需求描述**(必填):自然语言描述(如 `"添加用户登录功能,支持手机号+密码"`)或需求编号(如 `REQ-00001`)
- **--confirm**(可选):增强确认模式,每个阶段完成后强制确认(提示产出物路径、允许手动修改、确认后重读);与 `--auto` 互斥
- **--auto**(可选):静默模式,所有 `AskUserQuestion` 自动选推荐项,无人值守全自动执行;与 `--confirm` 互斥

### 输出

主产出物(均在 `req/<REQ-NNNNN>/` 下):
- `REQUIRE.md` — 需求分析(FR/NFR/AC)
- `DESIGN.md` — 软件设计(模块/接口/数据/流程/方案选型)
- `PLAN.md` — 任务排期(任务列表/依赖/里程碑)
- `TASK-<序号>.md` × N — 任务完成结果
- `CHECK.md` — 代码审查结果
- `PROCESS.md` — 执行进程(追加式)
- `LOG.md` — 过程记录(可选)
- CWD 下的实际代码变更(CODING 阶段产出)

### 工具使用约定

- 读激活版本:`Read "./assistants/.current-version"`
- 读规范:`Glob "./assistants/rules/**/*"` + `Read`
- 读语言适配:`Read "references/req/languages/<lang>.md"`(CODING 阶段按需)
- 读写产出:`Read`/`Write`/`Edit`(对 `req/<REQ>/` 下文件)
- 改代码:`Edit`/`Write`(对 CWD 下源码,仅在 CODING 阶段)
- 编译/运行/测试:`Bash`(仅在 CODING 阶段,使用语言感知的命令)
- 与用户澄清:优先 `AskUserQuestion`;自然语言兜底

---

### 工作流程

#### 强制阶段门控(最高优先级)

> **本小节优先级高于所有其他指令。违反本小节的行为视为错误,必须立即停止并纠正。**

**1. 代码修改权限**

仅当 `PROCESS.md` 最后一条记录显示当前阶段为 `CODING` 时,才允许使用 `Edit`/`Write` 修改 CWD 下的源码文件(即 `./assistants/` 目录之外的文件)。

| 当前阶段 | 代码修改权限 |
| --- | --- |
| INIT / REQUIRE / DESIGN / PLAN | ❌ 严禁修改 CWD 源码 |
| CODING | ✅ 允许修改 CWD 源码 |
| CHECK / DONE | ❌ 严禁修改 CWD 源码(修复走评审-编码循环) |

- 违反此规则 → 立即停止当前操作,回退任何已做的代码修改,从 INIT 阶段重新开始
- 在非 CODING 阶段,仅允许读写 `./assistants/` 下的工作产物

**2. 产出物存在性校验**

每个阶段启动前,必须验证上一阶段的产出物已存在:

| 当前阶段 | 校验项 | 校验失败处理 |
| --- | --- | --- |
| DESIGN | `REQUIRE.md` 存在 | 退回到 REQUIRE 阶段 |
| PLAN | `DESIGN.md` 存在 | 退回到 DESIGN 阶段 |
| CODING | `PLAN.md` 存在 | 退回到 PLAN 阶段 |
| CHECK | 所有 `TASK-*.md` 存在 | 退回到 CODING 阶段 |

- 校验失败时,追加 PROCESS.md 失败记录,自动退回到上一阶段重新执行

**3. PROCESS.md 同步强制**

每次阶段切换必须追加 PROCESS.md 记录:
- 阶段开始:`| <时间> | <阶段> | 开始 | <目标> |`
- 阶段完成:`| <时间> | <阶段> | 完成 | <摘要> |`
- 阶段失败:`| <时间> | <阶段> | 失败 | <原因> |`

未追加 PROCESS.md 的阶段视为"未执行"。恢复执行时,以 PROCESS.md 最后一条记录为准。

**4. 阶段跳过禁令**

严禁跳过任何阶段。阶段顺序为强制性顺序:**INIT → REQUIRE → DESIGN → PLAN → CODING → CHECK → DONE**。

**5. 流程内禁止激活 Claude Code 的 Plan 模式**

`EnterPlanMode` 是 Claude Code 内置的"开始规划"按钮。**本技能 = 完整的需求开发流程**,`PLAN 阶段`(`PLAN.md`)已经取代了 Plan 模式的作用。

**严禁**:
- 调 `EnterPlanMode`(覆盖整个 7 阶段流程)
- 跳过 REQUIRE / DESIGN 而直接产出代码修改
- 在 CODING 阶段之前用 `Edit`/`Write` 修改任何 CWD 源代码
- 用"用户描述复杂、需要先有一个完整方案再启动"为理由,直接编写源代码

**反模式**:用户输入 `/code req "合并所有 code-* 技能为 1 个"` → 错误做法:`EnterPlanMode` + 写 plan 文件 → 用 `Edit` 改 SKILL.md。**正确做法**:进入 `INIT` → `REQUIRE`(补完需求)→ `DESIGN`(设计目录结构 + 对外接口)→ `PLAN`(分任务)→ 按任务 `CODING`(每任务产 TASK-N.md)。

**发现反模式**:立即停下,在 `req/<REQ>/PROCESS.md` 追加失败行并退到 INIT 阶段重新开始。

#### 步骤 0 — 版本检测 + 恢复执行(强制前置)

> 详见 references/req/common.md §1-§2

1. 读取 `./assistants/.current-version`,不存在 → 停下,提示调 `/code ver`
2. 解析用户输入:自然语言描述 → 分配新编号;`REQ-NNNNN` → 直接使用
3. 检查 `req/<REQ-NNNNN>/PROCESS.md` 是否存在:
   - 不存在 → 创建目录 + 初始化 PROCESS.md,从 INIT 阶段开始
   - 存在 → 读取最后一行,确定当前阶段,从中断处继续
4. 若已是 DONE → 提示"已完成,无需重复执行"

#### 阶段执行器(通用)

> 详见 references/req/common.md §3-§4

每个阶段按统一模式执行:
1. 追加 PROCESS.md `| <时间> | <阶段> | 开始 | <目标> |`
2. 执行阶段逻辑(详见对应 references)
3. 追加 PROCESS.md `| <时间> | <阶段> | 完成 | <摘要统计> |`
4. 阶段边界确认(三态):
   - `--confirm` 模式 → 增强确认:提示产出物路径 + AskUserQuestion(继续/中止) + 重读产出物
   - `--auto` 模式 → 屏幕输出 `[code req --auto] <阶段> 完成,自动继续`
   - 默认(无 flag) → 自动继续,无输出

阶段顺序: **INIT → REQUIRE → DESIGN → PLAN → CODING → CHECK → DONE**

#### 步骤 1 — REQUIRE 阶段(需求分析)

> 详见 references/req/require.md

- 新建需求:分配编号,创建目录,初始化 PROCESS.md
- 收集需求材料,提取 FR/NFR/AC,检索关联需求
- 与用户澄清模糊点:需求细节澄清 + 边界条件确认(非 `--auto` 模式)
- 追加 `clarifications.md` 记录问答
- 产出 `REQUIRE.md`,按 `templates/req/REQUIRE.md` 结构,标注"待澄清"和"假设"
- 在 `RESULT.md` 需求清单追加一行

#### 步骤 2 — DESIGN 阶段(软件设计)

> 详见 references/req/design.md

- 读取 REQUIRE.md,探索项目现状
- 架构方案构思:模块拆分/接口设计/数据结构/关键流程/方案选型
- 与用户确认(非 `--auto`):扩展性确认 + 方案选型确认 + 改修方案确认 + 危险操作确认(涉及移除/变更现有行为时强制)
- 产出 `DESIGN.md`,按 `templates/req/DESIGN.md` 结构
- 不展开到伪代码级别,够 PLAN 阶段拆任务即可

#### 步骤 3 — PLAN 阶段(任务排期)

> 详见 references/req/plan.md

- 读取 DESIGN.md,按功能点拆分为独立任务
- 与用户确认(非 `--auto`):任务拆分确认 + 优先级确认
- 分析任务依赖,划分里程碑,绘制 Mermaid 依赖图
- 产出 `PLAN.md`,按 `templates/req/PLAN.md` 结构
- 任务编号:`TASK-<REQ-NNNNN>-<序号>`,序号从 00001 开始

#### 步骤 4 — CODING 阶段(编码执行)

> 详见 references/req/coding.md

- 解析 PLAN.md 任务列表,按依赖顺序逐任务执行
- 每个任务:前置守卫(增强:按 PLAN.md 行序判定,未完成→中止+推荐命令) → 推进状态 → 检测语言类型(加载 `references/req/languages/<lang>.md`) → 读取设计 → 探索代码 → 实施编码(含审查改修特殊规则) → 过程文档自适应判定 → 项目可测性守卫(7 项检查) → 按需写单测(3 类自动判定) → 编译验证(语言感知) → 运行验证(语言感知) → 测试验证(语言感知) → 逻辑行统计(tokei>cloc>heuristic) → 产出 TASK-N.md
- **运行环境约束**(详见 `references/runtime-environment.md`):编译/单测发现运行时缺失时,**先尝试运行一次**(判定为运行时缺失才能触发确认机制),走 4 选项(A 提供路径 / B 授权安装 / C 跳过运行验证 / D 回滚);`--auto` 模式下自动安装运行时;**直接**走包管理器处理缺失的依赖包(无需询问);**不允许**把运行时位置写入文档或记忆
- 编码原则:贴合项目风格,边界显式处理,代码注释不引用追踪编号
- 错误修复循环:区分运行时缺失/依赖包缺失/代码 bug/设计缺陷,最多连续失败 5 次,超过停下询问
- 非 `--auto` 模式:每个任务完成后确认

#### 步骤 5 — CHECK 阶段(代码审查)

> 详见 references/req/check.md

- 收集审查材料:REQUIRE/DESIGN/PLAN/TASK-N/源码
- 逐维度审查:正确性/需求一致性/设计一致性/规范性/安全性/性能/可维护性/测试覆盖/代码行数超标(新增)
- 分类发现:必须改/建议改/可选
- 评审-编码循环:存在"必须改"→ 生成改修任务 → CODING 修复 → 重新 CHECK → 循环直到无"必须改"(最多 5 轮)
- 对"建议改"询问用户(非 `--auto`)
- 产出 `CHECK.md`,按 `templates/req/CHECK.md` 结构

#### 步骤 6 — DONE(收尾)

1. 追加 PROCESS.md `| <时间> | DONE | 完成 | 全部阶段完成 |`
2. 屏幕输出完成报告:各阶段统计摘要
3. **执行兜底提交**(强制,不可跳过):
   - 执行 `Bash: git rev-parse --git-dir 2>/dev/null` → 退出码 ≠ 0 则输出"非 git 仓库,跳过提交"
   - 执行 `Bash: git status --porcelain` → 输出为空则输出"无文件变更,跳过提交"
   - 执行 `Bash: git add -A`
   - 生成 commit message(格式:`chore(code req): <需求编码> <标题>\n\n<阶段统计>\n\nCo-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`)
   - `--auto` 模式 → 直接执行 `Bash: git commit -m "<message>"`
   - 非 `--auto` 模式 → `AskUserQuestion` 确认后执行 commit
4. 建议下一步:`/code ver` 查看进度,或 `/code ver --publish` 发布

---

### 参数解析(req)

#### --confirm 模式

- 每个阶段完成后强制弹出增强确认
- 提示产出物文件路径,允许用户手动修改
- 用户确认继续后重新读取产出物(获取最新修改)
- 选项:A.继续(重读+下一阶段) / B.中止(保存进度,退出)
- 与 `--auto` 互斥,同时传入报错退出

#### --auto 模式

- 所有 `AskUserQuestion` 自动选第一项(推荐项)
- 屏幕输出前缀 `[code req --auto]`
- 阶段失败时仍中断(不静默吞错误)
- 与 `--confirm` 互斥,同时传入报错退出

#### 三态对比

| 模式 | 阶段边界 | 阶段内内容确认 |
| --- | --- | --- |
| --confirm | 增强确认(路径+重读) | 正常触发 |
| --auto | 自动继续(前缀输出) | 自动选推荐项 |
| 默认(无 flag) | 自动继续(无输出) | 正常触发 |

#### 需求编号分配

> 详见 references/req/require.md

- 新需求:扫描 `req/REQ-*/` 目录,取最大编号 +1,格式 `REQ-NNNNN`(5 位数字)
- 续跑:用户传入 `REQ-NNNNN` → 直接使用,验证目录存在

---

### 衔接

- **下游**:`code-check`(已内化在 CHECK 阶段);`/code ver --publish`(发布)
- **上游**:`/code ver`(必须,提供激活版本);`/code rule`(项目级规范)
- **横向**:`/code fix`(缺陷修复,复用本技能 references);`/code faq`(查询导出)

### 不要做的事(req)

- 不要在没有 `./assistants/.current-version` 的情况下继续执行
- 不要在 CODING 阶段之外修改 CWD 源码
- 不要跳过 PROCESS.md 追加(断点续跑的唯一依据)
- 不要在阶段失败时不追加 PROCESS.md 失败记录
- 不要在 `--auto` 模式下弹出 `AskUserQuestion`
- 不要在代码注释中引用 REQ-NNNNN/BUG-NNNNN/TASK-* 追踪编号
- 不要修改 `./assistants/rules/` 下的任何内容
- 不要修改 `RESULT.md` 中非本技能负责的区段
- 不要在 REQUIRE 阶段做技术选型(归 DESIGN 阶段)
- 不要一次问完所有澄清问题(每轮 1-3 个最阻塞的点)
- 不要在评审-编码循环中超过 5 轮不询问用户
- 不要在未检测项目语言类型的情况下直接执行编译/测试命令
- 不要在审查改修任务中越界修复其他问题(记入 deviations.md)
- 不要在 REQUIRE 阶段将需求冲突标注为"设计推断"而不向用户确认(见 references/req/require.md §5c)
- 不要在 DESIGN 阶段涉及移除/变更现有行为时跳过危险操作确认(见 references/req/design.md §9d)
- 不要在 DESIGN 阶段跳过步骤 9 用户确认(扩展性/方案选型/改修方案/危险操作)
- 不要在 CODING 阶段未尝试执行编译/单测就先询问"是否需要安装运行时"——必须先尝试运行,确认是"运行时缺失"而非"依赖包缺失"才触发确认机制(见 references/runtime-environment.md)
- 不要在 CODING 阶段未经用户同意(非 `--auto`)擅自执行 `winget/brew/apt install` 等系统级安装
- 不要把运行时安装位置、用户提供的运行时路径、PATH 内容等写入 TASK.md / PROCESS.md / LOG.md
- 不要把用户的本地运行时配置存为 MEMORY 项
- **不要调 `EnterPlanMode`**:本技能的 PLAN 阶段(`PLAN.md`)已取代其功能;**plan 模式 = 直接绕过 7 阶段流程的反模式**
- **不要在 `PROCESS.md` 最后阶段 ≠ `CODING` 时用 `Edit`/`Write` 修改 CWD 源代码**:违反即视为本技能执行失败;识别后立即停,在 `req/<REQ>/PROCESS.md` 追加 `| <时间> | <阶段> | 失败 | 违反强制阶段门控 §1:在 <不合法阶段> 阶段修改源代码 |`,然后回退到 INIT 阶段
- **不要因为"用户描述复杂 / 需要先出一个完整方案再动"为理由跳过 REQUIRE 或 DESIGN 直接动源代码**:即使加 `--auto` 也不能合并阶段

### 启动纪律自检表(进入步骤 1 之前必读)

执行以下 4 项自检,**全部通过**才能进入步骤 1 REQUIRE 阶段:

| # | 自检项 | 不通过则 |
| --- | --- | --- |
| 1 | `./assistants/.current-version` 存在 | 立即停,提示先调 `/code ver` |
| 2 | 已创建 `req/<REQ-NNNNN>/` 目录 + 初始化 `PROCESS.md` | 立即创建,记入 `\| <时间> \| INIT \| 开始 \| ... \|` |
| 3 | `PROCESS.md` 中已记入"阶段开始"行(不是结束行) | 立即追加 |
| 4 | 当前 CWD 源码未做过任何修改(若已改,回退) | 立即 `git checkout -- <files>` 回退后再继续 |

---

## 子命令:`fix` — 缺陷修复

> 替代原 `/code-fix`。所有行为一致。
> 流程细节复用 `references/req/` 下文件(`common.md` / `design.md` / `plan.md` / `coding.md` / `check.md` / `runtime-environment.md`),fix 专用资料见 `references/fix/fix-register.md`。

### 启动检查(读取本节后立即执行)

1. 读取 `./assistants/.current-version`,不存在 → 停止,提示用户先调 `/code ver`
2. 解析用户输入,分配缺陷编号(新缺陷取最大编号+1;已存在则直接使用)
3. 检查 `fix/<BUG-NNNNN>/PROCESS.md` 是否存在,不存在则创建目录并初始化 PROCESS.md
4. 从 PROCESS.md 确定当前阶段,开始执行

### 目标

提供缺陷修复的**全生命周期管理**,将 4 段式缺陷流程合并为单一入口:
- **缺陷登记**:将用户输入转化为结构化 BUG.md
- **修复设计**:结合项目现状,产出可被评审的 DESIGN.md
- **任务排期**:将设计拆分为可独立执行的任务 PLAN.md
- **编码执行**:逐任务编码,产出 TASK-N.md 与代码变更
- **代码审查**:系统化审查,发现并修复缺陷,产出 CHECK.md

### 适用场景

- 从零开始修复一个缺陷
- 缺陷已登记,续跑后续阶段(从 PROCESS.md 恢复)
- 任何需要"从缺陷登记到代码审查"全流程的场景
- `--auto` 模式:CI/批量场景,无人值守全自动跑通

### 不适用

- 当前**没有激活的版本工作空间**(请先调 `/code ver`)
- 需求开发(请调 `/code req`)
- 仅需单个阶段(如仅需缺陷登记)→ 也可用,但本技能会询问是否继续下一阶段
- 版本管理/项目初始化(请调 `/code ver`)

### 工作目录约定(强制)

```
./assistants/
├── rules/                  # 项目级规范(跨版本共享,只读)
├── .current-version        # 当前激活版本标记(只读)
└── <版本号>/
    ├── RESULT.md           # 版本看板(本技能在首次创建缺陷时追加一行)
    └── fix/<BUG-NNNNN>/    # 本技能产出
        ├── BUG.md          # 缺陷登记结果
        ├── DESIGN.md       # 修复设计
        ├── PLAN.md         # 任务排期
        ├── TASK-<序号>.md  # 任务完成结果(每任务一份)
        ├── CHECK.md        # 代码审查结果
        ├── PROCESS.md      # 执行进程(追加式,用于断点续跑)
        └── LOG.md          # 过程记录(可选,非必要不记录)
```

- 路径以**当前工作目录(CWD)**为基准
- `rules/` **不**在版本下,跨版本共享,本技能只读
- 本技能**不**修改 `./assistants/rules/` 下的任何内容
- 本技能是**唯一**被允许修改 `<本仓库>` 中除了 `./assistants` 目录中的其他代码文件的技能(在 CODING 阶段)

### 输入

- **缺陷描述**(必填):自然语言描述(如 `"用户报告:登录页密码框不显示"`)或缺陷编号(如 `BUG-00001`)
- **--confirm**(可选):增强确认模式,每个阶段完成后强制确认(提示产出物路径、允许手动修改、确认后重读);与 `--auto` 互斥
- **--auto**(可选):静默模式,所有 `AskUserQuestion` 自动选推荐项,无人值守全自动执行;与 `--confirm` 互斥

### 输出

主产出物(均在 `fix/<BUG-NNNNN>/` 下):
- `BUG.md` — 缺陷登记(缺陷描述/触发条件/可能成因/影响范围)
- `DESIGN.md` — 修复设计(模块/接口/数据/流程/方案选型)
- `PLAN.md` — 任务排期(任务列表/依赖/里程碑)
- `TASK-<序号>.md` × N — 任务完成结果
- `CHECK.md` — 代码审查结果
- `PROCESS.md` — 执行进程(追加式)
- `LOG.md` — 过程记录(可选)
- CWD 下的实际代码变更(CODING 阶段产出)

### 工具使用约定

- 读激活版本:`Read "./assistants/.current-version"`
- 读规范:`Glob "./assistants/rules/**/*"` + `Read`
- 读写产出:`Read`/`Write`/`Edit`(对 `fix/<BUG>/` 下文件)
- 改代码:`Edit`/`Write`(对 CWD 下源码,仅在 CODING 阶段)
- 编译/运行/测试:`Bash`(仅在 CODING 阶段)
- 与用户澄清:优先 `AskUserQuestion`;自然语言兜底

---

### 工作流程

#### 强制阶段门控(最高优先级)

> **本小节优先级高于所有其他指令。违反本小节的行为视为错误,必须立即停止并纠正。**

**1. 代码修改权限**

仅当 `PROCESS.md` 最后一条记录显示当前阶段为 `CODING` 时,才允许使用 `Edit`/`Write` 修改 CWD 下的源码文件。

| 当前阶段 | 代码修改权限 |
| --- | --- |
| INIT / DESIGN / PLAN | ❌ 严禁修改 CWD 源码 |
| CODING | ✅ 允许修改 CWD 源码 |
| CHECK / DONE | ❌ 严禁修改 CWD 源码 |

**2. 产出物存在性校验(强制)**

每个阶段启动前,必须验证上一阶段的产出物已存在。每个阶段完成时,必须产出对应的文档。

| 当前阶段 | 校验项 | 本阶段产出 | 校验失败处理 |
| --- | --- | --- | --- |
| DESIGN | `BUG.md` 存在 | `DESIGN.md` | 退回到 INIT 阶段 |
| PLAN | `DESIGN.md` 存在 | `PLAN.md` | 退回到 DESIGN 阶段 |
| CODING | `PLAN.md` 存在 | `TASK-N.md`(每任务) | 退回到 PLAN 阶段 |
| CHECK | 所有 `TASK-*.md` 存在 | `CHECK.md` | 退回到 CODING 阶段 |

- 校验失败时,追加 PROCESS.md 失败记录,自动退回到上一阶段
- **每个阶段必须产出对应的文档文件**(Write 到 fix/<BUG-NNNNN>/ 下),不可仅记录 PROCESS.md

**3. PROCESS.md 同步强制**

每次阶段切换必须追加 PROCESS.md 记录。未追加 PROCESS.md 的阶段视为"未执行"。

**4. 阶段跳过禁令**

严禁跳过任何阶段。阶段顺序为强制性顺序:**INIT → DESIGN → PLAN → CODING → CHECK → DONE**。

#### 步骤 0 — 版本检测 + 恢复执行(强制前置)

> 详见 references/req/common.md §1-§2

1. 读取 `./assistants/.current-version`,不存在 → 停下,提示调 `/code ver`
2. 解析用户输入:自然语言描述 → 分配新编号;`BUG-NNNNN` → 直接使用
3. 检查 `fix/<BUG-NNNNN>/PROCESS.md` 是否存在:
   - 不存在 → 创建目录 + 初始化 PROCESS.md,从 INIT 阶段开始
   - 存在 → 读取最后一行,确定当前阶段,从中断处继续
4. 若已是 DONE → 提示"已完成,无需重复执行"

#### 阶段执行器(通用)

> 详见 references/req/common.md §3-§4

每个阶段按统一模式执行:
1. 追加 PROCESS.md `| <时间> | <阶段> | 开始 | <目标> |`
2. 执行阶段逻辑(详见对应 references)
3. 追加 PROCESS.md `| <时间> | <阶段> | 完成 | <摘要统计> |`
4. 阶段边界确认(三态):
   - `--confirm` 模式 → 增强确认:提示产出物路径 + AskUserQuestion(继续/中止) + 重读产出物
   - `--auto` 模式 → 屏幕输出 `[code fix --auto] <阶段> 完成,自动继续`
   - 默认(无 flag) → 自动继续,无输出

阶段顺序: **INIT → DESIGN → PLAN → CODING → CHECK → DONE**

#### 步骤 1 — INIT 阶段(缺陷登记)

> 详见 references/fix/fix-register.md

**强制产出**:`fix/<BUG-NNNNN>/BUG.md`

- 新建缺陷:分配编号,创建目录,初始化 PROCESS.md
- 收集缺陷材料,提取触发条件/可能成因/影响范围/严重程度
- 与用户澄清模糊点(非 `--auto` 模式)
- 使用 `Write` 写入 `BUG.md`,按 `templates/fix/BUG.md` 结构
- 在 `RESULT.md` 缺陷清单追加一行

#### 步骤 2 — DESIGN 阶段(修复设计)

> 详见 references/req/design.md

**强制产出**:`fix/<BUG-NNNNN>/DESIGN.md`

- 读取 BUG.md,探索项目现状
- 修复方案构思:涉及模块/接口变更/数据变更/关键流程/方案选型
- 与用户确认(非 `--auto`):扩展性确认 + 方案选型确认 + 改修方案确认 + 危险操作确认(涉及移除/变更现有行为时强制)
- 使用 `Write` 写入 `DESIGN.md`,按 `templates/req/DESIGN.md` 结构
- 不展开到伪代码级别,够 PLAN 阶段拆任务即可

#### 步骤 3 — PLAN 阶段(任务排期)

> 详见 references/req/plan.md

**强制产出**:`fix/<BUG-NNNNN>/PLAN.md`

- 读取 DESIGN.md,按功能点拆分为独立任务
- 分析任务依赖,划分里程碑,绘制 Mermaid 依赖图
- 使用 `Write` 写入 `PLAN.md`,按 `templates/req/PLAN.md` 结构
- 任务编号:`TASK-<BUG-NNNNN>-<序号>`,序号从 00001 开始

#### 步骤 4 — CODING 阶段(编码执行)

> 详见 references/req/coding.md

**强制产出**:`fix/<BUG-NNNNN>/TASK-<序号>.md`(每个任务一份)

**运行环境约束**(详见 `references/runtime-environment.md`):
- 在 CODING 阶段末编译/运行/单测时,若常规命令找不到运行时,需走"运行时确认机制"(见 §2)询问用户,**不得擅自安装运行时**;`--auto` 模式下自动安装
- **直接**走包管理器安装缺失的依赖包(如 `pip install` / `npm install` / `go get`),不需要询问
- **允许**用户放弃后续运行验证:TASK-N.md 中标注"用户跳过"即可,本任务仍然可以完成
- **禁止**把运行时安装位置或用户提供的路径写入 TASK.md / PROCESS.md / LOG.md
- **禁止**把运行时相关信息存储为 MEMORY 项

- 解析 PLAN.md 任务列表,按依赖顺序逐任务执行
- 每个任务:前置守卫 → 推进状态 → 读取设计 → 探索代码 → 实施编码 → 编译验证 → 运行验证 → 按需写单测 → 使用 `Write` 写入 `TASK-<序号>.md`
- 编码原则:贴合项目风格,边界显式处理,代码注释不引用追踪编号
- 错误修复循环:最多连续失败 5 次,超过停下询问
- 非 `--auto` 模式:每个任务完成后确认

#### 步骤 5 — CHECK 阶段(代码审查)

> 详见 references/req/check.md

**强制产出**:`fix/<BUG-NNNNN>/CHECK.md`

- 收集审查材料:BUG/DESIGN/PLAN/TASK-N/源码
- 逐维度审查:正确性/缺陷修复一致性/设计一致性/规范性/安全性/性能/可维护性/测试覆盖
- 分类发现:必须改/建议改/可选
- 对"必须改"自动修复,对"建议改"询问用户(非 `--auto`)
- 使用 `Write` 写入 `CHECK.md`,按 `templates/req/CHECK.md` 结构

#### 步骤 6 — DONE(收尾)

1. 追加 PROCESS.md `| <时间> | DONE | 完成 | 全部阶段完成 |`
2. 屏幕输出完成报告:各阶段统计摘要
3. **执行兜底提交**(强制,不可跳过):
   - 执行 `Bash: git rev-parse --git-dir 2>/dev/null` → 退出码 ≠ 0 则输出"非 git 仓库,跳过提交"
   - 执行 `Bash: git status --porcelain` → 输出为空则输出"无文件变更,跳过提交"
   - 执行 `Bash: git add -A`
   - 生成 commit message(格式:`chore(code fix): <缺陷编号> <标题>\n\n<阶段统计>\n\nCo-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`)
   - `--auto` 模式 → 直接执行 `Bash: git commit -m "<message>"`
   - 非 `--auto` 模式 → `AskUserQuestion` 确认后执行 commit
4. 建议下一步:`/code ver` 查看进度,或 `/code ver --publish` 发布

---

### 参数解析(fix)

#### 三态对比

| 模式 | 阶段边界 | 阶段内内容确认 |
| --- | --- | --- |
| --confirm | 增强确认(路径+重读) | 正常触发 |
| --auto | 自动继续(前缀输出) | 自动选推荐项 |
| 默认(无 flag) | 自动继续(无输出) | 正常触发 |

#### 缺陷编号分配

> 详见 references/fix/fix-register.md

- 新缺陷:扫描 `fix/BUG-*/` 目录,取最大编号 +1,格式 `BUG-NNNNN`(5 位数字)
- 续跑:用户传入 `BUG-NNNNN` → 直接使用,验证目录存在

---

### 与 req 的关系

| 方面 | req | fix |
| --- | --- | --- |
| 第 1 阶段 | REQUIRE(产出 REQUIRE.md) | INIT(产出 BUG.md) |
| 后续阶段 | DESIGN/PLAN/CODING/CHECK | 复用 references/req/ 下设计/排期/编码/审查 |
| 输出目录 | `req/<REQ-NNNNN>/` | `fix/<BUG-NNNNN>/` |
| 看板区段 | 需求清单 | 缺陷清单 |

### 衔接

- **下游**:`/code ver --publish`(发布)
- **上游**:`/code ver`(必须,提供激活版本);`/code rule`(项目级规范)
- **横向**:`/code req`(需求开发,共用 references/req/);`/code faq`(查询导出)

### 不要做的事(fix)

- 不要在没有 `./assistants/.current-version` 的情况下继续执行
- 不要在 CODING 阶段之外修改 CWD 源码
- 不要跳过 PROCESS.md 追加(断点续跑的唯一依据)
- 不要在阶段失败时不追加 PROCESS.md 失败记录
- 不要在 `--auto` 模式下弹出 `AskUserQuestion`
- 不要在代码注释中引用 REQ-NNNNN/BUG-NNNNN/TASK-* 追踪编号
- 不要修改 `./assistants/rules/` 下的任何内容
- 不要修改 `RESULT.md` 中非本技能负责的区段
- 不要在 INIT 阶段做技术选型(归 DESIGN 阶段)
- 不要一次问完所有澄清问题(每轮 1-3 个最阻塞的点)
- 不要在 DESIGN 阶段涉及移除/变更现有行为时跳过危险操作确认(见 references/req/design.md §9d)
- 不要在 DESIGN 阶段跳过步骤 9 用户确认(扩展性/方案选型/改修方案/危险操作)
- 不要在 CODING 阶段未尝试执行编译/单测就先询问"是否需要安装运行时"——必须先尝试运行,确认是"运行时缺失"而非"依赖包缺失"才触发确认机制(见 references/runtime-environment.md)
- 不要在 CODING 阶段未经用户同意(非 `--auto`)擅自执行 `winget/brew/apt install` 等系统级安装
- 不要把运行时安装位置、用户提供的运行时路径、PATH 内容等写入 TASK.md / PROCESS.md / LOG.md
- 不要把用户的本地运行时配置存为 MEMORY 项
- **不要调 `EnterPlanMode`**:本技能的 PLAN 阶段(`PLAN.md`)已取代其功能
- **不要在 `PROCESS.md` 最后阶段 ≠ `CODING` 时用 `Edit`/`Write` 修改 CWD 源代码**:识别后立即停,`fix/<BUG>/PROCESS.md` 追加失败行,回退到 INIT

### 启动纪律自检表(fix,进入步骤 1 之前必读)

| # | 自检项 | 不通过则 |
| --- | --- | --- |
| 1 | `./assistants/.current-version` 存在 | 立即停,提示先调 `/code ver` |
| 2 | 已创建 `fix/<BUG-NNNNN>/` 目录 + 初始化 `PROCESS.md` | 立即创建,记入 `\| <时间> \| INIT \| 开始 \| ... \|` |
| 3 | `PROCESS.md` 中已记入"阶段开始"行(不是结束行) | 立即追加 |
| 4 | 当前 CWD 源码未做过任何修改(若已改,回退) | 立即 `git checkout -- <files>` 回退后再继续 |

---

## 子命令:`faq` — 知识查询

> 替代原 `/code-faq`。所有行为一致。
> 流程细节见 `references/faq/common.md`。

### 目标

提供跨版本的知识查询与文档导出能力:
- **知识查询**:跨版本搜索需求/缺陷/功能定义,回答用户问题
- **文档导出**:将需求分析、软件设计、概要信息导出为独立文档

### 适用场景

- 查询某个功能在哪个版本中定义/修改
- 跨版本检索需求或缺陷的详细信息
- 将需求文档导出为独立文件(`--require`)
- 将设计文档导出为独立文件(`--design`)
- 从设计文档中提取概要信息(`--summary`)
- 使用自定义模板格式化导出内容(`--template`)

### 不适用

- 当前**没有激活的版本工作空间**(请先调 `/code ver`;仅查询可不激活)
- 创建/修改需求(请调 `/code req`)
- 创建/修改缺陷(请调 `/code fix`)
- 版本管理/项目初始化(请调 `/code ver`)

### 工作目录约定(强制)

```
./assistants/
├── rules/                  # 项目级规范(跨版本共享,只读)
├── .current-version        # 当前激活版本标记(只读,仅查询可不激活)
└── <版本号>/
    ├── RESULT.md           # 版本看板(本技能只读)
    ├── req/<REQ-NNNNN>/    # 需求文档(本技能只读)
    │   ├── REQUIRE.md
    │   ├── DESIGN.md
    │   └── ...
    └── fix/<BUG-NNNNN>/    # 缺陷文档(本技能只读)
        ├── BUG.md
        ├── DESIGN.md
        └── ...
```

- 路径以**当前工作目录(CWD)**为基准
- 本技能**只读**所有文件,不修改 `./assistants/` 下的任何内容
- 导出文件写入**用户指定路径**(CWD 下或任意位置)
- 本技能**不**修改 `<本仓库>` 中 `./assistants` 目录以外的代码文件

### 输入

- **查询词**(可选):自然语言查询(如 `"用户登录功能在哪?"`)
- **--require <REQ-NNNNN> <输出路径>**:导出需求文档
- **--design <REQ-NNNNN> <输出路径>**:导出设计文档
- **--summary**:与 `--design` 配合,从 DESIGN.md 提取概要信息后导出
- **--template <模板路径>**:指定导出模板,将文档内容填充到模板中

### 输出

- **查询模式**:屏幕输出回答(含来源版本/需求编号/缺陷编号)
- **导出模式**:用户指定路径下的导出文件
- 本技能**不**写入 `./assistants/` 下的任何文件

### 工具使用约定

- 读激活版本:`Read "./assistants/.current-version"`
- 读规范:`Glob "./assistants/rules/**/*"` + `Read`
- 读文档:`Read`(对 `req/`/`fix/` 下文件)
- 跨版本搜索:`Glob "./assistants/*/req/**/*"` + `Grep`
- 写导出文件:`Write`(对用户指定路径)
- 与用户澄清:优先 `AskUserQuestion`;自然语言兜底

---

### 工作流程

#### 步骤 0 — 参数解析(强制前置)

> 详见 references/faq/common.md §1

1. 解析用户输入,识别查询词、导出参数(`--require`/`--design`/`--summary`/`--template`)
2. 判定模式:
   - 无导出参数 → **查询模式**(步骤 1Q-4Q)
   - 有 `--require` → **导出需求**(步骤 1E-4E)
   - 有 `--design` → **导出设计**(步骤 1E-4E,含 `--summary` 分支)
   - 有 `--template` + 导出参数 → **模板导出**(步骤 1E-4E,含模板填充)

#### 步骤 1Q — 查询模式:跨版本搜索

> 详见 references/faq/common.md §2

1. 尝试读取 `./assistants/.current-version`(若不存在,仅在全局搜索,不报错)
2. 确定搜索范围:
   - 有激活版本 → 优先搜索当前版本,若无结果再跨版本
   - 无激活版本 → 全局搜索所有版本
3. 搜索策略:
   - `Glob "./assistants/*/req/*/REQUIRE.md"` — 列出所有需求文档
   - `Glob "./assistants/*/fix/*/BUG.md"` — 列出所有缺陷文档
   - `Grep` 查询词 → 匹配文件名/标题/内容
4. 对匹配结果,读取摘要(文档头 + 关键章节),按相关性排序

#### 步骤 2Q — 查询模式:深度读取

> 详见 references/faq/common.md §2.4

1. 对排名前 3 的结果,读取完整文档
2. 提取关键信息:需求标题/FR/NFR/AC 或 缺陷描述/触发条件/影响范围
3. 标注来源:版本号 + 需求/缺陷编号

#### 步骤 3Q — 查询模式:组装回答

> 详见 references/faq/common.md §2.5

屏幕输出格式:
```
## 查询结果: "<查询词>"

### 1. <需求/缺陷标题> (<版本号> · <编号>)
<关键摘要>
来源: assistants/<版本号>/req/<编号>/REQUIRE.md

### 2. ...
```

#### 步骤 4Q — 查询模式:建议下一步

- 若需查看完整文档 → 建议 `--require`/`--design` 导出
- 若需创建新需求 → 建议 `/code req`
- 若需修复缺陷 → 建议 `/code fix`

---

#### 步骤 1E — 导出模式:定位源文档

> 详见 references/faq/common.md §3

1. 读取 `./assistants/.current-version`,不存在 → 停下,提示先调 `/code ver`
2. 根据参数定位源文档:
   - `--require <REQ>` → `assistants/<版本号>/req/<REQ>/REQUIRE.md`
   - `--design <REQ>` → `assistants/<版本号>/req/<REQ>/DESIGN.md`
3. 验证源文档存在,不存在 → 屏显 `⚠ 源文档不存在:<路径>`,退出

#### 步骤 2E — 导出模式:读取与处理

> 详见 references/faq/common.md §3.4

1. `Read` 源文档完整内容
2. 若 `--summary` 已指定:
   - 从 DESIGN.md 提取概要信息:设计概述 + 模块拆分 + 关键决策
   - 去掉详细接口签名/数据结构/算法伪代码
3. 若 `--template` 已指定:
   - `Read` 模板文件(不存在 → 屏显 `⚠ 模板不存在:<路径>`,跳过填充)
   - 扫描 `{{...}}` 占位符,从源文档提取对应数据填充
   - 模板占位符映射表详见 references/faq/common.md §4

#### 步骤 3E — 导出模式:写出文件

> 详见 references/faq/common.md §3.5

1. `Write` 到用户指定路径
2. 屏显: `✓ 导出完成: <输出路径> (<N> 个占位符已替换)`
3. 若目录不存在 → `Bash: mkdir -p` 先创建

#### 步骤 4E — 导出模式:汇报

- 屏显导出摘要:源文档 / 输出路径 / 模式(概要/模板) / 文件大小

---

### 参数解析(faq)

#### --require <REQ-NNNNN> <输出路径>

- 导出 `req/<REQ-NNNNN>/REQUIRE.md` 到指定路径
- 输出格式:`.md` 文件,内容为需求分析全文
- 若 `--template` 同时指定 → 将需求数据填充到模板后写出

#### --design <REQ-NNNNN> <输出路径>

- 导出 `req/<REQ-NNNNN>/DESIGN.md` 到指定路径
- 输出格式:`.md` 文件,内容为软件设计全文
- 若 `--summary` 同时指定 → 提取概要信息后导出
- 若 `--template` 同时指定 → 将设计数据填充到模板后写出

#### --summary

- 仅与 `--design` 配合使用
- 从 DESIGN.md 提取概要信息:
  - 设计概述(§1)
  - 模块拆分(§2,仅模块名+职责,不含详细接口)
  - 关键决策(方案选型章节)
- 不包含:详细接口签名/数据结构定义/算法伪代码

#### --template <模板路径>

- 与 `--require` 或 `--design` 配合使用
- 模板使用 `{{占位符}}` 语法
- 支持占位符详见 references/faq/common.md §4

---

### 衔接

- **下游**:`/code req`(创建需求)、`/code fix`(创建缺陷)
- **上游**:`/code ver`(导出模式必须有激活版本)
- **横向**:`/code ver`(版本管理与开发看板);`/code rule`(项目级规范)

### 不要做的事(faq)

- 不要在导出模式下修改 `./assistants/` 下的任何文件
- 不要在查询模式下修改任何文件
- 不要在无 `--require`/`--design` 时写出文件
- 不要在 `--summary` 与 `--require` 同时指定时生效(`--summary` 仅对 `--design` 有效)
- 不要臆造源文档中不存在的内容
- 不要修改 `./assistants/rules/` 下的任何内容
- 不要在 `--template` 指定的模板不存在时中断(跳过填充,原样输出)
- 不要修改 `<本仓库>` 中除了用户指定输出路径以外的代码文件

---

## 子命令:`rule` — 编码规范管理

> 替代原 `/code-rule`。所有行为一致。
> 当前 SKILL.md 内未抽出独立的 references,模板见 `templates/rule/` 与 `templates/fix/assistants-layout.md`(后者为 assistants/ 目录结构示意)。

### 目标

让用户用最自然的语言描述一条编码规范,本技能负责:
- **澄清**:识别模糊点,用 `AskUserQuestion` 主动追问
- **归类**:把规范归入已知的规范分类(命名/错误处理/安全/性能/...)
- **结构化**:把口语化描述转成结构化条款(含示例/例外/适用范围)
- **落地**:写入 `./assistants/rules/<分类>.md`,供后续所有 `code-*` 子命令消费

**定位**:`rule` 是"规范基建"工具,所有其他 `code-*` 子命令(`req` 等)都把 `./assistants/rules/` 视为**只读**的强约束输入。

### 适用场景

- 启动新项目,需要建立首批编码规范
- 在项目进行中追加新的规范(命名/错误处理/安全/性能/...)
- 发现现有规范有缺口,需要扩展某分类下的条款
- 团队 review 后形成新的规范条目,统一沉淀

### 不适用

- 修改 `./assistants/rules/` 下既有的具体条款内容(本技能只**追加/扩展**,删除/重构请直接用编辑器处理或后续扩展本技能)
- 给单个项目版本打"临时补丁规范"(规范是跨版本共享的,不存在版本级规范)
- 给某一类规范(命名/错误处理)做**整体重写**(本技能只增量)

### 工作目录约定(强制)

本技能**只**操作 `./assistants/` 下的 `rules/` 目录。本技能**不**读写 `./assistants/.current-version` 和 `./assistants/<版本号>/`。

### 输入

- **规范描述**(必填):用户的自然语言,可一段可一句
- **可选补充**:用户可一次给多条(用换行/编号/自然分段),本技能会逐条处理

### 输出

主产出物:`./assistants/rules/<分类>.md` 文件
- 若该分类文件**不存在** → 新建,基于 `templates/rule/rule.md` 模板填充
- 若该分类文件**已存在** → 在文件中**追加**新的"规则 N"小节(不重写既有内容)

**不修改**:`.current-version`、`<版本号>/` 下任何文件、`rules/` 下的其他分类文件。

### 工具使用约定

- 读分类文件:`Glob "./assistants/rules/**/*"` + `Read`
- 探 CWD 根:`Glob "./assistants/rules/*"` + `Bash: ls`
- 建目录:`Bash: mkdir -p "./assistants/rules/"`
- 写规范文件:`Write`(首次) / `Edit`(追加)
- 与用户澄清:**优先使用 `AskUserQuestion`**

---

### 工作流程

#### 步骤 0 — 不需要版本上下文

**与所有其他子命令不同,本技能不需要读取 `./assistants/.current-version`。**
- 规范是跨版本共享的,与具体版本无关
- 即使没有创建过任何版本,本技能仍可正常执行
- 本技能执行过程中**不创建**版本工作空间(那是 `ver` 的职责)

#### 步骤 1 — 探查 `./assistants/` 现状

1. `Bash: ls -la "./assistants/"` 与 `Glob "./assistants/rules/*"`
2. 整理内部状态:`assistants_exists` / `rules_dir_exists` / `existing_rule_files` / `current_version`

#### 步骤 2 — 兜底创建目录

- 若 `./assistants/` 不存在 → `mkdir -p "./assistants/rules/"`
- **绝不**创建 `.current-version` 或 `<版本号>/`(那是 `ver` 的事)

#### 步骤 3 — 收集规范描述

- 若用户已给出规范描述 → 直接使用 `<原始描述>`
- 若用户没有给 → 主动询问"请用一两句话描述你想添加的编码规范"

#### 步骤 4 — 拆分 + 类型识别 + 初步归类

**类型识别**:每条规则归入 **Type A**(规范条款) / **Type B**(CLAUDE.md AI 工作约定) / **Type C**(templates/ 提示) 中的一类。
**初步归类**:Type A 下再细分(C-1 框架 / C-2 依赖 / C-3 命名 / C-4 目录 / C-5 代码风格 / C-6 提交与合并等)。

#### 步骤 5 — 澄清规则细节

对每条规则追问 1-3 个最阻塞的字段(强制级别 / 适用范围 / 正反示例 / 例外场景 / 关联规范)。
**不要一次问完所有字段**。

#### 步骤 6 — 探测目标文件现状

检查 `./assistants/rules/<分类>.md` 是否已存在;识别冲突与重复。

#### 步骤 7 — 写文件

- 文件不存在 → `Write` 基于 `templates/rule/rule.md` 新建
- 文件已存在 → `Edit` 在末尾追加 "规则 N" 小节

#### 步骤 8 — 汇报

向用户汇报:分类、规则简称、强制级别、文件位置、下游影响。

#### 步骤 9 — 多规则与迭代

处理完全部规则后,询问用户"继续追加 / 查看现有清单 / 结束"。

---

### 已有规范识别与冲突处理

为避免规则污染,处理每条规则前必须:
1. 重复检测
2. 冲突检测
3. 跨分类引用

---

### Type B 子流程(AI 工作指引追加)

适用对象:`<本仓库>/CLAUDE.md` 中的"AI 工作约定(由 code-rule 维护)"小节。
新增"指引 N"小节,根据用户描述追加。

### Type C 子流程(模板内容提示追加)

适用对象:`templates/*.md`。
支持末尾追加模式(`## 提示: <主题>`)和内联模式(`### 提示: <字段>`)。

---

### 衔接

- **下游(被消费方)**:`/code req` / `/code fix` / `/code ver` / `/code faq` / `/code merge` 全部会 `Glob "./assistants/rules/**/*"` 读取本技能的产出,作为只读约束
- **上游(本技能的输入)**:用户直接发起的自然语言描述
- **横向**:本技能与 `/code ver` 无依赖关系,可任意顺序调用

### 不要做的事(rule)

- 不要读取或写入 `./assistants/.current-version`(与本技能无关)
- 不要操作 `./assistants/<版本号>/` 下任何文件
- 不要重写已有的规范文件(本技能只**追加/扩展**,不重写)
- 不要在分类未确认时直接写入文件(必须先步骤 4 的分类确认)
- 不要把"必须"和"推荐"的规则混用同一文件头部声明
- 不要在没有澄清强制级别的情况下写入文件
- 不要在没有 `Read` 现有文件的情况下用 `Write` 覆盖
- 不要把音视频/图片等不可直接读取的材料作为规则描述的来源
- 不要替用户决定分类(必须用 `AskUserQuestion` 让用户确认或调整)

---

## 子命令:`merge` — Worktree 模式自动合并

> 替代原 `/code-merge`。所有行为一致。
> 当前 SKILL.md 内未抽出独立的 references。

### 目标

在 git worktree 模式下,把"worktree 内开发 → 主分支合回"流程**完全自动化**:
1. 提交 worktree 内所有未提交文件
2. 拉取并合并主干分支(默认 `origin/main`)
3. LLM 智能解决冲突(看板数据 / 代码 / 文档 / 配置 / 二进制)
4. 看板 2 区段自检
5. 用 `git merge --no-ff` 合回 main

**核心约束**:
- **不**在 worktree 模式外运行(强约束,无 `--no-worktree` 开关)
- **不**产生过程文件 / 结果文件(SKILL.md 在首次创建时已产,执行阶段不再写 SKILL.md)
- **不**自动 `git push` / **不**自动 `git worktree remove`
- **不**回滚已 commit(commit 是 git 原子的)
- **不**调任何其他子技能(`/code ver` / `/code req` / 任何 `code-*`)

### 适用场景

- 用户在 git worktree 中完成某条 REQ 的开发,需把 worktree 合回 main
- 用户在 worktree 中遇到合并冲突,希望 LLM 智能合并
- 合并后希望自动扫描 2 个看板区段,确保统计数据无矛盾

### 不适用

- **不在 worktree 中**(主工作区直接 `git merge` 即可)
- **v1 follow-up 项**(留作 v2):`--ff-only` 开关、`--target <branch>`、自动 `git push`、自动 `git worktree remove`、跨多 worktree 同时合并、自检"自动修复"等
- 紧急线上修复(走 hotfix 流程)
- 修改既有 SKILL.md(本技能**零修改**)

### 工作目录约定(强制)

**版本工作空间**:`./assistants/<版本号>/`(由 `./assistants/.current-version` 决定)。
本技能的目录粒度是**单次执行**(1 次合并 = 1 个完整流程);**不创建**任何独立目录。

```
./assistants/
├── rules/                # 项目级规范(跨版本共享,本技能只读)
├── .current-version      # 当前激活版本标记(本技能只读)
└── <版本号>/
    ├── RESULT.md         # 版本看板(本技能只读消费 + FR-6 扫描)
    ├── req/<需求编码>/   # req 子命令产出(本技能只读)
    └── fix/<缺陷编码>/   # fix 子命令产出(本技能只读)
```

- 本技能**不修改** `./assistants/rules/` 下任何文件
- 本技能**不修改** `<版本号>/RESULT.md`(FR-6 仅**读** + **打印**自检报告)
- 本技能**不修改** 既有 SKILL.md
- 本技能**不**写 `assistants/<版本号>/req/` 或 `fix/` 下的任何文件
- **执行阶段不**写任何 `.md` 过程文件 / 结果文件

### 输入

| 参数 | 类型 | 必填 | 约束 | 缺省行为 |
| --- | --- | --- | --- | --- |
| `<branch>` | string | 可选 | 单个分支名,可省略 `origin/` 前缀(自动补全) | 默认 `origin/main` |
| `CODE_MERGE_SCOPE` | env | 可选 | commit message 的 `<scope>` 段 | 默认 `worktree-merge` |
| `CODE_MERGE_TARGET` | env | 可选 | 合并目标主分支名 | 默认 `main` |

**参数解析**(在步骤 0 之后):
- 0 个非空参 → target = `origin/main`
- 1 个非空参 → target = `<参>`(若不以 `origin/` 开头则补全)
- 2+ 个非空参 → 报错并打印用法(退出码非 0,E-M8)

**示例**:
```
/code merge                  # 默认合并 origin/main
/code merge develop          # 合并 origin/develop
/code merge origin/develop   # 显式前缀
+ CODE_MERGE_SCOPE=my-scope  # 自定义 commit scope
+ CODE_MERGE_TARGET=develop  # 合并到 develop 而非 main
```

### 输出

**3 段式**屏幕输出:

1. **进度日志**(每步一行)
```
=== code merge 启动 ===
worktree 路径: <worktree-path>
源分支: <worktree-branch>
默认目标分支: origin/main
[FR-1] 前置检查 ... ✓ 在 worktree 中 / ✗ dirty N 文件
[FR-2] 提交 worktree 内文件 ...
[FR-3] 拉取并合并主干 ...
[FR-4] 冲突解决(LLM 智能合并)...
[FR-5] 再次确认提交状态 ...
[FR-6] 看板自检(2 区段)...
[FR-7] 合并 worktree 到 main ...
[FR-8] 退出与清理 ...
```

2. **完成报告**(终态)

3. **磁盘输出**:**0 文件**(NFR-1 强约束)

### 退出码

| 退出码 | 含义 | 触发场景 |
| --- | --- | --- |
| 0 | 正常完成 | 全部 FR 走通(含非阻塞警告) |
| 非 0 | 致命错误 | E-M1/M2/M3/M4/M5/M8/M10/M12 |
| 130 | 用户中止 | Ctrl+C(E-M11) |

---

### 工作流程

#### 步骤 0 — 版本上下文检测(强制前置)

1. 读 `./assistants/.current-version` → 记为 `<版本号>`
2. 文件不存在 → 立即停下,提示"未找到 .current-version,请先调 `/code ver`"

> **注意**:本技能**不**做步骤 0a `git pull`(NFR-4 强约束)

#### 步骤 0.5 — 解析主干参数

```
function parseTarget(args):
 if len(args) == 0: return "origin/main"
 if len(args) == 1:
   branch = args[0]
   if not branch.startswith("origin/"):
     branch = "origin/" + branch
   return branch
 if len(args) >= 2:
   print "✗ 参数过多(最多 1 个),用法: /code merge [branch]"
   exit(非 0)  // E-M8
```

#### 步骤 FR-1 — worktree 模式识别 + 前置检查

```
function FR1_preCheck():
 common_dir = exec("git rev-parse --git-common-dir")
 git_dir = exec("git rev-parse --git-dir")

 if common_dir == git_dir:
   print "✗ 不在 worktree 中"
   print " 请先执行: git worktree add <path> -b <branch>"
   exit(非 0)  // E-M1

 status = exec("git status --porcelain")
 if status 非空:
   return DIRTY  // 走 FR-2
 else:
   return CLEAN  // 跳过 FR-2,走 FR-3
```

#### 步骤 FR-2 — 提交 worktree 内未提交文件

```
function FR2_commit():
 scope = env.CODE_MERGE_SCOPE ?? "worktree-merge"
 exec("git add -A")
 staged = exec("git diff --cached --stat")
 if staged 为空:
   print "✓ 无变更,跳过 commit"
   return
 target = parseTarget(args)
 message = f"chore({scope}): merge worktree into {target}"
 result = exec(f'git commit -m "{message}"')
 if result.exit_code != 0:
   print f"✗ commit 失败: {result.stderr}"
   exit(非 0)  // E-M5
 hash = exec("git log -1 --format=%H")
 print f"✓ commit 完成, hash: {hash}"
```

#### 步骤 FR-3 — 拉取并合并主干分支

```
function FR3_fetchMerge(target):
 fetch_result = exec("git fetch origin")
 if fetch_result.exit_code != 0:
   print f"⚠ git fetch 失败: {fetch_result.stderr}"
 merge_result = exec(f"git merge {target} --no-ff")
 if merge_result.exit_code == 0:
   return SUCCESS
 if "CONFLICT" in merge_result.stderr:
   return CONFLICT
 print f"✗ git merge 失败: {merge_result.stderr}"
 exit(非 0)
```

#### 步骤 FR-4 — 冲突解决(LLM 智能合并)

##### 4.1 看板数据冲突(最高优先级)

**触发条件**:冲突文件路径匹配 `assistants/V<版本>/RESULT.md` 或 `req/REQ-*/` / `fix/BUG-*/` 下关键文件。

**合并规则**(LLM 现场实施):
1. **保留双方数据** — 不删除任何一侧的记录
2. **保持顺序一致** — 按时间戳升序;时间戳相同按编号升序
3. **统计数据最终一致** — 合并后必须重新计算区段"统计"行
4. **完成后**:`git add <file>` 标记已解决

##### 4.2 其他类型文件(逐文件分析)

| 文件类型 | 处理方式 |
| --- | --- |
| 代码文件(.py / .ts / .go / .rs / .java 等) | LLM 读双侧 + 智能合并 + 优先保留双侧独有逻辑 |
| 配置文件(.json / .yaml / .toml) | 优先保留双侧字段并集(去重) |
| 文档文件(.md) | 同 4.1 看板数据规则 |
| 二进制文件(.png / .pdf / .mp4 / .mp3 / .zip) | **不**自动合并,留 unmerged + 提示用户(E-M6) |

##### 4.3 失败兜底

- 严重无法解决 → 留 unmerged + 提示用户
- **不**自动 `git add`(避免半成品入库)
- **不阻塞**整体流程

#### 步骤 FR-5 — 再次确认所有文件已提交

```
function FR5_verifyCommit():
 status = exec("git status --porcelain")
 unmerged = exec("git diff --name-only --diff-filter=U")

 if status 非空 且 非 unmerged:
   exec("git add -A")
   scope = env.CODE_MERGE_SCOPE ?? "worktree-merge"
   exec(f'git commit -m "chore({scope}): post-merge cleanup"')
   print "✓ post-merge cleanup 已 commit"

 if unmerged 非空:
   print f"⚠ 仍有 {len(unmerged)} 个 unmerged 文件"

 if status 为空:
   print "✓ 所有文件已提交,准备合回主分支"
```

#### 步骤 FR-6 — 看板自检(2 区段,全自动)

```
function FR6_dashboardCheck():
 version = read("./assistants/.current-version")
 result_md = read(f"assistants/{version}/RESULT.md")

 sections = ["需求清单", "缺陷清单"]

 all_consistent = true
 for section in sections:
   section_start = find_section(result_md, f"^## {section}$")
   table_rows = count_table_rows(result_md, section_start)
   stat_value = extract_stat(result_md, section)

   if table_rows == stat_value:
     print f"✓ {section}: {table_rows} 行 (一致)"
   else:
     print f"✗ {section}: 表格 {table_rows} 行 vs 统计 {stat_value} 行"
     all_consistent = false

 if all_consistent:
   print "✓ 看板自检通过"
 else:
   print "⚠ 看板自检发现问题(非阻塞)"
```

#### 步骤 FR-7 — 合并 worktree 到主分支

```
function FR7_mergeToMain():
 target = env.CODE_MERGE_TARGET ?? "main"

 checkout = exec(f"git checkout {target}")
 if checkout.exit_code != 0:
   print f"✗ git checkout {target} 失败: {checkout.stderr}"
   exit(非 0)

 worktree_branch = exec("git rev-parse --abbrev-ref HEAD", cwd=worktree_path)
 merge_msg = f"Merge branch '{worktree_branch}' into {target}"
 merge = exec(f"git merge {worktree_branch} --no-ff -m \"{merge_msg}\"")
 if merge.exit_code != 0:
   print f"✗ git merge 失败: {merge.stderr}"
   exit(非 0)
```

#### 步骤 FR-8 — 退出与清理

**最终报告**(stdout):
```
=== code merge 完成 ===
 · worktree: <worktree-path>
 · 源分支: <worktree-branch>
 · 目标分支: <target>
 · merge commit: <hash>
 · 看板自检: ✓ 通过 / ⚠ N 个不一致(非阻塞)
 · 退出码: 0
```

**清理(0 操作)**:
- **不**自动 `git push` 到 origin
- **不**自动 `git worktree remove`
- **不**写任何过程/结果文件

---

### 边界与异常

| ID | 场景 | 触发条件 | 退出码 |
| --- | --- | --- | --- |
| E-M1 | 不在 worktree | `git-common-dir == git-dir` | 非 0 |
| E-M2 | main 分支 dirty | `git status` 在 main 上非空 | 非 0 |
| E-M3 | worktree 路径不存在 | (保留) | 非 0 |
| E-M4 | 主干分支不存在 | `git rev-parse --verify origin/main` 失败 | 非 0 |
| E-M5 | pre-commit hook 失败 | FR-2 `git commit` 退出码非 0 | 非 0 |
| E-M6 | 二进制文件冲突 | FR-4 识别为二进制 | 0(警告) |
| E-M7 | 看板自检不一致 | FR-6 2 区段中任一不一致 | 0(警告) |
| E-M8 | 参数错 | 用户传 2+ 个非空参 | 非 0 |
| E-M9 | 主干分支冲突后无法合并 | FR-4 全 unmerged | 0(警告) |
| E-M10 | git 命令不可用 | `git --version` 失败 | 非 0 |
| E-M11 | Ctrl+C 中止 | 用户在执行中按 Ctrl+C | 130 |
| E-M12 | worktree 已被 prune | `git worktree list` 中无当前 path | 非 0 |

---

### 工具使用约定

- **Bash 工具**:执行 git 命令
- **Read 工具**:读 `.current-version` / `RESULT.md` / 冲突文件双方内容
- **Grep 工具**:解析 RESULT.md 区段
- **Glob 工具**:扫描看板数据冲突文件;读取编码规范
- **Write 工具**:**0 使用**
- **Edit 工具**:**0 使用**
- **Skill 工具**:**0 使用**

---

### 衔接

- **下游**:无(本技能为终态)
- **上游**:`/code ver`(必须,提供激活版本);`/code req` 完成后**不**自动调本技能(职责分离)
- **横向**:`/code ver` 看板算法(FR-6 复用其"算法 1 + 算法 5")

### 不要做的事(merge)

- 不要在没有 `.current-version` 的情况下继续(步骤 0 强制)
- 不要在主工作区(非 worktree)中运行本技能(E-M1 立即报错)
- 不要自动 `git push` 到 origin
- 不要自动 `git worktree remove`
- 不要回滚已 commit 的状态
- 不要写任何过程文件 / 结果文件
- 不要调任何其他子技能(INV-9 严守)
- 不要自动 `/code ver --publish` / `/code req --auto` / 任何子技能
- 不要修改既有 SKILL.md
- 不要修改 `marketplace.json` 既有字段
- 不要修改 `plugin.json`
- 不要修改 `./assistants/rules/` 已有规范
- 不要用 `--squash` 合并(必须用 `--no-ff`)
- 不要实现 v1 follow-up 项(`--ff-only` / `--target` / 自动 push / 自动 remove / 跨多 worktree / 自检自动修复)
- 不要在 SKILL.md 中嵌入具体 git 命令模板
- 不要接受 `--no-worktree` 开关
- 不要在异常 / 中止时尝试 flush 任何文件

---

