# 编码计划 — REQ-00003(优化 `code-rule` 技能,增加不同类型的核心编码规范的解析或引导)

- 需求编码:REQ-00003
- 所属版本:V0.0.1
- 计划版本:v1
- 状态:已完成(7/7 全部完成,待最终 commit)
- 责任人:wangmiao
- 创建:2026-06-03
- 最近更新:2024-06-04 11:00
- **上游详细设计**:`./assistants/V0.0.1/plan/REQ-00003/RESULT.md`(v1,已完成)
- **下游**:`code-it REQ-00003-NNN` 实施;`code-unit` 验证
- **任务总数**:7 / **commit 总数**:6

---

## 1. 任务总览

| 任务编号 | 类型 | 触发/来源 | 标题 | 开发状态 | 测试状态 | 涉及文件 | 关联任务 | commit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `REQ-00003-001` | 修改 | 需求新增 | 扩展 `code-rule/SKILL.md` 正文(类型识别 + Type A/B/C 文档化 + 工作目录约定) | 已完成 | 不适用 | `plugins/code-skills/skills/code-rule/SKILL.md` | 2026-06-04 10:26 | 086890d | T-002, T-003, T-005 |
| `REQ-00003-002` | 新增 | 需求新增 | 创建 6 个新分类占位文件(C-1~C-6) | 已完成 | 不适用 | `assistants/rules/framework-conventions.md`, `dependency-conventions.md`, `naming-conventions.md`, `directory-conventions.md`, `coding-style.md`, `commit-conventions.md` | 2026-06-04 10:53 | bec5f13 | T-001 | commit 2 |
| `REQ-00003-003` | 修改 | 需求新增 | 追加 `module-conventions.md` DEPRECATED 标记 | 已完成 | 不适用 | `assistants/rules/module-conventions.md` | 2026-06-04 10:55 | 695c029 | T-002 | commit 3 |
| `REQ-00003-004` | 修改 | 需求新增 | 扩展 `templates/rule.md`(占位 + 引导模式) | 已完成 | 不适用 | `plugins/code-skills/skills/code-rule/templates/rule.md` | 2026-06-04 10:55 | 2f41bb0 | T-001 | commit 4 |
| `REQ-00003-005` | 修改 | 需求新增 | 追加 `CLAUDE.md` "## AI 工作约定"小节(首次) | 已完成 | 不适用 | `plugins/code-skills/CLAUDE.md` | 2026-06-04 10:55 | 35bc26b | T-001 | commit 5 |
| `REQ-00003-006` | 文档 | 需求新增 | 同步版本看板 + 更新 `plan/REQ-00003/PLAN.md` 状态 | 已完成 | 不适用 | `assistants/V0.0.1/RESULT.md`, `assistants/V0.0.1/plan/REQ-00003/PLAN.md` | 2024-06-04 11:00 | ded7613 | T-001 ~ T-005 | (并入 commit 1-5) |
| `REQ-00003-007` | 文档 | 需求新增 | 全仓库 Grep + 不变量自检 + 6 commit 整理 | 已完成 | 不适用 | 无文件修改,产出 `code/REQ-00003-007/{RESULT,work-log,deviations,compile-and-run}.md` | 2024-06-04 10:55 | (无 commit) | T-001 ~ T-006 | commit 6 |

**统计**:
- 总任务数:7
- 代码类(新增/修改):5(T-001~005)
- 文档类:2(T-006, T-007)
- 测试类:0
- 测试状态=不适用:7 / 7(INV-10:全部为文档/规范/Markdown 处理)

---

## 2. 任务详情

### 任务 `REQ-00003-001`:扩展 `code-rule/SKILL.md` 正文

- **目标**:把 `code-rule/SKILL.md` 从"只支持 Type A 流程"扩展为"支持 Type A/B/C 3 种目标类型"
- **类型**:修改(扩展正文,不改 frontmatter)
- **触发/来源**:需求新增
- **涉及文件**:`plugins/code-skills/skills/code-rule/SKILL.md`
- **关键变更**:
  1. **L32-44 工作目录约定**:从 11 个旧文件名 → 11 个新分类文件名(4 保留 + 1 弃用 + 6 新建)
  2. **L117-128 步骤 4**:从"拆分 + 初步归类"扩展为"4.1 拆分 + 4.2 类型识别 + 4.3 初步归类"3 段
  3. **L117-128 步骤 4 子段 4.3 关键词表**:从 11 个旧分类 → 6 核心 + 5 保留专项
  4. **新增小节"Type B 子流程(AI 工作指引追加)"**:含触发识别 + 数据结构(5 字段)+ 插入算法
  5. **新增小节"Type C 子流程(模板内容提示追加)"**:含触发识别 + 数据结构(4 字段)+ 插入算法(末尾/内联)
  6. **新增"## 占位模式 / ## 引导模式"说明**:含触发条件 + 算法 + 用户选择分支
