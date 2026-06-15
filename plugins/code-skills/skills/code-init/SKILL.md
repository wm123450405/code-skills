---
name: code-init
description: 工程初始化(项目级一次性)。要求用户提供一个"初始版本号"(默认 V0.0.0),**初始化整个项目工程**:
1. 在 CWD 下创建 `./assistants/` 及完整子结构(`rules/`、`<初始版本号>/`、`require/`、...)
2. 把 `.current-version` 切换到该初始版本(此时**当前激活版本 = 初始版本**)
3. **若是首次初始化**(无任何现存 assistants 内容或 `<初始版本号>/` 不存在),则阅读项目中所有已有代码,理解所有已有功能,生成:
   - `./assistants/<初始版本号>/INIT-REPORT.md` 功能分析报告
   - `./assistants/<初始版本号>/require/EXISTING-NNN/RESULT.md` × N 现有软件功能的需求清单(每一项主要功能/模块对应一份)
4. 同步写入版本看板(RESULT.md)的"需求清单"和"变更记录"区段
5. **若 `./assistants/rules/` 缺失或为空**,完成初始化后引导用户调 `code-rule` 添加编码规范
6. **最终引导用户调 `code-version` 开启一个新的开发版本**(后续所有 `code-require` 等都在新版本上进行;初始版本作为历史基线)
- 一个项目**只应该被 `code-init` 一次**;若再调用,会要求用户确认(可能误调用)。
- 本技能**不**与其他 `code-*` 技能抢占职责:它实质上等价于"自动跑一次 `code-version`(创基线版本)+ 一次"批量 `code-require`(把现有功能登记为需求)",但走自己的快速通道,产物兼容下游技能。
---

# code-init — 工程初始化

## 目标
把一个**已有或新建的项目**纳入 `code-*` 技能体系:
- 建立版本工作空间(基线版本)
- 把**现有代码当成"已交付的需求"**登记到 `require/EXISTING-NNN/`,使后续所有改动都能走 `code-require → code-design → code-plan → code-it → code-check` 的标准化流程
- 建立功能分析报告,作为新成员(包括 AI Agent)快速理解项目的入口
- 引导用户补齐编码规范,并开启新的开发版本

## 适用场景
- **场景 A — 全新项目**:CWD 下没有任何代码,直接 `code-init`,跳过代码分析(分析结果是"无现有功能")
- **场景 B — 老项目接入**:CWD 下已有代码,想把它纳入 `code-*` 体系(典型场景,本技能的核心)
- **场景 C — 项目重置**:CWD 下已有 `assistants/` 但用户想重新初始化(极少;需用户明确确认)

## 不适用
- 已经初始化过项目,只是想**切换版本** → 用 `code-version`
- 已经初始化过项目,只想**添加/修改一条需求** → 用 `code-require`
- 已经初始化过项目,只想**添加一条编码规范** → 用 `code-rule`
- 只是想给项目**添加一个 README** 或 LICENSE → 走普通文件操作

## 工作目录约定(强制)

本技能执行**前**(假设为全新项目):
```
<当前工作目录(CWD)>/
└── <项目代码,可能完全没有,可能有 src/lib/...>
```

本技能执行**后**:
```
<当前工作目录(CWD)>/
├── assistants/
│   ├── rules/                                # 跨版本共享的编码规范(可能为空)
│   ├── .current-version                      # 指向 <初始版本号>
│   └── <初始版本号>/                          # 基线版本工作空间
│       ├── RESULT.md                         # 版本看板
│       ├── INIT-REPORT.md                    # 功能分析报告(仅首次初始化生成)
│       └── require/
│           ├── EXISTING-001/RESULT.md        # 第一项现有功能的需求
│           ├── EXISTING-002/RESULT.md        # 第二项现有功能的需求
│           └── ...                           # (按发现的功能数生成 N 份)
└── <原有项目代码不变>
```

