# BUG-00005 修复详细设计

- 缺陷编号:BUG-00005
- 所属版本:V0.0.3
- 上游引用:`./assistants/V0.0.3/fix/BUG-00005/RESULT.md`(缺陷详情)
- 遵循规范:13 份项目级规范(只读)
- 状态:已完成
- 责任人:wangmiao
- 创建:2026-06-22 14:50
- 最近更新:2026-06-23
- 当前版本:v2

## 1. 概述

本详细设计旨在修复 BUG-00005:`/code-require` 仍出现技术选型问路,违反 REQ-00033 字面硬约束。通过在步骤 7A 和步骤 8A 添加双重过滤机制,确保 `code-require` 只关注功能/行为/结构类需求,技术选型类问题自动跳过并记录到 clarifications.md,留待 `code-design` 阶段处理。

## 2. 上游引用

- **缺陷详情**:`./assistants/V0.0.3/fix/BUG-00005/RESULT.md`(code-fix 登记)
- **关联需求**:REQ-00033(`code-require` 不应分析或记录技术选型相关内容)
- **项目级规范**:13 份(只读)

## 3. 规范遵循

本修复严格遵循以下规范:
- `encoding-conventions §规则 1`:接收端宽松正则
- `skill-conventions §规则 2`:不引入新字段
- `coding-style.md`:命名规范
- `module-conventions.md`:模块结构规范
- `dashboard-conventions.md`:看板字段约定

## 4. 模块详细化

### 4.1 code-require/SKILL.md 步骤 7A 过滤器模块

**位置**:`plugins/code-skills/skills/code-require/SKILL.md` 步骤 7A(L322-333)

**改动内容**:
- 在步骤 7A 的"每轮问答"逻辑后,添加子步骤:"过滤技术选型类问题"
- 若问题涉及"技术选型 / 实现方式 / 框架 / 库"等关键词,自动跳过并记录到 `clarifications.md` 的 `deferred-to-code-design` 区段

**调用顺序**:
1. 步骤 7A 生成 AskUserQuestion 候选选项
2. 子步骤:过滤技术选型类问题
3. 若过滤后无选项 → 记录到 clarifications.md 并跳过
4. 若过滤后有选项 → 正常使用 AskUserQuestion

**状态归属**:无状态(纯过滤逻辑)

**与概要设计的对应**:对应方案 B(步骤 7A + 8A 双重过滤)

**符合的规范**:`skill-conventions §规则 2`(不引入新字段)

### 4.2 code-require/SKILL.md 步骤 8A NFR 过滤器模块

**位置**:`plugins/code-skills/skills/code-require/SKILL.md` 步骤 8A(L335-351)

**改动内容**:
- 在步骤 8A 的"NFR 记录"逻辑中,添加过滤条件:若 NFR 涉及"技术选型 / 实现方式"等关键词,标记为 `defer-to-code-design` 并在 `clarifications.md` 中记录

**调用顺序**:
1. 步骤 8A 提取 NFR 候选
2. 过滤技术选型类 NFR
3. 若过滤后为技术选型类 → 标记 `defer-to-code-design` 并记录到 clarifications.md
4. 若过滤后为功能/性能/安全类 → 正常记录到 RESULT.md

**状态归属**:无状态(纯过滤逻辑)

**与概要设计的对应**:对应方案 B(步骤 7A + 8A 双重过滤)

**符合的规范**:`skill-conventions §规则 2`(不引入新字段)

### 4.3 code-require/SKILL.md 步骤 615 硬约束增强模块

**位置**:`plugins/code-skills/skills/code-require/SKILL.md` 步骤 615

**改动内容**:
- 在步骤 615 的硬约束后,添加引用:"步骤 7A / 步骤 8A 中的技术选型类问题应自动跳过并记录到 clarifications.md"

**调用顺序**:
1. 步骤 615 检查硬约束
2. 引用步骤 7A / 8A 的过滤逻辑
3. 确保所有步骤都尊重"不涉及技术选型"约束

**状态归属**:无状态(纯约束声明)

**与概要设计的对应**:对应方案 B(步骤 7A + 8A 双重过滤)的补充

**符合的规范**:`skill-conventions §规则 2`(不引入新字段)

## 5. 算法与逻辑

### 5.1 步骤 7A 技术选型过滤算法