- **边界与异常**:
  - frontmatter(行 1-3)`name` + `description` **一字不动**(INV-5, `skill-conventions.md` §规则 1)
  - 现有 9 步骤主流程字段不变(FR-8, INV-1)
  - 关键词表扩展时,**保留旧关键词向后兼容**(design D-DESIGN-1)
- **验证手段**:
  - `Read SKILL.md` 确认 frontmatter 未变
  - `Grep "## Type A 子流程"` 等小节存在
  - 估算文档行数:272 → 380(约 +40%)
- **回退方式**:`git revert <commit>`
- **依赖**:无
- **关联任务**:T-002, T-003, T-005
- **commit**:commit 1(与 T-006 看板同步合并)

### 任务 `REQ-00003-002`:创建 6 个新分类占位文件

- **目标**:在 `./assistants/rules/` 下创建 6 个新分类文件的空占位骨架
- **类型**:新增
- **触发/来源**:需求新增
- **涉及文件**(6 个):
  - `assistants/rules/framework-conventions.md`(C-1,条件性)
  - `assistants/rules/dependency-conventions.md`(C-2,条件性)
  - `assistants/rules/naming-conventions.md`(C-3,默认)
  - `assistants/rules/directory-conventions.md`(C-4,默认)
  - `assistants/rules/coding-style.md`(C-5,默认)
  - `assistants/rules/commit-conventions.md`(C-6,条件性)
- **关键变更**:每个文件用 `Write` 工具创建,内容为详细设计 §3.3.5 的骨架模板
- **边界与异常**:
  - 文件内容**仅含骨架**,无预填规则(INV-2, design Q-5=H1)
  - 不修改任何现有规范文件
  - 文件命名严格按 §3.3.4 分类映射表
- **验证手段**:
  - `Bash ls assistants/rules/` 确认 6 个新文件存在
  - `Read <file>` 确认每个文件仅含分类标题 + 维护声明 + 1 个 "## 规则 1: (待添加)" 占位
- **回退方式**:`git revert <commit>` 撤回 6 个新文件
- **依赖**:无
- **关联任务**:T-001(步骤 4 关键词表引用这 6 个文件名)
- **commit**:commit 2

### 任务 `REQ-00003-003`:追加 `module-conventions.md` DEPRECATED 标记

- **目标**:在 `module-conventions.md` 文件头部追加 DEPRECATED 标记,引导用户使用新文件 `directory-conventions.md`
- **类型**:修改(仅追加标记)
- **触发/来源**:需求新增
- **涉及文件**:`assistants/rules/module-conventions.md`
- **关键变更**:
  - 在文件头部添加引用块(在原有 frontmatter-like 引用块之后,作为第二个引用块):
    ```markdown
    > ⚠️ **DEPRECATED(已弃用)**:本文件内容已迁移到 `directory-conventions.md`(2026-06-03 REQ-00003 H2 决策)。本文件保留作为历史参考,新规则请追加到 `directory-conventions.md`。
    ```
  - **不删除**任何现有内容
  - **不修改**任何现有小节
- **边界与异常**:
  - 仅追加,不删除(INV-7, design Q-8=H2)
  - 不破坏现有 frontmatter
- **验证手段**:
  - `Read module-conventions.md` 确认头部有 DEPRECATED 标记
  - `git diff module-conventions.md` 仅显示 DEPRECATED 段
  - 原有内容(规则 1, 2, 3 等)完好
- **回退方式**:`git revert <commit>` 撤回 DEPRECATED 标记
- **依赖**:无
- **关联任务**:T-002(6 个新文件中 `directory-conventions.md` 替代 `module-conventions.md`)
- **commit**:commit 3

### 任务 `REQ-00003-004`:扩展 `templates/rule.md`(占位 + 引导模式)

