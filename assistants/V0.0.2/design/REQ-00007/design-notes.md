# 设计笔记 — REQ-00007

更新时间:2026-06-05 09:10
版本:V0.0.2

## 关键设计问题清单

| # | 问题 | 候选数 | 选定 | 依据规范 |
| --- | --- | --- | --- | --- |
| D-1 | `code-auto` 的"主循环驱动机制"是什么?(用什么"在 Claude Code 中"串行调 6 个子技能) | 3 | A | `skill-conventions §规则 1`(沿用) |
| D-2 | `code-auto` 选 "推荐项" 的实现位置在哪?(在自身拦截 vs 要求子技能新增参数 vs 文档约定) | 3 | A | `module-conventions §规则 1`(零修改既有) |
| D-3 | "必须改"列表从哪个文件解析?(看板"评审发现汇总"区段 vs `REVIEW-REPORT.md` 某区段) | 3 | A | `dashboard-conventions §规则 1`(沿用看板锚点) |
| D-4 | `code-auto` 自身的产物文件结构?(`SKILL.md` 单一 vs `SKILL.md` + `templates/` 等) | 2 | A | `module-conventions §规则 1`(本技能无资源) |
| D-5 | `code-auto` 与"被驱动"子技能之间的契约?(`Skill` 工具 vs 文件传递 vs 共享上下文) | 3 | A | `skill-conventions §规则 1`(元信息约束) |
| D-6 | `auto-report.md` 写入失败时(`code-auto` 报告已打印到屏幕)的处理? | 3 | A | NFR-7(中断约定) |
| D-7 | SIGINT 中断时,`code-auto` 是否在退出前**尝试** flush `auto-report.md`? | 2 | A | NFR-7(中止约定:中止时**不**写) |

## 候选方案与选定方案

### D-1:主循环驱动机制

**问题**:`code-auto` 是"编排者",需要按固定顺序在 Claude Code 内部串行调 6 个子技能。具体怎么实现?

**候选**:
- **A(选定)**:`code-auto` 在自己的 `SKILL.md` 工作流中,按顺序使用 `Skill` 工具逐个调子技能(`Skill(code-require, "<原内容>")` → `Skill(code-design, "REQ-NNNNN")` → ...)。每次等子技能返回后再调下一个。**串行**是 Claude Code 模型层的自然行为。
- **B**:`code-auto` 通过 `Bash` 工具启动子进程(`claude plugin run code-require`)。需要 Claude Code 自身支持 CLI 嵌套(目前未确认)。
- **C**:`code-auto` 写一个"驱动脚本"(`scripts/auto-run.sh`),用户手动调脚本。

**选定 A 的理由**:
1. **符合 Claude Code 协议**:`Skill` 工具是 Claude Code 内置的"跨技能调用"标准方式,不需要额外依赖。
2. **零新增依赖**(NFR-1 强约束):不需要 CLI 工具或脚本。
3. **状态可观察**:`Skill` 工具每次返回时,`code-auto` 可读其输出再决定下一步,符合 NFR-10 进度可见。
4. **失败可中断**:`Skill` 调用返回时含退出状态(成功/异常),`code-auto` 可据此中断(Q-2 锁定 A)。
5. **与 REQ-00005 协同**:子技能内部已有"首步拉取 + 末步提交",`code-auto` 不需要重新实现,直接复用。

**B 被否决**:Claude Code CLI 嵌套调用未在仓库内验证过;`marketplace-protocol` 未定义 CLI 协议;风险高。

**C 被否决**:违反"用户调一次 `/code-auto`"的初衷;且本仓库不引入脚本(本仓库不写代码)。

**依据规范**:`skill-conventions.md §规则 1`(沿用)— `code-auto` 自身 frontmatter 符合规范;不修改子技能 frontmatter。

### D-2:选"推荐项"的实现位置

**问题**:`code-auto` 承诺"总选推荐项"(Q-4 锁定 A),但 `AskUserQuestion` 工具是 Claude Code 模型层行为,`code-auto` 无法直接拦截子技能内部的提问。落地方式?

