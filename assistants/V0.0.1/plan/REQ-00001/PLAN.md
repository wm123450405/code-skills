# 编码计划 — REQ-00001(Marketplace 根名称添加 `-marketplace` 后缀)

- 需求编码:REQ-00001(原 REQ-2026-0001)
- 所属版本:V0.0.1
- 计划版本:v1
- 状态:已完成(首次计划)
- 责任人:wangmiao
- 创建:2026-06-03
- 最近更新:2026-06-03 20:30
- **上游**:`./assistants/V0.0.1/require/REQ-00001/RESULT.md` + `design/REQ-00001/RESULT.md`
- **下游**:`code-it REQ-00001-NN` 实施 / `code-review REQ-00001` 评审 / `code-unit` 测试(本需求不适用)

---

## 1. 任务总览

| 任务编号 | 标题 | 类型 | 触发/来源 | 开发状态 | 测试状态 | 涉及文件 | 完成时间 | 提交哈希 | 关联任务 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `REQ-00001-001` | 改 `.claude-plugin/marketplace.json` 根 name | 修改 | 需求新增 | 待开始 | 不适用 | `.claude-plugin/marketplace.json` | — | — | — |
| `REQ-00001-002` | 同步中英 README | 修改 | 需求新增 | 待开始 | 不适用 | `plugins/code-skills/README.md`, `README.en.md` | — | — | — |
| `REQ-00001-003` | 核查 `plugins/code-skills/CLAUDE.md` | 文档 | 需求新增 | 待开始 | 不适用 | `plugins/code-skills/CLAUDE.md`(预期 0 变更) | — | — | — |
| `REQ-00001-004` | 全仓库穷举式 Grep + 偏差日志 + 不变量自检 + commit | 文档 | 需求新增 | 待开始 | 不适用 | 无文件修改,产出 `code/REQ-00001-004/RESULT.md` | — | — | — |

**统计**:
- 总任务数:4
- 真正可发布数(开发=已完成 ∧ 测试∈{已运行-通过, 不适用}):待 code-it 推进
- 开发已完成 / 未完成:0 / 4
- 测试已通过 / 已失败 / 不适用 / 未编写:0 / 0 / 4 / 0(纯文档/字符串任务,全部不适用)

---

## 2. 任务详情

### 2.1 `REQ-00001-001` — 改 `.claude-plugin/marketplace.json` 根 name

**目标**:把根 `name` 字段从 `"code-skills"` 改为 `"code-skills-marketplace"`,其它字段**严禁**变动。

**涉及文件**:`.claude-plugin/marketplace.json`(1 个文件)

**关键变更**(精确到字段路径):
| 路径 | 改前 | 改后 |
| --- | --- | --- |
| `$.name` | `"code-skills"` | `"code-skills-marketplace"` |

**操作步骤**:
1. `Bash: git status` —— 确认 working tree clean
2. `Read .claude-plugin/marketplace.json` —— 全文核对,定位根 name 行
3. `Edit .claude-plugin/marketplace.json`:
   - `old_string`:`    "name": "code-skills",` (第 3 行,2 空格缩进,精确字面量)
   - `new_string`:`    "name": "code-skills-marketplace",`
4. `Read .claude-plugin/marketplace.json` —— 验证:根 name 已改,其它字段未变
5. `Grep "name" .claude-plugin/marketplace.json` —— 验证:`$.plugins[0].name` 与 `$.owner.name` 仍为 `code-skills`

**边界与异常**:
- 误改 `plugins[0].name` → Edit 前 Read 全文,确认 old_string 唯一
- 误删 `$schema` → 同上
- JSON 语法错 → Edit 后 Read 全文确认(Claude Code 加载时自动校验)

**验证手段**:
- `git diff .claude-plugin/marketplace.json` —— 应仅 1 行变更
- `Grep "name" .claude-plugin/marketplace.json` —— 字段逐项核对

**回退方式**:
- `git checkout .claude-plugin/marketplace.json`

---

