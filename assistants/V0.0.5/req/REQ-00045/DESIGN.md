# 软件设计 — REQ-00045 · 补充 REQ-00044 重构后丢失的旧技能能力

> 所属版本:V0.0.5
> 创建时间:2026-06-30 19:40

## 1. 设计概述

本需求对 `code-req` 技能进行增量补全,不改变现有架构,仅在现有 references 中追加新章节、新增 `languages/` 子目录、在 SKILL.md 中追加引用。核心思路:

- **新增语言适配层**:在 `references/languages/` 下创建 6 个语言文件,CODING/CHECK 阶段按需加载
- **增强 CHECK 阶段**:在 check.md 中增加评审-编码循环,实现"审查→改修→再审查"闭环
- **增强交互确认**:在 require.md/design.md/plan.md 中增加用户确认环节
- **补全编码能力**:在 coding.md 中增加过程文档自适应判定、可测性守卫、按需单测、逻辑行统计、错误分类、审查改修特殊规则

## 2. 模块拆分

### 2.1 新增文件

| 模块 | 职责 | 涉及文件 | 依赖 |
| --- | --- | --- | --- |
| 语言适配:Go | Go 项目识别/构建/测试/运行/编码约定 | `references/languages/go.md` | — |
| 语言适配:Python | Python 项目识别/构建/测试/运行/编码约定 | `references/languages/python.md` | — |
| 语言适配:Node.js | Node.js 项目识别/构建/测试/运行/编码约定 | `references/languages/nodejs.md` | — |
| 语言适配:Rust | Rust 项目识别/构建/测试/运行/编码约定 | `references/languages/rust.md` | — |
| 语言适配:Java(Gradle) | Gradle 项目识别/构建/测试/运行/编码约定 | `references/languages/java-gradle.md` | — |
| 语言适配:Java(Maven) | Maven 项目识别/构建/测试/运行/编码约定 | `references/languages/java-maven.md` | — |

### 2.2 修改文件

| 模块 | 职责 | 涉及文件 | 变更类型 |
| --- | --- | --- | --- |
| 编码执行阶段 | 增加语言检测/过程文档/可测性/单测/逻辑行统计/错误分类/审查改修 | `references/coding.md` | 修改(追加章节) |
| 代码审查阶段 | 增加评审-编码循环/代码行数超标维度 | `references/check.md` | 修改(追加章节) |
| 需求分析阶段 | 增加用户确认环节(clarifications.md/边界确认) | `references/require.md` | 修改(追加章节) |
| 软件设计阶段 | 增加用户确认环节(扩展性/方案选型/改修方案) | `references/design.md` | 修改(追加章节) |
| 任务排期阶段 | 增加用户确认环节(任务拆分/优先级) | `references/plan.md` | 修改(追加章节) |
| 公共流程 | 增加标题解析 | `references/common.md` | 修改(追加章节) |
| 技能入口 | 更新引用说明 | `SKILL.md` | 修改(追加内容) |

## 3. 接口设计(关键函数签名)

### 3.1 语言检测

```
function detectLanguage(projectRoot):
  // 按优先级检测语言类型
  if exists("go.mod"): return "go"
  if exists("Cargo.toml"): return "rust"
  if exists("pom.xml"): return "java-maven"
  if exists("build.gradle") or exists("build.gradle.kts"): return "java-gradle"
  if exists("pyproject.toml") or exists("setup.py") or exists("setup.cfg"): return "python"
  if exists("package.json"): return "nodejs"
  return "unknown"
```

### 3.2 评审-编码循环

```
function checkCodeLoop(reqNum, autoMode, maxRounds = 5):
  round = 0
  while round < maxRounds:
    round++
    findings = executeCheck(reqNum)
    mustFix = findings.filter(f => f.level == "必须改" && f.status != "已处理")
    if mustFix.length == 0:
      return { status: "PASS", rounds: round }
    // 生成改修任务
    newTasks = mustFix.map(f => createFixTask(f))
    appendToPlan(reqNum, newTasks)
    // 执行改修
    for task in newTasks:
      executeCoding(task)
    // 追加 PROCESS.md
    appendProcess("CHECK", "完成", "第${round}轮审查:${mustFix.length}条必须改,已生成改修任务")
  return { status: "MAX_ROUNDS", rounds: round }
```

