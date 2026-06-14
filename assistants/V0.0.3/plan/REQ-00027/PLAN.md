# REQ-00027 编码计划 — 优化 code-fix 流程(纯登记型)+ code-auto BUG 路径

- **父级需求**:REQ-00027
- **版本**:V0.0.3
- **创建时间**:2026-06-08 15:35
- **详细设计**:./RESULT.md

---

## 1. 任务总览

| 任务编码 | 需求 | 类型 | 触发/来源 | 标题 | 开发状态 | 测试状态 | 涉及文件 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TASK-REQ-00027-00001 | REQ-00027 | 修改 | 详细设计 | [修改] code-fix/SKILL.md 纯登记型重写(状态机收敛 + 不产出 fix-plan.md + 引导后续调 code-plan/code-it/code-check) | 已完成 | 不适用 | plugins/code-skills/skills/code-fix/SKILL.md | 2026-06-08 15:40 | e860b0b | — |
| TASK-REQ-00027-00002 | REQ-00027 | 修改 | 详细设计 | [修改] code-auto/SKILL.md 模式 C 增加(模式识别正则 + BUG 路径子技能调用表 + fix/<BUG-NNN>/auto-report.md 输出) | 已完成 | 不适用 | plugins/code-skills/skills/code-auto/SKILL.md | 2026-06-08 15:45 | 55050f4 | — |
| TASK-REQ-00027-00003 | REQ-00027 | 文档 | 详细设计 | [文档] 同步版本看板"详细设计与任务计划汇总" + "任务清单" + "里程碑" + "变更记录"(`code-it` 末尾兜底承担) | 待开始 | 不适用 | assistants/V0.0.3/RESULT.md |
| TASK-REQ-00027-00004 | REQ-00027 | 修改 | 审查改修 | [修改] 修正 code-fix 步骤 4 状态推进表(删除中间/非本技能终态行,仅保留 5 候选状态) | 待开始 | 不适用 | plugins/code-skills/skills/code-fix/SKILL.md | 2026-06-08 17:30 | — | TASK-REQ-00027-00001 |
| TASK-REQ-00027-00005 | REQ-00027 | 修改 | 审查改修 | [修改] 修正 code-fix 步骤 9 引导表("已关闭-不修复" 与"已关闭-非缺陷"逻辑统一) | 待开始 | 不适用 | plugins/code-skills/skills/code-fix/SKILL.md | 2026-06-08 17:30 | — | TASK-REQ-00027-00001 |
| TASK-REQ-00027-00006 | REQ-00027 | 修改 | 审查改修 | [修改] 修正 code-fix 步骤 4 注释(本技能只推进"报告 / 调查中";"修复规划中"仅校验不主动推进) | 待开始 | 不适用 | plugins/code-skills/skills/code-fix/SKILL.md | 2026-06-08 17:30 | — | TASK-REQ-00027-00001 |
| TASK-REQ-00027-00007 | REQ-00027 | 修改 | 审查改修 | [修改] code-fix 全局清理 investigation.md 引用(纯登记型不再创建该文件) | 待开始 | 不适用 | plugins/code-skills/skills/code-fix/SKILL.md | 2026-06-08 17:30 | — | TASK-REQ-00027-00001 |
| TASK-REQ-00027-00008 | REQ-00027 | 修改 | 审查改修 | [修改] code-auto 步骤 1 新增"模式 C"识别(首段匹配 `^BUG-\d{5}$`),独立于 fix-skip-require | 待开始 | 不适用 | plugins/code-skills/skills/code-auto/SKILL.md | 2026-06-08 17:30 | — | TASK-REQ-00027-00002 |
| TASK-REQ-00027-00009 | REQ-00027 | 修改 | 审查改修 | [修改] code-auto §"路径感知模式"扩展为 5 种(新增"模式 C"),§"步骤 1 子分支"扩展为 1A-1E | 待开始 | 不适用 | plugins/code-skills/skills/code-auto/SKILL.md | 2026-06-08 17:30 | — | TASK-REQ-00027-00002 |
| TASK-REQ-00027-00010 | REQ-00027 | 修改 | 审查改修 | [修改] code-auto 步骤 2/3 适配 BUG 路径(`code-design` BUG 跳过 / `code-plan` BUG 路径入参) | 待开始 | 不适用 | plugins/code-skills/skills/code-auto/SKILL.md | 2026-06-08 17:30 | — | TASK-REQ-00027-00002 |

