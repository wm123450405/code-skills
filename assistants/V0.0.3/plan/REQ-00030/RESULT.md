# REQ-00030 — 优化 /code-design 与 /code-plan 职责分离(详细设计)

- 需求编码:REQ-00030
- 所属版本:V0.0.3
- 上游需求:./assistants/V0.0.3/require/REQ-00030/RESULT.md
- 上游概要设计:./assistants/V0.0.3/design/REQ-00030/RESULT.md
- 遵循规范:./assistants/rules/ 下 7 个文件(已逐条对照,无冲突)
- 详细设计状态:已完成
- 创建:2026-06-12
- 最近更新:2026-06-12 14:31

## 设计目标

> 沿用 `code-design` 步骤 0b 写入的"## 设计目标"小节 — `--extensible` 整体 + 功能性=高

| 维度 | 优先级 |
| --- | --- |
| 整体设计目标 | `--extensible` |
| 功能性 | 高 |
| 扩展性 | 高(用户主动选 → 触发 FR-8 三阶段下沉) |
| 健壮性 | 中 |
| 可维护性 | 中 |
| 封装性 | 不适用(本仓库 Markdown 自然语言技能) |
| 可复用性 | 不适用(本仓库 Markdown 自然语言技能) |
| 可读性 | 不适用(本仓库 Markdown 自然语言技能) |

**说明**:本需求为元技能改动,扩展性=高(用户主动选 `--extensible`)→ 触发架构骨架判定逻辑(FR-6 条件 5)+ 扩展性设计章节(FR-8 阶段 2 详设);功能性=高(用户原文:"**严格切分**概设/详设职责")。

## 1. 详细设计概述

本详细设计把 `code-design` §3.1~§3.8 8 个关键设计点落地为**5 个被改文件的具体修改内容 + 6 个可独立执行的任务**。核心是把"职责分离"从概念性表述转为**可验证的字节级变更**:5 个文件每个都有明确的"修改前后 diff 摘要",且**每条 INV(1~9)都对应一个具体的字节级保留锚点**。

**关键决策**:
- **任务拆分原则**:按"5 个被改文件各 1 任务" + 1 个验证任务(行数收敛观测)= **6 任务**
- **架构骨架任务**(--extensible 触发):**不**单独拆 1 个任务(因本需求**不**写新代码,而是改元技能定义),"扩展点预留"作为 T-001 的子项体现
- **测试状态**:全部任务为"纯文档改造",测试状态=`不适用`(NFR-7 严守工具集不变,无新代码 / 无新依赖)

**对应的任务计划**:PLAN.md 共 6 任务(T-001 ~ T-006)。

## 2. 上游引用

- **需求**:`./assistants/V0.0.3/require/REQ-00030/RESULT.md`(8 FR / 6 NFR / 9 AC)
- **概要设计**:`./assistants/V0.0.3/design/REQ-00030/RESULT.md`(17 章节 / 8 关键设计点 / 9 INV)
- **规范**:`./assistants/rules/` 下被引用的 7 个文件(沿用概设 `design/REQ-00030/rule-compliance.md` §1)

## 3. 规范遵循

(沿用 `code-design` §2.5 + `plan/REQ-00030/rule-compliance.md` §1-5)

- **完全合规**的章节:§1-§15 全部
- **经用户授权偏离**:无
- **待澄清冲突**:无

## 4. 模块详细化(对应概要设计 §7)

> 完整模块详细化见 `module-details.md`(5 个被改模块的"关键子节 / 调用顺序 / 状态归属 / 错误处理 / 资源管理 / 与概要设计对应 / 符合的规范")。

**本节是 RESULT.md 概览**:

