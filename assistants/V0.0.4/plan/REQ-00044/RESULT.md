# 详细设计 — REQ-00044 · 技能系统 v2 大改版

> 上游:`./assistants/V0.0.4/require/REQ-00044/RESULT.md` + `./assistants/V0.0.4/design/REQ-00044/RESULT.md`
> 遵循规范:`./assistants/rules/`(若存在)

## 文档头
- 需求编码:REQ-00044
- 所属版本:V0.0.4
- 状态:已完成
- 创建:2026-06-30 00:00

## 1. 改动范围

| 变更类型 | 数量 | 说明 |
| --- | --- | --- |
| 新增技能目录 | 4 | code-ver, code-req, code-fix, code-faq |
| 适配技能目录 | 3 | code-rule, code-merge, code-dashboard |
| 删除技能目录 | 10 | code-require/design/plan/it/check/auto/version/publish/init/answer |
| 更新规范文件 | 4 | encoding-conventions, skill-conventions, directory-conventions, dashboard-conventions |
| 更新配置文件 | 2 | plugin.json, marketplace.json |
| 新增模板文件 | 8 | REQUIRE.md, DESIGN.md, PLAN.md, TASK.md, CHECK.md, PROCESS.md, LOG.md, BUG.md |

## 2. 逐模块详细设计

### 2.1 code-ver (版本管理)

**SKILL.md 核心结构**:
```
---
name: code-ver
description: 版本管理。合并 code-version + code-publish + code-init 能力。
 新项目自动初始化;已初始化项目切换版本;当前版本未发布时询问是否先发布再切换。
---

# code-ver — 版本管理

## 工作流程
### 步骤 0 — 场景检测
1. 检测 assistants/ 目录是否存在
   - 不存在 → 新项目初始化(步骤 1A-5A)
   - 存在 → 版本切换(步骤 1B-4B)

### 步骤 1A — 新项目初始化(扫描代码)
### 步骤 2A — 登记基线需求
### 步骤 3A — 生成 INIT-REPORT.md
### 步骤 4A — 创建基线版本
### 步骤 5A — 创建 .current-version

### 步骤 1B — 版本切换:读当前版本
### 步骤 2B — 检查是否需要发布
### 步骤 3B — 执行发布(若用户选择)
### 步骤 4B — 切换到目标版本
```

**关键算法 — 场景检测**:
```
function detectScenario():
  if not exists("assistants/"):
    return "INIT"  // 新项目初始化
  if not exists("assistants/.current-version"):
    return "INIT"  // 有目录但无版本标记,补初始化
  return "SWITCH"  // 正常版本切换
```

### 2.2 code-req (需求开发)

**SKILL.md 核心结构**:
```
---
name: code-req
description: 需求开发全流程。合并 code-require+design+plan+it+check(需求路径)。
 默认交互确认,--auto 静默执行,支持 PROCESS.md 断点续跑。
---

# code-req — 需求开发

## 参数解析
- <需求描述> | <REQ-NNNNN>  (必填)
- --auto                       (可选,静默模式)

## 工作流程
### 步骤 0 — 版本检测 + 恢复执行
### 步骤 1 — REQUIRE 阶段(需求分析)
### 步骤 2 — DESIGN 阶段(软件设计)
### 步骤 3 — PLAN 阶段(任务排期)
### 步骤 4 — CODING 阶段(编码执行,循环 TASK-N)
### 步骤 5 — CHECK 阶段(代码审查)
### 步骤 6 — DONE(完成)
```

**关键算法 — 阶段执行器**:
```
async function executeStage(stage, context, autoMode):
  // 1. 追加 PROCESS.md 开始记录
  appendProcess(stage, "开始")
  
  // 2. 执行阶段逻辑
  result = await stageHandlers[stage](context)
  
  // 3. 追加 PROCESS.md 完成记录
  appendProcess(stage, "完成", result.summary)
  
  // 4. 交互确认(非 --auto 模式)
  if not autoMode:
    askUserQuestion("阶段完成,是否继续?")
  
  return result
```

**PROCESS.md 追加算法**:
```
function appendProcess(stage, status, summary = ""):
  line = `| ${now()} | ${stage} | ${status} | ${summary} |`
  // 追加式写入,不预读
  Bash: echo "line" >> PROCESS.md
```

### 2.3 code-fix (缺陷修复)