### 2.2 `REQ-00001-002` — 同步中英 README

**目标**:把 `plugins/code-skills/README.md` 与 `README.en.md` 中所有 `code-skills@code-skills` 字符串与"marketplace name 是 `code-skills`"解释段同步更新为新 marketplace name。

**涉及文件**:
- `plugins/code-skills/README.md`
- `plugins/code-skills/README.en.md`

**关键变更**(精确到行号预期,以 Read 实际为准):
| 文件 | 行号(预期) | 改前 | 改后 |
| --- | --- | --- | --- |
| `README.md` | 14 | `` `claude plugin install code-skills@code-skills` `` | `` `claude plugin install code-skills@code-skills-marketplace` `` |
| `README.md` | 22 | `marketplace name 是 \`code-skills\`` | `marketplace name 是 \`code-skills-marketplace\`` |
| `README.en.md` | 14 | `claude plugin install code-skills@code-skills` | `claude plugin install code-skills@code-skills-marketplace` |
| `README.en.md` | 22 | `marketplace name \`code-skills\`` | `marketplace name \`code-skills-marketplace\`` |

**操作步骤**:
1. 对每个文件:
   a. `Read` 全文
   b. 定位改前字符串(可能多行,需用 `Grep` 确认)
   c. `Edit` 逐处替换
2. 验证:
   - `Grep "code-skills@code-skills" README.md` → 0 命中
   - `Grep "code-skills@code-skills" README.en.md` → 0 命中
   - `Grep "code-skills@code-skills-marketplace" README.md` → ≥ 1 命中
   - `Grep "code-skills@code-skills-marketplace" README.en.md` → ≥ 1 命中
3. 并列对照:两个文件 `git diff` 对比,确认修改项一一对应

**边界与异常**:
- 中英行号偏移(若用户已部分手改) → 实际行号以 Read 为准
- README 含其它"marketplace name"引用(如描述性段落) → Grep 全部命中后逐处替换
- 替换遗漏(中文版改了,英文版漏改) → code-review 并列 diff 兜底

**验证手段**:
- 4 处 Grep 验证(每个文件 × 2 个方向)
- 中英并列 diff 对照(由 `code-review` 阶段执行)

**回退方式**:
- `git checkout plugins/code-skills/README.md plugins/code-skills/README.en.md`

---

### 2.3 `REQ-00001-003` — 核查 `plugins/code-skills/CLAUDE.md`

**目标**:在 `code-it` 实施阶段验证 CLAUDE.md 是否含 marketplace name 字面量引用;若 0 命中,记录"已核查,无需修改";若命中,按 FR-5 同步。

**涉及文件**:`plugins/code-skills/CLAUDE.md`(预期 0 变更)

**操作步骤**:
1. `Grep "code-skills@code-skills" plugins/code-skills/CLAUDE.md` → 预期 0 命中
2. `Grep "marketplace name" plugins/code-skills/CLAUDE.md` → 预期 0 命中
3. 若 0 命中:在 `code/REQ-00001-003/RESULT.md` 工作日志记录"已核查,无需修改"
4. 若命中:按 FR-5 同步,逐处 Edit 替换,记录替换点
5. 完成后:不主动 add 该文件到 commit(默认 0 变更)

**边界与异常**:
- CLAUDE.md 含 marketplace name 引用(超出 REQU M-7 预期) → 按 FR-5 同步
- CLAUDE.md 含"marketplace 仓库根"等结构描述 → 不算"字面量引用",无需修改

**验证手段**:
- 2 个 Grep 验证(各 0 命中 或 已记录)

**回退方式**:
- 若 0 命中,无文件变更,无需回退
- 若有变更,`git checkout plugins/code-skills/CLAUDE.md`

---

### 2.4 `REQ-00001-004` — 全仓库穷举式 Grep + 偏差日志 + 不变量自检 + commit

**目标**:对全仓库执行穷举式 Grep 验证,确认无残留旧 marketplace name 引用(除历史工作文件);并对 11 条不变量逐条自检;最后做单 commit 提交。