- 路径以**当前工作目录(CWD)**为基准
- 本技能**只**创建 `./assistants/` 及其子结构
- 本技能**不**修改项目源代码(只读分析)
- 本技能**不**创建 `.current-version` 以外的任何隐藏文件
- 本技能**不**读取/写入 `git`、`package.json` 等项目自身文件(只读)

## 输入
- **初始版本号**(必填,但有默认值):用户口头或文本指定
  - 默认:`V0.0.0`
  - 推荐用 semver(`V0.0.0`、`V0.1.0`)或日期风格(`2026-06`)
  - 校验:不能为空,不能含 `/` `\` `:` `*` `?` `"` `<` `>` `|`
  - **禁止**与 `code-init` 之后再创建的开发版本同名

## 输出
主产出物:
- `./assistants/.current-version`(内容 = `<初始版本号>`)
- `./assistants/<初始版本号>/RESULT.md`(版本看板)
- `./assistants/<初始版本号>/INIT-REPORT.md`(功能分析报告,**仅首次初始化**)
- `./assistants/<初始版本号>/require/EXISTING-NNN/RESULT.md` × N(现有功能需求,**仅首次初始化**)

**不修改**:
- 任何项目源代码(只读)
- `./assistants/<其他版本号>/`(若有,与本次初始化无关)
- `./assistants/rules/` 下任何已存在的文件(本技能不主动写规则)

## 工具使用约定
- 探 CWD 现状:`Bash: ls -la` + `Glob "**/*"`(控制深度,避免爆栈)
- 探 assistants 现状:`Bash: ls -la ./assistants/`(若不存在,`ls` 会报错)
- 读清单文件:`Read ./assistants/.current-version`(若存在)
- 建目录:`Bash: mkdir -p`
- 写文件:`Write`(首次)/ `Edit`(追加)
- 探项目结构:
  - `Glob` 找出所有源代码文件
  - `Read` 关键清单(package.json / go.mod / pyproject.toml / pom.xml / Cargo.toml / ...)
  - `Read` 入口文件
- 与用户澄清:优先 `AskUserQuestion`;自然语言兜底

---

## 工作流程

### 步骤 0 — 收集初始版本号

1. 若用户未提供,主动询问(用 `AskUserQuestion`,提供默认选项 + "其他" 自定义):
   - 提示用户:初始版本号建议 `V0.0.0`(代表"项目当前状态")
   - 用户可输入任何符合校验规则的字符串

2. 校验:
   - 非空
   - 不含路径分隔符或 Windows 保留字符
   - 不与已知已有版本重名(若 assistants 下已有 `<版本号>`,走步骤 1.5 的"重名"分支)

3. 记录为 `<初始版本号>`,后续所有路径用 `assistants/<初始版本号>/...`

### 步骤 1 — 探查 `assistants/` 现状

并行执行:
1. `Bash: ls -la ./assistants/ 2>/dev/null` → 推断 `assistants_exists`
2. 若存在,`Bash: ls -la ./assistants/rules/ 2>/dev/null` → 推断 `rules_dir_exists`
3. 若存在,`Read ./assistants/.current-version` → 推断 `previous_current_version`
4. 若存在,`Glob "./assistants/*/"` → 推断 `existing_versions`(过滤掉 `rules/`)
5. `Glob "**/*"`(限制深度,例如只到 `**/*.{js,ts,py,go,java,rs,c,cpp,h,hpp,rb,php,json,yaml,yml,toml,xml,md}` 等)→ 推断 `source_file_count`

把发现整理为内部状态:
- `assistants_exists`
- `rules_dir_exists`
- `rules_has_files`(若 `rules/` 存在但无文件,记 false)
- `previous_current_version`
- `existing_versions`
- `source_file_count`

### 步骤 1.5 — 决策分支

按状态分四种情形:

**情形 A:`!assistants_exists`(全新项目,从没跑过 `code-init`)**
- 直接进入步骤 2
- 无需确认

