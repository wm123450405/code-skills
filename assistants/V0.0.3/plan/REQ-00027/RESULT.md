# REQ-00027 详细设计 — 优化 code-fix 流程(纯登记型)+ code-auto BUG 路径

## 1. 概述

- **上游**:`./assistants/V0.0.3/require/REQ-00027/RESULT.md`(v1,2026-06-08 15:20)
- **上游**:`./assistants/V0.0.3/design/REQ-00027/RESULT.md`(v1,2026-06-08 15:30)
- **版本**:V0.0.3
- **本设计的目标**:把概要设计"系统长什么样"落地为可直接编码的细节
- **本设计的范围**:2 SKILL.md(`code-fix` + `code-auto`)修改,0 新增模块,0 新增依赖

## 2. 模块详细化

### 2.1 模块 1:`code-fix/SKILL.md` 纯登记型重写

- **路径**:`plugins/code-skills/skills/code-fix/SKILL.md`
- **关键变更区段**:
  - §"目标":在"提供**缺陷从登记到关闭的全生命周期跟踪**" 之后,新增第 2 段"本技能仅产出 `fix/<BUG-NNN>/RESULT.md`,不实施代码改动、不产出 `fix-plan.md`、不推进'修复规划中'及之后状态;修复全流程请依次调 `code-plan` / `code-it` / `code-unit` / `code-check`"
  - §"适用场景":删"想实施代码修复(那是 `code-it` 的事)"——保留"紧急线上修复(走 hotfix 流程,不在本流水线)"作为反向提示
  - §"工作目录约定":删去"`fix-plan.md` / `fix-work-log.md` / `fix-compile-and-run.md` / `fix-test-results.md` / `deviations.md`"等下游文件——本技能不产出;保留 `fix/RESULT.md`(总览) + `fix/<BUG-NNN>/RESULT.md`(缺陷详情)
  - §"工作流程 步骤 1.2 已有编号分支":保留"^BUG-\\d{3}$"格式校验;不修改(本仓库实际用 5 位,本需求不修复 SKILL.md 模板失校)
  - §"工作流程 步骤 1.3 新建缺陷分支":保留;不修改
  - §"工作流程 步骤 3 读取现有材料":保留;不修改
  - §"工作流程 步骤 4 询问本轮状态推进":**候选目标状态表**改为:
    | 当前状态 | 候选目标状态 |
    | --- | --- |
    | (新建) | 报告 / 调查中 |
    | 报告 | 调查中 / 已关闭-非缺陷 / 已取消 |
    | 调查中 | 已关闭-非缺陷 / 阻塞 / 已取消 |
    | 阻塞 | 解除阻塞(回到报告中合适状态) / 已取消 |
    | 已关闭-非缺陷 | (终态) |
    | 已取消 | (终态) |
  - §"工作流程 步骤 5 补充本轮信息":删除"`→ 修复规划中`" / "`→ 修复编码中`" / "`→ 已修复-待验证`" / "`→ 已修复-已验证`" / "`→ 已关闭-*`"等推进提示;改为统一的"若需推进修复规划/编码/已修复等状态,请先调 `code-plan <BUG-NNN>` 产出 `fix-plan.md`"
  - §"工作流程 步骤 6 写缺陷详情":**保留**(本技能仍维护 `fix/<BUG-NNN>/RESULT.md` 主体结构);"修复方案"小节改为"若已调 `code-plan`,可链接 `fix-plan.md`"
  - §"工作流程 步骤 7 写缺陷总览":保留;不修改
  - §"工作流程 步骤 8 同步版本看板":保留;不修改
  - §"工作流程 步骤 9 引导下一步":**完全重写**:
    | 当前状态 | 下一步建议 |
    | --- | --- |
    | 报告 | 调 `code-plan <BUG-NNN>` 进入"修复规划中",产出 `fix-plan.md` |
    | 调查中 | 调 `code-plan <BUG-NNN>` 进入"修复规划中";若已规划,调 `code-it` 推进 |
    | 修复规划中 | (由 `code-plan` 推进;本技能不推进此状态之后) |
    | 修复编码中 | (由 `code-it` 推进) |
    | 已修复-待验证 | (由 `code-it` 推进) |
    | 已修复-已验证 | (由 `code-check` 推进) |
    | 已关闭-非缺陷 / 已取消 | (终态) |
  - §"过程文档格式":删去 `fix-plan.md` / `fix-work-log.md` 等(本技能不产出);仅保留 `fix/<BUG-NNN>/RESULT.md` + `fix/RESULT.md` 格式
  - §"不要做的事":新增"不产出 `fix-plan.md`(由 `code-plan` 产出)" + "不实施代码改动(由 `code-it` 实施)" + "不推进'修复规划中'及之后状态(由 `code-plan` / `code-it` / `code-check` 推进)"