| 模块 | 关键子节 / 关键变更 | 详见 |
| --- | --- | --- |
| `code-design` 步骤定义 | 步骤 0b 收敛 + 步骤 9A/10A/11A 收窄 | `module-details.md` §模块 1 |
| `code-design` 模板 | §7/§8/§9/§10 重写 + §7.5/§8.5/§9.5 新增 + 顶部注释 | `module-details.md` §模块 2 |
| `code-plan` 步骤定义 | 步骤 7A 补做强约束 + 步骤 10A 架构骨架触发收紧 | `module-details.md` §模块 3 |
| `code-plan` 模板 | §4-§10 由"建议"改"必填" | `module-details.md` §模块 4 |
| `code-check` 步骤定义 | 评审清单追加 3 个校验点 | `module-details.md` §模块 5 |

**调用顺序**(本需求全景):
```
code-require → code-design → code-plan → code-it → code-check
                                              ↓
                                            派生任务(若有)
```

## 5. 算法与逻辑(本节是详细设计区别于概要设计的核心)

### 算法 1:步骤 0b 自适应问路判定

- **目的**:根据需求规模 + 扩展性触发条件,决定 0 / 1 / 2 问
- **输入**:
  - `req: ReqSummary` —— 需求摘要(taskCount / isSmall / pendingThirdPartyDeps / predictedModuleCount / frText)
  - `codeAutoCtx: boolean` —— 是否在 code-auto 上下文
- **输出**:`{ count: 0 | 1 | 2, reason: string, defaultGoal: '--minimal' | '--extensible' | '--balanced' | null }`
- **复杂度**:时间 O(1) / 空间 O(1)
- **依赖**:无(纯函数)
- **伪代码**:

```ts
function adjustAskUserQuestionCount(req: ReqSummary, codeAutoCtx: boolean): AdjustResult {
  // code-auto 上下文永远 0 问
  if (codeAutoCtx) {
    return { count: 0, reason: 'code-auto 上下文,0 问默认 --balanced', defaultGoal: '--balanced' }
  }

  // FR-1 判定:是否触发扩展性
  const triggersExtensibility = (
    req.pendingThirdPartyDeps.length > 0
    || req.predictedModuleCount >= 3
    || /\b(多实现|抽象层|可替换|多套实现)\b/.test(req.frText)
  )

  // FR-2 收紧:小需求 0 问
  if (req.taskCount <= 1 && req.isSmall() && !triggersExtensibility) {
    return { count: 0, reason: '小需求 + 不触发扩展性,0 问默认 --balanced', defaultGoal: '--balanced' }
  }

  // 大需求 2 问
  if (req.taskCount >= 6 || req.needsArchitectureSkeleton()) {
    return { count: 2, reason: '大需求,2 问(整体 + 功能性)', defaultGoal: null }
  }

  // 中等需求 / 触发扩展性 → 1 问
  return { count: 1, reason: '中等需求 / 触发扩展性,1 问(只问整体)', defaultGoal: null }
}
```

- **关键决策与权衡**:
  - 优先检查 `codeAutoCtx`(早返回,避免后续逻辑污染)
  - 字符串正则 `\b(多实现|抽象层|可替换|多套实现)\b` 沿用既有"关键词匹配"模式(轻量级)
  - `req.isSmall()` 调用而非 `req.taskCount <= 1` 直接判断:为"小需求"语义保留扩展点(未来若小需求判定标准变化,只改 `isSmall()` 实现)
- **边界条件**:
  - `req.taskCount = 0`(异常):按"小需求 0 问"处理,屏显警告 `⚠ 任务数 = 0`
  - `codeAutoCtx` 文件读取失败:屏显 `⚠` 警告,降级为"按用户手动调子技能处理",**不**默认 0 问
- **对应任务**:T-001
- **依据规范**:`skill-conventions §规则 1`

### 算法 2:code-check 校验点 1 — 详设完整性

- **目的**:校验 `plan/<REQ>/PLAN.md` 中每条任务的"涉及文件"在 `plan/<REQ>/RESULT.md §4-§10` 找对应章节
- **输入**:
  - `planResultPath: string` —— `plan/<REQ>/RESULT.md` 路径
  - `planPath: string` —— `plan/<REQ>/PLAN.md` 路径
