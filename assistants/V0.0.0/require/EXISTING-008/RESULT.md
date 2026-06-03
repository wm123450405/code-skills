# 现有功能需求 — EXISTING-008:单元测试(code-unit)

> 本文档由 `code-init` 技能基于项目现有代码生成。
> 描述的是"**代码中已实现**"的功能,而非待开发的功能。
> 未来对该功能的**修改**应通过 `code-require`(增量更新本文件)进行。
> 最后更新:2026-06-03 18:10
> 适用版本:基线版本 `V0.0.0`

## 需求概述
`code-unit` 是主流程的**第六步**(版本感知):接收任务编码(`REQ-YYYY-NNNN-NNN`),从 `plan/<需求>/RESULT.md` 读详细设计,`PLAN.md` 读任务详情,`code/<任务>/RESULT.md` 读代码改修正文,`./assistants/rules/` 读跨版本编码规范,编写或补充本任务涉及功能的单元测试。**必须运行**本任务与相关联模块的单元测试,迭代修复直到全部通过(或明确标"不适用")。

## 现有实现位置

| 维度 | 位置 |
| --- | --- |
| 主要文件 | `plugins/code-skills/skills/code-unit/SKILL.md`(452 行) |
| 关键函数/类 | (N/A) |
| 涉及文件数 | 4(SKILL.md + 2 个模板 + assistants-layout) |
| 大致代码量 | 约 540 行 |

### 关键代码位置(可选)
- `plugins/code-skills/skills/code-unit/SKILL.md` — 工作流(读 .current-version → 校验任务存在 → 读 plan/ + code/ + rules/ → 写/补单测 → 运行 → 迭代 → 更新看板)
- `plugins/code-skills/skills/code-unit/templates/RESULT.md` — 任务级 RESULT.md 模板
- `plugins/code-skills/skills/code-unit/templates/test-spec.md` — 测试规格说明模板
- `plugins/code-skills/skills/code-unit/templates/assistants-layout.md`

## 用户角色与场景

### 角色
- **开发者**:补齐某任务的单元测试、验证测试是否通过、提升覆盖率

### 场景
- 补齐某任务的单元测试
- 验证测试是否通过
- 提升覆盖率

## 功能点(FR)

- **FR-1**:读 `.current-version` 确认激活版本
- **FR-2**:校验任务编码 + `code/<任务>/RESULT.md` 存在(任务必须先在 `code-it` 完成开发)
- **FR-3**:读 `plan/<需求>/RESULT.md` 详细设计
- **FR-4**:读 `PLAN.md` 任务详情(含测试要点)
- **FR-5**:读 `code/<任务>/RESULT.md` 代码改修正文
- **FR-6**:读 `./assistants/rules/` 跨版本编码规范
- **FR-7**:编写或补充本任务涉及功能的单元测试
- **FR-8**:**必须运行**本任务与相关联模块的单元测试,迭代修复直到全部通过(或明确标"不适用")
- **FR-9**:将"改修"总结保存到 `test/<任务>/RESULT.md`
- **FR-10**:把 `PLAN.md` 中该任务的**测试状态**推进(已编写 → 已运行-通过/失败 / 不适用 / 阻塞)
- **FR-11**:同步更新看板"任务清单"(测试状态)/ "缺陷清单"(若发现代码 bug)/ "变更记录"

## 关键接口

### CLI
```
/code-skills:code-unit REQ-2026-0001-001
```

### 输入
- `./assistants/<版本号>/plan/<需求>/RESULT.md`(详细设计)
- `./assistants/<版本号>/plan/<需求>/PLAN.md`(任务详情)
- `./assistants/<版本号>/code/<任务>/RESULT.md`(代码改修正文)
- `./assistants/rules/`(跨版本编码规范)

### 输出
- 测试代码
- `./assistants/<版本号>/test/<任务>/RESULT.md`

## 数据模型(若适用)

| 实体 | 字段 | 约束 |
| --- | --- | --- |
| 测试状态 | 未编写/已编写/已运行-通过/已运行-失败/不适用/阻塞 | 看板"任务清单"字段 |
| 测试模板 | `test-spec.md` | 字段:用例/输入/预期输出/边界/异常/覆盖点 |
| 任务级 RESULT | `test/<任务>/RESULT.md` | 字段:已编写用例/已运行结果/失败原因/迭代记录/最终状态 |

## 验收标准(AC)

- **AC-1**:无 `.current-version` 时立即中止
- **AC-2**:`code/<任务>/RESULT.md` 不存在时立即中止(任务开发未完成)
- **AC-3**:`PLAN.md` 中本任务存在
- **AC-4**:**必须运行**本任务与相关联模块的单元测试,迭代修复直到全部通过(或明确标"不适用")
- **AC-5**:写 `test/<任务>/RESULT.md` 含"改修"总结
- **AC-6**:推进 `PLAN.md` 中该任务的测试状态
- **AC-7**:同步更新看板"任务清单"(测试状态)
- **AC-8**:发现代码 bug 时同步更新看板"缺陷清单"

## 关联功能

| 关联编码 | 关联点 | 影响 |
| --- | --- | --- |
| EXISTING-007 | 读 `code/<任务>/RESULT.md` 作为输入 | 强制上游(`code-it` 必须完成) |
| EXISTING-006 | 读 `plan/<需求>/RESULT.md` + `PLAN.md` 作为输入 | 主流程上游 |
| EXISTING-010 | 下游:补完单测后调 `code-review` 整需求评审 | 强制后续 |
| EXISTING-003 | 读 `rules/` 作为约束 | 强约束 |
| EXISTING-002 | `code-version` 是前置门 | 必须先有激活版本 |

## 已知限制/技术债

- "相关联模块"边界由 AI 自主判断,无静态依赖图工具辅助
- "迭代修复直到全部通过"会触发代码修改(写回),与 `code-it` 边界模糊 —— 没有明确"测试阶段不重构代码"的约束
- "不适用" 判定标准模糊(纯文档改动?无逻辑函数?);不同项目会有不同解读
- 不自动算覆盖率(若用户配置了覆盖率工具,需在 SKILL.md 显式说明)
- 也可独立重跑以补齐测试(允许 `code-it` 完成后任意时刻调),但**不**保证老任务在规范更新后自动重测

## 变更记录

| 时间 | 变更类型 | 变更摘要 | 关联项 |
| --- | --- | --- | --- |
| 2026-06-03 18:10 | 需求登记 | code-init 识别并登记现有功能 EXISTING-008 | EXISTING-008 |
