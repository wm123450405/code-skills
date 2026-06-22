# 风险分析 — REQ-00037

更新时间:2026-06-22 09:28
版本:V0.0.3

## 异常处理

### 异常路径 1:状态推进失败回退(NFR-2)

- **描述**:`code-it` 步骤 24 写 `fix/<BUG-NNN>/RESULT.md` 状态 `开发中 → 待审查` 成功,但同步 `fix/RESULT.md` 或看板失败。
- **处理**:
  1. 写回旧状态(用 `Edit` 工具把状态字段改回 `开发中`)
  2. 屏显 `⚠ 状态推进部分失败:fix/<BUG-NNN>/RESULT.md 已写回旧状态,但 fix/RESULT.md / 看板同步失败,请手动处理`
  3. 不阻断当前技能的后续流程(`code-it` 步骤 25 完善过程文档仍可执行)
- **监控**:沿用既有"开发命令记录"区段(无新增监控指标)

### 异常路径 2:`code-check` 评审发现"必须改"派生改修任务(E-3)

- **描述**:`code-check BUG-NNN` 评审产出"必须改"项,派生 `TASK-BUG-NNNNN-NNNNN` 任务交给 `code-it` 做改修。
- **处理**:
  - BUG 状态**不**回退到 `开发中`(沿用 REQ-00027 E-3)
  - 保持 `待审查`(因为尚未通过)
  - `code-it` 改修完成后,BUG 状态**维持** `待审查`
  - 等用户再调一次 `code-check` 重新评审;通过后 → `已完成`
- **替代设计**(本轮**不**采用,留作 Q-3):派生的改修任务完成后,自动重新评审,不需要用户手动再调一次 `code-check`

### 异常路径 3:多任务 BUG 中用户跳过中间任务(E-2)

- **描述**:用户先调 `code-it TASK-BUG-00005-00003`(第 3 个任务),未先做 `TASK-BUG-00005-00001`(第 1 个)。
- **处理**:`code-it` 步骤 0a 前置任务守卫拦截(沿用 `code-it/SKILL.md` 既有);任务**不执行**,提示用户先做前置任务。
- **状态影响**:BUG 状态保持 `待开发`(未触发"开发中"推进,因为第 1 个任务未启动)

### 异常路径 4:历史 BUG 被新流程推过时(E-5)

- **描述**:`code-plan` / `code-it` / `code-check` 推进时,BUG 当前状态为老字面(`报告 / 调查中 / 修复规划中 / ...`)。
- **处理**:
  - **不**做强迁(沿用 NFR-3)
  - 维持原字面继续走老路径(`code-plan` 步骤 27A 现有逻辑推 `修复规划中` / `code-it` 步骤 21 推 `修复编码中` 等)
  - 若用户希望把老 BUG 迁到新路径,**不提供**自动迁移工具(留作 Q-1 follow-up)

### 异常路径 5:`code-fix` 复跑 BUG-NNN 时,BUG 处于中段状态(E-4)

- **描述**:用户调 `/code-fix BUG-NNN`,BUG 当前状态为 `待开发 / 开发中 / 待审查`。
- **处理**:
  - `code-fix` 检测当前状态,若是这 3 字面,**不**做状态推进
  - 屏显 `⚠ 该缺陷当前状态为 <状态>,本技能不推进该状态;请继续调 code-plan / code-it / code-check`
  - **不**修改 `fix/<BUG-NNN>/RESULT.md` / `fix/RESULT.md` / 看板(沿用 S-4 软约束)

### 异常路径 6:`code-check` 步骤 1.5 模式选择的边界(E-6)

- **描述**:用户传入的参数既不匹配 `^REQ-\d{5}$` 也不匹配 `^BUG-\d{5}$`(如 `code-check` 或 `code-check invalid`)。
- **处理**:沿用既有"整版本模式 + 警告"路径(沿用 `code-check` 步骤 1.5 第 3 款)**不**触发异常。

### 异常路径 7:`code-check` 当前未原生支持 BUG-NNN 入参(E-7)

- **现状**(V0.0.3 截至本轮):`code-check` 既有 `REVIEW-REPORT.md` 等模板是按 REQ 路径设计的;BUG 路径需要扩展。
- **处理**:本轮 FR-5 中扩展 `code-check` 接受 `BUG-NNNNN` 入参;新增"单缺陷评审"分支(沿用既有"单需求评审"骨架)。
- **风险**:扩展可能引入 `code-check` 的回归 —— **缓解**:`code-check` REQ 路径**字节级不变**(FR-5 限定仅追加 BUG 路径,不动既有逻辑)。

## 安全边界

- **不适用**(本设计是 SKILL.md 行为变更,无安全边界)

## 性能与资源

