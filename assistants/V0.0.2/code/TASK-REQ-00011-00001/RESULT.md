# RESULT — TASK-REQ-00011-00001

- 任务编码:TASK-REQ-00011-00001
- 标题:[修改] `code-design/SKILL.md` 增量追加"步骤 0b 设计目标确认" + 模板顶部预留 + 步骤 0a 小注更新
- 类型:修改
- 触发/来源:详细设计
- 关联需求:REQ-00011
- 开发状态:**已完成**
- 完成时间:2026-06-05 19:55
- 完成人:wangmiao
- 提交哈希:见末尾(`git commit` 输出)

## 1. 改修内容总览

### 涉及文件(2 个,全部为 `**修改**`)

| 文件 | 变更类型 | 行数变化 | 说明 |
| --- | --- | --- | --- |
| `plugins/code-skills/skills/code-design/SKILL.md` | 修改 | +20 行 | §步骤 0a L107 既有"不含步骤 0b"小注更新(替换 1 句) + §步骤 0a L117 末尾追加"执行步骤 0b 设计目标确认"提示 + 新增"### 步骤 0b — 设计目标确认"完整章节(L119-135) |
| `plugins/code-skills/skills/code-design/templates/design.md` | 修改 | +3 行 | "## 文档头"模板区段后 + "## 1. 设计概述"前插入"## 设计目标"占位 |

### 不涉及文件(本任务范围外)

- `plugins/code-skills/skills/code-design/SKILL.md` frontmatter(L1-3)字节级保留(INV-1)
- `plugins/code-skills/skills/code-design/SKILL.md` 既有"步骤 0 ~ 步骤 15A / 步骤 7B ~ 10B"字节级保留(INV-2)
- `plugins/code-skills/skills/code-design/SKILL.md` 既有"末尾兜底提交"步骤 N 字节级保留
- 其他 11 个 `code-*` 技能 SKILL.md 字节级不变(FR-7.AC-7.1)
- `marketplace.json` / `plugin.json` / `assistants/rules/` 13 文件字节级不变(FR-8.AC-8.1 ~ AC-8.4)
- `code-plan/SKILL.md` / `code-plan/templates/plan.md` 在 T-002 实施(本任务**不**涉及)

## 2. 详细改动

### 改动 1:`code-design/SKILL.md` §步骤 0a L107 既有"不含步骤 0b"小注更新

- **原内容**:`code-design` **不**含步骤 0b(FR-2 显式仅 `code-require` 专属)。
- **新内容**:`code-design` 进入"步骤 0b 设计目标确认"(本需求 REQ-00011 新增,FR-1)。
- **理由**:FR-2 实际只针对原"需求澄清"问询;本需求 REQ-00011 把"步骤 0b"从 `code-require` 专属扩展到 `code-design` + `code-plan` 共 2 个技能。
- **INV-1 影响**:frontmatter 字节级保留(L1-3 不动)
- **INV-2 影响**:既有"步骤 0-N"流程仅 L107 这 1 句小注变化,其余 L106 / L108-117 字节级保留

### 改动 2:`code-design/SKILL.md` §步骤 0a L117 末尾追加"执行步骤 0b"提示

- **原内容**(L117 末尾):"进入既有'步骤 0 — 版本上下文检测'"
- **新内容**:"**执行'步骤 0b 设计目标确认'**(见下),成功后再进入既有'步骤 0 — 版本上下文检测'"
- **理由**:让读者在 §步骤 0a 末尾就看到"步骤 0b 在此之后"
- **INV-2 影响**:仅 L117 末尾 1 行追加,其余字节级保留

### 改动 3:`code-design/SKILL.md` 新增"### 步骤 0b — 设计目标确认"章节(L119-135)

- **位置**:§步骤 0a 之后(L118),§步骤 0 之前(L138)
- **完整内容**:
  ```markdown
  ### 步骤 0b — 设计目标确认(本需求 REQ-00011 新增,FR-1)
  1. 评估需求规模(小/中/大),自适应问题数(FR-6 强约束):
     - 小需求:1 个 `AskUserQuestion`(Q1 整体设计目标)
     - 中等需求:3 个 `AskUserQuestion`(Q1 + Q2 功能性 + Q3 扩展性)
     - 大需求:5 个 `AskUserQuestion`(Q1 + Q2 + Q3 + Q4 健壮性 + Q5 可维护性),可对不同细节功能分开提问(AC-6.3)
  2. 收集用户回答 → 调 `writeDesignGoalsSection(designResultPath, goals, "code-design")` 写入 `design/.../RESULT.md` 顶部"## 设计目标"小节(算法 2 / NFR-3 幂等覆盖)
  3. 屏显:
     ```
     === code-design 设计目标确认 ===
     整体设计目标:<--minimal/--extensible/--balanced>
     维度优先级:
       功能性:<高/中/低>  扩展性:<高/中/低>  健壮性:<高/中/低>  可维护性:<高/中/低>
     已回写至 design/<REQ>/RESULT.md "## 设计目标" 小节
     ```
  4. 用户取消 `AskUserQuestion` → 中止 + 回写空"## 设计目标"小节(E-3)
  5. **不**修改 frontmatter(INV-1)
  6. **不**修改"步骤 0"及之后的原有内容(INV-2)
  7. 完成后进入既有"步骤 0 — 版本上下文检测"
  ```
