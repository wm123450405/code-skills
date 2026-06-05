# REQ-00011 详细设计 — code-design / code-plan 步骤 0b 设计目标确认(实施细化)

> 写入方:`code-plan` 技能
> 上游:./assistants/V0.0.2/require/REQ-00011/RESULT.md
> 上游概要设计:./assistants/V0.0.2/design/REQ-00011/RESULT.md
> 遵循规范:`./assistants/rules/` 下 13 个文件(详 `rule-compliance.md`)
> 创建时间:2026-06-05
> 状态:**已完成(详细设计)**
> 编码计划:./assistants/V0.0.2/plan/REQ-00011/PLAN.md(2 任务 T-001 / T-002)

---

## 1. 详细设计概述

本详细设计在概要设计的基础上**细化实施锚点、伪代码、屏显输出模板**。覆盖 4 个文件改动点(2 SKILL.md 增量追加 + 2 templates 顶部预留位);新增 1 个算法(`askDesignGoals`),1 个回写策略(`writeDesignGoalsSection`),1 个回读策略(`readDesignGoalsFromDesign`),1 个任务粒度调整判定表;**0**新增模块,**0**新增依赖,**0**触发 `dashboard-conventions §规则 1` 3 处同步;**0**修改其他 8 个 `code-*` 技能;`code-auto` 沿用"总选推荐项"行为(NFR-5 强约束);`code-design` / `code-plan` 步骤 0a 既有说明中"`code-*` 不含步骤 0b"小注需被本需求**更新**(本需求后,`code-design` / `code-plan` 也含步骤 0b)。

## 2. 上游引用

- **需求**:`./assistants/V0.0.2/require/REQ-00011/RESULT.md`
  - 9 FR / 8 NFR / ~30 AC
  - 关键 FR:FR-1(`code-design` 步骤 0b)/ FR-2(`code-plan` 步骤 0b 沿用)/ FR-3(`code-plan` 退化)/ FR-4(任务粒度调整)/ FR-5(回写小节)/ FR-6(`AskUserQuestion` 多问题)/ FR-7(不改 8 技能)/ FR-8(不改 marketplace/plugin/规范)/ FR-9(报告)
- **概要设计**:`./assistants/V0.0.2/design/REQ-00011/RESULT.md`
  - 8 决策(D-1 ~ D-8)+ 8 不变量(INV-1 ~ INV-8)+ 8 风险(R-1 ~ R-5)
  - 关键决策:D-1 步骤 0b 位置 / D-2 顶部"## 设计目标"小节 / D-3 1-5 问自适应 / D-4 沿用或退化 / D-5 任务粒度调整 / D-6 幂等 / D-7 与 `code-auto` 0 冲突 / D-8 模板顶部预留
- **规范**:`./assistants/rules/` 13 个文件(详 `rule-compliance.md`)

## 3. 规范遵循

- 适用的规范文件与对应章节:详 `rule-compliance.md §1`
- 自检结论:**完全合规**(0 偏离,0 授权偏离,0 待澄清)
- 关键合规点:INV-1 frontmatter 不变 / INV-2 既有步骤 0-N 流程不变 / INV-3 顶部"## 设计目标"小节位置 / INV-4 沿用或退化 / INV-5 幂等 / INV-6 扩展性高 → 加扩展性任务 / INV-7 `code-auto` 0 冲突 / INV-8 不触发 `dashboard-conventions §规则 1`

## 4. 模块详细化

### 模块 1:`code-design` 步骤 0b(对应概要设计 §3 D-1 ~ D-3,§5.3)
- **路径**:`plugins/code-skills/skills/code-design/SKILL.md`
- **关键类/函数**(伪代码层面):
  - `askDesignGoals(needContext: NeedContext): DesignGoals` — 触发 1-5 个 `AskUserQuestion`,收集用户回答
  - `writeDesignGoalsSection(resultMdPath: string, goals: DesignGoals, trigger: "code-design"): void` — 写入 `design/.../RESULT.md` 顶部"## 设计目标"小节