**情形 B:`assistants_exists && !previous_current_version`(部分初始化过,但没有 current-version)**
- 用 `AskUserQuestion` 询问:
  > 检测到 `./assistants/` 目录已存在,但无 `.current-version` 标记文件。
  > - A. 继续 `code-init` 创建基线版本 `<初始版本号>`,在已有 `assistants/` 之上
  > - B. 我搞错了,应先调 `code-version` 处理遗留状态
  > - C. 取消

**情形 C:`assistants_exists && existing_versions contains <初始版本号>`(初始版本号已存在)**
- 用 `AskUserQuestion` 询问:
  > 目标初始版本号 `<初始版本号>` 已存在(可能由 `code-version` 创建)。
  > - A. 复用现有目录,**只增量分析现有代码并补齐 `INIT-REPORT.md` 与 `EXISTING-NNN`**(若已存在则跳过)
  > - B. 我搞错了,初始版本号应是另一个(请重答步骤 0)
  > - C. 取消

**情形 D:`assistants_exists && previous_current_version && existing_versions 包含其他版本`(完全已初始化过)**
- 用 `AskUserQuestion` 询问(**强警告**):
  > 检测到 `./assistants/` 已被 `code-init` 初始化过:
  > - `.current-version` = `<previous_current_version>`
  > - 已存在版本:[`<v1>`, `<v2>`, ...]
  >
  > **警告**:再次跑 `code-init` 会:
  > - 在 `./assistants/<初始版本号>/` 下创建新基线版本(若已存在会冲突,见情形 C)
  > - **不会**覆盖或删除任何已存在版本
  > - 若要分析全新项目状态,建议先用 `code-version` 切到想要的位置
  >
  > - A. 我**确定**要再跑一次 `code-init`,目标初始版本 `<初始版本号>`(走情形 C 的子分支)
  > - B. 我搞错了,我应该调 `code-version` 切换版本,而不是 `code-init`
  > - C. 取消

### 步骤 2 — 创建 `assistants/` 骨架

按需创建(**不覆盖任何已存在文件**):
1. `Bash: mkdir -p "./assistants/"`
2. `Bash: mkdir -p "./assistants/rules/"`
3. `Bash: mkdir -p "./assistants/<初始版本号>/require/"`
4. `Bash: mkdir -p "./assistants/<初始版本号>/review/"`
5. 若情形 A(全新) → 也创建 `design/`、`plan/`、`code/`、`test/` 目录(空目录占位,符合 `code-version` 的目录约定)

> **若任一目录已存在,保持不动**(本技能不删除任何东西)。

### 步骤 3 — 写入 `.current-version`

1. `Write "./assistants/.current-version"`,内容 = `<初始版本号>\n`
2. **覆盖**是允许的,因为步骤 1.5 的情形 D 已确认

### 步骤 4 — 写入版本看板 `RESULT.md`

1. `Write "./assistants/<初始版本号>/RESULT.md"`,基于 `templates/version-RESULT.md` 模板
2. 填写:
   - 文档头:版本号、创建时间、状态(`活跃`)
   - 里程碑:新增 `M0:工程初始化` 行,完成定义 = "INIT-REPORT.md 与现有功能需求清单已生成",状态 = `已完成`
   - 需求清单:留空(等步骤 7 由现有功能需求批量回填)
   - 变更记录:首条
     ```
     YYYY-MM-DD HH:mm  初始化  创建基线版本 <初始版本号>,code-init 完成工程初始化
     ```
3. 若 `RESULT.md` 已存在(情形 C 的"复用"分支) → **不**用 `Write` 覆盖,改用 `Edit` 追加变更记录:
   - 在"变更记录"末尾追加:
     ```
     YYYY-MM-DD HH:mm  初始化  code-init 增量补齐了 INIT-REPORT.md 与 N 条 EXISTING-NNN 需求
     ```
   - **不**重写文件其他部分

### 步骤 5 — 分析现有代码(仅"首次分析"分支)

> **若 `source_file_count` 极小(例如 < 5)或为零(空项目),本步骤可大幅简化**;若项目体量很大,需要分批处理。

