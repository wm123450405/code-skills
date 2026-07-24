---
name: code-fix
description: 缺陷修复 6 阶段全流程。仅首 token = `fix` 触发。例:`/code fix "登录页密码框不显示"`(新建)/ `/code fix BUG-00001`(续跑)/ `/code fix "..." --confirm`(每阶段强制确认)/ `/code fix "..." --auto`(静默全跑通)。严禁走 EnterPlanMode;严禁在 PROCESS.md 最后阶段 ≠ CODING 时改 CWD 源码。
---

# `/code fix` — 缺陷修复

> 流程细节复用 [`references/req/`](../req/) 下文件(`common.md` / `design.md` / `plan.md` / `coding.md` / `check.md` / `runtime-environment.md`),fix 专用资料见 [`fix-register.md`](fix-register.md)。

## 启动检查(读取本节后立即执行)

1. 读取 `./assistants/.current-version`,不存在 → 停止,提示用户先调 `/code ver`
2. 解析用户输入,分配缺陷编号(新缺陷取最大编号+1;已存在则直接使用)
3. 检查 `fix/<BUG-NNNNN>/PROCESS.md` 是否存在,不存在则创建目录并初始化 PROCESS.md
4. 从 PROCESS.md 确定当前阶段,开始执行

## 目标

提供缺陷修复的**全生命周期管理**:
- **缺陷登记**:将用户输入转化为结构化 BUG.md
- **修复设计**:结合项目现状,产出可被评审的 DESIGN.md
- **任务排期**:将设计拆分为可独立执行的任务 PLAN.md
- **编码执行**:逐任务编码,产出 TASK-N.md 与代码变更
- **代码审查**:系统化审查,发现并修复缺陷,产出 CHECK.md

## 适用场景

- 从零开始修复一个缺陷
- 缺陷已登记,续跑后续阶段(从 PROCESS.md 恢复)
- 任何需要"从缺陷登记到代码审查"全流程的场景
- `--auto` 模式:CI/批量场景,无人值守全自动跑通

## 不适用

- 当前**没有激活的版本工作空间**(请先调 `/code ver`)
- 需求开发(请调 `/code req`)
- 仅需单个阶段(如仅需缺陷登记)→ 也可用,但本技能会询问是否继续下一阶段
- 版本管理/项目初始化(请调 `/code ver`)

## 工作目录约定(强制)

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

## 输入

- **缺陷描述**(必填):自然语言描述(如 `"用户报告:登录页密码框不显示"`)或缺陷编号(如 `BUG-00001`)
- **--confirm**(可选):增强确认模式,每个阶段完成后强制确认(提示产出物路径、允许手动修改、确认后重读);与 `--auto` 互斥
- **--auto**(可选):静默模式,所有 `AskUserQuestion` 自动选推荐项,无人值守全自动执行;与 `--confirm` 互斥

## 输出

主产出物(均在 `fix/<BUG-NNNNN>/` 下):
- `BUG.md` — 缺陷登记(缺陷描述/触发条件/可能成因/影响范围)
- `DESIGN.md` — 修复设计(模块/接口/数据/流程/方案选型)
- `PLAN.md` — 任务排期(任务列表/依赖/里程碑)
- `TASK-<序号>.md` × N — 任务完成结果
- `CHECK.md` — 代码审查结果
- `PROCESS.md` — 执行进程(追加式)
- `LOG.md` — 过程记录(可选)
- CWD 下的实际代码变更(CODING 阶段产出)

## 工具使用约定

- 读激活版本:`Read "./assistants/.current-version"`
- 读规范:`Glob "./assistants/rules/**/*"` + `Read`
- 读写产出:`Read`/`Write`/`Edit`(对 `fix/<BUG>/` 下文件)
- 改代码:`Edit`/`Write`(对 CWD 下源码,仅在 CODING 阶段)
- 编译/运行/测试:`Bash`(仅在 CODING 阶段)
- 与用户澄清:优先 `AskUserQuestion`;自然语言兜底

---

## 工作流程

### 强制阶段门控(最高优先级)

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

### 步骤 0 — 版本检测 + 恢复执行(强制前置)

> 详见 `../req/common.md`「版本检测(强制前置)」「PROCESS.md 恢复(断点续跑)」

1. 读取 `./assistants/.current-version`,不存在 → 停下,提示调 `/code ver`
2. 解析用户输入:自然语言描述 → 分配新编号;`BUG-NNNNN` → 直接使用
3. 检查 `fix/<BUG-NNNNN>/PROCESS.md` 是否存在:
   - 不存在 → 创建目录 + 初始化 PROCESS.md,从 INIT 阶段开始
   - 存在 → 读取最后一行,确定当前阶段,从中断处继续
4. 若已是 DONE → 提示"已完成,无需重复执行"

### 阶段执行器(通用)

> 详见 `../req/common.md`「PROCESS.md 追加(强制)」「阶段执行器」

