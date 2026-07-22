# `code-skills` 技能能力全景与优化建议报告

> **审计日期**：2026-07-22  
> **审计对象**：本仓库当前已存在的 Claude Code 技能工程  
> **审计方式**：只读阅读 `SKILL.md`、`references/`、`templates/`、插件清单、README 与 `CLAUDE.md`；未运行项目代码，未假设任何语言工具链存在。  
> **本次实际变更**：仅新增本报告 `./opt.md`；没有修改任何原始 `SKILL.md`、reference、template、README、插件清单或其他源文件。  
> **证据标记**：`[已确认]` 表示可由当前仓库静态内容直接确认；`[需验证]` 表示应在实际 Claude Code 安装/沙箱中做冒烟验证后再定案；`[建议]` 表示设计优化方向，不代表已经实施。

---

## 0. 执行摘要

`code-skills` 已经形成了一个相当完整的、以 `/code` 为入口的 AI 协作软件开发生命周期系统。它不是单个“写代码”技能，而是一套带有版本工作空间、结构化产物、阶段门控、断点续跑、规范约束、知识导出和 worktree 合并能力的流程编排器。

当前系统的核心价值可以概括为：

1. **把自然语言开发请求转化为可追踪的文档和代码变更**：需求、设计、排期、任务报告、审查和进程均有固定产物。
2. **把版本上下文前置**：`/code ver` 负责初始化、切换、发布检查和看板，`req/fix` 在激活版本下运行。
3. **用 `PROCESS.md` 提供可恢复状态机**：中断后按阶段恢复，而不是依赖上下文记忆。
4. **用硬门控保护源码修改窗口**：`req/fix` 只有在 `CODING` 阶段才能修改 CWD 源码。
5. **把需求开发、缺陷修复、知识查询、规范维护、worktree 合并分离**，形成明确的职责边界。

但当前系统还存在三类高影响问题：

- **事实契约不一致**：README、主入口、子技能、模板和解析算法之间有若干字段、路径、状态和阶段数不一致，部分问题会直接导致导出、发布检查或看板统计失真。
- **技能注册模型不够明确**：主 `SKILL.md` 把自己描述成“首 token 路由器”，插件清单又把各子目录列为独立技能；这套设计需要明确到底是“一个用户入口 + 内部 reference”，还是“多个独立可触发 skill”。
- **信息层级和完成语义仍有冗余**：全局纪律在多个文件重复，长流程入口缺少阶段摘要和可勾选完成标准，失败、回退、阻塞和终止的语义没有统一成机器可检查的契约。

### 推荐的改修顺序

| 优先级 | 先解决什么 | 主要收益 |
| --- | --- | --- |
| **P0** | 统一技能注册/路由模型；修正 FAQ 映射、产物路径、看板/发布状态契约 | 先恢复功能正确性和触发确定性 |
| **P1** | 建立共享状态契约；补齐完成条件、失败分类、阶段摘要；收敛重复内容 | 让流程可恢复、可审计、可维护 |
| **P2** | 优化描述字段、渐进披露、模板折叠、确认策略和 merge 边界 | 降低上下文负担和用户摩擦 |
| **P3** | 增加静态一致性检查、冒烟场景矩阵、文档自动同步 | 防止后续再次出现契约漂移 |

---

# 1. 现有技能的完整能力描述

## 1.1 产品定位与工程形态

仓库采用 Claude Code marketplace 插件布局：

```text
code-skills/
├── .claude-plugin/marketplace.json       # marketplace 清单
└── plugins/code-skills/
    ├── .claude-plugin/plugin.json        # 插件元数据与 skill 路径
    ├── README.md                         # 中文使用说明
    ├── README.en.md                      # 英文使用说明
    ├── CLAUDE.md                         # 插件/仓库协作约定
    └── skills/code/
        ├── SKILL.md                     # /code 入口与路由
        ├── references/                   # 子命令流程与按需参考
        └── templates/                    # 结构化产物模板
```

主入口的定位是：

- 识别 `/code <首 token>`；
- 将 `ver`、`req`、`fix`、`faq`、`rule`、`merge` 路由到对应 reference；
- 对未知或缺失参数路由到 `help`；
- 在需求/缺陷流程中提供全局执行纪律和源码修改门控。

### 子命令数量的准确表述

当前存在三个不同的计数口径，后续文档应统一：

- **业务子命令**：6 个——`ver`、`req`、`fix`、`faq`、`rule`、`merge`。
- **路由分支**：7 个——上述 6 个再加 `help`。
- **插件清单中的 skill 路径**：当前是 8 个——主入口 `code` 加 7 个子目录入口。

`README.md` 与 `README.en.md` 目前写“含 6 个子命令”（例如 `plugins/code-skills/README.md:25-41`），而主入口 frontmatter 和路由表把 `help` 也算作分支（`plugins/code-skills/skills/code/SKILL.md:1-3,79-99`）。建议今后明确使用“6 个业务命令 + 1 个帮助分支”的表述，避免“6/7/8”在不同层次混用。

---

## 1.2 版本工作空间模型

所有主流程围绕以下运行时目录工作：

```text
assistants/
├── rules/                       # 跨版本共享的项目规范
├── .current-version             # 当前激活版本，纯文本
└── <版本号>/
    ├── RESULT.md                # 版本看板
    ├── req/<REQ-NNNNN>/         # 需求产物
    │   ├── REQUIRE.md
    │   ├── DESIGN.md
    │   ├── PLAN.md
    │   ├── TASK-*.md
    │   ├── CHECK.md
    │   ├── PROCESS.md
    │   └── LOG.md（可选）
    ├── fix/<BUG-NNNNN>/         # 缺陷产物
    │   ├── BUG.md
    │   ├── DESIGN.md
    │   ├── PLAN.md
    │   ├── TASK-*.md
    │   ├── CHECK.md
    │   ├── PROCESS.md
    │   └── LOG.md（可选）
    └── publish/                 # 发布手册
```

核心约定：

- `.current-version` 是主流程的前置上下文；`req/fix` 找不到它时停止并引导 `/code ver`。
- `rules/` 跨版本共享，主流程只读，`/code rule` 负责增量维护。
- `RESULT.md` 由 `/code ver` 创建，`req/fix` 在首次创建条目时同步需求/缺陷清单。
- 各阶段的详细进度不再频繁改写看板，而是追加到 `PROCESS.md`。
- `/code faq` 主要只读 `assistants/`；导出时才写入用户指定的输出路径。

仓库说明文件也明确了双状态任务模型：

- 开发状态：`待开始`、`进行中`、`已完成`、`已取消`、`阻塞`、`待重新评估`。
- 测试状态：`未编写`、`已编写`、`已运行-通过`、`已运行-失败`、`不适用`、`阻塞`。
- 真正可发布：开发状态为 `已完成`，且测试状态为 `已运行-通过` 或 `不适用`。

依据：仓库根 `CLAUDE.md:65-110`、`plugins/code-skills/skills/code/references/req/common.md:172-223`。

---

## 1.3 `/code ver`：版本管理、开发看板、发布检查

入口：`plugins/code-skills/skills/code/references/ver/SKILL.md`；详细算法在同目录 `common.md`。

### 触发形式

| 输入 | 场景 |
| --- | --- |
| `/code ver`，未初始化 | 新项目初始化 |
| `/code ver`，已初始化 | 只读开发进度看板 |
| `/code ver <版本号>` | 创建或切换版本 |
| `/code ver --publish` | 发布前置检查和手册生成 |

