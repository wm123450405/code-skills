# 修复设计 — BUG-00010

## 1. 设计目标

明确 `/code req` 与 `/code fix` 的 CHECK 阶段对"必须改/建议改/可选改"三档发现的两态行为:
- **默认模式**:必须改 → 自动修复(评审-编码循环);建议改 → 逐项 AskUserQuestion(选修复则走 CODING 修复,选跳过则保留);可选改 → 同建议改
- **`--auto` 模式**:必须改 → 自动修复;建议改 → 自动应用所有项(无需弹窗);可选改 → 自动应用所有项(无需弹窗)

## 2. 修复范围

| 项 | 是否修改 |
| --- | --- |
| `references/req/check.md` 步骤 5 + 阶段完成确认 | ✓ 明确三档 + 两态 |
| `references/req/check.md` 新增"可选改"步骤 | ✓ |
| plugins cache SKILL.md req 子命令步骤 5 | ✓ 同步 |
| plugins cache SKILL.md fix 子命令步骤 5 | ✓ 同步 |

## 3. 修复方案

### 3.1 references/req/check.md 改造

**步骤 5 改造**(将原"处理建议改"小节升级为"处理建议改/可选改"):

```
### 步骤 5 — 处理建议改与可选改(两态行为)

CHECK 评审-编码循环结束后,对剩余的"建议改"与"可选改"发现,按当前模式处理:

| 模式 | 必须改 | 建议改 | 可选改 |
| --- | --- | --- | --- |
| 默认 | 评审-编码循环(自动) | 逐项 AskUserQuestion(A 修复 / B 跳过) | 逐项 AskUserQuestion(A 修复 / B 跳过) |
| `--auto` | 评审-编码循环(自动) | 全部自动应用 | 全部自动应用 |
| `--confirm` | 评审-编码循环(自动) | 逐项 AskUserQuestion | 逐项 AskUserQuestion |

function handleOptionalFindings(findings, mode):
  // 必须改已由步骤 4 评审-编码循环处理,此处只处理建议改与可选改
  // 必须改不存在于本函数输入

  if mode == "--auto":
    // --auto:全部自动应用
    for finding in findings:
      if finding.status == "已处理":
        continue
      executeOptionalFix(finding)  // 走 CODING 修复流程
      finding.status = "已处理"
    print(f"--auto 模式:已自动应用 {findings.length} 项建议改/可选改")
    return { autoApplied: findings.length, userDeclined: 0 }

  // 默认 / --confirm:逐项 AskUserQuestion
  userDeclined = 0
  autoApplied = 0
  for finding in findings:
    if finding.status == "已处理":
      continue

    AskUserQuestion:
      {finding.level}: {finding.description}
      文件: {finding.file}:{finding.line}
      建议: {finding.suggestion}
      A. 修复(推荐)
      B. 跳过(保留)

    if A:
      executeOptionalFix(finding)  // 走 CODING 修复流程
      finding.status = "已处理"
      autoApplied++
    else:
      userDeclined++

  return { autoApplied, userDeclined }
```

**新增 executeOptionalFix 函数**(复用现有 CODING 任务执行能力):

```
function executeOptionalFix(finding):
  // 1. 生成改修任务(同必须改的逻辑,但 source = "建议改改修" / "可选改修")
  taskId = allocateNextTaskNum(reqNum)
  newTask = {
    id: taskId,
    type: "修改",
    source: "建议改改修" if finding.level == "建议改" else "可选改修",
    title: "[改修] {finding.description}",
    files: [finding.file],
    status: "待开始",
    deps: []
  }

  // 2. 追加到 PLAN.md
  appendTasksToPlan(reqNum, [newTask])

  // 3. 走 CODING 阶段执行(复用 coding.md 流程)
  appendProcess("CODING", "开始", "{taskId} 开始({newTask.source})")
  executeCodingTask(newTask)
  appendProcess("CODING", "完成", "{taskId} 完成")

  // 4. 不进入新一轮 CHECK 循环(只走 CODING 单次执行,不回头复审)
```

**关键差异 vs 必须改**:
- 必须改:进入评审-编码循环(改完再审,直到无必须改,最多 5 轮)
- 建议改/可选改:走 CODING 单次执行(改完不回头复审)

### 3.2 阶段完成确认小节改造

