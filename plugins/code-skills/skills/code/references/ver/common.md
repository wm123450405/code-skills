# 公共流程 — `/code ver`

> 本文件为 `/code ver` 子命令提供场景检测、初始化、版本切换、发布检查的详细流程。始终加载。
>
> **契约层引用**:本文件中所有"派生状态"的逻辑(§4 发布检查 / §8.6 高优先级缺陷统计)统一通过 `deriveItemStatus()` 实现,该函数定义在 `references/_shared/contracts.md` §3。`RESULT.md` 不再作为动态状态数据源(FR-1)。

## §0 派生函数引用

```
// 完整定义见 references/_shared/contracts.md §3
// 本文件不重复定义,所有调用方按契约层签名使用:
//   deriveItemStatus(reqOrBugId: string): ItemStatus
// 返回 { stage, devStatus, testStatus, completed }
// 编号不存在 → 返回 { stage: 'UNKNOWN', devStatus: 'N/A', testStatus: 'N/A', completed: false }
```

## §1 场景检测

### 检测算法

```
function detectScenario(userInput):
  // 1. 检测 assistants/ 目录
  assistantsExists = exists("assistants/")

  // 2. 检测 .current-version
  hasCurrentVersion = exists("assistants/.current-version")

  // 3. 解析用户输入
  hasVersionArg = userInput.version != null
  hasPublishFlag = userInput.flags.includes("--publish")

  // 4. 判定场景
  if hasPublishFlag:
    return "PUBLISH"

  if not assistantsExists:
    return "INIT"  // 新项目初始化

  if assistantsExists and not hasCurrentVersion:
    return "INIT"  // 有目录但无版本标记,补初始化

  if hasVersionArg:
    return "SWITCH"  // 版本切换

  // 无参数:显示开发看板
  return "DASHBOARD"
```

### 无参数时的行为

无参数 + 已初始化项目 → 显示开发看板(§8 看板模式),屏幕输出进度条 + 状态分布 + 建议。

无参数 + 未初始化项目 → 走 INIT 流程(§2)。

### 边界条件

- `assistants/` 存在但为空(无任何版本目录)→ 视为"无版本",走 INIT
- `assistants/` 存在 + 有版本目录但无 `.current-version` → 视为"部分初始化",走 INIT(补)
- 用户输入版本号但格式非法 → 报错,提示重新输入

---

## §2 新项目初始化

### §2.1 收集初始版本号

```
function collectInitialVersion():
  defaultVersion = "V0.0.0"

  AskUserQuestion:
    请输入初始版本号:
    A. V0.0.0(推荐,代表"项目当前状态")
    B. V0.1.0
    C. 自定义

  version = userAnswer

  // 校验
  validate(version):
    if empty(version): error("版本号不能为空")
    if contains(version, ["/", "\\", ":", "*", "?", "\"", "<", ">", "|"]):
      error("版本号不能包含特殊字符")
    if version in listVersions("assistants/"):
      error("版本号已存在,请选择其他版本号或先切换")

  return version
```

### §2.2 创建 assistants/ 骨架

```
function createSkeleton(version):
  dirs = [
    "assistants/",
    "assistants/rules/",
    "assistants/{version}/",
    "assistants/{version}/req/",
    "assistants/{version}/fix/",
    "assistants/{version}/publish/",
  ]

  for dir in dirs:
    if not exists(dir):
      mkdir -p dir
```

### §2.3 写入 .current-version

```
function writeCurrentVersion(version):
  Write "assistants/.current-version", content = version + "\n"
```

### §2.4 写入版本看板 RESULT.md

```
function writeDashboard(version):
  content = """
  # 版本开发进度看板 — {version}

  > 本文件是 `{version}` 版本工作空间的**单一事实来源**。
  > 由 `/code ver` 创建,`/code req` / `/code fix` 更新。

  ## 文档头
  - 版本号:`{version}`
  - 创建时间:{now}
  - 最近更新:{now}
  - 状态:活跃

  ## 需求清单

  > 写入方:`/code req`(新建需求时追加)
  > 进度通过 PROCESS.md 链接查看

  | 需求编码 | 标题 | 进度文档 |
  | --- | --- | --- |
  | — | — | — |

  **统计**:0

  ## 缺陷清单

  > 写入方:`/code fix`(登记缺陷时追加)

  | 缺陷编号 | 标题 | 进度文档 |
  | --- | --- | --- |
  | — | — | — |

  **统计**:0

  ## 变更记录

  | 时间 | 变更类型 | 变更摘要 | 关联项 |
  | --- | --- | --- | --- |
  | {now} | 初始化 | 创建版本 {version} 工作空间 | — |
  """

  Write "assistants/{version}/RESULT.md", content
```

### §2.5 分析现有代码

#### 项目类型识别

```
function detectProjectType():
  manifestFiles = [
    ("package.json", "Node.js / JS / TS"),
    ("pyproject.toml", "Python"),
    ("go.mod", "Go"),
    ("pom.xml", "Java / Kotlin (Maven)"),
    ("build.gradle", "Java / Kotlin (Gradle) / Android"),
    ("Cargo.toml", "Rust"),
    ("composer.json", "PHP"),
    ("Gemfile", "Ruby"),
    ("*.csproj", "C# / .NET"),
    ("Makefile", "C / C++ / 通用"),
    ("CMakeLists.txt", "C / C++ (CMake)"),
  ]

  for (file, type) in manifestFiles:
    if exists(file):
      return type

  return "未知类型(脚本项目 / 静态站点 / 配置文件仓库)"
```