**候选**:
- **A(选定)**:`code-auto` 在自己的 `SKILL.md` 中,**显式说明**"在调子技能时,若子技能内部触发 `AskUserQuestion`,**总选第一项 / 标注 (推荐) 的项**";子技能**不需要**新增"自动模式"参数(零修改)。**约定优先**,依赖子技能使用者(在 `code-auto` 驱动场景下)遵循约定。
- **B**:为 6 个子技能各加 `--auto` / `--no-confirm` 参数,在 `code-auto` 调时显式传 `--auto`。
- **C**:`code-auto` 自身**不**实现选推荐项逻辑,而是依赖"用户行为"(即用户在 `code-auto` 跑长时,主动选中"推荐")。

**选定 A 的理由**:
1. **FR-8.AC-8.1 强约束**:不修改其他 9 个子技能。B 方案违反。
2. **NFR-4 强约束**:不引入批量模式,B 方案的"参数"接近批量模式。
3. **行为一致性**:Claude Code 模型层在 `code-auto` 上下文中执行子技能时,行为与单独调子技能一致;`code-auto` 通过 prompt engineering("总选推荐项")约束子技能行为。
4. **可验证**:子技能独立运行时仍按原行为工作(NFR-4 / FR-8)。

**B 被否决**:违反 FR-8.AC-8.1(9 个子技能 SKILL.md 不被本需求修改)。

**C 被否决**:与 Q-4 锁定 A + G-4(完全无人确认)冲突;不能依赖用户行为。

**依据规范**:`module-conventions.md §规则 1`(零修改既有子技能)、`skill-conventions.md §规则 1`(不动子技能 frontmatter)。

### D-3:"必须改"列表的解析来源

**问题**:`code-auto` 需要从子技能产物中解析"必须改"任务列表,以决定是否进入派生任务循环。具体从哪个文件 / 哪个区段?

**候选**:
- **A(选定)**:`code-auto` 读 `review/REQ-NNNNN/REVIEW-REPORT.md` 的"评审发现汇总"区段,按 `code-dashboard` 解析锚点(看板 3 区段:`^## .*$` + `^\| .* \|$`)提取"必须改"行。
- **B**:读 `V0.0.2/RESULT.md` 看板的"评审发现汇总"区段(看板上也有)。
- **C**:读 `code-review` 的 stdout(不落盘)。

**选定 A 的理由**:
1. **`code-review` 既有约定**:`REVIEW-REPORT.md` 是 `code-review` 的标准产物(V0.0.1 REQ-00001 + V0.0.2 REQ-00008 确认)。
2. **数据源单一**:REVIEW-REPORT.md 是 `code-review` 的"权威产物",看板只是镜像。
3. **REQ-00008 协同**:V0.0.2 REQ-00008 明确"双写"(`REVIEW.md` 聚合 + `REVIEW-REPORT.md` 单需求),`code-auto` 消费单需求版本。
4. **NFR-6 一致性**:`code-publish` 的 PreflightChecker 也用同样锚点。

**B 被否决**:看板是"汇总视图",解析时易受其他需求干扰;`REVIEW-REPORT.md` 是单需求"权威源"。

**C 被否决**:`code-review` 输出落盘是 NFR(可追溯);stdout 易失。

**依据规范**:`dashboard-conventions.md §规则 1`(沿用看板锚点)、`encoding-conventions.md §规则 1-4`(解析"必须改"行时遵循编码格式)。

### D-4:`code-auto` 自身产物文件结构

**问题**:`code-auto` 是新技能,需要新增哪些文件?(SKILL.md 必加,其他子目录是否需要?)

**候选**:
- **A(选定)**:**仅** `plugins/code-skills/skills/code-auto/SKILL.md`(无 `templates/` / `checklists/` / `guidelines/` 子目录)。
- **B**:加 `SKILL.md` + `templates/auto-report.md`(报告模板)。

**选定 A 的理由**:
1. **`module-conventions §规则 1` 允许例外**:`SKILL.md` 本身放在技能根目录;`code-auto` 不需要模板(报告内容由 `code-auto` 运行时动态拼装,不是"模板替换式"产出)。
2. **简化**:子目录增加维护成本,无内容可放。
3. **参考其他无子目录的技能**:`code-init` / `code-version` / `code-rule` / `code-fix` 4 个技能都**无**子目录;`code-auto` 同样无外部资源(不读清单/规则/模板)。

**B 被否决**:`auto-report.md` 是**运行时输出**,不是模板;`Write` 工具直接生成即可。

