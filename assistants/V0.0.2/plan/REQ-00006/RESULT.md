# REQ-00006 — 详细设计:`/code-publish` 发布部署技能

- 需求编码:`REQ-00006`
- 所属版本:`V0.0.2`
- 上游需求:`./assistants/V0.0.2/require/REQ-00006/RESULT.md`(v1,已锁定)
- 上游概要设计:`./assistants/V0.0.2/design/REQ-00006/RESULT.md`(v1,已完成首次)
- 遵循规范:`./assistants/rules/` 下 4 个有效约束(`skill-conventions` / `module-conventions` / `dashboard-conventions` / `doc-conventions`)+ 6 个占位 + 3 个不相关
- 状态:已完成(首次详细设计)
- 责任人:wangmiao
- 创建:2026-06-04
- 最近更新:2026-06-04 17:01
- 当前版本:v1

---

## 1. 详细设计概述

在概要设计 7 个新增模块(`code-publish` SKILL + 6 个逻辑模块)+ 5 份模板的基础上,本详细设计补充了**实现层面**的 8 项决策 DD-1 ~ DD-8(看板解析的具体 Bash 命令链、字段名识别 vs 列号位置、字典序工具、placeholder 替换方式、覆盖前预检、Q&A 章节生成规则、错误退出行为、幂等的字节级语义)。对应的编码计划 `PLAN.md` 共 **8 条任务**(T-001 SKILL.md + T-002~T-006 5 份模板 + T-007 不变量自检与看板同步 + T-008 双 README 同步),全部位于 `plugins/code-skills/skills/code-publish/` 与少量"项目级 + 看板级"位置,严格 0 修改其他既有产物。

---

## 2. 上游引用

### 2.1 需求

`./assistants/V0.0.2/require/REQ-00006/RESULT.md` 关键摘录:
- **9 FR**:FR-1 前置检查 / FR-2 生成 3 份手册 / FR-3 DEPLOY 模板 / FR-4 UPDATE 模板 / FR-5 Q&A 模板 / FR-6 创建 qanda/ 骨架 / FR-7 错误处理 / FR-8 不修改其他 8 技能 / FR-9 报告
- **9 NFR**:零依赖 / 纯只读检查 / 不自动 commit / 不参与 REQ-00005 / 通用性优先 / 幂等覆盖 / 基线识别 / 与 dashboard 一致 / 可读性优先
- **~33 AC**(详 needs §10)
- **10 边界**:E-1 ~ E-10
- **已锁定** Q-1 ~ Q-4 + 默认采纳 Q-5 ~ Q-9

### 2.2 概要设计

`./assistants/V0.0.2/design/REQ-00006/RESULT.md` 关键摘录:
- **7 新增模块**(详 design §7.1 / §7.2)
- **5 份模板**(详 design §7.2.8 ~ §7.2.12)
- **0 修改既有**(design §7.4)
- **0 新增依赖**(design §10.2)
- **8 项决策 D-1 ~ D-8**(详 design §13 + `design-notes.md`)
- **完全合规**:0 偏离 / 0 待澄清冲突(详 design §2.5.2)

### 2.3 规范

详 `materials-index.md §1` + `rule-compliance.md`。4 个有效约束规范均被自检,0 冲突。

---

## 3. 规范遵循

详 `rule-compliance.md`。本节简版:

### 3.1 适用规范文件与对应章节

| 规范文件 | 关键条款 | 本设计对应章节 |
| --- | --- | --- |
| `skill-conventions.md §规则 1` | SKILL.md frontmatter 必含 `name` + `description` | §4 模块详细化 1 (T-001) |
| `module-conventions.md §规则 1` | templates/ / checklists/ / guidelines/ 固定子目录 | §4 模块详细化 8~12 (T-002~T-006) |
| `dashboard-conventions.md §规则 1` | 看板字段扩展需 3 处同步 | 0 触发(本设计不扩展看板字段) |
| `doc-conventions.md §规则 1 + §规则 2` | README 多语言对仗 + 持续维护 | §4 模块详细化:T-008 双 README 同步约束 |

### 3.2 自检结论
- **完全合规**:§4 / §5 / §6 / §7 / §8 / §9 / §10 / §11 / §12
- **用户授权偏离**:**0**
- **待澄清冲突**:**0**

### 3.3 用户授权的偏离
- 无