#### 目录结构分析

```
function analyzeDirectoryStructure():
  // 限制深度 3 层,避免爆栈
  files = Glob("**/*", depth=3)
  // 重点关注:
  // - 顶层目录: src/ lib/ app/ cmd/ internal/ pkg/
  // - 配置目录: config/ configs/ .env.example
  // - 文档目录: docs/ README*
  // - 测试目录: test/ tests/ __tests__/ spec/

  return buildAsciiTree(files, maxDepth=3)
```

#### 入口与主流程

```
function findEntryPoints():
  entryPoints = []

  // 按项目类型找入口
  switch projectType:
    case "Node.js":
      pkg = Read("package.json")
      if pkg.main: entryPoints.push(pkg.main)
      if pkg.bin: entryPoints.push(...Object.values(pkg.bin))
    case "Python":
      candidates = ["__main__.py", "app.py", "main.py", "manage.py"]
      entryPoints = candidates.filter(exists)
    case "Go":
      entryPoints = Glob("cmd/*/main.go")
    case "Java":
      // Grep public static void main
      entryPoints = Grep("public static void main")
    case "Rust":
      entryPoints = ["src/main.rs"].filter(exists)

  return entryPoints
```

#### 模块识别

```
function identifyModules():
  modules = []
  // 按目录划分模块
  srcDirs = ["src/", "lib/", "app/", "internal/", "pkg/", "cmd/"]
  for dir in srcDirs:
    if exists(dir):
      subdirs = listDirs(dir)
      for subdir in subdirs:
        modules.push({
          path: subdir,
          responsibility: inferFromFiles(subdir),
          interfaces: extractExports(subdir),
          dependencies: findImports(subdir),
        })

  return modules
```

#### 数据模型识别

```
function findDataModels():
  schemas = []
  // 找 schema 文件
  schemaPatterns = [
    "**/*.sql",           // SQL schema
    "**/schema.prisma",   // Prisma
    "**/models/**/*.py",  // Django/Flask models
    "**/entities/**/*.java", // JPA entities
    "**/*.entity.ts",     // TypeORM entities
  ]

  for pattern in schemaPatterns:
    files = Glob(pattern)
    for file in files:
      schemas.push(extractEntities(file))

  return schemas
```

#### 第三方依赖识别

```
function findDependencies():
  deps = {}
  // 读清单文件的依赖段
  if exists("package.json"):
    pkg = Read("package.json")
    deps = { ...pkg.dependencies, ...pkg.devDependencies }
  if exists("pyproject.toml"):
    pyproject = Read("pyproject.toml")
    deps = parsePyprojectDeps(pyproject)
  if exists("go.mod"):
    gomod = Read("go.mod")
    deps = parseGoModRequire(gomod)
  // ... 其他清单文件

  return deps
```

#### 编码与构建约定

```
function findConventions():
  conventions = {}
  // 编码规范
  conventionFiles = [
    ".editorconfig", ".eslintrc*", ".prettierrc*",
    "tsconfig.json", "pyproject.toml [tool.ruff]",
    ".golangci.yml", "checkstyle.xml",
  ]
  // 构建约定
  buildFiles = ["Makefile", "scripts/", ".github/workflows/", "Jenkinsfile"]

  for file in conventionFiles:
    if exists(file): conventions[file] = Read(file)
  for file in buildFiles:
    if exists(file): conventions[file] = Read(file)

  return conventions
```

### §2.6 生成 INIT-REPORT.md

```
function generateInitReport(analysis, version):
  content = """
  # 功能分析报告 — {version}

  > 由 `/code ver` 在 {now} 生成,用于快速了解项目现状。

  ## 1. 项目概述
  {analysis.summary}

  ## 2. 技术栈
  - 语言:{analysis.language}
  - 框架:{analysis.framework}
  - 关键依赖:{analysis.keyDependencies}

  ## 3. 目录结构
  {analysis.directoryTree}

  ## 4. 核心模块与职责
  | 模块 | 路径 | 职责 | 对外接口 |
  | --- | --- | --- | --- |
  {analysis.modules}

  ## 5. 入口与主流程
  {analysis.entryPoints}

  ## 6. 外部接口
  {analysis.externalInterfaces}

  ## 7. 数据模型
  {analysis.dataModels}

  ## 8. 构建与运行
  {analysis.buildCommands}

  ## 9. 测试情况
  {analysis.testStatus}

  ## 10. 可复用资产
  {analysis.reusableAssets}

  ## 11. 已知问题/技术债
  {analysis.techDebt}

  ## 12. 本报告生成信息
  - 生成时间:{now}
  - 生成工具:`/code ver`
  - 覆盖源文件数:{analysis.fileCount}
  """

  Write "assistants/{version}/INIT-REPORT.md", content
```

### §2.7 生成现有功能需求清单

#### 拆分功能边界

```
function splitFeatures(analysis):
  // 拆分原则:
  // - 一个功能 = 一个用户可识别的"能力"
  // - 不按文件/类拆分(粒度太细)
  // - 不按业务域拆分(粒度太粗)

  features = []
  // 基于模块分析结果拆分
  for module in analysis.modules:
    if isUserVisibleFeature(module):
      features.push({
        id: "EXISTING-{nextId()}",
        name: module.name,
        implementation: module.path,
        interfaces: module.interfaces,
      })

  // M 的合理范围:
  // - 小项目(< 1k 行): M = 1-3
  // - 中项目(1k-10k 行): M = 3-8
  // - 大项目(> 10k 行): M = 5-15

  return features
```

