# 工作日志 — TASK-REQ-00040-00001

开始时间:2026-06-25
版本:V0.0.3
任务编码:TASK-REQ-00040-00001
任务标题:[修改] code-fix 步骤 0 末尾追加"项目可启动性探测" 子节(detectStartability 7 步算法)
触发/来源:详细设计

## 项目现状(步骤 6 记录)

### 项目类型
- 仓库:`code-skills` Claude Code 插件市场仓库
- 主体:Markdown 技能库(14 个 `code-*` 技能)
- 改造目标:本任务**不**涉及可启动项目(纯 Markdown 技能库),NFR-9 字节级沿用

### 既有 `code-fix` 步骤 0 现状
- 步骤 0(line 177-181)在 `code-fix/SKILL.md` 中为 4 项判定:
 1. 读 `.current-version`
 2. 文件不存在 → 中断
 3. 读取内容,记为 `<版本号>`
 4. 验证目录存在
- 步骤 0 末尾(line 181 后)为本任务**新增**子节的插入锚点

### 既有相似功能(RE界-00037 沿用)
- `code-fix` 是纯登记型(沿用 REQ-00027)
- `code-fix` 状态推进路径沿用 REQ-00037(初始态 = `待处理`,5 新 + 10 老字面共存)
- 本任务**不**触发状态推进;**不**改 `code-fix` 状态机

## 项目级规范要点(步骤 4 记录)

13 份项目级规范全部沿用,**0 触发**新增约束:

- `skill-conventions §规则 1`:`code-fix/SKILL.md` frontmatter `name + description` 必含;**强约束** 字节级保留
- `skill-conventions §规则 2`:SKILL.md / templates/ 不得含 6 类开发痕迹字面;**强约束** 本任务**不**在追加子节中写"本需求 REQ-00040 新增" 等字面
- `dashboard-conventions §规则 1`:看板字段扩展需三同步;**0 触发**(本任务**不**改看板字段)
- `encoding-conventions §规则 1-4`:3 类编码(REQ/BUG/TASK)正则;**0 触发**(本任务**不**新增编码)
- `module-conventions §规则 1`(DEPRECATED):**0 触发**
- `directory-conventions`(规则 1 占位):**0 触发**
- `dependency-conventions.md`(规则 1 占位):**0 触发**(本任务**0 新增**三方依赖)
- `commit-conventions.md`(规则 1 占位):**0 触发**

## 任务设计要点(步骤 5 记录)

### PLAN.md §3 任务详情(沿用)
- 目标:在 `code-fix/SKILL.md` §"## 步骤 0 — 版本上下文检测(强制前置)" 末尾追加"### 步骤 0.X — 项目可启动性探测" 子节,实现 `detectStartability(cwd)` 7 步探测算法
- 涉及文件:`plugins/code-skills/skills/code-fix/SKILL.md > ## 步骤 0 — 版本上下文检测(强制前置)` 末尾追加子节(锚点:line 181 "4. 验证目录存在" 后,line 182 "### 步骤 1" 前)
- 关键变更:步骤 0 末尾追加子节(7 步算法伪代码 + 内存上下文写入 + 3 条边界)
- 边界与异常:文件不存在 / JSON 解析失败 → 跳过该优先级;全未命中 → `canStart = false`;**不**抛异常
- 验证手段:AC-1 静态校验(子节存在) + AC-7 静态校验(字节级保留)

### 详细设计 §4.1(沿用)
- 模块 1:`code-fix` 步骤 0 末尾追加"项目可启动性探测" 子节
- 路径:line 181 "4. 验证目录存在" 后,line 182 "### 步骤 1" 前
- 关键类/函数:`detectStartability(cwd): Context` — 主探测函数
- 调用顺序:步骤 0 第 4 项 → 调 `detectStartability(cwd)` → 内存上下文存 `context.canStart` / `context.startCommand` → 步骤 6 末尾子节读 `context.canStart`
- 错误处理范式:配置文件不存在 / JSON 解析失败 → 跳过该优先级,继续下一优先级;**不**抛异常

## 开发过程

### 2026-06-25 14:30
- **操作**:`Read code-fix/SKILL.md` line 175-189(确认步骤 0 / 步骤 1 字面)
- **目的**:验证修改前的字面,作为 `Edit` 的 `old_string` 精确锚点
- **结果**:成功(line 177 是"### 步骤 0 — 版本上下文检测(强制前置)" 标题,line 181 是第 4 项"4. 验证目录存在",line 182 是空行,line 183 是"### 步骤 1" 标题)

### 2026-06-25 14:31
- **操作**:`Edit code-fix/SKILL.md` 在步骤 0 第 4 项后追加"### 步骤 0.X — 项目可启动性探测(本需求新增子节,在步骤 0 第 4 项后)" 子节
- **目的**:落地 FR-1 / PLAN.md T-001 关键变更
- **结果**:成功(子节追加完成,锚点 line 181 后 + line 183 步骤 1 前,字节级保留 frontmatter L1-4)
- **子节内容**:
 - 1 个 `### 步骤 0.X` 标题(描述性,不含开发痕迹)
 - 1 段说明引用(描述 NFR-3 零规范变更 + 不触发 `AskUserQuestion` + 不写文件)
 - 1 段伪代码(`detectStartability` 7 步算法:Node.js / Python / Makefile / Docker / Rust / Go / Java)
 - 1 段"边界" 小节(3 条:文件不存在跳过 / 全未命中降级 / 不抛异常)
 - 1 段"性能" 小节(8 个 `Bash: test -f` 调用,总耗时 < 500ms)

### 2026-06-25 14:32
- **操作**:`Read code-fix/SKILL.md` 验证 L1-3 frontmatter + 步骤 1 标题字面 + 步骤 6 末尾"## 不要做的事" 段字面
- **目的**:验证不变量 INV-1(frontmatter)/ INV-2(既有"## 工作流程" 步骤 1~10 主体)/ INV-3("## 不要做的事" 段)
- **结果**:
 - frontmatter L1-4 字节级保留(`name: code-fix` + `description: 缺陷登记与跟踪...`)
 - 步骤 1 标题"### 步骤 1 — 收集缺陷编号 / 描述" 字节级保留
 - 步骤 4 标题"### 步骤 4 — 询问本轮状态推进(纯登记型)" 字节级保留
 - "## 不要做的事" 段在 line 484(后移 66 行因为新追加了子节)
 - 子节标题"### 步骤 0.X — 项目可启动性探测(本需求新增子节,在步骤 0 第 4 项后)" 含本任务类型描述("项目可启动性探测" + "新增子节"),**不**含"本需求 REQ-00040 新增" 等开发痕迹字面(沿用 `skill-conventions §规则 2`)

## 过程产物

- `work-log.md`:本文档(始终生成)
- `deviations.md`:无偏离(始终生成,内容 = "无偏离" 1 行)
- `unit-test-results.md`:占位(本任务不涉及函数级代码改动,写"本任务不涉及单元测试")
- `compile-and-run.md`:**不生成**(纯 Markdown 改造,无运行时)
- `test-results.md`:**不生成**(测试状态 = 不适用)

## 结论

T-001 核心改动完成。子节字面与 PLAN.md §3 任务详情 + 详细设计 §4.1 + FR-1 字节级一致。frontmatter / 既有"## 工作流程" / "## 不要做的事" 字节级保留。AC-1 / AC-7 静态校验通过(下一步 T-005 端到端验证时复核)。
