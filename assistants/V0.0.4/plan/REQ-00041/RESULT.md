# 详细设计 — REQ-00041 · 技能多语言模块化重构

> 上游需求:`require/REQ-00041/RESULT.md`
> 上游概要设计:`design/REQ-00041/RESULT.md`
> 遵循规范:`skill-conventions.md` / `encoding-conventions.md`

## 设计目标

- 整体设计目标:`--extensible`(沿用 design 阶段)
- 维度优先级:
  - 功能性:高
  - 扩展性/可维护性/可复用性/封装性/可读性:本项目为 Markdown 自然语言,不适用

## 1. 概述

本详细设计将概要设计中的 8 个模块展开为可直接编码的细节,包括:每个 SKILL.md 中保留/移除的内容清单、每个 references 文件的具体章节结构、语言检测的伪代码、以及任务拆分与依赖关系。

## 2. 上游引用

| 上游 | 路径 | 版本 |
| --- | --- | --- |
| 需求 | `require/REQ-00041/RESULT.md` | V0.0.4 |
| 概要设计 | `design/REQ-00041/RESULT.md` | V0.0.4 |

## 3. 规范遵循

| 规范 | 关键约束 | 本设计遵循 |
| --- | --- | --- |
| skill-conventions §规则 1 | name + description frontmatter | 不变 |
| skill-conventions §规则 2 | 不得包含开发痕迹 | 清理时移除 |
| encoding-conventions §规则 1-4 | 编码格式 | 不涉及 |

## 4. 模块详细化

### 模块 1: code-design/SKILL.md 精简

**路径**:`plugins/code-skills/skills/code-design/SKILL.md`
**动作**:Edit 精简,从 ~669 行缩减至 ~250 行

**保留内容**(字节级):
- YAML frontmatter(L1-3)
- `## 目标` ~ `## 不适用`(目标/适用场景/不适用)
- `## 工作目录约定(强制)`(简化版,仅目录树 + 路径约定)
- `## 输入` / `## 输出`(简化版,仅列表)
- `## 工具使用约定`(框架级,如"读激活版本:Read .current-version")
- `## 工作流程`(简化版,仅步骤编号+标题+references 引用)
- `## 衔接`
- `## 不要做的事`

**移除内容**(移到 references/):
- `## 过程文档自适应判定` → `references/common.md §3`
- `## 修改文件定位的语义化约定` → `references/common.md §4`
- `## 命令行参数解析` → `references/common.md §11`
- `## 模板填充步骤` → `references/common.md §8`
- `## 过程文档格式` → `references/common.md §7`
- 步骤 0a/0b.0/0b 操作细节 → `references/common.md §1-2`
- 步骤 5 子步骤(项目类型识别~可复用资产) → `references/common.md §5` + `references/<语言>.md §1`

**工作流程骨架**(简化后):
```markdown
### 步骤 0a — 拉取最新代码
> 详见 references/common.md §步骤0a

### 步骤 0b.0 — 调用上下文检测
> 详见 references/common.md §步骤0b.0

### 步骤 0b — 设计目标确认
> 详见 references/common.md §步骤0b

### 步骤 0 — 版本上下文检测
1. Read .current-version
2. 不存在 → 中止

### 步骤 1 — 收集需求编码
> 校验上游 RESULT.md 存在

### 步骤 2 — 创建工作目录
> mkdir -p design/<REQ>/

### 步骤 3 — 读取项目级规范
> 详见 references/common.md §步骤3

### 步骤 4 — 读取需求分析结果
> Read require/<REQ>/RESULT.md

### 步骤 5 — 探索项目结构
> 语言检测:见 references/<语言>.md §1
> 通用流程:见 references/common.md §5

### 步骤 6 — 检查 RESULT.md 是否存在
> 不存在 → 首次设计(7A-15A);存在 → 增量更新(7B-10B)

### 步骤 7A-15A — 首次设计
> 详见 references/common.md §步骤7A-15A

### 步骤 7B-10B — 增量更新
> 详见 references/common.md §步骤7B-10B

### 步骤 N — 末尾兜底提交
> 详见 references/common.md §步骤N
```

### 模块 2: code-design/references/ 创建

**路径**:`plugins/code-skills/skills/code-design/references/`
**动作**:新建 7 个文件

