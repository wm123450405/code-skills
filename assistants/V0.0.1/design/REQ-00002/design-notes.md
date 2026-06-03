# 设计笔记 — REQ-00002
更新时间:2026-06-03 20:25
版本:V0.0.1

## 0. 设计范围与定位

**本需求是"横切协议文本的批量字符串变更"**,**不新增任何模块、不修改任何代码结构**。设计核心是回答 4 个"如何做"的策略问题:

1. **编辑粒度**:按文件类型分组 vs 一锅端?
2. **任务拆分粒度**:10 SKILL.md + 20+ 模板 + 3 文档 + 1 看板模板 = 多少子任务?
3. **regex / 编号分配逻辑升级**:code-it / code-plan / code-review 三个技能的逻辑变更如何实施
4. **强约束 vs 弱约束的判定**:Q-6 / Q-8 / Q-9 / Q-10 / Q-12 五个待澄清项的处理顺序

> 本设计是"在 `code-require` 已锁定的范围内,对实施策略与子任务拆分做可执行级细化",不重新讨论"是否统一格式"或"统一为几位的格式"。

---

## 1. 关键设计问题清单

### Q-1:用什么工具修改 SKILL.md 与模板?
- **候选 A**:`Edit` 工具,逐处精确替换
  - ✅ 风险低,只动指定行
  - ✅ 保留 frontmatter(SKILL.md `name` / `description` 不动)
  - ❌ 30+ 文件 × 若干处 = 工作量大,但可拆分到子任务并行
- **候选 B**:`Write` 工具,整文件重写
  - ❌ 风险高,易破坏 frontmatter / 章节结构
- **选定 A**
- **依据规范**:`skill-conventions.md §规则 1`(frontmatter 必含且不可破坏);`module-conventions.md §规则 1`(资源在固定子目录)

### Q-2:用什么工具修改 README.md / README.en.md / CLAUDE.md?
- **候选 A**:`Edit` 工具,逐处精确替换
  - ✅ 与 Q-1 同等收益
  - ✅ 保留中英结构对仗
- **候选 B**:`Write` 工具
  - ❌ 易破坏 doc-conventions §规则 1(中英结构对仗)
- **选定 A**
- **依据规范**:`doc-conventions.md §规则 1`(中英结构对仗);§规则 2(命令反映实际)

### Q-3:`version-RESULT.md` 模板(看板模板)如何处理?
- **候选 A**:`Edit` 工具,逐处替换示例值(REQ-2026-0001 → REQ-00001 等)
  - ✅ 不破坏模板结构
  - ⚠ `dashboard-conventions.md §规则 1` 触发条件:仅当改"字段约定扩展"才需三处同步;改"示例值"不触发
- **候选 B**:`Write` 工具
  - ❌ 风险高
- **选定 A**
- **本设计的判定**:本需求**只改 `version-RESULT.md` 中的示例值**,**不改字段语义、不改区段结构、不改表格列**;**不触发** `dashboard-conventions.md §规则 1` 的"三处同步"
- **依据规范**:`dashboard-conventions.md §规则 1`(字段约定扩展的例外 — 纯排版/格式调整不触发)

### Q-4:子任务拆分粒度?
- **候选 A**:按"文件类型"拆(N 个子任务,每个负责一类文件)
  - ✅ 边界清晰,code-review 阶段可独立验收
  - ✅ 失败重试粒度合适
- **候选 B**:按"技能"拆(10 个 SKILL.md + 对应模板,每个子任务负责一个技能)
  - ✅ 与"横切"语义契合
  - ❌ 跨技能同步(README 同步)难以单点收敛
