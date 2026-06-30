# CLAUDE.md

本文件为 Claude Code(claude.ai/code)在本仓库工作时提供指引。

## 仓库用途

`code-skills` 是一套用于走完完整软件开发生命周期的 Claude Code 技能集合,内置**版本感知工作空间管理**:

```
code-ver → code-req → code-fix → code-faq → code-dashboard
 版本管理   需求开发   缺陷修复   知识查询   开发看板

 code-rule  (横向,非主流程) — 编码规范管理
 code-merge (横向,非主流程) — Worktree 自动合并
```

`code-ver` 是**必备的前置门** —— 合并了版本管理、项目初始化、发布检查三种能力:新项目自动检测并初始化;已初始化项目切换版本;当前版本未发布时询问是否先发布再切换。

`code-req` 是**需求开发全流程入口** —— 合并了需求分析、软件设计、任务排期、编码执行、代码审查五阶段,默认交互确认每阶段,`--auto` 静默执行,支持 `PROCESS.md` 断点续跑。

`code-fix` 是**缺陷修复全流程入口** —— 合并了缺陷登记、修复设计、任务排期、编码执行、代码审查五阶段,复用 `code-req` 的 references,同样支持 `--auto` 和断点续跑。

`code-faq` 是**知识查询与文档导出** —— 跨版本查询需求/缺陷,支持 `--require`/`--design`/`--summary`/`--template` 导出。

`code-rule` **不在主流程管道中** —— 它负责维护跨版本共享的 `./assistants/rules/` 目录,主流程中的所有技能都会以只读方式读取该目录作为约束。

`code-merge` **不在主流程管道中** —— 在 git worktree 中完成开发后,一键合回主干:提交未提交文件、拉取主干、LLM 智能解冲突、看板自检、`git merge --no-ff` 合回 main。

`code-dashboard` **不在主流程管道中** —— 只读看板,一行命令查看版本进度,解析简化版 `RESULT.md`(需求清单+缺陷清单)和 `PROCESS.md` 获取进度。

## 仓库结构

本仓库按 Claude Code **marketplace** 协议布局:仓库根承载一个 marketplace 清单,插件本体放在 `plugins/<name>/` 子目录中,这样既能整体发布到 marketplace,也能单插件直接 `claude plugin install` 引用子目录。

```
code-skills/                          ← marketplace 仓库根
├── .claude-plugin/
│   └── marketplace.json              # 插件市场清单(列出 plugins[])
└── plugins/
    └── code-skills/                  ← 插件本体
        ├── .claude-plugin/
        │   └── plugin.json           # 插件自身元信息
        ├── README.md                 # 工作流总览与技能表(中文)
        ├── README.en.md              # 工作流总览与技能表(英文)
        ├── CLAUDE.md                 # 本文件
        └── skills/
            ├── code-ver/             # 版本管理(合并 code-version + code-publish + code-init)
            ├── code-req/             # 需求开发全流程(合并 code-require + design + plan + it + check)
            ├── code-fix/             # 缺陷修复全流程(合并 code-fix + plan + it + check 缺陷路径)
            ├── code-faq/             # 知识查询与文档导出(原 code-answer)
            ├── code-rule/            # 编码规范管理(项目级共享)
            ├── code-merge/           # Worktree 自动合并
            └── code-dashboard/       # 开发看板(只读)
```

## 需与用户确认的约定

本仓库**不包含任何源代码、构建系统、测试框架、Lint 工具或包管理配置**。不要假设存在任何工具链。

如果用户要求执行 `run` / `build` / `lint` / `test` 等操作,请先与用户确认其目标技术栈 —— 本仓库本身未声明任何技术栈。

## 如何编写技能

- 每个 `SKILL.md` 遵循 Claude Code 的技能约定:YAML 前置元数据块(`name` 与 `description`)+ Markdown 正文。
- `name` 字段是技能的标识(如 `code-version`);`description` 字段应明确触发条件。
- 技能正文应描述:目标、适用场景、输入、输出、工作流步骤、上下游衔接。
- 技能引用的资源位于同级目录:`templates/`(技能产出的文档模板)、`references/`(技能强制执行的参考流程)。
- 一个技能的下游产出,就是下一个技能的上游输入。当某个技能的输出模式变更时,产出方与消费方都需同步更新。

## 版本感知工作空间约定

主流程中的技能(`code-req` / `code-fix`)在版本层之下运作:

