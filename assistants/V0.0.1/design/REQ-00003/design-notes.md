# 设计笔记 — REQ-00003
版本:V0.0.1

## 关键设计问题清单

### Q-1:核心架构 — 3 类型 + 共享识别引擎
- **方案 A:技能拆分** — 把 `code-rule` 拆为 3 个独立技能(`code-rule-a` / `code-rule-b` / `code-rule-c`)
  - 优点:职责清晰
  - 缺点:违反 FR-8"Type A 流程不变",3 个技能入口增加用户认知负担;NFR-4"最小化"
- **方案 B(本设计选定):单技能 + 3 子流程**
  - 优点:保持单一入口(用户视角);Type A 流程不变(FR-8);新子流程模块化扩展
  - 缺点:`code-rule/SKILL.md` 文档变长(从 272 行 → 估计 400+ 行)
- **关键设计**:
  1. 共享"类型识别引擎"(`code-rule` 步骤 4 之前)
  2. Type A / B / C 各自独立子流程(类似"插件式")
  3. Type A 现有 9 步骤流程**完全保持**(NFR-1)
  4. 步骤 4 增加"类型识别"分流点(FR-7)

### Q-2:Type A 6 分类的命名(基于 Q-4 决策)
- **本设计决定**(基于用户 Q-4 回答 + Q-8 H2):
  - **C-1 框架规范**:`framework-conventions.md`(新建,条件性)
  - **C-2 三方依赖规范**:`dependency-conventions.md`(新建,条件性)
  - **C-3 语言与命名规范**:`naming-conventions.md`(新建,默认)
  - **C-4 目录与模块规范**:`directory-conventions.md`(新建,默认;**承载原 `module-conventions.md` 内容**)
  - **C-5 代码书写规范**:`coding-style.md`(新建,默认)
  - **C-6 提交与合并规范**:`commit-conventions.md`(新建,条件性)
- **保留 4 个专项**(不动):
  - `dashboard-conventions.md`(看板)
  - `doc-conventions.md`(文档)
  - `marketplace-protocol.md`(marketplace 协议)
  - `skill-conventions.md`(技能)
- **1 个弃用**:
  - `module-conventions.md` → 内容迁移到 `directory-conventions.md`,旧文件保留并加 DEPRECATED 标记

### Q-3:Type B 字段决策(基于 Q-6 默认"不增加示例")
- **本设计决定**:
  - Type B 字段(5 个,REQU FR-5 锁定):指引简称 / 描述 / 适用场景 / 期望行为 / 来源
  - **不增加**"正面示例" / "反面示例"字段
  - 理由:AI 工作指引是"行为指令",不是"代码规范",示例作用有限;保持字段精简
- **与 Type A 字段对比**:
  - Type A 有 8 字段(含正反示例) — 适用于"代码可验证的规则"
  - Type B 有 5 字段(无示例) — 适用于"AI 行为指令"

### Q-4:Type C 字段决策(基于 Q-7 默认"两者并存")
- **本设计决定**:
  - **末尾追加模式**:`## 提示: <主题>`(二级标题)
  - **内联模式**:`### 提示: <字段>` 或 `#### 提示: <字段>`(三级/四级标题)
  - Type C 字段(4 个,REQU FR-6 锁定):字段/小节名 / 必填 / 简明说明 / 错误示例(可选)

### Q-5:类型识别引擎(FR-7)
- **算法**:
  1. **关键词扫描**:对用户描述进行关键词匹配
     - Type A 关键词:`规则` / `规范` / `约定` / `命名` / `提交` / `代码风格` / `依赖` / `框架` / `目录`
     - Type B 关键词:`CLAUDE.md` / `AI 工作` / `AI 约定` / `AI 写` / `AI 读` / `AI 应`
     - Type C 关键词:`模板` / `template` / `templates/` / 具体模板文件名(如 `plan.md` / `requirements.md`)
  2. **置信度计算**:
     - 命中 1 个唯一类型 + 命中 1+ 关键词 → **高置信度**
     - 命中 1 个唯一类型 + 命中 0 关键词但有语义提示 → **中置信度**(自动 + 显式确认)
     - 命中多类型 / 0 类型 → **低置信度**(必须显式追问)
  3. **显式覆盖**:用户可用 `"对 X 文件加 Y"` 形式显式指定(`X` 是文件名,`X ∈ {CLAUDE.md, templates/*, rules/*}`)

### Q-6:CLAUDE.md 插入位置
- **现状**:CLAUDE.md 有 7 个小节(L5 / L26 / L54 / L60 / L68 / L113 / L121),无"## AI 工作约定"
- **本设计决定**:
  - 插入位置:**文件末尾追加**(在 L127 `"完整技能清单..."` 之后)
  - 新小节标题:`## AI 工作约定(由 code-rule 维护)`
  - 二级小节用 `### 指引 N:<指引简称>` 编号
  - **不修改**任何现有小节(FR-10 边界)

### Q-7:多 commit 粒度
- **本设计决定**:**5 个 commit**(与实施阶段 `code-plan` 对齐)
  - Commit 1:SKILL.md 扩展(3 类型 + 6 分类 + 类型识别)
  - Commit 2:6 个新分类占位文件 + `module-conventions.md` DEPRECATED 标记
  - Commit 3:CLAUDE.md 新增"## AI 工作约定"小节(首次)
  - Commit 4:`templates/rule.md` 扩展(占位模式 + 引导模式)
  - Commit 5:`SKILL.md` 工作目录约定更新(11 个新分类列表)
  - **不合并** commit — 每类 1 commit,便于 review 与回退

