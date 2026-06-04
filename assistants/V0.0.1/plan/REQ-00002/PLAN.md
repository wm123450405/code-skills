# 编码计划 — REQ-00002(编码格式统一)

- 需求编码:REQ-00002
- 所属版本:V0.0.1
- 计划版本:v1
- 状态:已完成(M2 8 任务全部完成,待最终 commit)
- 责任人:wangmiao
- 创建:2026-06-03
- 最近更新:2026-06-04 10:20
- **上游**:`./assistants/V0.0.1/require/REQ-00002/RESULT.md` + `design/REQ-00002/RESULT.md` + 本目录 `RESULT.md`
- **下游**:`code-it REQ-00002-NN` 实施 / `code-review REQ-00002` 评审

---

## 1. 任务总览

| 任务编号 | 标题 | 类型 | 触发/来源 | 开发状态 | 测试状态 | 涉及文件 | 完成时间 | 提交哈希 | 关联任务 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `REQ-00002-001` | 同步 10 个 SKILL.md(只改正文) | 修改 | 需求新增 | 已完成 | 不适用 | `plugins/code-skills/skills/{code-fix,code-it,code-plan,code-require,code-unit}/SKILL.md`(5 文件) | 2026-06-04 09:50 | 8ac1c9a | — |
| `REQ-00002-002` | 同步 27 模板(改正文占位符 + 示例值) | 修改 | 需求新增 | 已完成 | 不适用 | 11 templates(见 §2.2 + RESULT.md 偏离 1) | 2026-06-04 10:05 | 3df8ae7 | T-1 |
| `REQ-00002-003` | 同步中英 README(同次 commit) | 修改 | 需求新增 | 已完成 | 不适用 | `plugins/code-skills/README.md`, `README.en.md` | 2026-06-04 10:00 | 31d6221 | T-1, T-2 |
| `REQ-00002-004` | 核查 CLAUDE.md(预期 0 变更) | 文档 | 需求新增 | 已完成 | 不适用 | plugins/code-skills/CLAUDE.md(0 变更,无 commit) | 2026-06-04 10:00 | (无 commit) | — |
| `REQ-00002-005` | 创建 encoding-conventions.md 规范文件 | 新增 | 需求新增(FR-7) | 已完成 | 不适用 | assistants/rules/encoding-conventions.md | 2026-06-04 10:05 | b092dec | T-1, T-2 |
| `REQ-00002-006` | 创建 migration-mapping.md 迁移映射 | 新增 | 需求新增(FR-8) | 已完成 | 不适用 | assistants/rules/migration-mapping.md | 2026-06-04 10:08 | 5121e3f | T-5 |
| `REQ-00002-007` | 全仓库穷举式 Grep + 偏差日志 + 不变量自检 | 文档 | 需求新增 | 已完成 | 不适用 | 无文件修改,产出 `code/REQ-00002-007/{RESULT,work-log,deviations,compile-and-run}.md` | 2026-06-04 10:15 | (无 commit) | T-1 ~ T-6 |
| `REQ-00002-008` | 同步版本看板 | 文档 | 需求新增 | 已完成 | 不适用 | `assistants/V0.0.1/RESULT.md` + 本 `PLAN.md` | 2026-06-04 10:20 | a24663d | T-1 ~ T-7 |
| `REQ-00002-009` | 同步 PLAN.md 任务总览 + M2 描述(审查派生) | 文档 | 审查改修 | 已完成 | 不适用 | `assistants/V0.0.1/plan/REQ-00002/PLAN.md`(3 个核心 Edit + 1 个自身状态) | 2026-06-04 12:40 | (不提交,见 deviations.md) | REQ-00002-007, REQ-00002-008 |

**统计**(目标):
- 总任务数:**8**(7 实施 + 1 看板同步)
- 真正可发布数(开发=已完成 ∧ 测试∈{已运行-通过, 不适用}):8 / 8(目标) ✅ M2 已达成
- 开发已完成 / 未完成:8 / 0(全部完成)
- 测试已通过 / 已失败 / 不适用 / 未编写:0 / 0 / 8 / 0(全部为"纯文档任务")