- **目标**:在 `code-rule/templates/rule.md` 头部追加"占位模式"和"引导模式"的说明,让 `code-rule` 在创建空占位或引导用户填示例时有模板依据
- **类型**:修改(扩展,不改 8 字段结构)
- **触发/来源**:需求新增
- **涉及文件**:`plugins/code-skills/skills/code-rule/templates/rule.md`
- **关键变更**:
  - 在文件头部添加"## 占位模式(本文件可作为空占位使用)"小节,说明:
    - 若用户选择"未来占位"模式,可省略"规则 1"及之后小节
    - 仅保留:分类标题 + "本规范由 code-rule 维护"声明 + 1 个"## 规则 1: (待添加)"空小节
  - 在文件头部添加"## 引导模式(本文件可作为引导模板使用)"小节,说明:
    - 若用户选择"引导模式"(默认分类首次添加),可提示用户填 1-2 条示例规则
    - 引导模式与占位模式互斥(用户二选一)
- **边界与异常**:
  - **不修改**原 8 字段规则小节(FR-8, INV-1)
  - **不删除**任何现有内容
- **验证手段**:
  - `Read templates/rule.md` 确认头部新模式说明存在
  - `git diff templates/rule.md` 仅显示头部扩展段
  - 原 8 字段结构(分类/规则简称/强制级别/适用范围/条款/正反示例/例外/关联规范/来源)完好
- **回退方式**:`git revert <commit>` 撤回扩展
- **依赖**:T-001(SKILL.md 中的"占位模式"逻辑依赖此模板)
- **关联任务**:T-001
- **commit**:commit 4

### 任务 `REQ-00003-005`:追加 `CLAUDE.md` "## AI 工作约定"小节(首次)

- **目标**:在 `plugins/code-skills/CLAUDE.md` 末尾追加"## AI 工作约定(由 code-rule 维护)"小节,作为 Type B 写入位置
- **类型**:修改(末尾追加)
- **触发/来源**:需求新增
- **涉及文件**:`plugins/code-skills/CLAUDE.md`
- **关键变更**:
  - 在文件末尾追加:
    ```markdown

    ## AI 工作约定(由 code-rule 维护)

    > 本小节由 `code-rule` 技能维护;手动修改可能被 `code-rule` 覆盖。
    > 适用对象:Claude Code 在本仓库工作时

    ### 指引 1: (待添加)
    ```
  - **不修改**任何现有小节(INV-3, FR-10)
- **边界与异常**:
  - 仅追加,不改 / 不删(INV-3)
  - 首次创建时,内容仅含"小节标题 + 1 个空指引占位"
  - 后续 `code-rule` 调用会在该小节内追加"指引 N"
- **验证手段**:
  - `Read CLAUDE.md` 末尾确认新小节存在
  - `git diff CLAUDE.md` 仅显示"+"行,无"-"行(INV-3, INV-11)
  - 原有 7 个小节(L5/L26/L54/L60/L68/L113/L121)完好
- **回退方式**:`git revert <commit>` 撤回小节
- **依赖**:T-001(SKILL.md Type B 子流程依赖此小节作为写入位置)
- **关联任务**:T-001
- **commit**:commit 5

### 任务 `REQ-00003-006`:同步版本看板 + 更新 PLAN.md 状态

- **目标**:每个 commit 落地后,同步更新版本看板 `RESULT.md` 的"任务清单"区段(开发状态推进)+ 同步本 PLAN.md 的状态
- **类型**:文档
- **触发/来源**:需求新增
- **涉及文件**:
  - `assistants/V0.0.1/RESULT.md`("任务清单"区段、"里程碑"区段、"变更记录"区段)
  - `assistants/V0.0.1/plan/REQ-00003/PLAN.md`(本文件,"任务总览"区段的状态)
- **关键变更**:
  - 每个 commit 落地后,把对应任务从"待开始"推进到"已完成"
  - 提交哈希填入"提交哈希"列
  - 关联任务列保持原值
  - 变更记录追加一条:`YYYY-MM-DD HH:mm  开发状态更新  <任务编号> ...  <任务编号>`
- **边界与异常**:
  - **不修改**其他需求的"任务清单"行
  - **不修改**其他区段(需求清单 / 概要设计清单 / 缺陷清单 / 评审发现汇总 / 派生任务记录 / 执行的开发命令记录)
- **验证手段**:
  - `Read V0.0.1/RESULT.md` 确认本需求任务状态推进
  - `Read V0.0.1/RESULT.md §变更记录` 确认追加条目