#### 5.1 项目类型识别
读取清单文件(任意一个存在即可推断项目类型):
| 清单文件 | 推断类型 |
| --- | --- |
| `package.json` | Node.js / JS / TS |
| `pyproject.toml` / `setup.py` / `requirements.txt` | Python |
| `go.mod` | Go |
| `pom.xml` / `build.gradle` | Java / Kotlin |
| `Cargo.toml` | Rust |
| `composer.json` | PHP |
| `Gemfile` | Ruby |
| `*.csproj` / `*.sln` | C# / .NET |
| `Makefile` / `CMakeLists.txt` | C / C++ |
| `build.gradle` (Android 风格) | Android |

**没有清单** → 推断为"脚本项目 / 静态站点 / 配置文件仓库",走简化流程。

#### 5.2 目录结构
- `Glob "**/*"` 列出所有文件(限制合理深度,例如 `**/*` 限制 5 层)
- 重点关注:
  - 顶层目录(`src/`、`lib/`、`app/`、`cmd/`、`internal/`、`pkg/`、...)
  - 配置目录(`config/`、`configs/`、`.env.example`)
  - 文档目录(`docs/`、`README*`)
  - 用户的测试目录(常见的命名约定)
- 在 `INIT-REPORT.md` 的"目录结构"区段绘制 ASCII 树(只到 2-3 层)

#### 5.3 入口与主流程
- 找入口文件:
  - Node: `package.json` 的 `"main"` / `"bin"` / 入口脚本
  - Python: `__main__.py` / `app.py` / `main.py` / `pyproject.toml` 的 `[project.scripts]`
  - Go: `cmd/*/main.go`
  - Java: 包含 `public static void main` 的类
  - Rust: `src/main.rs`
- `Read` 这些入口,理解主流程
- 识别主要的"用户路径"(用户调用了哪些功能)

#### 5.4 已有模块识别
- 按目录划分模块
- 对每个模块:
  - 路径
  - 职责(读核心文件归纳)
  - 对外暴露的接口(`Read` 关键类/函数的签名)
  - 依赖(对内其他模块 / 对外三方)

#### 5.5 已有数据模型
- 找 schema 文件:SQL、Prisma、ORM 模型类、TypeScript interface、结构体定义
- 列出实体、字段、关系
- 若完全没有结构化数据模型,标注"无显式数据模型"

#### 5.6 已有第三方依赖
- 读清单文件的依赖段
- 列出主要依赖及其用途(从代码中推断)

#### 5.7 编码与构建约定
- 找 `.editorconfig`、`eslintrc`、`prettierrc`、`tsconfig.json`、`pyproject.toml [tool.ruff]` 等
- 找 `Makefile` / `scripts/` / CI 配置(`.github/workflows/`)
- 把观察到的约定写入 `INIT-REPORT.md`

#### 5.8 可复用资产 / 已知技术债
- 复用资产:可被未来新功能复用的工具类、配置加载器、日志封装等
- 技术债:明显的坏味道(超大文件、循环依赖、魔法数字、缺少测试的核心模块、过期依赖等)
- 这一节不必追求全面,**有则记,无则省略**

### 步骤 6 — 生成 `INIT-REPORT.md`

**Write 整个文件**,基于 `templates/INIT-REPORT.md` 模板,核心区段:
1. **项目概述**:一两句话说清项目做什么
2. **技术栈**:语言、框架、关键依赖
3. **目录结构**:ASCII 树(2-3 层)
4. **核心模块与职责**:表格(模块/路径/职责/对外接口)
5. **入口与主流程**:从入口文件到用户可见功能的链路
6. **外部接口**:API 端点、CLI 命令、SDK 入口等
7. **数据模型**:实体、字段(若有)
8. **构建与运行**:构建命令、启动命令(从 Makefile / package.json scripts 推断)
9. **测试情况**:是否有测试、覆盖率(若有)、测试组织方式
10. **可复用资产**:值得未来新功能复用的工具/类/函数
11. **已知问题/技术债**:明显的坏味道
12. **本报告生成信息**:`code-init` 生成时间、生成人(AI Agent)、覆盖的源文件数