**任务编号说明**:
- 本设计 7 任务(详细设计 §3)+ 1 看板同步任务 = **8 任务**
- 编号 `REQ-00002-001` ~ `REQ-00002-008`,三位补零
- 与 Q-7 锁定的"嵌套式 TASK 编码"(`TASK-REQ-00002-NNNNN`)是**两种**编码体系:
  - 本计划用 `REQ-00002-NNN`(旧格式)便于内部追踪
  - 实施完成后,看板"任务清单"中此 8 行作为历史,**不**改名为新格式
  - **新需求**的任务将用 `TASK-REQ-XXXXX-NNNNN`(本需求起,新格式生效)

---

## 2. 任务详情

### 2.1 `REQ-00002-001` — 同步 10 SKILL.md

**目标**:把 10 个 SKILL.md 正文中所有 `REQ-\d{4}-\d{4}` 替换为 `REQ-\d{5}`,不动 YAML frontmatter。

**涉及文件**(10 个,均**只改正文**):
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

**关键变更**(基于初步 Grep,实际以 `Read` 全文为准):
| 文件 | 命中行(初步) | 改前示例 | 改后示例 |
| --- | --- | --- | --- |
| `code-it/SKILL.md` | L4, L107 | `REQ-2026-0001-001` | `REQ-00001-00001` |
| `code-plan/SKILL.md` | L4, L197 | `REQ-2026-0001-001` | `REQ-00001-00001` |
| `code-require/SKILL.md` | L44, L267, L270 | `REQ-2026-0001` / `REQ-2025-0099` | `REQ-00001` / `REQ-00510` |
| `code-unit/SKILL.md` | L103 | `REQ-2026-0001-001` | `REQ-00001-00001` |
| 其余 6 个 | 0(初步) | — | `Read` 全文确认 |

**操作步骤**:
1. 对每个 SKILL.md:
   a. `Read` 全文
   b. `Grep "REQ-\d{4}-\d{4}"` 定位所有命中点
   c. 逐处 `Edit`(用上下文锚定,确保 `old_string` 唯一)
2. 验证:
   - `Grep "REQ-\d{4}-\d{4}" plugins/code-skills/skills/` → 0 命中
   - `Grep "BUG-\d{3}\b" plugins/code-skills/skills/` → 0 命中
3. 单独 commit 1 次(继承 design D-10 多 commit 策略):
   - `git add plugins/code-skills/skills/*/SKILL.md`
   - `git commit -m "chore(encoding): sync 10 SKILL.md to new REQ/BUG format"`

**边界与异常**:
- SKILL.md frontmatter 误改 → 撤回该 `Edit`,重做(因 `Edit` 已记录差异,可用 `git checkout <file>` 恢复)
- 替换遗漏(改了 5 个,漏 5 个) → 重新 `Grep` 定位,补 `Edit`

**验证手段**:
- 全文件范围 `Grep "REQ-\d{4}-\d{4}"` → 0 命中
- 单文件 `Read` 抽查 3 个文件,确认 frontmatter 0 变更

**回退方式**:`git revert <commit-hash>`(单 commit 一次性回退)

**预期产出文件**(任务工作目录):
- `code/REQ-00002-001/RESULT.md`(改修总结)
- `code/REQ-00002-001/work-log.md`(实施日志)

---

### 2.2 `REQ-00002-002` — 同步 27 模板

**目标**:把 27 个模板文件中的占位符与示例值全部更新为新格式。

**涉及文件**(27 个,见 §3.2 详细设计):
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

**关键变更**(基于初步 Grep):
- 强命中文件:`code-design/templates/assistants-layout.md` / `code-require/templates/assistants-layout.md` / `code-plan/templates/assistants-layout.md` / `code-version/templates/assistants-layout.md` / `code-version/templates/version-RESULT.md` / `code-it/templates/assistants-layout.md` / `code-unit/templates/assistants-layout.md` / `code-require/templates/requirements.md` / `code-fix/templates/bug.md`
- 弱命中文件:`Read` 后逐文件确认

