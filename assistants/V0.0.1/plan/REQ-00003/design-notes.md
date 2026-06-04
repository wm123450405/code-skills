# 设计笔记 — REQ-00003(plan 阶段)

更新时间:2026-06-04 09:15
版本:V0.0.1

## 关键设计问题清单

### Q-1:核心架构 — 单技能 + 3 子流程
- **继承 design 阶段决策 D-1**:单技能扩展,保持入口唯一;Type A 现有 9 步骤流程不变
- **本 plan 阶段细化**:
  - 步骤 0-3(不需要版本上下文 / 探查 / 兜底 / 收集)保持不变
  - 步骤 4 **微调**:原"拆分 + 初步归类"扩展为"拆分 + 类型识别 + 归类"3 段(详见 Q-2)
  - 步骤 5-9(Type A 流程)在 Type A 分支保持不变
  - **新增** Type B 子流程(M-3, 详见 §3.4)
  - **新增** Type C 子流程(M-4, 详见 §3.5)

### Q-2:类型识别引擎的实现位置(plan 阶段微调)
- **design 阶段方案**:类型识别作为"独立子流程",插入在步骤 3 收集描述与步骤 4 拆分归类之间
- **plan 阶段微调**:**合并到步骤 4 拆分归类之内**(用户答复 2026-06-04)
- **微调理由**:
  - 减少 SKILL.md 文档膨胀(原 272 行 → 估计 400+ 行,微调后 380 行左右)
  - 类型识别与"拆分+归类"逻辑上紧密耦合,作为步骤 4 的 3 个子阶段更紧凑
  - 保持 9 步骤主流程的"主干可见性",子流程(Type B/C)作为分支独立列出
- **微调后步骤 4 结构**:
  ```
  ### 步骤 4 — 拆分 + 类型识别 + 初步归类
  1. 把 <原始描述> 拆成 Rule[1..N]
  2. 对每条 Rule,做类型识别:
     a. 关键词扫描(关键词表)
     b. 置信度评估(高/中/低)
     c. 中/低置信度 → AskUserQuestion 显式确认
     d. 高置信度 + 唯一类型 → 标记 type ∈ {A, B, C}
  3. Type A → 走原 11 关键词分类表
     Type B → 跳到 §Type B 子流程(M-3)
     Type C → 跳到 §Type C 子流程(M-4)
  ```
- **对 design M-1 模块的影响**:
  - M-1 在 design 阶段是"独立子流程";在 plan 阶段被吸收到步骤 4
  - 模块 M-1 仍存在,但其内容(关键词表 + 置信度评估 + AskUserQuestion)并入步骤 4
  - 模块命名保留 M-1(便于追踪)但归类为"步骤 4 子模块",非"独立子流程"

### Q-3:Type A 6 分类的命名
- **继承 design 决策 D-3 / Q-4**:
  - C-1 框架规范:`framework-conventions.md`(新建,条件性)
  - C-2 三方依赖规范:`dependency-conventions.md`(新建,条件性)
  - C-3 语言与命名规范:`naming-conventions.md`(新建,默认)
  - C-4 目录与模块规范:`directory-conventions.md`(新建,默认;**承载原 module-conventions 内容**)
  - C-5 代码书写规范:`coding-style.md`(新建,默认)
  - C-6 提交与合并规范:`commit-conventions.md`(新建,条件性)
- **保留 4 个专项**:dashboard / doc / marketplace / skill(`skill-conventions.md` 等)
- **1 个弃用**:`module-conventions.md` → 内容迁移到 `directory-conventions.md`,旧文件保留并加 DEPRECATED 标记

### Q-4:Type B 字段(基于 Q-6 默认)
- **继承 design 决策 D-4**:
  - 字段(5 个):指引简称 / 描述 / 适用场景 / 期望行为 / 来源
  - **不增加**"正面示例" / "反面示例"字段

### Q-5:Type C 字段(基于 Q-7 默认)
- **继承 design 决策 D-5**:
  - 末尾追加模式:`## 提示: <主题>`(二级标题)
  - 内联模式:`### 提示: <字段>`(三级标题)
  - 字段(4 个,末尾模式;3 个,内联模式):字段/小节名 / 必填 / 简明说明 / 错误示例(末尾可选)

### Q-6:CLAUDE.md 插入位置
- **继承 design 决策 D-6**:
  - 插入位置:文件末尾追加"## AI 工作约定(由 code-rule 维护)"小节
  - 首次创建时,内容仅含"小节标题 + 1 个空指引占位"

