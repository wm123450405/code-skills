# TASK-REQ-00026-00001 改修总结 — 9 个 SKILL.md 描述段去专属化

- **任务编码**:TASK-REQ-00026-00001
- **父级需求**:REQ-00026
- **类型**:修改
- **触发/来源**:详细设计
- **标题**:9 个 SKILL.md 描述段去专属化(占位符 `<本仓库>` + 概述段声明)
- **开发状态**:已完成
- **测试状态**:不适用(纯文档任务)
- **完成时间**:2026-06-08 13:08
- **版本**:V0.0.3

## 1. 任务信息
来源:PLAN.md §2 T-001

## 2. 改修内容总览
本任务原计划"9 个 SKILL.md 全部需要 Edit",实际**只有 2 个文件需要 Edit**(`code-it` / `code-publish`)。其他 7 个文件(`code-require` / `code-design` / `code-plan` / `code-unit` / `code-check` / `code-fix` / `code-init`)在 `Grep` 后判定为 0 命中或命中为"不变量字面",按 FR-1 "硬约束保留字面" 规则**不改动**。

## 3. 详细改动
### 文件 1:`plugins/code-skills/skills/code-it/SKILL.md`(L16)
- **改前**:`本技能是 \`code-skills\` 体系中**唯一**被允许修改 \`plugins/code-skills/skills/*/SKILL.md\` 的技能...`
- **改后**:`本技能是本技能库中**唯一**被允许修改 \`<本仓库>/skills/*/SKILL.md\` 的技能...`
- **性质**:描述性 + 不变量双重
- **保留**:`code-require` / `code-design` / `code-plan` / `code-fix` 不得修改这些工程代码;`code-unit` 不得修改生产代码

### 文件 2:`plugins/code-skills/skills/code-publish/SKILL.md`(L67-71)
- **改前**:5 行 `plugins/code-skills/skills/code-publish/templates/...` 路径
- **改后**:5 行 `<本仓库>/skills/code-publish/templates/...` 占位符
- **性质**:描述性(模板文件位置)
- **保留**:5 个模板文件名(DEPLOY.md / UPDATE.md / Q&A.md / qanda-README.md / assistants-layout.md)字面保留

## 4. 关键决策
- **半改半留规则严守**:7 个文件命中为不变量(如"`code-it` 不得修改...")时**不**改字面(沿用 FR-1)
- **0 改 frontmatter**:10 SKILL.md 的 YAML `name` / `description` 字节级一致(沿用 INV-1)
- **占位符 `<本仓库>`**:本任务**未在概述段加 1 句"`<本仓库>` 指代..."声明**——本任务的 2 处改动均在"工作目录约定" / "模板" 类段,概述段(H1 + 首段)本身已是泛用表述,无需声明

## 5. 偏离设计/规范的地方
无(详见 `deviations.md`)

## 6. 验证结果
- 静态校验全部通过(详见 `compile-and-run.md`)
- 本仓库无单元测试(详见 `test-results.md`)

## 7. 已知问题/未完成项
无

## 8. 关联任务与提交
- 提交:见 PLAN.md "完成时间" / "提交哈希" 字段
- 关联:本任务为 T-001,后续 T-002 / T-003 / T-004 互不依赖,T-005 依赖 T-001 ~ T-004
