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
- 当前项目代码:CWD 下的源文件

## 输出

每个任务产出:`req/<REQ-NNNNN>/TASK-<序号>.md`
代码变更:CWD 下的实际代码改动

## 工作流程

### 步骤 1 — 解析任务列表

从 PLAN.md 任务总览表中提取任务列表:

```
function parseTaskList(planMd):
  tasks = []
  for row in planMd.taskTable:
    if row.type != "删除":  // 删除任务在 TASK-010 统一处理
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

### 步骤 2 — 前置任务守卫

对当前任务,检查所有前置任务是否已完成:

```
function guardPredecessors(task, planMd):
  for dep in task.deps:
    depTask = findTask(planMd, dep)
    if depTask.status != "已完成":
      print("前置任务未完成: ${dep}")
      return false
  return true
```

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

#### 4.2 探索项目代码

- `Glob` 探索本任务涉及的文件
- `Grep` 搜索关键函数/类/接口
- `Read` 读取需要修改的文件

#### 4.3 实施编码

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

#### 4.4 修改文件前重读

> 修改任何文件前,必须先 `Read` 该文件的最新内容,确保基于最新版本编辑。

#### 4.5 编译验证

1. 检测构建命令(按项目类型)
2. `Bash` 执行构建
3. 失败 → 错误修复循环(最多 5 次)

#### 4.6 运行验证

1. 检测运行命令
2. 启动运行,验证功能正常
3. 失败 → 错误修复循环

#### 4.7 测试验证(若适用)

1. 检测测试框架
2. 按需编写单元测试
3. 执行测试,确保通过
4. 失败 → 错误修复循环

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

## 5. 变更记录
| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
```

> **约束**:TASK-N.md 中"关键逻辑"描述不得包含需求/缺陷/任务编号;使用功能描述替代。

### 步骤 6 — 更新 PLAN.md

更新 PLAN.md 中本任务的状态:
- 开发状态:进行中 → 已完成

### 步骤 7 — 错误修复循环

```
loop:
  if 编译/启动/测试 有错误:
    - 代码 bug → 修代码 → 重跑
    - 设计缺陷 → 记入 LOG.md,停下询问
    - 环境/依赖问题 → 尝试解决,记入 LOG.md
  else: 跳出循环
最多连续失败 5 次后必须停下询问用户
```

## 非 --auto 模式确认

### 任务间确认

每个任务完成后弹出确认:
```
任务完成: TASK-<序号> · <标题>
编译: <通过> / 运行: <通过> / 测试: <通过>
选项:
A. 继续下一个任务(推荐)
B. 暂停
C. 取消
```

### 全部任务完成后

```
CODING 阶段完成: <N> 任务全部完成
自动进入 CHECK 阶段
```

## 跳过规则

- 类型为"删除"的任务在 CODING 阶段跳过(由最后的清理任务统一处理)
- 开发状态为"已完成"的任务跳过
- 前置任务未完成的任务跳过(告警)