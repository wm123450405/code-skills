# 接口详细规格 — REQ-00030

更新时间:2026-06-12 14:31
版本:V0.0.3

> **本节是 `code-plan` 详设阶段产出**——把 `code-design` §8 4 项接口概要**详细化**为完整 schema(入参/出参/错误码/示例/版本策略/鉴权)。

## 接口 1:`code-design` 步骤 0b 判定入口(内部函数)

### 形式

- 内部函数(沿用既有 `writeDesignGoalsSection` 模式)

### 签名

```ts
function adjustAskUserQuestionCount(
  req: ReqSummary,           // 需求摘要(从 require/<REQ>/RESULT.md 解析)
  codeAutoCtx: boolean      // 是否在 code-auto 上下文中
): number                   // 返回 0 / 1 / 2(问路数量)
```

### 入参

```typescript
{
  req: {
    taskCount: number,                 // 任务总数(从 plan/PLAN.md 反推,本设计**不**直接读 PLAN.md)
    isSmall: (req: this) => boolean,   // 1 任务 ≤ 0.5-2 天
    pendingThirdPartyDeps: string[],   // 待评估三方依赖清单
    predictedModuleCount: number,      // 预评估涉及模块数
    frText: string                     // 上游需求 FR 文本
  },
  codeAutoCtx: boolean
}
```

### 出参

```typescript
{
  count: 0 | 1 | 2,                     // 问路数量
  reason: string,                      // 屏显文案(供日志)
  defaultGoal: '--minimal' | '--extensible' | '--balanced'  // 0 问时的默认值
}
```

### 错误码

- **不适用**(内部函数,无对外错误码)

### 示例

```json
// 示例 1:小需求 + 不触发扩展性
{
  "req": { "taskCount": 1, "isSmall": true, "pendingThirdPartyDeps": [], "predictedModuleCount": 1, "frText": "新增 code-answer 技能" },
  "codeAutoCtx": false
}
// → { "count": 0, "reason": "小需求 + 不触发扩展性,0 问默认 --balanced", "defaultGoal": "--balanced" }

// 示例 2:大需求
{
  "req": { "taskCount": 6, "isSmall": false, ... },
  "codeAutoCtx": false
}
// → { "count": 2, "reason": "大需求,2 问(整体 + 功能性)", "defaultGoal": null }

// 示例 3:code-auto 上下文
{
  "req": { ... },
  "codeAutoCtx": true
}
// → { "count": 0, "reason": "code-auto 上下文,0 问默认 --balanced", "defaultGoal": "--balanced" }
```

### 版本策略

- 沿用既有:**不**新增函数,仅在既有 `writeDesignGoalsSection` 调用前**追加**判定逻辑
- 函数**不**导出到 `module.exports`,仅在 `code-design/SKILL.md` 步骤 0b 内调用

### 兼容策略

- 既有 `writeDesignGoalsSection` 的**入参/出参**不变化,故**不**影响下游 `code-plan` 的 `readDesignGoalsFromDesign`
- `code-plan` 步骤 0b 沿用既有 7 维度问路,**不**受本修订影响

### 依据规范

- `skill-conventions §规则 1`
- `encoding-conventions §规则 1/3`(任务编号正则)

## 接口 2:`code-design` 步骤 9A 模块表生成(内部函数)

### 形式

- 内部函数(沿用既有"模块表生成"模式)

### 签名

```ts
function buildModuleBreakdownTable(modules: ModuleSummary[]): string  // 返回 markdown 表格字符串
```

### 入参

```typescript
{
  modules: Array<{
    name: string,        // 模块名
    path: string,        // 路径
    status: '新增' | '复用既有' | '修改既有',
    responsibility: string,  // 一句话职责
    dependency: string       // 依赖(对内其他模块 / 对外三方)
  }>
}
```

### 出参

```markdown
| 模块名 | 路径 | 状态(新增/复用既有/修改既有) | 职责 | 依赖 |
| --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... |
```

### 错误码

- **不适用**

### 示例

```json
// 示例 5 模块
{
  "modules": [
    { "name": "code-design 步骤定义", "path": "plugins/code-skills/skills/code-design/SKILL.md", "status": "修改既有", "responsibility": "步骤 0b 收敛 + 步骤 9A/10A/11A 输出深度收窄", "dependency": "无" },
    { "name": "code-design 模板", "path": "plugins/code-skills/skills/code-design/templates/design.md", "status": "修改既有", "responsibility": "§7 / §8 / §9 / §10 章节重写 + 顶部注释", "dependency": "无" },
    { "name": "code-plan 步骤定义", "path": "plugins/code-skills/skills/code-plan/SKILL.md", "status": "修改既有", "responsibility": "步骤 7A 补做强约束 + 步骤 10A 架构骨架触发收紧", "dependency": "无" },
    { "name": "code-plan 模板", "path": "plugins/code-skills/skills/code-plan/templates/plan.md", "status": "修改既有", "responsibility": "§4-§10 章节由'建议'改'必填'", "dependency": "无" },
    { "name": "code-check 步骤定义", "path": "plugins/code-skills/skills/code-check/SKILL.md", "status": "修改既有", "responsibility": "评审清单追加 3 个校验点", "dependency": "无" }
  ]
}
// → 5 行 markdown 表格
```

