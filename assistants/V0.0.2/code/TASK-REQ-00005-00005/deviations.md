# 偏离记录 — TASK-REQ-00005-00005

版本:V0.0.2
任务完成时间:2026-06-04 17:54

## 偏离数:**0**(严格执行 review §"不需要做的")

本任务的实施**100% 遵循** `review/TASK-REQ-00005-00005/RESULT.md`,无任何对 review 输入的偏离。

### 自检

| 检查项 | 状态 | 来源 |
| --- | --- | --- |
| F-1(文档头第 11 行) `<TBD>` → 完整 hash | ✅ | review/RESULT.md §2 F-1 + §3 文件 1 位置 1 |
| F-2(§3.1 第 60 行) `<TBD>` → 完整 hash | ✅ | review/RESULT.md §2 F-2 + §3 文件 1 位置 2 |
| **不**重写 T-004 RESULT.md 的任何其他字段 | ✅ | review §4 显式约束 |
| **不**修改 V0.0.2/RESULT.md 看板(已正确显示) | ✅ | review §4 |
| **不**修改 plan/REQ-00005/PLAN.md(已正确显示完整 hash) | ✅ | review §4 |
| **不**修改 3 个 SKILL.md(本任务与 T-001~T-003 完全无关) | ✅ | review §4 |
| **不**触发额外 commit 范围扩大 | ✅ | review §4 |
| **不**越界:在 review 阶段新增任务(`T-005`)的改修结果中,若发现其他问题,记到 `deviations.md`,不擅自修复 | ✅ | code-it 通用原则 |
| 任务编号 `TASK-REQ-00005-00005` 5+5 位 | ✅ | `encoding-conventions.md §规则 3` |
| commit message scope = `code-review`(因本任务由 code-review 派生,改的是 code/<T-XXX>/RESULT.md 文档) | ✅ | NFR-6 沿用 V0.0.1 实践 |

### 显式声明的"合理接受"(非偏离)

#### A-1:T-004 RESULT.md 中残留 3 处叙事性 `<TBD>`
- **位置**:T-004/RESULT.md 行 113 / 162 / 184
- **类别**:文档一致性(轻微)
- **现象**:回填后 `grep -c "<TBD>"` 仍 = 3
- **实际做法**:**保留**(不修改)— 严格遵守 review §4"不重写 T-004 RESULT.md 的任何其他字段"
- **理由**:
  - 这 3 处全部是**叙事性 / 说明性**文本(决策说明 / 提交字段注释 / commit 链示例),不是 F-1 / F-2 显式列举的"提交哈希 字段"
  - review 的"问题清单"只列了 2 处(行 11 + 行 36 → 实际行 60),未涉及这 3 处
  - review 的"不需要做的"显式说"**不**重写 T-004 RESULT.md 的任何其他字段"
- **影响**:低 — 看板 / PLAN.md / 任务自身 RESULT.md 三处已一致;这 3 处叙事仅是 T-004 自己的"过去决策"记录,不影响追踪
- **建议**:留作 follow-up(本任务**不**处理)— 后续若用户希望文档更干净,可单独派生"清理 T-004 RESULT.md 叙事性 `<TBD>`"任务
- **授权**:wangmiao(本任务执行者,严格遵守 review §4)

#### A-2:commit message scope 选用 `code-review` 而非 `code-it`
- **类别**:commit message 命名(轻微)
- **实际做法**:scope = `code-review`
- **理由**:
  - NFR-6 沿用 V0.0.1 实践 `chore(<scope>): <subject>`
  - scope 应反映"本任务实际改的是什么"或"本任务由谁派生"
  - 本任务**不是**普通 `code-it` 任务(改源码),而是 `code-review` 派生的"审查改修"任务(改文档)
  - 选择 `code-review` 更能反映"本任务的来源 + 实际改的文档是 code/<T-XXX>/RESULT.md"
- **不是偏离**:这是**有意的 scope 选择**,与 NFR-6 严格遵循