- **输出**:`{ passed: boolean, missing: Array<{ taskId, reason }> }`
- **复杂度**:时间 O(N × M)(N 任务数 × M 章节数)/ 空间 O(N)
- **依赖**:无
- **伪代码**:

```ts
function validatePlanIntegrity(planResultPath: string, planPath: string): ValidationResult {
  const planResult = readFile(planResultPath)
  const plan = readFile(planPath)

  // 解析 plan/PLAN.md 任务总览表格
  const tasks = parseTaskOverview(plan)  // 既有函数

  // 解析 plan/RESULT.md §4-§10 章节,提取所有"涉及文件"路径
  const referencedFiles = new Set<string>()
  for (const chapter of ['§4', '§5', '§6', '§7', '§8', '§9', '§10']) {
    const content = extractChapter(planResult, chapter)
    for (const filePath of extractFilePaths(content)) {
      referencedFiles.add(filePath)
    }
  }

  // 校验每条任务的"涉及文件"是否在 referencedFiles 中
  const missing: Missing[] = []
  for (const task of tasks) {
    for (const filePath of task.involvedFiles) {
      if (!referencedFiles.has(filePath)) {
        missing.push({
          taskId: task.id,
          reason: `涉及文件 ${filePath} 未在 §4-§10 任何章节引用`,
        })
      }
    }
  }

  return { passed: missing.length === 0, missing }
}
```

- **关键决策与权衡**:
  - 用 `Set` 加速查表(避免 N × M 退化为 O(N × M) 而非 O(N + M))
  - `extractChapter` 沿用既有解析函数(本设计**不**新增章节解析逻辑)
- **边界条件**:
  - 任务"涉及文件"为空(尚未填写):跳过该任务(由 `code-it` 完成后回填,本校验不阻断)
  - `§4-§10` 章节缺失:视为"该章节无引用",触发所有引用该章节的"涉及文件"任务 → 派生"详设缺失"
- **对应任务**:T-005
- **依据规范**:`commit-conventions`

### 算法 3:code-check 校验点 2 — 概设越界检测

- **目的**:校验 `design/<REQ>/RESULT.md §7/§8/§9` 不出现"完整字段类型 / 完整错误码 / 完整约束 / 完整索引"等详设深度内容
- **输入**:`designResultPath: string`
- **输出**:`{ passed: boolean, violations: Array<{ chapter, matchText, pattern }> }`
- **复杂度**:时间 O(N × P)(N 章节行数 × P 正则数)/ 空间 O(V)(V 违规数)
- **依赖**:无
- **伪代码**:

```ts
const DETAIL_PATTERNS: RegExp[] = [
  /\|\s*\w+\s*\|\s*(string|number|integer|boolean|datetime|UUID)\s*\|/,  // 表格行含类型
  /\b(错误码|error[_ ]?code)\s*[:=]?\s*\d{4,}/,                            // "错误码: 40001"
  /\b(鉴权|auth|authentication)\s*[:=]/,                                  // "鉴权:"
  /\b(索引|index)\s*[:=]?\s*\w+\s*\(/,                                    // "索引: <name>("
  /\b(迁移脚本|migration)\s*[:=]/,                                         // "迁移脚本:"
]

function validateDesignBoundary(designResultPath: string): ValidationResult {
  const design = readFile(designResultPath)
  const violations: Violation[] = []

  for (const chapter of ['§7', '§8', '§9']) {
    const content = extractChapter(design, chapter)
    for (const pattern of DETAIL_PATTERNS) {
      const matches = content.matchAll(new RegExp(pattern, 'gm'))
      for (const match of matches) {
        violations.push({
          chapter,
          matchText: match[0].slice(0, 100),  // 截断至 100 字符
          pattern: pattern.source,
        })
      }
    }
  }

  return { passed: violations.length === 0, violations }
}
```