场景检测算法在 `references/ver/common.md:4-49`。

### 初始化能力

初始化流程包含：

1. 收集初始版本号，默认 `V0.0.0`；
2. 创建 `assistants/`、`rules/`、版本目录、`req/`、`fix/`、`publish/`；
3. 写入 `.current-version`；
4. 创建 `RESULT.md`；
5. 只读扫描现有工程：项目类型、目录结构、入口、模块、数据模型、依赖、构建和测试约定；
6. 生成 `INIT-REPORT.md`；
7. 将现有功能拆成 `EXISTING-NNN` 基线条目；
8. 如果规则目录为空，提示用户调用 `/code rule`。

详细位置：`references/ver/common.md:51-473`。

### 开发看板能力

看板模式只读，预期输出四段：

1. 总开发进度：固定 12 字符 ASCII 进度条；
2. 状态分布：待需求分析、待设计、待排期、待编码、待审查；
3. P0/P1 未修复缺陷计数；
4. 最多 5 条后续操作建议。

数据来源包括：

- 当前版本的 `RESULT.md`；
- `req/REQ-*` 和 `fix/BUG-*` 目录；
- 每个条目的 `PROCESS.md`；
- 看板需求/缺陷区段的表格字段。

看板解析、降级和 ASCII 算法见 `references/ver/SKILL.md:101-281` 与 `references/ver/common.md:965-1298`。

### 版本切换能力

版本切换会区分：

- 目标不存在、当前无版本：首次创建；
- 目标不存在、当前有版本：确认后创建新版本；
- 目标存在且不同：确认后切换；
- 目标等于当前：再次确认或取消。

当前版本存在活动内容时，可先执行发布检查再切换。切换后还会尝试同步 CWD 工程描述文件中的版本号，具体规则在 `references/ver/common.md:477-601,861-920`。

### 发布检查能力

发布模式预期执行：

1. 解析需求、任务、缺陷并判断是否全部完成；
2. 判断当前版本是否为基线版本；
3. 生成 `publish/DEPLOY.md`；
4. 非基线版本生成 `publish/UPDATE.md`；
5. 聚合 `assistants/faq/` 生成 `publish/FAQ.md`；
6. 输出通过或未完成项报告。

详细位置：`references/ver/common.md:606-857`。

---

## 1.4 `/code req`：需求开发全生命周期

入口：`plugins/code-skills/skills/code/references/req/SKILL.md`。

### 输入

- 自然语言需求描述；或已有 `REQ-NNNNN` 编号用于续跑；
- 可选 `--confirm`；
- 可选 `--auto`；
- `--confirm` 与 `--auto` 互斥。

### 七阶段状态机

```text
INIT → REQUIRE → DESIGN → PLAN → CODING → CHECK → DONE
```

这里的“7 阶段”包括流程初始化和收尾；面向用户的主要工作阶段是 REQUIRE、DESIGN、PLAN、CODING、CHECK 五段。

### 阶段能力与产物

| 阶段 | 核心动作 | 必要产物/状态 |
| --- | --- | --- |
| INIT | 分配编号、创建目录、初始化 `PROCESS.md` | `req/REQ-NNNNN/PROCESS.md` |
| REQUIRE | 保留原始输入，提炼 FR/NFR/AC，关联需求，澄清边界，延迟技术选型 | `REQUIRE.md`，必要时 `clarifications.md`；同步 `RESULT.md` |
| DESIGN | 探索项目现状，设计模块、接口、数据、流程和方案选型 | `DESIGN.md` |
| PLAN | 将设计拆成独立任务，分析依赖，划分里程碑，绘制 Mermaid 图 | `PLAN.md` |
| CODING | 按依赖逐任务编码，按需写单测，编译/运行/测试，记录验证与偏差 | `TASK-*.md`、CWD 代码变更、必要的过程文档 |
| CHECK | 按正确性、需求一致性、设计一致性、规范、安全、性能、可维护性、测试覆盖、代码行数等维度审查 | `CHECK.md`；必要时向 `PLAN.md` 追加审查改修任务 |
| DONE | 写入完成记录，输出汇总，按条件执行兜底 git commit | `PROCESS.md` 最终为 `DONE` |

参考：`references/req/SKILL.md:163-254`、`references/req/common.md:10-170`。

### 需求分析的边界

`REQUIRE` 阶段只确定“系统要做什么”，不做框架、数据库、库、架构风格等技术选型。技术选型被延迟到 `DESIGN`。模糊问题按每轮 1-3 个最阻塞问题进行澄清，问答追加到 `clarifications.md`。

参考：`references/req/require.md:60-161,163-216`。

### 设计确认

`DESIGN` 阶段根据需求规模自适应确认：

- 是否需要扩展点；
- 多方案技术决策；
- 模块/接口/数据变更方案；
- 涉及移除现有行为、修改默认行为、标记过时或影响其他 `/code` 子命令时的危险操作确认。

危险操作不应由 `--auto` 静默放行，当前文档已明确这一点（`design.md:222-255`）。

### 编码安全门

源码修改的唯一合法窗口是 `PROCESS.md` 最后一条记录显示当前阶段为 `CODING`。在 INIT、REQUIRE、DESIGN、PLAN、CHECK、DONE 阶段，允许读写工作产物，但不得修改 CWD 源码。

参考：`references/req/SKILL.md:106-161`、`references/req/coding.md:30-62`。

### 运行环境和测试能力

CODING 阶段会：

- 根据 `go.mod`、`Cargo.toml`、`pom.xml`、`build.gradle`、`pyproject.toml`、`package.json` 检测项目类型；
- 按需加载 Go、Python、Node.js、Rust、Java Maven、Java Gradle 语言参考；
- 先实际执行编译/运行/测试，再区分运行时缺失、依赖包缺失、代码 bug、设计缺陷；
- 运行时缺失在非 `--auto` 模式下询问路径、授权安装、跳过验证或回滚；
- 缺失依赖包直接使用相应包管理器处理；
- 不把本机运行时绝对路径或 PATH 写入产物或 MEMORY；
- 按任务类型决定是否写单测；
- 记录逻辑行数，供 CHECK 阶段审查。

参考：`references/req/coding.md:142-331`、`references/runtime-environment.md:8-135`、`references/req/languages/*.md`。

### CHECK 修复闭环

如果存在未处理的“必须改”，系统会：

1. 生成审查改修任务；
2. 追加到 `PLAN.md`；
3. 返回 CODING；
4. 修复后重新执行 CHECK；
5. 最多循环 5 轮。

参考：`references/req/check.md:102-163`。

---

## 1.5 `/code fix`：缺陷修复全生命周期

入口：`plugins/code-skills/skills/code/references/fix/SKILL.md`。

### 输入与流程

- 自然语言缺陷描述；或已有 `BUG-NNNNN` 编号续跑；
- `--confirm` 或 `--auto`；
- 流程为：

```text
INIT → DESIGN → PLAN → CODING → CHECK → DONE
```

### 与 `/code req` 的差异

| 方面 | `/code req` | `/code fix` |
| --- | --- | --- |
| 首个业务产物 | `REQUIRE.md` | `BUG.md` |
| 关注内容 | FR/NFR/AC、用户目标 | 原始报告、复现、成因假设、影响范围、严重度 |
| 路径 | `req/REQ-NNNNN/` | `fix/BUG-NNNNN/` |
| 后续阶段 | 独立定义 | 复用 req 的 design/plan/coding/check/runtime references |
| 看板责任 | 需求清单 | 缺陷清单 |