#### 写每份 EXISTING-NNN/RESULT.md

```
function writeExistingRequirement(feature, version):
  content = """
  # 需求提示词文档 — EXISTING-{feature.id} · {feature.name}

  > 所属版本:{version}(基线)
  > 状态:已完成(现有功能,代码已存在)

  ## 需求概述
  {feature.description}

  ## 现有实现位置
  {feature.implementation}

  ## 用户角色与场景
  {feature.userScenarios}

  ## 功能点(FR)
  {feature.functionalRequirements}

  ## 关键接口
  {feature.interfaces}

  ## 数据模型
  {feature.dataModels}

  ## 验收标准(AC)
  {feature.acceptanceCriteria}

  ## 关联功能
  {feature.relatedFeatures}

  ## 已知限制/技术债
  {feature.limitations}

  ## 变更记录
  | 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
  | --- | --- | --- | --- | --- |
  | {now} | v1 | 需求登记 | `/code ver` 识别并登记现有功能 | <unknown> |
  """

  mkdir -p "assistants/{version}/req/EXISTING-{feature.id}/"
  Write "assistants/{version}/req/EXISTING-{feature.id}/RESULT.md", content
  // 兼容读取(NFR-7, V0.0.7 之内有效,V0.0.8 起移除):
  // 扫描时若发现旧的 require/EXISTING-NNN/ 目录,自动 mv 到 req/
  legacyRequireDir = "assistants/{version}/require/EXISTING-{feature.id}/"
  if exists(legacyRequireDir):
    mv legacyRequireDir "assistants/{version}/req/EXISTING-{feature.id}/"
```

#### 回填版本看板

```
function backfillDashboard(version, features):
  dashboard = Read("assistants/{version}/RESULT.md")
  // 在"需求清单"区段追加 M 行
  // 注意:dashboard-v2 schema 不存动态状态列(FR-1);状态从 deriveItemStatus() 派生
  // 写入时只填静态字段(编码 / 标题 / 进度文档);EXISTING-NNN 在 /code ver 初始化阶段
  // 由 deriveItemStatus() 判定为已完成(基线功能,无 PROCESS.md)
  for feature in features:
    appendToDashboard("需求清单", {
      需求编码: "EXISTING-{feature.id}",
      标题: feature.name,
      进度文档: "[RESULT.md](req/EXISTING-{feature.id}/RESULT.md)",
    })
  // 追加变更记录(变更记录保留,因为它本身是"何时发生什么"的元信息,不是动态状态)
  appendChangeRecord("需求新增", "批量登记了 {features.length} 条现有功能需求")
```

### §2.8 引导用户补齐编码规范

```
function guideToRules():
  rulesDir = "assistants/rules/"
  hasRules = exists(rulesDir) and listFiles(rulesDir).length > 0

  if not hasRules:
    print("""
    ⚠️ `./assistants/rules/` 目录为空,后续 `/code req` / `/code fix` 都会从这里读规范作为约束。

    建议下一步:调 `/code rule` 添加编码规范。
    输入示例:
    - "Python 函数命名统一用 snake_case"
    - "所有数据库操作必须走 ORM,禁止裸 SQL"
    - "前端组件 props 必须显式声明类型"
    """)
```

---

## §3 版本切换

### §3.1 读取当前版本与校验

```
function readCurrentAndValidate(targetVersion):
  currentVersion = null
  if exists("assistants/.current-version"):
    currentVersion = Read("assistants/.current-version").trim()

  // 校验目标版本号
  validate(targetVersion):
    if empty(targetVersion): error("版本号不能为空")
    if contains(targetVersion, ["/", "\\"]): error("版本号不能包含路径分隔符")

  targetExists = exists("assistants/{targetVersion}/")

  return { currentVersion, targetVersion, targetExists }
```

### §3.2 四种情形处理

```
function handleSwitchScenario(scenario):
  switch scenario:
    case "A": // 目标版本不存在 + 当前也无激活版本
      // 直接创建,无需确认
      createNewVersion(targetVersion)
      writeCurrentVersion(targetVersion)

    case "B": // 目标版本不存在 + 当前已有激活版本
      AskUserQuestion:
        检测到当前激活版本为 `<currentVersion>`,你提供的是新版本 `<targetVersion>`。
        A. 创建新版本并切换(旧版本保留)
        B. 我搞错了,目标应是 `<currentVersion>`,不切换
        C. 取消
      if A:
        checkAndPublish(currentVersion)  // 步骤 3.2
        createNewVersion(targetVersion)
        writeCurrentVersion(targetVersion)

    case "C": // 目标版本已存在 + 与当前激活版本不同
      AskUserQuestion:
        目标版本 `<targetVersion>` 已存在。当前激活版本: `<currentVersion>`。
        A. 切换到 `<targetVersion>`
        B. 不切换
        C. 取消
      if A:
        checkAndPublish(currentVersion)
        writeCurrentVersion(targetVersion)

    case "D": // 目标版本已存在 + 与当前激活版本相同
      AskUserQuestion:
        目标版本 `<targetVersion>` 已是当前激活版本。
        A. 确认,继续在此版本工作
        B. 重新初始化此版本的看板(会覆盖现有 RESULT.md)
        C. 取消
      if B:
        writeDashboard(targetVersion)
```