- **对应设计章节**:RESULT.md §4 模块 1,§5 算法 1 + 算法 2
- **依据规范**:FR-1(本需求新增步骤 0b)+ FR-5(回写小节)+ FR-6(多问)+ NFR-3 幂等 + INV-1 / INV-2 / INV-3 / INV-5

### 改动 4:`code-design/templates/design.md` 顶部"## 设计目标"占位(L25-27)

- **位置**:"## 文档头"模板区段(L9-23,代码块)后 + "## 1. 设计概述"(L26)前
- **完整内容**:
  ```markdown
  ## 设计目标
  <!-- 本节由 code-design / code-plan 步骤 0b 自动生成(写入或沿用),记录用户确认的设计目标;如需手动编辑,保留该注释以便步骤 0b 识别 -->
  ```
- **对应设计章节**:RESULT.md §4 模块 3,§3 D-8
- **依据规范**:`module-conventions.md §规则 1` 资源放 `templates/` 子目录 + INV-3 强约束(顶部"## 设计目标"小节位置)

## 3. 关键决策与权衡

### 决策 1:用 `### 步骤 0b` 标题(同 `### 步骤 0a`)
- **理由**:与既有"步骤 0a"模式同位叠加(NFR-6 强约束),与"步骤 0"既有"## 工作流程"段落平行
- **替代方案**:用"#### 步骤 0b"作为子节 — 拒绝理由:与"步骤 0a" / "步骤 0"既有的 3 级标题不平行

### 决策 2:屏显模板用"```代码块```"包裹
- **理由**:与既有"步骤 0a 失败处理"的代码块风格一致(步骤 0a 步骤 3 既有 3 个错误处理的代码块)

### 决策 3:`writeDesignGoalsSection` 函数名引用
- **理由**:与详细设计 RESULT.md §5 算法 2 的函数名一致,方便 AI 协作者对照

### 决策 4:不引入"## 设计目标"小节的写入位置详情
- **理由**:详情在模板占位中(`design.md` L25-27),`SKILL.md` 步骤 0b 章节只给"调 writeDesignGoalsSection"高层指令,避免在 SKILL.md 中堆砌细节

## 4. 偏离设计/规范的地方

**无**。本任务 100% 沿用概要设计 + 详细设计的指定内容(详情见 §2 详细改动)。

## 5. 验证结果

### 5.1 静态自检

| 检查项 | 结果 | 备注 |
| --- | --- | --- |
| INV-1 frontmatter 字节级保留 | ✅ | `code-design/SKILL.md` L1-3 字节级未动 |
| INV-2 既有"步骤 0-N"流程不变 | ✅ | L106-117 / L138-486 字节级未动(仅 L107 小注 1 句更新 + L117 末尾 1 行追加) |
| INV-3 顶部"## 设计目标"小节位置 | ✅ | `design.md` L25 在"## 文档头"区段后 + "## 1. 设计概述"前 |
| INV-5 幂等 | ✅ | 步骤 0b 步骤 2 明确调 `writeDesignGoalsSection`(算法 2 覆盖前次内容) |
| INV-8 不触发 `dashboard-conventions §规则 1` | ✅ | `code-design/SKILL.md` 不写看板;末尾兜底照常同步"概要设计清单" + "变更记录" |
| NFR-5 与 `code-auto` 0 冲突 | ✅ | `AskUserQuestion` 触发时 `code-auto` 沿用"总选推荐项" |
| FR-7.AC-7.1 不改 8 其他技能 | ✅ | 本任务**只**改 `code-design/SKILL.md` + `code-design/templates/design.md` 2 个文件;`code-plan/SKILL.md` + `code-plan/templates/plan.md` 在 T-002 改 |
| FR-8.AC-8.1 ~ AC-8.4 不改 marketplace / plugin / 规范 / README | ✅ | 全部字节级未动 |

### 5.2 编译/启动验证

**N/A**(本项目无构建/测试框架,纯 Markdown 技能;`code-unit` 守卫判定"不可测";任务测试状态=`不适用`)

### 5.3 端到端验证(下一步由 T-002 + `code-review` + `code-auto` 完成)

- 后续由 T-002 实施"读 `design/.../RESULT.md` 的"## 设计目标"小节"功能
- 后续由 `code-review` 评审本任务 + T-002 的实施
- 后续由 `code-auto` 调 `code-design REQ-...` 时验证步骤 0b 触发 + 屏显 + 写入文件全链路

## 6. 已知问题/未完成项

- **F-1**:`code-design` 步骤 0b 是否对所有需求都触发 5 问?(留作 follow-up,后续 `code-design` 调用时观察)
- **F-2**:`code-auto` 调 `code-design` 步骤 0b 时的具体屏显输出格式,需 `code-auto` 步骤 6 实际跑一个完整需求验证
- **F-3**:`code-review` 是否应感知"## 设计目标"小节?(留作后续版本,本需求**不**触发)

## 7. 关联任务与提交

### 提交

- 任务编码:`TASK-REQ-00011-00001`
- 提交哈希:见末尾(`git commit` 输出,`code-it` 末尾兜底步骤自动生成)
- commit message 预览:
  ```
  chore(code-it): TASK-REQ-00011-00001 code-design 增量追加步骤 0b
  ```

### 关联

- 上游:`plan/REQ-00011/PLAN.md` §TASK-REQ-00011-00001
- 下游:T-002(`code-plan/SKILL.md` 增量追加)
- 横向:**无**