```
### 建议改/可选改确认

对每个"建议改"或"可选改"发现,按模式处理:

**默认 / --confirm 模式**:
  逐项 AskUserQuestion:
    <level>: <description>
    A. 修复(推荐)
    B. 跳过

**--auto 模式**:
  全部自动应用,不弹窗。

**汇总**:
- 自动应用数: <N>
- 用户跳过数: <M>
```

### 3.3 SKILL.md req 子命令步骤 5 改造

```
#### 步骤 5 — CHECK 阶段(代码审查)

- 收集审查材料:REQUIRE/DESIGN/PLAN/TASK-N/源码
- 逐维度审查:正确性/需求一致性/设计一致性/规范性/安全性/性能/可维护性/测试覆盖/代码行数超标(新增)
- 分类发现:必须改/建议改/可选
- 评审-编码循环(必须改):存在"必须改"→ 生成改修任务 → CODING 修复 → 重新 CHECK → 循环直到无"必须改"(最多 5 轮)
- **建议改/可选改处理**:
  - 默认模式:逐项 AskUserQuestion(每项独立弹窗,A 修复 / B 跳过;选 A 则走 CODING 修复,选 B 则保留)
  - `--auto` 模式:全部自动应用所有项,不再弹窗
- 产出 `CHECK.md`,按 `templates/req/CHECK.md` 结构
```

### 3.4 SKILL.md fix 子命令步骤 5 改造

```
#### 步骤 5 — CHECK 阶段(代码审查)

- 收集审查材料:BUG/DESIGN/PLAN/TASK-N/源码
- 逐维度审查:正确性/缺陷修复一致性/设计一致性/规范性/安全性/性能/可维护性/测试覆盖
- 分类发现:必须改/建议改/可选
- **必须改**:评审-编码循环,自动修复直到无必须改(最多 5 轮)
- **建议改/可选改**:
  - 默认模式:逐项 AskUserQuestion(每项独立弹窗,A 修复 / B 跳过)
  - `--auto` 模式:全部自动应用所有项,不再弹窗
- 使用 `Write` 写入 `CHECK.md`,按 `templates/req/CHECK.md` 结构
```

## 4. 兼容性考虑

- 与现有评审-编码循环(必须改)兼容,本次仅扩展到建议改/可选改
- 与 `--confirm` 模式兼容(行为同默认模式,逐项询问)
- 单次执行 vs 循环:建议改/可选改走单次 CODING,不进入新 CHECK 循环(避免无限递归)
- 改修任务 source 区分:必须改 = "审查改修";建议改 = "建议改改修";可选 = "可选改修"

## 5. 风险评估

| 风险 | 影响 | 缓解 |
| --- | --- | --- |
| `--auto` 自动应用所有项可能误改 | 中 | source 字段明确区分,便于审计 |
| 建议改/可选改数量大时,默认模式逐项弹窗疲劳 | 低 | 用户可选择"全部跳过"批量处理(由 AskUserQuestion 选项扩展) |
| 现有用户已习惯"评审-编码循环"自动应用 | 低 | 必须改行为不变,本次仅扩展建议改/可选改 |

## 6. 验收标准

- AC-1: 默认模式 + 必须改 → 评审-编码循环,自动修复(已有,保持)
- AC-2: 默认模式 + 建议改 → 逐项 AskUserQuestion,A 修复则走 CODING,B 跳过则保留
- AC-3: 默认模式 + 可选改 → 同建议改
- AC-4: `--auto` 模式 + 必须改 → 自动修复(已有,保持)
- AC-5: `--auto` 模式 + 建议改 → 全部自动应用,不弹窗
- AC-6: `--auto` 模式 + 可选改 → 全部自动应用,不弹窗
- AC-7: 改修任务 source 字段明确区分(必须改 = "审查改修";建议改 = "建议改改修";可选 = "可选改修")
- AC-8: CHECK.md 的"评审结论"区段显示"自动应用数"和"用户跳过数"

## 7. 任务拆分(待 PLAN 阶段细化)

候选任务:
- TASK-001: 修改 references/req/check.md 步骤 5 + 新增 executeOptionalFix + 阶段完成确认小节
- TASK-002: 修改 plugins cache SKILL.md req 子命令步骤 5
- TASK-003: 修改 plugins cache SKILL.md fix 子命令步骤 5
- TASK-004: 验证修改(check.md / SKILL.md 两处一致)
