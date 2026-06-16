# 分析笔记 — REQ-00036

更新时间:2026-06-16 17:33

## 思考路径

### 1. 用户原始诉求解析

用户本次调 `code-require` 时的 ARGS 表面上是"需求分析",实际诉求是**"为清理动作本身登记需求,产出 RESULT.md,由 code-it 真正去清理 SKILL.md"**。这是 `code-require` 的合法用法(用户对清理动作的需求描述),所以走完整流程。

### 2. 关键范围决定(已与用户确认)

| 决定 | 选择 | 理由 |
| --- | --- | --- |
| 清理对象 | 所有 `code-*` 技能的 SKILL.md + 同目录 `templates/`(共 14 个技能目录) | 用户在澄清阶段确认 |
| `checklists/` / `guidelines/` | 不动 | 用户未提及,留作后续单独需求 |
| `assistants/` 工作空间 | 不动 | 这是历史工作产物,有史料价值,不是"开发痕迹" |
| 占位符(模板里的 `REQ-00001` / `BUG-00001`) | 保留 | 它们是模板示例,不是开发痕迹 |
| 已退场功能说明 | 清理 / 简化 | 用户确认 |
| 跨技能契约(章节引用、字段名、占位符映射) | 保留 | NFR-4 强约束 |
| Frontmatter(`name` / `description`) | 字节级保留 | NFR-2 强约束 |

### 3. 「开发痕迹」形态分类(下游 code-it 实施时使用)

共 6 类待清理痕迹:

1. **段落尾注型**(FR-1 覆盖):`(本需求 REQ-NNNNN FR-X 新增)` / `(本需求 REQ-NNNNN YYYY-MM-DD 起生效)` / `(本需求 BUG-NNNN 新增)` 等。
2. **历史回溯型**(FR-2 覆盖):`原 code-unit 步骤 X` / `沿用原 code-unit` / `原 fix-plan.md 退场` / `原 code-design 步骤 0b 4 问题 → 1 问题 → 0 问题` / `原 code-unit 退场前表述` / `本仓库主动产出 ... 原 X 位数字`。
3. **决策记录型**(FR-3 覆盖):`(Q-1 锁定 A)` / `(Q-P7 锁定)` / `(Q-2 采纳默认)` / `(Q-4 隐含答复 C)`。
4. **生效日型**(FR-4 覆盖):`YYYY-MM-DD 起生效` / `2026-06-15 起生效`。
5. **退场文件名型**(FR-5 覆盖):`fix-plan.md` / `fix-work-log.md` / `fix-compile-and-run.md` / `fix-test-results.md` 等已退场的过程文档名引用。
6. **杂项**(FR-6 覆盖):`变更人:<具体人名>` 等。

### 4. 「不变量」分类(必须保留)

| 不变量 | 例子 |
| --- | --- |
| YAML frontmatter (`name` / `description`) | NFR-2 字节级保留 |
| 跨技能契约(章节号、字段名、占位符映射) | NFR-4 |
| 模板占位符(示例性 `REQ-00001` / `BUG-00001`) | NFR-6 |
| 目录级引用(`<版本号>/plan/`、`<版本号>/code/` 等) | FR-5 主契约 |
| 跨版本规范继承引用(`encoding-conventions §规则 1`) | NFR-5 兼容 |
| 「步骤 0a 拉取」「步骤 N — 末尾兜底提交」等主流程小节标题 | NFR-3 章节结构 |
| 「不要做的事」类约束清单 | NFR-3 |

### 5. 为什么不直接调 Edit/Write 工具清理

理论上 `code-require` 主线完成后,`code-it` 会读这份 `RESULT.md` 真正去执行清理。但用户本次直接调 `code-require`,没调 `code-auto` 一键命令。`code-require` 自身有硬约束:「不修改 `<本仓库>` 中除了 `./assistants` 目录中的其他代码文件」(见 `code-require/SKILL.md`「不要做的事」)。SKILL.md 在 `plugins/` 下,所以**必须**走完整流程,由 `code-it` 实施。

### 6. 规模预估

- 14 个 SKILL.md(总 8582 行)中**绝大多数**有 1-3 处「本需求」字样。
- 模板文件(10 个)也有大量「(本需求 ...)」字面。
- 估算总影响行数:约 300-500 行删除 + 0 新增 + 少量原地改写(为保持行数对齐)。
- 单次 commit 即可(NFR-8)。

### 7. 风险点

- **R-1**:某些 SKILL.md 大段内容都是"回溯性叙述",剥离后骨架单薄(例如 `code-check/SKILL.md` 的 §8.10 ~ §8.13 校验点几乎全是 REQ-00030 新增的)→ 走 FR-1.AC-1.2 / E-3:回退该文件,在 analysis-notes 标注。
- **R-2**:用户后续在 `code-check` 阶段发现某些已清理段落是「对历史的合规性说明」→ 走 git revert 整次回退(NFR-10)。

## 4 类跳过说明(对照「过程文档自适应判定」准则)

- `clarifications.md`:本轮澄清在 AskUserQuestion 中已完成,无需落盘问答记录(与本技能主流程一致)。
- `related-requirements.md`:经 Grep 扫描 V0.0.3 下 16 个 REQ,无强关联,不生成。
- `process-doc-decisions.md`:本轮所有 4 类过程文档(materials-index / analysis-notes / 2 个跳过)都按自适应规则决定,**不**需"决策记录"专门文件(因为本轮不涉及"犹豫生成 / 不生成"问题,全部按既有规则自然落地)。
- 「变更记录」已追加 1 条(看板)。