每个阶段按统一模式执行:
1. 追加 PROCESS.md `| <时间> | <阶段> | 开始 | <目标> |`
2. 执行阶段逻辑(详见对应 references)
3. 追加 PROCESS.md `| <时间> | <阶段> | 完成 | <摘要统计> |`
4. 阶段边界确认(三态):
   - `--confirm` 模式 → 增强确认:提示产出物路径 + AskUserQuestion(继续/中止) + 重读产出物
   - `--auto` 模式 → 屏幕输出 `[code fix --auto] <阶段> 完成,自动继续`
   - 默认(无 flag) → 自动继续,无输出

阶段顺序: **INIT → DESIGN → PLAN → CODING → CHECK → DONE**

### 步骤 1 — INIT 阶段(缺陷登记)

> 详见 fix-register.md

**强制产出**:`fix/<BUG-NNNNN>/BUG.md`

- 新建缺陷:分配编号,创建目录,初始化 PROCESS.md
- 收集缺陷材料,提取触发条件/可能成因/影响范围/严重程度
- 与用户澄清模糊点(非 `--auto` 模式)
- 使用 `Write` 写入 `BUG.md`,按 `templates/fix/BUG.md` 结构
- 在 `RESULT.md` 缺陷清单追加一行

### 步骤 2 — DESIGN 阶段(修复设计)

> 详见 `../req/design.md`

**强制产出**:`fix/<BUG-NNNNN>/DESIGN.md`

- 读取 BUG.md,探索项目现状
- 修复方案构思:涉及模块/接口变更/数据变更/关键流程/方案选型
- 与用户确认(非 `--auto`):扩展性确认 + 方案选型确认 + 改修方案确认 + 危险操作确认(涉及移除/变更现有行为时强制)
- 使用 `Write` 写入 `DESIGN.md`,按 `templates/req/DESIGN.md` 结构
- 不展开到伪代码级别,够 PLAN 阶段拆任务即可

### 步骤 3 — PLAN 阶段(任务排期)

> 详见 `../req/plan.md`

**强制产出**:`fix/<BUG-NNNNN>/PLAN.md`

- 读取 DESIGN.md,按功能点拆分为独立任务
- 分析任务依赖,划分里程碑,绘制 Mermaid 依赖图
- 使用 `Write` 写入 `PLAN.md`,按 `templates/req/PLAN.md` 结构
- 任务编号:`TASK-<BUG-NNNNN>-<序号>`,序号从 00001 开始

### 步骤 4 — CODING 阶段(编码执行)

> 详见 `../req/coding.md`

**强制产出**:`fix/<BUG-NNNNN>/TASK-<序号>.md`(每个任务一份)

**运行环境约束**(详见 `../runtime-environment.md`):
- 在 CODING 阶段末编译/运行/单测时,若常规命令找不到运行时,需走"运行时确认机制"(见「确认提示模板(默认 / --confirm 模式)」)询问用户,**不得擅自安装运行时**;`--auto` 模式下自动安装
- **直接**走包管理器安装缺失的依赖包(如 `pip install` / `npm install` / `go get`),不需要询问
- **允许**用户放弃后续运行验证:TASK-N.md 中标注"用户跳过"即可,本任务仍然可以完成
- **禁止**把运行时安装位置或用户提供的路径写入 TASK.md / PROCESS.md / LOG.md
- **禁止**把运行时相关信息存储为 MEMORY 项

- 解析 PLAN.md 任务列表,按依赖顺序逐任务执行
- 每个任务:前置守卫 → 推进状态 → 读取设计 → 探索代码 → 实施编码 → 编译验证 → 运行验证 → 按需写单测 → 使用 `Write` 写入 `TASK-<序号>.md`
- 编码原则:贴合项目风格,边界显式处理,代码注释不引用追踪编号
- 错误修复循环:最多连续失败 5 次,超过停下询问
- 非 `--auto` 模式:每个任务完成后确认

### 步骤 5 — CHECK 阶段(代码审查)

> 详见 `../req/check.md`

**强制产出**:`fix/<BUG-NNNNN>/CHECK.md`

- 收集审查材料:BUG/DESIGN/PLAN/TASK-N/源码
- 逐维度审查:正确性/缺陷修复一致性/设计一致性/规范性/安全性/性能/可维护性/测试覆盖
- 分类发现:必须改/建议改/可选
- 对"必须改"自动修复,对"建议改"询问用户(非 `--auto`)
- 使用 `Write` 写入 `CHECK.md`,按 `templates/req/CHECK.md` 结构

### 步骤 6 — DONE(收尾)

1. 追加 PROCESS.md `| <时间> | DONE | 完成 | 全部阶段完成 |`
2. 屏幕输出完成报告:各阶段统计摘要
3. **执行兜底提交**(强制,不可跳过):
   - 执行 `Bash: git rev-parse --git-dir 2>/dev/null` → 退出码 ≠ 0 则输出"非 git 仓库,跳过提交"
   - 执行 `Bash: git status --porcelain` → 输出为空则输出"无文件变更,跳过提交"
   - 执行 `Bash: git add -A`
   - 生成 commit message(格式:`chore(code fix): <缺陷编号> <标题>\n\n<阶段统计>`)
   - `--auto` 模式 → 直接执行 `Bash: git commit -m "<message>"`
   - 非 `--auto` 模式 → `AskUserQuestion` 确认后执行 commit