- **内部状态**:**无**持久化状态;每次执行都触发 `AskUserQuestion`,结果写入文件
- **关键调用顺序**:
  1. 步骤 0a 拉取(REQ-00005 既有)
  2. **步骤 0b 触发 `AskUserQuestion`**(本需求新增)
  3. 收集回答 → 写"## 设计目标"小节
  4. 屏幕打印"已回写至 design/<REQ>/RESULT.md '## 设计目标' 小节"
  5. 进入步骤 0(版本上下文检测)— 沿用既有
- **并发模型**:单技能串行,无并发
- **资源管理**:无新资源
- **错误处理范式**:
  - 用户取消 `AskUserQuestion` → 中止 + 回写空"## 设计目标"小节(E-3)
  - 写文件失败 → 透传 stderr,中断退出
- **日志埋点**:屏显"=== code-design 设计目标确认 ==="区段(§6.1)+ "已回写至..."一行
- **依据规范**:`skill-conventions.md §规则 1` + NFR-2 增量修改 + INV-1 frontmatter 不变

### 模块 2:`code-plan` 步骤 0b(对应概要设计 §3 D-4,§5.3)
- **路径**:`plugins/code-skills/skills/code-plan/SKILL.md`
- **关键类/函数**:
  - `readDesignGoalsFromDesign(designResultPath: string): DesignGoals | null` — 读 `design/.../RESULT.md` 的"## 设计目标"小节,存在则返回,不存在返回 `null`
  - `askDesignGoalsDegraded(needContext: NeedContext): DesignGoals` — 退化时触发 1-5 问(`code-plan` 退化版)
  - `writeDesignGoalsSection(resultMdPath: string, goals: DesignGoals, trigger: "code-plan"): void`
  - `adjustTaskGranularityByGoals(plan: Plan, goals: DesignGoals): Plan` — 任务粒度调整
- **关键调用顺序**:
  1. 步骤 0a 拉取(REQ-00005 既有)
  2. **步骤 0b 读 `design/.../RESULT.md`**:
     - 存在 → 屏幕打印"沿用 design 的设计目标:<摘要>" + 复制到 `plan/.../RESULT.md` 顶部
     - 不存在 → 屏幕打印"⚠ 未检测到 design/<REQ>/RESULT.md" + 触发 `AskUserQuestion` 1-5 问 + 写 `plan/.../RESULT.md`(不写 `design/`)
  3. **任务拆分时**调 `adjustTaskGranularityByGoals`(FR-4)
  4. 进入步骤 0(版本上下文检测)— 沿用既有
- **并发模型**:串行
- **资源管理**:无新资源
- **错误处理范式**:
  - 读 `design/.../RESULT.md` 失败 → 视同不存在,退化
  - 用户取消 → 中止
- **日志埋点**:屏显"=== code-plan 设计目标确认 ==="区段(§6.2 / §6.3)+ "已沿用/已回写"一行
- **依据规范**:NFR-5 与 `code-auto` 0 冲突 + FR-3 退化行为

### 模块 3:模板顶部预留位(对应概要设计 §3 D-8,§5.3)
- **路径**:
  - `plugins/code-skills/skills/code-design/templates/design.md`
  - `plugins/code-skills/skills/code-plan/templates/plan.md`
- **关键变更**:在"## 文档头"模板区段**后** + "## 1. ..."章节**前**插入占位注释
- **占位注释**:
  ```markdown
  ## 设计目标
  <!-- 本节由 code-design / code-plan 步骤 0b 自动生成(写入或沿用),记录用户确认的设计目标 -->
  ```
- **依据规范**:`module-conventions.md §规则 1` 资源放子目录(已在 `templates/`)

