# 数据结构完整变更 — REQ-00008
更新时间:2026-06-05 16:00
版本:V0.0.2
需求编码:REQ-00008

> 本需求**不**修改任何数据库表 / ORM 模型 / 数据迁移脚本;主数据结构 = 聚合文件 `REVIEW.md` + 派生任务追加行(在 `PLAN.md` 中)。
>
> 全部数据结构都是**纯文本 / Markdown**,无 schema 变更、无类型校验、无索引、无外键。

---

## 新增数据结构 1:聚合文件 `REVIEW.md`(5 章节,本设计新增)

### 路径
- `./assistants/<版本号>/REVIEW.md`(版本顶层,与 `RESULT.md` 同级)
- **不**在 `review/` 子目录(NFR-6 强约束)
- **不**在 `code-review/templates/` 新增对应模板(D-1.B 决定)

### 字段

| 字段 | 类型(字符级) | 约束 | 说明 |
| --- | --- | --- | --- |
| 文件标题 | 字符串 | `# 整版本代码审查报告 — <版本号>` | 固定模板 |
| 文档头引用 | Markdown 引用 | 引用本文件 + 单需求文件路径 | 固定模板 |
| 评审时间 | YYYY-MM-DD HH:mm | 当前时间 | 由 `code-review` 写入时生成 |
| 评审范围 | REQ-NNNNN 列表 | 筛"已完成"的需求 | 由 §2.1 算法输出 |
| 评审人 | 字符串 | 固定 `"AI(code-review 技能)"` | 固定模板 |
| 发现总数 | 整数 | K + L + O(必须改 + 建议改 + 可选) | 由各需求 REVIEW-REPORT 累加 |
| 必须改 | 整数 | K | 同上 |
| 建议改 | 整数 | L | 同上 |
| 可选 | 整数 | O | 同上 |

### 5 章节结构

```markdown
# 整版本代码审查报告 — <版本号>

> 本文件由 `/code-review`(整版本模式)生成,聚合本版本所有"已完成"需求的评审发现。
> 单需求详情见 `./review/REQ-NNNNN/REVIEW-REPORT.md`。

## 1. 评审概览
- 评审时间:<YYYY-MM-DD HH:mm>
- 评审范围:本版本的 N 个"已完成"需求(REQ-NNNNN, ...)
- 评审人:AI(code-review 技能)
- 发现总数:M
  - 必须改:K
  - 建议改:L
  - 可选:O

## 2. 各需求评审摘要

### REQ-NNNNN <需求标题>
- 单需求 REVIEW-REPORT:./review/REQ-NNNNN/REVIEW-REPORT.md
- 发现:K(必须改) + L(建议改) + O(可选)
- 派生任务:K'(已写入对应 PLAN.md)

## 3. 评审发现汇总(去重)

| 评审 ID | 需求 | 维度 | 级别 | 描述 | 派生改修任务 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| F-1 | REQ-NNNNN | 一致性 | 必须改 | <...> | TASK-REQ-NNNNN-NNNNN | 已派生 |
| ... |

**去重规则**:跨需求的相同发现(`(需求编码, 描述前 50 字)` 一致)**不**重复列(NFR-7)

## 4. 派生任务汇总

| 派生任务 | 关联原任务 | 派生时间 | review 来源 | 状态 |
| --- | --- | --- | --- | --- |
| TASK-REQ-NNNNN-NNNNN | REQ-NNNNN-NNNNN | YYYY-MM-DD HH:mm | REVIEW-REPORT.md | 待开始 |
| ... |

**唯一性规则**:同发现**不**重复追加(NFR-8)

## 5. 评审人/AI 备注
(预留)
```

### 关系
- 与 N 个 `review/REQ-NNNNN/REVIEW-REPORT.md` 关联(单向引用,字符串级)
- 与各需求 `plan/REQ-NNNNN/PLAN.md` 派生任务行关联(由 §4 派生任务汇总引用)

### 存储选型
**纯 Markdown 文件**(无 DB,无 schema)

### 迁移脚本
**N/A**(本需求不涉及数据库迁移)

### 依据规范
- NFR-6 强约束(版本顶层,与 `RESULT.md` 同级)
- NFR-7 实现(去重键 `(需求编码, 描述前 50 字)`)
- INV-7 强约束(版本顶层)

---

## 修改数据结构 1:既有 `review/REQ-NNNNN/REVIEW-REPORT.md` — **不修改字节级**

### 路径
- `./assistants/<版本号>/review/REQ-NNNNN/REVIEW-REPORT.md`(既有,本设计**覆盖写入**但**不修改模板字面**)

### 字段(沿用既有 8 章节结构)
- 评审信息 / 评审清单 / 任务评审结果 / 发现汇总 / 派生的新任务列表 / 未派生任务的发现 / 超出本次评审范围的发现 / 整体结论

