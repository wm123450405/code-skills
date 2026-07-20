# 代码审查阶段 — code-req

> 本文件为 code-req 技能的 CHECK 阶段提供详细流程。在进入 CHECK 阶段时加载。

## 目标

在所有任务编码完成后,系统化审查代码质量,发现缺陷并给出可执行的改修建议,产出 `CHECK.md`。若存在"必须改"发现,自动生成改修任务并进入 CODING 阶段修复,修复后重新审查,循环直到无"必须改"发现。

## 前置条件

- CODING 阶段已完成(所有任务开发状态 = 已完成)
- 所有 TASK-N.md 已产出

## 输入

- `req/<REQ-NNNNN>/REQUIRE.md`(需求基线)
- `req/<REQ-NNNNN>/DESIGN.md`(设计基线)
- `req/<REQ-NNNNN>/PLAN.md`(任务列表)
- 所有 `req/<REQ-NNNNN>/TASK-N.md`(编码产出)
- 项目级规范:`./assistants/rules/` 下所有文件
- 当前项目代码:CWD 下的源文件(实际审查对象)

## 输出

主产出物:`req/<REQ-NNNNN>/CHECK.md`
辅助产物:`req/<REQ-NNNNN>/LOG.md`(可选)
改修任务:`PLAN.md` 中追加的审查改修任务

## 工作流程

### 步骤 1 — 收集审查材料

1. `Read "req/<REQ-NNNNN>/REQUIRE.md"` — 提取 FR/AC
2. `Read "req/<REQ-NNNNN>/DESIGN.md"` — 提取模块/接口/数据结构
3. `Read "req/<REQ-NNNNN>/PLAN.md"` — 提取任务列表
4. 逐任务 `Read "req/<REQ-NNNNN>/TASK-N.md"` — 提取改动内容、逻辑行统计
5. `Read` 实际源码文件(从 TASK-N.md 的涉及文件列表)

### 步骤 2 — 逐维度审查

#### 审查维度

| 维度 | 权重 | 检查内容 |
| --- | --- | --- |
| 正确性 | P0 | 逻辑是否正确,边界条件是否处理,异常是否覆盖 |
| 需求一致性 | P0 | 是否满足 REQUIRE.md 中的 FR/AC |
| 设计一致性 | P0 | 是否遵循 DESIGN.md 的模块/接口/数据结构 |
| 规范性 | P1 | 是否符合项目级编码规范 |
| 安全性 | P1 | 是否存在注入/泄漏/越权等安全风险 |
| 性能 | P2 | 是否存在明显性能问题(N+1 查询/大循环等) |
| 可维护性 | P2 | 命名是否清晰,注释是否充分,结构是否合理 |
| 测试覆盖 | P2 | 关键路径是否有测试,边界条件是否覆盖 |
| 代码行数超标 | P2 | 单文件是否超过逻辑行阈值(新增) |

#### 代码行数超标检查(新增)

> 从 TASK-N.md 的逻辑行统计中提取数据,按阈值判定。

| 超标比例 | 级别 |
| --- | --- |
| ≤10% | 可选 |
| >10% 且 ≤50% | 建议改 |
| >50% | 必须改 |

**阈值默认值**(可被 REQUIRE.md 覆盖):
- 单文件逻辑行总规模阈值:500
- 单文件逻辑行新增阈值:200

**阈值覆盖**:若 REQUIRE.md 中存在"## 阈值配置"小节,则使用覆盖值。

#### 审查方法

```
for each 维度:
  for each 涉及文件:
    Read 源码
    对比 需求/设计/规范
    记录发现
```

### 步骤 3 — 分类发现

#### 严重程度

| 级别 | 含义 | 处理 |
| --- | --- | --- |
| 必须改 | 功能缺陷/安全漏洞/设计偏离/代码行数超额>50% | 必须修复后才能合并 |
| 建议改 | 代码异味/性能优化/命名改进/代码行数超额 10-50% | 建议修复,可协商 |
| 可选 | 风格偏好/锦上添花/代码行数超额≤10% | 记录但不强制 |

#### 发现格式

```
发现编号: F-<序号>
级别: 必须改/建议改/可选
维度: 正确性/规范性/...
文件: <文件路径>:<行号>
描述: <具体问题>
建议: <可执行的修改方案>
状态: 待处理/已处理
```

### 步骤 4 — 评审-编码循环(增强)

> 评审完成后,若存在"必须改"发现,进入 CODING↔CHECK 循环。

