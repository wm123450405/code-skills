# 材料登记 — REQ-00021
更新时间:2026-06-06 17:05
版本:V0.0.3

## 用户输入(原始材料)

| 输入来源 | 关键摘要 | 读取状态 |
| --- | --- | --- |
| 用户命令 `/code-skills:code-require` | 优化 3 技能,允许增加 --result / --plan 参数对输出指定模板文件,产出按模板填充的额外输出文件(REQUIRE.docx / DESGIN.docx / PLAN.docx) | 已读 |

## 关键澄清(本轮 2 问)
- **Q-1 模板格式**:采纳"按用户给定的模板格式输出,二进制文件按实际数据格式填充" — 本需求**仅**实现可文本化格式,二进制**不**报错只跳过(留作 follow-up)
- **Q-2 输出文件名**:采纳"后缀名和用户提供的文件名保持一直,基本名 REQUIRE / DESGIN(详设/概设都是)/ PLAN"(DESGIN 拼写锁定沿用用户原文)

## 项目级规范(沿用)
- `./assistants/rules/dashboard-conventions.md` §规则 1(本需求 0 触发三同步)
- `./assistants/rules/skill-conventions.md` §规则 1(frontmatter 字节级保留)
- `./assistants/rules/encoding-conventions.md` §规则 1/3(本需求 0 触发;模板产出物无编号)
- `./assistants/rules/marketplace-protocol`(本需求 0 触发)
- `./assistants/rules/module-conventions.md` §规则 1(模板产出物放在原主产出物同目录)
- `./assistants/rules/commit-conventions`(沿用既有)
- `./assistants/rules/doc-conventions`(本需求 0 改中英 README)
- `./assistants/rules/naming-conventions`(本需求基本名 REQUIRE / DESGIN / PLAN 用户原文锁定)
- `./assistants/rules/dependency-conventions`(本需求 0 新增依赖;二进制格式填充**留作 follow-up**)

## 上游需求
- 来源:用户 `/code-skills:code-require` 命令
- 提取的 FR / NFR / AC 数量:7 FR / 6 NFR / ~30 AC / 9 INV
- 关键交叉点:3 技能 + 4 参数 + 15 内置占位符

## 项目现状(本次扫描)
- V0.0.3 工作空间:`./assistants/V0.0.3/RESULT.md` 看板(沿用 V0.0.2;本需求前含 REQ-00020 1 条)
- 当前里程碑:M0:工作空间就绪(已完成)
- 父版本:V0.0.2

## 命令行参数解析(本需求新增)

### `code-require --result <模板文件>`
- 模板文件示例:`./templates/requirement-template.docx` / `./tmpl.md` / `./org-requirement.html`
- 输出文件:`./assistants/V0.0.3/require/REQ-00021/REQUIRE.<ext>`
- 状态:已实现

### `code-design --result <模板文件>`
- 模板文件示例:`./templates/design-template.docx`
- 输出文件:`./assistants/V0.0.3/design/REQ-00021/DESGIN.<ext>`(用户原文拼写)
- 状态:已实现

### `code-plan --result <模板文件> --plan <模板文件>`
- `--result` 模板文件示例:`./templates/detail-design.docx`
- `--result` 输出文件:`./assistants/V0.0.3/plan/REQ-00021/DESGIN.<ext>`(用户原文拼写)
- `--plan` 模板文件示例:`./templates/dev-plan.xlsx`
- `--plan` 输出文件:`./assistants/V0.0.3/plan/REQ-00021/PLAN.<ext>`
- 状态:已实现

## 关联需求(同版本)
- REQ-00020(同版本):架构设计目标重新归位 + 3 新维度(本需求沿用 V0.0.3 工作空间)

## 跨版本关联(V0.0.2)
- REQ-00005:首步拉取最新代码 + 末步兜底提交(本需求 `--result` / `--plan` 在步骤 0 之前解析,沿用 REQ-00005 步骤 0a 位置)
- REQ-00007:`code-auto` 自动开发技能(本需求 `code-auto` 不传 `--result` / `--plan`,沿用 Q-4)
- REQ-00011:`code-design` / `code-plan` 步骤 0b 设计目标确认(本需求沿用步骤 0b,新增参数**不**影响)
- REQ-00013:6 技能启用"编号+标题" 显示(本需求模板填充屏显沿用 `formatReqTitle` 风格)
- REQ-00017:`code-plan` 不再为"更新看板"拆派生任务(INV-7 沿用;模板产出物**不**是任务)
- REQ-00019:`code-plan` BUG 模式同构(本需求模板填充对 BUG 路径同样生效)

## 本次变更源
| 变更源 | 检测方式 | 变化列表 |
| --- | --- | --- |
| 需求侧(本需求) | 用户原文 4 子需求 | FR-1 ~ FR-7 全部锁定 |
| 概要设计侧 | 0 | 0(本需求**不**写概要设计) |
| 规范侧 | 0 | 0(本需求 0 改规范) |
| 代码侧 | 0 | 0(本需求改 SKILL.md,无 CWD 代码改动) |
