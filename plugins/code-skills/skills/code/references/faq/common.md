# 公共流程 — `/code faq`

> 本文件为 `/code faq` 子命令提供参数解析、查询搜索、导出处理的详细流程。始终加载。

## 参数解析

### 解析算法

```
function parseArgs(userInput):
  result = { mode: null, query: "", reqNum: null, outputPath: null, summary: false, templatePath: null }

  // 1. 检测导出参数
  if userInput contains "--require":
    result.mode = "EXPORT_REQUIRE"
    result.reqNum = extractReqNum(userInput)  // REQ-NNNNN
    result.outputPath = extractOutputPath(userInput)
  else if userInput contains "--design":
    result.mode = "EXPORT_DESIGN"
    result.reqNum = extractReqNum(userInput)
    result.outputPath = extractOutputPath(userInput)
  else:
    result.mode = "QUERY"
    result.query = userInput.trim()  // 整段视为查询词

  // 2. 检测辅助参数
  if userInput contains "--summary":
    result.summary = true  // 仅 --design 时生效
  if userInput contains "--template":
    result.templatePath = extractTemplatePath(userInput)

  return result
```

### 参数冲突处理

| 冲突 | 处理 |
| --- | --- |
| `--require` + `--design` 同时 | 屏显 `⚠ 不支持同时导出需求和设计,请分别执行`,退出 |
| `--summary` + `--require` | 屏显 `⚠ --summary 仅对 --design 有效,已忽略`,继续 |
| `--template` 无 `--require`/`--design` | 屏显 `⚠ --template 需与 --require 或 --design 配合使用,已忽略`,继续 |
| 无查询词 + 无导出参数 | 屏显用法示例,退出 |

## 查询模式

### 搜索范围

```
function determineSearchScope():
  hasCurrentVersion = exists("assistants/.current-version")

  if hasCurrentVersion:
    version = Read("assistants/.current-version").trim()
    return {
      primary: ["assistants/{version}/req/*/REQUIRE.md", "assistants/{version}/fix/*/BUG.md"],
      fallback: ["assistants/*/req/*/REQUIRE.md", "assistants/*/fix/*/BUG.md"]
    }
  else:
    return {
      primary: ["assistants/*/req/*/REQUIRE.md", "assistants/*/fix/*/BUG.md"],
      fallback: []
    }
```

### 搜索策略

1. **Glob 列出所有文档**:
   - `Glob "./assistants/*/req/*/REQUIRE.md"` — 需求文档
   - `Glob "./assistants/*/fix/*/BUG.md"` — 缺陷文档
   - `Glob "./assistants/*/req/*/DESIGN.md"` — 设计文档(辅助)

2. **Grep 关键词匹配**:
   - 在列出的文档中 `Grep` 查询词(模糊匹配)
   - 匹配:文档标题(H1)、需求概述章节、FR 章节标题、缺陷描述章节

3. **相关性排序**:
   - 标题匹配 > 概述匹配 > FR/缺陷描述匹配
   - 当前版本 > 其他版本
   - 最近修改 > 较早修改

### 搜索结果提取

对每个匹配文档,提取:

| 字段 | 来源 | 提取方式 |
| --- | --- | --- |
| 标题 | REQUIRE.md H1 / BUG.md H1 | 正则 `^# .+ — (.+)$` |
| 版本号 | 文件路径 | 解析 `assistants/<版本号>/...` |
| 编号 | 文件路径 | 解析 `req/<REQ-NNNNN>` 或 `fix/<BUG-NNNNN>` |
| 摘要 | 需求概述 / 缺陷描述 | 读取前 5 行 |

### 深度读取

对排名前 3 的结果:

