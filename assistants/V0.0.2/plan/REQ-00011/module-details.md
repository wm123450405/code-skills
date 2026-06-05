# 模块详细化 — REQ-00011

更新时间:2026-06-05
版本:V0.0.2

## 模块 1:`code-design` 步骤 0b(对应概要设计 §3 D-1 ~ D-3,RESULT.md §4)

- **路径**:`plugins/code-skills/skills/code-design/SKILL.md`
- **关键类/函数**:
  - `askDesignGoals(needContext: NeedContext): DesignGoals` — 触发 1-5 个 `AskUserQuestion`,收集用户回答
  - `writeDesignGoalsSection(resultMdPath: string, goals: DesignGoals, trigger: "code-design"): void` — 写入 `design/.../RESULT.md` 顶部"## 设计目标"小节
- **内部状态**:**无**持久化状态
- **关键调用顺序**:
  1. 步骤 0a 拉取(REQ-00005 既有)
  2. **步骤 0b 触发 `AskUserQuestion`**(本需求新增)
  3. 收集回答 → 写"## 设计目标"小节
  4. 屏显"已回写至 design/<REQ>/RESULT.md '## 设计目标' 小节"
  5. 进入步骤 0(版本上下文检测)— 沿用既有
- **并发模型**:串行
- **资源管理**:**无**
- **错误处理范式**:
  - 用户取消 → 中止 + 回写空"## 设计目标"小节(E-3)
  - 写文件失败 → 透传 stderr
- **日志埋点**:屏显"=== code-design 设计目标确认 ==="区段
- **与概要设计的对应**:§3 D-1(步骤 0b 位置)/ D-2(顶部"## 设计目标"小节)/ D-3(1-5 问自适应)
- **符合的规范**:`skill-conventions.md §规则 1`(frontmatter 不变)+ NFR-2 增量修改 + INV-1 / INV-2 / INV-3 / INV-5

## 模块 2:`code-plan` 步骤 0b(对应概要设计 §3 D-4,RESULT.md §4)

- **路径**:`plugins/code-skills/skills/code-plan/SKILL.md`
- **关键类/函数**:
  - `readDesignGoalsFromDesign(designResultPath: string): DesignGoals | null` — 读 `design/.../RESULT.md` 的"## 设计目标"小节
  - `askDesignGoalsDegraded(needContext: NeedContext): DesignGoals` — 退化时触发 1-5 问
  - `writeDesignGoalsSection(resultMdPath: string, goals: DesignGoals, trigger: "code-plan"): void`
  - `adjustTaskGranularityByGoals(plan: Plan, goals: DesignGoals): Plan` — 任务粒度调整
- **内部状态**:**无**
- **关键调用顺序**:
  1. 步骤 0a 拉取
  2. **步骤 0b 读 `design/.../RESULT.md`**:
     - 存在 → 屏显"沿用 design 的设计目标:<摘要>" + 复制到 `plan/.../RESULT.md`
     - 不存在 → 屏显"⚠ 未检测到 design/<REQ>/RESULT.md" + 触发 `AskUserQuestion` + 写 `plan/.../RESULT.md`
  3. **任务拆分时**调 `adjustTaskGranularityByGoals`
  4. 进入步骤 0(版本上下文检测)
- **并发模型**:串行
- **资源管理**:**无**
- **错误处理范式**:
  - 读失败 → 视同不存在,退化
  - 用户取消 → 中止
- **日志埋点**:屏显"=== code-plan 设计目标确认 ==="区段(§6.2 / §6.3)
- **与概要设计的对应**:§3 D-4(沿用 or 退化)/ D-5(任务粒度调整)
- **符合的规范**:NFR-5 与 `code-auto` 0 冲突 + FR-3 退化行为

## 模块 3:模板顶部预留位(对应概要设计 §3 D-8)

- **路径**:
  - `plugins/code-skills/skills/code-design/templates/design.md`
  - `plugins/code-skills/skills/code-plan/templates/plan.md`
- **关键变更**:在"## 文档头"模板区段**后** + "## 1. ..."章节**前**插入占位注释
- **占位注释**:
  ```markdown
  ## 设计目标
  <!-- 本节由 code-design / code-plan 步骤 0b 自动生成(写入或沿用),记录用户确认的设计目标;如需手动编辑,保留该注释以便步骤 0b 识别 -->
  ```
- **与概要设计的对应**:§3 D-8
- **符合的规范**:`module-conventions.md §规则 1`(资源放 `templates/` 子目录)

## 模块 4:`code-design` / `code-plan` 步骤 0a 既有"不含步骤 0b"小注更新(本计划新增细化)

- **路径**:
  - `plugins/code-skills/skills/code-design/SKILL.md` §步骤 0a L107
  - `plugins/code-skills/skills/code-plan/SKILL.md` §步骤 0a L118
- **原内容**:`code-design` **不**含步骤 0b(FR-2 显式仅 `code-require` 专属)。
- **更新后**:`code-design` / `code-plan` 步骤 0a 成功后,进入'步骤 0b 设计目标确认'(本需求 REQ-00011 新增,FR-1 / FR-2)
- **依据规范**:本计划新增细化(概要设计 D-1 锁定"步骤 0b"位置,但未明确说明"小注更新";本计划作为详细化补充)

## 与概要设计的对应(汇总)

| 概要设计章节 | 本计划对应 |
| --- | --- |
| §3 D-1(步骤 0b 位置) | 模块 1 / 模块 2(位置)+ 模块 4(小注更新) |
| §3 D-2(顶部"## 设计目标"小节) | 模块 1 / 模块 2(回写)+ 模块 3(模板预留) |
| §3 D-3(1-5 问自适应) | 模块 1(`askDesignGoals`) |
| §3 D-4(沿用 or 退化) | 模块 2(`readDesignGoalsFromDesign` + `askDesignGoalsDegraded`) |
| §3 D-5(任务粒度调整) | 模块 2(`adjustTaskGranularityByGoals`) |
| §3 D-6(幂等) | 模块 1 / 模块 2(`writeDesignGoalsSection` 覆盖前次) |
| §3 D-7(与 `code-auto` 0 冲突) | T-001 / T-002 备注(NFR-5 强约束) |
| §3 D-8(模板顶部预留) | 模块 3 |
| §5.2(数据结构) | DesignGoals(内存)+ "## 设计目标"小节 Markdown |
| §5.3(SKILL.md 正文增量追加) | 模块 1 / 模块 2 / 模块 4 关键变更 |
| §5.4(任务粒度调整判定表) | T-002 §步骤 10A 末尾"按设计目标调整任务粒度"段 |