**操作步骤**:同 T-1
- 单独 commit 1 次:
  - `git add plugins/code-skills/skills/*/templates/`
  - `git commit -m "chore(encoding): sync 27 templates to new REQ/BUG/TASK format"`

**边界与异常**:同 T-1

**验证手段**:同 T-1
- `Grep "REQ-\d{4}-\d{4}" plugins/code-skills/skills/*/templates/` → 0 命中
- `Grep "BUG-\d{3}\b" plugins/code-skills/skills/*/templates/` → 0 命中

**回退方式**:`git revert <commit-hash>`

**预期产出文件**:
- `code/REQ-00002-002/RESULT.md`
- `code/REQ-00002-002/work-log.md`

---

### 2.3 `REQ-00002-003` — 同步中英 README

**目标**:把 `README.md` + `README.en.md` 中所有旧格式示例更新为新格式,**中英同次 commit**。

**涉及文件**:
- `plugins/code-skills/README.md`
- `plugins/code-skills/README.en.md`

**关键变更**(基于初步 Grep):
- README.md:20 处命中(具体行号见 §3.3)
- README.en.md:20 处命中(同结构)

**操作步骤**:
1. 对每个 README:
   a. `Read` 全文
   b. 逐处 `Edit` 替换
2. 中英同次 commit:
   - `git add plugins/code-skills/README.md plugins/code-skills/README.en.md`
   - `git commit -m "chore(encoding): sync README.md + README.en.md to new format (doc-conventions §规则 1)"`

**边界与异常**:
- 中英结构对仗漂移(一边改了,另一边漏改) → `git diff --stat` 对比两侧变更行数,差异 ≤ 1

**验证手段**:
- `Grep "REQ-\d{4}-\d{4}" plugins/code-skills/README.md` → 0 命中
- `Grep "REQ-\d{4}-\d{4}" plugins/code-skills/README.en.md` → 0 命中
- `git diff --stat` 两侧变更行数差异 ≤ 1

**回退方式**:`git revert <commit-hash>`

**预期产出文件**:
- `code/REQ-00002-003/RESULT.md`
- `code/REQ-00002-003/work-log.md`

---

### 2.4 `REQ-00002-004` — 核查 CLAUDE.md(预期 0 变更)

**目标**:验证 CLAUDE.md 是否含旧格式引用;若 0 命中,记录"已核查"。

**涉及文件**:`plugins/code-skills/CLAUDE.md`(预期 0 变更)

**操作步骤**:
1. `Grep "REQ-\d{4}-\d{4}" plugins/code-skills/CLAUDE.md` → 预期 0 命中
2. 若 0 命中:在 `code/REQ-00002-004/RESULT.md` 记录"已核查,无需修改"
3. 若命中:按 FR-5 同步,逐处 `Edit` 替换
4. 完成后:不主动 add 该文件到 commit(默认 0 变更)

**边界与异常**:
- CLAUDE.md 含 marketplace name 引用(超出 REQU M-7 预期) → 按 FR-5 同步

**验证手段**:1-2 个 Grep 验证(各 0 命中 或 已记录)

**回退方式**:若有变更,`git checkout plugins/code-skills/CLAUDE.md`

**预期产出文件**:
- `code/REQ-00002-004/RESULT.md`
- `code/REQ-00002-004/work-log.md`

**特殊说明**:本任务**无 commit**(除非 0 命中改为有变更)

---

### 2.5 `REQ-00002-005` — 创建 encoding-conventions.md

**目标**:在 `./assistants/rules/` 下创建 `encoding-conventions.md`,定义编码格式。

**涉及文件**:`assistants/rules/encoding-conventions.md`(新建)