**文件清单与章节结构**:

`common.md`:
```
§1 步骤0a(git pull 细节 + 3 种失败处理)
§2 步骤0b.0(code-auto 上下文检测 + 24h 超时)
§3 步骤0b(设计目标确认 + 扩展性触发判定 + 自适应问题数)
§4 过程文档自适应判定(7 类过程文档判定准则 + 决策流程)
§5 修改文件定位语义化约定(禁止行号 + 结构化锚点)
§6 步骤5 通用项目探索(语言无关的 9 步子步骤)
§7 步骤7A-15A 首次设计流程(架构方案/澄清/模块拆分/接口/依赖/关联/撰写/看板同步)
§8 步骤7B-10B 增量更新流程(4 类变更源识别/局部更新/规范自检/同步)
§9 步骤N 末尾兜底提交(5 步 git 提交流程)
§10 过程文档格式(materials-index/rule-compliance 等)
§11 模板填充步骤(触发条件/执行流程/占位符映射)
§12 标题解析工具函数(truncateTitle/formatReqTitle/parseResultTitle)
§13 命令行参数解析(--result 参数)
§14 通用屏显模板
§15 通用边界与异常处理
```

`nodejs.md` / `python.md` / `rust.md` / `go.md` / `java-maven.md` / `java-gradle.md`:
```
§1 项目结构识别(描述文件特征/目录约定)
§2 构建命令检测(package.json scripts / Cargo build / go build / mvn / gradle / pip)
§3 测试框架识别(Jest/Vitest/Mocha / pytest / cargo test / go test / JUnit)
§4 启动/运行命令检测
§5 Monorepo 声明文件解析(pnpm-workspace/Cargo workspace/Maven modules)
§6 编码约定(命名/文件组织/错误处理风格)
§7 工具链检测(代码行数统计 tokei/cloc / lint / 格式化)
```

### 模块 3-8: code-plan / code-it / code-check(同构)

三个技能的 SKILL.md 精简和 references/ 创建遵循与模块 1-2 相同的模式,差异在于各技能 references/ 的内容不同:

