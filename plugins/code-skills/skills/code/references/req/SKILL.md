---
name: code-req
description: 需求开发 7 阶段全流程。仅首 token = `req` 触发。例:`/code req "添加用户登录功能"`(新建)/ `/code req REQ-00001`(续跑)/ `/code req "..." --confirm`(每阶段强制确认)/ `/code req "..." --auto`(静默全跑通)。严禁走 EnterPlanMode;严禁在 PROCESS.md 最后阶段 ≠ CODING 时改 CWD 源码。
---

# `/code req` — 需求开发

> 流程细节见 [`common.md`](common.md) / [`require.md`](require.md) / [`design.md`](design.md) / [`plan.md`](plan.md) / [`coding.md`](coding.md) / [`check.md`](check.md) / [`runtime-environment.md`](../runtime-environment.md)(根级)/ [`languages/<lang>.md`](languages/)。

## 启动检查(读取本节后立即执行)

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

## 目标

提供需求开发的**全生命周期管理**:
- **需求分析**:将用户输入转化为结构化 REQUIRE.md
- **软件设计**:结合项目现状,产出可被评审的 DESIGN.md
- **任务排期**:将设计拆分为可独立执行的任务 PLAN.md
- **编码执行**:逐任务编码,产出 TASK-N.md 与代码变更
- **代码审查**:系统化审查,发现并修复缺陷,产出 CHECK.md

## 适用场景

- 从零开始开发一个新需求
- 需求已登记,续跑后续阶段(从 PROCESS.md 恢复)
- 任何需要"从需求到代码审查"全流程的场景
- `--auto` 模式:CI/批量场景,无人值守全自动跑通

## 不适用

- 当前**没有激活的版本工作空间**(请先调 `/code ver`)
- 缺陷修复(请调 `/code fix`)
- 仅需单个阶段(如仅需需求分析)→ 也可用,但本技能会询问是否继续下一阶段
- 版本管理/项目初始化(请调 `/code ver`)

## 工作目录约定(强制)

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

## 输入

- **需求描述**(必填):自然语言描述(如 `"添加用户登录功能,支持手机号+密码"`)或需求编号(如 `REQ-00001`)
- **--confirm**(可选):增强确认模式,每个阶段完成后强制确认(提示产出物路径、允许手动修改、确认后重读);与 `--auto` 互斥
- **--auto**(可选):静默模式,所有 `AskUserQuestion` 自动选推荐项,无人值守全自动执行;与 `--confirm` 互斥

## 输出

主产出物(均在 `req/<REQ-NNNNN>/` 下):
- `REQUIRE.md` — 需求分析(FR/NFR/AC)
- `DESIGN.md` — 软件设计(模块/接口/数据/流程/方案选型)
- `PLAN.md` — 任务排期(任务列表/依赖/里程碑)
- `TASK-<序号>.md` × N — 任务完成结果
- `CHECK.md` — 代码审查结果
- `PROCESS.md` — 执行进程(追加式)
- `LOG.md` — 过程记录(可选)
- CWD 下的实际代码变更(CODING 阶段产出)

## 工具使用约定

- 读激活版本:`Read "./assistants/.current-version"`
- 读规范:`Glob "./assistants/rules/**/*"` + `Read`
- 读语言适配:`Read "references/req/languages/<lang>.md"`(CODING 阶段按需)
- 读写产出:`Read`/`Write`/`Edit`(对 `req/<REQ>/` 下文件)
- 改代码:`Edit`/`Write`(对 CWD 下源码,仅在 CODING 阶段)
- 编译/运行/测试:`Bash`(仅在 CODING 阶段,使用语言感知的命令)
- 与用户澄清:优先 `AskUserQuestion`;自然语言兜底

---

## 工作流程

### 强制阶段门控(最高优先级)

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