**关键内容**(6 段):
1. 适用场景
2. 规范 1:编码格式定义(REQ/BUG/TASK 三类,正则与示例)
3. 规范 2:5 位纯数字格式约束
4. 规范 3:嵌套式 TASK 编码规则(Q-7 + Q-12)
5. 规范 4:实施流程
6. 来源(由 code-it 在 REQ-00002 创建,后续由 code-rule 维护)

**操作步骤**:
1. `Write assistants/rules/encoding-conventions.md` — 写入完整内容
2. `Read` 全文验证格式
3. 单独 commit 1 次:
   - `git add assistants/rules/encoding-conventions.md`
   - `git commit -m "chore(rules): add encoding-conventions.md (REQ-00002 FR-7)"`

**边界与异常**:
- 与既有规范文件内容冲突 → 重新审视并调整
- "创建"动作 vs "修改"既有约束 → **不违反**(本设计 D-PLAN-1 已澄清)

**验证手段**:
- `Read` 全文,逐条对照既有规范
- `Grep "REQ-\d{4}-\d{4}" assistants/rules/encoding-conventions.md` → 0 命中(新文件不应含旧示例)

**回退方式**:`git revert <commit-hash>`

**预期产出文件**:
- `code/REQ-00002-005/RESULT.md`
- `code/REQ-00002-005/work-log.md`
- `code/REQ-00002-005/deviations.md`(记录"code-it 创建新文件"作为用户授权的偏离)

**特殊说明**:本任务是本需求中**唯一**创建新文件的 2 个任务之一(T-5 + T-6)

---

### 2.6 `REQ-00002-006` — 创建 migration-mapping.md

**目标**:在 `./assistants/rules/` 下创建 `migration-mapping.md`,记录旧→新映射。

**涉及文件**:`assistants/rules/migration-mapping.md`(新建)

**关键内容**(4 段):
1. 适用场景
2. 映射表(旧→新 + 命中文件清单 + 处置)
3. 已知不完全映射(V0.0.0 EXISTING-*)
4. 维护说明

**操作步骤**:同 T-5
- 单独 commit:
  - `git commit -m "chore(rules): add migration-mapping.md (REQ-00002 FR-8)"`

**边界与异常**:同 T-5

**验证手段**:同 T-5

**回退方式**:同 T-5

**预期产出文件**:同 T-5(含 `deviations.md`)

---

### 2.7 `REQ-00002-007` — 全仓库 Grep + 偏差日志 + 不变量自检

**目标**:对全仓库执行穷举式 Grep 验证;13 条不变量自检;记录偏差。

**涉及文件**:**无项目文件修改**;产出:
- `code/REQ-00002-007/RESULT.md`
- `code/REQ-00002-007/work-log.md`
- `code/REQ-00002-007/deviations.md`

**操作步骤**:
1. **全仓库 Grep**:
   - `Grep "REQ-\d{4}-\d{4}" --glob="**/*.{md,json}" .`
   - 分类记录命中:本工作目录(V0.0.1 看板/工作文件,预期)/ V0.0.0 EXISTING-*(基线,预期)/ 5 个现有 rules/(若有,记 deviations)
2. **不变量自检**(INV-1 ~ INV-13):
   - 逐条执行,记录结果
3. **偏差日志**:
   - 已知偏离 1:`doc-conventions.md:113` install 命令旧串(规则文件不可改,留给 code-rule)
   - 已知偏离 2:V0.0.0 EXISTING-* 基线历史(范围外)
   - 已知偏离 3:5 个现有 rules/ 文件的旧串示例(范围外)
   - 已知偏离 4:本工作目录历史文件保留旧串(版本演进)
4. **无 commit**(5 个 commit 已由 T-1 / T-2 / T-3 / T-5 / T-6 完成;T-004 / T-007 无 commit 符合预期)

**边界与异常**:
- Grep 命中超出预期 → 偏差日志记录
- 工作文件被误改 → code-review 兜底

