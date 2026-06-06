# 修复方案 — BUG-00001

- 缺陷编号:BUG-00001
- 所属版本:V0.0.2
- 文档版本:v1
- 状态:已锁定
- 责任人:wangmiao
- 创建:2026-06-06 14:00
- 最近更新:2026-06-06 14:00
- 当前版本:v1
- **主题**:code-auto 调用子技能时子技能仍会手动选架构设计目标
- 链接:`./assistants/V0.0.2/fix/BUG-00001/RESULT.md`
- 依据规范:`./assistants/rules/` 下 13 个文件

## 设计目标

- 整体设计目标:`--minimal`(沿用 `code-fix` 调查采纳 — 修复方案极简)
- 维度优先级:
  - 功能性:**高**(必须修复 BUG)
  - 健壮性:**高**(脏标记文件异常情况全部走 `⚠` 屏幕输出)
  - 扩展性:**—**(本修复**不**引入新抽象层,沿用 V0.0.1 既有的"脏标记文件"模式)
  - 可维护性:**—**(1 文件修改 + 0 新增抽象)

## 1. 缺陷摘要

| 字段 | 值 |
| --- | --- |
| 缺陷编号 | BUG-00001 |
| 标题 | code-auto 调用子技能时子技能仍会手... |
| 严重度 | P0 |
| 当前状态 | 报告(本文件产出后推进为"修复规划中") |
| 报告时间 | 2026-06-06 13:45 |
| 报告人 | wangmiao |

## 2. 根因定位

### 关键事实(沿用 investigation.md)

1. `code-auto` D-8 零修改契约保持:`code-auto` 不向子技能传任何特殊参数(沿用 V0.0.1 既有 + REQ-00007 锁定)
2. `code-auto` 期望"完全无人确认":用户使用 `/code-auto "<需求>"` 时,所有 `AskUserQuestion` 应被自动选推荐项(沿用 code-auto §"子技能 prompt 模板"约束)
3. 子技能侧:`code-design` 步骤 0b 触发 `AskUserQuestion` 1-5 问(沿用 REQ-00011 / REQ-00018 既有),子技能**没有**"调用上下文检测"机制

### 根因(精准定位)

`code-auto` 的"自动选推荐项"约束**只在 `code-auto` 自己的 prompt 模板中声明**(子技能 prompt 模板注入),但子技能**本身**在执行 `AskUserQuestion` 时没有"我在被 `code-auto` 调用吗?"的检测逻辑。

**关键缺口**:`./assistants/` 目录下**没有**任何"调用上下文标记"文件,子技能**无法** Read 任何状态以判断"是否在 `code-auto` 上下文中"。

## 3. 修复方案(选定 + 候选 + 理由)

### 选定方案:方案 A3 — 脏标记文件(`./assistants/.code-auto-running`)

**核心思路**:
1. `code-auto` 步骤 0 后立即 `touch ./assistants/.code-auto-running`
2. `code-auto` 步骤 7 完成后立即 `rm ./assistants/.code-auto-running`
3. 子技能(主要是 `code-design` 步骤 0b + `code-plan` 步骤 0b)在触发 `AskUserQuestion` 前,先 `Read` 该文件:
   - 文件存在 → 自己在被 `code-auto` 调用 → **跳过** `AskUserQuestion`,直接采纳默认值/推荐项
   - 文件不存在 → 用户手动调子技能 → 正常触发 `AskUserQuestion`

**与 D-8 零修改契约的兼容性**:
- D-8 原文:"`code-auto` 不向子技能传任何特殊参数"(沿用 V0.0.1 既有)
- 脏标记文件**不**是"prompt 参数",而是"状态文件"(子技能通过文件系统 Read 检测)
- **D-8 修订建议**:从"完全不向子技能传任何特殊参数"修订为"不向子技能传 prompt 参数(状态文件除外)"

### 候选方案(否决)

#### 候选 A1:环境变量(`process.env.CODE_AUTO_MODE`)
- **否决理由**:设环境变量是"传特殊参数"的一种形式,**违反** D-8 零修改契约(严格解释)
- **优点**:实现简单
- **缺点**:与 D-8 不兼容

#### 候选 A2:检查 argv
- **否决理由**:依赖外部 CLI 实现,不稳定(不同 Claude Code 版本 / 操作系统 argv 格式不同)

#### 候选 A4:检查父进程命令行
- **否决理由**:需 `ps` 等工具,Windows 兼容性差

## 4. 涉及文件与变更

### 4.1 修改文件清单(2 个)