```
function checkCodeLoop(reqNum, autoMode, maxRounds = 5):
  round = 0
  allFindings = []
  
  while round < maxRounds:
    round++
    appendProcess("CHECK", "开始", "第${round}轮审查")
    
    // 收集材料 + 逐维度审查
    findings = executeReview(reqNum)
    allFindings.push(...findings)
    
    mustFix = findings.filter(f => f.level == "必须改" && f.status != "已处理")
    
    if mustFix.length == 0:
      appendProcess("CHECK", "完成", "第${round}轮审查:0条必须改,审查通过")
      return { status: "PASS", rounds: round, findings: allFindings }
    
    // 生成改修任务
    newTasks = []
    for finding in mustFix:
      taskId = allocateNextTaskNum(reqNum)
      newTask = {
        id: taskId,
        type: "修改",
        source: "审查改修",
        title: "[改修] ${finding.description}",
        files: [finding.file],
        status: "待开始",
        deps: []
      }
      newTasks.push(newTask)
    
    // 追加到 PLAN.md
    appendTasksToPlan(reqNum, newTasks)
    appendProcess("CHECK", "完成", "第${round}轮审查:${mustFix.length}条必须改,生成改修任务 ${newTasks.map(t => t.id).join(',')}")
    
    // 进入 CODING 阶段执行改修任务
    for task in newTasks:
      appendProcess("CODING", "开始", "${task.id} 开始(审查改修)")
      executeCodingTask(task)  // 执行单个任务的编码(复用 coding.md 流程)
      appendProcess("CODING", "完成", "${task.id} 完成")
    
    // 改修完成后重新审查(回到循环开头)
  
  // 达到上限
  appendProcess("CHECK", "完成", "达到最大循环轮数(${maxRounds}),仍有${mustFix.length}条必须改未处理")
  return { status: "MAX_ROUNDS", rounds: round, findings: allFindings }
```

**循环约束**:
- 循环上限:5 轮(与错误修复循环一致)
- 每轮 CHECK 必须重新审查所有变更(非仅改修任务)
- 改修任务编号:使用递增序号,在 PLAN.md 中追加
- `--auto` 模式下自动循环,无需确认
- 非 `--auto` 模式下,每轮循环完成后确认(继续改修/暂停/取消)
- 达到上限后停下询问用户(非 `--auto`)或报告( `--auto`)

### 步骤 5 — 处理建议改

对每个"建议改"发现,询问用户:

```
建议改: <发现描述>
选项:
A. 修复(推荐)
B. 跳过
C. 记录但不修复
```

### 步骤 6 — 撰写 CHECK.md

按 `templates/CHECK.md` 结构生成:

```
# 代码审查 — <REQ-NNNNN> · <标题>

## 评审维度
| 维度 | 权重 | 结果 |
| --- | --- | --- |
| 正确性 | P0 | 通过/不通过 |
| 需求一致性 | P0 | 通过/不通过 |
| ... | ... | ... |
| 代码行数超标 | P2 | 通过/不通过 |

## 发现汇总
| 编号 | 级别 | 维度 | 文件 | 描述 | 建议 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| F-1 | 必须改 | 正确性 | src/a.ts:42 | 空指针 | 加空检查 | 已处理 |
| F-2 | 建议改 | 命名 | src/b.ts:15 | 变量名不清 | 改为 userName | 待处理 |

## 评审结论
- 总发现数: <N>
- 必须改: <N1>(已处理: <N2>)
- 建议改: <N3>
- 可选: <N4>
- 循环轮数: <R>
- 结论: <通过/不通过>
```

### 步骤 7 — 评审结论判定

```
function determineConclusion(findings, loopStatus):
  mustFix = findings.filter(f => f.level == "必须改" && f.status != "已处理")
  if mustFix.length > 0:
    if loopStatus == "MAX_ROUNDS":
      return "不通过 — 达到最大循环轮数,仍有未处理的必须改项"
    return "不通过 — 存在未处理的必须改项"
  return "通过 — 所有必须改项已处理"
```

## 阶段完成确认

> 三态确认模型:阶段边界确认由 `--confirm`/`--auto`/默认 控制。阶段内内容确认(建议改/循环确认)仅在 `--auto` 模式下跳过。详见 common.md §4、§7、§11。

### 建议改确认

对每个"建议改"发现,询问用户:

```
建议改: <发现描述>
选项:
A. 修复(推荐)
B. 跳过
C. 记录但不修复
```

### 循环确认

每轮循环完成后:

```
第<N>轮审查完成: <M> 条必须改,已生成改修任务
```

`--confirm` 模式弹出确认(继续改修/中止)。`--auto` 和默认模式自动继续改修。

### --confirm 模式

阶段完成后弹出增强确认:
```
=== code-req --confirm: CHECK 阶段完成 ===
代码审查完成: <N> 发现 / <M> 必须改(已处理) / <K> 建议改 / <R> 轮循环
结论: <通过/不通过>

产出物文件:
  - req/<REQ>/CHECK.md

你可以手动修改上述文件,完成后选择:
A. 继续(重新读取产出物,获取最新修改,进入 DONE 阶段)
B. 中止(保存当前进度,退出)
```

### --auto 模式

自动继续,屏幕输出前缀。阶段内确认自动选推荐项。

### 默认模式(无 flag)

阶段边界自动继续,无输出。阶段内确认正常触发 `AskUserQuestion`。