**统计**:
- 总任务数:10
- 代码类:2(T-001 / T-002)
- 文档类:1(T-003)
- 审查改修类:7(T-004 ~ T-010)
- 测试需要:Y = 0(纯文档,沿用 `code-unit` 守卫"项目可测性")
- 架构任务:0(简单修改,无需插架构任务)

---

## 2. 任务详情

### TASK-REQ-00027-00001 — code-fix/SKILL.md 纯登记型重写

**目标**:把 `code-fix` 从"全生命周期跟踪"重构为"纯登记型",不实施代码改动、不产出 `fix-plan.md`、不推进"修复规划中"及之后状态。

**涉及文件**:
- `plugins/code-skills/skills/code-fix/SKILL.md` §"目标"
- `plugins/code-skills/skills/code-fix/SKILL.md` §"工作目录约定"
- `plugins/code-skills/skills/code-fix/SKILL.md` §"工作流程 步骤 4 询问本轮状态推进"
- `plugins/code-skills/skills/code-fix/SKILL.md` §"工作流程 步骤 5 补充本轮信息"
- `plugins/code-skills/skills/code-fix/SKILL.md` §"工作流程 步骤 6 写缺陷详情"
- `plugins/code-skills/skills/code-fix/SKILL.md` §"工作流程 步骤 9 引导下一步"
- `plugins/code-skills/skills/code-fix/SKILL.md` §"过程文档格式"
- `plugins/code-skills/skills/code-fix/SKILL.md` §"不要做的事"

**关键变更**(每个区段都要做):
1. **§"目标"**:在原"提供**缺陷从登记到关闭的全生命周期跟踪**"段后,新增第 2 段"本技能仅产出 `fix/<BUG-NNN>/RESULT.md`,不实施代码改动、不产出 `fix-plan.md`、不推进'修复规划中'及之后状态;修复全流程请依次调 `code-plan` / `code-it` / `code-unit` / `code-check`"
2. **§"适用场景"**:删去"想实施代码修复(那是 `code-it` 的事)"(纯登记型不再管修复实施)
3. **§"工作目录约定"**:从"本技能维护的缺陷工作空间"中删去 `fix-plan.md` / `fix-work-log.md` / `fix-compile-and-run.md` / `fix-test-results.md` / `deviations.md`;保留 `fix/RESULT.md`(总览)+ `fix/<BUG-NNN>/RESULT.md`(缺陷详情)
4. **§"工作流程 步骤 4 询问本轮状态推进"**:把"状态推进表"改为仅含"报告 / 调查中 / 已关闭-非缺陷 / 已取消 / 阻塞" 5 个候选状态(详见详细设计 §3.1)
5. **§"工作流程 步骤 5 补充本轮信息"**:删除所有"→ 修复规划中" / "→ 修复编码中" / "→ 已修复-待验证" 等推进提示;改为统一的"若需推进修复规划/编码/已修复等状态,请先调 `code-plan <BUG-NNN>` 产出 `fix-plan.md`"
6. **§"工作流程 步骤 6 写缺陷详情"**:保留,但"修复方案"小节改为"若已调 `code-plan`,可链接 `fix-plan.md`"
7. **§"工作流程 步骤 9 引导下一步"**:完全重写,候选目标状态表仅含登记/分析类(详见详细设计 §3.1 流程图)
8. **§"过程文档格式"**:删去"fix-plan.md" / "fix-work-log.md" 等(本技能不产出)
9. **§"不要做的事"**:新增 3 条"不产出 `fix-plan.md`(由 `code-plan` 产出)" / "不实施代码改动(由 `code-it` 实施)" / "不推进'修复规划中'及之后状态(由 `code-plan` / `code-it` / `code-check` 推进)"

**边界与异常**:
- 状态推进:本任务仅重写 SKILL.md 文字,不动 `code-fix/SKILL.md` 之外的任何文件
- 兼容:重写后 `code-fix` 仍能产出 `fix/<BUG-NNN>/RESULT.md`(沿用既有模板)

**验证手段**:
- `git diff` 校验 9 个区段全部 Edit
- `code-fix/SKILL.md` frontmatter 字节级一致
- `code-fix/SKILL.md` 步骤 4 状态推进表仅含 5 个候选状态
- `code-fix/SKILL.md` 步骤 9 引导下一步表仅含登记/分析类
- 0 改 marketplace.json / plugin.json / 4 个 README / CLAUDE.md
- 旧需求档案 0 diff