**依据规范**:`module-conventions.md §规则 1`(零子目录 = 零违反)。

### D-5:与"被驱动"子技能之间的契约

**问题**:`code-auto` 与 6 个子技能的"接口边界"是什么?(子技能需要知道"被 `code-auto` 调"吗?)

**候选**:
- **A(选定)**:**无显式契约**。`code-auto` 通过 `Skill` 工具调子技能,子技能**不感知**"被 `code-auto` 调"或"被用户直接调"的区别(零修改子技能)。
- **B**:子技能加 `--caller=auto` 参数,`code-auto` 调时显式传。
- **C**:子技能读环境变量 `CODE_AUTO_RUNNING=1`,按"被编排"模式运行。

**选定 A 的理由**:
1. **FR-8.AC-8.1 强约束**:B/C 都违反(子技能 SKILL.md 不被本需求修改)。
2. **NFR-4 强约束**:不引入批量模式 / 子技能特殊路径。
3. **隔离性**:`code-auto` 是"驱动者",不污染子技能上下文。

**B/C 被否决**:违反 FR-8.AC-8.1。

**依据规范**:`module-conventions.md §规则 1`(零修改既有子技能)。

### D-6:`auto-report.md` 写入失败时的处理

**问题**:`auto-report.md` 是本需求的"完整报告留痕"(FR-10)。如果写入失败(权限/磁盘满),`code-auto` 报告内容已打印到屏幕,如何处理?

**候选**:
- **A(选定)**:**警告不中断**。`code-auto` 打印报告到屏幕(主输出)+ stderr 警告 `⚠ auto-report.md 写入失败(<原因>),报告仅输出在屏幕`;继续到下一步(或退出)。
- **B**:写入失败视为致命错误,中断 + 报告(同子技能崩溃)。
- **C**:写入失败,改为写到 `./assistants/<版本号>/require/REQ-NNNNN/auto-report.md.tmp` 等候人工处理。

**选定 A 的理由**:
1. **报告已落到屏幕**:用户**核心需求**已满足(看到报告);磁盘留痕是"附赠"。
2. **NFR-7 中止约定**:中止时**不**写,避免半成品。
3. **E-10 边界**:需求 §9 E-10 显式定义"警告,不中断"。

**B 被否决**:过度反应(用户已看到报告)。

**C 被否决**:过度工程(没有用户场景需要 .tmp)。

**依据规范**:`doc-conventions.md`(留痕是辅助手段,非强约束)。

### D-7:SIGINT 中断时是否尝试 flush `auto-report.md`

**问题**:用户 `Ctrl+C` 中止时(NFR-7 显式"不写"),`code-auto` 是否在退出前**尝试**把内存中累积的报告写盘?

**候选**:
- **A(选定)**:**不写**。`code-auto` 检测到 SIGINT,直接打印"中止报告"到屏幕 + 退出(`exit 130`);`auto-report.md` **不**生成。
- **B**:**尝试写**。"中止报告"也落盘为"部分 auto-report"。

**选定 A 的理由**:
1. **NFR-7 强约束**:中止时"**不**写 `auto-report.md`"(避免半成品)。
2. **理由**:部分报告留痕价值低,反而干扰事后追溯。

**B 被否决**:违反 NFR-7。

**依据规范**:NFR-7 强约束。

## 选定的整体架构

`code-auto` 是**单文件技能**(仅 `SKILL.md`),内含**状态机式工作流**:

```
[启动] → [步骤 0a:git pull] → [步骤 0:读 .current-version]
        → [步骤 1:Skill(code-require, "<需求>") ] → 产出 REQ-NNNNN
        → [步骤 2:Skill(code-design, REQ-NNNNN) ] → 产出 design/RESULT.md
        → [步骤 3:Skill(code-plan, REQ-NNNNN) ] → 产出 plan/{RESULT,PLAN}.md
        → [步骤 4:任务循环]
            对 plan/PLAN.md 任务总览的每个任务编码:
              - Skill(code-it, <任务编码>)
              - 若 code-it 输出含 "测试需要=Y":Skill(code-unit, <任务编码>)
        → [步骤 5:Skill(code-review, REQ-NNNNN) ] → 产出 REVIEW-REPORT.md
        → [解析"必须改"列表]
            - 若空 → [完成 + 写 auto-report.md] → [退出]
            - 若非空 → [步骤 6:派生任务循环]
                对每个派生任务:
                  - Skill(code-it, <派生任务编码>)
                  - 若需要:Skill(code-unit, <派生任务编码>)
                → 回到步骤 5
```

