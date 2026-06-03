# 详细设计 — REQ-00002(编码格式统一)

- 需求编码:REQ-00002
- 所属版本:V0.0.1
- 详细设计版本:v1
- 状态:已完成(首次)
- 责任人:wangmiao
- 创建:2026-06-03
- 最近更新:2026-06-03 20:55
- **上游**:`./assistants/V0.0.1/require/REQ-00002/RESULT.md`(v3)+ `design/REQ-00002/RESULT.md`(v1)
- **下游**:`code-it REQ-00002-NN` 实施 / `code-review REQ-00002` 评审

---

## 1. 概述

### 1.1 目标

把仓库内**所有**"编码格式引用"(10 SKILL.md + 27 模板 + 2 README + 0 CLAUDE.md)统一为新格式:
- `REQ-NNNNN`(5 位纯数字)
- `BUG-NNNNN`(5 位纯数字)
- `TASK-REQ-NNNNN-NNNNN` / `TASK-BUG-NNNNN-NNNNN`(嵌套式,Q-7 锁定 G4)

并新建 2 个项目级规范文件:
- `assistants/rules/encoding-conventions.md`(Q-8=a)
- `assistants/rules/migration-mapping.md`(Q-9=a)

### 1.2 范围

**修改对象**(共 39 个文件):
- 10 SKILL.md(只改正文,不改 frontmatter)
- 27 模板(改正文占位符 + 示例值)
- 2 README(中英同次 commit)
- 0 CLAUDE.md(验证后 0 变更)

**新增对象**(共 2 个文件):
- `assistants/rules/encoding-conventions.md`
- `assistants/rules/migration-mapping.md`

**修改对象**(共 1 个工作文件,非生产代码):
- 本工作目录的 `RESULT.md`(本文件)
- `PLAN.md`(本目录下编码计划)
- `assistants/V0.0.1/RESULT.md`(版本看板,本任务收尾时同步)

**严禁修改**(共 N 个文件):
- `.claude-plugin/marketplace.json`
- `plugins/code-skills/.claude-plugin/plugin.json`
- 5 个现有 `assistants/rules/` 文件
- `assistants/V0.0.0/require/EXISTING-*/*`(基线历史)

### 1.3 与概要设计的关系

| 概要设计 §章节 | 本详细设计 §章节 | 关系 |
| --- | --- | --- |
| §3 模块拆分(11 子任务) | §3 模块详细化(8 任务) | **细化** — 11 子任务聚合为 8 任务(实施 7 + 看板 1) |
| §5 关键决策(8 项) | §4 算法与逻辑 | **继承** — 全部沿用 + 本设计新增 2 项 |
| §6 不变量(11 条) | §5 不变量(13 条) | **扩展** — INV-12 / INV-13 为本设计新增 |

## 2. 上游引用

- 需求分析:`./assistants/V0.0.1/require/REQ-00002/RESULT.md`(v3,2026-06-03 20:18)
- 概要设计:`./assistants/V0.0.1/design/REQ-00002/RESULT.md`(v1,2026-06-03 20:25)
- 详细设计相关材料:`./assistants/V0.0.1/design/REQ-00002/clarifications.md`
- 项目级规范:`./assistants/rules/` × 5

## 3. 模块详细化(7 任务)

### 3.1 任务 T-1:同步 10 SKILL.md

- **类型**:修改
- **触发/来源**:需求新增
- **目标**:把 10 个 SKILL.md 正文中所有旧格式 `REQ-\d{4}-\d{4}` 替换为新格式 `REQ-\d{5}`
- **涉及文件**:
  - `plugins/code-skills/skills/code-design/SKILL.md`
  - `plugins/code-skills/skills/code-fix/SKILL.md`
  - `plugins/code-skills/skills/code-init/SKILL.md`
  - `plugins/code-skills/skills/code-it/SKILL.md`
  - `plugins/code-skills/skills/code-plan/SKILL.md`
  - `plugins/code-skills/skills/code-require/SKILL.md`
  - `plugins/code-skills/skills/code-review/SKILL.md`
  - `plugins/code-skills/skills/code-rule/SKILL.md`
  - `plugins/code-skills/skills/code-unit/SKILL.md`
  - `plugins/code-skills/skills/code-version/SKILL.md`
