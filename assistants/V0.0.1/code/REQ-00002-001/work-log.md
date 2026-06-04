# 开发日志 — REQ-00002-001(同步 10 个 SKILL.md)
开始时间:2026-06-04 09:40
版本:V0.0.1

## 项目现状(步骤 6 记录)

- **项目类型**:Claude Code 技能集合(Markdown 文件,无构建/运行命令)
- **构建/运行命令**:N/A(无编译,Markdown 文件处理)
- **测试命令**:N/A(纯文档任务)
- **涉及模块**:10 个 SKILL.md 正文中编码格式示例
- **5 个文件 0 命中**(无需改):`code-design` / `code-init` / `code-review` / `code-rule` / `code-version` 的 SKILL.md
- **5 个文件有命中**(需改正文):`code-it` / `code-plan` / `code-require` / `code-unit` / `code-fix`

## 项目级规范要点(步骤 4 记录)

- `skill-conventions.md §规则 1`:SKILL.md frontmatter 必含 `name`+`description` 且与目录名一致 — 本任务**不改 frontmatter**,仅改正文(INV 继承自 design D-2)
- `doc-conventions.md §规则 1`:中英对仗 — 本任务不涉及 README
- `marketplace-protocol.md`:marketplace 协议约束 — 本任务不涉及 marketplace.json
- `dashboard-conventions.md`:看板字段约定 — 本任务不涉及

## 任务设计要点(步骤 5 记录)

- **PLAN.md §2.1**:`REQ-00002-001 — 同步 10 SKILL.md`,目标 = 把 10 个 SKILL.md 正文中所有 `REQ-\d{4}-\d{4}` 替换为 `REQ-\d{5}`
- **详细设计 §3.2**:编码映射表
  - `REQ-2026-0001` → `REQ-00001`
  - `REQ-2026-0001-001` → `TASK-REQ-00001-00001`(新嵌套式)
  - `REQ-2025-0099` → `REQ-00510`
  - `BUG-001` / `BUG-002` / `BUG-NNN` → `BUG-00001` / `BUG-00002` / `BUG-NNNNN`
- **本任务边界**:仅改正文 5 个含命中的 SKILL.md;其他 5 个 SKILL.md 0 命中,无须改动(Plan §2.1 已明确"其余 6 个 0 命中,Read 全文确认")

## 开发过程

### 2026-06-04 09:40
- 操作:Grep `REQ-\d{4}-\d{4}` 全部 10 SKILL.md
- 结果:5 个文件命中(`code-it` / `code-plan` / `code-require` / `code-unit` / `code-fix`),其余 5 个 0 命中
- 决定:仅改 5 个命中文件;`code-fix` 仅 BUG 格式命中(无 REQ 命中)
