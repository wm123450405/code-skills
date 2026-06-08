# REQ-00027 需求分析 — 优化 code-fix 流程(纯登记型)+ code-auto BUG 路径

## 文档头
- 需求编码:REQ-00027
- 创建时间:2026-06-08 15:10
- 状态:已完成(待评审)
- 最后更新:2026-06-08 15:10
- 版本:V0.0.3
- 描述:把 `code-fix` 技能重构为"纯登记型"(类似 `code-require`),并优化 `code-auto` 在检测到 BUG-NNN 任务时走 `code-plan` → `code-it` → `code-unit` → `code-check` 修复流程

## 1. 需求概述

### 1.1 用户原始诉求
> 优化 `/code-fix` 技能,该技能只登记并分析缺陷(类似 `/code-require` 技能),不进行直接修复。被登记的缺陷需要经过 `/code-plan` 技能进行比编码详细设计,在经过 `/code-it` 技能进行实际的编码修复和 `/code-unit` 技能补充单元测试,最后通过 `/code-check` 技能进行修复检查更新修复状态。再优化 `/code-auto` 技能,若检测到是缺陷修复任务,应该通过 `/code-plan`->`/code-it`->`/code-unit`->`/code-check`(可以直接复用原来针对 `/code-require` 创建需求的后续逻辑) 技能进行修复,并提交。

### 1.2 背景
当前 `code-fix` 技能承担 3 类职责:登记、跟踪、推进(状态机)。本需求聚焦"纯登记型"——即 `code-fix` 不产出 `fix-plan.md`,也不实施代码改动;后续修复全靠 `code-plan` → `code-it` → `code-unit` → `code-check` 编排。

`code-auto` 当前编排表(9 个子技能)未包含 BUG 路径,本需求要求 `code-auto` 在检测到 BUG-NNN 任务时,自动走缺陷修复流水线。

## 2. 背景与目标

### 2.1 背景
- 现有 `code-fix` SKILL.md 步骤 4 候选目标状态包含 "已修复-待验证" / "已关闭"等终态,意味着 `code-fix` 可直接关闭缺陷——这与"只登记"诉求冲突
- `code-auto` SKILL.md 步骤 4 "子技能调用表" 仅列 `code-it`,不调 `code-unit` / `code-check`;不识别 BUG-NNN 任务
- 现状下 BUG 修复流程散落在 `code-fix` + `code-plan` + `code-it` 各自的 SKILL.md 中,缺乏端到端编排

### 2.2 目标
- **目标 1**(重写 `code-fix`):`code-fix` 仅登记 + 分析缺陷,产出 `fix/<BUG-NNN>/RESULT.md`,**不**产出 `fix-plan.md`、**不**实施代码改动
- **目标 2**(优化 `code-auto`):`code-auto` 在检测到 BUG-NNN 任务时,自动编排 `code-plan` → `code-it` → `code-unit` → `code-check` 修复流程(可复用 `code-require` 路径逻辑)
- **目标 3**(状态机收敛):`code-fix` 不再负责"修复规划中 → 修复编码中 → 已修复-待验证 → 已关闭"等中间状态推进,这些状态由 `code-plan` / `code-it` / `code-check` 自动推进

### 2.3 非目标
- **不**改 `code-plan` / `code-it` / `code-unit` / `code-check` 的核心工作流(沿用既有)
- **不**改 `code-fix` 的缺陷元信息模型(状态、严重度、报告人等字段保持)
- **不**做中断恢复(本版本不实现"中断从断点恢复"功能,沿用 `code-auto` 既有约定)

## 3. 用户角色与场景

### 3.1 用户角色
| 角色 | 关注点 |
| --- | --- |
| 缺陷报告人 | 调 `code-fix` 快速登记 BUG,无需了解后续修复流程 |
| 修复实施人(AI 协作者) | 调 `code-plan` / `code-it` / `code-unit` / `code-check` 逐任务推进 |
| 项目维护者 | 通过 `code-dashboard` 看板查 BUG 全生命周期 |

### 3.2 场景
- **场景 1(用户调 `code-fix`)**:用户在 Claude Code 中调 `/code-fix 用户报告:某技能执行失败`,`code-fix` 仅产出 `fix/BUG-00002/RESULT.md` 并设置状态为"报告",**不**产出 `fix-plan.md`、**不**写代码
- **场景 2(用户调 `code-auto BUG-00002`)**:用户在 Claude Code 中调 `/code-auto BUG-00002`,`code-auto` 检测到 BUG-NNN 模式,自动走 `code-plan` → `code-it` → `code-unit` → `code-check` 修复流水线
- **场景 3(用户调 `code-plan BUG-00002`)**:用户显式调 `code-plan` 进入缺陷分支,产出 `fix-plan.md` 并推进 BUG 状态