### Q-8:`code-rule` SKILL.md 文档结构变更
- **变更清单**:
  - L3 frontmatter:`description` 中加"支持规则/CLAUDE.md/模板三种目标"(触发决策更明确)
  - L32-44 工作目录约定:11 个文件名更新(部分改名)
  - L117-128 步骤 4 分类识别:从 11 个旧分类 → 6 个新核心 + 5 个保留专项
  - L226-227 步骤 9 之后:新增"## 类型识别(自动 + 显式)"小节
  - L228-248 冲突处理:扩展为"Type A 冲突 + Type B 追加 + Type C 追加"3 类
  - 整体文档结构:在步骤 4 后插入"分流"决策点(FR-7)

## 关键决策与依据

| 决策 | 选定 | 依据 |
| --- | --- | --- |
| D-1 | 单技能 + 3 子流程(非 3 技能) | FR-8 + NFR-1 + NFR-4 |
| D-2 | 6 个新分类全为空占位 | Q-5 = H1 |
| D-3 | `module-conventions.md` 标记 DEPRECATED,内容迁移到 `directory-conventions.md` | Q-8 = H2 |
| D-4 | Type B 不加示例字段 | Q-6 默认 + 字段精简 |
| D-5 | Type C 末尾/内联两者并存 | Q-7 默认 + REQU FR-6 |
| D-6 | CLAUDE.md 末尾追加"AI 工作约定"小节 | REQU FR-5 + FR-10 |
| D-7 | 5 个 commit 粒度 | 便于 review + 回退 |
| D-8 | 类型识别:关键词 + 显式确认 | FR-7 锁定 Q-2 |

## 候选方案(已选定)

### 方案 A(选定):单技能扩展 + 5 commit
- 见 D-1 + D-7

### 方案 B(否决):3 技能独立
- 理由(否决):破坏 Type A 流程不变(FR-8);增加用户认知负担;违反 NFR-4 最小化

### 方案 C(否决):单技能单 commit
- 理由(否决):跨 11 文件 + 1 模板扩展,单 commit 体积过大;回退困难

## 不变量(本设计)

| # | 不变量 | 依据 |
| --- | --- | --- |
| INV-1 | 现有 Type A 9 步骤流程字段(关键词表除外)完全不变 | REQU FR-8 + NFR-1 |
| INV-2 | 6 个新分类文件仅含最小骨架(分类标题 + "由 code-rule 维护" + 1 个"## 规则 1: (待添加)"占位) | REQU FR-3 + Q-5=H1 |
| INV-3 | Type B 仅追加到 CLAUDE.md 末尾的"AI 工作约定"小节;不修改任何其他小节 | REQU FR-5 + FR-10 |
| INV-4 | Type C 仅追加到模板末尾的"提示"小节 或 内联到指定小节末尾;不修改任何其他内容 | REQU FR-6 + FR-10 |
| INV-5 | 不得修改 `marketplace.json` / `plugin.json` / 其他 9 个 SKILL.md frontmatter / `CLAUDE.md` 其他小节 / 任何 `assistants/V0.0.x/` 工作文件 | REQU FR-9 |
| INV-6 | 4 个保留文件(`dashboard-conventions.md` / `doc-conventions.md` / `marketplace-protocol.md` / `skill-conventions.md`)0 变更 | Q-8=H2 |
| INV-7 | `module-conventions.md` 仅追加 DEPRECATED 标记,**不**删除其内容(回退路径) | Q-8=H2 + 兜底 |
| INV-8 | `code-rule/SKILL.md` 步骤 0 工作目录约定更新为 11 个新分类列表;步骤 4 关键词表更新为 6 核心 + 5 专项 | 设计决策 D-1 + Q-8 |
| INV-9 | 5 个 commit 顺序:SKILL.md → 6 占位 + 1 弃用 → CLAUDE.md → 模板扩展 → SKILL.md 工作目录约定 | 设计决策 D-7 |

## 候选分类关键词表(用于 Type A 类型识别)

| 分类 | 关键词(中文) | 关键词(英文) | 默认/条件性 | 文件名 |
| --- | --- | --- | --- | --- |
| C-1 框架 | 框架 / 架构 / 框架选型 | framework / architecture | 条件性 | `framework-conventions.md` |
| C-2 三方依赖 | 依赖 / 第三方 / 库 / 包 | dependency / third-party / library / package | 条件性 | `dependency-conventions.md` |
| C-3 语言与命名 | 命名 / camelCase / snake_case / PascalCase / 前缀 / 后缀 | naming / camelCase / snake_case | 默认 | `naming-conventions.md` |
| C-4 目录与模块 | 目录 / 模块 / 包结构 / 文件组织 | directory / module / package | 默认 | `directory-conventions.md`(新建;`module-conventions.md` 弃用) |
| C-5 代码书写 | 代码风格 / 注释 / 错误处理 / 异常 / 性能 / 安全 / 编码规范 | coding-style / comment / error-handling | 默认 | `coding-style.md` |
| C-6 提交与合并 | 提交 / commit / 合并 / merge / PR / 分支 | commit / merge / PR / branch | 条件性 | `commit-conventions.md` |

**保留 4 个专项**(不参与关键词分类,在步骤 4 显式列出):
- `dashboard-conventions.md`(看板)— 用户说"看板" / "仪表盘" / "状态机"
- `doc-conventions.md`(文档)— 用户说"README" / "中英对仗"
- `marketplace-protocol.md`(marketplace)— 用户说"marketplace" / "plugin.json"
- `skill-conventions.md`(技能)— 用户说"SKILL.md" / "frontmatter"
