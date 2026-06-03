# 现有功能需求 — EXISTING-006:详细设计与任务计划(code-plan)

> 本文档由 `code-init` 技能基于项目现有代码生成。
> 描述的是"**代码中已实现**"的功能,而非待开发的功能。
> 未来对该功能的**修改**应通过 `code-require`(增量更新本文件)进行。
> 最后更新:2026-06-03 18:10
> 适用版本:基线版本 `V0.0.0`

## 需求概述
`code-plan` 是主流程的**第四步** + 缺陷修复流程的**规划步骤**(**双路径**,版本感知):按"输入 ID 格式"自动判定走主流程(`REQ-YYYY-NNNN`)还是缺陷分支(`BUG-NNN`)。主流程产 `plan/<id>/{RESULT.md, PLAN.md}`;缺陷分支产 `fix/<id>/fix-plan.md`。两者都同步更新版本看板(主流程更新"详细设计与任务计划汇总/任务清单/里程碑/变更记录";缺陷分支更新"缺陷清单/变更记录")。

## 现有实现位置

| 维度 | 位置 |
| --- | --- |
| 主要文件 | `plugins/code-skills/skills/code-plan/SKILL.md`(715 行,本项目最大) |
| 关键函数/类 | (N/A) |
| 涉及文件数 | 5(SKILL.md + 4 个模板) |
| 大致代码量 | 约 800 行 |

### 关键代码位置(可选)
- `plugins/code-skills/skills/code-plan/SKILL.md` — 双路径入口判定(REQ vs BUG)→ 各自工作流
- `plugins/code-skills/skills/code-plan/templates/plan.md` — 主流程详细设计模板
- `plugins/code-skills/skills/code-plan/templates/task-plan.md` — 任务计划模板
- `plugins/code-skills/skills/code-plan/templates/fix-plan.md` — 缺陷修复方案模板
- `plugins/code-skills/skills/code-plan/templates/assistants-layout.md`

## 用户角色与场景

### 角色
- **项目负责人 / 高级开发**:把需求拆成可执行任务;或为已登记的 bug 规划修复方案

### 场景
- 跨多文件/多模块的改动
- 需要多人协作或分阶段交付
- 任何在动手编码前希望降低返工成本的场景
- 已有 RESULT.md/PLAN.md,根据进展更新计划与状态
- 缺陷分支:为 `code-fix` 登记的 bug 产出修复方案

## 功能点(FR)

- **FR-1**:读 `.current-version` 确认激活版本
- **FR-2**:按输入 ID 格式自动判定路径(`REQ-YYYY-NNNN` → 主流程;`BUG-NNN` → 缺陷分支)
- **FR-3 (主流程)**:读 `require/<id>/RESULT.md` + `design/<id>/RESULT.md`(上游)
- **FR-4 (主流程)**:产出 `plan/<id>/RESULT.md`(详细设计)+ `PLAN.md`(任务拆分,任务编号格式 `REQ-YYYY-NNNN-NNN`,3 位数任务序号)
- **FR-5 (主流程)**:同步更新看板"详细设计与任务计划汇总" + "任务清单" + "里程碑" + "变更记录"
- **FR-6 (缺陷分支)**:读 `fix/<id>/RESULT.md`(上游)
- **FR-7 (缺陷分支)**:产出 `fix/<id>/fix-plan.md`(选定方案 + 风险 + 回退)
- **FR-8 (缺陷分支)**:同步更新看板"缺陷清单" + "变更记录",并同步 `fix/RESULT.md`
- **FR-9 (双路径共)**:读 `./assistants/rules/` 作为约束

## 关键接口

### CLI
```
/code-skills:code-plan REQ-2026-0001   # 主流程路径
/code-skills:code-plan BUG-001          # 缺陷分支路径
/code-skills:code-plan                  # 交互式
```

### 输出
- 主流程:`./assistants/<版本号>/plan/<需求编码>/{RESULT.md, PLAN.md}`
- 缺陷分支:`./assistants/<版本号>/fix/<缺陷编号>/fix-plan.md`
- 同步更新 `<版本号>/RESULT.md` 看板

## 数据模型(若适用)

| 实体 | 字段 | 约束 |
| --- | --- | --- |
| 任务编号 | `REQ-YYYY-NNNN-NNN` | 3 位顺序号,同需求内唯一 |
| 任务状态(双轴) | 开发状态 × 测试状态 | 详见 EXISTING-007/008 |
| 触发/来源 | 13 个枚举 | 决定 `code-it` 读 `plan/` 还是 `review/` |
| 主流程模板 | `plan.md` + `task-plan.md` | 字段:目标/前置/详细步骤/接口签名/测试要点/风险/回退 |
| 缺陷模板 | `fix-plan.md` | 字段:根因/方案选型/影响面/风险/回退/测试要点 |

## 验收标准(AC)

- **AC-1**:输入 `REQ-2026-0001` → 校验 `require/REQ-2026-0001/RESULT.md` + `design/REQ-2026-0001/RESULT.md` 都存在,缺一则中止
- **AC-2**:输入 `BUG-001` → 校验 `fix/BUG-001/RESULT.md` 存在,缺则中止
- **AC-3**:主流程产 `plan/<id>/{RESULT.md, PLAN.md}` 两份文件,符合对应模板
- **AC-4**:缺陷分支产 `fix/<id>/fix-plan.md`,符合 `fix-plan.md` 模板
- **AC-5**:主流程同步更新看板的"详细设计与任务计划汇总" + "任务清单" + "里程碑" + "变更记录"
- **AC-6**:缺陷分支同步更新看板的"缺陷清单" + "变更记录",并同步 `fix/RESULT.md`
- **AC-7**:任务编号格式严格 `REQ-YYYY-NNNN-NNN`,3 位数任务序号
- **AC-8**:无 `.current-version` 时立即中止

## 关联功能

| 关联编码 | 关联点 | 影响 |
| --- | --- | --- |
| EXISTING-004 / 005 | 主流程上游 | 两者必须完成才能进 `code-plan` 主流程 |
| EXISTING-009 | 缺陷分支上游(`fix/BUG-NNN/RESULT.md` 由 `code-fix` 写) | 缺陷必须先登记才能进 `code-plan` 缺陷分支 |
| EXISTING-007 | `code-it` 读 `plan/<id>/RESULT.md` + `PLAN.md` 作为输入 | 主流程下游 |
| EXISTING-007 (BUG) | `code-it BUG-NNN` 读 `fix-plan.md` 作为输入 | 缺陷分支下游 |
| EXISTING-002 | `code-version` 是前置门 | 必须先有激活版本 |

## 已知限制/技术债

- 同一需求下任务拆分的粒度完全由 AI 决定(团队需自己定义"任务=多大")
- `PLAN.md` 中任务的"测试要点"是描述性,实际测试在 `code-unit` 阶段补齐 —— 缺少"PLAN.md 阶段就生成测试骨架"的强约束
- 主流程与缺陷分支的产物在不同的子目录下(plan/ vs fix/),**不**互通 —— 同一需求的修复任务需要走主流程"需求变更"而不是缺陷分支
- 双路径判定只看 ID 格式,不校验 BUG 是否真存在 —— 输错 BUG-001 也会启动

## 变更记录

| 时间 | 变更类型 | 变更摘要 | 关联项 |
| --- | --- | --- | --- |
| 2026-06-03 18:10 | 需求登记 | code-init 识别并登记现有功能 EXISTING-006 | EXISTING-006 |
