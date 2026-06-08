# BUG-00002 缺陷详情 — SKILL.md 描述中"特定文件类型"字面

## 文档头
- 缺陷编号:BUG-00002
- 严重度:P0(阻断 — 让本项目"通用开发技能集"定位被弱化为"SKILL 专用"或"特定语言/特定项目专用",违背项目自我定位)
- 报告人:wangmiao
- 报告时间:2026-06-08 14:00
- 状态:修复规划中
- 当前负责人:wangmiao
- 修复时间:—
- 修复人:—
- 修复提交:—

## 缺陷描述

### 用户原始报告
本项目是通用开发技能集,并非只能开发 SKILL 或固定语言类型的技能,所以项目中不应该出现只针对特定文件类型/特定目录下的文件进行编码的要求,只有 `./assistants` 目录下的内容是本项目单独管理的,其他文件或目录都不应该被单独指定文件类型或目录。

### 典型例证
`code-it/SKILL.md` L16:
> 本技能是本技能库中**唯一**被允许修改 `<本仓库>/skills/*/SKILL.md` 的技能。

`skills/*/SKILL.md` 的文件描述明显是针对固定类型的项目,不应该出现在本项目的所有技能中。

### 期望行为
项目中若要描述用户实际使用时真实项目代码时,应该直接使用"`<本仓库>` 中除了 `./assistants` 目录中的其他代码文件"等类似的描述。

### 实际行为
多个 SKILL.md 在描述用户项目代码时,使用 `tests/` / `__tests__/` / `*.test.*` / `*.spec.*` 等"特定文件类型/特定目录"字面。

### 复现步骤
1. `Read plugins/code-skills/skills/code-it/SKILL.md` L16
2. `Read plugins/code-skills/skills/code-unit/SKILL.md` L13
3. `Read plugins/code-skills/skills/code-init/SKILL.md` L229
4. 观察:多个 SKILL.md 描述中使用"特定文件类型"字面,而本项目是"通用开发技能集",描述应泛化

### 涉及文件/模块
**A 类:`code-it` L16 描述性段(本轮报告的典型例子,1 处)**
**B 类:测试文件路径示例(用户项目语境,8 处):**
- `code-unit/SKILL.md` L13 / L318
- `code-init/SKILL.md` L229
- 6 个 `assistants-layout.md` 模板(`code-it` / `code-publish` / `code-unit` / `code-version` / `code-check` 等)

### 根因假设
本项目"通用开发技能集"定位未在所有 SKILL.md 描述中显式遵守。`code-it` L16 的"唯一被允许修改 `<本仓库>/skills/*/SKILL.md`"虽是描述本项目自身管理 SKILL.md 的硬约束(应保留),但其字面是"`skills/*/SKILL.md`"(特定文件类型),**也应**泛化。

## 修复方案
[fix-plan.md](./fix-plan.md)(4 步骤:code-it L16 + code-unit L13/L318 + code-init L229 + 静态校验)

## 修复实施
(由 `code-it BUG-00002` 产出 `fix-work-log.md`)

## 验证结果
(由 `code-it BUG-00002` 产出 `fix-test-results.md`)

## 修复日志
- 2026-06-08 14:00  登记  wangmiao 报告缺陷:SKILL.md 描述中"特定文件类型"字面违反本项目"通用开发技能集"定位
- 2026-06-08 14:20  修复规划  code-plan 已产出 fix-plan.md(4 步骤;A 类 1 处 + B 类 3 处;5 处不变量字面保留)

## 变更记录
- 2026-06-08 14:00  缺陷登记  code-fix 创建缺陷 BUG-00002(严重度 P0)  BUG-00002
- 2026-06-08 14:05  状态推进  BUG-00002 状态"报告"→"调查中"  BUG-00002
- 2026-06-08 14:20  计划完成  code-plan 完成 BUG-00002 修复方案(4 步骤,fix-plan.md);状态推进"调查中"→"修复规划中"  BUG-00002

## 不做边界
- **不**修改 `code-require` L530 / `code-design` L594 / `code-plan` L1093 / `code-fix` L433 中的"不修改 `plugins/code-skills/skills/*/SKILL.md` 任何文件"——这 4 处是**不变量字面**,描述的是"本项目自身管理 skills/ 目录"的硬约束,本项目是"开发技能库"必然管理 skills/ 目录;**保留字面**。
- **不**修改模板文件中的 `<如 pytest tests/test_module.py>` 之类示例占位符——模板是"用户消费的最终输出",示例要具体。