**涉及文件**:无文件修改。产出:
- `code/REQ-00001-004/RESULT.md` —— 验证报告 + 偏差日志 + 不变量自检表

**操作步骤**:
1. **全仓库 Grep**:
   - `Grep "code-skills@code-skills" .` → 应仅命中本需求工作目录(`require/REQ-00001/*`、`design/REQ-00001/*`、`plan/REQ-00001/*`、`code/REQ-00001-NNN/*`)
   - `Grep "code-skills@code-skills" --include="*.md" --include="*.json"` 限定文件类型
2. **不变量自检**(11 条):
   - `Bash: ls plugins/` → 确认 `code-skills/` 目录名保持
   - `Bash: git remote -v` → 确认远端仓库名未重命名
   - `Read .claude-plugin/marketplace.json` → 字段逐项核对(根 name 已改;其它字段未变)
   - `Read plugins/code-skills/.claude-plugin/plugin.json` → 确认 `name: "code-skills"` 保持
   - `Bash: git diff --stat` → 确认变更范围仅限 3-4 文件(取决于 T-003)
   - 其它:见 `data-changes.md` 与 `risk-analysis.md`
3. **偏差日志**:
   - 任何超出预期的命中 → 记录到 `code/REQ-00001-004/RESULT.md` §偏差日志
   - 任何不变量违反 → 同上
4. **提交 commit**(T-001~T-003 完成后):
   - `git add .claude-plugin/marketplace.json plugins/code-skills/README.md plugins/code-skills/README.en.md`(T-003 默认 0 变更,不加)
   - `git commit -m "chore(marketplace): rename root name ..."`(见 RESULT.md §4.3)
   - `git push`

**边界与异常**:
- Grep 命中超出预期 → 偏差日志记录;若命中点是历史工作文件,记录"预期内"
- 工作文件被误改 → code-review 兜底

**验证手段**:
- 1 次全仓库 Grep
- 11 条不变量自检
- 1 次 `git diff --stat` 整体审阅
- 1 次 `git commit` 提交(继承 design D-4 单 commit 决策)

**回退方式**:
- `git revert HEAD` 1 个 commit 全部回退
- 或 `git reset --hard HEAD~1`(若 commit 尚未 push)

---

## 3. 任务依赖图

```
[REQ-00001-001: 改 marketplace.json]
            │
            ▼
[REQ-00001-002: 同步中英 README]
            │
            ├──────────────────┐
            ▼                  ▼
[REQ-00001-003: 核查 CLAUDE.md]   [REQ-00001-004: 全仓库 Grep + 不变量自检 + commit]
            │                           │
            └─────────┬─────────────────┘
                      ▼
              [本需求全部任务完成]
```

**说明**:
- T-001 → T-002:逻辑依赖(语义上 marketplace 根 name 先改,文档引用后才能正确)
- T-002 → T-003:逻辑依赖(README 是显式字面量引用,CLAUDE.md 可能是隐式)
- T-002 → T-004:逻辑依赖(全仓库 Grep 必须等所有"写"任务完成)
- T-003 → T-004:无强依赖,可并行;但 T-004 包含 commit 操作,需 T-003 完成确认 0 变更后再 add

---

## 4. 里程碑

| 里程碑 | 包含任务 | 完成定义 | 状态 | 计划时间 |
| --- | --- | --- | --- | --- |
| M1:Marketplace 改名落地 | T-001~T-004 | 4 任务开发=已完成 ∧ 1 个 commit 已 push | 待开始 | 2026-06-03 |

---

## 5. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-03 20:30 | v1 | 计划新增 | 完成首次详细设计与编码计划:4 个任务(`REQ-00001-001`~`004`),单 commit 提交;继承概要设计 7 决策 + 11 不变量 + 4 文件变更集;Q-3/Q-4/Q-5 采用 REQU 文档默认;无新增依赖,无偏离规范 | wangmiao |