```
function filterTechSelectionQuestions(questions: AskUserQuestion[]): {
  validQuestions: AskUserQuestion[],
  deferredQuestions: DeferredQuestion[]
} {
  const techSelectionKeywords = [
    '技术选型', '实现方式', '框架', '库', '工具',
    'monorepo', 'single-package', 'pnpm', 'npm', 'yarn',
    'Jest', 'Vitest', 'Mocha', 'React', 'Vue', 'Angular',
    '数据库', 'ORM', '消息队列', '缓存', 'Redis', 'MongoDB'
  ];

  const validQuestions = [];
  const deferredQuestions = [];

  for (const question of questions) {
    const questionText = question.question.toLowerCase();
    const hasTechSelection = techSelectionKeywords.some(keyword =>
      questionText.includes(keyword.toLowerCase())
    );

    if (hasTechSelection) {
      deferredQuestions.push({
        question: question.question,
        reason: '技术选型类问题,应留待 code-design 阶段处理',
        deferredTo: 'code-design'
      });
    } else {
      validQuestions.push(question);
    }
  }

  return { validQuestions, deferredQuestions };
}
```

**复杂度**:O(n × m),其中 n = 问题数,m = 关键词数(通常 n < 10, m = 20,可接受)

**边界条件**:
- 空问题列表 → 返回 `{ validQuestions: [], deferredQuestions: [] }`
- 所有问题都是技术选型类 → 全部延迟,返回 `{ validQuestions: [], deferredQuestions: [...] }`
- 无技术选型类问题 → 全部有效,返回 `{ validQuestions: [...], deferredQuestions: [] }`

### 5.2 步骤 8A NFR 技术选型过滤算法

```
function filterTechSelectionNFRs(nfrs: NFR[]): {
  validNFRs: NFR[],
  deferredNFRs: DeferredNFR[]
} {
  const techSelectionKeywords = [
    '技术选型', '实现方式', '框架', '库', '工具',
    '数据库', 'ORM', '消息队列', '缓存', 'Redis', 'MongoDB',
    'pnpm-workspace', 'monorepo', 'single-package'
  ];

  const validNFRs = [];
  const deferredNFRs = [];

  for (const nfr of nfrs) {
    const nfrText = nfr.description.toLowerCase();
    const hasTechSelection = techSelectionKeywords.some(keyword =>
      nfrText.includes(keyword.toLowerCase())
    );

    if (hasTechSelection) {
      deferredNFRs.push({
        nfr: nfr,
        reason: '技术选型类 NFR,应标记为 defer-to-code-design',
        deferredTo: 'code-design'
      });
    } else {
      validNFRs.push(nfr);
    }
  }

  return { validNFRs, deferredNFRs };
}
```

**复杂度**:O(n × m),其中 n = NFR 数,m = 关键词数(通常 n < 20, m = 20,可接受)

**边界条件**:
- 空 NFR 列表 → 返回 `{ validNFRs: [], deferredNFRs: [] }`
- 所有 NFR 都是技术选型类 → 全部延迟,返回 `{ validNFRs: [], deferredNFRs: [...] }`
- 无技术选型类 NFR → 全部有效,返回 `{ validNFRs: [...], deferredNFRs: [] }`

## 6. 数据结构

本修复不涉及数据库/缓存变更,仅涉及运行时数据:

### 6.1 DeferredQuestion(延迟问题记录)

```typescript
interface DeferredQuestion {
  question: string;        // 原始问题文本
  reason: string;          // 延迟原因(如"技术选型类问题,应留待 code-design 阶段处理")
  deferredTo: 'code-design'; // 延迟到哪个技能
}
```

### 6.2 DeferredNFR(延迟 NFR 记录)

```typescript
interface DeferredNFR {
  nfr: NFR;                // 原始 NFR 对象
  reason: string;          // 延迟原因(如"技术选型类 NFR,应标记为 defer-to-code-design")
  deferredTo: 'code-design'; // 延迟到哪个技能
}
```

## 7. 接口

本修复不涉及接口变更(无 REST/gRPC/事件接口)。

## 8. 异常处理

### 8.1 过滤失败

**触发条件**:步骤 7A 或 8A 的过滤逻辑抛出异常(如关键词列表为空)

**检测手段**:try-catch 包裹过滤逻辑

**处理策略**:
- 记录警告到 `work-log.md`
- 回退到不过滤模式(所有问题/NFR 都有效)
- 继续执行后续步骤