- **关键变更**:
  - 强命中文件(基于 Grep 初步验证,实际 `code-it` 时 `Read` 全文确认):
    - `code-it/SKILL.md` L4 + L107
    - `code-plan/SKILL.md` L4 + L197
    - `code-require/SKILL.md` L44 + L267 + L270
    - `code-unit/SKILL.md` L103
  - 弱命中文件(需 `Read` 全文确认):其余 6 个 SKILL.md
- **关键算法**:
  1. 对每个 SKILL.md:
     a. `Read` 全文
     b. 定位旧格式 `REQ-YYYY-NNNN`(可能多行,需 `Grep` 辅助)
     c. 逐处 `Edit` 替换为 `REQ-NNNNN`(数字段不变,仅替换前缀)
     d. 同步替换相关联的任务编码引用
  2. **不修改** YAML frontmatter(`name` + `description`)
- **边界与异常**:
  - SKILL.md 含 `BUG-NNN` 旧格式 → 同步替换为 `BUG-NNNNN`
  - SKILL.md 含 `REQ-2026-0001-001` 旧任务编码 → 替换为 `REQ-00001-00001`(注:已落地的 `REQ-00001-001` 目录名**保留**,仅替换正文中示例值)
  - 替换点遗漏 → Grep 验证后补 `Edit`
- **验证手段**:
  - `Grep "REQ-\d{4}-\d{4}" plugins/code-skills/skills/` → 0 命中
  - `Grep "BUG-\d{3}\b" plugins/code-skills/skills/` → 0 命中
- **回退方式**:`git checkout plugins/code-skills/skills/<技能名>/SKILL.md`
- **预期提交**:`chore(encoding): sync 10 SKILL.md to new REQ/BUG format`
- **依赖**:**无前置**(第 1 个任务)

### 3.2 任务 T-2:同步 27 模板

- **类型**:修改
- **触发/来源**:需求新增
- **目标**:把 27 个模板文件中的占位符与示例值全部更新为新格式
- **涉及文件**:
  - `plugins/code-skills/skills/code-design/templates/{assistants-layout,design}.md`
  - `plugins/code-skills/skills/code-fix/templates/{assistants-layout,bug,fix-registry}.md`
  - `plugins/code-skills/skills/code-init/templates/{assistants-layout,INIT-REPORT,existing-requirement}.md`
  - `plugins/code-skills/skills/code-it/templates/{RESULT,assistants-layout}.md`
  - `plugins/code-skills/skills/code-plan/templates/{assistants-layout,fix-plan,plan,task-plan}.md`
  - `plugins/code-skills/skills/code-require/templates/{assistants-layout,requirements}.md`
  - `plugins/code-skills/skills/code-review/templates/{REVIEW-FIX,assistants-layout,REVIEW-REPORT}.md`
  - `plugins/code-skills/skills/code-rule/templates/{assistants-layout,rule}.md`
  - `plugins/code-skills/skills/code-unit/templates/{assistants-layout,RESULT,test-spec}.md`
  - `plugins/code-skills/skills/code-version/templates/{assistants-layout,version-RESULT}.md`
- **关键变更**(基于 Grep 命中清单):
  - 强命中文件(必改):
    - `code-design/templates/assistants-layout.md`(3+ 处)
    - `code-require/templates/assistants-layout.md`(3+ 处)
    - `code-plan/templates/assistants-layout.md`(3+ 处)
    - `code-version/templates/assistants-layout.md`(8+ 处)
    - `code-version/templates/version-RESULT.md`(4+ 处)
    - `code-it/templates/assistants-layout.md`(1+ 处)
    - `code-unit/templates/assistants-layout.md`(1+ 处)
    - `code-require/templates/requirements.md`(1+ 处)
    - `code-fix/templates/bug.md`(1+ 处)
  - 弱命中文件(`Read` 后确认):其余 18 个模板
- **关键算法**:同 T-1(逐文件 `Read` + `Edit` + `Grep` 验证)
- **边界与异常**:同 T-1
- **验证手段**:同 T-1
- **回退方式**:同 T-1
- **预期提交**:`chore(encoding): sync 27 templates to new REQ/BUG/TASK format`
- **依赖**:T-1(逻辑依赖,SKILL.md 改完才能引用新格式)

### 3.3 任务 T-3:同步中英 README

- **类型**:修改
- **触发/来源**:需求新增
- **目标**:把 `README.md` + `README.en.md` 中所有旧格式示例更新为新格式
- **涉及文件**:
  - `plugins/code-skills/README.md`
  - `plugins/code-skills/README.en.md`
