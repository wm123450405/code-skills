# 改修总结 — TASK-REQ-00006-00001

## 1. 任务信息

- **任务编码**:`TASK-REQ-00006-00001`
- **任务标题**:`[新增] 写 code-publish/SKILL.md(7 模块工作流 + frontmatter)`
- **类型**:新增
- **触发/来源**:需求新增
- **关联任务**:无
- **前置任务**:PLAN.md 中标注 T-002~T-006(用户已确认实际按 T-001 → ... 顺序执行;SKILL.md 仅字符串引用模板路径,不依赖文件存在)
- **来源 PLAN.md**:`./assistants/V0.0.2/plan/REQ-00006/PLAN.md` v1
- **完成时间**:2026-06-04 17:30
- **完成人**:wangmiao
- **提交哈希**:`<不提交 — 留 dirty tree 由用户在 T-007 后整体 commit>`

## 2. 改修内容总览

| 类别 | 路径 | 操作 | 大小 |
| --- | --- | --- | --- |
| 新增 | `plugins/code-skills/skills/code-publish/SKILL.md` | Write | 475 行,~16 KB |

**总计**:1 个新文件,0 个修改文件,0 个删除文件。

## 3. 详细改动

### 新增 `plugins/code-skills/skills/code-publish/SKILL.md`

#### 3.1 frontmatter(强约束 `skill-conventions §规则 1`)

```yaml
---
name: code-publish
description: 发布部署(版本感知)。要求用户提供可选位置参数"版本号"(缺省时取 `./assistants/.current-version`);先做发布前置检查(全检查最严:...);通过后在 `./assistants/<版本号>/publish/` 下生成 `DEPLOY.md` + `UPDATE.md`(基线跳过) + `Q&A.md`(从 `assistants/qanda/` 聚合);3 份手册均为"通用发布部署骨架 + placeholder + 默认示例",用户**必须**手动补全;本技能顺带创建 `assistants/qanda/` 目录与 `README.md`。**纯只读消费看板 + 不自动 commit + 不参与 REQ-00005**;在 `code-review` 完成后,长开发周期末使用;基线版本可直接调用归档。
---
```

- ✓ `name: code-publish` 与目录名 `code-publish` 一致
- ✓ `description` 完整非空非占位,~800 字符,覆盖目标/适用场景/关键触发/不参与项/上下游

#### 3.2 正文(13 大节,与既有 10 技能节奏一致)

1. `# code-publish — 发布部署(版本感知)`(H1 标题)
2. `## 目标`(与所有 10 技能对齐)
3. `## 适用场景`
4. `## 不适用`
5. `## 工作目录约定(强制)`
6. `## 输入`
7. `## 输出`
8. `## 工具使用约定`
9. `## 工作流程`(7 个子步骤)
10. `## 报告模板`(4 种场景)
11. `## 看板字段约定(只读消费)`
12. `## 衔接`
13. `## 不要做的事`

#### 3.3 7 个工作流子步骤

| 步骤 | 标题 | 实现模块 |
| --- | --- | --- |
| 0 | 版本上下文检测(强制前置) | (无对应逻辑模块,只是 .current-version 读取) |
| 1 | 发布前置检查(PreflightChecker) | 模块 2 |
| 2.0 | 基线识别(BaselineDetector) | 模块 3 |
| 2 | 生成手册(ManualBuilder) | 模块 4 |
| 2.5 | 创建 qanda/ 骨架(QandaScaffolder,条件) | 模块 5 |
| 2.6 | 聚合 Q&A 内容(QandaAggregator) | 模块 6 |
| 3 | 报告(ReportFormatter) | 模块 7 |

#### 3.4 异常路径(E-1 ~ E-10)

分布在相关步骤内,显式标注 "**异常路径**" 标记,与 `risk-analysis.md §1` 10 条异常路径一一对应。

#### 3.5 报告模板(4 种)

- 通过(非基线,qanda 有内容)
- 通过(基线)
- 不通过
- qanda 空(可与通过/基线模板组合)

外加 1 个无激活版本(无参数 + 无 .current-version)场景。

#### 3.6 看板字段约定(只读消费)

明确 3 区段的"解析锚点 + 解析字段 + 解决判定",与 `code-dashboard`(REQ-00004)共用同一份结构,严守 NFR-8。

#### 3.7 不要做的事(11 条)

与 needs §FR-8.AC-8.1~8.4 + NFR-3 / NFR-4 / NFR-5 / NFR-7 + 5 项默认 Q 锁定一一对应。

## 4. 关键决策与权衡(开发过程中做的选择)

### 决策 IT-1:frontmatter description 长度
- **选定**:`~800 字符`,覆盖目标/适用场景/关键触发/不参与项/上下游
- **理由**:本技能语义复杂(前置检查 + 3 份手册 + qanda 骨架 + 不自动 commit + 不参与 REQ-00005),短 description 不够;`code-design` 用了 ~600 字符,本技能 description 略长是合理的
- **依据**:`skill-conventions §规则 1`(description 完整自然语言)