**监控指标**:过滤失败次数(记录到 `work-log.md`)

### 8.2 clarifications.md 写入失败

**触发条件**:写入 `clarifications.md` 时 IO 错误

**检测手段**:try-catch 包裹写入逻辑

**处理策略**:
- 记录警告到 `work-log.md`
- 继续执行后续步骤(不阻断主流程)

**监控指标**:写入失败次数(记录到 `work-log.md`)

## 9. 安全要求

本修复不涉及安全相关变更(无鉴权/授权/输入校验/敏感数据处理)。

## 10. 状态机/流程

### 10.1 步骤 7A 流程(修复后)

```
[步骤 7A 开始]
  ↓
[生成 AskUserQuestion 候选选项]
  ↓
[子步骤:过滤技术选型类问题]
  ↓
{过滤后有选项?}
  ├─ 是 → [使用 AskUserQuestion 工具]
  │        ↓
  │       [记录到 clarifications.md]
  │        ↓
  │       [迭代下一批问题]
  └─ 否 → [记录到 clarifications.md 的 deferred-to-code-design 区段]
           ↓
          [跳过本批问题]
           ↓
          [迭代下一批问题]
```

### 10.2 步骤 8A 流程(修复后)

```
[步骤 8A 开始]
  ↓
[提取 NFR 候选]
  ↓
[过滤技术选型类 NFR]
  ↓
{过滤后为技术选型类?}
  ├─ 是 → [标记 defer-to-code-design]
  │        ↓
  │       [记录到 clarifications.md]
  │        ↓
  │       [跳过本 NFR]
  └─ 否 → [正常记录到 RESULT.md]
           ↓
          [迭代下一 NFR]
```

## 11. 性能与资源

### 11.1 性能目标

- 过滤逻辑耗时:< 10ms(通常 n < 20, m = 20,O(n × m) = 400 次字符串匹配,可接受)
- 总体影响:可忽略(步骤 7A / 8A 本身耗时 > 1s,过滤逻辑 < 10ms)

### 11.2 资源限制

- 内存:无额外内存消耗(过滤逻辑在原数组上操作)
- CPU:无额外 CPU 消耗(字符串匹配为轻量操作)

## 12. 测试要点

### 12.1 单元测试

- **过滤逻辑测试**:
  - 技术选型类问题被正确过滤
  - 功能/行为/结构类问题不被过滤
  - 边界情况:空问题列表、全部技术选型、全部功能类

- **NFR 过滤测试**:
  - 技术选型类 NFR 被正确标记 `defer-to-code-design`
  - 功能/性能/安全类 NFR 不被过滤
  - 边界情况:空 NFR 列表、全部技术选型、全部功能类

### 12.2 集成测试

- **端到端测试**:
  - 模拟用户提交含"技术选型"关键词的需求 → 验证步骤 7A 不弹出 AskUserQuestion
  - 模拟用户提交含"框架选型"关键词的需求 → 验证步骤 8A 不记录 NFR
  - 验证 clarifications.md 正确记录延迟问题

### 12.3 回归测试

- 验证 REQ-00033 的硬约束仍然生效(步骤 615)
- 验证步骤 1 / 5A / 8A 的其他功能不受影响
- 验证其他 7 个技能不受影响(code-design / code-plan / code-it / code-check / code-fix / code-init / code-rule)

## 13. 关联编码计划

- **任务清单**:`./assistants/V0.0.3/fix/BUG-00005/PLAN.md`(3 个任务)
- **里程碑**:M1-BUG-00005(3 任务全部开发=已完成 ∧ 测试=不适用)

## 14. 待澄清/未决项

无(用户已选择 --balanced 设计目标,修复方案已确定)。

## 15. 变更记录

| 时间 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- |
| 2026-06-22 15:00 | 详细设计完成 | 完成 BUG-00005 详细设计,3 个任务拆分,方案 B(步骤 7A + 8A 双重过滤) | wangmiao |
| 2026-06-23 | 评审完成 | code-check 单缺陷模式评审 BUG-00005 完成(14 维度,0 条"必须改"/1 条"建议改"/0 条"可选",F-001 — 关键词数量声称与字面不符留作 follow-up);`checkStateRollback` 推进 BUG-00005 状态 "已完成(详细设计)" → "已完成";`./assistants/V0.0.3/review/BUG-00005/REVIEW-REPORT.md` 主产出物;评审通过 | wangmiao |