**回退方式**:`git revert` 本任务 commit。

**依赖**:无

---

### TASK-REQ-00027-00002 — code-auto/SKILL.md 模式 C 增加

**目标**:在 `code-auto` 中增加 BUG-NNN 任务识别与编排路径。

**涉及文件**:
- `plugins/code-skills/skills/code-auto/SKILL.md` §"输入" 步骤 1.1
- `plugins/code-skills/skills/code-auto/SKILL.md` §"输入" 表"三种调用模式"
- `plugins/code-skills/skills/code-auto/SKILL.md` §"子技能调用表" 步骤 4
- `plugins/code-skills/skills/code-auto/SKILL.md` §"附加约束"
- `plugins/code-skills/skills/code-auto/SKILL.md` §"步骤 7 报告"
- `plugins/code-skills/skills/code-auto/SKILL.md` §"边界与异常"
- `plugins/code-skills/skills/code-auto/SKILL.md` §"不要做的事"

**关键变更**(每个区段都要做):
1. **§"输入" 步骤 1.1**:增加"模式 C"识别(首段匹配 `^BUG-\\d{5}$` → BUG 路径)
2. **§"输入" 表"三种调用模式"**:从"两种调用模式"扩展为"三种调用模式"(A / B / C)
3. **§"子技能调用表" 步骤 4**:新增 BUG 路径子技能表(7 步骤,详见详细设计 §2.2)
4. **§"附加约束"**:沿用 REQ 路径的"`AskUserQuestion` 自动选推荐项"
5. **§"步骤 7 报告"**:BUG 路径完成时写 `fix/<BUG-NNN>/auto-report.md`(非 `require/<REQ-NNNNN>/auto-report.md`)
6. **§"边界与异常"**:新增 E-18 / E-19 / E-20
7. **§"不要做的事"**:新增"不修改 `code-plan` / `code-it` / `code-unit` / `code-check` 的核心工作流"

**边界与异常**:
- 子技能调用表扩展:本任务仅扩展 BUG 路径编排,不修改 REQ 路径的子技能调用表
- 任务循环逻辑:BUG 路径的"任务循环"复用 REQ 路径的"任务总览 + 执行档案"模式

**验证手段**:
- `git diff` 校验 7 个区段全部 Edit
- `code-auto/SKILL.md` frontmatter 字节级一致
- `code-auto/SKILL.md` 模式识别表含 3 种模式
- `code-auto/SKILL.md` 子技能调用表 BUG 路径含 7 步骤
- 0 改 marketplace.json / plugin.json / 4 个 README / CLAUDE.md

**回退方式**:`git revert` 本任务 commit。

**依赖**:无

---

### TASK-REQ-00027-00003 — 同步版本看板(由 `code-it` 末尾兜底承担)

**目标**:在 `assistants/V0.0.3/RESULT.md` 中追加 REQ-00027 的详细设计条目 + 3 任务行 + 里程碑 + 变更记录。

**涉及文件**:
- `assistants/V0.0.3/RESULT.md` §"详细设计与任务计划汇总"
- `assistants/V0.0.3/RESULT.md` §"任务清单"
- `assistants/V0.0.3/RESULT.md` §"里程碑"
- `assistants/V0.0.3/RESULT.md` §"变更记录"

**关键变更**:
1. "详细设计与任务计划汇总"区段:追加 1 行(REQ-00027 / 标题 / 状态=已完成 / 创建时间 / 任务总数 3 / 链接)
2. "任务清单"区段:追加 3 行(T-001 / T-002 / T-003),每行字段对齐模板
3. "里程碑"区段:追加 M1-REQ-00027(所有任务完成,开发=已完成 ∧ 测试=不适用)
4. "变更记录"区段:追加 1 行(2026-06-08 15:35 设计新增 REQ-00027 详细设计与编码计划完成(共 3 个任务))

**边界与异常**:
- 本任务由 `code-it` 末尾兜底承担(沿用 REQ-00017 强约束)
- 任务类型=文档,测试状态=不适用
- 涉及文件留空(由 `code-it` 完成时填入)

