---
name: code-fix
description: 缺陷修复。从缺陷登记到修复审查,引导你一步步完成问题修复。
---

# code-fix — 缺陷修复

## 目标
提供缺陷修复的**全生命周期管理**,将 4 段式缺陷流程合并为单一入口:
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
- 当前**没有激活的版本工作空间**(请先调 `code-ver`)
- 需求开发(请调 `code-req`)
- 仅需单个阶段(如仅需缺陷登记)→ 也可用,但本技能会询问是否继续下一阶段
- 版本管理/项目初始化(请调 `code-ver`)

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
- **--auto**(可选):静默模式,所有 `AskUserQuestion` 自动选推荐项,无人值守全自动执行

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

### 步骤 0 — 版本检测 + 恢复执行(强制前置)

> 详见 ../code-req/references/common.md §1-§2

1. 读取 `./assistants/.current-version`,不存在 → 停下,提示调 `code-ver`
2. 解析用户输入:自然语言描述 → 分配新编号;`BUG-NNNNN` → 直接使用
3. 检查 `fix/<BUG-NNNNN>/PROCESS.md` 是否存在:
   - 不存在 → 创建目录 + 初始化 PROCESS.md,从 INIT 阶段开始
   - 存在 → 读取最后一行,确定当前阶段,从中断处继续
4. 若已是 DONE → 提示"已完成,无需重复执行"

### 阶段执行器(通用)

> 详见 ../code-req/references/common.md §3-§4

每个阶段按统一模式执行:
1. 追加 PROCESS.md `| <时间> | <阶段> | 开始 | <目标> |`
2. 执行阶段逻辑(详见对应 references)
3. 追加 PROCESS.md `| <时间> | <阶段> | 完成 | <摘要统计> |`
4. 非 `--auto` 模式 → `AskUserQuestion` 确认(继续/暂停/取消)
5. `--auto` 模式 → 屏幕输出 `[code-fix --auto] <阶段> 完成,自动继续`

阶段顺序: **INIT → DESIGN → PLAN → CODING → CHECK → DONE**

### 步骤 1 — INIT 阶段(缺陷登记)

> 详见 references/fix-register.md

- 新建缺陷:分配编号,创建目录,初始化 PROCESS.md
- 收集缺陷材料,提取触发条件/可能成因/影响范围/严重程度
- 与用户澄清模糊点(非 `--auto` 模式)
- 产出 `BUG.md`,按 `templates/BUG.md` 结构
- 在 `RESULT.md` 缺陷清单追加一行

### 步骤 2 — DESIGN 阶段(修复设计)

> 详见 ../code-req/references/design.md

- 读取 BUG.md,探索项目现状
- 修复方案构思:涉及模块/接口变更/数据变更/关键流程/方案选型
- 产出 `DESIGN.md`,按 `templates/DESIGN.md` 结构
- 不展开到伪代码级别,够 PLAN 阶段拆任务即可

### 步骤 3 — PLAN 阶段(任务排期)

> 详见 ../code-req/references/plan.md

- 读取 DESIGN.md,按功能点拆分为独立任务
- 分析任务依赖,划分里程碑,绘制 Mermaid 依赖图
- 产出 `PLAN.md`,按 `templates/PLAN.md` 结构
- 任务编号:`TASK-<BUG-NNNNN>-<序号>`,序号从 00001 开始

### 步骤 4 — CODING 阶段(编码执行)

> 详见 ../code-req/references/coding.md

- 解析 PLAN.md 任务列表,按依赖顺序逐任务执行
- 每个任务:前置守卫 → 推进状态 → 读取设计 → 探索代码 → 实施编码 → 编译验证 → 运行验证 → 按需写单测 → 产出 TASK-N.md
- 编码原则:贴合项目风格,边界显式处理,代码注释不引用追踪编号
- 错误修复循环:最多连续失败 5 次,超过停下询问
- 非 `--auto` 模式:每个任务完成后确认

### 步骤 5 — CHECK 阶段(代码审查)

> 详见 ../code-req/references/check.md

- 收集审查材料:BUG/DESIGN/PLAN/TASK-N/源码
- 逐维度审查:正确性/缺陷修复一致性/设计一致性/规范性/安全性/性能/可维护性/测试覆盖
- 分类发现:必须改/建议改/可选
- 对"必须改"自动修复,对"建议改"询问用户(非 `--auto`)
- 产出 `CHECK.md`,按 `templates/CHECK.md` 结构

### 步骤 6 — DONE(完成)

- 追加 PROCESS.md `| <时间> | DONE | 完成 | 全部阶段完成 |`
- 屏幕输出完成报告:各阶段统计摘要
- 建议下一步:`code-dashboard` 查看进度,或 `code-ver --publish` 发布

---

## 参数解析

### --auto 模式

- 所有 `AskUserQuestion` 自动选第一项(推荐项)
- 屏幕输出前缀 `[code-fix --auto]`
- 阶段失败时仍中断(不静默吞错误)
- 暂停选项(B)被跳过,自动选继续(A)

### 缺陷编号分配

> 详见 references/fix-register.md

- 新缺陷:扫描 `fix/BUG-*/` 目录,取最大编号 +1,格式 `BUG-NNNNN`(5 位数字)
- 续跑:用户传入 `BUG-NNNNN` → 直接使用,验证目录存在

---

## 与 code-req 的关系

| 方面 | code-req | code-fix |
| --- | --- | --- |
| 第 1 阶段 | REQUIRE(产出 REQUIRE.md) | INIT(产出 BUG.md) |
| 后续阶段 | DESIGN/PLAN/CODING/CHECK | 复用 code-req references |
| 输出目录 | `req/<REQ-NNNNN>/` | `fix/<BUG-NNNNN>/` |
| 看板区段 | 需求清单 | 缺陷清单 |

## 衔接
- **下游**:`code-ver --publish`(发布)
- **上游**:`code-ver`(必须,提供激活版本);`code-rule`(项目级规范)
- **横向**:`code-req`(需求开发,共享 DESIGN/PLAN/CODING/CHECK references);`code-faq`(查询导出)

## 不要做的事
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