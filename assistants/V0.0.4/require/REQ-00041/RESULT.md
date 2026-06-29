# 需求提示词文档 — REQ-00041 · 技能多语言模块化重构

> 上游:`./assistants/V0.0.4/require/REQ-00041/`(材料源自用户对话)
> 遵循规范:`./assistants/rules/`(若存在)

## 1. 需求概述

当前 `code-design` / `code-plan` / `code-it` / `code-check` 四个技能的 `SKILL.md` 文件合计约 4110 行,其中混杂了大量与具体开发语言/项目结构绑定的内容(构建命令检测、测试框架识别、monorepo 声明文件解析等),导致每次加载技能时消耗大量 token。

本需求将这 4 个技能重构为"流程骨架 + 语言差异文档"的两层架构:
- **SKILL.md**(主文件):仅保留步骤编号、步骤标题、决策点、上下游引用
- **references/**(语言差异文档):按语言/模块类型独立存放构建、测试、项目结构等差异说明
- **运行时动态加载**:根据项目实际开发环境,只加载 SKILL.md + 对应语言的 references 文档

## 2. 背景与目标

### 背景
- 一个项目工程可能包含多个子模块,每个子模块可能使用不同的开发语言
- 也可能整个工程不含子模块,仅一个模块就是工程本身
- 当任何一个需求进入 design 阶段时,需要对需要改写的模块的开发语言进行判断
- 当前 4 个技能文件膨胀严重,token 消耗大

### 目标
1. 将 4 个技能的 SKILL.md 精简为纯流程骨架
2. 将语言/项目结构差异内容独立到 references/ 目录
3. 按 6 类开发语言分别建立差异说明文档
4. 运行时按项目实际环境动态加载对应文档
5. 显著减少 token 消耗

## 3. 用户角色与场景

- **技能维护者**:新增一种开发语言支持时,只需新增一个 references 文档,无需修改 SKILL.md
- **技能调用者(AI)**:加载技能时自动获得精简的流程骨架 + 项目实际需要的语言差异文档
- **项目开发者**:多模块项目自动识别各模块语言,加载对应差异文档

## 4. 功能需求(FR)

### FR-1: 开发语言检测(design 阶段触发)
- **触发时机**:`code-design` 步骤 5(探索项目结构与已有代码)
- **检测范围**:需求涉及的模块/子模块
- **检测内容**:
  - 模块根目录的描述文件类型(package.json / Cargo.toml / go.mod / pom.xml / build.gradle / pyproject.toml)
  - 模块的构建系统
  - 模块的测试框架
  - 模块的 monorepo 工具(pnpm-workspace / lerna / nx / turbo / Maven modules / Cargo workspace)
- **输出**:每个模块的"语言类型"标签,传递给下游 `code-plan` / `code-it` / `code-check`
- **降级**:无法识别时,标记为 `unknown`,兜底使用通用流程

(源自:用户需求描述)

### FR-2: SKILL.md 流程骨架化
- **适用范围**:`code-design` / `code-plan` / `code-it` / `code-check` 四个技能
- **保留内容**:步骤编号 + 步骤标题 + 关键决策点 + 上下游引用 + 工具使用约定(框架级)
- **移除内容**:所有与特定语言/构建系统/测试框架绑定的操作细节
- **引用方式**:在步骤中通过 `> 详见 references/<语言>.md §<章节>` 引用语言差异文档
- **简化程度**:激进简化 —— 步骤描述仅保留编号和标题,细节全部下沉到 references

(源自:用户需求描述 + 澄清"激进简化")

### FR-3: references/ 目录结构
- **位置**:每个技能独立维护自己的 `references/` 目录
  ```
  skills/code-design/references/
  skills/code-plan/references/
  skills/code-it/references/
  skills/code-check/references/
  ```
- **共通文档**:每个 references/ 目录下包含一份 `common.md`(语言无关的通用流程细节)
- **语言文档**:每个 references/ 目录下按语言分别建立文档

(源自:用户需求描述 + 澄清"每个技能独立 references/")

### FR-4: 按语言建立差异文档
- **覆盖 6 类语言/模块类型**:
  1. `nodejs.md` — Node.js / TypeScript(npm/pnpm/yarn + Jest/Vitest/Mocha)
  2. `python.md` — Python(pip/poetry + pytest)
  3. `rust.md` — Rust(Cargo + cargo test)
  4. `go.md` — Go(go mod + go test)
  5. `java-maven.md` — Java(Maven + JUnit)
  6. `java-gradle.md` — Java(Gradle + JUnit)
- **每份语言文档包含章节**:
  - §1 项目结构识别(描述文件特征、目录约定)
  - §2 构建命令检测与执行
  - §3 测试框架识别与执行
  - §4 启动/运行命令检测
  - §5 Monorepo 声明文件解析(若适用)
  - §6 编码约定(命名、文件组织、错误处理风格)
  - §7 工具链检测(代码行数统计、lint、格式化)
- **文档长度**:每份语言文档应控制在 200-400 行

(源自:用户需求描述 + 澄清"全部 6 类")

### FR-5: 运行时动态加载
- **加载逻辑**:
  1. 加载技能 SKILL.md(流程骨架)
  2. 检测项目实际开发环境(从 CWD 或模块根目录)
  3. 加载 `references/common.md`(通用流程细节)
  4. 对每个涉及的语言类型,加载对应的 `references/<语言>.md`
  5. 多模块多语言时,加载多份语言文档
- **加载时机**:技能启动时(步骤 0 之后,步骤 3-5 之前)
- **降级**:
  - 语言无法识别 → 加载 `common.md` 兜底
  - references 文件缺失 → 加载 `common.md` + 屏显警告

(源自:用户需求描述)

### FR-6: 内容简化与 token 减少
- **目标**:SKILL.md 文件从当前平均 ~1000 行缩减到 ~200-300 行
- **策略**:
  - 步骤描述从多段详细说明缩减为"步骤编号 + 标题 + 1 句描述"
  - 代码块/pseudocode 移到 references
  - 边界与异常处理细节移到 references
  - 屏显模板移到 references
  - 过程文档格式定义移到 references
- **度量**:4 个技能 SKILL.md 合计从 ~4110 行降至 ~1000-1200 行(减少 70%+)

(源自:用户需求描述 + 澄清"激进简化")

### FR-7: 设计阶段语言判断
- 当任一需求进入 design 阶段时,`code-design` 必须:
  1. 识别需求涉及的所有模块
  2. 对每个模块判断其开发语言
  3. 将语言标签写入 `design/<REQ>/RESULT.md` 的模块拆分区段
  4. 将语言标签传递给下游 `code-plan` / `code-it` / `code-check`
- 下游技能读取语言标签,加载对应 references 文档

(源自:用户需求描述)

### FR-8: 通用流程细节文档(common.md)
- 每个技能的 references/ 目录下包含 `common.md`
- 内容:语言无关的通用流程细节
  - 决策树/流程图
  - 通用边界条件与异常处理
  - 通用屏显模板
  - 通用过程文档格式
  - 与语言无关的检查项/校验规则
- 所有技能调用时都加载 `common.md`

(源自:分析推断 —— 需要区分"语言相关"和"语言无关"的细节)

## 5. 非功能需求 / 约束(NFR)

### NFR-1: 向后兼容
- 现有技能调用方式不变(用户仍用 `/code-design REQ-00041` 等)
- 现有工作流步骤编号不变
- 现有看板字段约定不变

### NFR-2: 无功能回归
- 重构后 4 个技能的功能行为与重构前一致
- 所有现有过程文档产出格式不变
- 所有现有看板同步逻辑不变

### NFR-3: 可扩展性
- 新增一种语言支持只需:
  1. 在 4 个 references/ 目录下各新增一份 `<语言>.md`
  2. 在语言检测逻辑中新增一条识别规则
- 无需修改任何 SKILL.md

### NFR-4: 性能
- 动态加载 references 文档不增加额外 IO 开销(所有文件在同目录下)
- 语言检测在 Glob 扫描阶段自然完成,不增加额外步骤

### NFR-5: 可维护性
- 每个语言文档独立,修改一种语言不影响其他语言
- common.md 修改需谨慎(影响所有语言)
- 语言文档之间不相互引用(保持独立)

## 6. 页面与界面

本需求不涉及 UI 界面。产出物为 Markdown 文档。

## 7. 交互逻辑

### 7.1 技能调用流程(重构后)
```
用户调用 /code-design REQ-00041
  → 步骤 0: 版本检测
  → 步骤 0a: git pull
  → 步骤 1: 收集需求编码
  → 步骤 2: 创建工作目录
  → 步骤 3: 读取规范
  → 步骤 4: 读取需求
  → 步骤 5: 探索项目结构
    → 5.1 检测模块语言(FR-1)
    → 5.2 加载 references/common.md
    → 5.3 加载 references/<语言>.md (每个模块)
    → 5.4 执行项目探索(详见 references)
  → 后续步骤同现有流程
```

### 7.2 语言检测决策树
```
module_dir/
├── package.json + scripts.test → Node.js/TypeScript
├── pyproject.toml + [tool.pytest*] → Python
├── Cargo.toml → Rust
├── go.mod → Go
├── pom.xml → Java(Maven)
├── build.gradle[.kts] → Java(Gradle)
└── 无匹配 → unknown(兜底 common.md)
```

## 8. 数据与状态

### 8.1 模块语言标签
在 `design/<REQ>/RESULT.md` 的模块拆分表中新增"语言"列:
```
| 模块名 | 路径 | 状态 | 职责 | 依赖 | 语言 |
| --- | --- | --- | --- | --- | --- |
| auth | src/auth/ | 修改既有 | 认证模块 | — | nodejs |
```

### 8.2 语言标签传递
- `code-design` → 写入 `design/<REQ>/RESULT.md` 模块表
- `code-plan` → 读取模块表,在任务详情中注明语言
- `code-it` → 读取任务语言标签,加载对应 references
- `code-check` → 读取任务语言标签,加载对应 references

## 9. 边界与异常

| ID | 场景 | 处理 |
| --- | --- | --- |
| E-1 | 模块语言无法识别 | 标记为 `unknown`,加载 `common.md` 兜底,屏显警告 |
| E-2 | references 文件缺失 | 加载 `common.md`,屏显 `⚠ references/<语言>.md 缺失,使用通用流程` |
| E-3 | 多模块多语言 | 加载所有涉及语言的 references 文档 |
| E-4 | 空项目(无源码) | 仅加载 `common.md`,跳过语言检测 |
| E-5 | 既有技能无 references/ | 屏显 `⚠ references/ 目录不存在,使用 SKILL.md 内嵌流程`,不阻断 |

## 10. 验收标准(AC)

| ID | 验收标准 |
| --- | --- |
| AC-1 | `code-design/SKILL.md` 从 ~669 行缩减至 ≤300 行,且仅包含步骤骨架 |
| AC-2 | `code-plan/SKILL.md` 从 ~1187 行缩减至 ≤350 行,且仅包含步骤骨架 |
| AC-3 | `code-it/SKILL.md` 从 ~1551 行缩减至 ≤400 行,且仅包含步骤骨架 |
| AC-4 | `code-check/SKILL.md` 从 ~703 行缩减至 ≤300 行,且仅包含步骤骨架 |
| AC-5 | 4 个技能的 references/ 目录各包含 1 份 `common.md` + 6 份语言文档 |
| AC-6 | 语言检测在 `code-design` 步骤 5 中正确识别 6 类语言 |
| AC-7 | 运行时加载:仅加载 SKILL.md + common.md + 对应语言文档 |
| AC-8 | 现有技能调用方式不变,工作流步骤编号不变 |
| AC-9 | 所有现有过程文档产出格式不变 |
| AC-10 | 新增一种语言支持只需新增 references 文档,不修改 SKILL.md |

## 11. 关联需求

### 同版本
- 无(本需求为 V0.0.4 首个需求)

### 跨版本
- REQ-00034(code-it 模块识别):本需求的语言检测逻辑与 REQ-00034 的模块识别逻辑重叠,需整合
- REQ-00018(code-version CWD 描述文件同步):6 类描述文件清单与本需求重合,可复用识别逻辑

## 12. 待澄清 / 未决项

1. **references 文档的加载机制**:AI 如何"动态加载"references 文件? 是通过 Read 工具读取,还是通过技能系统内置机制? 当前方案:技能 SKILL.md 中通过 `> 详见 references/<语言>.md` 引用,AI 自行 Read 对应文件。(假设:无需额外机制,利用现有 Read 工具)

## 13. 变更记录

| 时间 | 变更类型 | 变更摘要 |
| --- | --- | --- |
| 2026-06-29 13:50 | 初始创建 | 需求分析完成(共 8 条 FR / 5 条 NFR / 10 条 AC) |