### 决策 IT-2:章节顺序与既有 10 技能对齐
- **选定**:严格按 10 技能的章节顺序(目标/适用/不适用/工作目录/输入/输出/工具/工作流程/衔接/不要做)
- **理由**:用户认知成本
- **依据**:无强制;但 0 偏离

### 决策 IT-3:步骤 2.0 / 2.5 / 2.6 的"半步编号"
- **选定**:步骤 0 → 1 → 2.0 → 2 → 2.5 → 2.6 → 3
- **理由**:步骤 2.0 是步骤 2 的前置;步骤 2.5 / 2.6 是步骤 2 的"附加";既符合执行顺序,又保持主流程 4 步(0/1/2/3)的清晰
- **依据**:与 `code-review` 等技能混用"步骤 X.Y"一致

### 决策 IT-4:每个工具调用都显式写
- **选定**:每步中显式写"`Bash: mkdir -p ...`" / "`Read: ...`" / "`Write: ...`" / "`Glob: ...`"
- **理由**:Claude 需要知道"用什么工具";"不暗示"会让 Claude 自行决定,可能走偏
- **依据**:既有 10 技能的章节内均显式说明

### 决策 IT-5:错误退出的"不阻塞 vs 立即退出"二元行为
- **选定**:
  - **不阻塞**:`qanda/` 骨架创建失败(FR-7.AC-7.4)
  - **立即退出**:前置检查不通过 / publish/ 写入失败 / 无 .current-version
- **依据**:detail design `risk-analysis.md §1` + needs §9 + 模仿 `code-version` 步骤 0

### 决策 IT-6:报告模板放 SKILL.md 内,不放在 templates/
- **选定**:4 种报告模板作为 fenced code block 放在 SKILL.md 的"## 报告模板"小节
- **理由**:报告是"运行时 stdout",生命周期不同于"生成的静态文档";SKILL.md 内 = Claude 必读
- **依据**:无规范强制

## 5. 偏离设计/规范的地方

**0 项**。详 `deviations.md`。

## 6. 验证结果(详 `compile-and-run.md`)

| 验证项 | 结论 |
| --- | --- |
| SKILL.md frontmatter `name` = 目录名 | ✓ `code-publish` |
| SKILL.md frontmatter `description` 非空非占位 | ✓ ~800 字符 |
| 章节顺序与既有 10 技能一致 | ✓ |
| `skill-conventions §规则 1` | ✓ |
| `module-conventions §规则 1` | ✓ |
| 不修改既有 10 技能 / rules / CLAUDE.md / README / marketplace / plugin | ✓ (`git status` 验证) |

**端到端验证**:由 T-007 在收尾阶段执行。

## 7. 已知问题/未完成项

### 已知问题
- **无**

### 未完成项(由后续任务承接)
- **T-002 ~ T-006**:5 份模板文件待写(本任务的 SKILL.md 中已引用其路径)
- **T-007**:不变量自检 + 端到端 3 场景验证
- **T-008**:双 README "主要能力"段同步(独立任务)
- **Q-D-1**(留 v2):`code-publish` 注册到 `marketplace.json` + `plugin.json`
- **Q-D-2**(本计划已纳入 T-008)
- **Q-D-3 ~ Q-D-7**(留 code-review / 其他 REQ)

## 8. 关联任务与提交

- **关联原任务**:无
- **关联后续任务**:T-002, T-003, T-004, T-005, T-006, T-007, T-008
- **Git 提交**:**未提交**(遵循 NFR-3 + 沿用 V0.0.0~V0.0.1 实践"涉及 publish/ 与 qanda/ 的 commit 由用户手动完成");**T-007 收尾时由用户整体 commit**

## 9. 步骤 14 状态更新(PLAN.md)

| 字段 | 旧值 | 新值 |
| --- | --- | --- |
| 开发状态 | 进行中 | **已完成** |
| 完成时间 | — | 2026-06-04 17:30 |
| 完成人 | — | wangmiao |
| 提交哈希 | — | (不提交) |

## 10. 步骤 15 看板同步(详情见 `version-board-sync.md`)

- 看板"任务清单"中 T-001 行:开发状态 `进行中` → `已完成` + 完成时间 2026-06-04 17:30
- 看板"变更记录"追加:2026-06-04 17:30 开发状态更新 T-001
- 看板"最近更新"更新

> **重要**:本任务的"完成"是**逻辑完成**(SKILL.md 文件已写好),**非 git 完成**;待 T-007 收尾时由用户统一 commit。

## 11. 下一步建议

1. **下一任务**:`/code-skills:code-it TASK-REQ-00006-00002`(DEPLOY.md 模板,~0.3d)
2. **建议并行执行**:T-002 ~ T-006 + T-008(6 任务全部独立,可并行)
3. **收尾**:`/code-skills:code-it TASK-REQ-00006-00007`(不变量自检 + 端到端 3 场景)
4. **评审**:`/code-skills:code-review REQ-00006`(Q-D-1 / Q-D-3 / Q-D-5 / Q-D-7 决策)