- **状态归属**:仍归 `code-fix`(登记/分析类状态);后续状态归 `code-plan` / `code-it` / `code-check`
- **与概要设计的对应**:§2.2 状态机收敛 / §2.4 决策 1
- **符合的规范**:`skill-conventions.md` §规则 1 满足(frontmatter 0 改);`doc-conventions.md` §规则 1 满足(README 0 改);`commit-conventions.md` 满足(commit 沿用 `chore(code-fix):`)

### 2.2 模块 2:`code-auto/SKILL.md` 模式 C 增加

- **路径**:`plugins/code-skills/skills/code-auto/SKILL.md`
- **关键变更区段**:
  - §"输入" 步骤 1.1 检测用户输入:增加"模式 C"识别:首段匹配 `^BUG-\\d{5}$` → BUG 路径
  - §"输入" 表"两种调用模式" 扩展为"三种调用模式":
    | 模式 | 触发条件 | 调用形式 |
    | --- | --- | --- |
    | A:全流程 | 首段不匹配 `^from REQ-\\d{5}$` / `^BUG-\\d{5}$` | `/code-auto "<需求内容>"` |
    | B:续跑需求 | 首段匹配 `^from REQ-\\d{5}$` | `/code-auto from REQ-NNNNN` |
    | C:BUG 路径(本轮新增) | 首段匹配 `^BUG-\\d{5}$` | `/code-auto BUG-NNNNN` |
  - §"子技能调用表" 步骤 4:新增 BUG 路径子技能表:
    | 步骤 | 子技能 | 输入参数 | 期望产物 | 失败处理 |
    | --- | --- | --- | --- | --- |
    | 1 | `code-plan` | `<BUG-NNN>` | `fix/<BUG-NNN>/fix-plan.md` | 中断 + 报告 |
    | 2 | `code-it` | `<BUG-NNN>` | `fix/<BUG-NNN>/fix-work-log.md` 等 | 中断 + 报告 |
    | 3 | `code-unit` | `<BUG-NNN>`(条件触发) | `fix/<BUG-NNN>/fix-test-results.md` | 中断 + 报告 |
    | 4 | `code-check` | `<BUG-NNN>` | `fix/<BUG-NNN>/REVIEW-REPORT.md` | 中断 + 报告 |
    | 5 | 解析"必须改"列表 | — | (派生任务清单) | — |
    | 6 | 派生任务循环 | — | (回归) | — |
    | 7 | 完成报告 | — | `fix/<BUG-NNN>/auto-report.md` | 警告不中断 |
  - §"附加约束"步骤 4 后:沿用 REQ 路径的"`AskUserQuestion` 自动选推荐项"约束
  - §"步骤 7 报告"输出:BUG 路径完成时写 `fix/<BUG-NNN>/auto-report.md`(非 `require/<REQ-NNNNN>/auto-report.md`)
  - §"边界与异常":新增 E-18 "BUG 路径模式 C 错配"+ E-19 "`code-check` SKILL.md 缺失"等
  - §"不要做的事":新增"不修改 `code-plan` / `code-it` / `code-unit` / `code-check` 的核心工作流(本轮仅扩展 BUG 路径编排)"
- **状态归属**:本技能不直接负责任何 BUG 状态推进,仅编排子技能
- **与概要设计的对应**:§2.3 模式 C 状态机 / §2.4 决策 2 / 3
- **符合的规范**:`module-conventions.md`(沿用既有子技能编排模式);`commit-conventions.md` 满足(commit 沿用 `chore(code-auto):`)

