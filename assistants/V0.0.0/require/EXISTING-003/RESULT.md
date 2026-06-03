# 现有功能需求 — EXISTING-003:编码规范管理(code-rule)

> 本文档由 `code-init` 技能基于项目现有代码生成。
> 描述的是"**代码中已实现**"的功能,而非待开发的功能。
> 未来对该功能的**修改**应通过 `code-require`(增量更新本文件)进行。
> 最后更新:2026-06-03 18:10
> 适用版本:基线版本 `V0.0.0`

## 需求概述
`code-rule` 是项目级共享编码规范的管理技能,操作 `./assistants/rules/` 目录(跨版本共享),**不**做版本感知。用户用自然语言描述一条规范,技能主动用 `AskUserQuestion` 澄清模糊点,把规范丰富整理为结构化文档保存到 `rules/<分类>.md`。**所有**主流程技能(`code-require` ~ `code-review`)在执行时都会读取 `rules/` 作为只读强约束。

## 现有实现位置

| 维度 | 位置 |
| --- | --- |
| 主要文件 | `plugins/code-skills/skills/code-rule/SKILL.md`(277 行) |
| 关键函数/类 | (N/A) |
| 涉及文件数 | 3(SKILL.md + 2 个模板) |
| 大致代码量 | 约 320 行 |

### 关键代码位置(可选)
- `plugins/code-skills/skills/code-rule/SKILL.md` — 工作流(读输入 → 用 AskUserQuestion 澄清分类与细节 → 写 `rules/<分类>.md` → 引导)
- `plugins/code-skills/skills/code-rule/templates/rule.md` — 单条规则模板
- `plugins/code-skills/skills/code-rule/templates/assistants-layout.md` — rules/ 目录约定

## 用户角色与场景

### 角色
- **项目负责人 / 架构师**:在项目初期建立规范、在主流程中发现缺口追加

### 场景
- 新项目启动:一次性补齐命名/错误处理/安全/性能/测试等首批规范
- 主流程中追加:发现某模块用了 ESLint 禁用项,补一条规范阻止后续任务
- 团队 review 后形成新规范条目,统一沉淀

## 功能点(FR)

- **FR-1**:接收自然语言规范描述(可一次给多条,换行分隔)
- **FR-2**:用 `AskUserQuestion` 让用户确认分类(11 个枚举:功能架构/模块规划/命名/错误处理/接口定义/数据结构/安全/性能/测试/可观测性/提交规范/其他)
- **FR-3**:用追问补充细节(适用范围/强制级别/例外/反例/正例)
- **FR-4**:把规范整理为结构化 Markdown,追加到 `./assistants/rules/<分类>.md` 的"规则 N"小节
- **FR-5**:**不**修改 `./assistants/<版本号>/` 任何内容
- **FR-6**:**不**读/写 `.current-version`
- **FR-7**:可在 `code-version` 之前或之后随时调用(无顺序约束)

## 关键接口

### CLI
```
/code-skills:code-rule "Python 函数命名统一用 snake_case"
/code-skills:code-rule "所有数据库操作必须走 ORM\n禁止裸 SQL"
/code-skills:code-rule      # 交互式
```

### 写入
- `./assistants/rules/<分类>.md` — 新建或追加"规则 N"小节
- 分类文件名(kebab-case):如 `naming.md` / `error-handling.md` / `security.md` / `coding-style.md` / `testing.md` / `commit-convention.md` 等

## 数据模型(若适用)

| 实体 | 字段 | 约束 |
| --- | --- | --- |
| 规则文档 | `rules/<分类>.md` | 按分类聚合,文件内按"规则 1 / 规则 2 / ..."编号追加 |
| 规则条目 | 标题(规则 N:xxx) + 适用范围 + 强制级别(必须/建议) + 正例/反例 | 由 `templates/rule.md` 定义 |

## 验收标准(AC)

- **AC-1**:跑 `code-rule "命名规则"` 后,`./assistants/rules/<分类>.md` 被创建(新建)或追加(已有)
- **AC-2**:`rules/<分类>.md` 内容符合 `rule.md` 模板结构
- **AC-3**:`code-rule` **不**修改 `./assistants/<版本号>/` 下任何文件
- **AC-4**:`code-rule` **不**读写 `.current-version`
- **AC-5**:新规则对所有未完成的任务都生效(老任务不受影响,只对新提交/新增代码强约束)
- **AC-6**:用户可以一次给多条规范(换行分隔),逐条走 FR-2~FR-4

## 关联功能

| 关联编码 | 关联点 | 影响 |
| --- | --- | --- |
| EXISTING-004 | `code-require` 读 `rules/` 作为约束 | 规范空时 `code-require` 退化为"无约束模式" |
| EXISTING-005 | `code-design` 读 `rules/` 作为约束 | 同上 |
| EXISTING-006 | `code-plan` 读 `rules/` 作为约束 | 同上 |
| EXISTING-007 | `code-it` 读 `rules/` + `guidelines/coding-style.md` 作为约束 | 双源 |
| EXISTING-008 | `code-unit` 读 `rules/` 作为约束 | 影响测试规范 |
| EXISTING-010 | `code-review` 读 `rules/` + `checklists/review-checklist.md` | 双源 |

## 已知限制/技术债

- 分类固定 11 个枚举 + "其他",不支持用户自定义分类名(用户可在"其他"下写,但文件名固定为 `other.md`)
- 规则条目**不能**被软删除(只能编辑或追加新规则覆盖) —— 不保留删除历史
- 分类文件**不**自动按字母/时间排序,完全依赖追加顺序
- "强制级别"是文本字段,无 schema 校验

## 变更记录

| 时间 | 变更类型 | 变更摘要 | 关联项 |
| --- | --- | --- | --- |
| 2026-06-03 18:10 | 需求登记 | code-init 识别并登记现有功能 EXISTING-003 | EXISTING-003 |