```
assistants/
├── rules/                  # 项目级规范,跨版本共享,由 code-rule 维护
├── .current-version        # 当前激活版本标记
└── <版本号>/               # 版本工作空间
    ├── RESULT.md           # 版本开发进度看板(简化版:需求清单+缺陷清单)
    ├── req/<REQ-NNNNN>/    # 需求路径(code-req 产出)
    │   ├── REQUIRE.md      # 需求分析
    │   ├── DESIGN.md       # 软件设计
    │   ├── PLAN.md         # 任务排期
    │   ├── TASK-N.md       # 任务完成报告
    │   ├── CHECK.md        # 代码审查
    │   ├── PROCESS.md      # 执行进程(断点续跑)
    │   └── LOG.md          # 过程记录(可选)
    └── fix/<BUG-NNNNN>/    # 缺陷路径(code-fix 产出)
        ├── BUG.md          # 缺陷分析
        ├── DESIGN.md       # 修复设计
        ├── PLAN.md         # 任务排期
        ├── TASK-N.md       # 任务完成报告
        ├── CHECK.md        # 代码审查
        ├── PROCESS.md      # 执行进程(断点续跑)
        └── LOG.md          # 过程记录(可选)
```

- `rules/` **跨版本共享**,主流程技能对其**只读**;`code-rule` 是唯一写入该目录的技能。
- 每个主流程技能的第一步是读取 `.current-version`;若文件不存在,技能立即中止并提示用户调 `code-ver`。
- `code-ver` 合并了初始化、版本切换、发布检查三种能力:新项目无 `assistants/` 时自动执行初始化(扫描代码、登记基线需求、创建基线版本);已初始化项目切换版本;当前版本未发布时询问是否先发布再切换。
- `code-rule` **不**做版本感知 —— 它直接操作 `rules/`,从不读取或写入 `.current-version` 与任何版本目录。
- `code-fix` 是**独立全流程技能**:缺陷登记 → 修复设计 → 任务排期 → 编码执行 → 代码审查,复用 `code-req` 的 references(DESIGN/PLAN/CODING/CHECK 阶段),支持 `--auto` 和 `PROCESS.md` 断点续跑。
- `code-req` 是**独立全流程技能**:需求分析 → 软件设计 → 任务排期 → 编码执行 → 代码审查,默认交互确认,`--auto` 静默,支持 `PROCESS.md` 断点续跑。
- 版本看板的写入责任划分:
  - `code-req` → 需求清单(首次创建需求时追加一行)
  - `code-fix` → 缺陷清单(首次创建缺陷时追加一行)
  - 各阶段的进度通过 `PROCESS.md` 追踪,不再频繁更新看板

## 双状态任务模型

每条任务有两个**正交**的状态字段:
- **开发状态**:`待开始` / `进行中` / `已完成` / `已取消` / `阻塞` / `待重新评估`
- **测试状态**:`未编写` / `已编写` / `已运行-通过` / `已运行-失败` / `不适用` / `阻塞`

任务**真正可发布**的判定条件:开发状态 = `已完成` **且** 测试状态 ∈ {`已运行-通过`, `不适用`}。

## 触发/来源(任务来源维度)

每条任务都带有一个 `触发/来源` 字段(13 个枚举值),用于决定 `code-it` 读取哪份上游输入:
- 大多数值 → `./assistants/<版本号>/plan/<需求编号>/RESULT.md`(详细设计)
- `审查改修` → `./assistants/<版本号>/review/<任务编码>/RESULT.md`(审查派生的改修)

完整技能清单、各自的输入/输出,以及端到端流程,请参见 `README.md`。

## AI 工作约定(由 code-rule 维护)

> 本小节由 `code-rule` 技能维护;手动修改可能被 `code-rule` 覆盖。
> 适用对象:Claude Code 在本仓库工作时

### 指引 1: (待添加)

### 指引 N: `code-dashboard` 行为约定
- 展示策略:ASCII 进度表 + 文本柱状图(固定 12 字符 + `█` / `░` / `▓`)
- 建议策略:5 类优先级(高/中/低/—)+ 最多 5 条;命令严格按既有 7 个 `code-*` SKILL.md 真实语法
- 解析锚点:看板 2 区段(需求清单 / 缺陷清单);按 `^## .*$` 定位 + 表格行 `^\| .* \|$` 匹配
- 进度追踪:通过 `PROCESS.md` 阶段追踪(INIT→REQUIRE→DESIGN→PLAN→CODING→CHECK→DONE)
- 双格式兼容:任务编号新格式 `^TASK-(REQ|BUG)-\d{5}-\d{5}$` 优先;旧格式 `^(REQ|BUG)-\d{5}-\d{5}$` 透传
- 状态字面:严格按字面匹配(不归一化)
- 工具集:仅 `Read` / `Glob` / `Grep`;禁用 `Write` / `Edit` / `Bash`