## 4. 功能需求 (FR)

### FR-1:`code-fix` 重写为"纯登记型"
- **描述**:`code-fix` 仅产出 `fix/<BUG-NNN>/RESULT.md`,**不**产出 `fix-plan.md`、**不**实施代码改动、**不**推进"修复规划中"及之后的状态
- **范围**:重写 `plugins/code-skills/skills/code-fix/SKILL.md`
- **替换规则**:
  - 移除步骤 4 中"修复规划中 / 修复编码中 / 已修复-待验证 / 已修复-已验证 / 已关闭"等候选目标状态
  - 保留 "报告 / 调查中 / 已关闭-非缺陷 / 已取消 / 阻塞 / 解除阻塞"等纯登记/分析类状态
  - 步骤 5 `→ 修复规划中` 等推进提示改为"请先调 `code-plan <BUG-NNN>` 产出 `fix-plan.md`"
  - 步骤 6 修复日志 / 变更记录区段保留(状态变更仍记录)
- **不做**:不删除 `code-fix` 的子流程章节(缺陷分支仍可被 `code-plan` / `code-it` 间接触发)

### FR-2:`code-auto` 增加 BUG-NNN 任务识别
- **描述**:`code-auto` 在 args 首段匹配 `^BUG-\d{5}$` 时,进入"BUG 路径",调用顺序: `code-plan` → `code-it` → `code-unit`(条件触发,沿用 code-plan §"项目可测性"判断) → `code-check`
- **范围**:修改 `plugins/code-skills/skills/code-auto/SKILL.md`
- **替换规则**:
  - 步骤 1 增加"模式 C"模式识别:首段匹配 `^BUG-\d{5}$` → BUG 路径
  - 步骤 4 子技能调用表扩展,BUG 路径:
    1. `code-plan <BUG-NNN>` → 产出 `fix-plan.md`
    2. `code-it <BUG-NNN>` → 实施修复,产出 `fix-work-log.md` 等
    3. `code-unit <BUG-NNN>`(若 fix-plan.md 标记"项目可测性 = Y")→ 补充单元测试
    4. `code-check <BUG-NNN>` → 修复检查,更新 BUG 状态为"已修复-已验证" / "已关闭"
  - 步骤 6 解析"必须改"列表复用 `code-check` 的"必须改"区段(逻辑同 REQ 路径)
  - 步骤 7 完成时写 `fix/<BUG-NNN>/auto-report.md`(路径适配 BUG 而非 REQ)
- **继承**:BUG 路径的"任务循环"逻辑复用 REQ 路径的"任务总览" + "执行档案"模式

### FR-3:`code-fix` 状态机收敛
- **描述**:`code-fix` 推进的状态边界收敛为"报告 / 调查中 / 已关闭-非缺陷 / 已取消 / 阻塞";不推进"修复规划中 / 修复编码中 / 已修复-待验证 / 已修复-已验证 / 已关闭"等中间/终态
- **范围**:`code-fix/SKILL.md` 步骤 4 状态推进表
- **替换规则**:
  - 候选目标状态缩减为"报告 / 调查中 / 已关闭-非缺陷 / 已取消 / 阻塞"
  - "已关闭"等终态保留在 BUG 生命周期末端(由 `code-check` 推进后,`code-fix` 复跑时直接确认)

### FR-4:`code-auto` BUG 路径的"调用约束"与 REQ 路径一致
- **描述**:`code-auto` 在 BUG 路径下,所有 `AskUserQuestion` 自动选推荐项;不向用户提问
- **范围**:`code-auto/SKILL.md` 步骤 4 子技能调用表的"附加约束"
- **替换规则**:沿用 REQ 路径的"`AskUserQuestion` 自动选推荐项"约束(本仓库已具备,直接复用)

## 5. 非功能需求 / 约束 (NFR)

### NFR-1:向后兼容
- **不**改 `code-plan` / `code-it` / `code-unit` / `code-check` 的核心工作流(本需求仅改 `code-fix` + `code-auto`)
- **不**改 `fix/<BUG-NNN>/RESULT.md` 模板结构(本仓库已有模板)
- **不**改 `code-fix` 既有"修复日志 + 变更记录"区段

### NFR-2:状态推进路径一致性
- `code-fix` 仍维护"报告 → 调查中 → 修复规划中"的"前 3 段"状态推进
- "修复规划中 → 修复编码中 → 已修复-待验证 → 已修复-已验证 → 已关闭"由 `code-plan` / `code-it` / `code-check` 推进
- 看板"缺陷清单"区段的状态推进权限按此分工(本仓库既有约定)