- **回退方式**:`git revert <commit>`(看板同步通常合入 commit 1-5,无需独立 commit)
- **依赖**:T-001~T-005(每个 commit 落地后同步)
- **关联任务**:T-001~T-005
- **commit**:并入 commit 1-5(不独立 commit,减少提交粒度)

### 任务 `REQ-00003-007`:全仓库 Grep + 不变量自检 + 6 commit 整理

- **目标**:在所有功能 commit 落地后,跑全仓库 Grep 验证不变量(INV-1~11),整理 6 commit 顺序
- **类型**:文档
- **触发/来源**:需求新增
- **涉及文件**:
  - 产出:`code/REQ-00003-007/RESULT.md`(审计报告)
  - 产出:`code/REQ-00003-007/work-log.md`(Grep 命令记录)
  - 产出:`code/REQ-00003-007/deviations.md`(若有不变量违反,记录)
- **关键变更**:
  - 跑以下 Grep 验证:
    - `Grep "规则 1" assistants/rules/*.md` 确认 6 个新文件含占位
    - `Grep "DEPRECATED" assistants/rules/module-conventions.md` 确认弃用标记存在
    - `Grep "## AI 工作约定" plugins/code-skills/CLAUDE.md` 确认小节存在
    - `git status` 确认仅预期文件被修改
    - `git diff --stat` 确认变更范围
  - 验证不变量:
    - INV-3:`git diff CLAUDE.md` 应仅"+"行
    - INV-5:`git status` 应不含 marketplace.json / plugin.json
    - INV-6:`git diff dashboard-conventions.md doc-conventions.md marketplace-protocol.md skill-conventions.md` 应 clean
    - INV-7:`git diff module-conventions.md` 应仅 DEPRECATED 段
  - 6 commit 整理:
    - 检查 commit 顺序:commit 1 → 2 → 3 → 4 → 5 → 6
    - 检查每个 commit 的 message 格式
    - 检查每个 commit 的文件数是否符合预期
- **边界与异常**:
  - **不修改**任何源文件
  - 仅产出审计报告
- **验证手段**:
  - 11 条不变量全部 ✅
  - 6 commit 顺序正确
- **回退方式**:N/A(本任务是审计,无可回退内容)
- **依赖**:T-001~T-006(全部完成后才能审计)
- **关联任务**:T-001~T-006
- **commit**:commit 6(独立 commit,便于 review 审计)

---

## 3. 任务依赖图

```
[T-001: 扩展 SKILL.md]
   │
   ├──→ [T-002: 创建 6 个新占位]
   │       └──→ [T-003: DEPRECATED 标记]
   │              └──→ [T-004: 扩展 templates/rule.md]
   │                     └──→ [T-005: 追加 CLAUDE.md 小节]
   │                            └──→ [T-006: 同步看板] (持续同步,合入 commit 1-5)
   │                                   └──→ [T-007: 全仓库 Grep + 不变量自检]
   │
   └──→ [T-006: 同步看板] (持续同步)
```

**关键路径**:T-001 → T-002 → T-003 → T-004 → T-005 → T-007

**并行机会**:
- T-002 / T-003 / T-004 / T-005 理论上可并行(不同文件),但为便于 review 与回退,保持串行
- T-006 持续同步,每个 commit 后立即执行

---

## 4. 里程碑

| 里程碑 | 包含任务范围 | 完成定义 | 状态 | 计划时间 | 实际完成 |
| --- | --- | --- | --- | --- | --- |
| M3:可发布 | REQ-00003:T-001~T-007(7 任务) | 7 任务开发=已完成 ∧ 测试状态=不适用(全部文档/规范) | 待开始 | 2026-06-04 | — |

**里程碑细分**:
- **M3a:类型识别 + Type A 扩展就绪** — T-001 完成后达成(SKILL.md 文档化,7 个新分类文件就位)
- **M3b:全类型就绪** — T-005 完成后达成(Type A/B/C 全部可用)
- **M3c:M3 达成** — T-007 完成后达成(11 条不变量自检全通过)

---

## 5. commit 顺序(6 个)

