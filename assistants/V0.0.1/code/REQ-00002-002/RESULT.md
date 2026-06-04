# RESULT — REQ-00002-002(同步 27 模板)

- 任务编码:`REQ-00002-002`
- 任务标题:同步 27 模板(改正文占位符 + 示例值)
- 类型:修改
- 触发/来源:需求新增
- 来源 PLAN.md:`./assistants/V0.0.1/plan/REQ-00002/PLAN.md` §2.2
- 任务编码版本:v1
- 状态:**已完成**
- 责任人:wangmiao
- 开始时间:2026-06-04 09:55
- 完成时间:2026-06-04 10:05

---

## 1. 改修内容总览

把 `plugins/code-skills/skills/*/templates/` 下所有模板的"占位符"和"示例值"同步为新格式。**PLAN §2.2 列 27 个 templates;经初步 Grep 验证,实际 11 个含旧格式,16 个 0 命中**(PLAN 自身已注明"弱命中 Read 后逐文件确认")。

## 2. 涉及文件(实际改 11 个)

| # | 文件 | 改动 |
| --- | --- | --- |
| 1 | `code-design/templates/assistants-layout.md` | 4 处 REQ 目录示例 |
| 2 | `code-fix/templates/assistants-layout.md` | 2 处 BUG 目录示例 + 2 处 BUG-NNN 描述 |
| 3 | `code-fix/templates/bug.md` | 1 处 REQ 关联需求示例 |
| 4 | `code-fix/templates/fix-registry.md` | 2 处 BUG 缺陷登记 + 6 处 BUG 变更日志 |
| 5 | `code-it/templates/assistants-layout.md` | 1 处 TASK 格式说明 |
| 6 | `code-plan/templates/assistants-layout.md` | 3 处 REQ 目录示例 + 1 处 TASK 格式说明 |
| 7 | `code-require/templates/assistants-layout.md` | 3 处 REQ 目录示例 |
| 8 | `code-require/templates/requirements.md` | 1 处 REQ-2025-0099 → REQ-00510 追溯 |
| 9 | `code-unit/templates/assistants-layout.md` | 1 处 TASK 格式说明 |
| 10 | `code-version/templates/assistants-layout.md` | 5 处 REQ 目录 + 2 处 TASK 目录 |
| 11 | `code-version/templates/version-RESULT.md` | 4 处 REQ 变更日志 + 1 处 BUG 缺陷清单 |

## 3. 详细改动

### 3.1 `code-design/templates/assistants-layout.md`
- L23:目录示例 `REQ-2026-0001/` → `REQ-00001/`
- L27:目录示例 `REQ-2026-0001/` → `REQ-00001/`
- L36:目录示例 `REQ-2026-0002/` → `REQ-00002/`
- L38:目录示例 `REQ-2025-0099/` → `REQ-00510/`

### 3.2 `code-fix/templates/assistants-layout.md`
- L12:BUG 目录示例 `BUG-001/` → `BUG-00001/`
- L20:BUG 目录示例 `BUG-002/` → `BUG-00002/`
- L30:BUG 调用说明 `code-plan <BUG-NNN>` → `code-plan <BUG-NNNNN>`
- L34:文件名约定 `BUG-NNN` 三位数字 → `BUG-NNNNN` 五位数字

### 3.3 `code-fix/templates/bug.md`
- L128:BUG 模板占位符 `REQ-2026-0001` → `REQ-00001`

### 3.4 `code-fix/templates/fix-registry.md`
- L24:缺陷登记 `BUG-001` → `BUG-00001`(+链接同步)
- L25:缺陷登记 `BUG-002` → `BUG-00002`(+链接同步)
- L86-91:变更日志 6 处 `BUG-001/002` → `BUG-00001/00002`

### 3.5 `code-it/templates/assistants-layout.md`
- L62:任务编码格式 `<需求编号>-<任务序号>` → `TASK-(REQ|BUG)-NNNNN-NNNNN`

### 3.6 `code-plan/templates/assistants-layout.md`
- L21, L25, L29:目录示例 `REQ-2026-0001/` → `REQ-00001/`
- L62:任务编号规范格式更新 + 5 位补零

### 3.7 `code-require/templates/assistants-layout.md`
- L17:目录示例 `REQ-2026-0001/` → `REQ-00001/`
- L29:目录示例 `REQ-2026-0002/` → `REQ-00002/`
- L31:目录示例 `REQ-2025-0099/` → `REQ-00510/`

### 3.8 `code-require/templates/requirements.md`
- L141:关联需求行 `REQ-2025-0099` → `REQ-00510` + 链接同步

### 3.9 `code-unit/templates/assistants-layout.md`
- L54:任务编码格式更新

### 3.10 `code-version/templates/assistants-layout.md`
- L23, L27, L31:目录示例 3 处 `REQ-2026-0001/` → `REQ-00001/`
- L36, L40:目录示例 2 处 `REQ-2026-0001-001/` → `TASK-REQ-00001-00001/`
- L44:目录示例 `REQ-2026-0001/` → `REQ-00001/`
- L47:目录示例 `REQ-2026-0001-005/` → `TASK-REQ-00001-00005/`

