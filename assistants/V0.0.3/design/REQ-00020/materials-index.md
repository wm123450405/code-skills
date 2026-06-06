# 材料登记 — REQ-00020
更新时间:2026-06-06 17:30
版本:V0.0.3

## 项目级规范

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `skill-conventions.md` | 技能规范 | §规则 1:frontmatter `name` 字节级保留 |
| `dashboard-conventions.md` | 看板规范 | §规则 1:任务清单 0 新增列/枚举/区段 |
| `encoding-conventions.md` | 编号规范 | §规则 1/3:任务编号 5+5 位嵌套式 |
| `marketplace-protocol.md` | 市场协议 | 0 改 `marketplace.json` / `plugin.json` |
| `module-conventions.md` | 模块规范 | §规则 1:过程文档摆放在 `<version>/design/<REQ>/` 根目录 |
| `commit-conventions.md` | 提交规范 | `chore(<scope>): <subject>` 格式 |
| `doc-conventions.md` | 文档规范 | 中英 README 同步 |
| `naming-conventions.md` | 命名规范 | 0 新增文件名前缀 |
| `dependency-conventions.md` | 依赖规范 | 0 新增依赖 |
| `framework-conventions.md` | 框架规范 | 框架选型偏好(N/A 本需求) |
| `coding-style.md` | 编码风格 | 命名 / 注释 / 提交风格 |
| `migration-mapping.md` | 迁移映射 | 旧 → 新格式映射(N/A 本需求) |
| `directory-conventions.md` | 目录规范 | 子目录命名 |

## 上游需求

- 来源:`./assistants/V0.0.3/require/REQ-00020/RESULT.md`(v1,2026-06-06 16:30)
- 提取的 FR / NFR / AC 数量:8 FR / 8 NFR / ~40 AC / 9 INV
- 关键交叉点(每条 FR 对应的设计章节):
  - FR-1 → §3 步骤 0b 简化为 1 维度
  - FR-2 → §3 步骤 0b 扩展为 7 维度
  - FR-3 → §4 任务粒度调整规则 +3 行
  - FR-4 → §3 步骤归并 M-1 ~ M-4
  - FR-5 ~ FR-8 → 强约束(详 §4 规范遵循)

## 项目现状(本次扫描)

### 项目类型
- 类型:Claude Code 插件仓库(meta-skills 工具集)
- 关键资产:13 份 `code-*` 技能(`code-require` / `code-design` / `code-plan` / `code-it` / `code-unit` / `code-review` / `code-auto` / `code-version` / `code-init` / `code-merge` / `code-publish` / `code-fix` / `code-dashboard` / `code-rule`)
- 跨版本工作空间:`./assistants/V0.0.0/` / `V0.0.1/` / `V0.0.2/` / `V0.0.3/`

### 目录结构
- `plugins/code-skills/skills/<skill>/SKILL.md` — 技能提示词文档
- `plugins/code-skills/skills/<skill>/templates/` — 技能内置章节结构模板
- `assistants/rules/*.md` — 13 份项目级规范(跨版本共享,只读)
- `assistants/<version>/<dir>/<req-id>/` — 版本工作空间

### 已有模块(本需求涉及)
| 模块/路径 | 职责 | 是否可复用 |
| --- | --- | --- |
| `code-design/SKILL.md` 步骤 0a / 0b.0 / 0b / 0 / 1-15A / N | 概要设计主流程 | 是(本需求仅改 0b) |
| `code-plan/SKILL.md` 步骤 0a / 0a.0 / 0b.0 / 0b / 0 / 1-18A / N | 详设主流程 | 是(本需求改 0b.0 / 0b / 3 / 5 / 6 / 21 / 22 + 任务粒度表) |
| `code-it/SKILL.md` 步骤 0a / 0 / 1-16 / N | 编码主流程 | 是(本需求改 0a.7 E 边界 / 步骤 23) |

### 已有接口
- `code-design` 沿用既有 CLI(无新增参数)
- `code-plan` 沿用既有 CLI
- `code-it` 沿用既有 CLI
- **预留**:`--result` / `--plan` 模板参数(由 REQ-00021 实现)

### 已有数据模型
- "## 设计目标"小节(REQ-00011 沿用,本需求扩展 7 维度)

### 已有第三方依赖
- 0(本需求 0 新增依赖)

### 编码与构建约定
- 沿用既有 `commit-conventions` / `coding-style` / `naming-conventions`

## 命令行参数解析(本需求新增,REQ-00021 沿用)

> 本需求**不**实现 `--result` / `--plan`;预留语义给 REQ-00021。

## 关联需求(同版本)

## 跨版本关联(V0.0.2)
- REQ-00011:`code-design` / `code-plan` 步骤 0b 设计目标确认(本需求**改造**步骤 0b)
- REQ-00019:`code-plan` BUG 模式同构(本需求**保持** BUG 路径)
- REQ-00010:`code-it` 步骤 0a 前置任务守卫(本需求 0 修改守卫逻辑)
- REQ-00013:6 技能标题解析(本需求沿用 `formatReqTitle` 风格)
- REQ-00017:`code-plan` 不再为"更新看板"拆派生任务(本需求 INV-7 沿用)
- BUG-00001:脏标记文件修复(本需求沿用 24h 超时检测)

## 本次变更源
| 变更源 | 检测方式 | 变化列表 |
| --- | --- | --- |
| 需求侧(本需求) | 用户原文 4 子需求 | FR-1 ~ FR-8 全部锁定 |
| 概要设计侧(本概设) | 7 决策 + 9 不变量 | 详 RESULT.md §3 |
| 规范侧 | 0 | 0(本需求 0 改规范) |
| 代码侧 | 0 | 0(本需求改 SKILL.md,无 CWD 代码改动) |