### 步骤 7 — 生成现有功能需求清单

#### 7.1 拆分功能边界
基于步骤 5 的分析,把项目拆成 M 个**主要功能/模块**:
- 拆分原则:
  - 一个功能 = 一个用户可识别的"能力"
  - 例:用户登录、订单管理、报表生成、定时任务、文件上传、权限校验
  - **不**要按文件/类拆分(粒度太细)
  - **不**要按业务域拆分(粒度太粗,除非是单一业务的简单项目)
- M 的合理范围:
  - 小项目(< 1k 行):M = 1-3
  - 中项目(1k-10k 行):M = 3-8
  - 大项目(> 10k 行):M = 5-15

#### 7.2 询问用户(可选,中大型项目推荐)
若 M 估算 > 5 且 < 20,可用 `AskUserQuestion` 让用户调整粒度:
- A. 按"用户可见功能"拆分(推荐)
- B. 按"代码模块"拆分
- C. 按"业务子域"拆分
- D. 由我(`code-init`)自行决定

小型项目可跳过此步,直接按"用户可见功能"拆分。

#### 7.3 编号
- 用 `EXISTING-NNN` 格式,从 `EXISTING-001` 开始
- 编号无业务含义,只保证全局唯一、按发现顺序递增

#### 7.4 写每份 `RESULT.md`
对每个功能 `EXISTING-NNN`:
1. `Bash: mkdir -p "./assistants/<初始版本号>/require/EXISTING-NNN/"`
2. `Write "./assistants/<初始版本号>/require/EXISTING-NNN/RESULT.md"`,基于 `templates/existing-requirement.md` 模板
3. 模板字段(强调"现有"特性):
   - 需求概述:一两句话说清该功能做什么
   - 现有实现位置:关键文件路径 + 行号区间(若可知)
   - 用户角色与场景:谁会用、用在什么场景
   - 功能点(FR-N):可观测到的功能项
   - 关键接口:函数签名 / API 端点 / CLI 命令
   - 数据模型:涉及的实体/字段(若适用)
   - 验收标准(AC):**从现有行为反推**的可验证条件
   - 关联功能:与其他 `EXISTING-MMM` 的关联(共享模块/数据)
   - 已知限制/技术债:本功能自身的局限
   - 变更记录:首条
     ```
     YYYY-MM-DD HH:mm  需求登记  code-init 识别并登记现有功能 EXISTING-NNN
     ```

#### 7.5 回填版本看板
1. `Read "./assistants/<初始版本号>/RESULT.md"`
2. 在"需求清单"区段追加 M 行,每行:
   - 需求编码 = `EXISTING-NNN`
   - 标题 = 该功能一句话
   - 状态 = `已完成`(因为功能已存在,等同于"已交付")
   - 创建时间 = 步骤 7.4 的写入时间
   - 完成时间 = 创建时间(默认"已存在即完成")
   - 需求文档 = `[RESULT.md](require/EXISTING-NNN/RESULT.md)`
   - 概要设计 = `—`(暂未做)
   - 详细设计 = `—`(暂未做)
3. 在"统计"区更新:
   - 总数 = M
   - 已完成 = M
4. 在"变更记录"末尾追加:
   ```
   YYYY-MM-DD HH:mm  需求新增  code-init 批量登记了 M 条现有功能需求(EXISTING-001 ~ EXISTING-NNN)
   ```

### 步骤 8 — 引导用户补齐编码规范

检查 `rules_has_files`:
- **若 false(`rules/` 不存在或为空)**,汇报:
  > ⚠️ `./assistants/rules/` 目录为空,后续 `code-design` / `code-plan` / `code-it` / `code-check` 都会从这里读规范作为约束,缺少规范会让这些技能退化为"无约束模式"。
  >
  > 建议下一步:调 `code-rule` 添加编码规范。
  >
  > 输入示例(可一次给多条):
  > - "Python 函数命名统一用 snake_case"
  > - "所有数据库操作必须走 ORM,禁止裸 SQL"
  > - "前端组件 props 必须显式声明类型"
  > - "提交信息必须用 Conventional Commits 格式"

