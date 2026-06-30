---
name: code-req
description: 需求开发。从需求分析到代码审查,引导你一步步完成功能开发。
---

# code-req — 需求开发

> **⚠️ 强制工作流:本技能必须按以下阶段顺序执行,严禁跳过或合并任何阶段:**
> **INIT → REQUIRE → DESIGN → PLAN → CODING → CHECK → DONE**
>
> **在 PROCESS.md 显示 CODING 阶段之前,严禁使用 Edit/Write 修改 CWD 源码文件。**
> **每个阶段必须独立完成并追加 PROCESS.md 后才能进入下一阶段。**

## 启动检查(读取本文件后立即执行)

1. 读取 `./assistants/.current-version`,不存在 → 停止,提示用户先调 `code-ver`
2. 解析用户输入,分配需求编号(新需求取最大编号+1;已存在则直接使用)
3. 检查 `req/<REQ-NNNNN>/PROCESS.md` 是否存在,不存在则创建目录并初始化 PROCESS.md
4. 从 PROCESS.md 确定当前阶段,开始执行

## 目标
提供需求开发的**全生命周期管理**,将 5 段式主流程合并为单一入口:
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
- 当前**没有激活的版本工作空间**(请先调 `code-ver`)
- 缺陷修复(请调 `code-fix`)
- 仅需单个阶段(如仅需需求分析)→ 也可用,但本技能会询问是否继续下一阶段
- 版本管理/项目初始化(请调 `code-ver`)

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
- **--auto**(可选):静默模式,所有 `AskUserQuestion` 自动选推荐项,无人值守全自动执行

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
- 读语言适配:`Read "./code-req/references/languages/<lang>.md"`(CODING 阶段按需)
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
- 不允许从 INIT 直接跳到 CODING
- 不允许合并 REQUIRE+DESIGN 为一个阶段
- 每个阶段必须独立完成并追加 PROCESS.md 后才能进入下一阶段

### 步骤 0 — 版本检测 + 恢复执行(强制前置)

> 详见 references/common.md §1-§2

1. 读取 `./assistants/.current-version`,不存在 → 停下,提示调 `code-ver`
2. 解析用户输入:自然语言描述 → 分配新编号;`REQ-NNNNN` → 直接使用
3. 检查 `req/<REQ-NNNNN>/PROCESS.md` 是否存在:
   - 不存在 → 创建目录 + 初始化 PROCESS.md,从 INIT 阶段开始
   - 存在 → 读取最后一行,确定当前阶段,从中断处继续
4. 若已是 DONE → 提示"已完成,无需重复执行"

### 阶段执行器(通用)

> 详见 references/common.md §3-§4

每个阶段按统一模式执行:
1. 追加 PROCESS.md `| <时间> | <阶段> | 开始 | <目标> |`
2. 执行阶段逻辑(详见对应 references)
3. 追加 PROCESS.md `| <时间> | <阶段> | 完成 | <摘要统计> |`
4. 非 `--auto` 模式 → `AskUserQuestion` 确认(继续/暂停/取消)
5. `--auto` 模式 → 屏幕输出 `[code-req --auto] <阶段> 完成,自动继续`

阶段顺序: **INIT → REQUIRE → DESIGN → PLAN → CODING → CHECK → DONE**

### 步骤 1 — REQUIRE 阶段(需求分析)

> 详见 references/require.md

- 新建需求:分配编号,创建目录,初始化 PROCESS.md
- 收集需求材料,提取 FR/NFR/AC,检索关联需求
- 与用户澄清模糊点:需求细节澄清 + 边界条件确认(非 `--auto` 模式)
- 追加 `clarifications.md` 记录问答
- 产出 `REQUIRE.md`,按 `templates/REQUIRE.md` 结构,标注"待澄清"和"假设"
- 在 `RESULT.md` 需求清单追加一行

### 步骤 2 — DESIGN 阶段(软件设计)

> 详见 references/design.md