### 字段级变更
**无**。整版本模式**完全复用**模式 1 既有模板(`templates/REVIEW-REPORT.md`)。
- 字节级字面 100% 一致(FR-6.AC-6.1 + INV-2)
- 模板文件 `plugins/code-skills/skills/code-review/templates/REVIEW-REPORT.md` **字节级不变**(INV-13)

### 写入策略
- `Write` 工具(覆盖,非 `Edit`)
- 多次执行整版本模式**幂等**(NFR-3 + INV-8)
- 模式 1 与模式 2 互覆盖(NFR-6 允许)

### 依据规范
- FR-3.AC-3.1(单需求文件与模式 1 完全一致)
- FR-6.AC-6.1(整版本模式生成的 `REVIEW-REPORT.md` 内容与模式 1 完全相同)
- INV-2(完全复用)

---

## 修改数据结构 2:既有 `plan/REQ-NNNNN/PLAN.md` "任务总览" 表 — **追加行,不修改既有**

### 路径
- `./assistants/<版本号>/plan/REQ-NNNNN/PLAN.md`(既有)

### 字段(沿用模式 1 既有"任务总览"表)

每行字段(沿用既有):
```
| 任务编号 | 需求 | 类型 | 触发/来源 | 标题 | 开发状态 | 测试状态 | 涉及文件 | 完成时间 | 提交哈希 | 关联任务 |
| TASK-REQ-NNNNN-NNNNN | REQ-NNNNN | 修改 | 审查改修 | 修复 F-X(必须改) | 待开始 | 未编写 | ... | ... | ... | REQ-NNNNN-NNNNN |
```

### 字段级变更
**不修改既有任务行**;只在表的最末行**追加**新行(派生任务)
- 派生任务**不**自己生成 TASK 编码(沿用 `code-plan` 既有规则 — `encoding-conventions §规则 4`)
- 派生任务字段 100% 沿用模式 1 既有(INV-3)
- 同 `(需求编码, 描述前 50 字)` 已存在 → **不**重复追加(NFR-8)

### 写入策略
- `Edit` 工具(追加,不覆盖)
- 严格按"任务总览"表最后一行后追加(沿用模式 1 既有锚点)

### 依据规范
- FR-5.AC-5.1(派生任务 `触发/来源=审查改修`, `关联任务=被修正原任务`)
- FR-5.AC-5.2(编码生成沿用 `code-plan`)
- FR-5.AC-5.3(PLAN.md "任务总览" 追加)
- NFR-8(派生任务唯一性)
- INV-3(完全沿用模式 1 既有)

---

## 修改数据结构 3:既有 `review/<新TASK>/RESULT.md` — **新增文件,沿用模板**

### 路径
- `./assistants/<版本号>/review/<新TASK>/RESULT.md`(新增)

### 字段(沿用模式 1 既有"派生改修要求"模板)
- 任务信息 / 问题清单 / 应当改修的文件清单 / 不需要做的 / 验证手段 / 关联依据汇总 / 完成定义(DoD)/ 变更记录

### 字段级变更
**无**。完全沿用模式 1 既有模板(`templates/REVIEW-FIX.md`)。
- 模板文件 `plugins/code-skills/skills/code-review/templates/REVIEW-FIX.md` **字节级不变**(INV-13)

### 写入策略
- `Write` 工具(新建)
- 由 `code-it` 消费(给 `code-it` 直接消费的工作输入)

### 依据规范
- FR-5 全节(派生任务字段一致)
- `code-it` 步骤 1 解析"触发/来源=审查改修"时**只读**此文件作为本任务的全部输入

---

## 不修改的数据结构

- `.claude-plugin/marketplace.json` — 字节级不变
- `plugins/code-skills/.claude-plugin/plugin.json` — 字节级不变
- 其他 9 个 `code-*/SKILL.md` — 字节级不变
- `assistants/rules/` 下 13 个规范文件 — 字节级不变
- `plugins/code-skills/README.md` / `README.en.md` — 字节级不变(Q-7 采纳默认)
- `plugins/code-skills/CLAUDE.md` — 字节级不变(Q-7 采纳默认)
- `code-review/templates/{REVIEW-REPORT,REVIEW-FIX,assistants-layout}.md` — 字节级不变(INV-13)
- `code-review/checklists/review-checklist.md` — 字节级不变(INV-13)
- `code-review/SKILL.md` frontmatter(L1-3)— 字节级不变(INV-4)
- `code-review/SKILL.md` 既有步骤 0-15 字面 — 字节级不变(INV-1/11/12)
- `assistants/V0.0.2/RESULT.md` — 字节级不变(整版本模式**不**触发额外看板区段;模式 1 既有同步逻辑覆盖)

---

## 数据结构自检结论

- ✅ 0 新增数据库表 / ORM / schema
- ✅ 0 新增索引 / 外键
- ✅ 0 数据迁移脚本
- ✅ 4 个数据结构变更(1 新增 + 3 修改,均为文本文件)
- ✅ 13 项 INV 全部满足(INV-1 ~ INV-13)
- ✅ 100% 沿用既有 4 模板