4. 建议下一步:`/code ver` 查看进度,或 `/code ver --publish` 发布

---

## 参数解析

### 三态对比

| 模式 | 阶段边界 | 阶段内内容确认 |
| --- | --- | --- |
| --confirm | 增强确认(路径+重读) | 正常触发 |
| --auto | 自动继续(前缀输出) | 自动选推荐项 |
| 默认(无 flag) | 自动继续(无输出) | 正常触发 |

### 缺陷编号分配

> 详见 fix-register.md

- 新缺陷:扫描 `fix/BUG-*/` 目录,取最大编号 +1,格式 `BUG-NNNNN`(5 位数字)
- 续跑:用户传入 `BUG-NNNNN` → 直接使用,验证目录存在

---

## 与 req 的关系

| 方面 | req | fix |
| --- | --- | --- |
| 第 1 阶段 | REQUIRE(产出 REQUIRE.md) | INIT(产出 BUG.md) |
| 后续阶段 | DESIGN/PLAN/CODING/CHECK | 复用 `../req/` 下设计/排期/编码/审查 |
| 输出目录 | `req/<REQ-NNNNN>/` | `fix/<BUG-NNNNN>/` |
| 看板区段 | 需求清单 | 缺陷清单 |

## 衔接

- **下游**:`/code ver --publish`(发布)
- **上游**:`/code ver`(必须,提供激活版本);`/code rule`(项目级规范)
- **横向**:`/code req`(需求开发,共用 `../req/`);`/code faq`(查询导出)

## 必须做事项清单

> 以下事项为强制要求,违反即视为本技能执行失败。
> 本技能复用 `../req/` references(REPORT/PLAN/CODING/CHECK),阶段内澄清/异常处理与 `/code req` 一致,详见 `../req/SKILL.md` 必须做清单。

### 阶段门控

- **执行前必须**读取 `./assistants/.current-version`;不存在则停下提示用户先调 `/code ver`
- **阶段开始/完成时必须**追加 `fix/<BUG>/PROCESS.md` 一行
- **阶段失败时必须**追加 `PROCESS.md` 失败行,不得静默吞错
- **6 阶段顺序必须**严格执行(`INIT → DESIGN → PLAN → CODING → CHECK → DONE`),严禁合并或跳过

### 源码修改窗口

- **修改 CWD 源码必须**仅在 `PROCESS.md` 最后阶段 = `CODING` 时执行
- **本技能不**经过 REQUIRE 阶段;但**严禁**在 INIT 阶段做技术选型(归 DESIGN 阶段)

### 文档与规范

- **代码注释必须**用功能描述,**不得**出现 BUG-NNNNN / TASK-* 追踪编号
- **修改既有规则文件**时**必须**用 `Edit` 在末尾追加;新建分类**必须**用 `Write` 首次
- **修改 `RESULT.md` 时必须**只动本技能负责的缺陷清单区段,不得越界写需求清单

### 阶段内操作

- **阶段内澄清问题**每轮**必须**聚焦 1-3 个最阻塞的点
- **DESIGN 阶段必须**完成 design.md 全部用户确认(扩展性/方案选型/改修方案/危险操作);复用 `../req/design.md`
- **危险操作**(移除/变更现有行为)时必须执行 `design.md` 危险操作确认流程
- **CODING 阶段编译/测试前必须**先检测项目语言
- **审查改修时必须**只处理发现清单中的项;其他问题记入 `deviations.md`

### 运行时

- **CODING 阶段编译/测试运行时缺失必须**先尝试运行一次,确认是"运行时缺失"才触发确认机制(见 `../runtime-environment.md`「适用范围与术语」)
- **系统级安装**(`winget`/`brew`/`apt` 等)**必须**经用户明确同意
- **运行时配置必须**只以枚举值(机器值)记录,不写路径到 TASK/PROCESS/LOG

### 模式

- **`--auto` 模式下**所有 `AskUserQuestion` 自动选第一项;**默认/--confirm 模式下**阶段内澄清正常触发

## 启动纪律自检表(进入步骤 1 之前必读)

| # | 自检项 | 不通过则 |
| --- | --- | --- |
| 1 | `./assistants/.current-version` 存在 | 立即停,提示先调 `/code ver` |
| 2 | 已创建 `fix/<BUG-NNNNN>/` 目录 + 初始化 `PROCESS.md` | 立即创建,记入 `\| <时间> \| INIT \| 开始 \| ... \|` |
| 3 | `PROCESS.md` 中已记入"阶段开始"行(不是结束行) | 立即追加 |
| 4 | 当前 CWD 源码未做过任何修改(若已改,回退) | 立即 `git checkout -- <files>` 回退后再继续 |
