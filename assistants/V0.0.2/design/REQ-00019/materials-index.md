# 材料登记 — REQ-00019
更新时间:2026-06-06 15:00
版本:V0.0.2

## 项目级规范
| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `./assistants/rules/skill-conventions.md` | SKILL 编写 | frontmatter `name` 字段字节级保留;L5 description 段可改 |
| `./assistants/rules/module-conventions.md` | 模块摆放 | SKILL.md 在技能根目录;`templates/` 子目录只放模板 |
| `./assistants/rules/dashboard-conventions.md` | 看板规范 | §规则 1:新增/删除/重命名区段/列/枚举值/字段语义需三同步 |
| `./assistants/rules/encoding-conventions.md` | 任务编号 | 5+5 位嵌套式 `TASK-REQ-NNNNN-NNNNN`;`TASK-BUG-NNNNN-NNNNN` 沿用 |
| `./assistants/rules/dependency-conventions.md` | 依赖 | 0 新增依赖强约束 |
| `./assistants/rules/marketplace-protocol.md` | 协议 | 0 改 `marketplace.json` / `plugin.json` |
| `./assistants/rules/commit-conventions.md` | 提交消息 | `chore(<scope>): <subject>` |
| `./assistants/rules/doc-conventions.md` | 文档 | 中英 README 同次提交 + 章节对仗 |
| `./assistants/rules/naming-conventions.md` | 命名 | kebab-case + 沿用既有前缀 |
| `./assistants/rules/directory-conventions.md` | 目录 | 过程文档摆放规则 |
| `./assistants/rules/coding-style.md` | 编码风格 | 沿用既有 SKILL.md 风格 |
| `./assistants/rules/framework-conventions.md` | 框架 | 不涉及(本需求纯文档重构) |
| `./assistants/rules/migration-mapping.md` | 迁移 | 不涉及(本需求纯文档重构) |

## 上游需求
- 来源:./assistants/V0.0.2/require/REQ-00019/RESULT.md (v1)
- 提取的 FR / NFR / AC 数量:8 FR / 11 NFR / ~30 AC / 11 INV
- 关键交叉点:FR-1 ~ FR-3 映射到 §5 组件图 / §6 功能域 1 / §7 模块 1;FR-4 ~ FR-7 映射到 §5 组件图 / §7 模块 2;FR-8 映射到 §3 非目标

## 上游概要设计
- 来源:无(本设计是元技能自身概要设计,无 design 上游)
- 提取的模块拆分 / 接口概要 / 数据结构 / 决策:0(本设计是首批 design 阶段产出)

## 项目现状(本次扫描)
### 项目类型
- **类型**:Meta-skills 工具集(仓库 `code-skills`)
- **框架**:Claude Code 技能系统(基于 SKILL.md frontmatter + Markdown 正文)
- **关键依赖**:无运行时依赖(纯文档技能集)

### 目录结构
- 顶层:`plugins/code-skills/skills/<技能名>/SKILL.md` + `templates/` 子目录
- 看板:`assistants/V0.0.2/RESULT.md` + `require/` / `design/` / `plan/` / `code/` / `test/` / `review/` / `fix/` 6 个子目录
- 规范:`./assistants/rules/` 13 个规范文件(项目级共享)

### 已有模块
| 模块/路径 | 职责 | 是否可复用 |
| --- | --- | --- |
| `plugins/code-skills/skills/code-plan/SKILL.md` | 详细设计 & 编码计划(版本感知) | **修改既有**(本需求核心改造) |
| `plugins/code-skills/skills/code-it/SKILL.md` | 任务实施 & 缺陷修复实施 | **修改既有**(本需求联动改造) |
| `plugins/code-skills/skills/code-fix/SKILL.md` | 缺陷登记与跟踪 | **不修改**(FR-8 强约束) |
| `plugins/code-skills/skills/code-design/SKILL.md` | 概要设计 | **不修改** |
| `plugins/code-skills/skills/code-dashboard/SKILL.md` | 只读型看板 | **不修改** |
| `plugins/code-skills/skills/code-review/SKILL.md` | 代码评审 | **不修改** |
| `plugins/code-skills/skills/code-auto/SKILL.md` | 自动开发编排 | **不修改** |
| `plugins/code-skills/skills/code-merge/SKILL.md` | worktree 自动合并 | **不修改** |
| `plugins/code-skills/skills/code-publish/SKILL.md` | 发布部署 | **不修改** |
| `plugins/code-skills/skills/code-version/SKILL.md` | 版本管理 | **不修改** |
| `plugins/code-skills/skills/code-init/SKILL.md` | 工程初始化 | **不修改** |
| `plugins/code-skills/skills/code-require/SKILL.md` | 需求分析 | **不修改** |
| `plugins/code-skills/skills/code-unit/SKILL.md` | 单元测试 | **不修改** |
| `plugins/code-skills/skills/code-plan/templates/plan.md` | 详细设计模板 | **复用既有** |
| `plugins/code-skills/skills/code-plan/templates/task-plan.md` | 任务计划模板 | **复用既有** |
| `plugins/code-skills/skills/code-plan/templates/fix-plan.md` | 旧 BUG 路径模板(留作历史) | **复用既有**(不删,不再引用) |

### 已有接口
- `code-plan/SKILL.md` 步骤 1-28 + 步骤 0a/0b + 步骤 N(本需求改造步骤 19-28A + 步骤 28A+1 新增)
- `code-it/SKILL.md` 步骤 1-25(本需求改造步骤 17/24/25 + frontmatter L5)
- `code-fix/SKILL.md` 步骤 1-3(沿用既有)
- `code-review/SKILL.md`(沿用既有,`code-review` 解析 `PLAN.md` 任务总览时,BUG 任务**同构** REQ 任务)

### 已有数据模型
- 任务编号体系:`TASK-REQ-NNNNN-NNNNN`(5+5 位嵌套式,沿用 `encoding-conventions §规则 1/3`);本需求新增 `TASK-BUG-NNNNN-NNNNN`
- 看板"任务清单"区段:12 列字段(任务编号 / 需求 / 类型 / 触发/来源 / 标题 / 开发状态 / 测试状态 / 涉及文件 / 完成时间 / 提交哈希 / 关联任务) — 沿用既有,BUG 任务**不**新增列
- 缺陷状态机:`报告` → `调查中` → `修复规划中` → `修复编码中` → `已修复-待验证` → `已修复-已验证` → `已关闭` — 沿用既有,由 `code-fix` 维护

### 已有第三方依赖
- 0 运行时依赖(纯文档技能集)
- 0 构建/测试工具(CLAUDE.md 严守)

### 编码与构建约定
- SKILL.md 编写:`name` 字段(技能标识)+ `description` 字段(触发条件)+ 12 节正文(目标 / 适用 / 不适用 / 目录 / 输入 / 输出 / 工具 / 步骤 / 边界 / 衔接 / 不要做)
- 任务编号分配:5+5 位嵌套式,任务序号自 00001 起递增
- commit 消息:`chore(<scope>): <subject>`

## 本次变更源(增量更新时)
| 变更源 | 检测方式 | 变化列表 |
| --- | --- | --- |
| 需求侧 | `./assistants/V0.0.2/require/REQ-00019/RESULT.md` 变更记录 | 0(本设计是首批) |
| 代码侧 | 重读 `code-plan/SKILL.md` L588-735 + `code-it/SKILL.md` L638-800 | 0(本设计是首批) |
| 规范侧 | `./assistants/rules/` 13 份 0 冲突 | 0 |
