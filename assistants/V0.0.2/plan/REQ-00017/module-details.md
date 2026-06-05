# 模块详细化 — REQ-00017
版本:V0.0.2

## 模块 1:/code-plan SKILL.md 锚点 A
- **路径**:`plugins/code-skills/skills/code-plan/SKILL.md`
- **关键段落**:§步骤 10A 任务拆分 → "#### 任务类型"小节**前**
- **调用顺序**:`/code-plan` 步骤 10A 拆任务时读取本段作为强约束
- **状态归属**:文档约束,无运行时状态
- **与概要设计的对应**:§3.1 / D-1
- **符合的规范**:`skill-conventions.md §规则 1` / `doc-conventions.md`

## 模块 2:/code-plan SKILL.md 锚点 B
- **路径**:`plugins/code-skills/skills/code-plan/SKILL.md`
- **关键段落**:§步骤 16A 同步版本看板(强制) → 第 3 款**前**
- **调用顺序**:`/code-plan` 步骤 16A 同步看板时读取本段作为强约束
- **状态归属**:文档约束,无运行时状态
- **与概要设计的对应**:§3.2 / D-1 / FR-4
- **符合的规范**:`skill-conventions.md §规则 1` / `dashboard-conventions.md §规则 1`

## 模块 3:/code-it SKILL.md 锚点 C
- **路径**:`plugins/code-skills/skills/code-it/SKILL.md`
- **关键段落**:§末尾兜底提交 → 步骤 5 执行 commit 成功判断**后**
- **调用顺序**:`/code-it` 末尾兜底 commit 成功后自动执行 P-1
- **状态归属**:运行时 read-modify-write 看板文件
- **与概要设计的对应**:§3.3 / D-2~D-8 / FR-2
- **符合的规范**:`skill-conventions.md §规则 1` / `dashboard-conventions.md §规则 1` / `encoding-conventions.md §规则 1+3`