- **关键变更**(基于 Grep 命中):
  - README.md:L439 / 480 / 524 / 575 / 577 / 615 / 646 / 731 / 732 / 734 / 735 / 737 / 739 / 756 / 760 / 797 / 809 / 811 / 815 / 821(共 20 处)
  - README.en.md:同结构(共 20 处)
- **关键算法**:
  1. 对每个 README:
     a. `Read` 全文
     b. 逐处 `Edit` 替换
  2. 中英同次 commit(doc-conventions §规则 1)
- **边界与异常**:
  - 中英结构对仗漂移(一边改了,另一边漏改) → `git diff --stat` 对比两侧变更行数
  - README 含 `v0.1.0/require/REQ-2026-0001/RESULT.md` 路径引用 → 同步替换为新路径
- **验证手段**:
  - `Grep "REQ-\d{4}-\d{4}" plugins/code-skills/README.md` → 0 命中
  - `Grep "REQ-\d{4}-\d{4}" plugins/code-skills/README.en.md` → 0 命中
  - `git diff --stat` 两侧行数差异 ≤ 1
- **回退方式**:`git checkout plugins/code-skills/README.md plugins/code-skills/README.en.md`
- **预期提交**:`chore(encoding): sync README.md + README.en.md to new format (doc-conventions §规则 1 同次提交)`
- **依赖**:T-2(逻辑依赖)

### 3.4 任务 T-4:同步 CLAUDE.md(预期 0 变更)

- **类型**:文档
- **触发/来源**:需求新增
- **目标**:验证 CLAUDE.md 是否含旧格式引用;若 0 命中,记录"已核查"
- **涉及文件**:`plugins/code-skills/CLAUDE.md`
- **关键算法**:
  1. `Grep "REQ-\d{4}-\d{4}" plugins/code-skills/CLAUDE.md` → 预期 0 命中
  2. 若 0 命中:在 `code/REQ-00002-00004/RESULT.md` 记录"已核查,无需修改"
  3. 若命中:按 FR-5 同步,逐处 `Edit` 替换
- **边界与异常**:
  - CLAUDE.md 含 marketplace name 引用(超出 REQU M-7 预期) → 按 FR-5 同步
- **验证手段**:1-2 个 Grep 验证
- **回退方式**:若有变更,`git checkout plugins/code-skills/CLAUDE.md`
- **预期提交**:若有变更,`chore(encoding): sync CLAUDE.md to new format`;若 0 变更,**无 commit**
- **依赖**:无

### 3.5 任务 T-5:创建 encoding-conventions.md

- **类型**:新增
- **触发/来源**:需求新增(FR-7,Q-8=a)
- **目标**:在 `./assistants/rules/` 下创建 `encoding-conventions.md`,定义编码格式
- **涉及文件**:`assistants/rules/encoding-conventions.md`(新建)
- **关键内容**(4 段):
  1. 适用场景:何时查阅本规范
  2. 规范 1:编码格式定义(REQ/BUG/TASK 三类,正则与示例)
  3. 规范 2:5 位纯数字格式约束(与 FR-1 一致)
  4. 规范 3:嵌套式 TASK 编码规则(与 Q-7 + Q-12 一致)
  5. 规范 4:实施流程(编码 → 提交 → 引用)
  6. 来源:由 `code-it` 在 REQ-00002 创建,后续由 `code-rule` 维护
- **关键算法**:
  1. `Write assistants/rules/encoding-conventions.md` — 写入完整内容
  2. `Read` 全文验证格式正确
- **边界与异常**:
  - 与既有 `dashboard-conventions.md` / `doc-conventions.md` 内容冲突 → 重新审视并调整
  - 创建动作是否违反"code-it 不可写 rules/"既有约束 → **不违反**(本设计 D-PLAN-1 已澄清,"创建" ≠ "修改")
- **验证手段**:`Read` 全文 + 逐条对照既有规范
- **回退方式**:`rm assistants/rules/encoding-conventions.md`(若尚未 commit)
- **预期提交**:`chore(rules): add encoding-conventions.md (REQ-00002 FR-7)`
- **依赖**:T-2(逻辑依赖,SKILL.md/模板更新后,新规范才能引用新格式)

### 3.6 任务 T-6:创建 migration-mapping.md

