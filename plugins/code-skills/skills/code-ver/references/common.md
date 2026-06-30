# 公共流程 — code-ver

> 本文件为 code-ver 技能提供场景检测、初始化、版本切换、发布检查的详细流程。始终加载。

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

  // 无参数:列出已有版本,让用户选择
  return "PROMPT"
```

### 无参数时的交互

```
function promptUserForAction():
  versions = listVersions("assistants/")
  currentVersion = readCurrentVersion()

  AskUserQuestion:
    当前激活版本: <currentVersion>
    已有版本: <versions>

    A. 切换到已有版本
    B. 创建新版本
    C. 初始化新项目
    D. 发布当前版本
```

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
  > 由 `code-ver` 创建,`code-req` / `code-fix` 更新。

  ## 文档头
  - 版本号:`{version}`
  - 创建时间:{now}
  - 最近更新:{now}
  - 状态:活跃

  ## 需求清单

  > 写入方:`code-req`(新建需求时追加)
  > 进度通过 PROCESS.md 链接查看

  | 需求编码 | 标题 | 进度文档 |
  | --- | --- | --- |
  | — | — | — |

  **统计**:0

  ## 缺陷清单

  > 写入方:`code-fix`(登记缺陷时追加)

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

  > 由 `code-ver` 在 {now} 生成,用于快速了解项目现状。

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
  - 生成工具:code-ver
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
  | {now} | v1 | 需求登记 | code-ver 识别并登记现有功能 | <unknown> |
  """

  mkdir -p "assistants/{version}/require/EXISTING-{feature.id}/"
  Write "assistants/{version}/require/EXISTING-{feature.id}/RESULT.md", content
```

#### 回填版本看板

```
function backfillDashboard(version, features):
  dashboard = Read("assistants/{version}/RESULT.md")
  // 在"需求清单"区段追加 M 行
  for feature in features:
    appendToDashboard("需求清单", {
      需求编码: "EXISTING-{feature.id}",
      标题: feature.name,
      状态: "已完成",
      创建时间: now,
      完成时间: now,
      需求文档: "[RESULT.md](require/EXISTING-{feature.id}/RESULT.md)",
    })
  // 更新统计
  updateStats("需求清单", total: features.length, 已完成: features.length)
  // 追加变更记录
  appendChangeRecord("需求新增", "批量登记了 {features.length} 条现有功能需求")
```

### §2.8 引导用户补齐编码规范

```
function guideToRules():
  rulesDir = "assistants/rules/"
  hasRules = exists(rulesDir) and listFiles(rulesDir).length > 0

  if not hasRules:
    print("""
    ⚠️ `./assistants/rules/` 目录为空,后续 `code-req` / `code-fix` 都会从这里读规范作为约束。

    建议下一步:调 `code-rule` 添加编码规范。
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
  - 创建首个需求 → 调 `code-req`
  - 登记缺陷 → 调 `code-fix`
  """)
```

---

## §4 发布检查

### §4.1 发布前置检查

#### 解析算法

```
function preflightCheck(version):
  dashboard = Read("assistants/{version}/RESULT.md")

  // 解析 3 区段
  requirements = parseSection(dashboard, "需求清单")
  defects = parseSection(dashboard, "缺陷清单")

  // 判定规则
  undone = []
  for req in requirements:
    if not req.状态.startswith("已完成"):
      undone.push({ type: "需求", id: req.编码, title: req.标题, status: req.状态 })

  for defect in defects:
    if defect.状态 != "已修复":
      undone.push({ type: "缺陷", id: defect.编号, title: defect.标题, status: defect.状态 })

  return {
    passed: undone.length == 0,
    undone: undone,
    stats: {
      requirements: { total: requirements.length, done: requirements.length - countUndone(requirements, "需求") },
      defects: { total: defects.length, done: defects.length - countUndone(defects, "缺陷") },
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

  > ⚠ **本手册为通用发布部署骨架**,由 `code-ver` 生成。
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

  > ⚠ **本手册为通用升级骨架**,由 `code-ver` 生成。
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
    请在 `assistants/faq/` 目录下添加 FAQ 内容,再重跑 `code-ver --publish`。
    """
  else:
    content = "# 发布部署 FAQ — {version}\n\n"
    for (i, file) in enumerate(faqFiles):
      fileContent = Read(file)
      content += "## {i+1}. {extractTitle(fileContent)}(来源:faq/{file})\n"
      content += fileContent + "\n\n"
    content += "## 占位:常见问题(待补充)\n"
    content += "请在 `assistants/faq/` 目录下添加 FAQ 内容,再重跑 `code-ver --publish`。\n"

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

    ## 与 code-ver 的关系
    `code-ver --publish` 会聚合本目录下的所有 FAQ 文件到 `publish/FAQ.md`。
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

## §5 CWD 描述文件版本号同步

```
function syncCwdVersionFiles(newVersion):
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

  for file in matched:
    try:
      if file == "go.mod":
        print("⚠ go.mod 无版本号字段(Go 用 git tag),跳过")
        continue

      content = Read(file)
      oldVersion = parseVersionField(file, content)

      if oldVersion == null:
        print("⚠ {file} 未找到版本号字段,跳过")
        continue

      newContent = replaceVersionField(file, content, newVersion)
      Write(file, newContent)

      print("✓ CWD 描述文件同步:{file}: {oldVersion} → {newVersion}")
    catch error:
      print("⚠ {file} 格式不可解析,跳过")
      continue
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

`code-ver` 创建的 `RESULT.md` 是简化版,仅含 2 个核心区段:

| 区段 | 主要写入方 | 用途 |
| --- | --- | --- |
| 需求清单 | `code-req`(首次创建时追加) | 需求编码、标题、PROCESS.md 链接 |
| 缺陷清单 | `code-fix`(登记缺陷时追加) | 缺陷编号、标题、PROCESS.md 链接 |

**与旧版看板的区别**:
- 不再包含:概要设计清单、详细设计与任务计划汇总、任务清单、评审发现汇总、派生任务记录
- 进度通过 `PROCESS.md` 链接查看,而非看板本身的表格
- `code-req` 各阶段完成时**不再改写**看板,仅追加 PROCESS.md

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