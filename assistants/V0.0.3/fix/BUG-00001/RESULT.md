# 缺陷详情 — BUG-00001

- 缺陷编号:BUG-00001
- 缺陷标题:code-require/code-design/code-plan/code-fix 不能实际修改代码(职责混淆)
- 严重度:**P0**(架构职责分离违反,影响主流程"谁可以改代码"的核心契约)
- 状态:**报告**(本轮新登记,尚未开始调查)
- 报告人:wangmiao
- 报告时间:2026-06-06 22:41
- 当前负责人:wangmiao
- 所属版本:V0.0.3
- 关联技能:`code-require` / `code-design` / `code-plan` / `code-fix`

---

## 1. 缺陷描述

### 1.1 用户原始报告(2026-06-06 22:41)

> 当前 `/code-require` 技能执行时就已经对代码进行实际的修改了,这是错误的,`/code-require`、`/code-design`、`/code-plan`、`/code-fix` 这些技能不能实际修改代码,只能分析需求和缺陷、安排开发方案和计划,只有 `/code-it` 可以修改实际的工程代码,`/code-unit` 可以编写实际的单元测试。

### 1.2 期望行为

按 `CLAUDE.md` 与本仓库工作流约定,主流程管道应严格分离"分析 / 计划 / 实施"三种职责:

| 技能 | 职责 | 可修改的目录 |
| --- | --- | --- |
| `code-require` | 需求分析 | `./assistants/<version>/require/<REQ>/` 下的文档 + 看板"需求清单"区段 |
| `code-design` | 概要设计 | `./assistants/<version>/design/<REQ>/` 下的文档 + 看板"概要设计清单"区段 |
| `code-plan` | 详细设计 + 任务计划 | `./assistants/<version>/plan/<REQ>/` 下的文档 + 看板"详细设计与任务计划汇总"区段 |
| `code-fix` | 缺陷登记 + 跟踪 | `./assistants/<version>/fix/` 下的文档 + 看板"缺陷清单"区段 |
| **`code-it`** | **实施开发** | **CWD 下的项目源码**(唯一允许的生产代码改动场景) |
| `code-unit` | 单元测试 | CWD 下的测试文件 |

### 1.3 实际行为(本仓库 5 个历史 commit 违反职责分离)

`code-require` / `code-design` / `code-plan` 在历史上**实际修改了 3 个 SKILL.md**(即"工程代码"):

| 提交哈希 | 提交类型 | 修改的工程代码 | 修改行数 |
| --- | --- | --- | --- |
| `e69a58a` | `chore(code-require): REQ-00020 ...` | `code-design/SKILL.md` + `code-plan/SKILL.md` + `code-it/SKILL.md` | 12 + 131 + 74 行 |
| `6dee813` | `chore(code-require): REQ-00021 ...` | `code-design/SKILL.md` + `code-plan/SKILL.md` + `code-require/SKILL.md` | 3 SKILL.md 全部 |
| `3e1573e` | `chore(code-design): REQ-00005 ...` | `code-design/SKILL.md` | 47 行(步骤 0a + 步骤 N) |
| `e568328` | `chore(code-plan): REQ-00005 ...` | `code-plan/SKILL.md` | 47 行(步骤 0a + 步骤 N) |

**这 4 个 commit 全部"应该由 `code-it` 实施"**(本应是 `code-plan <REQ>` 拆分任务后,`code-it <TASK-...>` 实施修改 SKILL.md 的任务)。

**潜在风险**:
- **审计追溯断裂**:commit `e69a58a` 的 6 个 TASK 全部被登记为"开发=已完成",但实际它们在 `code-require` 阶段一次性提交,违反 INV-7(0 派生"更新看板"任务)和 INV-8(0 修改其他 `code-*` SKILL.md)的隐含约束(本应通过拆分任务,逐个 `code-it` 实施)
- **职责边界失守**:用户已显式报告"`code-require` ... 这些技能不能实际修改代码"
- **可观察影响**:从 git log 角度看,`code-require` 类型的 commit 含 SKILL.md 变更,使职责不可分
- **修复成本**:低(纯 SKILL.md 文档 + 流程约束;无运行时影响)