**验证手段**:
- 1 次全仓库 Grep
- 13 条不变量自检
- 1 次 `git log --oneline -7` 整体审阅

**回退方式**:不适用(本任务无 commit)

**预期产出文件**:
- `code/REQ-00002-007/RESULT.md`(含 13 不变量自检表)
- `code/REQ-00002-007/work-log.md`
- `code/REQ-00002-007/deviations.md`(含 4 条已知偏离)

---

### 2.8 `REQ-00002-008` — 同步版本看板

**目标**:把本计划 + 7 任务实施结果同步到版本看板。

**涉及文件**:
- `assistants/V0.0.1/RESULT.md`
- `assistants/V0.0.1/plan/REQ-00002/PLAN.md`(本文件,本任务收尾时填完成时间)

**关键变更**(看板 6 区段):
- 文档头"最近更新" → 20:55
- 当前里程碑 → M2 编码格式统一落地
- 详细设计与任务计划汇总 → 新增 REQ-00002 计划条目
- 任务清单 → 新增 8 行(REQ-00002-001 ~ 008)
- 里程碑 → M2 状态=已完成
- 变更记录 → 追加 9 条(本设计 + 8 任务)
- 执行的开发命令记录 → 追加 7+ 条
- 索引 → 新增 7 个 code/ 链接

**操作步骤**:
1. `Read assistants/V0.0.1/RESULT.md` 全文
2. 定位 6 区段
3. 逐区段 `Edit` 更新
4. 同步本 `PLAN.md` 中 8 任务的状态字段
5. 单独 commit 1 次:
   - `git add assistants/V0.0.1/RESULT.md assistants/V0.0.1/plan/REQ-00002/PLAN.md`
   - `git commit -m "chore(dashboard): sync V0.0.1 dashboard for REQ-00002 (8 tasks complete)"`

**边界与异常**:
- 看板既有区段被破坏 → 完整 `Read` 后逐处恢复
- 看板同步遗漏 → code-review 兜底

**验证手段**:
- `Read` 看板全文,确认 6 区段均已更新
- 看板"任务清单"中 8 行均显示"已完成 / 不适用"
- 看板"里程碑"中 M2 状态=已完成

**回退方式**:`git revert <commit-hash>`

**预期产出文件**:
- `code/REQ-00002-008/RESULT.md`
- `code/REQ-00002-008/work-log.md`

---

## 3. 任务依赖图

```
[T-1: 同步 10 SKILL.md]
            │
            ▼
[T-2: 同步 27 模板]
            │
            ▼
[T-3: 同步中英 README]   [T-4: 核查 CLAUDE.md(0 变更)]
            │                       │
            ├───────────────────────┤
            ▼                       ▼
[T-5: 创建 encoding-conventions.md]   │
            │                          │
            ▼                          │
[T-6: 创建 migration-mapping.md]       │
            │                          │
            ├──────────────────────────┘
            ▼
[T-7: 全仓库 Grep + 13 不变量自检 + deviations]
            │
            ▼
[T-8: 同步版本看板]
            │
            ▼
[本需求全部 8 任务完成,M2 达成]
```

**说明**:
- T-1 → T-2:逻辑依赖(SKILL.md 先改,模板再引用新格式)
- T-2 → T-3:逻辑依赖(同 T-1)
- T-1 ~ T-4 → T-5:逻辑依赖(新规范引用新格式定义)
- T-5 → T-6:逻辑依赖(迁移映射基于编码定义)
- T-1 ~ T-6 → T-7:强依赖(全仓库 Grep 必须等所有"写"任务完成)
- T-7 → T-8:强依赖(看板反映最终状态)
- T-3 与 T-4 可并行(均依赖 T-2,但 T-4 预期 0 变更)

---

## 4. 里程碑

| 里程碑 | 包含任务 | 完成定义 | 状态 | 计划时间 |
| --- | --- | --- | --- | --- |
| M2:编码格式统一落地 | T-1 ~ T-8 | 8 任务开发=已完成 ∧ 5 个 commit 已 push(2 任务无 commit 符合预期 T-004 / T-007) | 已完成 | 2026-06-03 |