### §3.3 检查是否需要发布

```
function checkAndPublish(currentVersion):
  dashboard = Read("assistants/{currentVersion}/RESULT.md")

  // 检查是否有活跃内容
  hasActiveContent = hasRequirements(dashboard) or hasTasks(dashboard)

  if not hasActiveContent:
    return  // 无需发布

  AskUserQuestion:
    当前版本 `<currentVersion>` 有活跃内容。
    A. 先发布当前版本,再切换
    B. 直接切换(不发布)
    C. 取消

  if A:
    result = runPublishCheck(currentVersion)
    if not result.passed:
      AskUserQuestion:
        发布检查未通过,是否仍要切换?
        A. 仍要切换(跳过发布)
        B. 取消切换,先解决未完成项
      if B: exit()
```

### §3.4 创建新版本

```
function createNewVersion(version):
  mkdir -p "assistants/{version}/"
  mkdir -p "assistants/{version}/req/"
  mkdir -p "assistants/{version}/fix/"
  mkdir -p "assistants/{version}/publish/"

  if not exists("assistants/{version}/RESULT.md"):
    writeDashboard(version)
```

### §3.5 验证与汇报

```
function verifyAndReport(version):
  // 验证
  currentContent = Read("assistants/.current-version")
  assert currentContent.trim() == version

  lsOutput = Bash("ls assistants/{version}/")
  dashboard = Read("assistants/{version}/RESULT.md")

  // 汇报
  print("""
  ✅ 当前激活版本: {version}
  工作空间根目录: ./assistants/{version}/
  看板位置: ./assistants/{version}/RESULT.md
  该版本下已有内容:
  {lsOutput}

  下一步建议:
  - 创建首个需求 → 调 `/code req`
  - 登记缺陷 → 调 `/code fix`
  """)
```

---

## §4 发布检查

### §4.1 发布前置检查

#### 解析算法

```
function preflightCheck(version):
  // 数据源:从各需求/缺陷的 PROCESS.md / PLAN.md / BUG.md 派生,
  // 不再从 RESULT.md 状态列读取(FR-1, schema-v2 不存动态状态列)
  requirements = Glob(`assistants/${version}/req/REQ-*/`)
  defects = Glob(`assistants/${version}/fix/BUG-*/`)

  undone = []
  for reqDir in requirements:
    reqId = extractReqId(reqDir)  // 例:REQ-00051
    status = deriveItemStatus(reqId)
    if not status.completed:
      meta = readReqMeta(reqId)    // 读 REQUIRE.md 的标题
      undone.push({ type: "需求", id: reqId, title: meta.title, stage: status.stage })

  for bugDir in defects:
    bugId = extractBugId(bugDir)  // 例:BUG-00009
    status = deriveItemStatus(bugId)
    if not status.completed:
      meta = readBugMeta(bugId)    // 读 BUG.md 的标题
      undone.push({ type: "缺陷", id: bugId, title: meta.title, stage: status.stage })

  return {
    passed: undone.length == 0,
    undone: undone,
    stats: {
      requirements: { total: requirements.length, done: countCompleted(requirements) },
      defects: { total: defects.length, done: countCompleted(defects) },
    }
  }
```

#### 解析区段

```
function parseSection(dashboard, sectionName):
  // 定位区段:从 ^## {sectionName}$ 到下一个 ^##  之间
  sectionText = extractSection(dashboard, sectionName)

  if not sectionText:
    return []  // 区段不存在,视为空

  // 解析表格行
  lines = sectionText.split("\n")
  headerRow = findHeaderRow(lines)
  separatorRow = findSeparatorRow(lines)
  dataRows = findDataRows(lines, separatorRow)

  // 用列名识别(而非列号位置)
  headers = parseHeaderColumns(headerRow)
  results = []
  for row in dataRows:
    cols = parseRowColumns(row)
    results.push(mapColumnsToFields(cols, headers))

  return results
```

#### 不通过报告

```
function formatFailedReport(result):
  print("""
  ✗ 发布前置检查未通过

  未完成项明细:
  {formatUndoneItems(result.undone)}

  阻塞统计:
  - 需求: {result.stats.requirements.done}/{result.stats.requirements.total} 已完成
  - 缺陷: {result.stats.defects.done}/{result.stats.defects.total} 已修复

  ✗ 未生成任何手册。请先解决上述项后重试。
  """)
```

### §4.2 基线识别

```
function isBaselineVersion(version):
  allVersions = listVersions("assistants/")
  sortedVersions = allVersions.sort()  // 字典序
  minVersion = sortedVersions[0]

  return version == minVersion
```

### §4.3 生成部署手册

#### DEPLOY.md(始终生成)

```
function generateDeployManual(version):
  content = """
  # 发布部署手册 — {version}

  > ⚠ **本手册为通用发布部署骨架**,由 `/code ver` 生成。
  > 请先手动补全所有 `<placeholder>`,再按本手册的步骤执行部署。

  ## 1. 概述
  - **版本号**:{version}
  - **目标环境**:<生产 / 预发 / 测试>
  - **发布时间**:<YYYY-MM-DD>
  - **发布者**:<执行部署的人员>

  ## 2. 打包
  <根据你的软件形态选择打包方式>

  ## 3. 获取成果物
  <列出本版本的所有发布物>

  ## 4. 上传服务器
  <上传到目标服务器的步骤>

  ## 5. 初始化系统
  <环境准备、数据库建表、配置修改>

  ## 6. 启动运行
  <启动服务并验证>

  ## 7. 首次进入软件系统
  <访问 URL、默认账号、首次操作建议>

  ## 8. 验证清单
  <部署完成后的逐项勾选清单>
  """

  mkdir -p "assistants/{version}/publish/"
  Write "assistants/{version}/publish/DEPLOY.md", content
```