**验证手段**:
- `git diff` 校验 RESULT.md 改动
- 看板"任务清单"中本计划 3 任务行存在
- 看板"统计"中真正可发布数 50 → 53

**回退方式**:`git revert` 本任务 commit。

**依赖**:T-001 / T-002 完成(看板同步必须在 2 个修改任务完成后)

---

### TASK-REQ-00027-00004 — 修正 code-fix 步骤 4 状态推进表(仅保留 5 候选状态)

**目标**:把 `code-fix/SKILL.md` 步骤 4 "询问本轮状态推进"的候选目标状态表收敛为 5 候选状态(报告 / 调查中 / 已关闭-非缺陷 / 已取消 / 阻塞),删除残留的"修复规划中 / 修复编码中 / 已修复-待验证 / 已修复-已验证 / 已关闭-不修复"等中间/非本技能终态行。

**触发/来源**:审查改修(由 `code-review` REQ-00027 评审派生,F-1)
**关联原任务**:TASK-REQ-00027-00001
**改修要求**:`./assistants/V0.0.3/review/TASK-REQ-00027-00004/RESULT.md`
**审查发现 ID**:F-1(必须改,设计符合度)

**涉及文件**:
- `plugins/code-skills/skills/code-fix/SKILL.md` 步骤 4 状态推进表(L249-261)+ "超出本技能范围" 小节(L268-271)

**边界与异常**:
- 仅改 code-fix/SKILL.md 步骤 4 段,不动其他章节
- 0 改 frontmatter
- 0 改 README / CLAUDE.md / marketplace.json / plugin.json

**验证手段**:
- `git diff --stat` 列出 1 文件
- 步骤 4 状态表行数 = 6(含表头与分隔) — 收敛到 5 候选
- 步骤 4 注释与表内容无矛盾(由 T-006 配合)
- `git diff marketplace.json plugin.json README*.md CLAUDE.md` 0 diff

**回退方式**:`git revert <commit>`。

**依赖**:无

---

### TASK-REQ-00027-00005 — 修正 code-fix 步骤 9 引导表("已关闭-不修复" 与"已关闭-非缺陷"逻辑统一)

**目标**:把 `code-fix/SKILL.md` 步骤 9 引导表中"已关闭-不修复" 与"已关闭-非缺陷"逻辑统一——"已关闭-不修复"在步骤 4 是终态,在步骤 9 又"由 code-check 推进",自相矛盾;本任务让两者统一为单一终态(沿用 `code-check` 实际推进的"已关闭"终态)。

**触发/来源**:审查改修(由 `code-review` REQ-00027 评审派生,F-2)
**关联原任务**:TASK-REQ-00027-00001
**改修要求**:`./assistants/V0.0.3/review/TASK-REQ-00027-00005/RESULT.md`
**审查发现 ID**:F-2(必须改,一致性)

**涉及文件**:
- `plugins/code-skills/skills/code-fix/SKILL.md` L259(步骤 4 表)+ L367-368(步骤 9 表)

**边界与异常**:
- 仅改 code-fix/SKILL.md 这 3 行
- 0 改 frontmatter

**验证手段**:
- 步骤 4 表行数从 11 行减为 10 行
- 步骤 9 表"已关闭-不修复"行措辞统一

**回退方式**:`git revert <commit>`。

**依赖**:无

---

### TASK-REQ-00027-00006 — 修正 code-fix 步骤 4 注释(本技能只推进"报告 / 调查中";"修复规划中"仅校验不主动推进)

**目标**:把 `code-fix/SKILL.md` 步骤 4 注释改为"本技能**只**主动推进'报告 / 调查中' 2 段;'修复规划中'由用户调 `code-plan` 推进,本技能仅在复跑时**校验**该状态是否已对齐 `fix-plan.md` 是否存在",对齐设计意图。

**触发/来源**:审查改修(由 `code-review` REQ-00027 评审派生,F-3)
**关联原任务**:TASK-REQ-00027-00001
**改修要求**:`./assistants/V0.0.3/review/TASK-REQ-00027-00006/RESULT.md`
**审查发现 ID**:F-3(必须改,可维护性)

**涉及文件**:
- `plugins/code-skills/skills/code-fix/SKILL.md` L245-246(注释段)

**边界与异常**:
- 仅改注释 2 行,不动表行(由 T-004 配合)
- 0 改 frontmatter