### 3.4 待澄清的规范冲突
- 无

---

## 4. 模块详细化

详 `module-details.md`。本节给每个模块的关键摘要 + 对应任务。

### 模块 1:`code-publish` 技能(SKILL.md)(对应 design §7.2.1)

- **关键类/函数**:无(纯文档,Claude 自然语言执行)
- **关键调用顺序**:Step 0(版本上下文)→ Step 1(PreflightChecker)→ Step 2.0(BaselineDetector)→ Step 2(ManualBuilder)→ Step 2.5(QandaScaffolder)→ Step 2.6(QandaAggregator)→ Step 3(ReportFormatter)
- **并发模型**:单进程顺序
- **资源管理**:无连接/锁/缓存
- **错误处理范式**:文本报告 + 不留半成品 + 退出(模仿其他 7 版本感知技能)
- **日志埋点**:无(Step 3 报告即日志)
- **依据规范**:`skill-conventions.md §规则 1` + `module-conventions.md §规则 1`
- **对应任务**:T-001

### 模块 2:PreflightChecker(对应 design §7.2.2)

- **关键函数**:`preflight_check(version_number) → PreflightResult` + `extract_section` + `parse_header_row` + `parse_data_rows` + `is_resolved`
- **关键调用顺序**:Read 看板 → 对 3 区段:extract → parse_header → parse_data → 对每行 is_resolved 累积 undone → 汇总
- **错误处理范式**:看板不存在 → `passed: false`(不抛);区段不存在 → 退化"全未解决"
- **依据规范**:NFR-2 纯只读 + NFR-8 与 dashboard 一致
- **对应任务**:T-001(SKILL.md 步骤 1)

### 模块 3:BaselineDetector(对应 design §7.2.3)