缺陷登记会按 P0-P3 判定严重程度，默认 P2；修复设计和后续执行复用需求流程的通用阶段。

参考：`references/fix/SKILL.md:16-78`、`references/fix/fix-register.md:0-179`。

---

## 1.6 `/code faq`：跨版本查询和文档导出

入口：`plugins/code-skills/skills/code/references/faq/SKILL.md`。

### 查询模式

- 有当前版本时优先搜索当前版本，无结果再跨版本；
- 无当前版本时可以全局搜索；
- 通过 `Glob` 列出需求/缺陷文档，`Grep` 匹配关键词；
- 对相关性最高的结果进行深度读取；
- 回答中标注版本、编号和来源路径；
- 最多展示前若干结果，并在结果过多时提示缩小范围。

### 导出模式

| 参数 | 能力 |
| --- | --- |
| `--require <REQ> <out>` | 导出需求文档 |
| `--design <REQ> <out>` | 导出完整设计文档 |
| `--design <REQ> <out> --summary` | 导出设计概要 |
| `--template <tpl>` | 将源文档字段填充到用户模板 |

查询模式和导出模式均不修改 `assistants/` 内部产物；导出只写用户指定路径，并带有模板不存在、未识别占位符、路径越界等降级策略。

参考：`references/faq/SKILL.md:79-221`、`references/faq/common.md:4-250`。

---

## 1.7 `/code rule`：跨版本编码规范基础设施

入口：`plugins/code-skills/skills/code/references/rule/SKILL.md`。

该命令不读取 `.current-version`，直接维护 `./assistants/rules/`：

1. 探查规则目录；
2. 收集自然语言规范；
3. 逐条识别类型和分类；
4. 追问强制级别、适用范围、示例、例外和关联规范；
5. 检测重复与冲突；
6. 新分类使用 `Write` 创建；已有分类只能在末尾追加；
7. 向用户汇报分类、级别、文件位置和下游影响。

当前还定义了三种对象：

- Type A：一般编码规范条款；
- Type B：仓库 `CLAUDE.md` 中的 AI 工作约定；
- Type C：`templates/` 中的提示内容。

参考：`references/rule/SKILL.md:9-149`。

---

## 1.8 `/code merge`：worktree 合回主干

入口：`plugins/code-skills/skills/code/references/merge/SKILL.md`。

### 前置条件

- 必须在 git linked worktree 中运行；主工作区立即报错 E-M1；
- 需要 `.current-version`；
- 默认目标为 `origin/main`，可传一个分支名；
- 不自动 push，不自动删除 worktree，不写过程文档。

### 主流程

1. 识别 worktree 并检查状态；
2. 提交 worktree 中的未提交文件；
3. fetch 并将主干合入当前 worktree 分支；
4. 对看板、代码、文档、配置和二进制冲突进行分类处理；
5. 检查是否仍有未合并文件；
6. 检查看板需求/缺陷区段的一致性；
7. 用 `git merge --no-ff` 将 worktree 分支合回目标分支；
8. 输出完成报告和退出码。

退出码包含正常完成、致命错误和 Ctrl+C 的 130；E-M1 至 E-M12 覆盖 worktree、分支、冲突、参数、git 和中止场景。

参考：`references/merge/SKILL.md:7-20,57-110,113-320`。

---

## 1.9 `/code help`：入口帮助和参数异常引导

入口：`plugins/code-skills/skills/code/references/help/SKILL.md`。

触发条件：

- `/code` 无参数；
- 首 token 未知；
- `/code help`、`--help`、`-h`；
- 已识别子命令但参数不完整时，由对应子命令处理。

能力：

- 展示完整命令表、示例、flag 和约束；
- 对未知首 token 展示错误对照；
- 用 `AskUserQuestion` 提供 7 个选择：ver、req、fix、faq、rule、merge、help；
- 只读输出，不落盘。

参考：`references/help/SKILL.md:11-146`。

---

# 2. 现有设计的主要优点

## 2.1 生命周期覆盖完整

从版本初始化、需求/缺陷登记，到设计、排期、编码、测试、审查、发布和合并，系统已经覆盖了大多数常见 AI 协作开发场景。每段都有明确的文档产物，能够让后续会话重新建立上下文。

## 2.2 `PROCESS.md` 是很好的可恢复机制

追加式进程记录比依赖模型上下文更可靠。当前的阶段顺序、完成/失败记录、恢复入口和前置产物校验已经具备状态机雏形。

## 2.3 源码修改门控清晰且有防误触意识

“先建立工作产物，再进入 CODING 修改源码”是整个系统最有价值的安全设计之一。它尤其适合修改技能自身这类元任务，能避免模型直接跳过需求和设计阶段。

## 2.4 需求与缺陷共享阶段能力，避免两套流程漂移

`fix` 复用 `req` 的设计、排期、编码、审查和运行环境参考，减少了维护两套完全相同流程的成本。后续只需要把共享契约进一步抽取出来即可。

## 2.5 对运行时与隐私边界考虑较周全

“先尝试命令，再区分运行时和依赖包”“非自动模式下系统级安装须确认”“不记录本机路径”这些规则能降低不可预期副作用，也避免把机器特有环境污染到长期记忆。

## 2.6 看板有明确的退化策略

区段缺失、表格列错位、字段为空、PROCESS 缺失和解析失败都有降级行为，不会因一个坏表格直接失去全部进度信息。这种 L1/L2/L3 分层思路值得保留。

## 2.7 语言适配是可扩展的

语言参考文件将目录识别、构建、测试、运行、命名和工具链约定分开，未来可以按同样结构增加其他生态，而不必把所有命令硬编码进主流程。

---

# 3. 已确认的问题与影响

下面只列静态阅读可以直接确认，或者由两个文件的明确契约冲突可以确认的问题。没有把纯粹的风格偏好当作功能缺陷。

## 3.1 P0：看板字段与发布/看板解析算法不是同一份数据契约

### 证据

- 初始化 `RESULT.md` 的表格只有“编码、标题、进度文档”三列：`references/ver/common.md:103-148`。
- `/code req` 和 `/code fix` 追加的看板行也只有三列：`references/req/require.md:189-195`、`references/fix/fix-register.md:136-142`。
- 发布检查却按 `状态` 字段判断需求和缺陷是否完成：`references/ver/common.md:606-638`。
- 看板高优先级缺陷统计也读取 `优先级`、`状态` 或同义列：`references/ver/common.md:1144-1161`。
- 根 `CLAUDE.md:99-102` 明确说阶段进度通过 `PROCESS.md` 追踪，不再频繁更新看板。

### 影响

`/code ver --publish`、P0/P1 缺陷统计和建议生成可能读不到状态/优先级；在不同版本的 RESULT 格式下，可能把未完成内容当成未知，或者长期显示 0/`?`。这不是单纯文案问题，而是生产者和消费者使用了不同 schema。

### 建议

选择并固化一种单一事实来源：

- 推荐：`RESULT.md` 只作为索引，不存动态状态；发布检查、看板和建议全部从 `PROCESS.md`、`PLAN.md`、`BUG.md` 及任务状态派生。
- 备选：给 `RESULT.md` 明确增加状态、优先级、测试状态等列，并规定每个阶段谁负责更新；这会增加写入竞争和合并冲突。

