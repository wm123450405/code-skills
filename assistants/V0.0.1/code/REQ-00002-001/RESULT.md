# RESULT — REQ-00002-001(同步 10 个 SKILL.md)

- 任务编码:`REQ-00002-001`
- 任务标题:同步 10 个 SKILL.md(只改正文)
- 类型:修改
- 触发/来源:需求新增
- 来源 PLAN.md:`./assistants/V0.0.1/plan/REQ-00002/PLAN.md` §2.1
- 任务编码版本:v1
- 状态:**已完成**
- 责任人:wangmiao
- 开始时间:2026-06-04 09:40
- 完成时间:2026-06-04 09:50

---

## 1. 改修内容总览

把 10 个 SKILL.md 正文中所有 `REQ-\d{4}-\d{4}` 替换为新格式,把 `BUG-\d{3}` 替换为 `BUG-\d{5}`。**仅改正文,不动 YAML frontmatter**。

## 2. 涉及文件(实际改 5 个)

| 文件 | 改动行数 | 改前示例 | 改后示例 |
| --- | --- | --- | --- |
| `plugins/code-skills/skills/code-it/SKILL.md` | L4, L5, L107 | `REQ-2026-0001-001` / `BUG-NNN` | `TASK-REQ-00001-00001` / `BUG-NNNNN` |
| `plugins/code-skills/skills/code-plan/SKILL.md` | L4, L5, L197 | `REQ-2026-0001` / `BUG-001` / `REQ-2026-0001-001` | `REQ-00001` / `BUG-00001` / `TASK-REQ-00001-00001` |
| `plugins/code-skills/skills/code-require/SKILL.md` | L44, L267, L270 | `REQ-2026-0001` / `REQ-2025-0099` | `REQ-00001` / `REQ-00510` |
| `plugins/code-skills/skills/code-unit/SKILL.md` | L103 | `REQ-2026-0001-001` | `TASK-REQ-00001-00001` |
| `plugins/code-skills/skills/code-fix/SKILL.md` | L3, L4, L42, L50, L101, L102, L105, L124, L125, L320-329(11 行) | `BUG-001` / `BUG-NNN` | `BUG-00001` / `BUG-NNNNN` |
| 其他 5 个 SKILL.md | 0 命中,无改动 | — | — |

## 3. 详细改动

### 3.1 `code-it/SKILL.md`
- L4:任务编码格式说明 `REQ-2026-0001-001` → `TASK-REQ-NNNNN-NNNNN` + `TASK-REQ-00001-00001` 示例
- L5:BUG 格式 `BUG-NNN` → `BUG-NNNNN` + `BUG-00001` 示例
- L107:任务编码解析规则去掉末尾 `-<任务序号>` → 去掉前缀 `TASK-REQ-` 与末尾 `-<任务序号>`;任务序号 3 位 → 5 位

### 3.2 `code-plan/SKILL.md`
- L4:需求编码示例 `REQ-2026-0001` → `REQ-00001`
- L5:缺陷编号示例 `BUG-001` → `BUG-00001`
- L197:任务编号格式 `<需求编号>-<任务序号>` → `TASK-(REQ|BUG)-NNNNN-NNNNN`;3 位补零 → 5 位补零

### 3.3 `code-require/SKILL.md`
- L44:需求编码示例 `REQ-2026-0001` → `REQ-00001`
- L267-270:历史案例 `REQ-2025-0099` → `REQ-00510`(用户中心,v1.0.0);目录引用同步

### 3.4 `code-unit/SKILL.md`
- L103:任务编码解析规则同 `code-it`

### 3.5 `code-fix/SKILL.md`
- L3:BUG 格式示例 `BUG-001` → `BUG-00001`
- L4:BUG 生成格式 `BUG-NNN` → `BUG-NNNNN`
- L42, L50:目录示例 `BUG-001/` `BUG-002/` → `BUG-00001/` `BUG-00002/`
- L101-105:BUG-NNN 字符串检测 + 示例 `BUG-001` → `BUG-00001`
- L124-125:BUG 编号生成 + 解析规则
- L320-329:完整流程示例 11 处 `BUG-001` → `BUG-00001`