**反模式**:用户输入 `/code req "对 /code 技能做结构性改造"` → 错误做法:`EnterPlanMode` + 写 plan 文件 → 用 `Edit` 改 SKILL.md。**正确做法**:进入 `INIT` → `REQUIRE`(补完需求)→ `DESIGN`(设计目录结构 + 对外接口)→ `PLAN`(分任务)→ 按任务 `CODING`(每任务产 TASK-N.md)。

**发现反模式**:立即停下,在 `req/<REQ>/PROCESS.md` 追加失败行并退到 INIT 阶段重新开始。

### 步骤 0 — 版本检测 + 恢复执行(强制前置)

> 详见 common.md「版本检测(强制前置)」「PROCESS.md 恢复(断点续跑)」

1. 读取 `./assistants/.current-version`,不存在 → 停下,提示调 `/code ver`
2. 解析用户输入:自然语言描述 → 分配新编号;`REQ-NNNNN` → 直接使用
3. 检查 `req/<REQ-NNNNN>/PROCESS.md` 是否存在:
   - 不存在 → 创建目录 + 初始化 PROCESS.md,从 INIT 阶段开始
   - 存在 → 读取最后一行,确定当前阶段,从中断处继续
4. 若已是 DONE → 提示"已完成,无需重复执行"

### 阶段执行器(通用)

> 详见 common.md「PROCESS.md 追加(强制)」「阶段执行器」

每个阶段按统一模式执行:
1. 追加 PROCESS.md `| <时间> | <阶段> | 开始 | <目标> |`
2. 执行阶段逻辑(详见对应 references)
3. 追加 PROCESS.md `| <时间> | <阶段> | 完成 | <摘要统计> |`
4. 阶段边界确认(三态):
   - `--confirm` 模式 → 增强确认:提示产出物路径 + AskUserQuestion(继续/中止) + 重读产出物
   - `--auto` 模式 → 屏幕输出 `[code req --auto] <阶段> 完成,自动继续`
   - 默认(无 flag) → 自动继续,无输出

阶段顺序: **INIT → REQUIRE → DESIGN → PLAN → CODING → CHECK → DONE**

### 步骤 1 — REQUIRE 阶段(需求分析)

> 详见 require.md

- 新建需求:分配编号,创建目录,初始化 PROCESS.md
- 收集需求材料,提取 FR/NFR/AC,检索关联需求
- 与用户澄清模糊点:需求细节澄清 + 边界条件确认(非 `--auto` 模式)
- 追加 `clarifications.md` 记录问答
- 产出 `REQUIRE.md`,按 `templates/req/REQUIRE.md` 结构,标注"待澄清"和"假设"
- 在 `RESULT.md` 需求清单追加一行

### 步骤 2 — DESIGN 阶段(软件设计)

> 详见 design.md

- 读取 REQUIRE.md,探索项目现状
- 架构方案构思:模块拆分/接口设计/数据结构/关键流程/方案选型
- 与用户确认(非 `--auto`):扩展性确认 + 方案选型确认 + 改修方案确认 + 危险操作确认(涉及移除/变更现有行为时强制)
- 产出 `DESIGN.md`,按 `templates/req/DESIGN.md` 结构
- 不展开到伪代码级别,够 PLAN 阶段拆任务即可

### 步骤 3 — PLAN 阶段(任务排期)

> 详见 plan.md

- 读取 DESIGN.md,按功能点拆分为独立任务
- 与用户确认(非 `--auto`):任务拆分确认 + 优先级确认
- 分析任务依赖,划分里程碑,绘制 Mermaid 依赖图
- 产出 `PLAN.md`,按 `templates/req/PLAN.md` 结构
- 任务编号:`TASK-<REQ-NNNNN>-<序号>`,序号从 00001 开始

### 步骤 4 — CODING 阶段(编码执行)

> 详见 coding.md