#### UPDATE.md(仅非基线)

```
function generateUpdateManual(version, previousVersion):
  if isBaselineVersion(version):
    return  // 跳过

  content = """
  # 升级部署手册 — {version}(从 {previousVersion} 升级)

  > ⚠ **本手册为通用升级骨架**,由 `/code ver` 生成。
  > 请先手动补全所有 `<placeholder>`,再按本手册的步骤执行升级。

  ## 1. 升级概述
  - **源版本**:{previousVersion}
  - **目标版本**:{version}

  ## 2. 升级前准备
  <备份数据库、配置文件、当前版本文件>

  ## 3. 数据迁移
  <数据库 schema 变更、数据迁移脚本>

  ## 4. 配置变更
  <新增/修改/删除的配置项>

  ## 5. 替换程序文件
  <替换主程序、依赖、静态资源>

  ## 6. 重启服务
  <停止旧服务、启动新服务>

  ## 7. 升级后验证
  <验证关键功能、数据完整性>

  ## 8. 回滚方案
  <如果升级失败,如何回滚到 {previousVersion}>
  """

  Write "assistants/{version}/publish/UPDATE.md", content
```

#### FAQ.md(始终生成)

```
function generateFAQManual(version):
  faqFiles = Glob("assistants/faq/*.md").filter(f => f != "README.md")

  if faqFiles.length == 0:
    content = """
    # 发布部署 FAQ — {version}

    > 本手册聚合自 `assistants/faq/`,供发布部署中遇到问题时查阅。

    ## 占位:常见问题(待补充)
    请在 `assistants/faq/` 目录下添加 FAQ 内容,再重跑 `/code ver --publish`。
    """
  else:
    content = "# 发布部署 FAQ — {version}\n\n"
    for (i, file) in enumerate(faqFiles):
      fileContent = Read(file)
      content += "## {i+1}. {extractTitle(fileContent)}(来源:faq/{file})\n"
      content += fileContent + "\n\n"
    content += "## 占位:常见问题(待补充)\n"
    content += "请在 `assistants/faq/` 目录下添加 FAQ 内容,再重跑 `/code ver --publish`。\n"

  Write "assistants/{version}/publish/FAQ.md", content
```

### §4.4 创建 faq/ 骨架

```
function scaffoldFaq():
  if not exists("assistants/faq/"):
    mkdir -p "assistants/faq/"
    Write "assistants/faq/README.md", """
    # FAQ 目录

    本目录用于存放项目级 FAQ 内容,跨版本共享。

    ## 使用方式
    1. 在本目录下创建 `.md` 文件,每个文件一个主题
    2. 文件名建议用问题简述(如 `数据库连接失败.md`)
    3. 内容建议包含:问题描述、触发条件、解决方案、预防措施

    ## 与 `/code ver` 的关系
    `/code ver --publish` 会聚合本目录下的所有 FAQ 文件到 `publish/FAQ.md`。
    """
```

### §4.5 发布报告

```
function formatPublishReport(result):
  if result.passed:
    if result.isBaseline:
      print("""
      ✓ 发布前置检查通过(本版本 {version} 是基线)

      已生成 2 份手册(基线无 UPDATE.md):
      - assistants/{version}/publish/DEPLOY.md
      - assistants/{version}/publish/FAQ.md

      ⚠ 提示:手册均为通用骨架,请手动补全占位符后再按手册执行
      """)
    else:
      print("""
      ✓ 发布前置检查通过

      已生成 3 份手册:
      - assistants/{version}/publish/DEPLOY.md
      - assistants/{version}/publish/UPDATE.md(从 {previousVersion} 升级)
      - assistants/{version}/publish/FAQ.md

      ⚠ 提示:手册均为通用骨架,请手动补全占位符后再按手册执行
      """)
  else:
    formatFailedReport(result)
```

---

## §5 CWD 描述文件版本号同步(四步流程,FR-9 方案 B)

> 保留自动同步 CWD 描述文件的默认行为,加"差异预览 → 用户确认 → 失败回滚 → 提交记录"四步前置。完整契约见 `references/_shared/contracts.md` §7。

