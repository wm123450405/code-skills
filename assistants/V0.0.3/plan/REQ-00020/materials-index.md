# 材料登记 — REQ-00020
更新时间:2026-06-06 18:00
版本:V0.0.3

## 项目级规范

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `skill-conventions.md` | 技能规范 | §规则 1:frontmatter `name` 字节级保留 |
| `dashboard-conventions.md` | 看板规范 | §规则 1:任务清单 0 新增列/枚举/区段 |
| `encoding-conventions.md` | 编号规范 | §规则 1/3:任务编号 5+5 位嵌套式 |
| `marketplace-protocol.md` | 市场协议 | 0 改 `marketplace.json` / `plugin.json` |
| `module-conventions.md` | 模块规范 | §规则 1:过程文档摆放在 `<version>/plan/<REQ>/` 根目录 |
| `commit-conventions.md` | 提交规范 | `chore(<scope>): <subject>` 格式 |
| `doc-conventions.md` | 文档规范 | 中英 README 同步 |
| `naming-conventions.md` | 命名规范 | 0 新增文件名前缀 |
| `dependency-conventions.md` | 依赖规范 | 0 新增依赖 |
| `framework-conventions.md` | 框架规范 | N/A(本需求是 SKILL.md 文档改造) |
| `coding-style.md` | 编码风格 | 命名 / 注释 / 提交风格 |
| `migration-mapping.md` | 迁移映射 | N/A(本需求 0 改旧格式) |
| `directory-conventions.md` | 目录规范 | 子目录命名 |

## 上游需求

- 来源:`./assistants/V0.0.3/require/REQ-00020/RESULT.md`(v1,2026-06-06 16:30)
- 提取的 FR / NFR / AC 数量:8 FR / 8 NFR / ~40 AC / 9 INV
- 关键交叉点(每条 FR 对应的设计章节):
  - FR-1 → `plan/.../RESULT.md` §3.1 模块详细化(D-1)
  - FR-2 → §3.2 模块详细化(D-2)
  - FR-3 → §3.3 模块详细化(D-3)
  - FR-4 → §3.4 ~ §3.7 模块详细化(D-4)
  - FR-5 ~ FR-8 → 强约束(详 §12 规范遵循)

## 上游概要设计

- 来源:`./assistants/V0.0.3/design/REQ-00020/RESULT.md`(v1,2026-06-06 17:30)
- 提取的模块拆分 / 接口概要 / 数据结构 / 决策:
  - 7 项设计决策(D-1 ~ D-7)
  - 9 条不变量(INV-1 ~ INV-9)
  - 7 维度确认(整体=--extensible + 6 维度)
- 关键交叉点(每条 D 对应的设计章节):
  - D-1 → §3.1
  - D-2 → §3.2
  - D-3 → §3.3
  - D-4 → §3.4 ~ §3.7(M-1 ~ M-4)
  - D-5 → §10 性能(略增接受)
  - D-6 → §3.8 预留(--result / --plan)
  - D-7 → §3 任务粒度调整规则

## 项目现状(实现细节)

### 命名风格

- `code-design` / `code-plan` / `code-it` SKILL.md 既有命名:`### 步骤 0a` / `### 步骤 0b` / `### 步骤 0b.0` / `### 步骤 1` ...
- 本需求改造:`### 步骤 0b` / `### 步骤 0b.0` / `### 步骤 10A 末尾` 命名沿用
- 本需求 0 新增子段命名

### 错误模型

- SKILL.md 不抛错(纯文档);沿用 `AskUserQuestion` 取消 / 模板文件不存在 / 二进制格式的屏显 `⚠` 约定

### 既有相似功能的实现风格

- 步骤归并约定(REQ-00011 + REQ-00019):`> 引用:` 块引用同源段;沿用
- 任务粒度调整规则(REQ-00014):表格形式;本需求 +3 行沿用

### 既有测试用例的风格与覆盖度

- 本仓库 0 测试框架(沿用 REQ-00009 守卫判定);本计划所有任务"测试状态"="不适用"

### 可复用的工具函数/中间件

- `truncateTitle` / `formatReqTitle` / `formatTaskTitle` / `parseResultTitle` / `parsePlanTaskTitle`(REQ-00013 沿用)
- `writeDesignGoalsSection` / `readDesignGoalsFromDesign` / `adjustTaskGranularityByGoals`(REQ-00011 沿用)
- `preTaskGuard`(REQ-00010 沿用)

## 本次变更源

| 变更源 | 检测方式 | 变化列表 |
| --- | --- | --- |
| 需求侧(本需求) | 用户原文 4 子需求 | FR-1 ~ FR-8 全部锁定 |
| 概要设计侧(本概设) | 7 决策 + 9 不变量 | 详 `design/.../RESULT.md` §3 |
| 规范侧 | 0 | 0(本需求 0 改规范) |
| 代码侧 | 0 | 0(本需求改 SKILL.md,无 CWD 代码改动) |
