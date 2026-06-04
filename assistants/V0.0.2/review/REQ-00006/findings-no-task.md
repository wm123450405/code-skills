# 未派生任务的发现 — REQ-00006

版本:V0.0.2
时间:2026-06-04 18:09

## 总览

共 7 项发现(F-001 / F-003 / F-004 / F-005 / F-006 / F-007 / F-008)留作 v2 follow-up。**未派生任务的决定**由用户在评审阶段通过 `AskUserQuestion` 确认:仅 F-002(必须改)派生 T-009;其余**无立即派工价值**,记录在此处。

---

## 类别:建议改

### F-001:T-001 SKILL.md 步骤 2.6 S-6 强制发布场景与"不要做的事"第 8 条口径不一致

- **位置**:`plugins/code-skills/skills/code-publish/SKILL.md`
  - "## 工作流程" 步骤 3 报告模板 4(S-6 强制发布场景)
  - "## 不要做的事" 第 8 条
- **类别**:一致性 / 可维护性
- **严重程度**:建议改
- **描述**:SKILL.md "## 不要做的事" 明确说"v1 不实现 --force";但 "## 报告模板" 段中的"4 种报告模板"并未显式排除 S-6(强制发布);Q-D-5 决定 v1 不实现 --force,但 S-6 场景文本是 `needs §S-6` 中沿用,SKILL.md 应在"## 报告模板"中**显式标注**"S-6 场景仅供未来 v2 参考,v1 不会触发"或**删除 S-6**。
- **建议**:
  - 选项 A:删除 S-6 场景(报告模板只保留 3 种 — 通过/不通过/qanda 空)+ "## 报告模板" 段添加注释"v1 不实现 --force;故无强制发布模板"
  - 选项 B:保留 S-6 场景 + 在"## 报告模板"开头标注"以下 4 种场景,S-6 仅供 v2 参考"
- **影响**:轻微文档不一致;不影响任何 FR / AC / NFR
- **建议派生任务**:**否**(轻微,可留 v2 整体审视时处理)

### F-003:T-002 DEPLOY.md 模板的 placeholder 拆分需同步 data-changes.md 文档

- **位置**:
  - `plugins/code-skills/skills/code-publish/templates/DEPLOY.md` §7.1 访问 URL
  - `assistants/V0.0.2/plan/REQ-00006/data-changes.md` §4.1 章节 7
- **类别**:设计符合度(规范内偏离已记录)
- **严重程度**:建议改
- **描述**:T-002 DEPLOY.md 模板把 `<首次访问 URL>` 拆为 `<server>:<port>`(T-002 deviations.md 偏离 1 已记录,授权:无需用户授权,类别:实现细节细化)。但 `data-changes.md §4.1` 章节 7 仍写 "<首次访问 URL>" 单一占位,未标注"实际可拆为 server/port"。**评审接受此偏离**;但应将 `data-changes.md` 同步更新,便于后续维护清晰。
- **建议**:`data-changes.md §4.1` 章节 7 placeholder 描述中加"实际模板可拆为 server + port;具体看 templates/DEPLOY.md"
- **影响**:文档同步,不影响任何 FR / AC / NFR
- **建议派生任务**:**否**(可在 v2 整体文档审视时处理)

### F-005:T-001 SKILL.md 应显式提示 qanda/ 内容的 XSS 风险

