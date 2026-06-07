# 编码计划 — BUG-00001

> 本文件由 `code-plan BUG-00001` 在 2026-06-07 产出。结构与需求路径 PLAN.md 完全同构(8 章节),仅任务编号 / 需求列 / 关联任务列不同。

- 缺陷编号:BUG-00001
- 计划标题:修复职责分离 — 6 个 SKILL.md 加硬约束(`code-it` 唯一可改 SKILL.md)
- 状态:待 code-it 实施
- 所属版本:V0.0.3
- 整体设计目标:`--balanced`(默认粒度)
- 维度优先级:可维护性=高;封装性/可读性=不适用(自然语言);功能性/扩展性/健壮性=中;可复用性=低

---

## 1. 计划概述

本计划按 5 个独立任务实施 BUG-00001 的修复方案:在 6 个 `code-skills` 插件自身的 SKILL.md 文档中追加"职责边界"硬约束,固化"`code-it` 是唯一可改 SKILL.md 的技能"。

**任务粒度依据**(沿用 `code-plan` §步骤 10A):
- 整体=`--balanced` → 默认 1 任务 = 1 个 SKILL.md 段追加
- 可维护性=高 → 任务标题精化(每任务只改 1 段),涉及文件用语义化锚点(`§不要做的事` 段 / `§目标` 段)
- 封装性/可读性=不适用 → 不抽公共子节,各 SKILL.md 独立追加

**触发/来源**:全部任务 = `缺陷修复`(沿用既有 13 枚举之一,**不**新增)

**任务总数**:5(纯文档型,测试状态=不适用;0 派生"更新看板"任务,沿用 REQ-00017 强约束)

---

## 2. 任务总览

| 任务编号 | 需求 | 类型 | 触发/来源 | 标题 | 开发状态 | 测试状态 | 涉及文件 | 关联任务 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TASK-BUG-00001-00001 | BUG-00001 | 修改 | 缺陷修复 | [修改] code-require 加"不修改 SKILL.md"硬约束 | 待开始 | 不适用 | plugins/code-skills/skills/code-require/SKILL.md §不要做的事 | BUG-00001 |
| TASK-BUG-00001-00002 | BUG-00001 | 修改 | 缺陷修复 | [修改] code-design 加"不修改 SKILL.md"硬约束 | 待开始 | 不适用 | plugins/code-skills/skills/code-design/SKILL.md §不要做的事 | BUG-00001 |
| TASK-BUG-00001-00003 | BUG-00001 | 修改 | 缺陷修复 | [修改] code-plan 加"不修改 SKILL.md"硬约束 | 待开始 | 不适用 | plugins/code-skills/skills/code-plan/SKILL.md §不要做的事 | BUG-00001 |
| TASK-BUG-00001-00004 | BUG-00001 | 修改 | 缺陷修复 | [修改] code-fix 加"不修改 SKILL.md"硬约束 | 待开始 | 不适用 | plugins/code-skills/skills/code-fix/SKILL.md §不要做的事 | BUG-00001 |
| TASK-BUG-00001-00005 | BUG-00001 | 修改 | 缺陷修复 | [修改] code-it 加"唯一可改"声明 + code-unit 加"可改测试代码"边界 | 待开始 | 不适用 | plugins/code-skills/skills/code-it/SKILL.md §目标 段后 + plugins/code-skills/skills/code-unit/SKILL.md §目标 段后 | BUG-00001 |

**统计**:
- 总任务数:5
- 真正可发布数(开发=已完成 ∧ 测试∈{已运行-通过, 不适用}):0
- 开发已完成 / 未完成:0 / 5
- 测试已通过 / 不适用 / 未编写:0 / 5 / 0
- 任务颗粒度(每个任务的"实际产出"):5 段 SKILL.md 文本追加(候选集 = `{文档改写}`,符合 REQ-00017 强约束)
- 0 派生"更新看板"任务(沿用 REQ-00017)

---

## 3. 任务详情

### 3.1 TASK-BUG-00001-00001 · [修改] code-require 加"不修改 SKILL.md"硬约束