**验证手段**:
- L245 注释"只**主动**推进 报告 / 调查中 2 段"字面满足

**回退方式**:`git revert <commit>`。

**依赖**:无

---

### TASK-REQ-00027-00007 — code-fix 全局清理 investigation.md 引用(纯登记型不再创建该文件)

**目标**:把 `code-fix/SKILL.md` 中 4 处 `investigation.md` 引用(L237 / L279 / L381 / L400-406)统一为"由 `code-it` 写入,本技能只读",清除"纯登记型" 与"可写 `investigation.md`" 的语义矛盾。

**触发/来源**:审查改修(由 `code-review` REQ-00027 评审派生,F-4)
**关联原任务**:TASK-REQ-00027-00001
**改修要求**:`./assistants/V0.0.3/review/TASK-REQ-00027-00007/RESULT.md`
**审查发现 ID**:F-4(必须改,一致性 / 可维护性,经用户升级)

**涉及文件**:
- `plugins/code-skills/skills/code-fix/SKILL.md` L237 / L279 / L381 / L400-406(共 4 处)

**边界与异常**:
- 仅改这 4 处,不动其他章节
- 0 改 frontmatter
- 0 改 `code-it` SKILL.md 自身

**验证手段**:
- `grep "investigation.md" code-fix/SKILL.md` 应仅 4 处(原 5 处)
- 4 处全部加 "由 code-it 写入,本技能只读" 说明

**回退方式**:`git revert <commit>`。

**依赖**:无

---

### TASK-REQ-00027-00008 — code-auto 步骤 1 新增"模式 C"识别(首段匹配 `^BUG-\d{5}$`),独立于 fix-skip-require

**目标**:把 `code-auto/SKILL.md` BUG 路径子技能调用表的"触发:模式 C,首段匹配 `^BUG-\d{5}$`" 措辞落实(详 T-009 的实现)。

**触发/来源**:审查改修(由 `code-review` REQ-00027 评审派生,F-5)
**关联原任务**:TASK-REQ-00027-00002
**改修要求**:`./assistants/V0.0.3/review/TASK-REQ-00027-00008/RESULT.md`
**审查发现 ID**:F-5(必须改,设计符合度)

**涉及文件**:
- `plugins/code-skills/skills/code-auto/SKILL.md` L219(BUG 路径子技能调用表标题)

**边界与异常**:
- 仅改 L219 一行
- 0 改 frontmatter

**验证手段**:
- L219 字面为"触发:模式 C,首段匹配 `^BUG-\d{5}$`"

**回退方式**:`git revert <commit>`。

**依赖**:T-009(模式 C 在 §"路径感知模式" 表中真正实现)+ T-010(步骤 2/3 适配)

---

### TASK-REQ-00027-00009 — code-auto §"路径感知模式"扩展为 5 种(新增"模式 C"),§"步骤 1 子分支"扩展为 1A-1E

**目标**:把 `code-auto/SKILL.md` §"路径感知模式" 表从 4 种扩展为 5 种(新增"模式 C" / `bug-skip-require`);把"步骤 1 子分支" 从 1A-1D 扩展为 1A-1E,新增 1E 子分支覆盖 BUG 路径。

**触发/来源**:审查改修(由 `code-review` REQ-00027 评审派生,F-6)
**关联原任务**:TASK-REQ-00027-00002
**改修要求**:`./assistants/V0.0.3/review/TASK-REQ-00027-00009/RESULT.md`
**审查发现 ID**:F-6(必须改,规范 / 接口)

**涉及文件**:
- `plugins/code-skills/skills/code-auto/SKILL.md` L73(段头)+ L75-80(表)+ L82-94(算法)+ L99(屏显契约)+ L273-323(步骤 1 子分支)

**边界与异常**:
- 0 改 frontmatter
- 0 改 E-20 措辞(已正确)
- 0 改其他 `code-*` SKILL.md

**验证手段**:
- `grep "4 种路径感知模式" code-auto/SKILL.md` 应为 0 处
- `grep "bug-skip-require" code-auto/SKILL.md` 应有 ≥ 4 处
- `grep "^#### 1E" code-auto/SKILL.md` 应有 1 处

**回退方式**:`git revert <commit>`。

**依赖**:无

---

### TASK-REQ-00027-00010 — code-auto 步骤 2/3 适配 BUG 路径(`code-design` BUG 跳过 / `code-plan` BUG 路径入参)