**code-plan references/**:common.md 内容侧重任务拆分原则、PLAN.md 撰写规范;语言文档侧重实现细节探索
**code-it references/**:common.md 内容侧重编码原则、编译验证流程;语言文档侧重构建/测试/运行命令、monorepo 检测(步骤 8a.0)
**code-check references/**:common.md 内容侧重评审维度速查(14 维)、评审清单加载;语言文档侧重语言特定评审项

## 5. 算法与逻辑

### 5.1 语言检测算法(伪代码)

```
function detectLanguage(moduleDir: string): string {
  files = Glob(moduleDir + "/*")

  if exists(moduleDir + "/package.json"):
    pkg = Read(moduleDir + "/package.json")
    if pkg has "scripts.test" and pkg.scripts.test is non-empty:
      return "nodejs"

  if exists(moduleDir + "/pyproject.toml"):
    content = Read(moduleDir + "/pyproject.toml")
    if content matches "[tool.pytest]" or "[tool.pytest.ini_options]":
      return "python"

  if exists(moduleDir + "/Cargo.toml"):
    return "rust"

  if exists(moduleDir + "/go.mod"):
    return "go"

  if exists(moduleDir + "/pom.xml"):
    return "java-maven"

  if exists(moduleDir + "/build.gradle") or exists(moduleDir + "/build.gradle.kts"):
    return "java-gradle"

  return "unknown"
}
```

### 5.2 多模块语言检测

```
function detectAllLanguages(projectDir: string): Map<string, string> {
  // 1. 检测是否为 monorepo
  workspaceDirs = detectWorkspace(projectDir)  // 解析 pnpm-workspace/lerna/etc

  if workspaceDirs is non-empty:
    result = {}
    for each dir in workspaceDirs:
      result[dir] = detectLanguage(dir)
    return result

  // 2. 单模块项目
  return { ".": detectLanguage(projectDir) }
}
```

### 5.3 SKILL.md 简化算法

```
function simplifySkillMd(skillPath: string, refDir: string): void {
  content = Read(skillPath)

  // 1. 提取各代码块到 references
  extractSection(content, "过程文档自适应判定") → refDir + "/common.md §3"
  extractSection(content, "修改文件定位") → refDir + "/common.md §4"
  extractSection(content, "命令行参数解析") → refDir + "/common.md §11"
  extractSection(content, "模板填充步骤") → refDir + "/common.md §8"
  extractSection(content, "过程文档格式") → refDir + "/common.md §7"
  extractSection(content, "标题解析") → refDir + "/common.md §12"
  extractSection(content, "步骤 0a/0b/0b.0") → refDir + "/common.md §1-2"

  // 2. 提取语言相关内容
  extractLangContent(content, "构建命令") → refDir + "/<lang>.md §2"
  extractLangContent(content, "测试框架") → refDir + "/<lang>.md §3"
  extractLangContent(content, "monorepo") → refDir + "/<lang>.md §5"

  // 3. 替换原内容为 references 引用
  replace(content, "## 过程文档自适应判定", "> 详见 references/common.md §3")
  replace(content, "步骤 5 子步骤", "> 详见 references/common.md §5 和 references/<语言>.md §1")

  // 4. 保留 frontmatter 不变
  // 5. 保留步骤编号+标题不变
  // 6. 写入简化后的 SKILL.md
  Write(skillPath, simplified)
}
```

## 6. 接口细节

### 6.1 SKILL.md → references/ 引用接口

| 引用标记 | 指向 | 示例 |
| --- | --- | --- |
| `> 详见 references/common.md §<编号>` | 通用流程细节 | `> 详见 references/common.md §3` |
| `> 详见 references/<语言>.md §<编号>` | 语言差异细节 | `> 详见 references/nodejs.md §1` |
| `> 详见 references/<语言>.md §<编号>`(多语言) | 多语言文档 | `> 详见 references/nodejs.md §2, references/python.md §2` |

### 6.2 语言标签传递接口

**design/RESULT.md 模块表**:
```
| 模块名 | 路径 | 状态 | 职责 | 依赖 | 语言 |
| --- | --- | --- | --- | --- | --- |
| auth | src/auth/ | 修改既有 | 认证模块 | — | nodejs |
```

**下游读取**:`code-plan` / `code-it` / `code-check` 读取 `design/<REQ>/RESULT.md` 模块表"语言"列,加载对应 references 文档。

## 7. 异常处理

| 异常场景 | 处理 |
| --- | --- |
| 语言检测失败(unknown) | 仅加载 common.md,屏显 `⚠ 无法识别项目语言,使用通用流程` |
| references 文件缺失 | 屏显 `⚠ references/<语言>.md 缺失,使用通用流程` |
| SKILL.md 简化后步骤编号不匹配 | 交叉验证(步骤 17A)中捕获并修正 |
| 多语言项目 references 文件过多 | 仅加载涉及的语言(最多 6 个),每个 ~200-400 行 |

## 8. 安全要求

- 不删除原始 SKILL.md 内容(已通过 git 历史保留)
- references/ 文件创建前检查目录存在性
- SKILL.md frontmatter 字节级保留(不修改 L1-3)

## 9. 状态机/流程

```
任务 1(架构) → 任务 2-5(4 技能重构,可并行)
  │
  ├─ 任务 2: code-design 重构
  │     ├─ 2a: 创建 references/ + 7 文件
  │     └─ 2b: 精简 SKILL.md
  │
  ├─ 任务 3: code-plan 重构
  ├─ 任务 4: code-it 重构
  └─ 任务 5: code-check 重构
```

## 10. 性能与资源

- 每任务:Markdown 文件编辑,~100-300 行写入/编辑操作
- 无编译/构建/测试步骤
- 无外部依赖

## 11. 测试要点

- 验证:每个 SKILL.md 简化后 frontmatter 不变
- 验证:每个 SKILL.md 简化后步骤编号完整
- 验证:每个 references/ 目录包含 7 个文件
- 验证:语言检测算法对 6 类描述文件正确识别
- 验证:references 引用标记格式正确

## 12. 关联

- 跨版本:REQ-00034(模块识别)的 8 套声明文件解析逻辑在 code-it/references/ 中复用

## 13. 待澄清

- 无

## 14. 变更记录

| 时间 | 变更类型 | 变更摘要 |
| --- | --- | --- |
| 2026-06-29 13:50 | 初始创建 | 详细设计完成(5 模块详细化 / 3 算法 / 5 任务) |