```
function syncCwdVersionFiles(newVersion, flags):
  // 跳过同步开关:--no-sync
  if flags.includes("--no-sync"):
    print("⚠ --no-sync 启用,跳过 CWD 描述文件同步")
    return

  descriptorFiles = [
    "package.json",     // Node.js / npm
    "pom.xml",          // Maven Java
    "manifest.json",    // Web App / PWA
    "Cargo.toml",       // Rust
    "pyproject.toml",   // Python
    "go.mod",           // Go(无版本号字段,仅跳过)
  ]

  matched = descriptorFiles.filter(exists)

  if matched.length == 0:
    print("⚠ CWD 下未检测到任何已知工程类型描述文件,跳过同步")
    return

  // 步骤 1:差异预览
  pendingChanges = []
  for file in matched:
    if file == "go.mod":
      print("⚠ go.mod 无版本号字段(Go 用 git tag),跳过")
      continue
    content = Read(file)
    oldVersion = parseVersionField(file, content)
    if oldVersion == null:
      print("⚠ {file} 未找到版本号字段,跳过")
      continue
    newContent = replaceVersionField(file, content, newVersion)
    diffSummary = computeDiff(content, newContent)
    pendingChanges.push({ file: file, oldVersion: oldVersion, newVersion: newVersion, newContent: newContent, diff: diffSummary })

  if pendingChanges.length == 0:
    print("✓ 无 CWD 描述文件需要同步")
    return

  print("""
  ╔══ CWD 描述文件版本号同步预览 ══╗
  待变更 {pendingChanges.length} 项:
  {formatPendingChanges(pendingChanges)}
  ╚════════════════════════════════╝
  """)

  // 步骤 2:用户确认
  response = AskUserQuestion("确认同步?", [
    "A. 全部同步(推荐)",
    "B. 中止(只更新 .current-version,不写 CWD)",
    "C. 仅同步特定文件(子流程:列出文件名让用户多选)",
  ])

  if response == "B":
    print("⚠ 用户中止同步,只更新 .current-version")
    return
  if response == "C":
    pendingChanges = filterByUserSelection(pendingChanges)

  // 步骤 3:写文件 + 失败回滚
  appliedFiles = []
  for change in pendingChanges:
    try:
      Write(change.file, change.newContent)
      appliedFiles.push(change.file)
      print("✓ {change.file}: {change.oldVersion} → {change.newVersion}")
    catch error:
      // 失败回滚:已写的也回退
      for applied in appliedFiles:
        git checkout -- applied
      print("✗ {change.file} 写入失败,已回滚所有已变更文件: {error}")
      return 1

  // 步骤 4:提交记录(走 BUG-00009 的修复路径:流程末尾统一 commit)
  print("✓ CWD 描述文件同步完成 {appliedFiles.length} 项;待流程末尾统一 commit")
  return 0
```

### 版本号字段解析

```
function parseVersionField(filename, content):
  switch filename:
    case "package.json":
    case "manifest.json":
      match = content.match(/"version"\s*:\s*"([^"]+)"/)
      return match ? match[1] : null
    case "pom.xml":
      match = content.match(/<version>([^<]+)<\/version>/)
      return match ? match[1] : null
    case "Cargo.toml":
    case "pyproject.toml":
      match = content.match(/^version\s*=\s*"([^"]+)"/m)
      return match ? match[1] : null
    default:
      return null
```

---

## §6 看板字段约定(简化版)

`/code ver` 创建的 `RESULT.md` 是简化版,仅含 2 个核心区段:

| 区段 | 主要写入方 | 用途 |
| --- | --- | --- |
| 需求清单 | `/code req`(首次创建时追加) | 需求编码、标题、PROCESS.md 链接 |
| 缺陷清单 | `/code fix`(登记缺陷时追加) | 缺陷编号、标题、PROCESS.md 链接 |

**简化版看板的范围**:
- 仅含 2 个核心区段(需求清单、缺陷清单)
- 进度通过 `PROCESS.md` 链接查看,而非看板本身的表格
- `/code req` 各阶段完成时**不再改写**看板,仅追加 PROCESS.md

**发布检查**直接解析 PROCESS.md 或需求/缺陷目录下的状态文件,而非看板表格。

---

## §7 通用边界

### 错误处理

- 文件写入失败 → 屏显警告,不阻断主流程(除 `.current-version` 和 `RESULT.md` 写入)
- Git 操作失败 → 屏显警告,不阻断主流程
- 分析代码时文件读取失败 → 跳过该文件,继续分析
- 发布检查时区段解析失败 → 保守判定(该区段视为"全未解决")

### 幂等性

- 重复执行初始化 → 不覆盖已有 `INIT-REPORT.md` 和 `EXISTING-NNN/` 文件
- 重复执行版本切换 → `.current-version` 覆盖
- 发布手册重复生成 → 覆盖已有文件

### 安全约束

- 版本号不允许含 `/` `\` `..`(防路径穿越)
- 不在 `assistants/rules/` 下创建版本子目录
- 不修改项目源代码(初始化时只读分析)

---

## §8 看板模式(无参数,已初始化项目)

### §8.1 版本上下文检测

```
function checkVersionContext():
  currentVersion = Read("assistants/.current-version")
  if not currentVersion:
    print("✗ 未检测到激活的版本工作空间")
    print("请先调 /code ver <版本号> 初始化或切换版本")
    exit()

  version = currentVersion.trim()
  if not exists("assistants/{version}/"):
    print("✗ 版本 {version} 工作空间不存在")
    print("请先调 /code ver <版本号> 初始化或切换版本")
    exit()

  return version
```

### §8.2 数据加载

```
function loadDashboardData(version):
  // 1. 读主看板
  dashboard = Read("assistants/{version}/RESULT.md")
  if not dashboard:
    print("✗ 看板文件不存在,请先初始化版本")
    exit()

  // 2. 列出所有需求/缺陷
  reqDirs = Glob("assistants/{version}/req/REQ-*")
  bugDirs = Glob("assistants/{version}/fix/BUG-*")

  // 3. 并行读取所有 PROCESS.md
  reqProcesses = []
  for dir in reqDirs:
    processFile = "{dir}/PROCESS.md"
    if exists(processFile):
      reqProcesses.push({ id: basename(dir), content: Read(processFile) })
    else:
      reqProcesses.push({ id: basename(dir), content: null })

  bugProcesses = []
  for dir in bugDirs:
    processFile = "{dir}/PROCESS.md"
    if exists(processFile):
      bugProcesses.push({ id: basename(dir), content: Read(processFile) })
    else:
      bugProcesses.push({ id: basename(dir), content: null })

  return { dashboard, reqProcesses, bugProcesses }
