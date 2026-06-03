# 材料登记 — REQ-00002
更新时间:2026-06-03 20:55
版本:V0.0.1

## 项目级规范(5 个)

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `./assistants/rules/architecture.md` | — | **不存在**(本仓库尚未建立) |
| `./assistants/rules/module-conventions.md` | — | **不存在**(本仓库尚未建立) |
| `./assistants/rules/api-standards.md` | — | **不存在**(本仓库尚未建立) |
| `./assistants/rules/data-modeling.md` | — | **不存在**(本仓库尚未建立) |
| `./assistants/rules/dashboard-conventions.md` | 看板/仪表盘 | 看板字段约定、版本号写法(详见本表脚注) |
| `./assistants/rules/doc-conventions.md` | 文档 | README 多语言对仗(规则 1)+ 仓库级使用说明文档(规则 2)+ 强制级别逐条标注 |
| `./assistants/rules/marketplace-protocol.md` | marketplace | `marketplace.json` 与 `plugin.json` 协议约束 |
| `./assistants/rules/skill-conventions.md` | 技能 | `SKILL.md` frontmatter 必含 `name` + `description` 且 `name` 与目录名一致(规则 1) |

**Glob 实际命中**(5 个文件):
- `dashboard-conventions.md` / `doc-conventions.md` / `marketplace-protocol.md` / `module-conventions.md` / `skill-conventions.md`

> 注:Glob 命中 5 个,本表补 8 行说明(Glob 路径含子目录)。`architecture/api-standards/data-modeling` 三类规范**本仓库未建立**,本详细设计不依赖这三类。

**规范关键约束(直接影响本需求的子集)**:
- `doc-conventions.md §规则 1`:README 多语言版本必须保持结构对仗,同次提交 → 本次需在同一次 commit 中同步中英 README
- `doc-conventions.md §规则 2`:README 中提到的命令/目录名/配置项必须与仓库实际状态一致 → 本次需更新 `code-skills@code-skills` 之外,还要按新格式更新示例编码
- `skill-conventions.md §规则 1`:`SKILL.md` frontmatter 必含 `name`+`description` 且 `name` 与目录名一致 → 本次**不修改 frontmatter**;只改正文中示例编码(本规则边界)
- `dashboard-conventions.md`:看板字段约定扩展(待 `code-rule` 跟进)
- `marketplace-protocol.md`:不动 `marketplace.json` / `plugin.json`(本需求 FR-10 明确边界)

## 上游需求

- 来源:`./assistants/V0.0.1/require/REQ-00002/RESULT.md`
- 版本:v3(2026-06-03 20:18,v3 反映 FR-6 部分提前落地)
- 提取:10 FR / 7 NFR / 11 AC
- 5 项待澄清(Q-6/Q-8/Q-9/Q-10/Q-12) + 1 项已锁定(Q-7 G4 新嵌套式)
- FR-6 部分提前落地:目录 `assistants/V0.0.1/require/REQ-2026-0001/` → `REQ-00001/` 已完成(2026-06-03 20:20);**未触及**:SKILL.md / 模板 / README / CLAUDE.md / V0.0.0 EXISTING-*(由本需求 `code-it` 阶段统一清理)

**关键交叉点**(每条 FR → 本详细设计章节):

| FR | 摘要 | 本设计章节 |
| --- | --- | --- |
| FR-1 | 5 位纯数字格式 `REQ-NNNNN` / `TASK-REQ-<父级>-NNNNN` / `TASK-BUG-<父级>-NNNNN` | §1.2 数据结构 |
| FR-2 | 同步 10 个 SKILL.md(只改正文,不改 frontmatter) | §3.1 模块 T-1 |
| FR-3 | 同步 20+ 模板(占位符 + 示例值) | §3.2 模块 T-2 |
| FR-4 | 同步中英 README | §3.3 模块 T-3 |
| FR-5 | 同步 CLAUDE.md | §3.4 模块 T-4 |
| FR-6 | REQ-2026-0001 → REQ-00001 重命名(部分已落地) | §3.5 模块 T-5 |
| FR-7 | (Q-8=a 默认)新建 `encoding-conventions.md` 规范文件 | §3.6 模块 T-6 |
| FR-8 | (Q-9=a 默认)新建 `migration-mapping.md` 迁移映射 | §3.7 模块 T-7 |
| FR-9 | 同步看板文件 RESULT.md / PLAN.md(本设计 + 实施) | §3.8 模块 T-8 |
| FR-10 | 不修改 `marketplace.json` / `plugin.json` / 9 个非本需求 SKILL.md frontmatter | 不变量 §5 |

