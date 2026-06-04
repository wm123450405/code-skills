# RESULT — REQ-00003-003(追加 module-conventions.md DEPRECATED 标记)

- 任务编码:`REQ-00003-003`
- 任务标题:追加 `module-conventions.md` DEPRECATED 标记
- 类型:修改(仅追加标记)
- 触发/来源:需求新增
- 来源 PLAN.md:`./assistants/V0.0.1/plan/REQ-00003/PLAN.md` §T-003
- 任务编码版本:v1
- 状态:**已完成**
- 责任人:wangmiao
- 开始时间:2026-06-04 10:55
- 完成时间:2026-06-04 10:55

---

## 1. 改修内容总览

在 `assistants/rules/module-conventions.md` 文件头部(原 frontmatter-like 引用块之后)插入 1 个 `> ⚠️ **DEPRECATED**` 引用块,引导用户使用替代文件 `directory-conventions.md`(由 T-002 创建)。

## 2. 涉及文件(1 个修改)

| 文件 | 改动 | 统计 |
| --- | --- | --- |
| `assistants/rules/module-conventions.md` | 头部追加 DEPRECATED 引用块 | +2 行(0 删除) |

## 3. 详细改动

### 变更位置

`assistants/rules/module-conventions.md` 行 7(在原 5 行 frontmatter-like 引用块之后,`## 适用场景` 之前)

### 变更内容

```markdown
> ⚠️ **DEPRECATED(已弃用)**:本文件内容已迁移到 `directory-conventions.md`(2026-06-04 REQ-00003 H2 决策,详见 `plan/REQ-00003/RESULT.md`)。本文件保留作为历史参考,新规则请追加到 `directory-conventions.md`。
```

### 变更原则

- 仅追加引用块,**不修改**任何现有内容
- **不删除**任何现有小节或规则
- 原 5 行 frontmatter + DEPRECATED 引用块 + `## 适用场景` 构成新的"前 8 行头部"

## 4. 关键决策与权衡

- **决策 D-IT-003-3-1**:DEPRECATED 引用块位置 — 头部 frontmatter 之后,`## 适用场景` 之前
  - **依据**:PLAN §T-003 "在原有 frontmatter-like 引用块之后,作为第二个引用块"
  - **影响**:视觉上"先看到维护声明,再看弃用警告"逻辑清晰
- **决策 D-IT-003-3-2**:措辞与 PLAN 略有微调(2 处)
  - **依据**:实际实施日期 + 可追溯性
  - **详见**:`deviations.md` 偏离 1

## 5. 偏离设计/规范的地方

**1 项**:DEPRECATED 引用块措辞与 PLAN 略有不同(日期修正 + 追加 plan RESULT.md 链接)
详见 `deviations.md`。

## 6. 验证结果

| 验证项 | 结果 |
| --- | --- |
| DEPRECATED 块位置(行 7,作为第 2 个引用块) | ✅ |
| DEPRECATED 块内容完整(弃用警告 + 替代文件 + 决策引用 + 引导) | ✅ |
| 原有 frontmatter(行 1-5)完整保留 | ✅ |
| `## 适用场景` 及后续内容完好 | ✅ |
| `git diff --stat` 2+/0- | ✅(纯追加) |
| INV-7 验证(仅追加,不删除) | ✅ |
| INV-5 验证(其他 12 个规范文件未修改) | ✅ |

详见 `compile-and-run.md` + `test-results.md`。

## 7. 已知问题/未完成项

- **无**。本任务按 PLAN §T-003 完整实施。
- **范围外事项**(留给 T-004~T-008):模板扩展 / CLAUDE.md 新小节 / 审计 / 看板。

## 8. 关联任务与提交

- 关联任务:`REQ-00003-002`(已完成的 directory-conventions.md 创建)+ T-001(关键词表引用)
- 下游任务:`REQ-00003-004`(模板扩展)
- 提交哈希:`695c029`

## 9. 提交计划

```bash
git add assistants/rules/module-conventions.md

git commit -m "chore(rules): deprecate module-conventions.md (REQ-00003 H2)

在 module-conventions.md 头部追加 DEPRECATED 引用块:
- 内容已迁移到 directory-conventions.md(2026-06-04 REQ-00003 H2 决策)
- 本文件保留作为历史参考
- 新规则请追加到 directory-conventions.md

INV-7: 仅追加, 不删除任何现有内容。
INV-5: 其他 12 个规范文件均未被修改。
"
```

## 10. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 |
| --- | --- | --- | --- |
| 2026-06-04 10:55 | v1 | 改修完成 | `module-conventions.md` 头部 +2 行 DEPRECATED 引用块;不删除任何内容(INV-7);不修改其他文件(INV-5) |