### 3.11 `code-version/templates/version-RESULT.md`
- L121:BUG 缺陷清单占位符 `BUG-001` → `BUG-00001`;关联任务列 `REQ-YYYY-NNNN-XXX` → `TASK-REQ-00001-00001`
- L170-173:变更日志 4 处 `REQ-2026-0001/REQ-2026-0001-001/REQ-2026-0001-005` → `REQ-00001/TASK-REQ-00001-00001/TASK-REQ-00001-00005`

## 4. 关键决策与权衡

- **决策 D-IT-002-1**:仅改 11 个命中文件(其余 16 个 templates 0 命中,不改)
  - **依据**:PLAN §2.2 "弱命中文件:Read 后逐文件确认"
  - **实际**:经初步 Grep 验证,16 个 templates 完全 0 命中(无 `REQ-\d{4}-\d{4}` 也无 `BUG-\d{3}\b`)
- **决策 D-IT-002-2**:`REQ-2025-0099` 追溯为 `REQ-00510`
  - **依据**:PLAN §2.2 强命中表 + REQU FR-1 锁定
  - **影响**:2 处目录链接 + 1 处关联需求表格同步更新
- **决策 D-IT-002-3**:`code-version/templates/assistants-layout.md` 中 `REQ-2026-0001-001/` 改为 `TASK-REQ-00001-00001/`
  - **依据**:REQU FR-1 G4 新嵌套式(2026-06-03 20:18 锁定)
  - **影响**:5 个 SKILL.md + 多个 templates 中所有"任务目录示例"统一为新格式
- **决策 D-IT-002-4**:`code-fix/templates/assistants-layout.md` 中 BUG 文件名约定扩展
  - **依据**:REQU FR-1 `BUG-NNNNN` 5 位
  - **影响**:BUG 目录示例 + BUG 描述文本同步

## 5. 偏离设计/规范的地方

**无**。所有改动严格遵循 PLAN.md §2.2 + REQU §FR-1/FR-2 编码映射表。

仅 1 项范围微调:实际改 11 个(PLAN 列 27 范围,但 16 个 0 命中,PLAN 自身已允许)。详见 `deviations.md` 偏离 1。

## 6. 验证结果

| 验证项 | 结果 |
| --- | --- |
| `Grep "REQ-\d{4}-\d{4}" plugins/code-skills/skills/*/templates/` | 0 命中 ✅ |
| `Grep "BUG-\d{3}\b" plugins/code-skills/skills/*/templates/` | 0 命中 ✅ |
| `git diff --stat` | 11 files changed, 40 insertions(+), 40 deletions(-) ✅ |
| 模板无 frontmatter(纯 Markdown),无需 frontmatter 验证 | N/A |

详见 `compile-and-run.md` + `test-results.md`。

## 7. 已知问题/未完成项

- **无**。本任务范围内已全部完成。
- **范围外事项**(留给 T-003~T-008):中英 README、CLAUDE.md 核查、encoding-conventions.md 新建、migration-mapping.md 新建、看板同步、审计。

## 8. 关联任务与提交

- 关联任务:`REQ-00002-001`(已完成,T-002 的前置)
- 下游任务:`REQ-00002-003`(同步中英 README)
- 提交哈希:`3df8ae7`

## 9. 提交计划

```bash
git add plugins/code-skills/skills/code-design/templates/ \
        plugins/code-skills/skills/code-fix/templates/ \
        plugins/code-skills/skills/code-it/templates/ \
        plugins/code-skills/skills/code-plan/templates/ \
        plugins/code-skills/skills/code-require/templates/ \
        plugins/code-skills/skills/code-unit/templates/ \
        plugins/code-skills/skills/code-version/templates/

git commit -m "chore(encoding): sync 11 templates to new REQ/BUG/TASK format

- code-design/assistants-layout: REQ-NNNNN directory examples
- code-fix/{assistants-layout,bug,fix-registry}: BUG-NNNNN + REQ-NNNNN
- code-it/assistants-layout: TASK-REQ/BUG-NNNNN-NNNNN
- code-plan/assistants-layout: REQ-NNNNN + TASK-REQ-NNNNN-NNNNN
- code-require/{assistants-layout,requirements}: REQ-NNNNN + REQ-00510
- code-unit/assistants-layout: TASK-REQ-NNNNN-NNNNN
- code-version/{assistants-layout,version-RESULT}: REQ-NNNNN + TASK-REQ-NNNNN-NNNNN + BUG-NNNNN

11 files changed, 40 insertions(+), 40 deletions(-)。
PLAN §2.2 列 27 个 templates 范围(强+弱命中),实际 16 个 0 命中无需改,11 个有命中已改。
REQ-00002 FR-1 + FR-2 落地(部分,含 templates)。
"
```

## 10. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 |
| --- | --- | --- | --- |
| 2026-06-04 10:05 | v1 | 改修完成 | 11 个 templates 改正文占位符/示例值(40+/40-);无 frontmatter 受影响;无偏离设计;仅范围微调(11/27) |
