# 改修总结 — TASK-REQ-00040-00004 · [修改] assistants-layout.md 同步追加 reproduce/ 子目录行

- 任务编码:TASK-REQ-00040-00004
- 任务标题:[修改] assistants-layout.md 同步追加 reproduce/ 子目录行(在 fix/<BUG-NNN>/ 子目录列表)
- 所属版本:V0.0.3
- 所属需求:REQ-00040
- 触发/来源:详细设计
- 任务类型:修改
- 完成时间:2026-06-25
- 上游:`./assistants/V0.0.3/plan/REQ-00040/PLAN.md §3 TASK-REQ-00040-00004` + `RESULT.md §4.5 模块 5`

## 1. 任务信息

- **任务编码**:`TASK-REQ-00040-00004`
- **标题**:assistants-layout.md 同步追加 reproduce/ 子目录行
- **类型**:修改(Markdown 模板扩展)
- **触发/来源**:详细设计
- **关联任务**:REQ-00040
- **里程碑**:M1-REQ-00040

## 2. 改修内容总览

- **修改的文件**:`plugins/code-skills/skills/code-fix/templates/assistants-layout.md`(1 个文件)
- **新增的行数**:1 行
- **删除的行数**:0
- **新增文件**:0
- **删除文件**:0

## 3. 详细改动

### 3.1 `plugins/code-skills/skills/code-fix/templates/assistants-layout.md`

#### 3.1.1 修改位置

- 锚点:`## 目录结构` 段(line 7-23 ASCII 树)中,`BUG-00001/` 子目录列表(line 12-19)末尾
- 修改方式:`Edit` 工具在 line 19 `deviations.md` 行后 + line 20 `BUG-00002/` 行前追加 1 行
- 字节级保留:BUG-00001 头(line 12)+ BUG-00001 子目录 7 行(line 13-19)+ BUG-00002 头(line 20)+ BUG-00002 占位 2 行(line 21-22)+ 关键约束段 + 文件名约定段

#### 3.1.2 新增内容字面

| 操作 | 字面 |
| --- | --- |
| 追加 | `│ └── reproduce/ # 复现产物(由 code-fix 步骤 6 末尾生成,可选)` |

#### 3.1.3 字节级保留

- BUG-00001 头(line 12)字节级保留
- BUG-00001 子目录 7 行(line 13-19)字节级保留
- BUG-00002 头(line 21)+ 占位 2 行(line 22-23)字节级保留
- 关键约束段(line 26-31)字节级保留(仅位置后移 1 行)
- 文件名约定段(line 33-38)字节级保留(仅位置后移 1 行)

#### 3.1.4 关键决策(本任务无新决策,沿用 PLAN.md)

- 在 BUG-00001 子目录列表末尾追加(沿用 D-8,同步更新 `assistants-layout.md`)
- 注释"由 code-fix 步骤 6 末尾生成,可选"(沿用 FR-2,提示产物是可选的)
- 命名 `reproduce/`(沿用 FR-4 + PD-8,小写 + 复数)

## 4. 关键决策与权衡

**0 项新决策**。本任务**完全**沿用 PLAN.md §3 TASK-REQ-00040-00004 + 详细设计 §4.5 + 概设 D-8。

## 5. 偏离设计/规范的地方

**0 项偏离**(详见 `deviations.md`)。本任务所有改动与上游字面一致。

## 6. 验证结果

### 6.1 静态校验(本任务范围内)

- **AC-7**:既有结构字节级未变 → **✓ 通过**(BUG-00001 头 + 子目录 7 行 + BUG-00002 头 + 占位 2 行 + 关键约束 + 文件名约定 全部字节级保留,仅位置后移 1 行)
- **AC-11**:`Grep` 关键词("本需求 REQ-00040" / "沿用原" / "Q-X 锁定")→ **0 命中**

### 6.2 端到端降级为静态

- 本任务**不**涉及可启动项目(纯 Markdown 技能库)
- 12 条 AC 端到端验证由 T-005 承担

## 7. 已知问题 / 未完成项

- **0 项**。本任务所有改动按 PLAN.md §3 + 详细设计 §4.5 完整落地

## 8. 过程文档清单(由 code-it 内化)

### 8.1 工作流上下文
```typescript
const decisions = {
  workLog: '生成',
  compileAndRun: '不生成',  // 纯 Markdown 改造
  deviations: '生成',
  testResults: '不生成',     // 测试状态 = 不适用
  unitTestResults: '生成',  // 占位
  kanbanChangeLog: '生成',
  processDocDecisions: '生成',
};
```

### 8.2 决策结果表

| 过程文档 | 决策 | 理由 |
| --- | --- | --- |
| `work-log.md` | ✅ 生成 | 任务实施日志 |
| `compile-and-run.md` | ❌ 不生成 | 纯 Markdown 改造 |
| `deviations.md` | ✅ 生成 | 评审要查;内容 = 0 偏离 |
| `test-results.md` | ❌ 不生成 | 测试状态 = 不适用 |
| `unit-test-results.md` | ✅ 生成(占位) | 任务类型 = 文档 |
| 看板"变更记录" | ✅ 生成 | 本轮有任务完成 + 状态推进 |
| `process-doc-decisions.md` | ✅ 生成(本文件) | 有不生成项 |

### 8.3 决策依据

- 引用 `code-it/SKILL.md` §"## 过程文档自适应判定"(line 101-138)与 §"## 步骤 8.7"(line 805+)的判定准则

### 8.4 关联任务

- **前置任务**:TASK-REQ-00040-00001 / TASK-REQ-00040-00002 / TASK-REQ-00040-00003(全部已完成)
- **后置任务**:**无**(本任务是 M1-REQ-00040 6 任务中的第 4 个;后续 T-005 端到端验证)
- **取代任务**:**无**
- **关联 code-check**:M1-REQ-00040 里程碑全部 6 任务完成后,由 `code-check` 评审

## 9. 单元测试

**0 项**。详见 `unit-test-results.md`。

## 10. 逻辑行统计

**不适用**(NFR-8 锁定)。

## 11. 变更记录

| 时间 | 变更类型 | 变更摘要 | 关联项 |
| --- | --- | --- | --- |
| 2026-06-25 14:46 | 任务完成 | TASK-REQ-00040-00004 完成(开发状态:已完成);`assistants-layout.md` BUG-00001 子目录列表末尾追加 1 行 `│ └── reproduce/ # 复现产物(由 code-fix 步骤 6 末尾生成,可选)`;既有结构(7 子文件 + 关键约束 + 文件名约定)字节级保留;0 偏离;AC-7 / AC-11 静态校验通过 | TASK-REQ-00040-00004 |