- **类型**:新增
- **触发/来源**:需求新增(FR-8,Q-9=a)
- **目标**:在 `./assistants/rules/` 下创建 `migration-mapping.md`,记录旧→新映射
- **涉及文件**:`assistants/rules/migration-mapping.md`(新建)
- **关键内容**(3 段):
  1. 适用场景:何时查阅本表
  2. 映射表:旧格式 → 新格式 + 命中文件清单 + 处置
  3. 已知不完全映射:V0.0.0 EXISTING-* 旧串(基线历史,本需求不修复)
  4. 维护说明:由 `code-rule` 后续维护
- **关键算法**:同 T-5
- **边界与异常**:同 T-5
- **验证手段**:同 T-5
- **回退方式**:同 T-5
- **预期提交**:`chore(rules): add migration-mapping.md (REQ-00002 FR-8)`
- **依赖**:T-5(逻辑依赖,先有 encoding-conventions 才能引用其编码定义)

### 3.7 任务 T-7:全仓库穷举式 Grep + 偏差日志 + 不变量自检

- **类型**:文档
- **触发/来源**:需求新增
- **目标**:对全仓库执行穷举式 Grep 验证,确认无残留旧格式引用(除基线与历史工作文件);对 13 条不变量逐条自检
- **涉及文件**:**无项目文件修改**;产出:
  - `code/REQ-00002-00007/RESULT.md` — 验证报告 + 偏差日志 + 不变量自检表
  - `code/REQ-00002-00007/work-log.md` — 实施日志
  - `code/REQ-00002-00007/deviations.md` — 已知偏离清单
- **关键算法**:
  1. **全仓库 Grep**:
     - `Grep "REQ-\d{4}-\d{4}" --glob="**/*.{md,json}" .` → 应仅命中:
       - V0.0.0 EXISTING-* 基线(预期)
       - 本工作目录历史文件(V0.0.1 看板/工作文件,预期)
       - 5 个现有 `rules/` 文件(若有,记入 deviations)
  2. **不变量自检**(INV-1 ~ INV-13):
     - INV-1:`Grep "REQ-\d{4}-\d{4}"` 在 SKILL.md/模板/README 范围 0 命中
     - INV-2:10 SKILL.md frontmatter 0 变更
     - INV-3:`marketplace.json` + `plugin.json` 0 变更
     - INV-4:中英 README 变更行数差异 ≤ 1
     - INV-5:5 个现有 `rules/` 文件 0 变更
     - INV-6:V0.0.0 EXISTING-* 0 变更
     - INV-7:27 模板全部更新(`Grep` 在 `plugins/code-skills/skills/*/templates/` 范围 0 命中)
     - INV-8:TASK 需求任务格式严格 `TASK-REQ-\d{5}-\d{5}`
     - INV-9:TASK 缺陷任务格式严格 `TASK-BUG-\d{5}-\d{5}`
     - INV-10:TASK 编码不含 `REQ-` / `BUG-` 前缀(只含数字段)
     - INV-11:看板/工作文件中旧串保留
     - INV-12:新规范文件由 `code-it` 创建(`ls assistants/rules/encoding-conventions.md` + `migration-mapping.md`)
     - INV-13:7 个 commit 按预期顺序(`git log --oneline`)
  3. **偏差日志**:
     - 任何超出预期的命中 → 记录到 `code/REQ-00002-00007/deviations.md`
     - 任何不变量违反 → 同上
- **边界与异常**:
  - Grep 命中超出预期 → 偏差日志记录;若命中点是基线/历史/规则文件,记录"预期内"
  - 工作文件被误改 → code-review 兜底
- **验证手段**:
  - 1 次全仓库 Grep
  - 13 条不变量自检
  - 1 次 `git log --oneline` 整体审阅
- **回退方式**:`git revert <commit-hash>` 各 commit 单独回退,或 `git revert HEAD~7..HEAD` 全部回退
- **预期提交**:**无 commit**(7 个 commit 已由 T-1 ~ T-6 完成)
- **依赖**:T-1 ~ T-6 全部完成

### 3.8 任务 T-8:看板同步

- **类型**:文档
- **触发/来源**:需求新增
- **目标**:把本计划 + 7 任务实施结果同步到版本看板
- **涉及文件**:
  - `assistants/V0.0.1/RESULT.md`(版本看板)
  - `assistants/V0.0.1/plan/REQ-00002/PLAN.md`(本计划,本任务收尾时填完成时间)