**关键架构决策**:
1. **`code-auto` 是"纯调度者"**:不持有"事务"概念,所有产物由子技能写盘;`code-auto` 只写 1 个文件 `auto-report.md`(完成时)。
2. **串行而非并发**(NFR-2 + Q-7 采纳默认):避免看板并发写入冲突。
3. **状态来自看板 / 产物文件,不来自内存**:`code-auto` 不维护"已完成了哪些任务"的状态机;每次循环都从 `plan/PLAN.md` / `review/REVIEW-REPORT.md` 重新解析(Q-11 采纳默认:不实现增量恢复)。
4. **子技能零修改**(FR-8.AC-8.1):`code-auto` 不向子技能传任何特殊参数,只传工作流标准参数(需求内容 / 需求编码 / 任务编码)。
5. **报告双通道**:屏幕(stdout)+ 磁盘(`auto-report.md`,完成时);异常 / 中止时仅屏幕(避免半成品)。

## 备选方案被否决的理由汇总

| 备选 | 来自 | 否决理由 |
| --- | --- | --- |
| CLI 嵌套调用 | D-1B | 协议未定义、风险高、违反 NFR-1 |
| 外部驱动脚本 | D-1C | 违反"用户调一次"初衷、仓库不写代码 |
| 子技能加 `--auto` 参数 | D-2B | 违反 FR-8.AC-8.1 |
| 依赖用户行为 | D-2C | 违反 Q-4 锁定 A |
| 读看板"评审发现汇总" | D-3B | 看板是镜像,易受其他需求干扰 |
| 读 `code-review` stdout | D-3C | stdout 易失,违反可追溯 |
| 加 `templates/auto-report.md` | D-4B | auto-report 是运行时拼装,非模板替换 |
| 子技能加 `--caller=auto` | D-5B | 违反 FR-8.AC-8.1 |
| 子技能读环境变量 | D-5C | 违反 FR-8.AC-8.1 |
| auto-report 写入失败 → 中断 | D-6B | 过度反应(用户已看到报告) |
| auto-report 写 .tmp | D-6C | 过度工程 |
| SIGINT 尝试 flush | D-7B | 违反 NFR-7 |

## 规范自检(逐条)

| 规范 | 条款 | 本设计响应 | 合规 |
| --- | --- | --- | --- |
| `skill-conventions §规则 1` | SKILL.md frontmatter 含 name+description,name 与目录名一致 | `skills/code-auto/SKILL.md` 顶部 `name: code-auto` + 完整 description | ✅ |
| `module-conventions §规则 1` | 资源放 `templates/` / `checklists/` / `guidelines/` 固定子目录 | `code-auto/` 无子目录(无资源) | ✅ |
| `marketplace-protocol §规则 1` | $schema / name / version 必填,skills 是相对路径数组 | **不**修改 marketplace.json / plugin.json | ✅ |
| `dashboard-conventions §规则 1` | 字段约定扩展需三同步 | 本设计**不**扩展字段,只追加"概要设计清单"行 | ✅ |
| `doc-conventions §规则 1` | README 中英同次提交 + 结构对仗 | 中英 README 同次追加 1 行能力描述(FR-8.AC-8.5) | ✅ |
| `doc-conventions §规则 2` | README 必须存在并持续维护 | 不修改 README 主体,只追加 1 行 | ✅ |
| `encoding-conventions §规则 1-4` | 编码格式权威源 | **不**产生新编码,仅消费既有 | ✅ |
| `migration-mapping §规则 1-4` | 已落地映射 | 不追溯 V0.0.0 EXISTING-NNN | ✅ |
| `commit-conventions`(占位) | 待添加 | NFR-3 显式不沉淀(留 follow-up) | ✅ |
| `dependency-conventions`(占位) | 待添加 | NFR-1 显式零新增依赖 | ✅ |

**结论:本设计 100% 合规,0 用户授权偏离,0 待澄清冲突。**
