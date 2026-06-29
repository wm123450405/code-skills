# 概要设计 — REQ-00041 · 技能多语言模块化重构

> 上游:`./assistants/V0.0.4/require/REQ-00041/RESULT.md`
> 遵循规范:`./assistants/rules/skill-conventions.md` / `encoding-conventions.md` / `directory-conventions.md`(共 3 个文件)
> 设计目标:`--extensible`(完整覆盖 6 类语言 + 4 技能全重构)

## 设计目标

- 整体设计目标:`--extensible`
- 维度优先级:
  - 功能性:高
  - 扩展性/可维护性/可复用性:下沉到 code-plan 详设阶段

## 1. 设计概述

### 1.1 目标
将 4 个技能(code-design / code-plan / code-it / code-check)的 SKILL.md 从当前平均 ~1000 行/文件精简为 ~200-300 行的流程骨架,同时将语言/项目结构差异内容提取到各自的 `references/` 目录中,实现"加载即用、按需加载"。

### 1.2 核心思路
采用**两层架构**:
- **SKILL.md**(流程骨架层):仅保留步骤编号、步骤标题、决策点、references 引用指令
- **references/** (差异细节层):按语言和通用两类存放操作细节

### 1.3 架构图

```
技能调用
    │
    ├─ 1. 加载 SKILL.md(流程骨架, ~250 行)
    │       │
    │       ├─ "步骤 5: 探索项目结构"
    │       │     └─> 详见 references/common.md §5
    │       │     └─> 详见 references/<语言>.md §1(项目结构识别)
    │       │
    │       ├─ "步骤 9: 编译验证"
    │       │     └─> 详见 references/<语言>.md §2(构建命令检测)
    │       │
    │       └─ ...
    │
    ├─ 2. 检测项目语言(步骤 5 内)
    │       │
    │       ├─ package.json + scripts.test → nodejs
    │       ├─ pyproject.toml + [tool.pytest*] → python
    │       ├─ Cargo.toml → rust
    │       ├─ go.mod → go
    │       ├─ pom.xml → java-maven
    │       └─ build.gradle[.kts] → java-gradle
    │
    └─ 3. 加载 references/
            ├─ common.md(始终加载)
            └─ <语言>.md(按检测结果加载)
```

## 2. 上游引用

| 上游 | 路径 | 关键内容 |
| --- | --- | --- |
| 需求 | `require/REQ-00041/RESULT.md` | 8 FR / 5 NFR / 10 AC |

**对应 FR**:FR-1(语言检测) / FR-2(SKILL.md 骨架化) / FR-3(references/ 目录) / FR-4(6 语言文档) / FR-5(动态加载) / FR-6(简化目标) / FR-7(语言标签传递) / FR-8(common.md)

## 3. 规范遵循

| 规范文件 | 关键约束 | 本设计遵循 |
| --- | --- | --- |
| `skill-conventions.md §规则 1` | SKILL.md 必须含 name + description frontmatter | 保持不变 |
| `skill-conventions.md §规则 2` | SKILL.md 与 templates/ 不得包含开发痕迹 | 清理时遵循 |
| `encoding-conventions.md §规则 1-4` | 编码格式定义 | 不涉及新编码 |

## 4. 模块拆分

### 模块清单

| 模块名 | 路径 | 状态 | 职责 | 依赖 |
| --- | --- | --- | --- | --- |
| code-design/SKILL.md | `plugins/code-skills/skills/code-design/SKILL.md` | 修改既有 | 流程骨架,仅保留步骤编号+标题+决策点 | references/common.md |
| code-design/references/ | `plugins/code-skills/skills/code-design/references/` | 新增 | 通用流程细节 + 6 语言差异文档 | 无 |
| code-plan/SKILL.md | `plugins/code-skills/skills/code-plan/SKILL.md` | 修改既有 | 流程骨架,仅保留步骤编号+标题+决策点 | references/common.md |
| code-plan/references/ | `plugins/code-skills/skills/code-plan/references/` | 新增 | 通用流程细节 + 6 语言差异文档 | 无 |
| code-it/SKILL.md | `plugins/code-skills/skills/code-it/SKILL.md` | 修改既有 | 流程骨架,仅保留步骤编号+标题+决策点 | references/common.md |
| code-it/references/ | `plugins/code-skills/skills/code-it/references/` | 新增 | 通用流程细节 + 6 语言差异文档 | 无 |
| code-check/SKILL.md | `plugins/code-skills/skills/code-check/SKILL.md` | 修改既有 | 流程骨架,仅保留步骤编号+标题+决策点 | references/common.md |
| code-check/references/ | `plugins/code-skills/skills/code-check/references/` | 新增 | 通用流程细节 + 6 语言差异文档 | 无 |

### 模块详细说明

#### 模块 1/3/5/7: SKILL.md 流程骨架(模式统一)

四个技能的 SKILL.md 采用**统一模式**重构:

**保留的内容**:
- YAML frontmatter(name + description)
- 目标 / 适用场景 / 不适用
- 工作目录约定(简化)
- 输入 / 输出(简化)
- 工具使用约定(框架级)
- 工作流程步骤(仅编号 + 标题 + 1 句描述 + references 引用)
- 不要做的事(关键约束)
- 衔接

**移除的内容**(移到 references/):
- 所有语言相关的操作细节(构建命令检测、测试框架识别、monorepo 检测)
- 所有代码块/pseudocode(算法实现细节)
- 所有屏显模板(移到 common.md)
- 所有过程文档格式定义(移到 common.md)
- 所有边界与异常处理细节(移到 common.md 或语言文档)
- 命令行参数解析(移到 common.md)
- 模板填充步骤(移到 common.md)
- 标题解析工具函数(移到 common.md)
- 修改文件定位语义化约定(移到 common.md)
- 过程文档自适应判定(移到 common.md)
- 步骤 0a(git pull)细节(移到 common.md)
- 步骤 0b.0(code-auto 检测)细节(移到 common.md)
- 步骤 0b(设计目标确认)细节(移到 common.md)

#### 模块 2/4/6/8: references/ 目录(结构统一)

每个技能的 references/ 目录包含 7 个文件:

```
skills/<技能名>/references/
├── common.md          # 语言无关的通用流程细节
├── nodejs.md          # Node.js/TypeScript
├── python.md          # Python
├── rust.md            # Rust
├── go.md              # Go
├── java-maven.md      # Java(Maven)
└── java-gradle.md     # Java(Gradle)
```

## 5. 接口与数据结构

### 5.1 SKILL.md → references/ 引用接口

SKILL.md 通过以下格式引用 references 文档:

```markdown
### 步骤 5 — 探索项目结构与已有代码

> 详见 references/common.md §步骤5-通用流程
> 语言检测:详见 references/<语言>.md §1(项目结构识别)
```

### 5.2 语言检测接口

**输入**:CWD 下的模块根目录
**输出**:语言标签(`nodejs` / `python` / `rust` / `go` / `java-maven` / `java-gradle`)

检测逻辑:
```
module_dir/
├── package.json + scripts.test → nodejs
├── pyproject.toml + [tool.pytest*] → python
├── Cargo.toml → rust
├── go.mod → go
├── pom.xml → java-maven
├── build.gradle[.kts] → java-gradle
└── 无匹配 → unknown(兜底 common.md)
```

### 5.3 语言标签传递

在 `design/<REQ>/RESULT.md` 模块拆分表中新增"语言"列,下游技能读取该列加载对应 references。

### 5.4 references 文档内部结构

#### common.md 章节结构(统一)
```
§1 通用前置步骤(git pull / code-auto 检测 / 版本检测)
§2 设计目标确认流程
§3 过程文档自适应判定
§4 修改文件定位语义化约定
§5 通用项目探索流程(语言无关部分)
§6 通用屏显模板
§7 过程文档格式定义
§8 模板填充步骤
§9 标题解析工具函数
§10 边界与异常处理通用规则
§11 命令行参数解析
```

#### <语言>.md 章节结构(统一)
```
§1 项目结构识别(描述文件特征、目录约定)
§2 构建命令检测与执行
§3 测试框架识别与执行
§4 启动/运行命令检测
§5 Monorepo 声明文件解析(若适用)
§6 编码约定(命名、文件组织、错误处理风格)
§7 工具链检测(代码行数统计、lint、格式化)
```

## 6. 关键流程

### 6.1 技能调用流程(重构后)

```
1. 加载 SKILL.md(流程骨架, ~250 行)
2. 执行步骤 0-5(通用流程,引用 common.md)
3. 步骤 5 中检测项目语言
4. 加载对应 references/<语言>.md
5. 执行后续步骤(引用 common.md + <语言>.md)
```

### 6.2 语言检测流程(在 code-design 步骤 5 中)

```
1. Glob 模块根目录,查找描述文件
2. 按优先级匹配:package.json > pyproject.toml > Cargo.toml > go.mod > pom.xml > build.gradle
3. 多模块时:对每个模块独立检测
4. 写入 design/<REQ>/RESULT.md 模块表"语言"列
5. 输出语言标签清单
```

### 6.3 SKILL.md 简化流程

```
1. 读取当前 SKILL.md
2. 识别"语言相关"内容块(构建命令/测试框架/monorepo 检测等)
3. 提取到对应 references/<语言>.md
4. 识别"通用细节"内容块(屏显模板/过程文档格式/边界处理等)
5. 提取到 references/common.md
6. 替换原内容为 references 引用
7. 保留步骤编号+标题+决策点
8. 验证 frontmatter 不变
```

## 7. 三方依赖评估

本需求**不引入任何新的第三方依赖**。所有操作为 Markdown 文件编辑,使用现有工具链(Read / Write / Edit / Glob / Bash)。

## 8. 关键决策与不变量

### 关键决策

| ID | 决策 | 理由 |
| --- | --- | --- |
| D-1 | 每个技能独立 references/ | 各技能的语言差异内容不同,独立维护避免耦合 |
| D-2 | 先建 common.md + 6 语言文件骨架,再逐步填充 | 降低首次实施风险,后续按需补充 |
| D-3 | 语言检测在 code-design 步骤 5 中完成 | 该步骤已有"探索项目结构"职责,自然扩展 |
| D-4 | references 引用格式:`> 详见 references/<文件>.md §<章节>` | 简洁、可读、AI 可直接解析 |
| D-5 | 不删除原 SKILL.md 内容,而是移到 references | 保留所有细节,只是换位置 |

### 不变量

| ID | 不变量 | 约束 |
| --- | --- | --- |
| INV-1 | SKILL.md frontmatter 不变 | 字节级保留 |
| INV-2 | 工作流步骤编号不变 | 步骤 0-16 编号保持不变 |
| INV-3 | 看板字段约定不变 | 不触发 dashboard-conventions §规则 1 |
| INV-4 | 技能调用方式不变 | 用户仍用 `/code-design REQ-00041` 等 |
| INV-5 | 过程文档产出格式不变 | RESULT.md / PLAN.md 等格式不变 |
| INV-6 | 编码格式不变 | 沿用 encoding-conventions §规则 1-4 |

## 9. 关联设计

- 无同版本关联设计(本需求为 V0.0.4 首个需求)
- 跨版本:REQ-00034(code-it 模块识别)的 8 套声明文件解析逻辑可复用

## 10. 待澄清

- 无(已在 code-require 阶段澄清 3 个问题)

## 11. 变更记录

| 时间 | 变更类型 | 变更摘要 |
| --- | --- | --- |
| 2026-06-29 13:50 | 初始创建 | 概要设计完成(8 模块 / 5 决策 / 6 不变量) |