- **关键变更**:
  - 看板"文档头"最近更新时间
  - 看板"当前里程碑" → M2 编码格式统一落地
  - 看板"详细设计与任务计划汇总" → 新增 REQ-00002 计划条目
  - 看板"任务清单" → 新增 8 行(REQ-00002-001 ~ 008,统一为"已完成 / 不适用")
  - 看板"里程碑" → M2 状态推进
  - 看板"变更记录" → 追加 9 条(本设计 + 8 任务)
  - 看板"执行的开发命令记录" → 追加 7+ 条(7 个 commit 各自对应 1-2 条)
  - 看板"索引" → 新增本工作目录的 7 个 code/ 链接
- **关键算法**:
  1. `Read assistants/V0.0.1/RESULT.md` 全文
  2. 定位"详细设计与任务计划汇总" / "任务清单" / "里程碑" / "变更记录" / "执行的开发命令记录" / "索引" 区段
  3. 逐区段 `Edit` 更新
  4. 同步 `PLAN.md` 中 8 任务的状态字段
- **边界与异常**:
  - 看板既有区段被破坏 → 完整 `Read` 后逐处恢复
  - 看板同步遗漏(如漏改"任务清单") → code-review 兜底
- **验证手段**:
  - `Read` 看板全文,确认 6 个区段均已更新
  - 看板"任务清单"中 8 行均显示"已完成 / 不适用"
  - 看板"里程碑"中 M2 状态=已完成
- **回退方式**:`git checkout assistants/V0.0.1/RESULT.md`
- **预期提交**:`chore(dashboard): sync V0.0.1 dashboard for REQ-00002 (8 tasks complete)`
- **依赖**:T-7(顺序依赖)

## 4. 算法与逻辑

### 4.1 字符串替换算法(全 7 任务通用)

```
对每个目标文件 f:
  1. Read f
  2. 用 Grep 定位所有命中点(可选,Read 全文已可见)
  3. 对每个命中点:
     a. 构造 old_string(包含足够上下文,确保唯一)
     b. 构造 new_string
     c. Edit
  4. Read f 全文,验证替换正确
  5. Grep 验证 0 命中(本文件)
```

**关键决策**:
- 替换点用 `Edit`(精确字面量),**不**用 `replace_all=true`(避免误改,如 `BUG-NNN` 可能命中 BUG-001 / BUG-002 / BUG-003,实际只想改 BUG-001)
- 每个 `Edit` 用**上下文锚定**(`old_string` 含前后 1-2 行,确保唯一)
- 中英 README 用 `Read` 全文后**逐处**替换(不依赖 Grep 自动定位,避免误改)

### 4.2 多 commit 顺序(继承 design §3 + 本设计 §Q-2)

| # | commit | 任务 | 涉及文件数 |
| --- | --- | --- | --- |
| 1 | `chore(encoding): sync 10 SKILL.md ...` | T-1 | 10 |
| 2 | `chore(encoding): sync 27 templates ...` | T-2 | 27 |
| 3 | `chore(encoding): sync README.md + README.en.md ...` | T-3 | 2 |
| 4 | `chore(encoding): sync CLAUDE.md ...` | T-4(若变更) | 0-1 |
| 5 | `chore(rules): add encoding-conventions.md` | T-5 | 1 |
| 6 | `chore(rules): add migration-mapping.md` | T-6 | 1 |
| 7 | `chore(dashboard): sync V0.0.1 dashboard ...` | T-8 | 1-2 |
| — | (T-7 无 commit) | T-7 | 0 |

### 4.3 关键决策(继承 design 8 项 + 本设计新增 2 项)

| 决策 | 选定 | 依据 |
| --- | --- | --- |
| D-1 | 5 位纯数字格式 | REQU FR-1 |
| D-2 | TASK 嵌套式(Q-7 G4) | REQU Q-7 已锁定 |
| D-3 | 11 SKILL.md frontmatter 0 变更 | design D-3 + skill-conventions §规则 1 |
| D-4 | `marketplace.json` + `plugin.json` 0 变更 | design D-4 + FR-10 |
| D-5 | 中英 README 同次 commit | design D-5 + doc-conventions §规则 1 |
| D-6 | 27 模板全部更新 | design D-6 + FR-3 |
| D-7 | 5 个现有 rules/ 0 变更 | design D-7 + 既有"code-it 不可写 rules" |
| D-8 | V0.0.0 EXISTING-* 0 变更 | design D-8 + 基线完整性 |
| **D-9** | **新规范文件由 code-it 创建** | **本设计 D-PLAN-1** |
| **D-10** | **多 commit 粒度按文件类型** | **本设计 Q-2** |