| 文件 | 修改类型 | 关键变更 |
| --- | --- | --- |
| `plugins/code-skills/skills/code-auto/SKILL.md` | **修改**(需 D-8 修订) | 步骤 0 后增加 `touch ./assistants/.code-auto-running`;步骤 7 完成后(成功/异常/中止任一情况)增加 `rm -f ./assistants/.code-auto-running`(保证退出时清理) |
| `plugins/code-skills/skills/code-design/SKILL.md` | **修改** | 步骤 0b 触发 `AskUserQuestion` **前**增加"调用上下文检测"分支:若 `./assistants/.code-auto-running` 存在 → 跳过 `AskUserQuestion`,直接采纳 `--balanced` 默认值写入 `design/.../RESULT.md` "## 设计目标" 小节 |

### 4.2 修改文件清单(2 个 — 同等修改,沿用同模式)

| 文件 | 修改类型 | 关键变更 |
| --- | --- | --- |
| `plugins/code-skills/skills/code-plan/SKILL.md` | **修改** | 步骤 0b 同 `code-design` 增加"调用上下文检测"分支 |
| `plugins/code-skills/skills/code-require/SKILL.md` | **修改**(可选) | 若本技能有 `AskUserQuestion` 触发点(查证后),增加相同"调用上下文检测"分支 |

### 4.3 不修改文件清单(明确)

- 其他 7 个 `code-*` SKILL.md(`code-fix` / `code-review` / `code-merge` / `code-publish` / `code-dashboard` / `code-unit` / `code-init` / `code-version`)— **暂不**修改(本修复聚焦 `code-design` / `code-plan` / `code-require` 3 个有明确 `AskUserQuestion` 触发点的技能;其他技能留作 v2 follow-up,详 §6 风险与回退)
- `code-fix` 当前已使用 `AskUserQuestion` 步骤 4(询问本轮状态推进)— **不**修改(缺陷登记是用户主动行为,不应被 `code-auto` 调用)

### 4.4 关键变更(锚点语义化)

#### 变更 1:`code-auto/SKILL.md`

- **锚点 A**:`§工作流程` 段后(步骤 0 完成后 + 步骤 1 之前)插入新步骤:
  ```
  ### 步骤 0b — 设置 code-auto 运行标记(本需求新增)

  - 在 `./assistants/` 下创建空标记文件 `.code-auto-running`
  - 子技能(主要 code-design / code-plan / code-require)Read 该文件判断是否在 code-auto 上下文中
  - D-8 修订:本步骤是状态文件设置,**不**是 prompt 参数
  - 异常处理:`touch` 失败 → 屏幕输出 `⚠ 无法设置 code-auto 标记,子技能可能仍会触发 AskUserQuestion` + **不**中断
  ```

- **锚点 B**:`§状态机/流程` 段后(步骤 7 完成后)追加清理:
  ```
  ### 步骤 7 收尾 — 清理 code-auto 运行标记

  - 在步骤 7 的"完成分支"/"中止分支"/"中断分支"**三处**全部追加 `rm -f ./assistants/.code-auto-running`
  - 异常处理:`rm` 失败 → 屏幕输出 `⚠ 清理 code-auto 标记失败,需手动删除` + **不**中断
  ```

#### 变更 2:`code-design/SKILL.md`

- **锚点 C**:`§步骤 0b 设计目标确认` 段前(在"读 `design/.../RESULT.md` 的 '## 设计目标' 小节"后 + "触发 `AskUserQuestion`"前)插入新子节:
  ```
  ### 步骤 0b.0 — 调用上下文检测(本需求新增)

  - 检测:Read `./assistants/.code-auto-running`
    - 文件存在 → 自己在被 code-auto 调用 → 跳过 AskUserQuestion,直接采纳 `--balanced` 默认值写入 design/.../RESULT.md 顶部 "## 设计目标" 小节 + 屏显 `⚠ code-auto 上下文:跳过设计目标问路,采纳 --balanced 默认`
    - 文件不存在 → 用户手动调子技能 → 正常触发 AskUserQuestion
  - 异常处理:Read 失败 → 屏幕输出 `⚠ 无法检测 code-auto 上下文,默认按用户手动调子技能处理(触发 AskUserQuestion)` + **不**中断
  ```

#### 变更 3:`code-plan/SKILL.md`

- **锚点 D**:同 `code-design` 锚点 C,在 `§步骤 0b 设计目标确认` 段前插入相同的"调用上下文检测"子节

#### 变更 4:`code-require/SKILL.md`

