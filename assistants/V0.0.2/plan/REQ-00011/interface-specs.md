# 接口详细规格 — REQ-00011

更新时间:2026-06-05
版本:V0.0.2

## 接口 1:`askDesignGoals(needContext)`(code-design 步骤 0b 触发)

- **形式**:Claude Code 工具 `AskUserQuestion`
- **签名**(伪代码):
  ```
  function askDesignGoals(needContext: NeedContext): DesignGoals
  ```
- **入参**:`needContext`(含需求规模评估字段,用于自适应问题数)
- **出参**:`DesignGoals` 对象
- **错误码**:**N/A**(由 `AskUserQuestion` 工具内部处理)
- **示例**:
  - 正常:用户回答 `--balanced` / 中 / 中 / 中 / 中 → `DesignGoals{overallGoal: "--balanced", ...}`
  - 取消:用户点"取消" → 工具返回取消信号 → 中止 + 回写空
- **版本策略**:**无版本**(本技能内部使用)
- **兼容策略**:**无**
- **依据规范**:FR-6 强约束"1-5 个问题自适应"

## 接口 2:`writeDesignGoalsSection(resultMdPath, goals, trigger)`(回写"## 设计目标"小节)

- **形式**:`Read` + `Write` 工具组合
- **签名**(伪代码):
  ```
  function writeDesignGoalsSection(
    resultMdPath: string,
    goals: DesignGoals,
    trigger: "code-design" | "code-plan"
  ): void
  ```
- **入参**:
  - `resultMdPath`:`string`,必填,目标 `RESULT.md` 路径
  - `goals`:`DesignGoals`,必填,设计目标对象
  - `trigger`:`"code-design" | "code-plan"`,必填,回写触发方
- **出参**:**无**(直接写文件)
- **错误码**:**N/A**(由 `Read` / `Write` 工具内部处理)
- **示例**:
  - 正常:`writeDesignGoalsSection("./assistants/V0.0.2/design/REQ-00011/RESULT.md", goals, "code-design")` → 在文件顶部"## 文档头"区段后 + "## 1. ..."前插入"## 设计目标"小节
  - 异常:`Write` 工具失败 → 透传 stderr
- **版本策略**:**无版本**
- **兼容策略**:**幂等**(NFR-3)— 多次执行覆盖前次内容
- **依据规范**:FR-5 + NFR-3

## 接口 3:`readDesignGoalsFromDesign(designResultPath)`(code-plan 步骤 0b 读取)

- **形式**:`Read` 工具
- **签名**(伪代码):
  ```
  function readDesignGoalsFromDesign(designResultPath: string): DesignGoals | null
  ```
- **入参**:`designResultPath`:`string`,必填,`design/.../RESULT.md` 路径
- **出参**:`DesignGoals | null`(存在小节 → 返回对象;不存在 → 返回 `null`)
- **错误码**:**N/A**
- **示例**:
  - 正常:文件存在且含"## 设计目标"小节 → 返回 `DesignGoals{...}`
  - 异常:文件不存在 → 返回 `null`(FR-3 退化)
  - 异常:文件存在但无小节 → 返回 `null`(E-5 退化)
- **版本策略**:**无版本**
- **兼容策略**:**无**
- **依据规范**:FR-2 / FR-3 + E-5 边界

## 接口 4:`adjustTaskGranularityByGoals(plan, goals)`(code-plan 任务粒度调整)

- **形式**:内部函数(纯计算,无 IO)
- **签名**(伪代码):
  ```
  function adjustTaskGranularityByGoals(plan: Plan, goals: DesignGoals): Plan
  ```
- **入参**:
  - `plan`:`Plan`,必填,当前 PLAN.md 任务总览
  - `goals`:`DesignGoals`,必填,设计目标对象
- **出参**:`Plan`,调整后的 PLAN.md 任务总览
- **错误码**:**N/A**
- **示例**:
  - 正常:goals = `{overallGoal: "--extensible", extensibility: "高"}` → 在 plan.tasks 首位插入 3 个扩展性任务
  - 异常:goals = `{overallGoal: "--balanced"}` → 无调整,返回原 plan
- **版本策略**:**无版本**
- **兼容策略**:**无**(纯计算)
- **依据规范**:FR-4 + D-5 判定表

## 接口总览表

| 接口名 | 形式 | 状态 | 对应任务 | 依据规范 |
| --- | --- | --- | --- | --- |
| `askDesignGoals` | `AskUserQuestion` | 新增 | T-001 | FR-6 |
| `writeDesignGoalsSection` | `Read` + `Write` | 新增 | T-001 / T-002 | FR-5 / NFR-3 |
| `readDesignGoalsFromDesign` | `Read` | 新增 | T-002 | FR-2 / FR-3 |
| `adjustTaskGranularityByGoals` | (内部) | 新增 | T-002 | FR-4 |

## 关键决策
- **不引入对外 API**:本需求不新增任何对外契约(纯技能内部流程调整)
- **屏显模板**:`=== code-design 设计目标确认 ===` / `=== code-plan 设计目标确认 ===` 区段(参考 REQ-00011 §6.1 / §6.2 / §6.3)
- **幂等性**:NFR-3 强约束(覆盖前次内容)
- **链路追踪**:**无**(本需求不涉及)
