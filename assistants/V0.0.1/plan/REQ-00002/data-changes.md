# 数据结构完整变更 — REQ-00002
版本:V0.0.1

> 本需求**无新增数据实体**(无数据库 schema 变更,纯文档/字符串字面量替换)。
> 本节记录"编码字符串格式"层面的数据结构变化。

## 修改实体:REQ 编码格式(全仓库引用)

- **路径**:`./assistants/<版本号>/require/<需求编号>/` 目录名 + `<需求编号>` 字面量
- **字段变更**:
  | 字段 | 改前 | 改后 |
  | --- | --- | --- |
  | 编码格式 | `REQ-YYYY-NNNN`(10 字符) | `REQ-NNNNN`(9 字符) |
  | 正则 | `^REQ-\d{4}-\d{4}$` | `^REQ-\d{5}$` |
  | 父级(目录名) | `REQ-2026-0001` | `REQ-00001` |
- **索引变更**:无
- **迁移需求**:
  - 旧编码已落地实体:`assistants/V0.0.1/require/REQ-00001/`(原 `REQ-2026-0001/`,FR-6 部分提前落地)
  - 旧编码历史实体:`assistants/V0.0.0/require/EXISTING-*`(基线历史,本需求**不修改**)
- **依据规范**:FR-1(新格式定义)+ FR-6(已落地)

## 修改实体:BUG 编码格式(全仓库引用)

- **路径**:`./assistants/<版本号>/fix/<缺陷编号>/` 目录名 + `<缺陷编号>` 字面量
- **字段变更**:
  | 字段 | 改前 | 改后 |
  | --- | --- | --- |
  | 编码格式 | `BUG-NNN`(6 字符) | `BUG-NNNNN`(9 字符) |
  | 正则 | `^BUG-\d{3}$` | `^BUG-\d{5}$` |
- **索引变更**:无
- **迁移需求**:
  - 旧编码已落地实体:无(本仓库尚未有 BUG 实体)
  - 旧编码历史实体:无
- **依据规范**:FR-1(新格式定义)

## 修改实体:TASK 编码格式(全仓库引用,Q-7 锁定 G4 新嵌套式)

- **路径**:`./assistants/<版本号>/code/<任务编码>/` 目录名 + `<任务编码>` 字面量
- **字段变更**:
  | 字段 | 改前 | 改后 |
  | --- | --- | --- |
  | 编码格式(需求任务) | `REQ-YYYY-NNNN-NNN`(14 字符) | `TASK-REQ-NNNNN-NNNNN`(19 字符) |
  | 编码格式(缺陷任务) | `BUG-NNN-NNN`(11 字符) | `TASK-BUG-NNNNN-NNNNN`(19 字符) |
  | 正则(需求任务) | `^REQ-\d{4}-\d{4}-\d{3}$` | `^TASK-REQ-\d{5}-\d{5}$` |
  | 正则(缺陷任务) | `^BUG-\d{3}-\d{3}$` | `^TASK-BUG-\d{5}-\d{5}$` |
  | **TASK 编码"父级段"** | 含 `REQ-` 前缀 | **仅含数字段**(Q-12 默认 a) |
- **索引变更**:无
- **迁移需求**:
  - 旧编码已落地实体:`assistants/V0.0.1/code/REQ-00001-001/`(REQU FR-6 部分已落地)
  - **关键决策**:已落地的旧格式 `REQ-00001-001` **保留**(作为 V0.0.1 历史快照);**不**重命名为 `TASK-REQ-00001-00001`
  - **理由**:
    1. `REQ-00001-001` 是 REQ-00002 之前已落地的命名,符合当时规范
    2. 重命名会破坏"REQ-00001 已完成"的事实链
    3. 命名是"实体内码",不是"显示格式",在 .md 文档中可读即可
- **依据规范**:FR-1 + Q-7 锁定 + Q-12 默认

## 新增实体:encoding-conventions.md(规范文档)