### 模块 4:`code-design` 步骤 0a 既有"不含步骤 0b"小注更新
- **路径**:`plugins/code-skills/skills/code-design/SKILL.md` §步骤 0a 既有"含步骤 0b"小注
- **原内容**(L107):"所有其他 `code-*` 技能的第一步都是这一步。位于既有"步骤 0"之前。`code-design` **不**含步骤 0b(FR-2 显式仅 `code-require` 专属)。"
- **更新后**(本需求引入 `code-design` 步骤 0b):
  - 保留第 1 句(所有 `code-*` 技能第一步)
  - 保留"位于既有"步骤 0"之前"
  - **删除**"code-design 不含步骤 0b(FR-2 显式仅 code-require 专属)"的整句小注
  - **替换**为:"步骤 0a 成功后,`code-design` 进入"步骤 0b 设计目标确认"(本需求新增,见 §步骤 0b 章节)"
  - **同步**:`code-plan/SKILL.md` §步骤 0a L118 同样的小注需删除并替换

## 5. 算法与逻辑

### 算法 1:askDesignGoals(`code-design` 步骤 0b 触发)
- **目的**:收集用户对"设计目标"的选择(整体 + 4 维度)
- **输入**:`needContext`(含需求规模评估字段,用于自适应问题数)
- **输出**:`DesignGoals` 对象
- **复杂度**:O(N),N ∈ {1, 3, 5}(问题数)
- **依赖**:`AskUserQuestion` 工具
- **伪代码**:
  ```
  function askDesignGoals(needContext):
      # 自适应问题数(Q-3 锁定)
      if needContext.size == "small":
          questions = [Q1_overall]                       # 1 问
      else if needContext.size == "medium":
          questions = [Q1_overall, Q2_func, Q3_ext]      # 3 问
      else: # large
          questions = [Q1_overall, Q2_func, Q3_ext, Q4_robust, Q5_maint]  # 5 问
      
      # 大需求可对不同细节功能分开提问(AC-6.3)
      if needContext.isLarge:
          # 按 needContext.subFeatures 拆分,每 subFeature 问 1 问
          for sub in needContext.subFeatures:
              questions.append(questionForSubFeature(sub))
      
      # 触发 1-N 个 AskUserQuestion(每个问题 1 个 AskUserQuestion 调用)
      answers = []
      for q in questions:
          answer = AskUserQuestion(q)    # 用户取消 → 中止 + 回写空
          answers.append(answer)
      
      return parseToDesignGoals(answers)
  ```
- **关键决策与权衡**:1 问 vs 多问(多问对齐"维度独立选择"原则,Q-3 锁定)
- **边界条件**:用户取消 → 写空"## 设计目标"小节 + 中止
- **对应任务**:T-001(写 `code-design/SKILL.md` 步骤 0b 段)

### 算法 2:writeDesignGoalsSection(回写"## 设计目标"小节)
- **目的**:在 `RESULT.md` 顶部"## 文档头"区段之后 + "## 1. ..."章节之前,插入或覆盖"## 设计目标"小节
- **输入**:`resultMdPath` / `goals: DesignGoals` / `trigger: "code-design" | "code-plan"`
- **输出**:无(直接写文件)
- **复杂度**:O(L),L = `RESULT.md` 总行数
- **伪代码**:
  ```
  function writeDesignGoalsSection(resultMdPath, goals, trigger):
      # 幂等性(NFR-3):先删除已有 "## 设计目标" 小节(若有)
      content = ReadFile(resultMdPath)
      content = removeExistingSection(content, "^## 设计目标$")
      
      # 构造新小节
      section = buildSection(goals, trigger)   # 见 §5.4 数据结构
      
      # 定位插入位置:在 "## 文档头" 模板区段后(以 "## 1. " 章节作为锚点)
      # 用 Read 找第一个 "^## 1\." 的位置,在它之前插入 section
      newContent = content.insertBefore("## 1.", section)
      
      WriteFile(resultMdPath, newContent)
  ```