- **锚点 E**(可选,需先查证 `code-require` 是否有 `AskUserQuestion` 触发点 — 本 plan 阶段先标记,具体实施时由 `code-it` 查证):
  - 若有,在 `AskUserQuestion` 触发前增加同模式"调用上下文检测"分支
  - 若无,**不**修改

## 5. 测试方案(回归用例)

### 5.1 单测 / 集成测

本仓库**不**包含任何测试框架(CLAUDE.md 严守),验证靠**静态 Read + 人工场景验证**。

### 5.2 回归用例清单

| ID | 场景 | 预期行为 | 验证方法 |
| --- | --- | --- | --- |
| R-1 | 用户手动调 `code-design REQ-00019`(无 `code-auto` 上下文) | 步骤 0b 触发 `AskUserQuestion`(既有行为不变) | 临时目录新建 REQ-00019,调 `code-design`;屏显 `AskUserQuestion` |
| R-2 | 用户用 `code-auto "<需求>"` | `code-auto` 步骤 0b 设置 `.code-auto-running` + `code-design` 步骤 0b.0 检测到标记 + 跳过 `AskUserQuestion` + 采纳 `--balanced` 默认 | 调 `code-auto "<测试需求>"`;屏显 `⚠ code-auto 上下文:跳过设计目标问路,采纳 --balanced 默认`;无 `AskUserQuestion` 触发 |
| R-3 | `code-auto` 异常中止(用户 Ctrl+C) | `.code-auto-running` 被清理(SIGINT handler 调 `rm -f`) | 调 `code-auto` 后立即 Ctrl+C;`.code-auto-running` 文件**不**存在 |
| R-4 | `code-auto` 子技能失败(子技能退出码 ≠ 0) | `.code-auto-running` 仍被清理(`code-auto` 步骤 7 中断分支处理) | 调 `code-auto` + 子技能失败;`.code-auto-running` 文件**不**存在 |
| R-5 | 多个 `code-auto` 并发(CI / 批处理场景) | 仅 1 个 `.code-auto-running` 标记(`touch` 幂等);子技能 Read 时严格按"存在即被 code-auto 调用"判定(可能误判,但并发场景不在本修复范围内,留作 v2 follow-up) | 模拟 2 个 `code-auto` 并发;屏显 + 文件状态确认 |

## 6. 风险与回退

### 6.1 风险

| ID | 风险描述 | 风险等级 | 缓解措施 |
| --- | --- | --- | --- |
| **R-1** | `code-auto` 异常崩溃(进程被杀 / 系统断电)时 `.code-auto-running` 未被清理,残留 | 中 | 实施时用 `try-finally` 模式保证清理;`code-design` 步骤 0b.0 检测时若发现残留 + 距离 `code-auto` 启动超过 24 小时 → 视为"脏数据",屏幕输出 `⚠ 检测到残留的 .code-auto-running 文件(已超过 24 小时),按用户手动调子技能处理` |
| **R-2** | D-8 修订(从"不传任何特殊参数"→"不传 prompt 参数(状态文件除外)")对其他 `code-*` 技能的影响 | 低 | D-8 修订**只**放宽"状态文件"类边界,其他契约(`code-auto` 不修改子技能 SKILL.md / 不传 prompt 参数)保持 |
| **R-3** | 其他 7 个 `code-*` 技能未来增加 `AskUserQuestion` 触发点时,可能忘记加"调用上下文检测"分支 | 低 | 留作 v2 follow-up;**不**在本修复中强制覆盖所有技能 |
| **R-4** | `code-fix` 步骤 4 本身有 `AskUserQuestion`(询问本轮状态推进)— 但 `code-fix` 不在 `code-auto` 流水线中,无需修复 | 低 | 本修复**不**修改 `code-fix`;用户用 `code-fix` 主动登记/跟踪缺陷时,正常触发 `AskUserQuestion` 是预期行为 |

### 6.2 回退方式

- `git revert` 本修复 commit(单一 commit,回退粒度清晰)
- 删除残留的 `./assistants/.code-auto-running` 文件(如存在)

## 7. 修复步骤(本修复跨多步,在 `fix-plan.md` 中以"步骤"形式列出)

### 步骤 1:`code-auto/SKILL.md` 增量追加(锚点 A + 锚点 B)

- 涉及文件:`plugins/code-skills/skills/code-auto/SKILL.md`
- 关键变更:
  - 锚点 A:在 `§工作流程` 段后插入"### 步骤 0b — 设置 code-auto 运行标记"子节
  - 锚点 B:在 `§状态机/流程` 段后(步骤 7 完成后)追加"### 步骤 7 收尾 — 清理 code-auto 运行标记"子节
  - 关键决策:用 `try-finally` 模式保证清理;`touch` 失败**不**中断
  - D-8 修订:在本 SKILL.md 顶部"## 不要做的事"小节更新 D-8 条款