- **关键决策与权衡**:
  - 5 个正则覆盖"表格行含类型 / 错误码 / 鉴权 / 索引 / 迁移脚本"5 类典型越界模式
  - 截断 `matchText` 至 100 字符(避免屏显过长)
- **边界条件**:
  - `§7/§8/§9` 章节缺失(异常):视为"无内容",`passed: true`
  - 章节内容含正则误匹配(如代码示例含 "error_code: 500"):按"误判"处理,**不**阻断;`code-check` 评审人员可手动忽略
- **对应任务**:T-005
- **依据规范**:`commit-conventions`

### 算法 4:code-check 校验点 3 — 行数比例警告

- **目的**:校验 `design < plan × 1.2`(FR-7 锁定阈值)
- **输入**:`designResultPath: string, planResultPath: string`
- **输出**:`{ passed: boolean, ratio: number, warning: string | null }`
- **复杂度**:时间 O(1) / 空间 O(1)
- **依赖**:无
- **伪代码**:

```ts
const WARNING_THRESHOLD = 1.2  // FR-7 锁定

function validateLineRatio(designResultPath: string, planResultPath: string): ValidationResult {
  const designLines = readFile(designResultPath).split('\n').length
  const planLines = readFile(planResultPath).split('\n').length
  const ratio = designLines / planLines

  if (ratio > WARNING_THRESHOLD) {
    return {
      passed: true,  // 不阻断
      ratio,
      warning: `⚠ 概设/详设行数比例异常(${ratio.toFixed(2)}),建议复核概设是否过深`,
    }
  }

  return { passed: true, ratio, warning: null }
}
```

- **关键决策与权衡**:
  - 阈值 1.2 来自 FR-7
  - **不**阻断 `code-check`(沿用既有:警告而非错误)
- **边界条件**:
  - `planLines = 0`(异常):视为"详设为空",`ratio = Infinity`,**不**警告(避免除零)
  - 既有 9 个 REQ 的 design / plan 比例异常:**不**触发警告(本校验**仅**作用于新 REQ)
- **对应任务**:T-005
- **依据规范**:`commit-conventions`

## 6. 数据结构完整变更(对应概要设计 §9)

> 完整变更见 `data-changes.md`(4 个实体的字段变更 / 索引 / 迁移 / 兼容策略)。

**本节是 RESULT.md 概览**:

| 实体 | 状态 | 关键变更 |
| --- | --- | --- |
| `check-validation-point` | 新增 | 3 个校验点的"id / name / trigger / action / taskType / triggerSource / relatedTask / warningThreshold" |
| `design-template-chapter` | 修改 | §7.1(7→5 列) / §7.2(7→5 列) / §7.5(新增) / §8(6→4 列) / §8.5(新增) / §9(6→4 列) / §9.5(新增) / §10(7→4 列) / 顶部注释(+1 行) |
| `plan-process-doc-status` | 修改 | 4 份过程文档"可选"→"必选" |
| `plan-template-chapter-required-flag` | 新增 | §4-§12 9 个章节的"required / minContent / fallbackText" |

详见 `data-changes.md`。

## 7. 接口细节(对应概要设计 §8)

> 完整 schema 见 `interface-specs.md`(6 个内部函数的入参 / 出参 / 错误码 / 示例 / 版本 / 兼容)。

**本节是 RESULT.md 概览**:

| 接口名 | 形式 | 状态 | 对应任务 |
| --- | --- | --- | --- |
| `code-design` 步骤 0b 判定入口 | 函数 | 修改既有 | T-001 |
| `code-design` 步骤 9A 模块表生成 | 函数 | 修改既有 | T-001 |
| `code-design` 步骤 10A 接口概要生成 | 函数 | 修改既有 | T-001 |
| `code-plan` 步骤 7A 补做入口 | 函数 | 修改既有 | T-003 |
| `code-plan` 步骤 10A 架构骨架判定 | 函数 | 修改既有 | T-003 |
| `code-check` 校验点 1(详设完整性) | 函数 | 新增 | T-005 |
| `code-check` 校验点 2(概设越界) | 函数 | 新增 | T-005 |
| `code-check` 校验点 3(行数比例) | 函数 | 新增 | T-005 |