- **关键决策与权衡**:幂等(覆盖) vs 追加 — 选定幂等(NFR-3)
- **边界条件**:
  - 文件不存在 → 失败(由 `code-design` / `code-plan` 步骤 2 创建工作目录保证存在)
  - "## 1. ..." 锚点不存在 → 退化为"追加到文件末尾"(理论上不会发生,因 RESULT.md 一定有 §1)
- **对应任务**:T-001 / T-002

### 算法 3:readDesignGoalsFromDesign(`code-plan` 步骤 0b 读取)
- **目的**:`code-plan` 从 `design/.../RESULT.md` 读"## 设计目标"小节;存在则返回,不存在返回 `null`
- **输入**:`designResultPath`
- **输出**:`DesignGoals | null`
- **复杂度**:O(L)
- **伪代码**:
  ```
  function readDesignGoalsFromDesign(designResultPath):
      if not FileExists(designResultPath):
          return null
      
      content = ReadFile(designResultPath)
      # 匹配 "## 设计目标" 章节(从该行到下一个 "## " 一级标题之前)
      match = RegexMatch(content, r"## 设计目标\n([\s\S]*?)\n## ")
      if not match:
          return null  # 存在但无该小节,视为 "无 design 输入"(E-5)
      
      sectionText = match[1]
      return parseSectionToDesignGoals(sectionText)
  ```
- **关键决策与权衡**:E-5 边界处理(存在文件但无小节 → 退化)
- **对应任务**:T-002

### 算法 4:adjustTaskGranularityByGoals(`code-plan` 任务粒度调整)
- **目的**:据"## 设计目标"小节调整 PLAN.md 任务总览的粒度
- **输入**:`plan: Plan` / `goals: DesignGoals`
- **输出**:调整后的 `plan`
- **复杂度**:O(T),T = 任务数
- **伪代码**:
  ```
  function adjustTaskGranularityByGoals(plan, goals):
      # D-5 判定表
      if goals.overall == "--extensible" or goals.extensibility == "高":
          # 加 "扩展架构设计" / "设计模式使用" 等扩展性任务
          extensibilityTasks = buildExtensibilityTasks(goals)
          plan.tasks.insert(position=0, extensibilityTasks)  # 插入到首位
          
          if goals.overall == "--extensible" and goals.extensibility == "高":
              # 至少 3 个扩展性相关任务
              assert len(extensibilityTasks) >= 3
      elif goals.overall == "--minimal":
          # 同类任务合并,粒度粗化
          plan.tasks = mergeSimilarTasks(plan.tasks)  # 启发式:相似 title 合并
      else:
          # "--balanced" + 扩展性 ∈ {中, 低} → 默认粒度
          pass
      return plan
  ```
- **关键决策与权衡**:粒度粗化的"合并"启发式可能误判 → 建议**轻度合并**(只合并明显同类的)
- **对应任务**:T-002

## 6. 数据结构完整变更

### 6.1 新增数据结构

#### DesignGoals(内存中传递,无持久化)
```ts
{
  writeTime: string,         // "YYYY-MM-DD HH:mm"
  writeTrigger: "code-design" | "code-plan"
  overallGoal: "--minimal" | "--extensible" | "--balanced"
  dimensionPriority: {
    functionality: "高" | "中" | "低"
    extensibility: "高" | "中" | "低"
    robustness: "高" | "中" | "低"
    maintainability: "高" | "中" | "低"
  }
}
```

### 6.2 修改文档结构

#### "## 设计目标"小节 Markdown 模板
- **位置**:`design/.../RESULT.md` 顶部(在"## 文档头"之后,"## 1. 设计概述"之前);`plan/.../RESULT.md` 同位置
- **模板**:
  ```markdown
  ## 设计目标

  > 本小节由 `code-design` / `code-plan` 步骤 0b 自动生成,记录用户确认的设计目标。

  - **回写时间**:2026-06-05 19:50
  - **回写触发**:code-design

  ### 整体设计目标
  `--balanced`

  ### 维度优先级

  | 维度 | 优先级 |
  | --- | --- |
  | 功能性 | 中 |
  | 扩展性 | 中 |
  | 健壮性 | 中 |
  | 可维护性 | 中 |
  ```