### NFR-3:`code-auto` 不做中断恢复
- 沿用 `code-auto` 既有"无增量恢复"约定(本版本不实现"中断从断点恢复")

### NFR-4:`code-check` 复用 `code-review` 能力
- `code-check` 仍是 `code-review` 的重命名(REQ-00022 已完成重命名)
- BUG 路径的"必须改"列表解析与 REQ 路径一致

## 6. 页面与界面

N/A(本需求不涉及 UI)

## 7. 交互逻辑

### 7.1 `code-fix` 步骤 4 状态推进表(优化后)

| 当前状态 | 候选目标状态 |
| --- | --- |
| (新建) | 报告 / 调查中 |
| 报告 | 调查中 / 已关闭-非缺陷 / 已取消 |
| 调查中 | 已关闭-非缺陷 / 阻塞 / 已取消 |
| 阻塞 | 解除阻塞(回到报告中合适状态) / 已取消 |
| 已关闭-非缺陷 | (终态) |
| 已取消 | (终态) |

### 7.2 `code-auto` 模式识别表(扩展后)

| 模式 | 触发条件 | 调用形式 |
| --- | --- | --- |
| A:全流程需求 | 首段不匹配 `^from REQ-\d{5}$` / `^BUG-\d{5}$` | `/code-auto "需求内容"` |
| B:续跑需求 | 首段匹配 `^from REQ-\d{5}$` | `/code-auto from REQ-NNNNN` |
| C:BUG 路径(新增) | 首段匹配 `^BUG-\d{5}$` | `/code-auto BUG-NNNNN` |

### 7.3 `code-auto` BUG 路径子技能调用表(扩展后)

| 步骤 | 子技能 | 输入参数 | 期望产物 | 失败处理 |
| --- | --- | --- | --- | --- |
| 1 | `code-plan` | `<BUG-NNN>` | `fix/<BUG-NNN>/fix-plan.md` | 中断 + 报告 |
| 2 | `code-it` | `<BUG-NNN>` | `fix/<BUG-NNN>/fix-work-log.md` 等 | 中断 + 报告 |
| 3 | `code-unit` | `<BUG-NNN>`(条件触发) | `fix/<BUG-NNN>/fix-test-results.md` | 中断 + 报告 |
| 4 | `code-check` | `<BUG-NNN>` | `fix/<BUG-NNN>/REVIEW-REPORT.md` | 中断 + 报告 |
| 5 | 解析"必须改"列表 | — | (派生任务清单) | — |
| 6 | 派生任务循环 | — | (回归) | — |
| 7 | 完成报告 | — | `fix/<BUG-NNN>/auto-report.md` | 警告不中断 |

## 8. 数据与状态

### 8.1 `code-fix` 状态机收敛后的状态枚举
- 登记/分析类:`报告` / `调查中` / `已关闭-非缺陷`
- 推进类(由 `code-plan` 等推进):`修复规划中` / `修复编码中` / `已修复-待验证` / `已修复-已验证` / `已关闭`
- 阻塞/取消类:`阻塞` / `已取消`

### 8.2 状态推进权限表

| 状态 | `code-fix` 推进? | `code-plan` 推进? | `code-it` 推进? | `code-check` 推进? |
| --- | --- | --- | --- | --- |
| 报告 | ✓(用户调) | — | — | — |
| 调查中 | ✓(用户调) | — | — | — |
| 修复规划中 | ✗(仅复跑时校验) | ✓ | — | — |
| 修复编码中 | ✗ | ✗ | ✓ | — |
| 已修复-待验证 | ✗ | ✗ | ✓ | — |
| 已修复-已验证 | ✗ | ✗ | ✗ | ✓ |
| 已关闭 | ✗(终态) | — | — | ✓ |

## 9. 边界与异常

### 9.1 边界
- **不**改 `code-plan` / `code-it` / `code-unit` / `code-check` 的核心工作流
- **不**改 `fix/<BUG-NNN>/RESULT.md` 模板结构
- **不**做 BUG 路径的"中断从断点恢复"