**目标**:把 `code-auto/SKILL.md` 步骤 2 `code-design` 拆为 2A(默认需求路径)/ 2B(BUG 路径跳过);把步骤 3 `code-plan` 拆为 3A(默认需求路径)/ 3B(缺陷分支,接收 `<BUG-NNN>`)。

**触发/来源**:审查改修(由 `code-review` REQ-00027 评审派生,F-7)
**关联原任务**:TASK-REQ-00027-00002
**改修要求**:`./assistants/V0.0.3/review/TASK-REQ-00027-00010/RESULT.md`
**审查发现 ID**:F-7(必须改,设计符合度)

**涉及文件**:
- `plugins/code-skills/skills/code-auto/SKILL.md` L325-333(步骤 2)+ L335-343(步骤 3)

**边界与异常**:
- 仅改 2 段
- 0 改 frontmatter
- 0 改 `code-design` / `code-plan` 自身

**验证手段**:
- `grep "^#### 2A" code-auto/SKILL.md` 应有 1 处
- `grep "^#### 3A" code-auto/SKILL.md` 应有 1 处
- 3B 期望产物为 `fix/<BUG-NNN>/fix-plan.md`

**回退方式**:`git revert <commit>`。

**依赖**:T-009(模式 C 落地后,1E 子分支才被 2A / 2B / 3A / 3B 引用)

---

## 3. 任务依赖图

```mermaid
graph TD
  T001[T-001: code-fix 重写] --> T003
  T002[T-002: code-auto 模式 C] --> T003
  T003[T-003: 看板同步]
  T004[T-004: 步骤 4 状态表修正] -.审查改修.-> T001
  T005[T-005: 步骤 9 引导表修正] -.审查改修.-> T001
  T006[T-006: 步骤 4 注释修正] -.审查改修.-> T001
  T007[T-007: investigation.md 清理] -.审查改修.-> T001
  T008[T-008: 模式 C 识别] -.审查改修.-> T002
  T009[T-009: 路径感知模式扩展 5 种] -.审查改修.-> T002
  T010[T-010: 步骤 2/3 BUG 路径适配] -.审查改修.-> T002
  T004 --> T011[T-011: 看板同步收尾(原 T-003)]
  T005 --> T011
  T006 --> T011
  T007 --> T011
  T008 --> T011
  T009 --> T011
  T010 --> T011
```

T-001 / T-002 互相无依赖;T-003 依赖 T-001 / T-002。
T-004 ~ T-010(审查改修)分别依赖其关联原任务(T-001 或 T-002);T-003 看板同步收尾依赖全部 7 个审查改修任务。

---

## 4. 里程碑

| 里程碑 | 包含任务 | 完成定义 |
| --- | --- | --- |
| M1-REQ-00027 | T-001 + T-002 + T-003 | `git diff --stat` 列出 2 SKILL.md;frontmatter 字节级一致;模式识别表 3 模式;`git diff marketplace.json plugin.json README*.md CLAUDE.md` 0 diff |
| M3-REQ-00027 | T-004 ~ T-010(7 个审查改修任务) + T-003(看板收尾) | 7 个审查改修任务开发=已完成 ∧ 测试=不适用;code-fix 步骤 4 状态表 5 候选字面满足;code-auto §"路径感知模式"含 5 种;步骤 1 子分支 1A-1E;步骤 2 拆 2A/2B;步骤 3 拆 3A/3B;investigation.md 角色统一 |

---

## 5. 变更记录

| 时间 | 变更 | 关联 |
| --- | --- | --- |
| 2026-06-08 15:35 | 计划新增 | REQ-00027 详细设计与编码计划完成(共 3 个任务;M1-REQ-00027) |
| 2026-06-08 15:40 | 状态更新 | TASK-REQ-00027-00001 状态"待开始"→"已完成",提交 e860b0b |
| 2026-06-08 15:45 | 状态更新 | TASK-REQ-00027-00002 状态"待开始"→"已完成",提交 55050f4 |
| 2026-06-08 17:30 | 增量更新(审查) | 评审发现 7 个问题(F-1 ~ F-7),全部派生为审查改修任务 TASK-REQ-00027-00004 ~ TASK-REQ-00027-00010,关联原任务 T-001 / T-002,触发/来源=审查改修 |