- **目标**:在 `code-require/SKILL.md` 的 `## 不要做的事` 段**最前面**追加 1 条,内容为"不修改 `plugins/code-skills/skills/*/SKILL.md` 任何文件(工程代码改动由 `code-it` 实施,本技能只写 `require/<REQ>/RESULT.md` 等工作空间文档)"
- **涉及文件**:`plugins/code-skills/skills/code-require/SKILL.md > §不要做的事(段首插入)`
- **关键变更**:
  - 目标位置:`## 不要做的事` 段,NFR-7 的"不调用 Write/Edit"条目**之前**
  - 已有结构保留:段标题 + 现有 5-7 条"不要做的事"全部不动
  - 新增内容:约 80 字符(详见 `RESULT.md §7.4.1`)
- **边界与异常**:
  - 若 `## 不要做的事` 段不存在 → 通过 `code-fix BUG-00001` 走派生任务(不直接重建)
  - 若 frontmatter 区域被误改 → 通过 `INV-16` 静态校验失败回滚
- **验证手段**:`grep -n "不修改.*SKILL.md" plugins/code-skills/skills/code-require/SKILL.md` 命中 ≥ 1 行(INV-10)
- **回退方式**:`git checkout HEAD~1 -- plugins/code-skills/skills/code-require/SKILL.md`(单文件回退)

### 3.2 TASK-BUG-00001-00002 · [修改] code-design 加"不修改 SKILL.md"硬约束

- **目标**:在 `code-design/SKILL.md` 的 `## 不要做的事` 段**最前面**追加 1 条
- **涉及文件**:`plugins/code-skills/skills/code-design/SKILL.md > §不要做的事(段首插入)`
- **关键变更**:类似 3.1,文案为"本技能只写 `design/<REQ>/RESULT.md` 等工作空间文档"
- **验证手段**:`grep -n "不修改.*SKILL.md" plugins/code-skills/skills/code-design/SKILL.md` 命中 ≥ 1 行(INV-11)
- **回退方式**:单文件 git checkout

### 3.3 TASK-BUG-00001-00003 · [修改] code-plan 加"不修改 SKILL.md"硬约束

- **目标**:在 `code-plan/SKILL.md` 的 `## 不要做的事` 段**最前面**追加 1 条
- **涉及文件**:`plugins/code-skills/skills/code-plan/SKILL.md > §不要做的事(段首插入)`
- **关键变更**:类似 3.1,文案为"本技能只写 `plan/<REQ>/RESULT.md` / `PLAN.md` 等工作空间文档"
- **验证手段**:`grep -n "不修改.*SKILL.md" plugins/code-skills/skills/code-plan/SKILL.md` 命中 ≥ 1 行(INV-12)
- **回退方式**:单文件 git checkout

### 3.4 TASK-BUG-00001-00004 · [修改] code-fix 加"不修改 SKILL.md"硬约束

- **目标**:在 `code-fix/SKILL.md` 的 `## 不要做的事` 段**最前面**追加 1 条
- **涉及文件**:`plugins/code-skills/skills/code-fix/SKILL.md > §不要做的事(段首插入)`
- **关键变更**:类似 3.1,文案为"本技能只写 `fix/<BUG-NNN>/RESULT.md` 等工作空间文档"
- **验证手段**:`grep -n "不修改.*SKILL.md" plugins/code-skills/skills/code-fix/SKILL.md` 命中 ≥ 1 行(INV-13)
- **回退方式**:单文件 git checkout

### 3.5 TASK-BUG-00001-00005 · [修改] code-it 加"唯一可改"声明 + code-unit 加"可改测试代码"边界

- **目标**(合并 2 段追加,因 2 段声明极短):
  1. 在 `code-it/SKILL.md` 的 `## 目标` 段后**新增** `## 唯一允许的生产代码改动场景` 小节(约 150 字符)
  2. 在 `code-unit/SKILL.md` 的 `## 目标` 段后**新增** `## 可改测试代码边界` 小节(约 130 字符)
- **涉及文件**(2 个):
  - `plugins/code-skills/skills/code-it/SKILL.md > §目标 段后(新增小节)`
  - `plugins/code-skills/skills/code-unit/SKILL.md > §目标 段后(新增小节)`
- **关键变更**(2 处):
  - code-it:声明"本技能是唯一被允许修改 `plugins/code-skills/skills/*/SKILL.md` 的技能"
  - code-unit:声明"本技能被允许仅修改 CWD 下的测试文件,不得修改生产代码"
- **边界与异常**:
  - 若 `## 目标` 段缺失 → 通过 `code-fix BUG-00001` 走派生任务
  - 合并 2 个文件改动,因 2 段声明均依赖"反向引用"(code-it 声明 = 4 个技能不得改 + code-unit 不得改;code-unit 声明 = code-it 唯一实施),分开任务会失去语义连贯性