### 9.2 异常
- **风险 1**:`code-fix` 不产出 `fix-plan.md` 后,后续 `code-plan BUG-NNN` 必须基于 `code-fix` 已产出的 `fix/<BUG-NNN>/RESULT.md`(由 `code-plan` 步骤 20 校验)。**缓解**:`code-plan` 步骤 20 已有"`fix/<BUG-NNN>/RESULT.md` 缺失 → 报错"逻辑
- **风险 2**:`code-auto` BUG 路径需明确区分"模式 C" 与"模式 A / B"。**缓解**:模式识别正则 `^BUG-\d{5}$` 与 REQ 路径 `^from REQ-\d{5}$` / 需求内容互不冲突
- **风险 3**:`code-check` 复用 `code-review` 能力的路径是否正确。**缓解**:本仓库 V0.0.3 实际文件名已为 `code-check`,SKILL.md 内容仍名 `code-review`(REQ-00022 改名未完成 100%覆盖)

## 10. 验收标准 (AC)

### AC-1:`code-fix` 重写后状态机
- **AC-1.1**:`code-fix/SKILL.md` 步骤 4 状态推进表候选状态仅含"报告 / 调查中 / 已关闭-非缺陷 / 已取消 / 阻塞"
- **AC-1.2**:`code-fix` 步骤 5 `→ 修复规划中` 提示改为"请先调 `code-plan <BUG-NNN>` 产出 `fix-plan.md`"
- **AC-1.3**:`code-fix` 步骤 9 引导改为"调 `code-plan` / `code-it` / `code-check` 推进后续状态"

### AC-2:`code-auto` BUG 路径
- **AC-2.1**:`code-auto/SKILL.md` 步骤 1 增加"模式 C"识别:首段匹配 `^BUG-\d{5}$` 进入 BUG 路径
- **AC-2.2**:`code-auto/SKILL.md` 步骤 4 BUG 路径子技能调用表包含 `code-plan` / `code-it` / `code-unit`(条件)/ `code-check`
- **AC-2.3**:`code-auto` BUG 路径完成时写 `fix/<BUG-NNN>/auto-report.md`(非 `require/<REQ-NNNNN>/auto-report.md`)
- **AC-2.4**:`code-auto` BUG 路径的"附加约束"沿用 REQ 路径的"自动选推荐项"

### AC-3:`code-check` 身份校验
- **AC-3.1**:`plugins/code-skills/skills/code-check/SKILL.md` 存在(本仓库 V0.0.3 现状)
- **AC-3.2**:`code-check/SKILL.md` 内容与 `code-review` 等价(仅 frontmatter `name` + H1 标题改为 `code-check`)

### AC-4:向后兼容
- **AC-4.1**:`code-fix` 调一次产出 `fix/BUG-NNN/RESULT.md`,**不**产出 `fix-plan.md`
- **AC-4.2**:`code-plan BUG-NNN` 仍能从 `fix/<BUG-NNN>/RESULT.md` 读并产出 `fix-plan.md`
- **AC-4.3**:`code-it BUG-NNN` 仍能从 `fix/<BUG-NNN>/fix-plan.md` 读并实施

## 11. 关联需求

- **REQ-00009**(V0.0.2):`code-unit` 守卫"项目可测性"(沿用,本需求不修改)
- **REQ-00022**(V0.0.3):`code-review` → `code-check` 重命名(本需求依赖此重命名)
- **REQ-00005**(V0.0.2):`code-require` / `code-design` / `code-plan` 首步拉取 + 末步提交模式(BUG 路径沿用)
- **BUG-00001**(V0.0.3):现有 BUG 修复全流程(本需求为该全流程的自动化编排)

## 12. 待澄清 / 未决项

| 编号 | 项 | 状态 |
| --- | --- | --- |
| Q1 | `code-fix` 步骤 6 中"修复方案小节"是否仍保留(指向未来 `code-plan` 产出) | 已决策:保留(链接到 `fix-plan.md`) |
| Q2 | `code-check` SKILL.md 与 `code-review` 内容是否完全等价,还是需要补充 BUG 路径的专项内容 | 已决策:沿用 `code-review` 内容(本需求不修改) |

## 13. 变更记录

- `2026-06-08 15:10` 需求初始,材料登记完成(共 1 条 args 输入)
- `2026-06-08 15:15` 澄清 4 项(已决策)
- `2026-06-08 15:20` 需求分析完成:4 FR / 4 NFR / 4 类 AC(共 12 条 AC)

## 不做边界(项目级硬约束)

- **不**改 `code-plan` / `code-it` / `code-unit` / `code-check` 的核心工作流
- **不**改 `fix/<BUG-NNN>/RESULT.md` 模板结构
- **不**改 `code-review` → `code-check` 重命名(REQ-00022 已完成)
- **不**改 marketplace.json / plugin.json 路径(本仓库元信息硬约束)
- **不**改 `./assistants/rules/` 项目级规范
- **不**实现中断恢复(沿用 `code-auto` 既有约定)