- 解析 PLAN.md 任务列表,按依赖顺序逐任务执行
- 每个任务:前置守卫(增强:按 PLAN.md 行序判定,未完成→中止+推荐命令) → 推进状态 → 检测语言类型(加载 `references/req/languages/<lang>.md`) → 读取设计 → 探索代码 → 实施编码(含审查改修特殊规则) → 过程文档自适应判定 → 项目可测性守卫(7 项检查) → 按需写单测(3 类自动判定) → 编译验证(语言感知) → 运行验证(语言感知) → 测试验证(语言感知) → 逻辑行统计(tokei>cloc>heuristic) → 产出 TASK-N.md
- **运行环境约束**(详见 `references/runtime-environment.md`):编译/单测发现运行时缺失时,**先尝试运行一次**(判定为运行时缺失才能触发确认机制),走 4 选项(A 提供路径 / B 授权安装 / C 跳过运行验证 / D 回滚);`--auto` 模式下自动安装运行时;**直接**走包管理器处理缺失的依赖包(无需询问);**不允许**把运行时位置写入文档或记忆
- 编码原则:贴合项目风格,边界显式处理,代码注释不引用追踪编号
- 错误修复循环:区分运行时缺失/依赖包缺失/代码 bug/设计缺陷,最多连续失败 5 次,超过停下询问
- 非 `--auto` 模式:每个任务完成后确认

### 步骤 5 — CHECK 阶段(代码审查)

> 详见 check.md

- 收集审查材料:REQUIRE/DESIGN/PLAN/TASK-N/源码
- 逐维度审查:正确性/需求一致性/设计一致性/规范性/安全性/性能/可维护性/测试覆盖/代码行数超标(新增)
- 分类发现:必须改/建议改/可选
- 评审-编码循环:存在"必须改"→ 生成改修任务 → CODING 修复 → 重新 CHECK → 循环直到无"必须改"(最多 5 轮)
- 对"建议改"询问用户(非 `--auto`)
- 产出 `CHECK.md`,按 `templates/req/CHECK.md` 结构

### 步骤 6 — DONE(收尾)

1. 追加 PROCESS.md `| <时间> | DONE | 完成 | 全部阶段完成 |`
2. 屏幕输出完成报告:各阶段统计摘要
3. **执行兜底提交**(强制,不可跳过):
   - 执行 `Bash: git rev-parse --git-dir 2>/dev/null` → 退出码 ≠ 0 则输出"非 git 仓库,跳过提交"
   - 执行 `Bash: git status --porcelain` → 输出为空则输出"无文件变更,跳过提交"
   - 执行 `Bash: git add -A`
   - 生成 commit message(格式:`chore(code req): <需求编码> <标题>\n\n<阶段统计>`)
   - `--auto` 模式 → 直接执行 `Bash: git commit -m "<message>"`
   - 非 `--auto` 模式 → `AskUserQuestion` 确认后执行 commit
4. 建议下一步:`/code ver` 查看进度,或 `/code ver --publish` 发布

---

## 参数解析

### --confirm 模式

- 每个阶段完成后强制弹出增强确认
- 提示产出物文件路径,允许用户手动修改
- 用户确认继续后重新读取产出物(获取最新修改)
- 选项:A.继续(重读+下一阶段) / B.中止(保存进度,退出)
- 与 `--auto` 互斥,同时传入报错退出

### --auto 模式

- 所有 `AskUserQuestion` 自动选第一项(推荐项)
- 屏幕输出前缀 `[code req --auto]`
- 阶段失败时仍中断(不静默吞错误)
- 与 `--confirm` 互斥,同时传入报错退出

### 三态对比

| 模式 | 阶段边界 | 阶段内内容确认 |
| --- | --- | --- |
| --confirm | 增强确认(路径+重读) | 正常触发 |
| --auto | 自动继续(前缀输出) | 自动选推荐项 |
| 默认(无 flag) | 自动继续(无输出) | 正常触发 |

### 需求编号分配

> 详见 require.md

- 新需求:扫描 `req/REQ-*/` 目录,取最大编号 +1,格式 `REQ-NNNNN`(5 位数字)
- 续跑:用户传入 `REQ-NNNNN` → 直接使用,验证目录存在

---

## 衔接

