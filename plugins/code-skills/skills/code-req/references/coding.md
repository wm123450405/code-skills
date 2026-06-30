# 编码执行阶段 — code-req

> 本文件为 code-req 技能的 CODING 阶段提供详细流程。在进入 CODING 阶段时加载。

## 目标

按 PLAN.md 中的任务列表,逐任务执行编码,产出可工作的代码与 `TASK-N.md` 完成报告。

## 前置条件

- `PLAN.md` 必须存在且 PLAN 阶段已完成
- 所有前置任务必须已完成(开发状态 = 已完成)

## 输入

- `req/<REQ-NNNNN>/PLAN.md`(任务列表)
- `req/<REQ-NNNNN>/DESIGN.md`(设计参考)
- `req/<REQ-NNNNN>/REQUIRE.md`(需求参考)
- 项目级规范:`./assistants/rules/` 下所有文件
- 语言适配:`./code-req/references/languages/<lang>.md`(按需加载)
- 当前项目代码:CWD 下的源文件

## 输出

每个任务产出:`req/<REQ-NNNNN>/TASK-<序号>.md`
代码变更:CWD 下的实际代码改动
过程文档:`compile-and-run.md`(编译/运行记录)、`test-results.md`(测试结果)、`deviations.md`(偏差记录)、`process-doc-decisions.md`(过程文档判定记录)

## 工作流程

### 步骤 0 — CODING 阶段激活校验(强制)

> **在任何代码修改之前,必须先通过本校验。本校验是代码修改权限的唯一依据。**

1. 读取 `PROCESS.md` 最后一行
2. 解析阶段字段:
   - 阶段 = `CODING` → 校验通过,允许后续步骤修改 CWD 源码
   - 阶段 ≠ `CODING` → **校验失败**,输出:
     ```
     ⛔ 代码修改被拒绝:当前阶段为 <阶段>,不允许修改 CWD 源码。
     请先完成前置阶段(REQUIRE→DESIGN→PLAN),待 PROCESS.md 显示 CODING 阶段后再执行代码修改。
     ```
     立即停止,不执行任何代码修改操作
3. 若 `PROCESS.md` 不存在 → 视为 `INIT` 阶段,拒绝修改代码,提示:
   ```
   ⛔ 代码修改被拒绝:PROCESS.md 不存在,当前视为 INIT 阶段。
   请先完成 REQUIRE→DESIGN→PLAN 阶段后再执行代码修改。
   ```

```
function codingStageGate(reqDir):
  processMd = reqDir + "/PROCESS.md"
  if not exists(processMd):
    return { allowed: false, currentStage: "INIT", reason: "PROCESS.md 不存在" }
  
  lastLine = tail(processMd, 1)
  stage = parseStage(lastLine)
  
  if stage == "CODING":
    return { allowed: true, currentStage: "CODING" }
  else:
    return { allowed: false, currentStage: stage, reason: "当前阶段不是 CODING" }
```

### 步骤 1 — 解析任务列表

从 PLAN.md 任务总览表中提取任务列表:

```
function parseTaskList(planMd):
  tasks = []
  for row in planMd.taskTable:
    if row.type != "删除":  // 删除任务在最后统一处理
      tasks.push({
        id: row.id,
        type: row.type,
        title: row.title,
        files: row.files,
        status: row.status,
        deps: row.deps
      })
  return tasks
```

### 步骤 2 — 前置任务守卫(增强)

对当前任务,检查所有前置任务是否已完成:

```
function guardPredecessors(task, planMd):
  // 按 PLAN.md 任务总览文件行序判定"当前任务的前置任务是否全部完成"
  // 前置任务 = 当前任务之前的所有任务(按行序)
  for dep in task.deps:
    depTask = findTask(planMd, dep)
    if depTask.status != "已完成":
      print("前置任务未完成: ${dep}")
      print("推荐先执行: code-it ${dep}")
      return false
  return true
```

- PLAN.md 不存在/解析失败 → 守卫通过(软失败退化)
- 前置任务未完成 → 中止当前任务,打印推荐命令

### 步骤 3 — 任务循环

```
for task in tasks:
  // 1. 前置守卫
  if not guardPredecessors(task, planMd):
    skip(task)
    continue
  
  // 2. 跳过已完成
  if task.status == "已完成":
    continue
  
  // 3. 推进状态
  updateTaskStatus(task.id, "进行中")
  appendProcess("CODING", "开始", "${task.id} 开始")
  
  // 4. 执行编码
  try:
    result = executeTask(task)
    updateTaskStatus(task.id, "已完成")
    appendProcess("CODING", "完成", "${task.id} 完成")
  catch error:
    updateTaskStatus(task.id, "阻塞")
    appendProcess("CODING", "失败", "${task.id}: ${error}")
    if not autoMode:
      askUserQuestion("任务失败,是否继续?")
      if answer == "取消":
        break
```

