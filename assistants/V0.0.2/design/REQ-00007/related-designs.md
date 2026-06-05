# 关联概要设计 — REQ-00007

更新时间:2026-06-05 09:30
版本:V0.0.2

## 1. 扫描范围

- **同版本**(`./assistants/V0.0.2/design/*/RESULT.md`):
  - `REQ-00004/RESULT.md` — `/code-dashboard` 开发看板技能
  - `REQ-00005/RESULT.md` — 优化 3 技能(首步拉取 + 末步提交)
  - `REQ-00006/RESULT.md` — `/code-publish` 发布部署技能
- **跨版本**(`./assistants/V0.0.1/design/*/RESULT.md` + V0.0.0):
  - `V0.0.1/design/REQ-00001/RESULT.md` — Marketplace 改名落地(REVIEW 派生任务样板)
  - `V0.0.1/design/REQ-00002/RESULT.md` — 编码格式统一
  - `V0.0.1/design/REQ-00003/RESULT.md` — 优化 `code-rule` 技能
  - `V0.0.0/` — 基线版本

## 2. 同版本关联设计

### 2.1 REQ-00006(V0.0.2)— `/code-publish` 发布部署技能

- **关联点**:
  - **下游衔接**:`code-auto` 完成后,建议用户调 `code-publish`(Q-6 采纳默认)
  - **数据源一致性**:`code-publish` 的 PreflightChecker 用看板 3 区段解析锚点(同 `code-dashboard` 共享),与 `code-auto` 解析 `REVIEW-REPORT.md` 用同一锚点 — **两技能数据源一致**
  - **手工位差异**:`code-publish` 是"只读 + 生成手册",`code-auto` 是"驱动子技能";两者不冲突,可串联
- **对本设计的影响**:
  - `code-auto` 完成时,`auto-report.md` "后续建议"段需显式包含 `code-publish` 与 `code-dashboard`
  - `code-auto` 不调 `code-publish`(职责分离,Q-6 锁定)
- **来源**:`./assistants/V0.0.2/design/REQ-00006/RESULT.md` §1 / §10 / §15

### 2.2 REQ-00005(V0.0.2)— 优化 3 技能(首步拉取 + 末步提交)

- **关联点**:
  - **被调用的子技能**:`code-require` / `code-design` / `code-plan` 已被 REQ-00005 加了"步骤 0a 拉取 + 末尾兜底提交"
  - **执行频次**:`code-auto` 一次完整执行会触发 N1+N2+N3 次 `git pull`(NFR-4 显式不引入批量模式,接受冗余)
  - **末尾提交被反复触发**:`code-require` / `code-design` / `code-plan` 每次执行都会"末步兜底 commit",`code-auto` 一次跑通可能产生 5~20+ 个 commit
- **对本设计的影响**:
  - `code-auto` 沿用 REQ-00005 模式:自身步骤 0a 也调 `git pull`(与子技能内部 0a 重叠;接受,Q-2 锁定 A 衍生)
  - `code-auto` 自身**不** commit(NFR-3),由子技能按各自规则提交
- **来源**:`./assistants/V0.0.2/design/REQ-00005/RESULT.md` §1 / §7 / §10

### 2.3 REQ-00004(V0.0.2)— `/code-dashboard` 开发看板技能

- **关联点**:
  - **数据源共享**:`code-auto` 完成的"任务清单" / "需求清单" / "缺陷清单" 三区段更新,必须能被 `code-dashboard` 看到(NFR-5)
  - **解析锚点复用**:本设计解析 `REVIEW-REPORT.md` 时,沿用 `code-dashboard` 的"`^## .*$` 区段 + `^\| .* \|$` 表格行"锚点
- **对本设计的影响**:
  - `code-auto` 完成后,`auto-report.md` "后续建议"段需显式包含 `code-dashboard`
  - 双格式兼容:任务编号新格式 `^TASK-(REQ|BUG)-\d{5}-\d{5}$` 优先,旧格式 `^(REQ|BUG)-\d{5}-\d{5}$` 透传(沿用 `code-dashboard` NFR-3)
- **来源**:`./assistants/V0.0.2/design/REQ-00004/RESULT.md` §1 / §7 / §NFR-3

## 3. 跨版本关联设计

### 3.1 REQ-00003(V0.0.1)— 优化 `code-rule` 技能