- **选定 A**(以"文件类型"为拆分轴,辅以"按需二次拆分")
- **预想子任务清单**(供 `code-plan` 阶段参考,非定案):
  | 子任务 | 标题 | 主要修改文件 |
  | --- | --- | --- |
  | T-1 | 同步 10 个 SKILL.md | 10 SKILL.md |
  | T-2 | 同步 20+ 模板(占位符 + 示例值) | 全部 `templates/*.md` |
  | T-3 | 同步 README.md / README.en.md | 2 README(同次提交) |
  | T-4 | 同步 CLAUDE.md | 1 文件 |
  | T-5 | 同步 version-RESULT.md 模板(看板模板) | 1 文件 |
  | T-6 | code-it regex + 双路径解析 | (由 T-1 覆盖) |
  | T-7 | code-plan 任务编号分配逻辑 | (由 T-1 覆盖) |
  | T-8 | code-review 派生任务编码规则 | (由 T-1 覆盖) |
  | T-9 | (条件 Q-8 = a)新建 `encoding-conventions.md` | 1 新文件(由 `code-rule` 创建,**本需求不直接操作 rules/**) |
  | T-10 | (条件 Q-9 = a)持久化 `migration-mapping.md` | 1 新文件 |
  | T-11 | 全仓库穷举式 Grep 验证 | 无文件修改 |

> T-6/T-7/T-8 是 T-1 的子项,实际 `code-plan` 阶段可合并或拆分,本设计不强制

### Q-5:任务编号如何分配?(Q-7 锁定后的算法)
- **锁定方案**:Q-7 = G4,父级内独立递增
- **算法**(`code-plan` 在用户告知父级后执行):
  1. 解析父级类型(从 TASK 编码第 2 段 `REQ` / `BUG` 推断,或用户显式告知)
  2. `Glob ./assistants/V0.0.1/plan/<父级>/PLAN.md` 与 `./assistants/V0.0.1/code/TASK-<父类型>-<父级>-*/` 同父级下的所有 TASK 编码
  3. `Grep ^TASK-(REQ|BUG)-<父级数字段>-\d{5}` 取父级内已用最大值
  4. 新任务 = 父级内 max + 1,格式化为 5 位
  5. 拼装新编码:`TASK-REQ-<父级>-NNNNN` 或 `TASK-BUG-<父级>-NNNNN`
- **依据**:Q-7 锁定 + REQU §7 交互 2

### Q-6:code-it 的"双路径解析"如何实施?
- **算法**(`code-it` 收到任务编码后):
  1. 用 `^TASK-(REQ|BUG)-\d{5}-\d{5}$` 验证
  2. 提取第 2 段(`REQ` 或 `BUG`):
     - `REQ` → 工作目录 `./assistants/V<版本号>/plan/<REQ 数字段>-NNNNN/`,从 TASK 编码第 3 段 `<REQ 数字段>-NNNNN` 拼出 REQ 完整编码
     - `BUG` → 工作目录 `./assistants/V<版本号>/fix/<BUG 数字段>-NNNNN/`
  3. 提取第 4 段(`<NNNNN>`)作为任务在父级内的序号
- **依据**:Q-7 锁定 + REQU FR-2

### Q-7:code-review 的"派生任务编码"如何处理?
- **现状**(Q-7 锁定后):派生任务在原任务所属父级(REQ 或 BUG)内继续递增
- **算法**:
  1. 解析被派生的原任务编码,提取父级(REQ-NNNNN 或 BUG-NNNNN)
  2. 查该父级下 TASK 序列最大值
  3. 派生新编码 = `TASK-REQ-<父级>-NNNNN` 或 `TASK-BUG-<父级>-NNNNN`
- **示例**:原任务 `TASK-REQ-00001-00001` 的派生改修任务为 `TASK-REQ-00001-00002`
- **依据**:REQU §7 交互 2 + §8 实体关系

### Q-8:Q-6 (EXISTING-) 默认值
- **REQU 默认**:H1 保留 EXISTING- 前缀
- **本设计采用**:H1(保留)
- **理由**:
  1. 保留 code-init 基线的特殊语义("代码现状的快照" vs "未来需求")
  2. code-init SKILL.md 改动最小(NFR-5 最小化)
  3. "三类编码统一"目标不彻底 — 但通过文档说明(EXISTING- 是基线特例,语义独立)弥补
- **回退路径**:若用户选 H2(改 REQ-NNNNN),需新增 FR-11 覆盖 V0.0.0/EXISTING- 全量迁移
- **依据**:`code-init` SKILL.md 第 7-8 步 + analysis-notes.md §H 候选方案

### Q-9:Q-8 (encoding-conventions.md) 默认值
- **REQU 默认**:Q-8 待用户确认
- **本设计采用默认 (a)**:新建 `./assistants/rules/encoding-conventions.md`
- **理由**:
  1. 编码格式有唯一权威源(NFR-1 强烈建议)
  2. 各 SKILL.md 引用该规则,不硬编码 — 减少后续维护成本
  3. 符合"项目级规范"语义边界(`code-rule` 维护)
- **实施方式**:**本需求不直接写入 rules/**;由用户在 `code-it` 阶段调 `code-rule` 技能创建(REQU FR-7 显式说明)
- **回退路径**:若用户选 (b),不新建规则文件,FR-2 必须穷尽,各 SKILL.md 独立硬编码
- **依据**:NFR-1 + analysis-notes.md §假设 A4

### Q-10:Q-9 (migration-mapping.md) 默认值
- **REQU 默认**:Q-9 待用户确认
- **本设计采用默认 (a)**:持久化 `migration-mapping.md`
- **理由**:
  1. 追溯可长期查询(NFR-3)
  2. 已知映射:`REQ-2026-0001 → REQ-00001`(已部分落地)
  3. (若 Q-6 = H2)可记录 EXISTING- 全部 10 行
- **实施位置**:`./assistants/V0.0.1/require/REQ-00002/migration-mapping.md`(REQU FR-8 显式指定)
- **回退路径**:若用户选 (b) 仅 commit message 或 (c) 不记录,FR-8 不落地
- **依据**:REQU FR-8 + analysis-notes.md §假设 A5

### Q-11:Q-10 (cache 同步提示) 默认值
- **REQU 默认**:b(不加)
- **本设计采用**:b(不加)
- **理由**:NFR-5 最小化;README 中"实施后需 /reload-plugins"已隐含(无需显式加段)
- **回退路径**:若用户选 a,在 README 加一句"实施完成后请执行 /reload-plugins"
- **依据**:NFR-5

### Q-12:Q-12 (TASK 嵌套前缀) 默认值
- **REQU 默认**:a(仅数字段)
- **本设计采用**:a
- **理由**:
  1. 字面简洁(18 字符 vs 23 字符)
  2. 正则更短
  3. 与分析笔记 §Q-12 推荐一致
- **示例**:
  - 需求任务:`TASK-REQ-00001-00001`
  - 修复任务:`TASK-BUG-00001-00001`
- **回退路径**:若用户选 b(含 REQ- 前缀),所有正则与示例批量更新为 `TASK-REQ-REQ-00001-00001`
- **依据**:analysis-notes.md §Q-12

---

## 2. 架构图(数据流)

### 2.1 组件图

```
┌─────────────────────────────────────────────────────────────────┐
│  本次横切影响范围(35+ 文件)                                      │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  10 个 SKILL.md (T-1)                                    │   │
│  │  - code-init / code-version / code-rule                  │   │
│  │  - code-require / code-design / code-plan                │   │
│  │  - code-it / code-unit / code-fix / code-review          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                          ↓                                      │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  20+ 模板 (T-2)                                          │   │
│  │  - requirements.md / design.md / plan.md / task-plan.md  │   │
│  │  - RESULT.md (it/unit) / REVIEW-REPORT.md / REVIEW-FIX.md│   │
│  │  - fix-registry.md / existing-requirement.md             │   │
│  │  - INIT-REPORT.md / assistants-layout.md (10 个副本)     │   │
│  │  - test-spec.md / bug.md / version-RESULT.md             │   │
│  └─────────────────────────────────────────────────────────┘   │
│                          ↓                                      │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  3 文档 (T-3 / T-4)                                       │   │
│  │  - README.md (中) ↔ README.en.md (英,同次提交)            │   │
│  │  - CLAUDE.md                                             │   │
│  └─────────────────────────────────────────────────────────┘   │
│                          ↓                                      │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  1 看板模板 (T-5)                                          │   │
│  │  - version-RESULT.md (条件触发 dashboard-conventions §1) │   │
│  └─────────────────────────────────────────────────────────┘   │
│                          ↓                                      │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  1 新文件(条件 Q-8=a) (T-9,code-rule 创建)               │   │
│  │  - assistants/rules/encoding-conventions.md              │   │
│  └─────────────────────────────────────────────────────────┘   │
│                          ↓                                      │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  1 新文件(条件 Q-9=a) (T-10)                              │   │
│  │  - assistants/V0.0.1/require/REQ-00002/migration-mapping.md│   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 变更传播路径

```
code-require (REQU 阶段)
   ↓ 锁定 10 FR / 7 NFR / 11 AC / 5 项 Q
   ↓
code-design (本设计阶段)
   ↓ 锁定 8 项 Q 默认值 + 11 个子任务预想
   ↓
code-plan
   ↓ 把 11 个子任务预想拆为 N 个开发任务 + 验证任务
   ↓
code-it (实施阶段)
   ├─→ T-1: 10 SKILL.md 逐处 Edit
   ├─→ T-2: 20+ 模板逐处 Edit(占位符 + 示例值)
   ├─→ T-3: README.md + README.en.md (同次提交)
   ├─→ T-4: CLAUDE.md
   ├─→ T-5: version-RESULT.md 模板(示例值)
   ├─→ T-9 (Q-8=a): code-rule 创建 encoding-conventions.md
   └─→ T-10 (Q-9=a): 写 migration-mapping.md
   ↓
code-review
   ├─→ 穷举式 Grep:`REQ-2026-`、`BUG-NNN[^N]`、`<任务编码>` + `格式`、`<需求编号>-<任务序号>`
   ├─→ diff 审阅每个修改文件
   └─→ 中英 README 同次提交核查
   ↓
/reload-plugins (用户手动)
   └─→ cache 同步(超出本仓库可控范围)
```

### 2.3 验证路径

```
1. SKILL.md 旧格式 0 残留
   └─→ Grep "REQ-YYYY" → 0 命中
   └─→ Grep "BUG-NNN[^N]" → 0 命中
   └─→ Grep "<任务编码>" + "格式 `<需求编号>-<任务序号>`" → 0 命中
   └─→ Grep "^REQ-\\d{4}-\\d{4}-\\d{3}$" → 0 命中
   └─→ Grep "^TASK-\\d{5}$" → 0 命中(确认未残留 G1)
   └─→ Grep "^TASK-(REQ|BUG)-\\d{5}-\\d{5}$" → 命中(确认 G4 已落地)

2. 模板旧格式 0 残留
   └─→ 同 1 的 Grep 模式,范围 plugins/code-skills/skills/*/templates/**
   └─→ Grep "REQ-2026-0001-001" → 0 命中
   └─→ Grep "TASK-REQ-00001-00001" → 命中

3. README 中英同次提交
   └─→ Grep 关键短语 0 命中
   └─→ 二级标题并列对仗
   └─→ git log --oneline -- README.md README.en.md 确认同 commit

4. CLAUDE.md 已同步
   └─→ Grep 关键短语 0 命中

5. 看板模板与 V0.0.1 看板同步
   └─→ V0.0.1 看板"需求清单"行使用 REQ-00001 / REQ-00002
   └─→ (Q-8=a) V0.0.1 看板"变更记录"含"新建 encoding-conventions.md"条目

6. (Q-8=a) 各 SKILL.md 引用 encoding-conventions.md
   └─→ Grep "encoding-conventions.md" → 10 命中(每个 SKILL.md 至少 1 处引用)

7. (Q-9=a) migration-mapping.md 存在
   └─→ Read 文件,确认含 REQ-2026-0001 → REQ-00001 一行

8. 不变量验证
   └─→ 不触发 marketplace-protocol §规则 1(marketplace.json / plugin.json 不动)
   └─→ 不触发 skill-conventions §规则 1(SKILL.md frontmatter 完整)
   └─→ (Q-6=H1)V0.0.0/EXISTING- 文件名保持
```

---

## 3. 关键不变量(本需求严禁破坏)

| 不变量 | 来源 | 验证方式 |
| --- | --- | --- |
| `marketplace.json` 任何字段 | `marketplace-protocol.md §规则 1`;REQU FR-10 | `git diff --stat` |
| `plugin.json` 任何字段 | 同上 | 同上 |
| `plugins/code-skills/` 目录名 | REQU FR-10 | `ls plugins/` |
| git 远端仓库名 | REQU FR-10 | `git remote -v` |
| 10 个 SKILL.md frontmatter(`name` + `description`)| `skill-conventions.md §规则 1` | `Grep "^name: code-" + "^description: "` |
| 10 个 SKILL.md 的 `name` 与目录名一致 | `skill-conventions.md §规则 1` | 人工核对 |
| 模板文件位置(templates/ / checklists/ / guidelines/)| `module-conventions.md §规则 1` | `ls skills/<技能>/` |
| V0.0.0 EXISTING- 目录名(Q-6=H1 时) | REQU FR-10 + Q-6 决策 | `ls V0.0.0/require/` |
| (Q-6=H1)V0.0.0 EXISTING- 文件**内**的旧编码 | 不变(基线特例) | 保持 |
| 中英 README 结构对仗 | `doc-conventions.md §规则 1` | 并列 diff |
| (Q-6=H1)code-init SKILL.md 产生 EXISTING- 的逻辑 | 保持 | Read 确认 |

---

## 4. 备选方案被否决的理由

| 备选方案 | 否决理由 |
| --- | --- |
| 整文件 Write SKILL.md | 风险高,易破坏 frontmatter(`skill-conventions.md §规则 1`) |
| 按"技能"拆子任务(每个子任务负责一个技能的 SKILL.md + 模板) | 跨技能同步(README 同步)难以单点收敛 |
| 升 dashboard-conventions §规则 1(强制三处同步看板模板) | 本需求**只改示例值**,不改字段语义,§规则 1 不触发(本规则的"纯排版/格式调整"例外) |
| 强制改 EXISTING- 全部 10 个为 REQ-NNNNN(Q-6=H2) | Q-6 待澄清,REQU 默认 H1 保留;若用户改 H2 走回退路径新增 FR-11 |
| 含 `REQ-` 前缀(Q-12 候选 b)的 TASK 编码 | Q-12 待澄清,REQU 默认 a 仅数字段;字面更简洁,正则更短 |
| 引入编码"自动校验脚本" | NFR-5 显式禁止(本仓库无 lint 体系) |
| 引入编码"自动生成器" | NFR-5 显式禁止(沿用 AI + 人工) |
| 强制新建 `encoding-conventions.md` 不论 Q-8 | Q-8 待澄清,本设计采用默认 (a) 准备新增但不**直接**操作 rules/(由 code-rule 创建) |