- **位置**:`plugins/code-skills/skills/code-publish/SKILL.md` 步骤 2.6 QandaAggregator
- **类别**:安全
- **严重程度**:建议改
- **描述**:SKILL.md 步骤 2.6 明确说"不**做** HTML/JS 转义",但**未**显式说明"不防 XSS" + **未**解释**为什么**(在 Markdown 渲染场景下安全)。对于聚合用户输入(用户可能向 qanda/*.md 写任意内容),Q&A.md 在 README 等渲染场景下通常**安全**(Markdown 渲染器默认不执行 JS),但**当用户将 publish/Q&A.md 复制到支持 HTML 的系统(Confluence / Notion)时,可能引入 XSS**。
- **建议**:SKILL.md 步骤 2.6 末尾加 1 段:
  > **安全提示**:qanda/*.md 内容由用户负责;**不要**在 qanda/ 中放置未经审查的 HTML/JS 片段。当 publish/Q&A.md 被复制到支持 HTML 渲染的系统时,需自行审查。
- **影响**:用户安全意识提升,不影响任何 FR / AC / NFR
- **建议派生任务**:**否**(v2 整体安全审视时处理)

### F-006:T-001 SKILL.md §工作目录约定 应补充 5 模板在项目级(不在版本工作空间内)

- **位置**:`plugins/code-skills/skills/code-publish/SKILL.md` §工作目录约定
- **类别**:一致性 / 可维护性
- **严重程度**:建议改
- **描述**:SKILL.md §工作目录约定的目录树只列出 5 大类(rules/qanda/.current-version/&lt;版本号&gt;/publish + 子目录),**不**包含 5 模板在 `plugins/.../code-publish/templates/`(项目级,不在版本工作空间内)。这点在 `templates/assistants-layout.md` 的"## 整体布局"段有详细注释,SKILL.md 缺。
- **建议**:在 SKILL.md §工作目录约定 补充 1-2 句:
  > 5 模板(DEPLOY.md / UPDATE.md / Q&A.md / qanda-README.md / assistants-layout.md)位于项目级 `plugins/code-skills/skills/code-publish/templates/`,**不**进入版本工作空间;它们是 code-publish 技能的源文档,不是产物。
- **影响**:提升可维护性,用户更清楚 5 模板的物理位置
- **建议派生任务**:**否**(轻微)

### F-007:T-005 qanda-README.md 应说明"以模板为准"维护规则

- **位置**:`plugins/code-skills/skills/code-publish/templates/qanda-README.md`
- **类别**:可维护性
- **严重程度**:建议改
- **描述**:T-004 Q&A.md 模板的"占位章节"**显式指向** `qanda/README.md`;T-005 qanda-README.md 的"## 引用规范"**也指向** T-004。两者**循环引用**,但都通过"文件名"而非 SKILL.md 步骤。**轻微可维护性风险**:若任一文件被改,另一文件可能不同步。
- **建议**:qanda-README.md 末尾加 1 段:
  > **维护说明**:本 README 在 `code-publish/templates/qanda-README.md` 维护;`assistants/qanda/README.md` 应与本文件**保持一致**;若两者内容有差异,**以模板为准**。
- **影响**:模块边界更清晰
- **建议派生任务**:**否**(轻微)

---

## 类别:可选

### F-004:T-006 assistants-layout.md 范式与 code-version 略有不同

- **位置**:`plugins/code-skills/skills/code-publish/templates/assistants-layout.md`
- **类别**:一致性
- **严重程度**:可选
- **描述**:T-006 沿用 `code-version` 范式 6 段结构。`code-version` 自身在"## 关键点"中含"与各 code-* 技能目录粒度对比"表(10 个技能)。T-006 简化了这点(仅说"5 类资源与 4 类读/写角色"表)。这种简化**不违反规范**,但与"完整范式"略有不同;可在 v2 范式更新时考虑统一。
- **建议**:v2 时让 `code-version` / `code-design` / `code-require` / `code-plan` / `code-fix` / `code-publish` 6 个技能 assistants-layout.md 都补"目录粒度对比"表。
- **影响**:统一性增强,工作量 ~0.5d
- **建议派生任务**:**否**(v2 整体范式更新时处理)

### F-008:T-007 与 T-008 自检流程部分重叠;v2 应设计统一自检脚本

- **位置**:T-007 的 8 项不变量自检 + T-008 的双 README 同步自检
- **类别**:可维护性
- **严重程度**:可选
- **描述**:T-007 与 T-008 的"静态自检"流程**部分重叠**(都做"不修改既有 10 技能 SKILL.md"、"不修改 rules"等检查)。T-007 在 T-008 之前完成,**没有**双 README 对仗验证;T-008 在 T-007 之后完成,**没有**重新验证 10 既有 SKILL.md 的"0 改动"。**当前状态**:两次自检的"并集"覆盖了所有 8 项不变量,但**没有"单一来源"做集成验证**。
- **建议**:v2 时可设计一个统一的"REQ-XXXX 收尾自检脚本"覆盖所有 invariant(单一 Bash 脚本,跑一次全检)。`code-review` 步骤 13 末尾"整体结论"可调用此脚本。
- **影响**:v2 收尾自动化
- **建议派生任务**:**否**(v2 整体流程优化时处理)

---

## 总览

| 类别 | 数量 | 任务编码 |
| --- | --- | --- |
| 必须改 | 1 | F-002(已派生 T-009) |
| 建议改 | 5 | F-001 / F-003 / F-005 / F-006 / F-007 |
| 可选 | 2 | F-004 / F-008 |
| **合计** | **8** | (F-002 派生,其余 7 项留此 follow-up) |