---

## 2. 涉及文件 / 模块

- `plugins/code-skills/skills/code-require/SKILL.md`(流程约束修订,不动)
- `plugins/code-skills/skills/code-design/SKILL.md`(流程约束修订,不动)
- `plugins/code-skills/skills/code-plan/SKILL.md`(流程约束修订,不动)
- `plugins/code-skills/skills/code-fix/SKILL.md`(流程约束修订,不动)
- `plugins/code-skills/skills/code-it/SKILL.md`(边界明确为"唯一可改代码")
- `plugins/code-skills/skills/code-unit/SKILL.md`(边界明确为"可改测试代码")
- `./assistants/rules/`(可能需要补充"技能职责分离"规范)

---

## 3. 根因分析(待 `code-plan BUG-00001` 阶段细化)

**初步假设**:
1. **历史惯例**:V0.0.1 / V0.0.2 时代,SKILL.md 改造"少而集中",`code-require` 阶段直接修改效率高,形成历史惯例
2. **流程约束弱化**:现 SKILL.md 中,`code-require` / `code-design` / `code-plan` 步骤虽提到"实施 / 编码"是 `code-it` 的事,但**没有显式的"禁止修改 CWD 项目源码"硬约束**
3. **未受审查**:本仓库历史 PR 未严格按"主流程 vs 实施"职责分离审查

**根因确认路径**:需 `code-plan BUG-00001` 在 `fix-plan.md` 中确认 + 设计修复方案

---

## 4. 修复方案

> 本节由 `code-plan BUG-00001` 产出 `fix-plan.md` 后回写链接

- **当前**:无(`code-plan` 尚未执行)
- **下一步**:调 `/code-skills:code-plan BUG-00001` 产出 `fix-plan.md`,方案应包含:
  1. SKILL.md 改造:在 `code-require` / `code-design` / `code-plan` / `code-fix` SKILL.md 中显式追加"禁止修改 CWD 项目源码"硬约束
  2. SKILL.md 改造:在 `code-it` SKILL.md 中显式追加"唯一允许的生产代码改动场景"声明
  3. SKILL.md 改造:在 `code-unit` SKILL.md 中显式追加"可改测试代码"声明
  4. 规范补充(可选):在 `./assistants/rules/` 下新增 `skill-responsibility.md`,固化"技能 → 目录映射"约束
  5. 历史 commit 处理:无需回滚(`e69a58a` / `6dee813` / `3e1573e` / `e568328` 4 个 commit 的实际改造是有价值的;只是流程需约束;本缺陷修复**仅约束未来**,不追溯)

---

## 5. 修复实施

> 本节由 `code-it BUG-00001` 阶段产出 `fix-work-log.md` 等后回写链接

- **当前**:无(`code-it` 尚未执行)
- **下一步**:调 `/code-skills:code-it BUG-00001` 实施 SKILL.md 改造(在 `code-plan` 拆分任务后,逐任务实施)

---

## 6. 验证结果

> 本节由 `code-it BUG-00001` 阶段产出 `fix-test-results.md` 后回写链接

- **当前**:无
- **验证方式**:本仓库 0 测试框架,验证手段为**静态校验**:
  - INV 自检:新增 4 个 INV(INV-10~13 需 `code-plan` 阶段定义)
  - 流程约束:`grep` 各 SKILL.md 关键字(`"禁止修改" / "唯一可改" / "CWD 项目源码"`)
  - 回归校验:对历史 4 个 commit 的实际 SKILL.md 改造**不**回滚(那是"流程违反但功能正确")

---

## 7. 修复日志

| 时间 | 操作 | 摘要 |
| --- | --- | --- |
| 2026-06-06 22:41 | 登记 | wangmiao 报告缺陷:code-require/code-design/code-plan/code-fix 不能实际修改代码(职责混淆) |

---

## 8. 变更记录

| 时间 | 变更类型 | 变更摘要 | 关联项 |
| --- | --- | --- | --- |
| 2026-06-06 22:41 | 缺陷登记 | code-fix 创建缺陷 BUG-00001(严重度 P0,状态 报告) | BUG-00001 |