### 版本策略

- 沿用既有:**不**新增函数,仅在既有"模块表生成"调用前**追加**字段数限制(≤ 5 列)
- 字段超过 5 列 → 步骤 8A 询问用户,允许"用户授权的偏离"(写入 `rule-compliance.md`)

### 兼容策略

- 既有"模块表生成"的**入参/出参**不变化,故**不**影响下游
- `code-plan` 步骤 4 读模块表时**不**校验字段数(本设计**不**加校验,避免硬约束太死)

### 依据规范

- `module-conventions §规则 1`

## 接口 3:`code-design` 步骤 10A 接口概要生成(内部函数)

### 形式

- 内部函数

### 签名

```ts
function buildInterfaceSummary(interfaces: InterfaceSummary[]): string  // 返回 markdown 表格字符串
```

### 入参

```typescript
{
  interfaces: Array<{
    name: string,           // 接口名
    form: 'REST' | 'gRPC' | '事件' | '函数' | 'SDK 方法',
    status: '新增' | '扩展既有' | '修改既有',
    responsibility: string  // 一句话职责
  }>
}
```

### 出参

```markdown
| 接口名 | 形式 | 状态 | 一句话职责 |
| --- | --- | --- | --- |
| ... | ... | ... | ... |
```

### 错误码

- **不适用**

### 示例

```json
// 本需求 9 个内部函数接口
{
  "interfaces": [
    { "name": "code-design 步骤 0b 判定入口", "form": "函数", "status": "修改既有", "responsibility": "评估'小需求 / 扩展性触发',决定问题数" },
    { "name": "code-design 步骤 9A 模块表生成", "form": "函数", "status": "修改既有", "responsibility": "输出 5 列模块表" },
    { "name": "code-design 步骤 10A 接口概要生成", "form": "函数", "status": "修改既有", "responsibility": "输出 4 项 / 接口" },
    { "name": "code-design 步骤 10A 数据结构生成", "form": "函数", "status": "修改既有", "responsibility": "输出 4 项 / 实体" },
    { "name": "code-plan 步骤 7A 补做入口", "form": "函数", "status": "修改既有", "responsibility": "强制 §4-§10 必填 + 4 过程文档必选" },
    { "name": "code-plan 步骤 10A 架构骨架判定", "form": "函数", "status": "修改既有", "responsibility": "5 条件'或'判定是否插入 T-001" },
    { "name": "code-check 校验点 1(详设完整性)", "form": "函数", "status": "新增", "responsibility": "校验每条任务'涉及文件'在 §4-§10 找对应章节" },
    { "name": "code-check 校验点 2(概设越界)", "form": "函数", "status": "新增", "responsibility": "校验 design §7/§8/§9 不出现详设深度内容" },
    { "name": "code-check 校验点 3(行数比例)", "form": "函数", "status": "新增", "responsibility": "校验 design / plan 行数比例 ≤ 1.2" }
  ]
}
```

### 版本策略 / 兼容策略 / 依据规范

- 沿用接口 2 的版本/兼容/规范策略

## 接口 4:`code-check` 校验点 1 — 详设完整性(新增)

### 形式

- 内部函数(由 `code-check` 步骤 6 调用)

### 签名

```ts
function validatePlanIntegrity(
  planResultPath: string,    // plan/<REQ>/RESULT.md 路径
  planPath: string           // plan/<REQ>/PLAN.md 路径
): ValidationResult
```

### 入参

- `planResultPath`:`./assistants/<版本号>/plan/<REQ>/RESULT.md`
- `planPath`:`./assistants/<版本号>/plan/<REQ>/PLAN.md`

### 出参

```typescript
{
  passed: boolean,
  missing: Array<{
    taskId: string,           // 任务编号(如 TASK-REQ-00030-00003)
    reason: string,           // "涉及文件 X 未在 §4-§10 任何章节引用"
  }>
}
```

### 错误码

- **不适用**(内部函数)

### 示例

```json
// 正常:每条任务的"涉及文件"都在 §4-§10 找到对应章节
{
  "passed": true,
  "missing": []
}

// 异常:T-003 涉及 file_A.md 但 §4-§10 无引用
{
  "passed": false,
  "missing": [
    { "taskId": "TASK-REQ-00030-00003", "reason": "涉及文件 plugins/code-skills/skills/code-plan/templates/plan.md 未在 §4-§10 任何章节引用" }
  ]
}
```

### 版本策略

- 沿用既有 `code-check` 评审清单:**追加**1 个校验点(本接口)
- 既有 5 个校验点**不**修改

### 兼容策略