## 上游概要设计

- 来源:`./assistants/V0.0.1/design/REQ-00002/RESULT.md`
- 版本:v1(2026-06-03 20:25)
- 8 项设计决策 + 11 个子任务预想 + 11 条不变量
- 11 子任务预想清单(本详细设计在 §3 落地为编码计划任务):

| 设计预想编号 | 标题 | 落地为 PLAN 任务 |
| --- | --- | --- |
| 子任务 1 | 同步 10 个 SKILL.md | TASK-REQ-00002-00001 |
| 子任务 2 | 同步 20+ 模板 | TASK-REQ-00002-00002 |
| 子任务 3 | 同步中英 README | TASK-REQ-00002-00003 |
| 子任务 4 | 同步 CLAUDE.md | TASK-REQ-00002-00004(预 0 变更) |
| 子任务 5 | 同步 version-RESULT.md 模板 | 包含在 TASK-REQ-00002-00002 |
| 子任务 9 | (Q-8=a)创建 `encoding-conventions.md` | TASK-REQ-00002-00005 |
| 子任务 10 | (Q-9=a)创建 `migration-mapping.md` | TASK-REQ-00002-00006 |
| 子任务 11 | 全仓库穷举式 Grep 验证 | TASK-REQ-00002-00007 |

> 详细设计阶段将设计预想的"11 子任务"进一步细化为 7 个 `code-it` 任务(更高效)

## 项目现状(实现细节)

### 文件命中清单(本需求修改对象)

#### A. SKILL.md(10 个,均**只改正文**,不改 frontmatter)

| 文件路径 | 旧格式出现次数(估算) | 类型 |
| --- | --- | --- |
| `plugins/code-skills/skills/code-design/SKILL.md` | 0(快速 Grep 验证) | 正文 |
| `plugins/code-skills/skills/code-fix/SKILL.md` | 0(快速 Grep 验证) | 正文 |
| `plugins/code-skills/skills/code-init/SKILL.md` | 0(快速 Grep 验证) | 正文 |
| `plugins/code-skills/skills/code-it/SKILL.md` | **≥ 2**(L4 / L107 命中) | 正文 |
| `plugins/code-skills/skills/code-plan/SKILL.md` | **≥ 2**(L4 / L197 命中) | 正文 |
| `plugins/code-skills/skills/code-require/SKILL.md` | **≥ 3**(L44 / L267 / L270 命中) | 正文 |
| `plugins/code-skills/skills/code-review/SKILL.md` | 0(快速 Grep 验证) | 正文 |
| `plugins/code-skills/skills/code-rule/SKILL.md` | 0(快速 Grep 验证) | 正文 |
| `plugins/code-skills/skills/code-unit/SKILL.md` | **≥ 1**(L103 命中) | 正文 |
| `plugins/code-skills/skills/code-version/SKILL.md` | 0(快速 Grep 验证) | 正文 |

> 注:以上"出现次数"为 `REQ-\d{4}-\d{4}` 模式命中数。实际还需 `Read` 每个文件后逐文件确认替换点。

#### B. 模板文件(27 个,**改正文占位符 + 示例值**)

| 技能 | 模板文件 | 旧格式命中数 |
| --- | --- | --- |
| code-design | `templates/assistants-layout.md` | **3+** |
| code-design | `templates/design.md` | 0(快速 Grep 验证) |
| code-fix | `templates/assistants-layout.md` | 0 |
| code-fix | `templates/bug.md` | **1+** |
| code-fix | `templates/fix-registry.md` | 0 |
| code-init | `templates/assistants-layout.md` | 0 |
| code-init | `templates/INIT-REPORT.md` | 0 |
| code-init | `templates/existing-requirement.md` | 0 |
| code-it | `templates/RESULT.md` | 0 |
| code-it | `templates/assistants-layout.md` | **1+** |
| code-plan | `templates/assistants-layout.md` | **3+** |
| code-plan | `templates/fix-plan.md` | 0 |
| code-plan | `templates/plan.md` | 0 |
| code-plan | `templates/task-plan.md` | 0 |
| code-require | `templates/assistants-layout.md` | **3+** |
| code-require | `templates/requirements.md` | **1+** |
| code-review | `templates/REVIEW-FIX.md` | 0 |
| code-review | `templates/assistants-layout.md` | 0 |
| code-review | `templates/REVIEW-REPORT.md` | 0 |
| code-rule | `templates/assistants-layout.md` | 0 |
| code-rule | `templates/rule.md` | 0 |
| code-unit | `templates/assistants-layout.md` | **1+** |
| code-unit | `templates/RESULT.md` | 0 |
| code-unit | `templates/test-spec.md` | 0 |
| code-version | `templates/assistants-layout.md` | **8+** |
| code-version | `templates/version-RESULT.md` | **4+** |