### 3.3 可测性守卫

```
function testabilityGuard(projectRoot):
  checks = [
    "package.json" + "scripts.test",
    "pyproject.toml",
    "Cargo.toml",
    "go.mod",
    "pom.xml",
    "build.gradle",
    "test/ 目录"
  ]
  hitCount = checks.filter(c => exists(c)).length
  return hitCount > 0  // 至少 1 个命中 → 可测
```

### 3.4 单测自动判定

```
function shouldWriteUnitTest(taskType, files):
  if taskType == "文档": return "NO"
  if taskType == "配置/类型定义": return "NO"
  if taskType == "函数级代码": return "YES"
  return "NO"
```

## 4. 数据设计

### 4.1 语言适配文件结构(每个文件)

```
# <语言> 项目参考 — code-req

> 本文件为 code-req 技能提供 <语言> 项目的语言差异说明。
> 在 CODING 阶段(步骤 4.2)中,当检测到项目语言为 <lang> 时加载本文件。

## §1 项目结构识别
## §2 构建命令检测
## §3 测试框架识别
## §4 启动/运行命令检测
## §5 Monorepo 声明文件解析
## §6 编码约定
## §7 工具链检测
```

### 4.2 PROCESS.md 新增记录格式

评审-编码循环每轮追加:
```
| 2026-06-30 20:00 | CHECK | 完成 | 第1轮审查:3条必须改,已生成改修任务 TASK-REQ-00045-00010~00012 |
| 2026-06-30 20:15 | CODING | 开始 | TASK-REQ-00045-00010 开始(审查改修) |
| 2026-06-30 20:20 | CODING | 完成 | TASK-REQ-00045-00010 完成 |
| 2026-06-30 20:25 | CHECK | 完成 | 第2轮审查:0条必须改,审查通过 |
```

## 5. 关键流程

### 5.1 CODING 阶段增强流程

```
CODING 阶段:
  步骤 1: 解析任务列表
  步骤 2: 前置任务守卫(增强:按文件行序判定,未完成→中止)
  步骤 3: 任务循环
    步骤 3.1: 检测项目语言类型 → 加载 languages/<lang>.md
    步骤 3.2: 读取设计参考
    步骤 3.3: 探索项目代码
    步骤 3.4: 实施编码(含审查改修特殊规则)
    步骤 3.5: 过程文档自适应判定(compile-and-run/unit-test/deviation/process-doc)
    步骤 3.6: 项目可测性守卫(7 项检查)
    步骤 3.7: 按需写单测(3 类自动判定)
    步骤 3.8: 编译验证(使用语言感知的构建命令)
    步骤 3.9: 运行验证(使用语言感知的运行命令)
    步骤 3.10: 测试验证(使用语言感知的测试命令)
    步骤 3.11: 逻辑行统计(tokei > cloc > heuristic)
    步骤 3.12: 错误修复循环(区分 bug/设计缺陷/环境问题,最多 5 次)
    步骤 3.13: 撰写 TASK-N.md
  步骤 4: 更新 PLAN.md
```

### 5.2 CHECK 阶段增强流程(含评审-编码循环)

```
CHECK 阶段:
  步骤 1: 收集审查材料
  步骤 2: 逐维度审查(新增:代码行数超标维度)
  步骤 3: 分类发现
  步骤 4: 处理"必须改"
    4a. 生成改修任务,追加到 PLAN.md
    4b. 进入 CODING 阶段执行改修任务
    4c. 改修完成后重新进入 CHECK 阶段(回到步骤 1)
    4d. 循环直到无"必须改"或达到上限(5 轮)
  步骤 5: 处理"建议改"(非 --auto 确认)
  步骤 6: 撰写 CHECK.md
  步骤 7: 评审结论判定
```