- 派生任务**不**直接阻断 `code-check`(沿用既有:派生"重构"类型任务,供 `code-it` 处理)
- 派生任务格式:类型=`重构` / 触发/来源=`设计变更` / 关联任务=被修正原任务

### 依据规范

- `commit-conventions`(派生任务按"重构"类型登记)
- `dashboard-conventions §规则 1`(派生任务同步到"任务清单"区段)

## 接口 5:`code-check` 校验点 2 — 概设越界检测(新增)

### 形式

- 内部函数

### 签名

```ts
function validateDesignBoundary(designResultPath: string): ValidationResult
```

### 入参

- `designResultPath`:`./assistants/<版本号>/design/<REQ>/RESULT.md`

### 出参

```typescript
{
  passed: boolean,
  violations: Array<{
    chapter: string,           // "§7 / §8 / §9"
    matchText: string,         // 匹配的"详设深度"关键词上下文(≤ 100 字符)
    pattern: string            // 触发的正则(如 "字段类型\\s*[:=]\\s*\\w+")
  }>
}
```

### 错误码

- **不适用**

### 触发模式(正则)

```typescript
const DETAIL_PATTERNS = [
  /\|\s*\w+\s*\|\s*(string|number|integer|boolean|datetime|UUID)\s*\|/,  // 表格行含类型(string/number 等)
  /\b(错误码|error[_ ]?code)\s*[:=]?\s*\d{4,}/,                            // "错误码: 40001" 模式
  /\b(鉴权|auth|authentication)\s*[:=]/,                                  // "鉴权:" 模式
  /\b(索引|index)\s*[:=]?\s*\w+\s*\(/,                                    // "索引: <name>(" 模式
  /\b(迁移脚本|migration)\s*[:=]/,                                         // "迁移脚本:" 模式
]
```

### 示例

```json
// 异常:design §9 出现 "字段类型:string"
{
  "passed": false,
  "violations": [
    { "chapter": "§9 数据结构", "matchText": "| name | string | NOT NULL | ...", "pattern": "/\\|\\s*\\w+\\s*\\|\\s*(string|...)" }
  ]
}
```

### 版本策略 / 兼容策略 / 依据规范

- 沿用接口 4

## 接口 6:`code-check` 校验点 3 — 行数比例警告(新增)

### 形式

- 内部函数

### 签名

```ts
function validateLineRatio(designResultPath: string, planResultPath: string): ValidationResult
```

### 入参

- `designResultPath` / `planResultPath`(同接口 4)

### 出参

```typescript
{
  passed: boolean,        // 始终 true(标黄警告,不阻断)
  ratio: number,          // design 行数 / plan 行数
  warning?: string        // 标黄文案(若 ratio > 1.2)
}
```

### 错误码

- **不适用**

### 阈值

- 阈值:1.2(来自 FR-7 / AC-6.3)
- 警告文案:`⚠ 概设/详设行数比例异常(<ratio>),建议复核概设是否过深`

### 示例

```json
// design=200 行, plan=300 行 → ratio=0.67 → 通过
{ "passed": true, "ratio": 0.67, "warning": null }

// design=200 行, plan=100 行 → ratio=2.0 → 警告
{ "passed": true, "ratio": 2.0, "warning": "⚠ 概设/详设行数比例异常(2.0),建议复核概设是否过深" }
```

### 版本策略 / 兼容策略 / 依据规范

- 沿用接口 4
- 额外:**不**阻断 `code-check`(即使 ratio > 1.2)

## 接口总览(本节)

| 接口名 | 形式 | 状态 | 对应任务 | 依据规范 |
| --- | --- | --- | --- | --- |
| `code-design` 步骤 0b 判定入口 | 函数 | 修改既有 | T-001 | `skill-conventions §规则 1` |
| `code-design` 步骤 9A 模块表生成 | 函数 | 修改既有 | T-001 | `module-conventions §规则 1` |
| `code-design` 步骤 10A 接口概要生成 | 函数 | 修改既有 | T-001 | `module-conventions §规则 1` |
| `code-plan` 步骤 7A 补做入口 | 函数 | 修改既有 | T-003 | `encoding-conventions §规则 1/3` |
| `code-plan` 步骤 10A 架构骨架判定 | 函数 | 修改既有 | T-003 | `encoding-conventions §规则 1/3` |
| `code-check` 校验点 1(详设完整性) | 函数 | 新增 | T-005 | `commit-conventions` |
| `code-check` 校验点 2(概设越界) | 函数 | 新增 | T-005 | `commit-conventions` |
| `code-check` 校验点 3(行数比例) | 函数 | 新增 | T-005 | `commit-conventions` |

## 关键决策(本节)

- **鉴权方式**:**不适用**(本仓库无 API / 无鉴权)
- **错误码体系**:**不适用**(无对外 API)
- **限流策略**:**不适用**
- **幂等保证**:**不适用**
- **链路追踪字段**:**不适用**