**SKILL.md 核心结构**:与 code-req 类似,差异:
- 第 0 阶段为 `INIT`(缺陷登记,产出 `BUG.md`)
- 其余阶段复用 code-req 的 references
- 输出目录为 `fix/<BUG-NNNNN>/`

**关键差异**:
```
code-req:  INIT → REQUIRE → DESIGN → PLAN → CODING → CHECK → DONE
code-fix:  INIT(登记BUG.md) → DESIGN → PLAN → CODING → CHECK → DONE
           ↑ 差异:登记 BUG.md 而非 REQUIRE.md
```

**复用 code-req references**:
```
code-fix/references/design.md → 引用 ../code-req/references/design.md
code-fix/references/plan.md   → 引用 ../code-req/references/plan.md
code-fix/references/coding.md → 引用 ../code-req/references/coding.md
code-fix/references/check.md  → 引用 ../code-req/references/check.md
```

### 2.4 code-faq (知识查询)

**参数解析**:
```
--require <路径>  → 导出需求文档(REQUIRE.md → 指定路径)
--design <路径>   → 导出详细设计(DESIGN.md → 指定路径)
--summary         → 与 --design 配合,导出概要设计
--template <路径> → 指定导出模板
```

**导出算法**:
```
function exportDocument(source, target, mode, templatePath = null):
  content = Read(source)
  if mode == "SUMMARY":
    content = extractSummary(content)  // 从 DESIGN.md 提取概要信息
  if templatePath:
    template = Read(templatePath)
    content = fillTemplate(template, content)
  Write(target, content)
```

### 2.5 保留技能适配

**code-rule**: 读取路径从旧结构更新为新结构(`req/`/`fix/`)
**code-merge**: 读取 `PROCESS.md` 确认进度,读取 `req/`/`fix/` 下的文档
**code-dashboard**: 解析简化版 `RESULT.md`(仅 2 区段:需求清单/缺陷清单),读取 `PROCESS.md` 获取进度

### 2.6 规范文件更新

**encoding-conventions.md**:
- 更新目录结构示例:旧 `require/`/`design/`/`plan/` → 新 `req/`/`fix/`
- 更新文档命名示例:旧 `RESULT.md`/`PLAN.md` → 新 `REQUIRE.md`/`DESIGN.md`/`CHECK.md`

**skill-conventions.md**:
- 更新技能名列表:14 → 7
- 更新文件引用路径

**directory-conventions.md**:
- 更新为 `req/`+`fix/` 两大目录结构

**dashboard-conventions.md**:
- 更新看板解析锚点:从 3 区段简化为 2 区段

### 2.7 配置文件更新

**plugin.json**: 更新 `skills` 字段,列出 7 个新技能
**marketplace.json**: 更新 `plugins[].skills` 列表

## 3. 模板详细设计

### REQUIRE.md 模板章节
```
# 需求分析 — <REQ-NNNNN> · <标题>
## 1. 需求概述
## 2. 背景与目标
## 3. 功能需求(FR)
## 4. 非功能需求(NFR)
## 5. 验收标准(AC)
## 6. 关联需求
## 7. 变更记录
```

### DESIGN.md 模板章节
```
# 软件设计 — <REQ-NNNNN> · <标题>
## 1. 设计概述
## 2. 模块拆分
## 3. 接口设计
## 4. 数据设计
## 5. 关键流程
## 6. 方案选型
## 7. 规范合规
## 8. 变更记录
```

### PLAN.md 模板章节
```
# 任务排期 — <REQ-NNNNN> · <标题>
## 任务总览
## 任务依赖
## 里程碑
## 任务详情
```

### TASK.md 模板章节
```
# TASK-<序号> — <任务标题>
## 1. 任务概述
## 2. 改动内容
## 3. 关键决策
## 4. 验证结果
```

### CHECK.md 模板章节
```
# 代码审查 — <REQ-NNNNN> · <标题>
## 评审维度
## 发现汇总
## 评审结论
```

### PROCESS.md 模板
```
# 执行进程 — <REQ-NNNNN>
| 时间 | 阶段 | 状态 | 摘要 |
| --- | --- | --- | --- |
```

### BUG.md 模板章节
```
# 缺陷分析 — <BUG-NNNNN> · <标题>
## 1. 缺陷描述
## 2. 触发条件
## 3. 可能成因
## 4. 影响范围
## 5. 变更记录
```

## 4. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-30 00:00 | v1 | 初始创建 | 详细设计完成,7 模块 / 8 模板 | wangmiao |