- **关键函数**:`detect_baseline(target_version) → BaselineResult`
- **关键调用顺序**:Glob ./assistants/*/ → 过滤 + 字典序 sort → 取 min → 比较 + 前一版本
- **错误处理范式**:target 不在列表 → 报错退出
- **依据规范**:NFR-7 规则 1
- **对应任务**:T-001(SKILL.md 步骤 2.0)

### 模块 4:ManualBuilder(对应 design §7.2.4)

- **关键函数**:`build_manuals(version, baseline_result) → ManualBuildResult` + `write_one_manual(template, target, replacements)`
- **关键调用顺序**:mkdir publish/ → ls existing → Read+渲染+Write DEPLOY → (非基线)Read+渲染+Write UPDATE → (Q&A 由 §2.6 渲染)Write Q&A
- **错误处理范式**:mkdir 失败 → 报错退出(E-7);Write 失败 → 立即退出不留半成品
- **依据规范**:FR-2 / FR-3 / FR-4 / NFR-6
- **对应任务**:T-001(SKILL.md 步骤 2)+ 模板由 T-002 / T-003 提供

### 模块 5:QandaScaffolder(对应 design §7.2.5)

- **关键函数**:`scaffold_qanda() → QandaScaffoldResult`
- **关键调用顺序**:ls qanda/ → 不存在 → mkdir + Write README.md(从 templates/qanda-README.md)→ 失败 → 不阻塞
- **错误处理范式**:mkdir/Write 失败 → 标记 `创建失败`,继续 Step 2.6
- **依据规范**:FR-6 + FR-7.AC-7.4
- **对应任务**:T-001(SKILL.md 步骤 2.5)+ 模板由 T-005 提供

### 模块 6:QandaAggregator(对应 design §7.2.6)

- **关键函数**:`aggregate_qanda() → QandaAggregateResult`
- **关键调用顺序**:Glob qanda/*.md → 过滤 README → 按文件名排序 → 空 → 占位;非空 → 占位 + 每文件渲染"## 名 + 来源 + 全文"
- **错误处理范式**:单文件读取失败 → 跳过 + 在 Q&A.md 加警告
- **依据规范**:FR-5 + AC-5.4
- **对应任务**:T-001(SKILL.md 步骤 2.6)+ 模板由 T-004 提供

### 模块 7:ReportFormatter(对应 design §7.2.7)

- **关键函数**:`format_report(*4 results) → str` + 4 个子函数
- **关键调用顺序**:根据 4 输入选择模板 → 渲染 → stdout
- **错误处理范式**:本身不应失败
- **依据规范**:FR-9 + NFR-9
- **对应任务**:T-001(SKILL.md 步骤 3)

### 模块 8 ~ 12:5 份模板

| 模块 | 路径 | 任务 |
| --- | --- | --- |
| `templates/DEPLOY.md` | `plugins/code-skills/skills/code-publish/templates/DEPLOY.md` | T-002 |
| `templates/UPDATE.md` | 同上目录 | T-003 |
| `templates/Q&A.md` | 同上目录 | T-004 |
| `templates/qanda-README.md` | 同上目录 | T-005 |
| `templates/assistants-layout.md` | 同上目录 | T-006 |

详 `module-details.md`。

---

## 5. 算法与逻辑

详 `design-notes.md §2`。本节给关键算法的伪代码 + 流程图。

### 算法 1:PreflightChecker

- **目的**:解析版本看板 3 区段,判定是否可发布
- **输入**:`version_number: str`(版本号)
- **输出**:`PreflightResult`(见 §9.1)
- **复杂度**:时间 O(N) — N = 看板行数;空间 O(N)
- **依赖**:`Read` 工具
- **伪代码**:见 `design-notes.md §2 算法 1`(完整版)
- **关键决策**:
  - 字段名识别 vs 列号(DD-2):选**字段名**,容忍未来新增列
  - 退化策略(DD-7):区段不存在 → 该区段"全未解决";容忍而非崩溃
- **边界条件**:
  - 空看板 → 退化为"3 区段全空 → 通过"(0/0 都满足)
  - 区段含 0 行数据 → 该区段 0/0(通过)
  - 状态值含未知枚举 → 视为"未解决"(保守判定)
  - 旧格式编码(REQ-00001-001)→ 按字符串处理(E-9)
- **对应任务**:T-001
- **依据规范**:NFR-2 + NFR-8

### 算法 2:BaselineDetector

- **目的**:判定目标版本是否是基线(规则 1:字典序最小)
- **输入**:`target_version: str`
- **输出**:`BaselineResult`(见 §9.2)
- **复杂度**:O(V) — V = 总版本数;空间 O(V)
- **依赖**:`Glob` 工具
- **伪代码**:见 `design-notes.md §2 算法 2`
- **关键决策**:
  - 字典序工具(DD-3):Bash `sort` 默认 ASCII 字典序
  - 排除 `rules` / 隐藏文件(详 DD-3 Bash 命令)
- **边界条件**:
  - 只有 1 个版本 → 该版本即基线
  - target_version 不在列表 → 报错退出(严重不一致)
- **对应任务**:T-001
- **依据规范**:NFR-7 规则 1

### 算法 3:ManualBuilder

- **目的**:生成 2 或 3 份手册到 publish/
- **输入**:`version_number, baseline_result`
- **输出**:`ManualBuildResult`(见 §9.4)
- **复杂度**:O(1)(固定 3 文件)
- **依赖**:`Bash`(mkdir/ls)+ `Read`(模板)+ `Write`(目标)
- **伪代码**:见 `design-notes.md §2 算法 3`
- **关键决策**:
  - placeholder 替换方式(DD-4):Claude 在 Write 时直接渲染(无 sed)
  - 覆盖前预检(DD-5):ls 现有 → 报告"将覆盖 N 个"
- **边界条件**:
  - publish/ 不存在 → mkdir
  - mkdir 失败 → E-7
  - Write 失败 → 立即退出
  - 已有 0 文件 → 0 覆盖
- **对应任务**:T-001(消费 T-002/T-003 提供的模板)
- **依据规范**:FR-2/3/4 + NFR-6

### 算法 4:QandaScaffolder + QandaAggregator + ReportFormatter

详 `design-notes.md §2`。3 算法都遵循"单线程顺序 + 失败软退化 + 不阻塞"原则。

### 流程图(对应 design §5.3 的控制流)

```mermaid
graph TD
    Start[/code-publish [version]/]
    Step0[Step 0: 版本上下文]
    E5[E-5: 提示调 code-version<br/>退出]
    E2[E-2: 看板不存在<br/>提示用户<br/>退出]
    Step1[Step 1: PreflightChecker]
    E1[E-1/E-2: 不通过<br/>报告 + 退出]
    Step20[Step 2.0: BaselineDetector]
    Step2[Step 2: ManualBuilder]
    E7[E-7: mkdir/Write 失败<br/>报错 + 退出]
    Step25[Step 2.5: QandaScaffolder<br/>失败不阻塞]
    Step26[Step 2.6: QandaAggregator]
    Step3[Step 3: ReportFormatter]
    End[End/stdout]

    Start --> Step0
    Step0 -->|无 .current-version 且无参数| E5
    Step0 -->|看板不存在| E2
    Step0 -->|成功| Step1
    Step1 -->|不通过| E1
    Step1 -->|通过| Step20
    Step20 --> Step2
    Step2 -->|mkdir/Write 失败| E7
    Step2 -->|成功| Step25
    Step25 --> Step26
    Step26 --> Step3
    Step3 --> End
    E1 --> End
```

---

## 6. 数据结构完整变更

详 `data-changes.md`。

### 6.1 新增实体
- **0 个持久化实体**(无 DB、无 ORM)
- **6 个运行时数据结构**(内存):PreflightResult / UncompletedItem / BaselineResult / ManualBuildResult / QandaScaffoldResult / QandaAggregateResult(详 `data-changes.md §2`)

### 6.2 修改实体
- **0 个**(NFR-2 纯只读)

### 6.3 数据迁移
- **不适用**(无数据库迁移)

### 6.4 读侧数据格式(看板 3 区段)
- 详 `data-changes.md §3`:严格列定义 + 判定规则

### 6.5 写侧数据格式(publish/ 3 份手册 + qanda/ README)
- 详 `data-changes.md §4`:DEPLOY.md / UPDATE.md / Q&A.md / qanda-README.md 完整字段

---

## 7. 接口细节

详 `interface-specs.md`。

### 7.1 接口总览

| 接口名 | 形式 | 状态 | 对应任务 | 依据规范 |
| --- | --- | --- | --- | --- |
| `/code-publish` | Claude Code CLI | 新增 | T-001 | `skill-conventions §规则 1` |
| `/code-publish <版本号>` | 同上 | 新增 | T-001 | 同上 |
| stdout 报告 4 种模板 | 文本 | 新增 | T-001 | NFR-9 |
| 6 个内部模块函数接口 | SKILL 自然语言 | 新增 | T-001 | 无 |

### 7.2 关键决策
- **鉴权**:无(本机文件 IO)
- **错误码体系**:无数字码;文本报告
- **限流策略**:不适用
- **幂等保证**:NFR-6 + DD-8(字节级幂等)
- **链路追踪**:不适用

---

## 8. 异常处理

详 `risk-analysis.md §1`。

按异常类别组织:
- **输入校验**:版本号防路径穿越(`/` `\` `..`);Step 0 校验
- **外部依赖**:无(0 网络)
- **并发冲突**:不适用
- **资源耗尽**:写文件失败 → E-7 报错退出
- **业务异常**:前置检查不通过 → E-1 报告分支
- **未知异常**:无全局兜底(技能本身简单)

每条异常的"触发 → 检测 → 处理 → 监控 → 对应任务"详 `risk-analysis.md §1`(10 条异常路径 vs needs §9 E-1 ~ E-10 全覆盖)。

---

## 9. 安全要求

详 `risk-analysis.md §2`。

- **鉴权**:不适用(本机)
- **授权**:不适用
- **输入校验**:版本号防路径穿越;qanda 文件名靠 Glob 过滤
- **敏感数据**:模板内 `<默认账号>` 警告 + Step 3 报告提醒"git diff 审阅再 commit"(避免口令落 git)
- **防注入**:不适用(Markdown 渲染场景)
- **审计**:不适用(Claude Code 本身记录调用)
- **依据规范**:无安全规范文件

---

## 10. 状态机 / 流程

本技能**无有状态对象**(每次调用独立,无持久化状态)。

可发布版本的"状态"在版本看板中由 `code-require` / `code-plan` / `code-it` / `code-unit` / `code-review` 维护(需求/任务/缺陷的状态机),本技能**只读消费**。

---

## 11. 性能与资源

详 `risk-analysis.md §3`。

- **关键路径耗时目标**:P95 < 5 秒
- **并发上限**:不适用(单次调用)
- **资源限制**:看板内存 < 1 MB;聚合 qanda < 10 MB
- **缓存策略**:无(每次重读看板,符合 NFR-6 幂等)
- **批量/异步**:不适用
- **降级策略**:看板缺区段 → 退化"全未解决";qanda mkdir 失败 → 退化"占位 Q&A"

---

## 12. 测试要点

详 `risk-analysis.md §5`。

| 测试类型 | 范围 | 对应任务 |
| --- | --- | --- |
| 单元测试 | 不适用(纯文档项目无传统单测) | — |
| 集成测试 | 不适用(NFR-4 不与其他技能集成) | — |
| 端到端测试 | 2 个场景:V0.0.2 上调技能(预期不通过)+ V0.0.0 调技能(预期基线通过) | T-007 不变量自检 |
| 性能测试 | 不适用(< 5 秒) | — |
| 安全测试 | 路径穿越拒绝 | T-007 |
| 回归测试 | 0 受影响旧功能 | T-007 |
| AC 验证 | ~33 AC vs 实际行为对照 | T-007 |
| 双 README 同步 | T-008 完成后 git log 验证同次提交 | T-008 + T-007 |

**T-001 ~ T-008 任务的测试状态默认 `不适用`**(纯文档型技能);`code-review` 后续若要求,可补"手动验证脚本"。

---

## 13. 关联编码计划

详 `PLAN.md`。本节列任务编号 + 对应设计章节(交叉引用):

| 任务编号 | 标题 | 对应本 RESULT.md 章节 |
| --- | --- | --- |
| `TASK-REQ-00006-00001` | [新增] 写 `code-publish/SKILL.md`(7 模块工作流) | §4 模块 1~7 + §5 算法 1~4 + §7 + §8 |
| `TASK-REQ-00006-00002` | [新增] 写 `templates/DEPLOY.md` 模板 | §4 模块 8 + §6.5 |
| `TASK-REQ-00006-00003` | [新增] 写 `templates/UPDATE.md` 模板 | §4 模块 9 + §6.5 |
| `TASK-REQ-00006-00004` | [新增] 写 `templates/Q&A.md` 模板 | §4 模块 10 + §6.5 |
| `TASK-REQ-00006-00005` | [新增] 写 `templates/qanda-README.md` 模板 | §4 模块 11 + §6.5 |
| `TASK-REQ-00006-00006` | [新增] 写 `templates/assistants-layout.md` 模板 | §4 模块 12 |
| `TASK-REQ-00006-00007` | [文档] 不变量自检 + 同步看板 + 偏差日志 | §3 规范遵循 + §12 测试要点 |
| `TASK-REQ-00006-00008` | [修改] 同步双 README "主要能力" 段(中英同次提交) | §3 + `doc-conventions §规则 1` |

---

## 14. 待澄清 / 未决项

继承自 design §15 的 7 项 Q-D 全部维持(详 `clarifications.md`)。本阶段新增 0 项(Q-D-8 在 `clarifications.md §3` 已完成本计划决策 → 拆为 T-008)。

| 编号 | 问题 | 影响范围 | 阻塞方 | 期望回复时间 |
| --- | --- | --- | --- | --- |
| Q-D-1 | `code-publish` 注册 marketplace.json | 跨需求 | code-review 派生 | code-review 阶段 |
| Q-D-2 | README "主要能力" 同步 | T-008 | **本计划已纳入** | — |
| Q-D-3 | 沉淀 publish-conventions.md | 跨需求 | code-review | code-review 阶段 |
| Q-D-4 | dashboard "全完成" 升级建议 | REQ-00004 | REQ-00004 设计 | — |
| Q-D-5 | 加入 REQ-00005 改写 | 跨需求 | code-review | code-review 阶段 |
| Q-D-6 | v2 `--force` 实现方式 | v2 | v2 | v2 |
| Q-D-7 | 报告升级 REQ-NNNNN·标题 | 跨需求 | code-review | code-review 阶段 |

**本计划 0 阻塞项**;Q-D-1 ~ Q-D-7 全部不影响 `code-it` 实施。

---

## 15. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-04 17:01 | v1 | 初始创建 | 完成首次详细设计(8 项实现层决策 DD-1~DD-8),对应 PLAN.md v1 的 8 条任务(T-001 SKILL.md + T-002~T-006 5 份模板 + T-007 自检 + T-008 双 README 同步);Q-D-2 升级为本计划决策(T-008 拆为独立任务);0 修改既有产物 + 0 新增依赖 + 0 偏离 + 0 待澄清冲突 | wangmiao |
