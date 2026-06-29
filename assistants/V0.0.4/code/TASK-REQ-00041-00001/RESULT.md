# 改修总结 — TASK-REQ-00041-00001

## 1. 任务信息
- **任务编码**:TASK-REQ-00041-00001
- **标题**:[架构] 建立 references/ 框架 + 语言检测逻辑 + common.md 模板
- **类型**:新增
- **触发/来源**:需求新增
- **来源 PLAN.md**:`./assistants/V0.0.4/plan/REQ-00041/PLAN.md`

## 2. 改修内容总览
- **新增文件**:28 个(4 个 references/ 目录 × 7 个文件)
- **修改文件**:无(本任务为新建,不修改既有文件)
- **删除文件**:无

## 3. 详细改动

### 3.1 code-design/references/(7 文件)
- `common.md`:15 章节通用流程细节(步骤 0a-15 共 15 个 §)
- `nodejs.md`:7 章节 Node.js 项目差异说明
- `python.md`:7 章节 Python 项目差异说明
- `rust.md`:7 章节 Rust 项目差异说明
- `go.md`:7 章节 Go 项目差异说明
- `java-maven.md`:7 章节 Java(Maven) 项目差异说明
- `java-gradle.md`:7 章节 Java(Gradle) 项目差异说明

### 3.2 code-plan/references/(7 文件)
- `common.md`:15 章节(任务拆分原则/PLAN.md 撰写规范/双状态管理等)
- 6 语言文档:同 code-design 模式,内容侧重实现细节探索

### 3.3 code-it/references/(7 文件)
- `common.md`:15 章节(前置任务守卫/编码原则/可测性守卫/按需写单测/错误修复循环等)
- 6 语言文档:同 code-design 模式,内容侧重构建/测试/运行命令

### 3.4 code-check/references/(7 文件)
- `common.md`:15 章节(14 维评审维度/整版本模式/派生任务/评审清单等)
- 6 语言文档:同 code-design 模式,内容侧重语言特定评审项

## 4. 关键决策与权衡
- **语言检测算法**:嵌入在 code-design/references/common.md §6,按优先级 Glob 描述文件
- **语言文档策略**:code-design 的语言文档包含完整内容,其他 3 技能复制骨架(任务 2-5 将填充)

## 5. 偏离设计/规范
- 无偏离

## 6. 验证结果
- 4 个 references/ 目录各含 7 个文件(共 28 个) ✓
- 每个 common.md 包含 15 个章节 ✓
- 每个语言文档包含 7 个章节 ✓
- 语言检测算法在 common.md §6 中定义 ✓

## 7. 已知问题/未完成项
- 其他 3 技能的语言文档内容为 code-design 的副本,任务 2-5 将填充各自技能特定的内容

## 8. 关联任务与提交
- 前置任务:无
- 后置任务:TASK-REQ-00041-00002 ~ 00005
- 提交:待末尾兜底提交