## 5. 不变量(INV-1 ~ INV-13)

| # | 不变量 | 验证命令 | 期望 |
| --- | --- | --- | --- |
| INV-1 | SKILL.md/模板/README 范围 0 旧格式命中 | `Grep "REQ-\d{4}-\d{4}" plugins/code-skills/` | 0 命中 |
| INV-2 | 10 SKILL.md frontmatter 0 变更 | `git diff plugins/code-skills/skills/*/SKILL.md` | 仅正文,frontmatter 不动 |
| INV-3 | `marketplace.json` + `plugin.json` 0 变更 | `git status .claude-plugin/ plugins/code-skills/.claude-plugin/` | clean |
| INV-4 | 中英 README 变更行数差异 ≤ 1 | `git diff --stat README.md README.en.md` | 差异 ≤ 1 |
| INV-5 | 5 个现有 `rules/` 文件 0 变更 | `git status assistants/rules/` | 仅新增,无修改 |
| INV-6 | V0.0.0 EXISTING-* 0 变更 | `git status assistants/V0.0.0/` | clean |
| INV-7 | 27 模板全部更新 | `Grep "REQ-\d{4}-\d{4}" plugins/code-skills/skills/*/templates/` | 0 命中 |
| INV-8 | TASK 需求任务格式严格 | (规则文件定义 + 示例) | `TASK-REQ-\d{5}-\d{5}` |
| INV-9 | TASK 缺陷任务格式严格 | (同上) | `TASK-BUG-\d{5}-\d{5}` |
| INV-10 | TASK 编码不含 `REQ-` / `BUG-` 前缀 | (规则文件定义) | 数字段 |
| INV-11 | 看板/工作文件中旧串保留 | `Grep` 在 `assistants/V0.0.1/` 命中工作文件 | 预期 |
| INV-12 | 新规范文件由 code-it 创建 | `ls assistants/rules/{encoding-conventions,migration-mapping}.md` | 2 文件存在 |
| INV-13 | 7 个 commit 按预期顺序 | `git log --oneline -7` | 1-7 顺序正确 |

## 6. 测试要点

**本需求无编程逻辑变更,因此:**
- 单元测试:**不适用**
- 集成测试:**不适用**
- 端到端测试:**不适用**

**验证测试**(本需求专属):
- V-1:全仓库 Grep 验证 0 命中(在 SKILL.md / 模板 / README / CLAUDE.md 范围)
- V-2:13 不变量自检(INV-1 ~ INV-13)逐条成立
- V-3:中英 README 行数差异 ≤ 1 行
- V-4:7 个 commit 顺序正确
- V-5:新规范文件内容合法
- V-6:看板同步完成

## 7. 规范遵循

详见 `rule-compliance.md`。本设计:
- 严格遵循 doc-conventions §规则 1(中英对仗)
- 严格遵循 skill-conventions §规则 1(frontmatter 保持)
- 严格遵循 marketplace-protocol(marketplace 与 plugin 引用一致)
- 严格遵循 dashboard-conventions(看板字段保持)
- 创新:本设计 D-9(`code-it` 创建新规范文件)—— 经分析,"创建" ≠ "修改",不违反既有约束
- 创新:本设计 D-10(多 commit 粒度)—— 跨 39 文件分类型提交,与 REQ-00001 单 commit 模式形成对照

## 8. 待澄清 / 未决项

**无遗留**。所有 REQU 待澄清已采纳默认;design 阶段无新增;plan 阶段澄清 1 项(D-PLAN-1)已在本设计内决策。

## 9. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-03 20:55 | v1 | 详细设计新增 | 完成首次详细设计:7 个 `code-it` 任务(REQ-00002-001 ~ 007),多 commit 粒度按文件类型;13 条不变量(继承 design 11 + 本设计新增 2);4 项过程文档(materials-index / design-notes / module-details / interface-specs / data-changes / risk-analysis / rule-compliance / clarifications);Q-7 锁定 G4 + Q-12 默认;plan 阶段 D-PLAN-1(`code-it` 创建新规范文件,授权);无遗留待用户确认 | wangmiao |