```

### §8.3 区段解析

```
function parseDashboard(dashboard):
  // 按 ^## (.+)$ 匹配所有区段标题
  anchors = {}
  for match in dashboard.matchAll(/^## (.+)$/gm):
    anchors[match[1]] = match.index

  // 提取需求清单区段
  reqSection = extractSection(dashboard, "需求清单", anchors)
  bugSection = extractSection(dashboard, "缺陷清单", anchors)

  // 解析表格行
  reqRows = parseTableRows(reqSection)
  bugRows = parseTableRows(bugSection)

  return { reqRows, bugRows }

function parseTableRows(sectionText):
  if not sectionText:
    return []

  rows = []
  for line in sectionText.split("\n"):
    if line.match(/^\| .* \|$/) and not line.match(/^\| ---/):
      cols = line.split("|").map(c => c.trim()).filter(c => c != "")
      rows.push(cols)

  return rows
```

**L2 退化**:
- 区段缺失 → 返回 `[]`(显示 `(无)`)
- 表格列错位 → 退化到原始 markdown 块原样输出
- 字段值缺失 → 显示 `?` 占位

### §8.4 进度计算

```
function calculateProgress(reqProcesses, bugProcesses):
  // 需求 6 阶段: INIT→REQUIRE→DESIGN→PLAN→CODING→CHECK→DONE
  // 缺陷 5 阶段: INIT→DESIGN→PLAN→CODING→CHECK→DONE

  reqStages = ["INIT", "REQUIRE", "DESIGN", "PLAN", "CODING", "CHECK"]
  bugStages = ["INIT", "DESIGN", "PLAN", "CODING", "CHECK"]

  totalStages = reqProcesses.length * reqStages.length + bugProcesses.length * bugStages.length
  completedStages = 0

  for req in reqProcesses:
    if not req.content:
      continue  // 0 阶段完成
    lastStage = parseLastStage(req.content)
    if lastStage == "DONE":
      completedStages += reqStages.length
    else:
      idx = reqStages.indexOf(lastStage)
      if idx >= 0:
        completedStages += idx  // 已完成阶段数(不含当前阶段)

  for bug in bugProcesses:
    if not bug.content:
      continue
    lastStage = parseLastStage(bug.content)
    if lastStage == "DONE":
      completedStages += bugStages.length
    else:
      idx = bugStages.indexOf(lastStage)
      if idx >= 0:
        completedStages += idx

  return { completedStages, totalStages }

function parseLastStage(processContent):
  // 读取 PROCESS.md 最后一条记录,提取阶段字段
  lines = processContent.trim().split("\n")
  lastLine = lines[lines.length - 1]
  // 格式: | <时间> | <阶段> | <状态> | <描述> |
  cols = lastLine.split("|").map(c => c.trim())
  if cols.length >= 3:
    return cols[2]  // 阶段字段
  return null
```

### §8.5 状态归类

```
function classifyByStatus(reqProcesses, bugProcesses):
  statuses = {
    "待需求分析": 0,
    "待设计": 0,
    "待排期": 0,
    "待编码": 0,
    "待审查": 0,
  }

  for req in reqProcesses:
    lastStage = req.content ? parseLastStage(req.content) : null
    if not lastStage or lastStage == "INIT":
      statuses["待需求分析"]++
    else if lastStage == "REQUIRE":
      statuses["待设计"]++
    else if lastStage == "DESIGN":
      statuses["待排期"]++
    else if lastStage == "PLAN":
      statuses["待编码"]++
    else if lastStage == "CODING":
      statuses["待审查"]++

  for bug in bugProcesses:
    lastStage = bug.content ? parseLastStage(bug.content) : null
    if not lastStage or lastStage == "INIT":
      statuses["待设计"]++  // 缺陷不经过"待需求分析"
    else if lastStage == "DESIGN":
      statuses["待排期"]++
    else if lastStage == "PLAN":
      statuses["待编码"]++
    else if lastStage == "CODING":
      statuses["待审查"]++

  return statuses
```

### §8.6 高优先级缺陷统计

```
function countHighPriorityBugs(bugRows, version):
  // 数据源:从 BUG.md 派生 + deriveItemStatus(),
  // 不再从 RESULT.md 状态/优先级列读取(FR-1, schema-v2 不存动态状态列)
  // bugRows 参数仅用于回退展示,实际统计走派生
  p0 = 0
  p1 = 0
  bugDirs = Glob(`assistants/${version}/fix/BUG-*/`)

  for bugDir in bugDirs:
    bugId = extractBugId(bugDir)
    bugMeta = readBugMeta(bugId)        // 读 BUG.md 的优先级 + 标题
    status = deriveItemStatus(bugId)

    // 仅统计未完成的(契约层 §3 判定 completed)
    if status.completed:
      continue
    if bugMeta.priority == "P0":
      p0++
    else if bugMeta.priority == "P1":
      p1++

  return { p0, p1 }
```

### §8.7 建议生成

```
function generateSuggestions(reqProcesses, bugProcesses, bugRows):
  suggestions = []

  // 1. 高:P0 待修复
  p0Bugs = bugRows.filter(b => b.priority == "P0" and b.status not in ["已完成", "已修复-已验证", "已关闭"])
  if p0Bugs.length > 0:
    suggestions.push({
      command: "/code fix {p0Bugs[0].id}",
      priority: "高",
      reason: "P0 待修复 {p0Bugs.length} 个",
    })

  // 2. 高:需求 INIT 阶段
  initReqs = reqProcesses.filter(r => not r.content or parseLastStage(r.content) == "INIT")
  if initReqs.length > 0:
    suggestions.push({
      command: "/code req {initReqs[0].id}",
      priority: "高",
      reason: "{initReqs.length} 个需求待启动",
    })

  // 3. 中:需求 DESIGN 阶段 或 缺陷 INIT 阶段
  designReqs = reqProcesses.filter(r => parseLastStage(r.content) == "DESIGN")
  initBugs = bugProcesses.filter(b => not b.content or parseLastStage(b.content) == "INIT")
  if designReqs.length > 0:
    suggestions.push({
      command: "/code req {designReqs[0].id}",
      priority: "中",
      reason: "{designReqs.length} 个需求待排期",
    })
  if initBugs.length > 0:
    suggestions.push({
      command: "/code fix {initBugs[0].id}",
      priority: "中",
      reason: "{initBugs.length} 个缺陷待启动",
    })

  // 4. 低:需求 CODING 阶段
  codingReqs = reqProcesses.filter(r => parseLastStage(r.content) == "CODING")
  if codingReqs.length > 0:
    suggestions.push({
      command: "/code req {codingReqs[0].id}",
      priority: "低",
      reason: "{codingReqs.length} 个需求待编码完成",
    })

  // 5. 特殊:全版本已完成
  allDone = reqProcesses.every(r => parseLastStage(r.content) == "DONE")
         and bugProcesses.every(b => parseLastStage(b.content) == "DONE")
         and p0Bugs.length == 0 and p1Bugs.length == 0
  if allDone and (reqProcesses.length > 0 or bugProcesses.length > 0):
    suggestions.push({
      command: "/code ver V0.0.x",
      priority: "高",
      reason: "当前版本已完成,建议切换新版本",
    })

  // 无任何建议
  if suggestions.length == 0:
    suggestions.push({ command: null, priority: null, reason: "无后续动作" })

  return suggestions.slice(0, 5)
```

### §8.8 屏幕渲染

```
function renderDashboard(progress, statuses, highPriorityBugs, suggestions):
  // 段 1: 进度条
  if progress.totalStages == 0:
    print("— / 无需求无缺陷,无需进度")
  else:
    pct = round(progress.completedStages / progress.totalStages * 100)
    blocks = round(pct / 100 * 12)
    bar = "[" + "█" * blocks + "░" * (12 - blocks) + "] " + pct + "%"
    print(bar)

  // 段 2: 状态分布
  nonZeroStatuses = []
  for (status, count) in statuses:
    if count > 0:
      nonZeroStatuses.push("{status} {count}")
  if nonZeroStatuses.length > 0:
    print("状态: " + nonZeroStatuses.join(" / "))
  else:
    print("状态: (无)")

  // 段 3: 高优先级缺陷
  p0Marker = highPriorityBugs.p0 > 0 ? "█" : "░"
  p1Marker = highPriorityBugs.p1 > 0 ? "▓" : "░"
  print("P0 待修复: {p0Marker} {highPriorityBugs.p0} | P1 待修复: {p1Marker} {highPriorityBugs.p1}")

  // 段 4: 建议
  for s in suggestions:
    if s.command:
      print("> {s.command} [{s.priority}] (依据: {s.reason})")
    else:
      print("> 无后续动作")
```

### §8.9 看板模式边界

#### L1 启动错误

| 场景 | 触发条件 | 屏幕输出 |
| --- | --- | --- |
| E-1 无激活版本 | `.current-version` 不存在 | `✗ 未检测到激活的版本工作空间` |
| E-2 版本工作空间不存在 | 目录缺失 | `✗ 版本 <X> 工作空间不存在` |
| E-3 看板文件缺失 | `RESULT.md` 不存在 | `✗ 看板文件不存在,请先初始化版本` |

#### L2 数据错误(可降级)

| 场景 | 触发条件 | 处理 |
| --- | --- | --- |
| 区段缺失 | 看板不含目标区段 | 该段显示 `(无)` |
| 表格列错位 | 列数≠期望 | 退化到原始 markdown 块 |
| 字段值缺失 | 单元格为空 | 显示 `?` |
| PROCESS.md 缺失 | 文件不存在 | 视为 0 阶段完成 |
| PROCESS.md 解析失败 | 阶段字段异常 | 归入"待需求分析" |
| 全版本无需求 | 初始化态 | 建议 `/code req`(高) |
| 全版本已完成 | 所有 DONE + 无 P0/P1 待修复 | 建议 `/code ver V0.0.x`(高) |
| 旧格式任务编号 | 字面透传 | 不解析路径 |

#### L3 异常兜底

任何未预期异常 → `✗ 内部错误: <msg>` + 退出

### §8.10 看板模式工具约束

- 仅调用 `Read`/`Glob`/`Grep`
- 不调用 `Write`/`Edit`/`Bash`/`WebFetch`/`WebSearch`/`Task`/`Agent`
- 不修改任何文件(只读)
- 多次执行幂等