- **关键路径预估**:每个状态回写动作**1 次 `Read` + 1 次 `Edit` + 1 次同步 `fix/RESULT.md` 或看板 `Edit`**,3-5 次 IO
- **资源限制**:不适用
- **缓存策略**:不适用

## 回退策略

### R-1:状态推进失败回退(详异常路径 1)

- **触发条件**:同步 `fix/RESULT.md` 或看板失败
- **步骤**:
  1. 写回 `fix/<BUG-NNN>/RESULT.md` 文档头"状态"字段(用 `Edit`)
  2. 屏显 `⚠` 警告
  3. 不阻断技能后续流程
- **验证**:用户后续手工同步 `fix/RESULT.md` 与看板后,看板状态与 `fix/<BUG-NNN>/RESULT.md` 一致

### R-2:`code-check` 评审不通过(详异常路径 2)

- **触发条件**:评审发现"必须改"项
- **步骤**:
  1. `code-check` 派生 `TASK-BUG-NNNNN-NNNNN` 任务
  2. BUG 状态维持 `待审查`
  3. 用户调 `code-it` 改修
  4. 用户再调 `code-check` 重审
- **验证**:重审通过后,BUG 状态推 `已完成`

### R-3:`code-fix` 复跑中段状态(详异常路径 5)

- **触发条件**:用户调 `/code-fix BUG-NNN`,BUG 处于 `待开发 / 开发中 / 待审查` 中段
- **步骤**:
  1. `code-fix` 检测当前状态
  2. 屏显警告
  3. 不做状态推进
- **验证**:无副作用;用户需继续调 `code-plan` / `code-it` / `code-check`

## 测试要点

### 单元测试

- 不适用(本设计**不**写单元测试;沿用既有 `code-it` 步骤 8.5 自含按需写单测)

### 集成测试

- **T-1(`code-fix` 步骤 6 状态回写)**:
  - 调 `/code-fix "测试"` → 期望 `fix/BUG-NNNNN/RESULT.md` 文档头"状态" = `待处理`
  - 调 `/code-fix BUG-NNNNN` 复跑 → 期望 `fix/BUG-NNNNN/RESULT.md` 文档头"状态" 可推进到 `报告`(前段)
- **T-2(`code-plan` 步骤 27A 状态回写)**:
  - 调 `/code-plan BUG-NNNNN` → 期望 `fix/<BUG-NNN>/RESULT.md` 文档头"状态" 从 `待处理` 推进到 `待开发`
- **T-3(`code-it` 步骤 21 状态回写)**:
  - 调 `/code-it TASK-BUG-NNNNN-00001` → 期望 BUG 状态推 `开发中`(若总任务数 = 1)
  - 调 `/code-it TASK-BUG-NNNNN-00002`(若总任务数 ≥ 2)→ 期望 BUG 状态**维持** `开发中`
- **T-4(`code-it` 步骤 24 状态回写)**:
  - 全部任务完成 → 期望 BUG 状态推 `待审查`
- **T-5(`code-check` 步骤 1.5 BUG 模式)**:
  - 调 `/code-check BUG-NNNNN` → 期望进入"单缺陷评审"分支,产出 `review/<BUG-NNN>/REVIEW-REPORT.md`
  - 调 `/code-check REQ-NNNNN` → 期望**字节级不变**(REVIEW-REPORT.md 路径与既有同构)
- **T-6(`code-dashboard` 步骤 4 段 3 扩展)**:
  - 调 `/code-dashboard` → 期望段 3 屏显"P0 待修复: N"包含 5 新字面 + 老字面 BUG 数(沿用 PD-2 锁定)
- **T-7(端到端 AC 验证)**:
  - AC-1 ~ AC-10 全部通过(沿用上游 §10)

### 端到端测试

- **AC-1**:登记新 BUG → `fix/BUG-NNNNN/RESULT.md` 文档头"状态" = `待处理`
- **AC-2**:`code-plan BUG-NNN` → 状态 = `待开发`
- **AC-3**:`code-it TASK-BUG-NNNNN-00001` → 状态 = `开发中`
- **AC-4**:`code-it` 全部完成 → 状态 = `待审查`
- **AC-5**:`code-check BUG-NNN` → 状态 = `已完成`
- **AC-6**:`code-fix BUG-NNN`(BUG 处于 `待开发`)→ 屏显警告,**不**修改状态
- **AC-7**:完整 4 步流程,**无**中途 `code-fix` 复跑;看板"缺陷清单"状态字段 5 个节点正确
- **AC-8**:历史 BUG 状态保留(不强迁)
- **AC-9**:`code-check BUG-NNN` 扩展接受 BUG-NNN 入参;REQ 路径字节级不变
- **AC-10**:典型完整流程 SKILL.md 文档同步(4 个 SKILL.md 的"## 衔接"段 + "## 不要做的事"段)

### 性能测试

- 不适用(本设计无性能关键路径)

### 安全测试

- 不适用(本设计无安全边界)