### 步骤 4 — 执行单个任务

#### 4.1 读取设计参考

- 从 DESIGN.md 中定位本任务涉及的模块/接口/数据结构
- 从 REQUIRE.md 中定位本任务涉及的 FR/AC

#### 4.2 检测项目语言类型(新增)

> 在探索项目代码前,先检测项目语言,加载对应语言适配文件。

```
function detectLanguage(projectRoot):
  if exists("go.mod"): return "go"
  if exists("Cargo.toml"): return "rust"
  if exists("pom.xml"): return "java-maven"
  if exists("build.gradle") or exists("build.gradle.kts"): return "java-gradle"
  if exists("pyproject.toml") or exists("setup.py") or exists("setup.cfg"): return "python"
  if exists("package.json"): return "nodejs"
  return "unknown"
```

- 检测到语言后,加载 `references/languages/<lang>.md`
- 后续编译/测试/运行步骤使用语言感知的命令
- 未知语言 → 使用通用启发式检测,退化到常见命令

#### 4.3 探索项目代码

- `Glob` 探索本任务涉及的文件
- `Grep` 搜索关键函数/类/接口
- `Read` 读取需要修改的文件

#### 4.4 实施编码

**编码原则**:
- 贴合项目现有风格
- 命名自解释,避免缩写
- 边界条件显式处理,不吞异常
- 关键路径埋点
- 代码注释解释"为什么",不解释"做什么"
- **代码注释不引用内部追踪编号**:用功能描述替代 REQ-/BUG-/TASK- 编号
- 不引入未经评审的新依赖
- 每次只做本任务范围的事

**追踪编号禁用规则**:
产出代码中不得出现 REQ-NNNNN / BUG-NNNNN / TASK-* 格式的编号。
- ✅ `// 用户登录:验证用户名密码,返回 JWT token`
- ❌ `// REQ-00042: 实现用户登录`
此约束不覆盖 commit message 和 `./assistants/` 工作产物。

**审查改修任务特殊规则**(当触发/来源 = 审查改修时):
- 按 CHECK.md 的发现清单展开改修,仅处理"应当改修的文件清单"中的内容
- 严格遵守"不需要做的"部分,不越界
- 发现其他问题 → 记入 `deviations.md`,不擅自修复
- 改修完成后标记对应发现状态为"已处理"

#### 4.5 修改文件前重读

> 修改任何文件前,必须先 `Read` 该文件的最新内容,确保基于最新版本编辑。

#### 4.6 过程文档自适应判定(新增)

> 在编译/运行/测试前,自适应判定本轮是否生成对应过程文档。

| 过程文档 | 判定准则 |
| --- | --- |
| `compile-and-run.md` | 编译或运行被触发 → 生成 |
| `test-results.md` | 测试被触发 → 生成 |
| `deviations.md` | 发生设计偏离/审查改修越界 → 生成 |
| `process-doc-decisions.md` | 上述任一"不生成"判定 → 生成 |

- 仅当存在"不生成"判定时才写 `process-doc-decisions.md`
- 全为"生成" → 不写决策记录

#### 4.7 项目可测性守卫(新增)

> 在写单测前,先判定项目是否可测。

```
function testabilityGuard(projectRoot):
  checks = [
    "package.json" + "scripts.test",
    "pyproject.toml" + 测试配置,
    "Cargo.toml",
    "go.mod",
    "pom.xml",
    "build.gradle[.kts]",
    "test/ 目录"
  ]
  hitCount = 0
  for check in checks:
    if exists(check): hitCount++
  return hitCount > 0  // 至少 1 个模块命中 → 可测
```

- 守卫通过(≥1 命中) → 进入步骤 4.8 按需写单测
- 守卫未通过(0 命中) → 跳过单测,记录原因

#### 4.8 按需写单测(新增)

> 根据任务类型自动判定是否需要写单测。

```
function shouldWriteUnitTest(taskType, files):
  if taskType == "文档" or taskType == "配置/类型定义":
    return "NO"  // 不写单测,写占位说明
  if taskType == "函数级代码":
    return "YES"  // 写单测并跑通
  return "NO"  // 默认不写
```

- 判定为"YES" → 使用语言感知的测试框架,编写覆盖关键路径的单元测试
- 判定为"NO" → 在 TASK-N.md 中写占位说明(如"不适用:文档类型任务")
- 测试失败 → 进入步骤 4.11 错误修复循环

#### 4.9 编译验证

1. 使用语言感知的构建命令(参考 `languages/<lang>.md §2`)
2. `Bash` 执行构建
3. 记录到 `compile-and-run.md`
4. 失败 → 进入步骤 4.11 错误修复循环