#### C. 顶层文档(2 个,中英同次提交)

| 文件路径 | 旧格式命中数 |
| --- | --- |
| `plugins/code-skills/README.md` | **14+** |
| `plugins/code-skills/README.en.md` | **14+** |

#### D. CLAUDE.md(预期 0 变更)

- `plugins/code-skills/CLAUDE.md`:Grep 命中 0 → 预期 0 变更

#### E. 范围外(本需求不修改,记入 `code/REQ-00002-NNN/deviations.md`)

- `./assistants/V0.0.0/require/EXISTING-00[4-8]/*.md`(V0.0.0 基线历史,**基线完整性原则**不修改)
- `./assistants/V0.0.1/require/REQ-00001/*` + `design/REQ-00001/*` + `plan/REQ-00001/*` + `code/REQ-00001-001~004/*`(历史工作文件,保留旧串作为版本历史)

#### F. 范围外(本需求严禁修改)

- `.claude-plugin/marketplace.json` — FR-10 边界
- `plugins/code-skills/.claude-plugin/plugin.json` — FR-10 边界
- 10 个 SKILL.md 的 YAML frontmatter — skill-conventions §规则 1 边界
- 5 个 `assistants/rules/` 现有文件(可能含旧串但不允许本任务修改,留待 `code-rule` 跟进)

### 命名风格(已锁定)

- **REQ 编码**:`REQ-NNNNN`(5 位纯数字,左补零)
- **BUG 编码**:`BUG-NNNNN`(5 位纯数字,左补零)
- **TASK 编码**(Q-7 锁定 G4 新嵌套式):
  - 需求任务:`TASK-REQ-<父级编码>-NNNNN`(父级编码为数字段,如 `TASK-REQ-00001-00001`)
  - 缺陷任务:`TASK-BUG-<父级编码>-NNNNN`(父级编码为数字段,如 `TASK-BUG-00001-00001`)

> Q-12 已默认(a):需求编码"在 TASK 编码中**仅含数字段**,不重复 `REQ-` 前缀"

### 实施顺序(Q-11 待用户确认)

- REQU 默认(a):SKILL.md → 模板 → README/CLAUDE.md → 看板 → (条件)新规范文件 → (条件)迁移映射 → 全仓库 Grep
- design 默认(同 REQU a):**保持与 REQU 一致**

### 提交策略(继承自 REQ-00001 design D-4)

- **doc-conventions §规则 1** 强制:中英 README 同次 commit
- **本需求扩展**:所有 `code-*` 文档改动**单 commit** 落地(10 SKILL.md + 20+ 模板 + 2 README + 0 CLAUDE.md + 2 新规范文件 + 看板/工作文件)

## 本次变更源

| 变更源 | 检测方式 | 变化列表 |
| --- | --- | --- |
| 需求侧 | 上游 REQU v3 变更记录 | FR-6 部分提前落地(目录重命名完成) |
| 概要设计侧 | 上游 design v1 变更记录 | 8 项决策、11 子任务预想、11 不变量 |
| 规范侧 | `./assistants/rules/` 对比 | 无变化(`code-rule` 调用) |
| 代码侧 | 重跑项目探索 | 已发现 27 模板 + 10 SKILL.md + 2 README + 1 CLAUDE.md 命中点 |

## 预检冲突(无)

- 规范 vs 需求冲突:**无**(`skill-conventions §规则 1` 不约束正文示例编码,只约束 frontmatter)
- 规范 vs 现状冲突:**无**(项目现状符合 doc-conventions 强制要求)
- 设计 vs 现状冲突:**无**(design v1 已适配本仓库结构)