推荐方案下，应删除所有“从 RESULT 状态列判断发布”的伪代码，改为调用统一的 `deriveItemStatus()` 契约，并定义缺失数据的保守行为。

---

## 3.2 P0：FAQ 占位符章节映射错误

### 证据

`references/faq/common.md:204-243` 的需求导出映射写成：

- FR → REQUIRE.md §4；
- NFR → §5；
- AC → §10；
- 关联需求 → §11；
- 待澄清 → §12。

而实际模板 `templates/req/REQUIRE.md` 的章节是：

- FR → §3；
- NFR → §4；
- AC → §5；
- 关联需求 → §6；
- 变更记录 → §7；
- 模板中没有 §10、§11、§12，也没有稳定的“待澄清”一级章节。

### 影响

`/code faq --template` 可能把 FR/NFR/AC 读取错位，或者留下未替换占位符。查询深读逻辑在 `references/faq/common.md:91-99` 也使用了错误的 §4/§5/§10 说明。

### 建议

以模板真实标题而不是手工章节号作为唯一映射键，至少修正为：

```text
FR_LIST   → ## 3. 功能需求(FR)
NFR_LIST  → ## 4. 非功能需求(NFR)
AC_LIST   → ## 5. 验收标准(AC)
关联需求  → ## 6. 关联需求
待澄清    → clarifications.md 或 REQUIRE.md 中显式定义的章节
```

更稳妥的方案是为每个可导出字段定义稳定锚点，例如 `<!-- code-skills:field=FR_LIST -->`，避免以后章节编号变化再次破坏导出。

---

## 3.3 P0：多个 reference 指向仓库中不存在的模板路径

已确认的文字引用包括：

| 引用位置 | 当前写法 | 实际模板 |
| --- | --- | --- |
| `references/req/require.md:166` | `templates/REQUIRE.md` | `templates/req/REQUIRE.md` |
| `references/req/design.md:266` | `templates/DESIGN.md` | `templates/req/DESIGN.md` |
| `references/req/plan.md:193` | `templates/PLAN.md` | `templates/req/PLAN.md` |
| `references/req/coding.md:336` | `templates/TASK.md` | `templates/req/TASK.md` |
| `references/req/check.md:180` | `templates/CHECK.md` | `templates/req/CHECK.md` |
| `references/fix/fix-register.md:110` | `templates/BUG.md` | `templates/fix/BUG.md` |

### 影响

模型按指针读取时可能得到“文件不存在”，或者在错误位置寻找模板，导致同一阶段出现不同格式的产物。

### 建议

建立统一路径规则：所有 reference 内的模板链接均从技能根目录明确写成 `../../templates/...` 或使用仓库内可解析的 Markdown 相对链接；不要混用“相对于当前文件”和“相对于技能根目录”的写法。随后做一次链接存在性扫描。

---

## 3.4 P0：初始化基线路径与主流程路径不一致

- 工作空间总览和主流程使用 `req/<REQ-NNNNN>/`：根 `CLAUDE.md:75-82`、`references/req/SKILL.md:51-67`。
- 初始化基线算法却写入 `assistants/<version>/require/EXISTING-NNN/RESULT.md`：`references/ver/common.md:358-433`，以及 `references/ver/SKILL.md:61-67` 的输出说明。

### 影响

基线功能可能落到 `require/`，而后续 `/code faq`、看板、需求续跑只扫描 `req/`，造成基线不可见或无法续跑。

### 建议

统一选择 `req/`（因为当前主流程、模板和 README 均使用它），把 `EXISTING-NNN` 也纳入 `req/EXISTING-NNN/`，并在迁移期间提供旧 `require/` 兼容读取。不要在没有兼容策略时直接重命名已有用户工作空间。

---

## 3.5 P1：默认确认行为在文档之间相互矛盾

- 根 `CLAUDE.md:19-21` 和 `README.md:95-97` 描述默认模式会在每阶段询问是否继续。
- `references/req/SKILL.md:178-187`、`references/fix/SKILL.md:144-153` 和 `references/req/common.md:157-170` 描述默认模式阶段边界自动继续，只有阶段内内容确认正常触发。

### 影响

用户无法从文档预知 `/code req` 是否会停在阶段边界；模型也可能按不同文档选择不同交互策略。

### 建议

明确三态模型并让所有入口使用同一表述。推荐：

| 模式 | 阶段边界 | 阶段内高影响决策 |
| --- | --- | --- |
| 默认 | 自动继续 | 只询问阻塞/危险决策 |
| `--confirm` | 每阶段确认并重读产物 | 正常询问 |
| `--auto` | 自动继续 | 普通问题用默认值，危险操作仍停下 |

如果产品更重视人工审阅，则将默认改为阶段确认也可以，但必须同步全部 README、CLAUDE、req/fix/common 和 help 文档。

---

## 3.6 P1：帮助选项数量和路由说明不一致

- 主入口 `SKILL.md:96-98` 写“AskUserQuestion 6 选项引导”。
- `references/help/SKILL.md:15-17,83-97,120` 实际列出 A-G 共 7 项，并包含 `help`。

### 建议

统一为“7 个路由选项（6 个业务命令 + help）”，并把同一命令矩阵作为 README、help 和主入口的唯一来源。

---

## 3.7 P1：PLAN 模板包含测试状态，PLAN 流程未定义其初始化和流转

- 模板 `templates/req/PLAN.md:6-10` 有“开发状态”和“测试状态”两列。
- `references/req/plan.md:190-214` 的计划表只描述开发状态、前置任务，没有定义测试状态。
- 根 `CLAUDE.md:104-110` 又把测试状态列为发布判定的一部分。

### 影响

同一份 PLAN 可能有测试状态列但没有初值规则；CODING 阶段更新开发状态后，测试状态可能仍停留在模板默认值。

### 建议

在 PLAN 阶段正式定义：

- 每种任务类型的初始测试状态；
- “不适用”的判定条件；
- CODING 编译/运行/测试后的状态转移；
- 运行环境缺失时是否为 `阻塞`、`未编写` 或 `用户跳过`；
- CHECK 和 publish 如何消费该字段。

同时让 `plan.md` 的任务表与模板完全同列。

---

## 3.8 P1：CHECK 模板承载不了正文定义的审查维度

`references/req/check.md:40-68` 定义了 9 个维度，包括测试覆盖和代码行数超标；`templates/req/CHECK.md:5-22` 只有正确性、规范、设计、安全、性能、可维护性等 6 个维度。

### 影响

CODING 记录了逻辑行统计，CHECK 也执行了代码行数检查，但最终 `CHECK.md` 没有稳定位置保存这些结果。

### 建议

将审查维度、权重、判定阈值和模板列放入共享契约，至少补齐：

- 需求一致性；
- 测试覆盖；
- 代码行数超标；
- 每个维度的结果、证据、发现数。

结论应由可检查条件生成：未处理“必须改”数量为 0，或明确记录为阻塞/达到轮次上限。

---

## 3.9 P1：`/code ver` 声明只读，但版本切换流程会写 CWD 描述文件

`references/ver/SKILL.md:48-53,437-449` 声明版本管理不修改 `assistants/` 以外的仓库代码；`references/ver/common.md:861-900` 却定义了写入 `package.json`、`pom.xml`、`Cargo.toml`、`pyproject.toml`、`manifest.json` 等 CWD 文件的版本号同步逻辑。