- 读取 REQUIRE.md,探索项目现状
- 架构方案构思:模块拆分/接口设计/数据结构/关键流程/方案选型
- 与用户确认(非 `--auto`):扩展性确认 + 方案选型确认 + 改修方案确认
- 产出 `DESIGN.md`,按 `templates/DESIGN.md` 结构
- 不展开到伪代码级别,够 PLAN 阶段拆任务即可

### 步骤 3 — PLAN 阶段(任务排期)

> 详见 references/plan.md

- 读取 DESIGN.md,按功能点拆分为独立任务
- 与用户确认(非 `--auto`):任务拆分确认 + 优先级确认
- 分析任务依赖,划分里程碑,绘制 Mermaid 依赖图
- 产出 `PLAN.md`,按 `templates/PLAN.md` 结构
- 任务编号:`TASK-<REQ-NNNNN>-<序号>`,序号从 00001 开始

### 步骤 4 — CODING 阶段(编码执行)

> 详见 references/coding.md

- 解析 PLAN.md 任务列表,按依赖顺序逐任务执行
- 每个任务:前置守卫(增强:按 PLAN.md 行序判定,未完成→中止+推荐命令) → 推进状态 → 检测语言类型(加载 `languages/<lang>.md`) → 读取设计 → 探索代码 → 实施编码(含审查改修特殊规则) → 过程文档自适应判定 → 项目可测性守卫(7 项检查) → 按需写单测(3 类自动判定) → 编译验证(语言感知) → 运行验证(语言感知) → 测试验证(语言感知) → 逻辑行统计(tokei>cloc>heuristic) → 产出 TASK-N.md
- 编码原则:贴合项目风格,边界显式处理,代码注释不引用追踪编号
- 错误修复循环:区分代码 bug/设计缺陷/环境问题,最多连续失败 5 次,超过停下询问
- 非 `--auto` 模式:每个任务完成后确认

### 步骤 5 — CHECK 阶段(代码审查)

> 详见 references/check.md

- 收集审查材料:REQUIRE/DESIGN/PLAN/TASK-N/源码
- 逐维度审查:正确性/需求一致性/设计一致性/规范性/安全性/性能/可维护性/测试覆盖/代码行数超标(新增)
- 分类发现:必须改/建议改/可选
- 评审-编码循环:存在"必须改"→ 生成改修任务 → CODING 修复 → 重新 CHECK → 循环直到无"必须改"(最多 5 轮)
- 对"建议改"询问用户(非 `--auto`)
- 产出 `CHECK.md`,按 `templates/CHECK.md` 结构

### 步骤 6 — DONE(收尾)

- 追加 PROCESS.md `| <时间> | DONE | 完成 | 全部阶段完成 |`
- 屏幕输出完成报告:各阶段统计摘要
- 兜底提交代码(详见 references/common.md §10):
  - 非 git 仓库 → 跳过
  - git 仓库有变更 → `git add` + `git commit`
  - `--auto` 模式 → 自动提交,无需确认
  - 非 `--auto` 模式 → 展示 commit message 预览,确认后提交
- 建议下一步:`code-dashboard` 查看进度,或 `code-ver --publish` 发布

---

## 参数解析

### --auto 模式

- 所有 `AskUserQuestion` 自动选第一项(推荐项)
- 屏幕输出前缀 `[code-req --auto]`
- 阶段失败时仍中断(不静默吞错误)
- 暂停选项(B)被跳过,自动选继续(A)

### 需求编号分配

> 详见 references/require.md

- 新需求:扫描 `req/REQ-*/` 目录,取最大编号 +1,格式 `REQ-NNNNN`(5 位数字)
- 续跑:用户传入 `REQ-NNNNN` → 直接使用,验证目录存在

---

## 衔接
- **下游**:`code-check`(已内化在 CHECK 阶段);`code-ver --publish`(发布)
- **上游**:`code-ver`(必须,提供激活版本);`code-rule`(项目级规范)
- **横向**:`code-fix`(缺陷修复,复用本技能 references);`code-faq`(查询导出)

## 不要做的事
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