---

## 5. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-03 20:55 | v1 | 计划新增 | 完成首次详细设计与编码计划:8 个任务(`REQ-00002-001` ~ `008`),多 commit 粒度按文件类型;继承概要设计 8 决策 + 11 不变量 + 本设计新增 2 不变量(INV-12/13)+ 本设计 D-PLAN-1(`code-it` 创建新规范文件,授权);Q-1 ~ Q-12 全部采纳 REQU 文档默认;无新增依赖,无偏离规范;task 编号沿用旧格式便于内部追踪,新需求起生效新 TASK 编码 | wangmiao |
| 2026-06-04 09:50 | v1.1 | 状态更新 | `REQ-00002-001` 状态"待开始"→"已完成",提交 `8ac1c9a`(5 SKILL.md 改正文,31+/31-;frontmatter 完整保留) | wangmiao |
| 2026-06-04 10:05 | v1.2 | 状态更新 | `REQ-00002-002` 状态"待开始"→"已完成",提交 `3df8ae7`(11 templates 改正文占位符/示例值,40+/40-;实际改 11/27,16 个 0 命中无需改) | wangmiao |
| 2026-06-04 10:00 | v1.3 | 状态更新 | `REQ-00002-003` 状态"待开始"→"已完成",提交 `31d6221`(2 README 改正文示例,72+/72-;中英严格对仗,`doc-conventions §规则 1` 严格遵循) | wangmiao |
| 2026-06-04 10:00 | v1.4 | 状态更新 | `REQ-00002-004` 状态"待开始"→"已完成"(核查 0 命中,无 commit;符合 PLAN §2.4 预期) | wangmiao |
| 2026-06-04 10:05 | v1.5 | 状态更新 | `REQ-00002-005` 状态"待开始"→"已完成",提交 `b092dec`(新建 `encoding-conventions.md` 212 行;4 规则权威源;`code-it` 创建新文件由 D-PLAN-1 授权) | wangmiao |
| 2026-06-04 10:08 | v1.6 | 状态更新 | `REQ-00002-006` 状态"待开始"→"已完成",提交 `5121e3f`(新建 `migration-mapping.md` 230 行;5 规则;22 条映射数据;`code-it` 创建新文件由 D-PLAN-1 授权) | wangmiao |
| 2026-06-04 10:15 | v1.7 | 状态更新 | `REQ-00002-007` 状态"待开始"→"已完成"(13/13 不变量自检通过;全仓库 0 命中;2 项 PLAN 推断与实际不符已记录;无 commit) | wangmiao |
| 2026-06-04 10:20 | v1.8 | 状态更新 | `REQ-00002-008` 状态"待开始"→"已完成"(M2 全部 8 任务完成;看板 6 区段同步;M2 状态"待开始"→"已完成";commit `a24663d`) | wangmiao |
| 2026-06-04 10:40 | v2 | 增量更新(审查) | REQ-00002 评审发现 3 项问题:1 项派生任务 T-009(建议改,PLAN.md 状态字段漏更新 + M2 描述与实际 commit 数不一致),2 项记入 findings-no-task.md(F-2 描述修正 + F-3 文件结构验证)。计划版本 v1.8 → v2。 | wangmiao |
| 2026-06-04 12:40 | v2.1 | 状态推进 | T-009 完成(3 个核心 Edit + 1 自身状态,合理范围收缩):PLAN.md:25 T-007 字段回填 + 行 288 "7 commit"→"5 commit + 任务清单" + 行 396 M2 完成定义 + 状态对齐;F-2 review 标的 V0.0.1/RESULT.md:41 实际已被 T-008 修正,本任务不再重复(见 deviations.md 偏离 1);无 commit(留 dirty tree 给用户);F-4 + F-5 派生任务 2/2 已处理;M2 真正可发布 8/8 已达成 | wangmiao |