### 影响

用户调用版本切换时可能发生未被预期的源码/工程描述文件变更，且这部分修改不经过 req/fix 的 CODING 门控。

### 建议

二选一：

1. 推荐：版本同步改成显式 `--sync-project-version`，默认只更新 `assistants/.current-version`；
2. 保留自动同步，但把它声明为版本管理的合法写入范围，增加差异预览、用户确认、失败回滚和提交记录。

不能同时保留“绝不修改 CWD”和“自动 Write CWD 描述文件”两套语义。

---

## 3.10 P1：运行时状态枚举在模板与参考规则中不一致

- `templates/req/TASK.md:28-35` 使用：`已配置`、`用户提供路径`、`自动安装`、`用户跳过`、`未配置`。
- `references/runtime-environment.md:117-135` 允许记录的枚举是：`已配置`、`由用户跳过`、`由用户授权自动安装`、`由用户提供路径`，并强调只能记录枚举，不记录路径。

### 建议

定义一份唯一枚举并在所有地方原样复制。推荐机器值与展示值分离：

```text
runtimeStatus:
  configured
  user-provided
  auto-installed
  skipped
  unavailable
```

文档展示再映射为中文；不要让模板直接创造参考文件没有定义的状态。

---

## 3.11 P1：需求分析技术选型过滤存在两套词表

`references/req/require.md:102-117` 声称有 20 个关键词，但实际列出了更多项目；`require.md:197-200` 又给出另一套较短的关键词集合。

### 影响

同一问题可能在一轮被过滤、另一轮被询问；技术选型过滤的边界不可预测。

### 建议

把词表和动作定义成一个共享 reference：

- `decisionKeywords`：只用于延迟到 DESIGN；
- `conflictKeywords`：即使属于技术词也必须在 REQUIRE 确认；
- 每项记录命中的词、原问题、延迟原因；
- 删除“20 个”这类容易失真的人工计数，或由校验工具生成。

---

## 3.12 P1：`/code merge` 的目标分支操作存在高概率 worktree 冲突

静态流程在当前 worktree 中先执行 `git merge origin/main`，随后 `FR-7` 又直接执行 `git checkout <target>` 并将 worktree 分支合回目标分支（`references/merge/SKILL.md:176-190,266-283`）。在常规使用中，`main` 往往已经被主工作区占用；linked worktree 不能同时 checkout 同一分支。

### 需验证

这是高概率运行时问题，需在实际 git worktree 场景冒烟验证，但从流程设计看没有解析“主工作区路径”的步骤。

### 建议

- 用 `git worktree list --porcelain` 找到目标分支对应的主工作区；
- 在目标工作区使用 `git -C <main-worktree> merge <feature-branch> --no-ff`；
- 在开始前分别检查 feature worktree 和 target worktree 是否 dirty；
- 未解决冲突时返回非 0，不要把“仍有 unmerged 文件”定义为成功警告；
- 把 `CODE_MERGE_TARGET` 的分支名、远端 ref 和本地 checkout 目标分开建模。

---

## 3.13 P1：`/code merge` 看板自检与 RESULT 契约需要统一

`references/merge/SKILL.md:239-264` 用每个区段的“表格行数”和“统计行”比较；而 `references/ver/common.md:924-938` 又把看板描述为只含需求/缺陷清单、进度通过 PROCESS 读取。初始化模板当前确实写了 `统计` 行（`common.md:124-138`），但追加行、旧格式和降级格式没有统一要求。

### 建议

明确 `RESULT.md` 的 schema 版本：

- `schema: dashboard-v2`；
- 固定区段名称、表头和统计行格式；
- merge 自检只验证该 schema；旧 schema 使用兼容解析并明确标记“兼容模式”；
- 如果采用“状态从 PROCESS 派生”，则 merge 只检查索引链接和条目唯一性，不检查不存在的状态列。

---

## 3.14 P2：主入口的 §0 自检会在每次调用时打断用户

`plugins/code-skills/skills/code/SKILL.md:44-60` 要求每次进入 `/code` 都用 `AskUserQuestion` 询问用户是否读懂 5 条不变式。

### 影响

- 用户每次调用都遭遇元层确认；
- 与默认自动推进、帮助快速响应的体验不一致；
- 规则本身已经在入口和子命令启动检查中重复出现。

### 建议

删除“用户确认是否读懂规则”这一问询，保留模型内部的启动门控。只有在检测到即将违反门控、危险操作或用户明确要求跳过阶段时，才给出针对性说明。若确实需要可见确认，改为首次安装/首次运行一次，而不是每次调用。

---

## 3.15 P2：`/code rule` 的 Type B/Type C 子流程不足以保证确定性

`references/rule/SKILL.md:121-130` 只用几句话描述：

- Type B 写入哪个 `CLAUDE.md`、如何编号、如何避免覆盖；
- Type C 写入哪个 template、采用末尾提示还是内联提示；
- 分类确认和普通规则文件的追加权限如何区分。

### 建议

为 Type A/B/C 各定义独立的目标、schema、写入权限和完成条件。例如：

| 类型 | 目标文件 | 允许动作 | 完成条件 |
| --- | --- | --- | --- |
| A | `assistants/rules/<category>.md` | 新建或末尾追加 | 分类、级别、范围、例外已记录 |
| B | 明确指定的 `CLAUDE.md` | 仅追加 AI 工作约定区段 | 指引编号唯一，未改仓库说明区 |
| C | 明确指定的 template | 末尾/字段内二选一并记录 | 提示位置和触发字段可定位 |

如果 Type B/C 不是稳定产品能力，建议先从公开命令中移除，避免“规则命令可能修改技能源码”的权限含糊。

---

## 3.16 P2：`fix-registry.md` 与当前 RESULT/PROCESS 双模型关系不清

`templates/fix/fix-registry.md` 定义了独立的缺陷注册表、状态统计、严重度统计和变更记录；而主流程文档把当前版本 `RESULT.md` 作为缺陷清单，阶段进度由 `PROCESS.md` 追踪（`references/fix/SKILL.md:39-78`、根 `CLAUDE.md:75-102`）。

### 建议

明确它的命运：

- 如果是旧格式：标记为 legacy，并定义迁移/只读兼容；
- 如果仍要使用：将其纳入 producer-consumer 矩阵，规定 `/code fix` 何时、如何维护统计；
- 不要同时让模型维护两个缺陷注册事实源。

---

# 4. 按 writing-great-skills 原则的整体优化方案

## 4.1 先做架构决策：一个路由 skill，还是多个独立 skill

当前主入口的文本语义是“一个 `/code` skill 内部首 token 路由”，但插件清单同时暴露主入口和 7 个子目录入口。这里不应继续靠文案猜测，必须先确定注册模型。

### 推荐方案：一个用户入口 + 内部 reference

适合当前产品的理由：

- 用户明确使用 `/code <subcommand>`；
- 子命令之间由首 token 互斥；
- `help` 是路由失败分支，不是独立业务动作；
- 需求和缺陷流程共享大量 reference；
- 一个入口可以避免 7 个长 description 同时参与模型触发判断。

建议结构：

```text
skills/code/
├── SKILL.md                    # 唯一注册入口，负责路由
├── references/
│   ├── ver/FLOW.md
│   ├── req/FLOW.md
│   ├── fix/FLOW.md
│   ├── faq/FLOW.md
│   ├── rule/FLOW.md
│   ├── merge/FLOW.md
│   ├── help/FLOW.md
│   └── _shared/
└── templates/
```