## 8. 异常处理

按异常类别组织:

- **输入校验**:`code-check` 校验点 1 / 2 派生"重构"类型任务
- **外部依赖**:**不适用**(本仓库无外部依赖)
- **并发冲突**:**不适用**(本仓库串行执行)
- **资源耗尽**:**不适用**(本仓库无资源)
- **业务异常**:模板字段缺失 → `code-design` 步骤 8A 询问用户
- **未知异常**:`code-check` 评审人员可手动忽略派生任务

详见 `risk-analysis.md §异常处理`。

## 9. 安全要求

- **鉴权**:**不适用**(本仓库无 API / 无鉴权)
- **授权**:**不适用**
- **输入校验**:`code-check` 校验点 1 / 2 兜底
- **敏感数据处理**:**不适用**
- **防注入**:**不适用**
- **审计**:沿用既有 `commit-conventions` 提交审计

## 10. 状态机 / 流程

本需求是**元技能改动**,无传统状态机。流程图见 `module-details.md §6`。

## 11. 性能与资源

- **关键路径耗时**:**不适用**(本仓库无性能目标)
- **并发上限**:每个 `code-*` 技能串行
- **资源限制**:**不适用**
- **缓存策略**:**不适用**
- **批量/异步**:**不适用**
- **降级策略**:`code-check` 校验点 3(行数比例)即使 ratio > 1.2 也**不**阻断,**仅**标黄警告

## 12. 测试要点

(详见 `risk-analysis.md §测试要点`)

本仓库**不**含测试框架,故"测试"主要是**人工评审 + git diff 验证**。13 项人工评审清单已列在 `risk-analysis.md`。

## 13. 关联编码计划

- `PLAN.md` 中本详细设计对应的所有任务编号:
  - `TASK-REQ-00030-00001`:`code-design/SKILL.md` 修改(步骤 0b + 9A/10A/11A)
  - `TASK-REQ-00030-00002`:`templates/design.md` 修改(§7/§8/§9/§10 重写)
  - `TASK-REQ-00030-00003`:`code-plan/SKILL.md` 修改(7A + 10A)
  - `TASK-REQ-00030-00004`:`templates/plan.md` 修改(§4-§10 必填)
  - `TASK-REQ-00030-00005`:`code-check/SKILL.md` 修改(3 校验点)
  - `TASK-REQ-00030-00006`:行数收敛观测(纯验证类)

## 14. 待澄清 / 未决项

| 编号 | 问题 | 影响范围 | 阻塞方 | 期望回复时间 |
| --- | --- | --- | --- | --- |
| Q-1 | 行数收敛指标"≥ 30%"是否过严? | AC-8.1 / AC-8.2 | 无 | (沿用上游澄清 Q-1) |
| Q-2 | `code-check` 3 校验点是否作为 V0.0.4 才引入? | FR-7 / AC-6 | 无 | (沿用上游澄清 Q-2) |
| Q-3 | 若未来"概设合理但详设漏做"需求出现,是否新增"补做详设"独立技能? | 未来 | 无 | (沿用上游澄清 Q-3) |
| Q-4 | 任务粒度按"文件"还是"功能点"? | §5 任务拆分 | 无 | (本轮澄清 Q-7 选 C — 沿用 REQ-00014 原则) |

## 15. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-12 14:31 | v1 | 初始创建 | 详细设计完成;6 任务(T-001 ~ T-006)对应 5 个被改文件 + 1 个验证任务;4 算法伪代码(问路判定 / 详设完整性 / 概设越界 / 行数比例);4 实体变更(2 新增 + 2 修改);0 新增三方依赖;0 触发看板字段三方同步 | 用户 |