| Commit # | 任务 | 涉及文件数 | commit message | 验证手段 |
| --- | --- | --- | --- | --- |
| 1 | T-001 + T-006(看板) | 1(SKILL.md)+ 看板同步 | `feat(code-rule): add 3 target types + 6 classification categories (REQ-00003 FR-1+FR-2+FR-7)` | frontmatter 不变;9 步骤主流程不变 |
| 2 | T-002 + T-006(看板) | 6 新建 | `feat(rules): add 6 placeholder rule files (REQ-00003 FR-2+FR-3)` | 6 文件仅含骨架(INV-2) |
| 3 | T-003 + T-006(看板) | 1 修改 | `chore(rules): deprecate module-conventions.md (REQ-00003 H2)` | 仅 DEPRECATED 段(INV-7) |
| 4 | T-004 + T-006(看板) | 1 修改 | `feat(code-rule): extend rule.md template with placeholder/bootstrap modes (REQ-00003 FR-3+FR-4)` | 8 字段结构不变(FR-8) |
| 5 | T-005 + T-006(看板) | 1 修改 | `feat(CLAUDE.md): add "AI 工作约定" section (REQ-00003 FR-5)` | 仅"+"行(INV-3) |
| 6 | T-007 | 0(仅审计报告) | `chore(code-rule): audit 11 invariants + verify 6 commits (REQ-00003 AC-1~10)` | 11 条不变量 ✅ |

---

## 6. 任务状态推进规则

- **开发状态**:`待开始` → `进行中` → `已完成`(`code-it` 推进)
- **测试状态**:本需求全部 = `不适用`(INV-10,纯文档/规范任务)
- **真正可发布** = 开发状态=已完成 ∧ 测试状态∈{已运行-通过, 不适用}
- 本需求 7 任务全部"真正可发布"判定 = 开发状态=已完成(测试状态不适用不影响)

---

## 7. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-04 09:15 | v1 | 计划新增 | 完成首次编码计划(7 任务 / 6 commit)。范围:扩展 `code-rule/SKILL.md` 正文 + 6 个新分类占位文件 + `module-conventions.md` 弃用 + 扩展 `templates/rule.md` + 追加 `CLAUDE.md` 小节 + 看板同步 + 全仓库审计。所有任务测试状态=不适用(INV-10);11 条不变量(INV-1~11);**plan 阶段对 design 的微调**:类型识别合并到步骤 4 子段 4.2(Q-PLAN-2);**任务粒度**:7 任务 / 6 commit(Q-PLAN-1,commit 1 含 T-001 + T-006);无新增依赖,无偏离规范;**M3 待开始,REQ-00003 阻塞 `code-it` 等待用户触发** | wangmiao |
| 2026-06-04 10:26 | v1.1 | 状态更新 | `REQ-00003-001` 状态"待开始"→"已完成",提交 `086890d`(SKILL.md 272 → 449 行,+177;6 个变更;frontmatter 完整保留;关键词表 11 → 13 项) | wangmiao |
| 2026-06-04 10:53 | v1.2 | 状态更新 | `REQ-00003-002` 状态"待开始"→"已完成",提交 `bec5f13`(新建 6 个新分类占位文件,896-1088 bytes/各;INV-2 最小骨架;INV-5 既有未改;`directory-conventions.md` 含迁移说明) | wangmiao |
| 2026-06-04 10:55 | v1.3 | 状态更新 | `REQ-00003-003` 状态"待开始"→"已完成",提交 `695c029`(`module-conventions.md` 头部 +2 行 DEPRECATED 引用块;INV-7 仅追加不删;不修改其他 12 规范文件) | wangmiao |
| 2026-06-04 10:55 | v1.4 | 状态更新 | `REQ-00003-004` 状态"待开始"→"已完成",提交 `2f41bb0`(`templates/rule.md` 头部 +23 行 2 个 H2 小节;INV-1 8 字段结构保持) | wangmiao |
| 2026-06-04 10:55 | v1.5 | 状态更新 | `REQ-00003-005` 状态"待开始"→"已完成",提交 `35bc26b`(`CLAUDE.md` 末尾 +7 行 1 个 H2 小节"## AI 工作约定(由 code-rule 维护)";INV-3 纯追加不删;原 7 个小节保留) | wangmiao |
| 2024-06-04 10:55 | v1.6 | 状态更新 | `REQ-00003-007` 状态"待开始"→"已完成"(11/11 不变量自检通过;全仓库 0 命中;5 commit 顺序正确;无 commit) | wangmiao |
| 2024-06-04 11:00 | v1.7 | 状态更新 | `REQ-00003-006` 状态"待开始"→"已完成"(M3 全部 7 任务完成;看板 6 区段同步;M3 状态"待开始"→"已完成";commit `ded7613`) | wangmiao |