### 5.3 REQUIRE 阶段增强流程(用户确认)

```
REQUIRE 阶段:
  步骤 1: 创建目录与 PROCESS.md
  步骤 2: 收集需求材料
  步骤 3: 提取需求要素
  步骤 4: 检索关联需求
  步骤 5: 与用户澄清(增强)
    5a. 需求细节澄清:对模糊/歧义/缺失的功能点,提供选项
    5b. 边界条件确认:异常路径/边界值/用户角色/权限
    5c. 每轮最多 1-3 个问题
    5d. 追加 clarifications.md 记录
  步骤 6: 撰写 REQUIRE.md(标注"待澄清"和"假设")
  步骤 7: 同步版本看板
```

### 5.4 DESIGN 阶段增强流程(用户确认)

```
DESIGN 阶段:
  步骤 1-8: 原有流程(读取需求→探索→构思→拆分→接口→数据→流程→选型)
  步骤 9: 用户确认(新增)
    9a. 扩展性确认:预留扩展点/未来变更/模块粒度
    9b. 方案选型确认:多方案时给出选项,用户选择
    9c. 改修方案确认:模块修改范围/接口变更影响/数据兼容性
  步骤 10: 撰写 DESIGN.md
```

### 5.5 PLAN 阶段增强流程(用户确认)

```
PLAN 阶段:
  步骤 1-2: 原有流程(读取设计→任务拆分)
  步骤 3: 用户确认(新增)
    3a. 任务拆分确认:粒度/依赖/里程碑
    3b. 优先级确认:排序/关键路径
  步骤 4-7: 原有流程(依赖分析→里程碑→依赖图→撰写→关联)
```

## 6. 方案选型

### 决策 D-1: 语言适配文件组织方式

- **选择**:在 `code-req/references/languages/` 下创建独立文件
- **备选**:合并到 coding.md 中作为子章节
- **选择理由**:① 与旧技能架构一致,可复用旧文件内容;② 独立文件便于按需加载,不增加 coding.md 长度;③ 可被 code-fix 复用
- **权衡**:增加 6 个文件,但每个文件不超过 60 行

### 决策 D-2: 评审-编码循环实现方式

- **选择**:在 check.md 中增加循环逻辑,CHECK 完成后检测"必须改"→生成改修任务→调用 CODING→回到 CHECK
- **备选**:在 SKILL.md 的阶段执行器中增加循环
- **选择理由**:① 循环逻辑本身是 CHECK 阶段的职责;② 保持 SKILL.md 简洁;③ 与 PROCESS.md 断点续跑兼容
- **权衡**:check.md 复杂度增加,但通过分步骤清晰描述可缓解

### 决策 D-3: 用户确认环节实现方式

- **选择**:在各阶段 references 中增加确认步骤,非 --auto 模式触发 AskUserQuestion
- **备选**:在 SKILL.md 共同执行器中增加确认步骤
- **选择理由**:① 每个阶段的确认内容不同,放在各自 references 中更清晰;② 便于 code-fix 复用
- **权衡**:references 文件长度增加,但确认步骤独立成节,不影响原有流程

### 决策 D-4: 循环上限

- **选择**:评审-编码循环最多 5 轮
- **备选**:3 轮或无限
- **选择理由**:与既有错误修复循环"最多连续失败 5 次"一致,避免无限循环
- **权衡**:5 轮后若有"必须改"仍未处理,需人工介入

## 7. 规范合规

| 规范文件 | 检查项 | 结果 |
| --- | --- | --- | --- |
| skill-conventions.md | 技能目录结构 | ✅ 新增文件在 `skills/code-req/references/` 下 |
| encoding-conventions.md | 编号格式 | ✅ 沿用 REQ-NNNNN / TASK-REQ-NNNNN-NNNNN |
| directory-conventions.md | 目录命名 | ✅ 新目录 `languages/` 符合命名规范 |

## 8. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-30 19:40 | v1 | 初始创建 | 软件设计完成,6 新增文件 / 7 修改文件 / 4 决策 | wangmiao |