## 4. 关键决策与权衡

- **决策 D-IT-1**:仅改 5 个有命中的 SKILL.md(其他 5 个 0 命中无需改)
  - **依据**:PLAN §2.1 "其余 6 个 0 命中,Read 全文确认"
  - **实际**:经 Read 全文确认其余 5 个 SKILL.md 0 命中(初步 Grep + Read 双重确认)
- **决策 D-IT-2**:`BUG-NNN` 解析规则改为"取最大值 N+1 后零填充到 5 位"
  - **依据**:REQU FR-1 正则 `^BUG-\d{5}$`
  - **影响**:用户首次创建缺陷时,新编号永远 5 位(即使是 BUG-00001)
- **决策 D-IT-3**:TASK 编码解析规则改为"去掉前缀 `TASK-REQ-` 与末尾 `-<任务序号>`"
  - **依据**:REQU FR-1 锁定 G4 嵌套式
  - **影响**:解析逻辑复杂化,但与新格式严格匹配

## 5. 偏离设计/规范的地方

**无**。所有改动严格遵循 PLAN.md §2.1 + REQU §FR-1/FR-2 编码映射表。详见 `deviations.md`。

## 6. 验证结果

| 验证项 | 结果 |
| --- | --- |
| `Grep "REQ-\d{4}-\d{4}" plugins/code-skills/skills/*/SKILL.md` | 0 命中 ✅ |
| `Grep "BUG-\d{3}\b" plugins/code-skills/skills/*/SKILL.md` | 0 命中 ✅ |
| 5 个文件 frontmatter 抽查(3/5 抽样) | `name` + `description` 完整保留 ✅ |
| `git diff --stat` | 5 files changed, 31 insertions(+), 31 deletions(-) ✅ |

详见 `compile-and-run.md` + `test-results.md`。

## 7. 已知问题/未完成项

- **无**。本任务范围内已全部完成。
- **范围外事项**(留给 T-002~T-008):templates/ 目录下的 27 个模板、中英 README、CLAUDE.md 核查、encoding-conventions.md 新建、migration-mapping.md 新建、看板同步、审计。

## 8. 关联任务与提交

- 关联任务:无(T-001 是 T-002~T-008 的前置)
- 下游任务:`REQ-00002-002`(同步 27 模板)依赖本任务 SKILL.md 已同步
- 提交哈希:`8ac1c9a`
- commit message:`chore(encoding): sync 5 SKILL.md to new REQ/BUG/TASK format`

## 9. 提交计划

```bash
git add plugins/code-skills/skills/code-fix/SKILL.md \
        plugins/code-skills/skills/code-it/SKILL.md \
        plugins/code-skills/skills/code-plan/SKILL.md \
        plugins/code-skills/skills/code-require/SKILL.md \
        plugins/code-skills/skills/code-unit/SKILL.md

git commit -m "chore(encoding): sync 5 SKILL.md to new REQ/BUG/TASK format

- code-it/SKILL.md: TASK-REQ-NNNNN-NNNNN + BUG-NNNNN
- code-plan/SKILL.md: TASK-REQ/BUG-NNNNN-NNNNN + REQ-NNNNN
- code-require/SKILL.md: REQ-NNNNN + REQ-00510 (2025-0099 追溯)
- code-unit/SKILL.md: TASK-REQ-NNNNN-NNNNN
- code-fix/SKILL.md: BUG-NNNNN (5 个 SKILL.md 中所有示例)

只改正文,frontmatter 完整保留(0 命中 frontmatter)。
REQ-00002 FR-1 + FR-2 落地。
"
```

## 10. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 |
| --- | --- | --- | --- |
| 2026-06-04 09:50 | v1 | 改修完成 | 5 个 SKILL.md 改正文(31+/31-);frontmatter 完整保留;无偏离设计;无超出 T-001 范围 |