1. `Read` 完整文档
2. 提取:
   - **需求**:FR 列表(## 3. 功能需求(FR))、NFR 列表(## 4. 非功能需求(NFR))、AC 列表(## 5. 验收标准(AC))
   - **缺陷**:缺陷描述、触发条件、可能成因、影响范围
3. 标注来源路径

### 回答组装

```
## 查询结果: "<查询词>"

### <标题> (<版本号> · <编号>)
**类型**:需求/缺陷
**摘要**:<概述核心信息>
**关键点**:
- FR-1: ...
- FR-2: ...
**来源**:`assistants/<版本号>/req/<编号>/REQUIRE.md`

### ...
```

- 若结果 > 5 条 → 先展示前 3 条,末尾提示"还有 N 条结果,请缩小查询范围"
- 若结果 = 0 → 提示"未找到匹配结果,请尝试不同关键词或调 `/code req` 创建新需求"

## 导出模式

### 源文档定位

```
function locateSourceDoc(mode, reqNum, version):
  if mode == "EXPORT_REQUIRE":
    path = "assistants/{version}/req/{reqNum}/REQUIRE.md"
  else if mode == "EXPORT_DESIGN":
    path = "assistants/{version}/req/{reqNum}/DESIGN.md"

  if not exists(path):
    print("⚠ 源文档不存在:" + path)
    exit(1)

  return path
```

### 概要提取(--summary)

仅对 `--design` 模式生效:

```
function extractSummary(designContent):
  sections = parseSections(designContent)

  result = {
    title: sections["设计概述"],      // 设计概述
    overview: sections["设计概述"],   // 设计概述 全文
    modules: sections["模块拆分"],    // 模块拆分,仅模块名+职责
    decisions: sections["方案选型"],  // 方案选型,保留完整决策
  }

  // 去掉详细接口签名/数据结构/算法伪代码
  if result.modules:
    result.modules = stripDetailedInterfaces(result.modules)

  return formatSummary(result)
```

### 概要信息格式

```
# 概要设计 — <REQ-NNNNN> · <标题>

## 设计概述
<DESIGN.md 设计概述 全文>

## 模块拆分
| 模块 | 职责 |
| --- | --- |
| ... | ... |

## 关键决策
<DESIGN.md 方案选型 全文,每个决策含:选择/备选/理由/权衡>
```

### 模板填充

```
function fillTemplate(templateContent, sourceContent):
  placeholders = scanPlaceholders(templateContent)  // {{...}}
  data = extractData(sourceContent)  // 从源文档提取结构化数据

  for each placeholder:
    if placeholder in data:
      templateContent = replace(templateContent, placeholder, data[placeholder])

  return templateContent
```

### 写出文件

```
function writeExport(outputPath, content):
  dir = dirname(outputPath)
  if not exists(dir):
    Bash: mkdir -p {dir}

  Write(outputPath, content)

  print("✓ 导出完成: " + outputPath + " (" + countLines(content) + " 行)")
```

## 模板占位符映射表

> 本表定义 `--template` 模式下支持的占位符及其数据来源。

### 需求导出(--require)占位符

| 占位符 | 来源 | 说明 |
| --- | --- | --- |
| `{{REQ_ID}}` | REQUIRE.md 文档头 | 需求编号 |
| `{{REQ_TITLE}}` | REQUIRE.md H1 | 需求标题 |
| `{{需求概述}}` | REQUIRE.md ## 1. 需求概述 | 需求概述全文 |
| `{{FR_LIST}}` | REQUIRE.md ## 3. 功能需求(FR)(或锚点 `<!-- code-skills:field=FR_LIST -->`) | 功能需求列表 |
| `{{NFR_LIST}}` | REQUIRE.md ## 4. 非功能需求(NFR)(或锚点 `<!-- code-skills:field=NFR_LIST -->`) | 非功能需求列表 |
| `{{AC_LIST}}` | REQUIRE.md ## 5. 验收标准(AC)(或锚点 `<!-- code-skills:field=AC_LIST -->`) | 验收标准列表 |
| `{{关联需求}}` | REQUIRE.md ## 6. 关联需求(或锚点 `<!-- code-skills:field=RELATED -->`) | 关联需求列表 |
| `{{待澄清}}` | clarifications.md | 待澄清项列表 |

### 设计导出(--design)占位符

| 占位符 | 来源 | 说明 |
| --- | --- | --- |
| `{{REQ_ID}}` | DESIGN.md 文档头 | 需求编号 |
| `{{REQ_TITLE}}` | DESIGN.md H1 | 设计标题 |
| `{{设计概述}}` | DESIGN.md 设计概述 | 设计概述全文 |
| `{{模块列表}}` | DESIGN.md 模块拆分 | 模块拆分列表 |
| `{{接口列表}}` | DESIGN.md 接口设计 | 接口设计列表 |
| `{{数据结构}}` | DESIGN.md 数据设计 | 数据设计全文 |
| `{{方案选型}}` | DESIGN.md 方案选型 | 方案选型全文 |
| `{{关键流程}}` | DESIGN.md 关键流程 | 关键流程全文 |

### 概要导出(--design + --summary)占位符

| 占位符 | 来源 | 说明 |
| --- | --- | --- |
| `{{REQ_ID}}` | DESIGN.md 文档头 | 需求编号 |
| `{{REQ_TITLE}}` | DESIGN.md H1 | 设计标题 |
| `{{设计概述}}` | DESIGN.md 设计概述 | 设计概述全文 |
| `{{模块概要}}` | DESIGN.md 模块拆分(精简) | 仅模块名+职责 |
| `{{关键决策}}` | DESIGN.md 方案选型 | 方案选型全文 |

### 边界与异常

- **E-1**:模板无占位符 → 把源文档完整内容追加到模板末尾
- **E-2**:占位符未识别 → 已识别的替换,未识别的保留原样 `{{...}}`
- **E-3**:模板文件 > 1MB → 屏显 `⚠ 模板文件过大,仍继续`
- **E-4**:输出路径 `../` 跳出工作空间 → 屏显 `⚠ 输出路径不安全`,跳过
- **E-5**:输出路径含通配符 → 屏显 `⚠ 输出路径不支持通配符`,跳过