如果当前 Claude Code 版本会自动发现嵌套 `SKILL.md`，则应通过实际安装验证；必要时将 reference 文件改名为 `FLOW.md`/`REFERENCE.md`，避免意外注册。

### 备选方案：7 个独立 skill

只有在以下需求成立时采用：

- 希望模型在用户没有输入 `/code` 时也能自主调用某个子命令；
- 子命令要从其他技能被直接调用；
- 可以接受每个 skill 的 description 带来的上下文负担。

若选此方案，必须删除“首 token 路由”的假设，让每个 skill 拥有真正互斥的触发描述，并同步插件清单、README、命名和下游引用。

### 需要做的验证

在决定前做一个最小安装冒烟测试，记录：

1. marketplace/plugin 实际注册了多少 skill；
2. `/code req` 是否会被父入口正确路由；
3. 直接输入需求自然语言时是否会误触发 `code-req`；
4. 子目录 `SKILL.md` 是否会被自动加载；
5. `help` 是否会抢占正常子命令。

---

## 4.2 重写 description：描述触发分支，不写执行手册

当前 description 过长，混入示例、硬禁止、阶段门和内部恢复规则。按“触发信号优先”的原则，description 应只回答：

- 这个技能处理哪类用户意图；
- 哪些明确动作/词会触发；
- 不属于它的相邻意图应去哪里。

### 推荐的正面触发词

统一使用一组短而稳定的 leading words：

```text
路由 / 版本 / 需求 / 缺陷 / 查询 / 规范 / 合并 / 帮助
```

正文再用“门控、记录、续跑、校验、发布、合并”形成分布式定义。不要在 description 中重复几十条“严禁”。

### 若采用独立 skill，description 可压缩为

```yaml
# code-ver
description: 用于项目初始化、切换开发版本、查看版本进度看板或执行发布前检查。用户明确要求初始化项目、切换版本、查看进度或发布检查时使用；不要用它开发需求或修复缺陷。

# code-req
description: 用于新建或续跑一条需求开发流程，覆盖需求分析、设计、排期、编码和审查。用户明确要求开发新功能或继续 REQ-NNNNN 时使用；缺陷请用 code-fix。

# code-fix
description: 用于登记并修复一个缺陷，覆盖缺陷分析、修复设计、排期、编码和审查。用户明确报告 bug 或继续 BUG-NNNNN 时使用；新功能请用 code-req。

# code-faq
description: 用于查询已有需求/缺陷文档，或将需求、设计导出为文件。用户询问某功能定义、历史版本或要求导出文档时使用；不要用它创建或修改需求。

# code-rule
description: 用于向跨版本共享的项目规范追加一条结构化规则。用户要求新增命名、错误处理、安全、性能或 AI 协作约定时使用。

# code-merge
description: 用于把 git worktree 中的开发分支合回指定主干。用户明确要求合并 worktree、解决合并冲突或执行 no-ff 合并时使用。

# code-help
description: 用于 `/code` 缺少子命令、首 token 无法识别或用户明确询问 /code 用法时显示帮助和命令选择。
```

这些文案只是建议，不应在本次任务中直接写入原文件。

---

## 4.3 让主 SKILL.md 只负责路由和最小硬门

推荐主入口控制在约 40-70 行，包含：

1. frontmatter；
2. 一句话说明“先识别首 token”；
3. 路由表；
4. 仅保留跨所有分支都成立的 3 条硬门；
5. 子命令 reference 指针；
6. 未知参数进入 help。

应从主入口移出的内容：

- 需求/缺陷特有的源码修改门；
- 规则文件追加细节；
- 运行时安装策略；
- 版本看板解析算法；
- 大段反例和重复的“不要做的事”；
- 每次调用的自检问询。

需求和缺陷只需要在自己的入口保留“门控摘要”，完整规则放到共享 `STATE-MACHINE.md` / `CODING-GATE.md`。

---

## 4.4 建立共享契约层，消除复制粘贴

建议新增一个只读 reference 层（名称可按最终架构调整）：

```text
references/_shared/
├── workspace.md             # assistants 目录、路径和访问矩阵
├── state-machine.md         # 阶段、状态、转换、恢复
├── artifacts.md             # 每阶段输入/输出/完成条件
├── permissions.md           # 源码、规则、看板和导出路径的写权限
├── confirmation.md          # default/confirm/auto 三态
├── failure-policy.md        # BLOCKED/RECOVERABLE/FATAL
├── status-enums.md          # 开发、测试、运行时、缺陷状态
└── parser-contracts.md      # RESULT、PROCESS、模板锚点和 ID 规则
```

每个子命令只保留自己特有的分支和动作。这样可以把当前散落于：

- 主 `SKILL.md`；
- `req/SKILL.md`；
- `fix/SKILL.md`；
- `req/common.md`；
- `runtime-environment.md`；
- `CLAUDE.md`

中的同义规则收敛到单一事实源。

---

## 4.5 用“阶段摘要 + 按需 reference”实现真正的渐进披露

`req/SKILL.md` 和 `fix/SKILL.md` 当前把大量阶段细节直接铺在入口中。建议改成：

```text
## 工作流摘要
1. INIT：建立工作目录和 PROCESS.md → state-machine.md
2. REQUIRE/BUG：形成业务基线 → require.md 或 fix-register.md
3. DESIGN：形成可排期设计 → design.md
4. PLAN：形成可执行任务图 → plan.md
5. CODING：在源码门控内逐任务实现 → coding.md
6. CHECK：审查并按需回到 CODING → check.md
7. DONE：完成条件和提交结果 → artifacts.md
```

每个阶段开始时再读取对应的详细文件。每个详细文件开头用 5-10 行写清：

- 前置条件；
- 输入；
- 动作；
- 输出；
- 可检查完成条件；
- 失败时去哪里。

这比“入口里写一遍 + reference 再写一遍”更可预测。

---

## 4.6 为每个阶段补可勾选的完成条件

建议将以下完成条件写入共享契约，并在阶段 reference 的末尾重复一行指针，而不是散落在叙述中。

### req

| 阶段 | 完成条件 |
| --- | --- |
| INIT | 版本已激活；`req/REQ-NNNNN/` 存在；`PROCESS.md` 有 INIT 开始记录；CWD 源码未改 |
| REQUIRE | `REQUIRE.md` 存在且保留原始输入；所有 FR/NFR/AC 有来源或“假设”标记；技术选型未误写；关联需求已检索；看板条目不重复 |
| DESIGN | 每个 FR/关键 AC 都能映射到模块/接口/流程；方案决策含选项、理由、权衡；危险操作已有明确确认 |
| PLAN | 所有设计模块都有任务覆盖；任务 ID 唯一；依赖无环；每项有完成标准、验证方式、开发/测试初始状态 |
| CODING | 每个可执行任务都有 TASK 报告；源码修改发生在 CODING 门内；验证结果是明确枚举；PLAN 状态已同步；偏差已记录 |
| CHECK | 所有任务和变更已审查；所有发现有文件/行号、级别、状态；未处理必须改为 0，或明确进入阻塞/轮次上限分支 |
| DONE | 关键产物齐全；PROCESS 最后一条为 DONE 完成；提交成功或明确记录跳过原因；下一步建议与真实命令一致 |

