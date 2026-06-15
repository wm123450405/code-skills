# 设计目标

> 本节由 `code-plan` 步骤 0b 自动生成(从 `design/REQ-00035/RESULT.md` 顶部"## 设计目标"小节读取并沿用)

- 整体设计目标:`--balanced`
- 功能性:中
- 扩展性:不触发
- 健壮性:中
- 可维护性:中
- 封装性:不适用
- 可复用性:不适用
- 可读性:不适用
- code-auto 上下文:0 问路
- 任务粒度调整:无(--balanced 默认粒度)

---

# REQ-00035 — 详细设计

- 需求编码:REQ-00035
- 所属版本:V0.0.3
- 上游需求:./assistants/V0.0.3/require/REQ-00035/RESULT.md (v1)
- 上游概要设计:./assistants/V0.0.3/design/REQ-00035/RESULT.md (v1)
- 遵循规范:./assistants/rules/{encoding-conventions,dashboard-conventions,skill-conventions,module-conventions,doc-conventions,marketplace-protocol,migration-mapping}.md
- 状态:已完成
- 创建:2026-06-15
- 最近更新:2026-06-15

## 1. 详细设计概述

本详细设计将概要设计的 7 个改写点(M1-M3 模块)细化为 7 个独立可执行的任务,每个任务的"涉及文件"和"关键变更"明确到结构化语义锚点。

核心要点:
- **7 个改写任务**(T-001 ~ T-007),每个任务对应 1 个实际产出(改 1 个 SKILL.md / 改 1 个 dashboard)
- **5 个模板新增任务**(T-008 ~ T-012,作为 T-001~T-005 的子步骤,合并到主任务中)— 因"5 模板新增"与"5 主流程技能改写"在同一文件家族,合并拆分为 1 个大任务更合理
- **0 个新增接口**(NFR-3 强约束)
- **0 个数据结构变更**(本需求为 markdown 文本改写)

## 2. 上游引用

- **需求**:./assistants/V0.0.3/require/REQ-00035/RESULT.md 关键摘录
  - FR-1:过程文档"不涉及"判定准则建立
  - FR-2:新增 `process-doc-decisions.md` 决策记录文件
  - FR-3:过程文档自适应规则纳入 SKILL.md
  - FR-4:模板改造:`process-doc-decisions.md` 模板新增
  - FR-5:`code-auto` 编排同步改造
  - FR-6:`code-dashboard` 解析兼容
  - FR-7:看板 `RESULT.md`"变更记录"自适应
  - FR-8:过程文档不生成时 SKILL.md 步骤跳过
- **概要设计**:
  - M1 模块:5 个主流程技能(§4.模块拆分)
  - M2 模块:`code-auto` 编排(§4)
  - M3 模块:`code-dashboard` 看板(§4)
  - M4 模块:5 个模板新增(§4)
- **规范**:本设计引用 7 个项目级规范(详见 `rule-compliance.md`)

## 3. 规范遵循

详见 `rule-compliance.md`(本设计 §3 仅列关键约束):
- `skill-conventions.md`:**强约束** — 锚点(不修改 frontmatter / 不修改既有章节)
- `dashboard-conventions.md`:**强约束** — 不扩展字段(NFR-7)
- `module-conventions.md`:**不触发** — 本需求不改模块边界

## 4. 模块详细化

详见 `module-details.md`(本设计 §4 仅列模块路径/关键类/对应任务)。

| 模块 | 路径 | 关键变更锚点 | 对应任务 |
| --- | --- | --- | --- |
| M1.code-require | `plugins/code-skills/skills/code-require/SKILL.md` | 步骤 0(版本检测)之后 + "## 工作流程" 之前,新增小节"## 过程文档自适应判定" | T-001 |
| M1.code-design | `plugins/code-skills/skills/code-design/SKILL.md` | 同上锚点 | T-002 |
| M1.code-plan | `plugins/code-skills/skills/code-plan/SKILL.md` | 同上锚点 | T-003 |
| M1.code-it | `plugins/code-skills/skills/code-it/SKILL.md` | 同上锚点 | T-004 |
| M1.code-check | `plugins/code-skills/skills/code-check/SKILL.md` | 步骤 8(逐任务评审)末尾 + 既有维度 8.12 之后,新增 8.13 过程文档适配性 | T-005 |
| M2.code-auto | `plugins/code-skills/skills/code-auto/SKILL.md` | "## 子技能调用表" 备注列加 1 行(不破坏表格结构) | T-006 |
| M3.code-dashboard | `plugins/code-skills/skills/code-dashboard/SKILL.md` | "## 解析锚点" 小节末尾加 1 条"变更记录行数自适应"说明 | T-007 |
| M4.模板新增 × 5 | `plugins/code-skills/skills/<5 技能>/templates/process-doc-decisions.md` | 新文件(Write) | T-001~T-005 内联 |

## 5. 算法与逻辑(关键决策的伪代码)

### 5.1 过程文档自适应判定算法