- **路径**:`./assistants/rules/encoding-conventions.md`(新建)
- **字段(文档章节)**:
  | 章节 | 内容 |
  | --- | --- |
  | 适用场景 | 何时查阅本规范 |
  | 规范 1 | 编码格式定义(REQ/BUG/TASK 三类) |
  | 规范 2 | 5 位纯数字格式约束 |
  | 规范 3 | 嵌套式 TASK 编码规则(需求/缺陷两种) |
  | 规范 4 | 实施流程(编码 → 提交 → 引用) |
  | 来源 | 由 `code-rule` 后续维护 |
- **存储选型**:Markdown 文件(项目级规范统一格式)
- **迁移脚本**:无
- **依据规范**:本规范由 `code-it` 创建,由 `code-rule` 接管维护

## 新增实体:migration-mapping.md(迁移映射)

- **路径**:`./assistants/rules/migration-mapping.md`(新建)
- **字段(文档章节)**:
  | 章节 | 内容 |
  | --- | --- |
  | 适用场景 | 何时查阅本表 |
  | 映射表 | 旧格式 → 新格式 + 命中文件清单 + 处置 |
  | 已知不完全映射 | V0.0.0 EXISTING-* 旧串(基线历史) |
  | 维护说明 | 由 `code-rule` 后续维护 |
- **存储选型**:Markdown 表格
- **迁移脚本**:无
- **依据规范**:本规范由 `code-it` 创建,由 `code-rule` 接管维护

## 不修改实体(范围外,本需求严禁修改)

- `.claude-plugin/marketplace.json`(根 name + 子项 plugins[0].name)
- `plugins/code-skills/.claude-plugin/plugin.json`(plugin name)
- 10 SKILL.md 的 YAML frontmatter(`name` + `description`)
- 5 个现有 `assistants/rules/` 文件(`dashboard-conventions.md` / `doc-conventions.md` / `marketplace-protocol.md` / `module-conventions.md` / `skill-conventions.md`)
- `assistants/V0.0.0/require/EXISTING-*/*`(基线历史)
- 本工作目录中的历史文件(`require/REQ-00001/*` + `design/REQ-00001/*` + `plan/REQ-00001/*` + `code/REQ-00001-001~004/*`)中的旧编码引用

## 实体关系图(本需求范围)

```
旧格式(范围外/不修改)              新格式(本需求落地)
─────────────────────             ─────────────────────
REQ-YYYY-NNNN (e.g. REQ-2026-0001)  REQ-NNNNN (e.g. REQ-00001)
                                     ↓ (派生)
BUG-NNN (e.g. BUG-001)              BUG-NNNNN (e.g. BUG-00001)
                                     ↓ (派生)
REQ-YYYY-NNNN-NNN (旧 TASK)         TASK-REQ-NNNNN-NNNNN
                                    TASK-BUG-NNNNN-NNNNN
```

> 旧格式的 REQ-2026-0001/REQ-2026-0002 等**已重命名**为 REQ-00001/REQ-00002(FR-6 部分提前落地);旧格式的 BUG-NNN / REQ-YYYY-NNNN-NNN **本需求不重命名**既有实体(仅替换 SKILL.md/模板/README 中的示例值)。

## 命名规范锁定表(本需求后)

| 实体 | 格式 | 正则 | 示例 |
| --- | --- | --- | --- |
| 需求 | `REQ-NNNNN` | `^REQ-\d{5}$` | `REQ-00001` |
| 缺陷 | `BUG-NNNNN` | `^BUG-\d{5}$` | `BUG-00001` |
| 需求任务 | `TASK-REQ-NNNNN-NNNNN` | `^TASK-REQ-\d{5}-\d{5}$` | `TASK-REQ-00001-00001` |
| 缺陷任务 | `TASK-BUG-NNNNN-NNNNN` | `^TASK-BUG-\d{5}-\d{5}$` | `TASK-BUG-00001-00001` |
| 任务目录 | `<任务编码>/` | (与任务编码一致) | `TASK-REQ-00001-00001/` |