- 预期产出:`code-auto/SKILL.md` 净增 ~30 行(2 子节 + D-8 修订)

### 步骤 2:`code-design/SKILL.md` 增量追加(锚点 C)

- 涉及文件:`plugins/code-skills/skills/code-design/SKILL.md`
- 关键变更:
  - 锚点 C:在 `§步骤 0b 设计目标确认` 段前插入"### 步骤 0b.0 — 调用上下文检测"子节
  - 关键决策:Read `./assistants/.code-auto-running` + 24 小时超时判断
- 预期产出:`code-design/SKILL.md` 净增 ~25 行(1 子节)

### 步骤 3:`code-plan/SKILL.md` 增量追加(锚点 D,同 `code-design` 模式)

- 涉及文件:`plugins/code-skills/skills/code-plan/SKILL.md`
- 关键变更:同步骤 2(锚点 D)
- 预期产出:`code-plan/SKILL.md` 净增 ~25 行(1 子节)

### 步骤 4:`code-require/SKILL.md` 增量追加(锚点 E,可选,需查证)

- 涉及文件:`plugins/code-skills/skills/code-require/SKILL.md`(若有 `AskUserQuestion` 触发点)
- 关键变更:同步骤 2(锚点 E)
- 预期产出:`code-require/SKILL.md` 净增 ~25 行(若有)
- 若查证后无 `AskUserQuestion` 触发点,**不**修改

### 步骤 5:人工场景验证(R-1 ~ R-5)

- 验证 R-1:手动调 `code-design`,既有行为不变
- 验证 R-2:`code-auto` 跳过 `AskUserQuestion`,采纳 `--balanced` 默认
- 验证 R-3:`code-auto` SIGINT 后 `.code-auto-running` 被清理
- 验证 R-4:`code-auto` 子技能失败后 `.code-auto-running` 被清理
- 验证 R-5:并发场景降级(留作 v2 follow-up)

## 8. 规范遵循(13 份)

| 规范 | 自检 | 备注 |
| --- | --- | --- |
| skill-conventions §规则 1 | ✅ | frontmatter 字节级保留(SKILL.md 修改必须遵守) |
| module-conventions §规则 1 | ✅ | 不新增资源文件 |
| dependency-conventions | ✅ | 0 新增依赖(脏标记文件 = 文件系统操作,既有能力) |
| dashboard-conventions §规则 1 | ✅ | 不扩展看板字段 |
| encoding-conventions | ✅ | 不涉及任务编号(本修复是单文件修改) |
| commit-conventions | ✅ | commit 消息格式 |
| doc-conventions | ✅ | SKILL.md 行数变化在 ±20% 范围(单文件 +25~30 行,基线 ~750~1000 行) |
| marketplace-protocol | ✅ | 不修改 `marketplace.json` / `plugin.json` |
| naming-conventions | ✅ | 子节名 kebab-case;`.code-auto-running` 沿用点号开头的隐藏文件约定 |
| coding-style | ✅ | 沿用既有 SKILL.md 风格 |
| framework-conventions | ✅ | 不涉及 |
| migration-mapping | ✅ | 不涉及 |
| directory-conventions | ✅ | 不新增子目录;`.code-auto-running` 放在 `./assistants/` 下(与 `.current-version` 同级) |

**总览**:13 份规范全部严守。

## 9. 待澄清 / 未决项

| 编号 | 内容 | 状态 |
| --- | --- | --- |
| (无) | 本方案**不**提出新澄清,所有 4 个文件修改 + 5 步修复 + 13 规范严守均**已锁定** | 0 待澄清 |

## 10. 变更记录

| 时间 | 版本 | 变更摘要 | 变更人 |
| --- | --- | --- | --- |
| 2026-06-06 14:00 | v1 | 初始创建:选定方案 A3(脏标记文件 `./assistants/.code-auto-running`)+ 4 步修复 + 5 项 R-1~R-5 回归用例 + 13 份规范严守 + 0 待澄清;D-8 修订:从"不传任何特殊参数"→"不传 prompt 参数(状态文件除外)";0 新增依赖 / 0 新增资源文件;2 子技能修改(`code-auto` / `code-design` / `code-plan` 3 个)+ 0 触发 dashboard 3 处同步;关联 BUG-00001 状态"报告"→"修复规划中" | wangmiao |