- **下游**:CHECK 阶段已包含代码审查;`/code ver --publish` 用于发布
- **上游**:`/code ver`(必须,提供激活版本);`/code rule`(项目级规范)
- **横向**:`/code fix`(缺陷修复,复用本技能 references);`/code faq`(查询导出)

## 必须做事项清单

> 以下事项为强制要求,违反即视为本技能执行失败。

### 阶段门控

- **执行前必须**读取 `./assistants/.current-version`;不存在则停下提示用户先调 `/code ver`
- **阶段开始/完成时必须**追加 `PROCESS.md` 一行(详见 `common.md`「PROCESS.md 追加(强制)」)
- **阶段失败时必须**追加 `PROCESS.md` 失败行,不得静默吞错
- **7 阶段顺序必须**严格执行(`INIT → REQUIRE → DESIGN → PLAN → CODING → CHECK → DONE`),严禁合并或跳过(即使 `--auto` 也不能跳过阶段)

### 源码修改窗口

- **修改 CWD 源码必须**仅在 `PROCESS.md` 最后阶段 = `CODING` 时执行(详见不变式 I-3)
- 修改前**必须**先 `git status --porcelain` 检查,已有修改先回退

### 文档与规范

- **代码注释必须**用功能描述,**不得**出现 REQ-NNNNN / BUG-NNNNN / TASK-* 追踪编号
- **修改既有规则文件**时**必须**用 `Edit` 在末尾追加;新建分类**必须**用 `Write` 首次(详见不变式 I-5)
- **修改 `RESULT.md` 时必须**只动本技能负责的区段,不得越界写其他技能区域

### 阶段内操作

- **阶段内澄清问题**每轮**必须**聚焦 1-3 个最阻塞的点(详见 `require.md`「交互确认」)
- **需求冲突必须**用 `AskUserQuestion` 确认,不可仅标注"设计推断"延迟到 DESIGN 阶段(见 `require.md` 阶段内冲突确认)
- **REQUIRE 阶段必须**不做技术选型,归 DESIGN 阶段
- **DESIGN 阶段必须**完成 design.md 全部用户确认(扩展性/方案选型/改修方案/危险操作)
- **危险操作**(移除/变更现有行为)时必须执行 `design.md` 危险操作确认流程
- **CODING 阶段编译/测试前必须**先检测项目语言;未检测则走通用启发式
- **评审-编码循环达到 5 轮上限时必须**停下询问用户
- **审查改修时必须**只处理发现清单中的项;其他问题记入 `deviations.md`,不得擅自越界

### 运行时

- **CODING 阶段编译/测试运行时缺失必须**先尝试运行一次,确认是"运行时缺失"才触发确认机制(见 `references/runtime-environment.md`「适用范围与术语」);严禁未尝试就先询问
- **系统级安装**(`winget`/`brew`/`apt` 等)**必须**经用户明确同意,非 `--auto` 模式需 `AskUserQuestion`
- **运行时配置必须**只以枚举值(机器值)记录,不写路径到 TASK/PROCESS/LOG,不存为 MEMORY 项

### 模式

- **`--auto` 模式下**所有 `AskUserQuestion` 自动选第一项;**默认/--confirm 模式下**阶段内澄清正常触发 `AskUserQuestion`(详见 `common.md`「阶段执行器」)

## 启动纪律自检表(进入步骤 1 之前必读)

执行以下 4 项自检,**全部通过**才能进入步骤 1 REQUIRE 阶段:

| # | 自检项 | 不通过则 |
| --- | --- | --- |
| 1 | `./assistants/.current-version` 存在 | 立即停,提示先调 `/code ver` |
| 2 | 已创建 `req/<REQ-NNNNN>/` 目录 + 初始化 `PROCESS.md` | 立即创建,记入 `\| <时间> \| INIT \| 开始 \| ... \|` |
| 3 | `PROCESS.md` 中已记入"阶段开始"行(不是结束行) | 立即追加 |
| 4 | 当前 CWD 源码未做过任何修改(若已改,回退) | 立即 `git checkout -- <files>` 回退后再继续 |