### fix

将 REQUIRE 替换成 BUG 登记，并额外要求：

- 复现步骤和期望/实际行为清晰；
- 严重度有证据或用户确认；
- 根因是假设时必须标注假设；
- 修复任务至少覆盖复现路径和回归验证。

### ver --publish

完成条件应明确为：

- 当前版本已定位；
- 需求/缺陷/任务状态来自同一个权威 schema；
- 所有发布阻塞项为空；
- 手册只在通过后生成；
- 生成文件列表与基线/非基线规则一致；
- 失败时不产生半成品手册。

### merge

完成条件应明确为：

- 当前确实是 linked worktree；
- feature 和 target 工作区都满足 clean 前置；
- 没有 unmerged 文件；
- target 分支产生预期 no-ff merge commit；
- 看板检查结果可复现；
- 未自动 push/remove，且报告清楚说明这一点。

---

## 4.7 统一失败模型和重试预算

建议所有子命令采用三档失败分类：

| 类别 | 含义 | 统一处置 |
| --- | --- | --- |
| `BLOCKED` | 缺少前置产物、依赖用户决策或环境 | 写入 PROCESS，保留当前产物，退出等待续跑 |
| `RECOVERABLE` | 可退回上阶段重做的解析/产物问题 | 写失败记录，指定回退阶段，下一次从该阶段开始 |
| `FATAL` | 权限、安全门、不可逆合并/提交失败 | 停止，不推进状态，必要时回滚本次变更 |

每条 PROCESS 记录建议增加稳定的事件语义：

```text
| 时间 | 阶段 | 状态 | 结果类别 | 目标 | 摘要 |
```

如果不想改变现有 4 列格式，也至少在摘要中固定 `[BLOCKED]`、`[RECOVERABLE]`、`[FATAL]` 前缀。

此外，CODING 错误重试和 CHECK 修复循环不应各自独立拥有“5 次”而不说明总预算。建议使用一个执行上下文计数器：

```text
retryBudget.total = 10
retryBudget.coding = ...
retryBudget.review = ...
```

每次消耗时在屏幕和 PROCESS 中显示剩余预算，避免用户遇到多层嵌套循环却不知道还会尝试多久。

---

## 4.8 正向表述硬门，减少无效否定

当前许多文件反复写“不要调 EnterPlanMode”“不要在非 CODING 修改源码”“不要重写规则”。其中源码门和规则追加是必要硬约束，但可以用正向执行句作为主规则：

```text
需求和缺陷工作先建立版本目录、业务基线和 PROCESS.md；只有 PROCESS.md 当前阶段为 CODING 时才编辑 CWD 源码。

已有规则文件采用末尾追加；首次出现的分类才创建文件。
```

只有无法等价表达的安全禁令保留“禁止”形式，并紧跟替代动作。这样既减少否定触发，也让模型更容易执行目标行为。

---

# 5. 文件级详细改修建议（只建议，不实施）

以下列表用于后续真正开发时分任务。当前均未修改。

| 优先级 | 文件 | 建议改修 |
| --- | --- | --- |
| P0 | `.claude-plugin/plugin.json`、根 `.claude-plugin/marketplace.json` | 先确定单入口或多独立 skill；让清单、目录、frontmatter 和 README 采用同一模型；补充注册冒烟验证结果 |
| P0 | `skills/code/SKILL.md` | 缩短为路由器；删除每次调用的自检问询；保留最小跨流程门控；统一 6+1 命令计数 |
| P0 | `references/faq/common.md` | 修正 REQUIRE 章节映射；改用稳定标题/锚点；统一模板占位符语法和未识别处理 |
| P0 | `references/req/require.md`、`design.md`、`plan.md`、`coding.md`、`check.md`、`references/fix/fix-register.md` | 修复全部 `templates/...` 路径；增加链接存在性约定 |
| P0 | `references/ver/common.md`、`ver/SKILL.md` | 统一 `req/` 与 `require/`；重写发布检查的数据来源；明确 CWD 版本同步是否需要显式 flag |
| P0 | `references/ver/common.md`、`req/require.md`、`fix/fix-register.md`、`merge/SKILL.md` | 定义唯一 RESULT schema；决定状态从 PROCESS 派生还是存列；同步看板和发布算法 |
| P1 | `references/req/plan.md`、`templates/req/PLAN.md` | 统一开发状态/测试状态列、初值、转移和依赖格式 |
| P1 | `references/req/check.md`、`templates/req/CHECK.md` | 补齐审查维度、权重、代码行数、测试覆盖和结论判定 |
| P1 | `references/runtime-environment.md`、`templates/req/TASK.md` | 统一运行时枚举，区分机器值和展示值，保留隐私约束 |
| P1 | `references/req/require.md` | 合并技术选型过滤词表，取消不准确的关键词数量描述，定义冲突优先级 |
| P1 | `references/merge/SKILL.md` | 解析 target 主工作区；分别检查两侧 dirty；unmerged 文件返回失败；补充 dry-run/确认策略评估 |
| P1 | `references/req/SKILL.md`、`references/fix/SKILL.md` | 改为阶段摘要；把共性门控、恢复、确认和错误策略移到 `_shared/` |
| P1 | `references/req/common.md` | 成为状态机和产物契约唯一来源；消除与 req/fix SKILL 的重复实现 |
| P1 | `references/rule/SKILL.md`、`templates/rule/*` | 为 Type A/B/C 补目标、权限、模板选择、编号和完成条件；明确是否允许修改 CLAUDE/template |
| P1 | `templates/fix/fix-registry.md` | 标记 legacy 或重新纳入主流程；不要与 RESULT 同时作为事实源 |
| P2 | `README.md`、`README.en.md`、插件 `CLAUDE.md` | 统一命令计数、阶段数、默认确认行为、安装后实际入口和 help 说明；最好从共享命令矩阵生成 |
| P2 | `references/help/SKILL.md` | 作为命令矩阵的消费方，统一 7 个选项、错误示例和参数优先级 |
| P2 | 所有 `SKILL.md` frontmatter | 精简为触发描述；将内部纪律移入正文；若独立注册，确保每个 description 互斥 |
| P2 | `templates/req/*.md`、`templates/fix/*.md` | 增加小需求/简单缺陷的折叠规则和“无此内容时如何填写”说明 |
| P3 | 全部 Markdown | 引入静态链接、占位符、章节、枚举和命令示例一致性检查；去除重复“不要做的事” |

---

# 6. 建议的分阶段实施路线

## Phase 0：契约决策（先不改行为）

1. 决定单入口还是多独立 skill；
2. 决定 `RESULT.md` 是索引还是动态状态源；
3. 决定 canonical 路径为 `req/` 还是兼容 `require/`；
4. 决定默认确认模式；
5. 决定 `/code ver` 是否允许修改 CWD 描述文件；
6. 决定 `fix-registry.md` 是继续使用还是标记遗留。

**退出标准**：上述 6 项各有一条可执行决策，并记录受影响文件。

## Phase 1：修复功能正确性

1. 修正 FAQ 映射；
2. 修正模板链接；
3. 统一基线路径；
4. 统一 RESULT/PROCESS/PLAN/BUG 的状态来源；
5. 修复 publish、dashboard、merge 的读取契约；
6. 统一模板和参考文件字段。

**退出标准**：每个生产者写入的字段，都能被每个消费者按同一名称读取；没有指向不存在文件的模板引用。