## 3. 算法与逻辑

### 3.1 `code-fix` 步骤 4 状态推进表(重写后)

```
(新建) ───→ 报告 ───┐
                ↓
              调查中 ──┐
                ↓     │
       已关闭-非缺陷   │ (code-fix 不再推进)
                ↑     │
                └──┐  │
                   │  │
       (用户调 code-fix)
       (在已推进的状态基础上校验或不更新)
```

### 3.2 `code-auto` 模式识别算法(扩展后)

```
输入:args token
  ↓
拼接为字符串
  ↓
正则匹配(按顺序):
  1. ^from REQ-\\d{5}$    → 模式 B(续跑需求)
  2. ^BUG-\\d{5}$          → 模式 C(BUG 路径,本轮新增)
  3. 都不匹配              → 模式 A(全流程)
  ↓
按模式进入对应子技能编排
```

## 4. 数据结构完整变更

**0 变更**。本仓库是纯文档,无数据结构变更。

## 5. 接口细节

**0 变更**。本轮仅改 SKILL.md 文字描述,不修改任何函数签名或 API。

唯一"接口层面"变化:BUG 路径的 `auto-report.md` 输出路径:
- REQ 路径:`./assistants/<版本号>/require/<REQ-NNNNN>/auto-report.md`
- BUG 路径(本轮新增):`./assistants/<版本号>/fix/<BUG-NNN>/auto-report.md`

## 6. 异常处理

### 6.1 `code-fix` 重写后的边界
- 用户调 `code-fix` 复跑时,如果 BUG 状态是"修复规划中"或之后,`code-fix` 可读取但**不主动推进**——用户需调 `code-plan` / `code-it` / `code-check` 推进
- 若用户误调 `code-fix` 想推进"修复规划中"等状态,`code-fix` 步骤 9 引导建议明确提示

### 6.2 `code-auto` 模式 C 的异常
- E-18:BUG 路径模式 C 错配(例如 args 含 `BUG-00001-00001` 而非 `BUG-00001`)→ 提示格式错误
- E-19:`code-check` 缺失 → 沿用既有"`fix/<BUG-NNN>/RESULT.md` 缺失 → 提示先调 `code-fix`" 模式
- E-20:BUG 路径的中断恢复 → 沿用 `code-auto` 既有"无增量恢复"约定

## 7. 安全要求

N/A(本轮仅改 SKILL.md 文字描述)

## 8. 状态机 / 流程

参见 §3.1 / §3.2。

## 9. 性能与资源

N/A(本轮 0 改代码,0 新增依赖)

## 10. 测试要点

### 10.1 静态校验(本轮 0 改代码,无单元测试)
- `git diff` 校验 2 SKILL.md 的 frontmatter 字节级一致(0 改)
- `code-fix` SKILL.md 步骤 4 状态推进表仅含 5 个候选状态(报告 / 调查中 / 已关闭-非缺陷 / 已取消 / 阻塞)
- `code-auto` SKILL.md 模式识别表含 3 种模式(A / B / C),子技能调用表 BUG 路径含 7 步骤

### 10.2 端到端校验(后续 `code-check` 执行)
- 人工调 `code-fix "用户报告:某技能执行失败"` → 校验只产出 `fix/BUG-NNN/RESULT.md`,**不**产出 `fix-plan.md`
- 人工调 `code-auto BUG-00002` → 校验自动编排 `code-plan` → `code-it` → `code-unit`(条件) → `code-check`,写 `fix/BUG-00002/auto-report.md`

## 11. 规范遵循

详见 `rule-compliance.md`(0 冲突)。

## 12. 待澄清 / 未决项

| 编号 | 项 | 状态 |
| --- | --- | --- |
| Q1 | `code-fix` 步骤 6 中"修复方案小节"是否仍保留(指向未来 `code-plan` 产出) | 已决策:保留(链接到 `fix-plan.md`) |
| Q2 | `code-check` SKILL.md 与 `code-review` 内容是否完全等价 | 已决策:沿用 `code-review` 内容(本需求不修改) |

## 13. 变更记录

- `2026-06-08 15:35` 详细设计完成(3 任务,2 SKILL.md 修改,0 新增依赖)