### Q-7:多 commit 粒度(plan 阶段细化)
- **继承 design 决策 D-7**:**5 commit**
- **本 plan 阶段任务拆分**:7 任务(对应 5 commit,部分 commit 含多任务)
  | Commit | 任务 | 涉及文件数 |
  | --- | --- | --- |
  | 1 | T-001 扩展 SKILL.md(类型识别 + Type A/B/C 子流程文档化) | 1(SKILL.md) |
  | 2 | T-002 创建 6 个新分类占位文件 | 6 新 |
  | 3 | T-003 追加 module-conventions.md DEPRECATED 标记 | 1 修改 |
  | 4 | T-004 扩展 templates/rule.md(占位 + 引导模式) | 1 修改 |
  | 5 | T-005 追加 CLAUDE.md "AI 工作约定"小节 | 1 |
  | (合 1) | T-006 更新 SKILL.md 工作目录约定(11 个新分类列表) | 1(SKILL.md,合入 commit 1) |
  | (新增) | T-007 全仓库 Grep + 不变量自检 + commit 整理 | 0 文档 |

  修订:**T-006 合并到 T-001 同一 commit**(改 SKILL.md 两次属于同一文件的 2 次编辑,合并提交);T-007 独立 commit(审计)

  最终:7 任务 / 6 commit(commit 1 含 T-001 + T-006,commit 2-5 各 1 任务,commit 6 = T-007)

## 关键决策与依据

| 决策 | 选定 | 依据 |
| --- | --- | --- |
| D-PLAN-1 | 类型识别合并到步骤 4(微调 design M-1) | 用户 2026-06-04 答复 + 文档紧凑性 |
| D-PLAN-2 | 7 任务 / 6 commit(T-001 + T-006 合入 commit 1) | design D-7 5 commit 粒度 + 用户 7-9 任务答复 |
| D-PLAN-3 | T-007(全仓库 Grep + 不变量自检)独立 commit | 审计可独立回退 + 不污染功能性 commit |
| D-PLAN-4 | 任务编号 REQ-00003-001 ~ 007(7 位 5 位,数字段连续 001-007) | REQ-00002 已落地的新编码格式(5 位数字) |
| D-PLAN-5 | 测试状态统一为"不适用" | 全部为文档/规范/Markdown 文件处理,无编程逻辑可测 |

## 候选方案(已选定)

### 方案 A(选定):单技能扩展 + 5 commit + 7 任务
- 见 D-PLAN-1 / D-PLAN-2

### 方案 B(否决):3 技能独立
- 理由(否决):破坏 Type A 流程不变(FR-8);增加用户认知负担;违反 NFR-4 最小化

### 方案 C(否决):单技能单 commit
- 理由(否决):跨 11 文件 + 1 模板扩展,单 commit 体积过大;回退困难

## 不变量(本 plan 阶段继承 design 9 条 + 本 plan 阶段新增)

| # | 不变量 | 依据 |
| --- | --- | --- |
| INV-1 | 现有 Type A 9 步骤流程字段(关键词表除外)完全不变 | REQU FR-8 + NFR-1 |
| INV-2 | 6 个新分类文件仅含最小骨架(分类标题 + "由 code-rule 维护" + 1 个"## 规则 1: (待添加)"占位) | REQU FR-3 + design Q-5=H1 |
| INV-3 | Type B 仅追加到 CLAUDE.md 末尾的"AI 工作约定"小节;不修改任何其他小节 | REQU FR-5 + FR-10 |
| INV-4 | Type C 仅追加到模板末尾的"提示"小节 或 内联到指定小节末尾;不修改任何其他内容 | REQU FR-6 + FR-10 |
| INV-5 | 不得修改 `marketplace.json` / `plugin.json` / 其他 9 个 SKILL.md frontmatter / `CLAUDE.md` 其他小节 / 任何 `assistants/V0.0.x/` 工作文件 | REQU FR-9 |
| INV-6 | 4 个保留文件(`dashboard-conventions.md` / `doc-conventions.md` / `marketplace-protocol.md` / `skill-conventions.md`)0 变更 | design Q-8=H2 |
| INV-7 | `module-conventions.md` 仅追加 DEPRECATED 标记,**不**删除其内容(回退路径) | design Q-8=H2 + 兜底 |
| INV-8 | `code-rule/SKILL.md` 步骤 4 工作目录约定更新为 11 个新分类列表;关键词表更新为 6 核心 + 5 专项 | design D-1 + Q-8 |
| INV-9 | 6 commit 顺序:SKILL.md(含 T-001 + T-006) → 6 占位 → 1 弃用 → 模板扩展 → CLAUDE.md → 全仓库 Grep | design D-7 + 本 plan D-PLAN-2 |
| INV-10(plan 新增) | 任务 REQ-00003-001 ~ 007 全部为"文档/规范/Markdown 文件处理"类,测试状态=不适用(纯文档任务) | plan 阶段决策 D-PLAN-5 |
| INV-11(plan 新增) | Type B/C 严禁重写既有内容(INV-3/4)的 git 验证手段:commit 后跑 `git diff <file>` 应仅显示"+"行,无"-"行 | REQU FR-10 + AC-9 |

## 候选分类关键词表(用于 Type A 类型识别)

> 继承 design 阶段 §候选分类关键词表,本 plan 阶段不修改。

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
