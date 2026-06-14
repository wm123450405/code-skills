# 改修总结 — TASK-REQ-00025-00009

- 任务编码:TASK-REQ-00025-00009
- 标题:[修改] code-dashboard 算法 4 字面更新(双正则兼容)
- 需求:REQ-00025
- 所属版本:V0.0.3
- 类型:修改
- 触发/来源:详细设计
- 来源 PLAN.md:`./assistants/V0.0.3/plan/REQ-00025/PLAN.md` §3 任务详情 T-9
- 责任人:wangmiao
- 关联任务:—
- 开始时间:2026-06-08
- 完成时间:2026-06-08
- 提交哈希:`(见 git log)`

---

## 1. 任务信息

| 字段 | 值 |
| --- | --- |
| 任务编码 | TASK-REQ-00025-00009 |
| 标题 | [修改] code-dashboard 算法 4 字面更新(双正则兼容) |
| 需求 | REQ-00025 |
| 上游详细设计 | `./assistants/V0.0.3/plan/REQ-00025/RESULT.md` §4.9 / §5 算法 3 |
| 上游任务计划 | `./assistants/V0.0.3/plan/REQ-00025/PLAN.md` §3 任务详情 T-9 |
| 类型 | 修改(SKILL.md 字面更新) |
| 触发/来源 | 详细设计 |
| 实际产出 | SKILL.md 文档改造(纯文档,无代码) |

---

## 2. 改修内容总览

| 文件 | 状态 | 关键变更 |
| --- | --- | --- |
| `plugins/code-skills/skills/code-dashboard/SKILL.md` §附录 A | **修改**(净 +1 / -4 行) | 任务分支正则从 `^TASK-(REQ|BUG)-\d{5}-\d{5}$` 改为 `^TASK-(REQ|BUG)-[A-Za-z0-9.\-_]+-[A-Za-z0-9.\-_]+$`(双正则兼容,沿用 §规则 1 接收端);旧格式同步放宽;标题追加"本需求 REQ-00025 双正则兼容" |
| `plugins/code-skills/skills/code-dashboard/SKILL.md` §步骤 4 段 4 | **修改**(净 +1 / -1 行) | 算法 4 引用从 `buildSuggestions` 统一为 `parseTaskId` 描述(消除原标签冲突) |

---

## 3. 详细改动

### 3.1 §附录 A 任务编号解析(算法 4)(修改)

- **原**:
  ```
  parseTaskId(raw):
    // 新格式优先
    m = match(/^TASK-(REQ|BUG)-(\d{5})-(\d{5})$/, raw)
    if m:
      return { format: "new", type: m[1], parentNum: m[2], taskNum: m[3], displayId: raw }
    // 旧格式透传
    m = match(/^(REQ|BUG)-(\d{5})-(\d{5})$/, raw)
    ...
  ```
- **新**:
  ```
  parseTaskId(raw):
    // 宽松正则优先(沿用 encoding-conventions §规则 1 接收端,后缀自由)
    m = match(/^TASK-(REQ|BUG)-([A-Za-z0-9.\-_]+)-([A-Za-z0-9.\-_]+)$/, raw)
    if m:
      return { format: "new", type: m[1], parentNum: m[2], taskNum: m[3], displayId: raw }
    // 旧格式透传(同上游放宽)
    m = match(/^(REQ|BUG)-([A-Za-z0-9.\-_]+)-([A-Za-z0-9.\-_]+)$/, raw)
    ...
  ```

### 3.2 §步骤 4 段 4 算法 4 引用(修改)

- **原**:`**算法 4**:\`buildSuggestions(items, allTasks): Suggestion[]\`(沿用 plan/REQ-00023/RESULT.md §4.4)`
- **新**:`**算法 4**:\`parseTaskId(raw): {format, type, parentNum, taskNum, displayId} | null\`(双正则兼容,新规则 REQ-00025;详 §附录 A)`

---

## 4. 关键决策与权衡

### 4.1 为什么 §附录 A 标题追加"本需求 REQ-00025 双正则兼容"?

- 算法 4 的"双正则兼容"是本需求 REQ-00025 的核心软化点(沿用 AC-7 锁定)
- 标题追加让后续维护者一眼识别"这是软化后的版本",避免误以为是默认 5 位纯数字版

### 4.2 为什么 §步骤 4 段 4 算法 4 引用对齐到 `parseTaskId`?

- 原 SKILL.md §步骤 4 段 4 末尾把"算法 4"标注为 `buildSuggestions`,而 §附录 A 标注"算法 4 = `parseTaskId`"——存在标签冲突
- 本任务以 §附录 A 为权威源(算法 4 = `parseTaskId`),统一 §步骤 4 段 4 的引用描述
- 0 触及段 4 的"5 类状态映射" / "核心规则"等核心逻辑(均为算法 3 `buildSuggestions` 的实际职责)

### 4.3 为什么不修改 §步骤 5 (下一步建议生成) 的 `TASK-REQ-NNNNN-NNNNN` 字面?

- §步骤 5 中的 `TASK-REQ-NNNNN-NNNNN` / `REQ-NNNNN-NNNNN` 是"建议命令模板"(展示给用户的命令字面)
- 模板沿用"默认 5 位纯数字"格式(展示典型用法),**不**强制格式(实际正则匹配由 §附录 A `parseTaskId` 处理)
- 0 修改以保持"建议命令"的可读性(用户看到的是规范格式,而非"接收端放宽"格式)

---

## 5. 偏离设计 / 规范

**0 偏离**。详见 `deviations.md`。

注:§步骤 4 段 4 末尾的算法 4 引用描述做了"轻量语义对齐"(消除原 `buildSuggestions` / `parseTaskId` 标签冲突),**不**触及段 4 的核心逻辑。

---

## 6. 验证结果

### 6.1 编译验证
- **不适用**

### 6.2 启动验证
- **不适用**

### 6.3 测试验证
- **不适用**(本仓库 0 测试框架)
- 详见 `test-results.md`

### 6.4 静态校验

- ✅ frontmatter L1-3 **未**改(NFR-7)
- ✅ §附录 A 函数体结构(`if m: return {...} / return null`)**未**改
- ✅ §步骤 4 段 4 的"5 类状态映射" / "核心规则"等其他行**未**改
- ✅ §步骤 5(算法 3 `buildSuggestions` / 建议命令模板)**未**改
- ✅ §步骤 3 / §边界与异常 / §衔接 / §不要做的事 等既有小节锚点全部保留
- ✅ 0 引入新依赖

---

## 7. 已知问题 / 未完成项

**0**。本任务为一次性完成。

---

## 8. 关联任务与提交

| 提交哈希 | 时间 | 提交说明 | 本任务涉及文件 |
| --- | --- | --- | --- |
| `(本任务 commit)` | 2026-06-08 | `chore(code-it): REQ-00025 — T-9 code-dashboard 算法 4 字面更新(双正则兼容)` | `plugins/code-skills/skills/code-dashboard/SKILL.md` |

---

## 9. 任务档案同步清单

- [x] `RESULT.md`(本文件)
- [x] `work-log.md`
- [x] `compile-and-run.md`
- [x] `deviations.md`
- [x] `test-results.md`
- [x] `assistants/V0.0.3/plan/REQ-00025/PLAN.md` 中本任务状态(由 `code-it` 步骤 14 推进)
- [x] `assistants/V0.0.3/RESULT.md` 看板"任务清单"行(由 `code-it` 步骤 15 推进)
- [x] `assistants/V0.0.3/RESULT.md` 看板"变更记录"追加任务完成条目(由 `code-it` 步骤 15 追加)