### 6.3 数据迁移
- **无**(本需求不涉及数据迁移)

## 7. 接口细节

### 7.1 接口总览

| 接口名 | 形式 | 状态 | 对应任务 | 依据规范 |
| --- | --- | --- | --- | --- |
| `askDesignGoals(needContext): DesignGoals` | `AskUserQuestion` | 新增 | T-001 | FR-6 |
| `writeDesignGoalsSection(...)` | `Read` + `Write` | 新增 | T-001 / T-002 | FR-5 / NFR-3 |
| `readDesignGoalsFromDesign(...)` | `Read` | 新增 | T-002 | FR-2 |
| `adjustTaskGranularityByGoals(...)` | (内部) | 新增 | T-002 | FR-4 |

### 7.2 关键决策
- **不引入对外 API**:本需求不新增任何对外契约
- **屏显模板**:`=== code-design 设计目标确认 ===` 区段(参考 REQ-00011 §6.1)
- **幂等性**:NFR-3 强约束(覆盖前次内容)
- **链路追踪**:**无**(本需求不涉及)

## 8. 异常处理

| 异常类别 | 触发条件 | 检测 | 处理 | 监控 | 对应任务 |
| --- | --- | --- | --- | --- | --- |
| 用户取消 | `code-design` 步骤 0b `AskUserQuestion` 取消 | 工具返回取消信号 | 中止 + 回写空"## 设计目标"小节 | stderr | T-001 |
| 文件不存在 | `code-plan` 步骤 0b 读 `design/.../RESULT.md` 不存在 | `FileExists` 检测 | 退化(D-4) | 屏幕打印"⚠ 未检测到..." | T-002 |
| 文件无小节 | `code-plan` 步骤 0b 读 `design/.../RESULT.md` 存在但无"## 设计目标"小节 | 正则匹配失败 | 退化(E-5) | 屏幕打印"⚠ 未检测到..." | T-002 |
| 写文件失败 | `Write` 工具失败 | 工具返回失败 | 透传 stderr,中断退出 | stderr | T-001 / T-002 |
| 锚点漂移 | `RESULT.md` 缺"## 1. ..."章节 | 正则匹配失败 | 退化为"追加到文件末尾" | stderr 告警 | T-001 / T-002 |

## 9. 安全要求

- **鉴权**:**无**(本技能由 Claude Code 内部调用,无对外鉴权)
- **输入校验**:`AskUserQuestion` 工具自带选项校验,无需额外校验
- **敏感数据处理**:`Write` 工具写入文件,**不**涉及敏感数据
- **防注入**:**无**(Markdown 内容,无 SQL/NoSQL/命令)
- **审计**:**无**(本技能不涉及审计)
- **依据规范**:**无特殊安全要求**

## 10. 状态机 / 流程

```
[code-design 步骤 0b 状态机]

[*] --> Idle
Idle --> AskUserQuestion: 触发 N 个问题(N ∈ {1, 3, 5})
AskUserQuestion --> UserAnswered: 用户回答
AskUserQuestion --> UserCancelled: 用户取消
UserAnswered --> WriteSection: 写 "## 设计目标" 小节
UserCancelled --> WriteEmptySection: 写空 "## 设计目标" 小节
WriteSection --> Done: 屏显"已回写至..."
WriteEmptySection --> Abort: 中止流程
Done --> [*]
Abort --> [*]
```