- **关联点**:
  - **`code-rule` 维护项目级规范**:`code-auto` 是"新增技能",不直接写规范
  - **`auto-conventions.md` 沉淀建议**:Q-13 建议派生"用 `code-rule` 沉淀 `auto-conventions.md`(自动化边界/终止条件/中止开关)"(由 `code-review` 决定)
- **对本设计的影响**:
  - 本设计**不**创建 `auto-conventions.md`(留作 follow-up)
  - 派生任务"用 `code-rule` 沉淀 `auto-conventions.md`"在 §15 风险与缓解中显式列出
- **来源**:`./assistants/V0.0.1/design/REQ-00003/RESULT.md` §1.2 / §1.3

### 3.2 REQ-00002(V0.0.1)— 编码格式统一

- **关联点**:
  - **编码权威源**:`code-auto` 解析任务编码时,严格遵循 `^TASK-(REQ|BUG)-\d{5}-\d{5}$`(新格式)与 `^(REQ|BUG)-\d{5}-\d{5}$`(旧格式,透传)
  - **`code-auto` 自身不产生新编码**:仅消费子技能产物(由 `code-require` / `code-plan` 按 `encoding-conventions §规则 4` 自取)
- **对本设计的影响**:本设计**不**触发 `encoding-conventions §规则 4`(实施流程)— 由子技能负责
- **来源**:`./assistants/V0.0.1/design/REQ-00002/RESULT.md` §3 编码变更算法

### 3.3 REQ-00001(V0.0.1)— Marketplace 改名落地(REVIEW 派生任务样板)

- **关联点**:
  - **REVIEW 派生任务模式**:`code-review` 派生的"必须改"任务,在 `code-auto` 步骤 6 中被自动驱动 `code-it` 完成
  - **派生任务的 commit 行为**:沿用 V0.0.1 实践(`code-it` 内部 commit,`code-auto` 不 commit)
- **对本设计的影响**:
  - `code-auto` 步骤 5/6 必须能识别派生任务(从 `plan/PLAN.md` 任务总览的"触发/来源"列读)
  - 派生任务的 commit 由 `code-it` 内部 commit,`code-auto` 不再 commit(NFR-3)
- **来源**:`./assistants/V0.0.1/design/REQ-00001/RESULT.md` §3 Q-4 + V0.0.1 看板"派生任务记录"段

### 3.4 V0.0.0 基线(EXISTING-001 ~ EXISTING-010)

- **关联点**:V0.0.0 基线由 `code-init` 生成,**不**修改(`migration-mapping.md §规则 4` 强制不追溯)
- **对本设计的影响**:无;本设计不触达 V0.0.0
- **来源**:`./assistants/V0.0.0/INIT-REPORT.md`

## 4. 跨需求聚合(供 `code-plan` 阶段权衡)

| 维度 | 涉及需求 | 共性 | 处理建议 |
| --- | --- | --- | --- |
| 子技能边界 | REQ-00005 | 子技能被 N 次调用,触发重复拉取/重复提交 | `code-auto` 不引入批量模式(NFR-4),子技能按原设计运行 |
| 上下游衔接 | REQ-00006 / REQ-00004 | `code-auto` 完成 → 建议调 `code-publish` / `code-dashboard` | `auto-report.md` "后续建议"段显式追加 2 条 |
| 派生任务模式 | REQ-00001 | `code-review` 派生任务被反复触发 | 子技能按既有模式处理;`code-auto` 步骤 6 识别 |
| 编码生成 | REQ-00002 | `code-auto` 内部会**消费**编码(任务编码解析) | 严格遵循 `encoding-conventions.md §规则 1` + §规则 3 |
| 规范沉淀 | REQ-00003 | 项目级规范由 `code-rule` 维护 | 本设计不直接写规范,留作 follow-up(Q-13) |

## 5. 与同版本其他设计阶段的关联

- 本设计是同版本下**第 4 个概要设计**(前 3 个:REQ-00004 / REQ-00005 / REQ-00006)
- 同版本下 REQ-00008 / 09 / 10 / 11 / 12 / 13 的设计阶段尚未开始
- **本设计不**依赖其他 V0.0.2 设计的产出(因 `code-auto` 仅消费既有 6 个子技能)
- **本设计的产出** `SKILL.md` 将在 V0.0.2 后续 REQ-00013 优化"编号+标题显示"中可能涉及(若 Q-4 锁定包含 `code-auto`)