```
# 输入:本技能读取的全部上游内容(已在内存)
# 输出:每类过程文档的"生成" / "不生成"决策列表

function decideProcessDocs(skill: string, upstream: object): Decision[] {
  decisions = []
  for each processDocType in processDocTypeRegistry[skill]:
    if processDocType.alwaysGenerated === true:
      decisions.append({type, decision: '生成', reason: '始终生成'})
    else if evaluateCriterion(processDocType.criterion, upstream):
      decisions.append({type, decision: '生成', reason: criterionName})
    else:
      decisions.append({type, decision: '不生成', reason: criterionName})
  return decisions
}

function evaluateCriterion(criterion: string, upstream: object): boolean {
  switch criterion:
    case 'hasUserClarification': return upstream.clarifications.length > 0
    case 'hasRelatedRequirements': return upstream.requirementsRelated.length >= 1
    case 'moduleCount>=2': return upstream.modules.length >= 2
    case 'hasExternalDependency': return upstream.externalDeps.length >= 1
    case 'hasInterfaceSpec': return upstream.interfaces.length >= 2
    case 'hasDataChanges': return upstream.dataChanges.length > 0
    case 'taskCount>=3': return upstream.tasks.length >= 3
    case 'hasRulesFiles': return upstream.rulesFiles.length > 0
    case 'hasMinorFindings': return upstream.findings.length > 0
    case 'testStatusInapplicable': return upstream.testStatus === '不适用'
    case 'taskInvolvesRuntime': return upstream.taskInvolvesRuntime === true
    case 'investigationPhase': return upstream.fixStatus === '调查中'
    default: return true  # 倾向生成(E-2 边界)
}
```

### 5.2 决策记录文件写入算法

```
function writeDecisionsFile(path, decisions) {
  if decisions.filter(d => d.decision === '不生成').length === 0:
    return  # 不写决策记录文件(D-2 选定 A)
  content = renderDecisionsFile(decisions)
  Write(path, content)
}
```

### 5.3 看板变更记录不追加判定

```
function shouldAppendChangeLog(skill, dirty) {
  return dirty.length > 0  # 仅当有变更才追加(NFR-7)
}
```

## 6. 数据结构完整变更(本设计 0 触发)

- **不**新增实体(NFR-8 强约束,不修改既有模板)
- **不**修改既有字段
- **不**触发数据迁移

## 7. 接口细节(本设计 0 触发)

- **不**新增外部接口(NFR-3 强约束)
- **不**修改既有 CLI 参数
- **不**触发 `AskUserQuestion` 新增

## 8. 异常处理

| 异常路径 | 处理策略 | 监控指标 |
| --- | --- | --- |
| AI 过度"不生成" | NFR-1 零空白文件校验(每个 `code-check` 8.13 评审派生"建议改"任务) | "建议改"任务数 |
| `process-doc-decisions.md` 写入失败 | 屏显警告,不阻断(沿用 E-1 边界) | 写入失败计数 |
| 看板变更记录 0 追加但实际有变更 | 步骤 N 末尾兜底检查(NFR-4 强约束) | "无变更却追加"计数 |
| 历史需求重跑 | NFR-5 字节级保留(子技能不感知) | "历史需求被改"计数 |

## 9. 安全要求

- **不**触发(本需求不涉及运行时安全边界,纯元技能改)

## 10. 状态机 / 流程

每个主流程技能的状态机在原 SKILL.md 步骤上**追加** 1 个新步骤(0a / 0a.5),不修改既有状态机:

```
原有流程:
  步骤 0(版本检测) → 步骤 1 → 步骤 2 → ... → 步骤 N(末尾提交)

新流程:
  步骤 0(版本检测) → 步骤 0a(过程文档判定,新增) → 步骤 1 → ... → 步骤 N(末尾提交)
```

## 11. 性能与资源

- **不**触发(本需求不涉及运行时性能)
- 静态分析:7 个 SKILL.md 各加 ~30 行(共 ~210 行)+ 5 模板各 ~50 行(共 ~250 行)+ 2 SKILL.md 改写 ~10 行(共 ~20 行)= **~480 行新增**

## 12. 测试要点

- 静态测试:本需求**不**触发单元测试(沿用 REQ-00031 范式,纯元技能改)
- 评审测试:`code-check` 8.13 评审维度校验 NFR-1(零空白文件)+ §6 判定准则合理性
- 端到端测试:对 REQ-00035 本身走完整 `code-auto` 流程(本轮正在执行)
- 后续回归:对 V0.0.3 既有 15 个需求(REQ-00020~REQ-00034),`code-check` 评审时**不**触发 8.13(NFR-5 字节级保留)

## 13. 关联需求

详见 `design/REQ-00035/related-designs.md`(本设计沿用 5 个关联设计):
- REQ-00020 / REQ-00030 / REQ-00031 / REQ-00032 / REQ-00034

## 14. 待澄清 / 未决项

- 无(本设计无显著未决项)

## 15. 变更记录

| 时间 | 事件 | 摘要 |
| --- | --- | --- |
| 2026-06-15 19:15 | 详细设计完成 | REQ-00035 详细设计完成(7 任务 / 0 接口 / 0 数据结构 / 0 依赖) |
