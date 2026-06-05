# CLAUDE.md

本文件为 Claude Code(claude.ai/code)在本仓库工作时提供指引。

## 仓库用途

`code-skills` 是一套用于走完完整软件开发生命周期的 Claude Code 技能集合,内置**版本感知工作空间管理**:

```
code-version → code-require → code-design → code-plan → code-it → code-unit → code-review
   版本管理      需求分析        概要设计      详细计划     开发编码    单元测试      代码评审

   code-init  (项目级一次性引导)— 扫描现有代码,登记为基线
   code-rule  (横向,非主流程)  — 编码规范管理
   code-fix   (支线流程入口)   — 缺陷登记与跟踪(与 code-plan / code-it 接驳)
```

`code-version` 是**必备的前置门** —— 主流程中其他所有 `code-*` 技能在执行时,都会先读取 `./assistants/.current-version` 以确定工作目录。

`code-init` 是新项目的**一次性引导**:扫描现有源码,将每个已有功能登记为 `require/EXISTING-NNN/`,生成 `INIT-REPORT.md`,并创建基线版本。`code-init` 执行完成后,用户应调 `code-version` 切到新开发版本。

`code-rule` **不在主流程管道中** —— 它负责维护跨版本共享的 `./assistants/rules/` 目录,主流程中的所有技能都会以只读方式读取该目录作为约束。

`code-fix` 是**支线流程入口**:负责登记缺陷与跟踪其生命周期。它与 `code-plan` / `code-it`(两者均已扩展以接受 `BUG-NNN` 输入)协作,完整支线流程为:`code-fix`(登记)→ `code-plan <BUG-NNN>`(规划修复)→ `code-it <BUG-NNN>`(实施修复)→ `code-fix <BUG-NNN>`(推进状态/关闭)。

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
            ├── code-init/            # 工程初始化(项目级一次性引导)
            ├── code-version/         # 版本管理(版本感知入口)
            ├── code-rule/            # 编码规范管理(项目级共享)
            ├── code-require/         # 需求分析
            ├── code-design/          # 概要设计
            ├── code-plan/            # 详细设计 / 实施计划(REQ 路径)+ 缺陷修复方案(BUG 路径)
            ├── code-it/              # 开发编码(任务路径)+ 缺陷修复实施(缺陷路径)
            ├── code-unit/            # 单元测试
            ├── code-fix/             # 缺陷登记与跟踪
            └── code-review/          # 代码评审
```

## 需与用户确认的约定

本仓库**不包含任何源代码、构建系统、测试框架、Lint 工具或包管理配置**。不要假设存在任何工具链。

如果用户要求执行 `run` / `build` / `lint` / `test` 等操作,请先与用户确认其目标技术栈 —— 本仓库本身未声明任何技术栈。

## 如何编写技能

- 每个 `SKILL.md` 遵循 Claude Code 的技能约定:YAML 前置元数据块(`name` 与 `description`)+ Markdown 正文。
- `name` 字段是技能的标识(如 `code-version`);`description` 字段应明确触发条件。
- 技能正文应描述:目标、适用场景、输入、输出、工作流步骤、上下游衔接。
- 技能引用的资源位于同级目录:`templates/`(技能产出的文档)、`guidelines/`(技能强制执行的规则)、`checklists/`(校验清单)。
- 一个技能的下游产出,就是下一个技能的上游输入。当某个技能的输出模式变更时,产出方与消费方都需同步更新。

## 版本感知工作空间约定

主流程中的技能(`code-require` 到 `code-review`)在版本层之下运作:

```
assistants/
├── rules/                  # 项目级规范,跨版本共享,由 code-rule 维护
├── .current-version        # 当前激活版本标记
└── <版本号>/               # 版本工作空间
    ├── RESULT.md           # 版本开发进度看板
    ├── INIT-REPORT.md      # (仅基线版本)code-init 生成的功能分析报告
    ├── require/<需求编号>/
    │   └── EXISTING-NNN/   # (仅基线版本)现有功能需求,由 code-init 批量创建
    ├── design/<需求编号>/
    ├── plan/<需求编号>/    # 需求路径的详细设计与任务计划(code-plan REQ 分支)
    ├── code/<任务编码>/    # 任务路径的开发执行(code-it 任务分支)
    ├── test/<任务编码>/
    ├── review/
    └── fix/                # 缺陷路径(code-fix + code-plan/code-it BUG 分支)
        ├── RESULT.md       # 缺陷总览
        └── <BUG-NNN>/
            ├── RESULT.md   # 缺陷详情
            ├── fix-plan.md # 修复方案(code-plan BUG 分支)
            ├── fix-work-log.md / fix-compile-and-run.md / fix-test-results.md / deviations.md
            └── ...
```

- `rules/` **跨版本共享**,主流程技能对其**只读**;`code-rule` 是唯一写入该目录的技能。
- 每个主流程技能的第一步是读取 `.current-version`;若文件不存在,技能立即中止并提示用户调 `code-version`。
- `code-init` 是**唯一**会创建基线版本并填充 `EXISTING-NNN/` 的技能 —— 它不修改 `rules/`,且每个项目只应执行一次。执行完毕后,用户应调 `code-version` 开启新开发版本。
- `code-rule` **不**做版本感知 —— 它直接操作 `rules/`,从不读取或写入 `.current-version` 与任何版本目录。
- `code-fix` **不在主流程管道中**但**做版本感知**:在当前激活版本的 `fix/` 目录下工作。它登记缺陷、跟踪生命周期,并与 `code-plan` / `code-it`(两者均已扩展以接受 `BUG-NNN` 输入)协作。
- `code-plan` 与 `code-it` 是**双路径**设计:既接受需求编码(REQ-YYYY-NNNN),也接受缺陷编号(BUG-NNN),并分别路由到相应子目录。
- 每个主流程技能在执行结束时,会更新 `<版本号>/RESULT.md`(版本看板)中其负责的区段。
- 版本看板的写入责任划分:
  - `code-require` → 需求清单, 变更记录
  - `code-design` → 概要设计清单, 变更记录
  - `code-plan`(REQ 路径)→ 详细设计与任务计划汇总, 任务清单, 里程碑, 变更记录
  - `code-plan`(BUG 路径)→ 缺陷清单, 变更记录
  - `code-it`(任务路径)→ 任务清单(开发状态), 缺陷清单, 执行的开发命令记录, 变更记录
  - `code-it`(缺陷路径)→ 缺陷清单, 执行的开发命令记录, 变更记录
  - `code-unit` → 任务清单(测试状态), 缺陷清单, 执行的开发命令记录, 变更记录
  - `code-fix` → 缺陷清单, 变更记录
  - `code-review` → 评审发现汇总, 派生任务记录, 缺陷清单, 任务清单(派生任务), 变更记录

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
- 建议策略:5 类优先级(高/中/低/—)+ 最多 5 条;命令严格按既有 10 个 `code-*` SKILL.md 真实语法
- 解析锚点:看板 3 区段(需求清单 / 任务清单 / 缺陷清单);按 `^## .*$` 定位 + 表格行 `^\| .* \|$` 匹配
- 双格式兼容:任务编号新格式 `^TASK-(REQ|BUG)-\d{5}-\d{5}$` 优先;旧格式 `^(REQ|BUG)-\d{5}-\d{5}$` 透传
- 状态字面:严格按字面匹配(不归一化 `已完成(需求分析)` 到 `已完成`)
- 工具集:仅 `Read` / `Glob` / `Grep`;禁用 `Write` / `Edit` / `Bash`