#### 4.10 运行验证

1. 使用语言感知的运行命令(参考 `languages/<lang>.md §4`)
2. 启动运行,验证功能正常
3. 记录到 `compile-and-run.md`
4. 失败 → 进入步骤 4.11 错误修复循环

#### 4.11 测试验证(若适用)

1. 使用语言感知的测试命令(参考 `languages/<lang>.md §3`)
2. 执行测试,确保通过
3. 记录到 `test-results.md`
4. 失败 → 进入步骤 4.11 错误修复循环

#### 4.12 逻辑行统计(新增)

> 统计本任务变更文件的逻辑行,供 CHECK 阶段"代码行数超标"检查使用。

1. 检测统计工具:`tokei` > `cloc` > heuristic(按行计数)
2. 变更文件:`git diff --name-only HEAD~1`(非 git 仓库 → 跳过)
3. 在 TASK-N.md 中记录:
   - 单文件总逻辑行
   - 单文件新增逻辑行
4. 阈值:单文件总逻辑行 500 / 单文件新增逻辑行 200(可从 REQUIRE.md 覆盖)

### 步骤 5 — 撰写 TASK-N.md

按 `templates/TASK.md` 结构生成:

```
# TASK-<序号> — <任务标题>

## 1. 任务概述
- 所属需求: <REQ-NNNNN>
- 任务类型: <新增/修改/删除>
- 涉及文件: <文件列表>

## 2. 改动内容
- <文件路径>: <改动说明>
  - 关键逻辑: <核心实现描述>

## 3. 关键决策
- <决策 1>: <说明>
- <决策 2>: <说明>

## 4. 验证结果
- 编译: <通过/失败>
- 运行: <通过/失败>
- 测试: <通过/失败/不适用>
- 逻辑行统计: <总行数>/<新增行数>

## 5. 变更记录
| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
```

> **约束**:TASK-N.md 中"关键逻辑"描述不得包含需求/缺陷/任务编号;使用功能描述替代。

### 步骤 6 — 更新 PLAN.md

更新 PLAN.md 中本任务的状态:
- 开发状态:进行中 → 已完成

### 步骤 7 — 错误修复循环(增强)

```
loop:
  if 编译/启动/测试 有错误:
    // 区分错误类型
    if 代码 bug:
      → 修代码 → 重跑
    if 设计缺陷:
      → 记入 deviations.md → 停下询问用户
    if 环境/依赖问题:
      → 尝试解决 → 记入 work-log.md
  else: 跳出循环
最多连续失败 5 次后必须停下询问用户
```

- 代码 bug:逻辑错误、语法错误、空指针等 → 自行修复
- 设计缺陷:方案本身有问题,需调整设计 → 记录到 deviations.md,停下询问
- 环境/依赖问题:缺少依赖、版本不匹配 → 尝试解决,记入 work-log.md

## 阶段完成确认

> 三态确认模型:阶段边界确认由 `--confirm`/`--auto`/默认 控制。详见 common.md §4、§7、§11。

### 任务间确认

`--confirm` 模式下每个任务完成后弹出确认:
```
任务完成: TASK-<序号> · <标题>
编译: <通过> / 运行: <通过> / 测试: <通过>
选项:
A. 继续下一个任务(推荐)
B. 中止
```

`--auto` 模式和默认模式下任务间自动继续(无确认)。

### 全部任务完成后

`--confirm` 模式下弹出增强确认:
```
=== code-req --confirm: CODING 阶段完成 ===
<N> 任务全部完成

产出物文件:
  - req/<REQ>/TASK-*.md(所有任务文件)

你可以手动修改上述文件,完成后选择:
A. 继续(重新读取产出物,获取最新修改,进入 CHECK 阶段)
B. 中止(保存当前进度,退出)
```

`--auto` 模式和默认模式下自动进入 CHECK 阶段。

## 跳过规则

- 类型为"删除"的任务在 CODING 阶段跳过(由最后的清理任务统一处理)
- 开发状态为"已完成"的任务跳过
- 前置任务未完成的任务跳过(告警)

## 语言适配文件索引

> 以下语言适配文件在步骤 4.2 中按需加载。

| 语言 | 文件 | 检测标志 |
| --- | --- | --- |
| Go | `references/languages/go.md` | `go.mod` |
| Python | `references/languages/python.md` | `pyproject.toml` / `setup.py` |
| Node.js | `references/languages/nodejs.md` | `package.json` |
| Rust | `references/languages/rust.md` | `Cargo.toml` |
| Java (Gradle) | `references/languages/java-gradle.md` | `build.gradle[.kts]` |
| Java (Maven) | `references/languages/java-maven.md` | `pom.xml` |