- **若 true**,跳过本步,直接进入步骤 9

### 步骤 9 — 引导用户开启新开发版本

无论 `rules/` 是否为空,最后一步都向用户汇报:
> ✅ **code-init 完成**
>
> - 当前激活版本:`<初始版本号>`(基线)
> - 现有功能需求:`EXISTING-001` ~ `EXISTING-NNN`,共 M 条
> - 功能分析报告:`./assistants/<初始版本号>/INIT-REPORT.md`
> - 编码规范:`./assistants/rules/`(状态:有 N 个文件 / 空)
>
> **建议下一步**:
> 1. **(若 rules 为空)**先调 `code-rule` 补齐编码规范
> 2. **调 `code-version` 开启新的开发版本**(如 `V0.1.0`)
>    - 新版本会成为"激活版本"
>    - 后续所有 `code-require` / `code-design` / `code-plan` / `code-it` 等都落在新版本上
>    - 基线版本 `<初始版本号>` 保留作历史快照,不被修改
>
> 输入新版本号(推荐 `V0.1.0`),调 `code-version` 即可开启。

---

## 过程文档格式

### INIT-REPORT.md
见 `templates/INIT-REPORT.md`,核心区段:项目概述 / 技术栈 / 目录结构 / 核心模块与职责 / 入口与主流程 / 外部接口 / 数据模型 / 构建与运行 / 测试情况 / 可复用资产 / 已知问题/技术债 / 报告元信息。

### EXISTING-NNN/RESULT.md
见 `templates/existing-requirement.md`,核心区段:需求概述 / 现有实现位置 / 用户角色与场景 / 功能点(FR) / 关键接口 / 数据模型 / 验收标准(AC) / 关联功能 / 已知限制/技术债 / 变更记录。

---

## 与其他技能的关系

| 技能 | 关系 |
| --- | --- |
| `code-version` | 本技能**取代**其在初始版本创建上的角色(用快速通道,产物一致);之后调 `code-version` 开启新开发版本 |
| `code-rule` | 后续步骤 8 引导用户调它 |
| `code-require` | 后续 `EXISTING-NNN` 的 RESULT.md 格式与 `code-require` 的输出格式**保持一致**,使未来对这些功能的**修改**仍可走 `code-require`(增量) |
| `code-design` / `code-plan` / `code-it` / `code-check` | 后续都基于 `<初始版本号>/` 下的产物工作,无改动 |

## 衔接
- **下游**:`code-rule`(补齐规范)/ `code-version`(开启新版本)/ `code-require`(对现有功能做修改时)
- **上游**:无,通常由用户在项目接入时直接发起
- **横向**:本技能是"一次性引导",不应与 `code-version` 形成循环调用

## 不要做的事
- 不要在 `./assistants/` 已完全初始化后**未经用户确认**强行跑(情形 D 必须先警告)
- 不要修改项目源代码(本技能只读分析)
- 不要写 `./assistants/rules/` 下任何文件(那是 `code-rule` 的职责)
- 不要把分析结果写进 CWD 根目录(应写进 `./assistants/<初始版本号>/`)
- 不要给"现有功能"捏造未实现的细节(只描述代码中**可观测到**的行为)
- 不要让 EXISTING-NNN 的粒度过细(按用户可识别功能,而非按类/文件)
- 不要让 EXISTING-NNN 的粒度过粗(每个子模块应有独立的 EXISTING-NNN,除非它不可独立验证)
- 不要在版本看板的"需求清单"中**手动**维护状态(本技能一次性写完 M 条"已完成"后,未来对这些功能的修改会由 `code-require` 增量更新)
- 不要在 `INIT-REPORT.md` 中列出**所有**源文件(只列关键模块和代表性文件)
- 不要在 `code-init` 还没完成前就调 `code-rule` / `code-version`(那是后续步骤,本技能结束才轮到它们)