## Phase 2：重构技能层级

1. 新建 `_shared/` 契约 references；
2. 将主 SKILL 缩成路由器；
3. 将 req/fix 入口改成阶段摘要；
4. 将详细逻辑按阶段按需加载；
5. 精简 description；
6. 去掉重复全局禁令和 no-op 说明。

**退出标准**：每个阶段有唯一主定义；从任一子命令入口都能在不读取全部文档的情况下找到下一步 reference 和完成条件。

## Phase 3：强化可恢复性和安全

1. 统一 BLOCKED/RECOVERABLE/FATAL；
2. 统一重试预算；
3. 增加写权限矩阵；
4. 修复 merge 的主工作区操作；
5. 将危险操作、系统级安装和提交动作的确认策略统一；
6. 明确恢复时读取“最后完成事件”还是“最后事件”。

**退出标准**：每种失败场景都有明确的状态、磁盘记录、下一次入口和是否回滚说明。

## Phase 4：一致性验证和文档同步

1. 对插件路径、frontmatter、Markdown 链接做静态检查；
2. 对模板标题、章节锚点、占位符做静态检查；
3. 对状态枚举和命令示例做静态检查；
4. 运行各命令的最小冒烟场景；
5. 同步中文/英文 README；
6. 发布一份“契约版本变更说明”。

**退出标准**：所有场景矩阵通过，README、help、SKILL 和模板对同一命令给出相同行为描述。

---

# 7. 建议的验证场景矩阵

本次没有执行以下场景；它们是后续改修完成后必须验证的清单。由于仓库没有声明统一技术栈，验证应优先测试技能行为和文件契约，不应擅自假设某种项目运行时。

## 7.1 入口与注册

- `/code` 无参数是否只触发 help；
- 未知首 token 是否进入 help；
- `/code ver`、`req`、`fix` 不互相抢占；
- 插件加载后实际注册数量与设计决策一致；
- `/code help` 与 `/code --help` 行为一致。

## 7.2 ver

- 全新空项目初始化；
- 已有 `assistants/` 但缺 `.current-version`；
- 已有版本切换到新版本；
- 当前版本有未完成内容时切换；
- `--publish` 未通过时不生成手册；
- 基线和非基线版本手册数量正确；
- 看板缺区段、缺 PROCESS、坏表格时降级正确；
- 是否写 CWD 描述文件的确认和回滚正确。

## 7.3 req/fix

- 新建条目是否先创建正确目录和 PROCESS；
- 续跑从 INIT、阶段完成、阶段失败、中止、DONE 各状态恢复；
- 非 CODING 阶段尝试编辑源码是否被门控；
- `--confirm` 是否重读用户手工修改的产物；
- `--auto` 是否不弹普通问题但仍阻止危险操作；
- 任务依赖环、缺前置任务、测试不适用、运行时缺失分别如何处理；
- CHECK 必须改循环达到上限时状态和报告是否诚实。

## 7.4 faq

- 无 `.current-version` 时查询是否仍可工作；
- 同一编号跨多个版本时结果是否可区分；
- `--require`、`--design`、`--summary` 组合校验；
- 所有模板占位符是否有值；
- 未识别占位符、模板不存在、输出路径越界时结果是否明确；
- 导出过程是否绝不修改 `assistants/`。

## 7.5 rule

- 新分类新建；
- 已有分类只追加；
- 重复和冲突规则如何处理；
- Type B/C 是否写入正确目标；
- 没有版本上下文时仍能运行；
- 不会误写其他分类或版本目录。

## 7.6 merge

- 主工作区调用立即拒绝；
- feature dirty、target dirty 分别拒绝；
- target 已被主工作区 checkout 时仍能完成；
- 文本、看板、配置、二进制冲突分别处理；
- unresolved 文件不会被报告为成功；
- 不 push、不 remove worktree；
- 看板自检在新旧 schema 下结果明确。

---

# 8. 最终建议

## 8.1 最小可行改修集

如果只能进行一轮小改修，优先做以下 8 项：

1. 明确单入口/多 skill 注册模型；
2. 修正 FAQ 章节映射；
3. 修正所有模板引用路径；
4. 统一 `req/` 与 `require/`；
5. 让 publish/dashboard 从同一状态源读取；
6. 对齐 PLAN 与 CHECK 模板字段；
7. 统一默认确认行为和 help 选项数量；
8. 修正 merge 的 target worktree 操作和 unresolved 退出语义。

## 8.2 不建议的改法

- 不要继续在多个 SKILL.md 中复制同一套门控规则；
- 不要只修 README 而不修解析算法和模板；
- 不要在没有确定状态事实源前增加更多 RESULT 统计列；
- 不要把所有详细流程重新塞回主 SKILL.md；
- 不要用更多“不要……”来弥补不清晰的正向流程；
- 不要把 Type B/Type C 的隐式写权限继续留在一个模糊的 `/code rule` 入口里；
- 不要在未验证 worktree 路径和目标分支占用关系前自动执行 merge。

## 8.3 成功的最终形态

优化后的系统应满足以下判断：

> 对同一个用户意图，入口 description 只触发一个正确分支；该分支先读取一份共享状态契约，再按阶段加载一份详细 reference；每个阶段都有可检查的完成条件；每次写入都有明确权限窗口；每次失败都有统一的恢复语义；每个下游消费者都从同一个事实源读取；README、help、模板和算法对同一行为只说一种话。

这会保留当前系统最有价值的“版本感知、过程可追踪、源码门控和生命周期闭环”，同时显著降低上下文负担、文档漂移和模型提前完成/错误路由的概率。

---

## 附录 A：关键文件索引

| 能力 | 主要文件 |
| --- | --- |
| 总入口/路由 | `plugins/code-skills/skills/code/SKILL.md` |
| 插件清单 | `.claude-plugin/marketplace.json`、`plugins/code-skills/.claude-plugin/plugin.json` |
| 版本 | `skills/code/references/ver/SKILL.md`、`ver/common.md` |
| 需求 | `skills/code/references/req/SKILL.md`、`common.md`、`require.md`、`design.md`、`plan.md`、`coding.md`、`check.md` |
| 缺陷 | `skills/code/references/fix/SKILL.md`、`fix-register.md` |
| 查询导出 | `skills/code/references/faq/SKILL.md`、`faq/common.md` |
| 规则 | `skills/code/references/rule/SKILL.md` |
| 合并 | `skills/code/references/merge/SKILL.md` |
| 帮助 | `skills/code/references/help/SKILL.md` |
| 运行环境 | `skills/code/references/runtime-environment.md` |
| 语言适配 | `skills/code/references/req/languages/*.md` |
| 需求模板 | `skills/code/templates/req/*.md` |
| 缺陷模板 | `skills/code/templates/fix/*.md` |
| 规则模板 | `skills/code/templates/rule/*.md` |
| FAQ 模板 | `skills/code/templates/faq/*.md` |
| 总体协作约定 | 根 `CLAUDE.md`、`plugins/code-skills/CLAUDE.md` |

## 附录 B：本报告的变更边界

- 已阅读并分析原始技能文件；
- 已生成本 `opt.md`；
- 未对原始技能代码、Markdown、JSON、模板、README 或配置进行实际修改；
- 未运行构建、测试、lint、发布或 merge；
- 后续若要实施上述建议，应另行创建需求/设计/计划并逐项改修，而不是把本报告本身视为已完成的代码变更。