- **验证手段**:
  - `grep -n "唯一.*生产代码改动" plugins/code-skills/skills/code-it/SKILL.md` 命中 ≥ 1 行(INV-14)
  - `grep -n "可改测试代码" plugins/code-skills/skills/code-unit/SKILL.md` 命中 ≥ 1 行(INV-15)
- **回退方式**:`git checkout HEAD~1 -- plugins/code-skills/skills/{code-it,code-unit}/SKILL.md`(2 文件回退)

---

## 4. 任务依赖图

```
        [T-1: code-require] ─┐
        [T-2: code-design]  ─┤
        [T-3: code-plan]    ─┼─→ [T-5: code-it + code-unit 声明]
        [T-4: code-fix]     ─┘                ↑
                                              │
                  (反向引用,无强依赖,5 任务可并行)
```

- **Mermaid 源**:
  ```mermaid
  graph LR
    T1[T-1: code-require] --> T5[T-5: code-it+code-unit]
    T2[T-2: code-design] --> T5
    T3[T-3: code-plan] --> T5
    T4[T-4: code-fix] --> T5
  ```
- **说明**:T-1 ~ T-4 之间**无**强依赖(各自追加独立段落),T-5 引用 T-1 ~ T-4 的新约束("code-require 等不得改 SKILL.md"),故 T-5 在 T-1 ~ T-4 完成后**语义最优**;但实际不阻塞 — 即使 T-1 ~ T-4 未实施,T-5 仍可独立追加(只引用既有命名约定)
- **实施建议**:code-it 可一次提交 5 任务(无强文件冲突);若分 2 轮实施,推荐"先 T-1~T-4 一次提交,再 T-5 一次提交"

---

## 5. 里程碑

- **M-BUG-00001**:BUG-00001 全部 5 任务
  - 完成定义:5 任务开发状态=已完成 ∧ 测试状态=不适用 ∧ INV-10~16 全部通过 ∧ 回归校验(e69a58a 等 4 commit 保留)通过
  - 状态:待开始 → 进行中(随 code-it 推进)→ 已完成
  - 计划时间:2026-06-07
  - 实际完成:—

---

## 6. 状态管理规则

- **双状态字段**(每任务):开发状态 + 测试状态
- **本计划初始化**:
  - 5 任务开发状态=`待开始`(初值)
  - 5 任务测试状态=`不适用`(纯文档任务,无运行时影响,无测试框架)
- **测试状态推进路径**:纯文档型任务**不**会推到"已运行-通过",**只**有 1 种终态 = `不适用`
- **真正可发布判定**:开发状态=已完成 ∧ 测试状态=不适用(本计划所有任务满足此条件即视为"真正可发布")

---

## 7. 关联计划

| 关联项 | 路径 | 关联方式 |
| --- | --- | --- |
| 缺陷详情 | `./fix/BUG-00001/RESULT.md` | 本计划的上游(本需求 REQ-00019 起 BUG 路径不生成 `fix-plan.md`,沿用 RESULT.md 14 章节) |
| 详细设计 | `./fix/BUG-00001/RESULT.md §7` | 本计划的设计依据(§7.4 模块详细化) |
| 7 份过程文档 | `./fix/BUG-00001/{materials-index,module-details,interface-specs,data-changes,risk-analysis,rule-compliance,design-notes}.md` | 本计划的辅助文档 |
| V0.0.3 看板 | `./RESULT.md §缺陷清单` | 本计划完成后由 code-check 同步 BUG-00001 状态 |
| V0.0.3 看板"任务清单" | `./RESULT.md §任务清单` | 本计划 5 任务在 code-plan 阶段已追加(沿用 §步骤 28A+1 12 列字段) |
| 规范依据 | `./assistants/rules/{skill-conventions,encoding-conventions,dashboard-conventions}.md` | 强约束来源 |

---

## 8. 变更记录

| 时间 | 变更类型 | 变更摘要 | 关联项 |
| --- | --- | --- | --- |
| 2026-06-07 | 计划完成 | code-plan 完成 BUG-00001 详细设计 + 5 任务拆分(整体=--balanced, 可维护性=高, 封装性/可读性=不适用);产出 9 份文档(RESULT.md / PLAN.md / 7 份过程文档);5 任务开发状态=待开始,测试状态=不适用;触发/来源=缺陷修复 | BUG-00001 |