```
[code-plan 步骤 0b 状态机]

[*] --> CheckDesign
CheckDesign --> ReadExists: design/.../RESULT.md 存在
CheckDesign --> DegradedAsk: design/.../RESULT.md 不存在
ReadExists --> ReadSection: 读 "## 设计目标" 小节
ReadSection --> SectionExists: 小节存在
ReadSection --> DegradedAsk: 小节不存在(E-5)
SectionExists --> CopyToPlan: 复制到 plan/.../RESULT.md
CopyToPlan --> PrintInherit: 屏显"沿用 design 的设计目标"
DegradedAsk --> UserAnswered: 用户回答
DegradedAsk --> UserCancelled: 用户取消
UserAnswered --> WritePlanSection: 写 plan/.../RESULT.md
UserCancelled --> Abort: 中止流程
PrintInherit --> Done
WritePlanSection --> PrintWrite: 屏显"已回写至..."
Done --> [*]
PrintWrite --> [*]
Abort --> [*]
```

## 11. 性能与资源

- **关键路径耗时目标**:`AskUserQuestion` 1-5 次 ≤ 5 分钟(用户感知;NFR-8)
- **并发上限**:**无**(单技能串行)
- **资源限制**:**无**(纯 Markdown 文本操作)
- **缓存策略**:**无**
- **批量/异步**:**无**
- **降级策略**:**无**

## 12. 测试要点

- **单元测试**:**不适用**(本项目无构建/测试框架,纯 Markdown 技能;沿用 REQ-00009 `code-unit` 守卫"不可测"判定 → 任务测试状态=`不适用`)
- **集成测试**:**无**
- **端到端测试**:**无**
- **性能/压力测试**:**无**
- **安全测试**:**无**
- **回归测试**:NFR-5 验证 `code-auto` 调 `code-design` / `code-plan` 时,`AskUserQuestion` 触发后选"推荐项",**不**中断

> **关键决策**:本项目所有 12 个 `code-*` 技能任务的测试状态沿用 V0.0.2 既有实践 = `不适用`(纯 Markdown 技能),本需求 2 任务同样 = `不适用`。

## 13. 关联编码计划

- `PLAN.md` 中本详细设计对应的所有任务编号:
  - `TASK-REQ-00011-00001`(`[修改] code-design/SKILL.md 增量追加"步骤 0b 设计目标确认"`+ 模板顶部预留)
  - `TASK-REQ-00011-00002`(`[修改] code-plan/SKILL.md 增量追加"步骤 0b 设计目标确认"+ 任务粒度调整段`+ 模板顶部预留)
- 关键任务与本节设计的对应关系:
  - T-001 → §5 算法 1 / 算法 2 + §4 模块 1 / 模块 3 / 模块 4
  - T-002 → §5 算法 2 / 算法 3 / 算法 4 + §4 模块 2 / 模块 3 / 模块 4

## 14. 待澄清 / 未决项

| 编号 | 问题 | 影响范围 | 阻塞方 | 期望回复时间 |
| --- | --- | --- | --- | --- |
| Q-1 | `code-design` 步骤 0b 是否对所有需求都触发 5 问? | §5 算法 1 | 用户 | 后续调 `code-design` 时观察 |
| Q-2 | `code-plan` 步骤 0b 退化时,`AskUserQuestion` 1 问还是 5 问? | §5 算法 3 | 用户 | 后续调 `code-plan` 时观察 |
| Q-3 | `code-review` 是否应感知"## 设计目标"小节(在评审清单中加 1 项)? | §10 状态机 | 用户 | 后续版本(本需求**不**触发) |

## 15. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-05 | v1 | 初始创建 | 完成首次详细设计,对应 PLAN.md v1 的 2 条任务(T-001 / T-002);覆盖 4 算法(askDesignGoals / writeDesignGoalsSection / readDesignGoalsFromDesign / adjustTaskGranularityByGoals);2 状态机(`code-design` / `code-plan` 步骤 0b);0 新增依赖;0 触发 `dashboard-conventions §规则 1` | wangmiao |
