# 材料登记 — REQ-00002
更新时间:2026-06-03 20:25
版本:V0.0.1

## 项目级规范
| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `dashboard-conventions.md` | 看板/模板/CLAUDE.md | §规则 1:看板字段约定扩展需三处同步(模板 + CLAUDE.md + 本规范);本需求**条件触发**(若改 `version-RESULT.md` 模板或字段语义说明) |
| `doc-conventions.md` | 文档编写 | §规则 1:README 中英同次提交同步;§规则 2:README 中命令/路径反映实际状态、占位文本必须有 issue 引用 |
| `marketplace-protocol.md` | Marketplace 协议 | §规则 1:`$schema` / `name` / `version` 必填,`plugins[].name` 与 `plugin.json` 同步,**不**允许未知字段;本需求**不触发** |
| `module-conventions.md` | 技能资源摆放 | §规则 1:技能资源放 `templates/` / `checklists/` / `guidelines/` 子目录;SKILL.md 在技能根;本需求**不**改技能资源结构 |
| `skill-conventions.md` | 技能元信息 | §规则 1:SKILL.md frontmatter 必含 `name` + `description`,`name` 与目录名一致;本需求**只改正文,不改 frontmatter**,但仍需保持 frontmatter 完整 |

> 规范层面对本需求的约束总览:
> - **强触发**:`doc-conventions.md §规则 1`(中英 README 同次提交)、`§规则 2`(命令反映实际)
> - **条件触发**:`dashboard-conventions.md §规则 1`(若改 `version-RESULT.md` 模板)
> - **不触发**:`marketplace-protocol.md §规则 1`、`module-conventions.md §规则 1`、`skill-conventions.md §规则 1`(仅改正文)
>
> 注:本需求不直接修改 `./assistants/rules/`,若 Q-8 = (a)由用户调 `code-rule` 在实施阶段创建 `encoding-conventions.md`(本设计不实施)

## 上游需求
- 来源:`./assistants/V0.0.1/require/REQ-00002/RESULT.md`
- 版本:v3(2026-06-03 20:20,含 FR-6 部分提前落地)
- 提取的 FR / NFR / AC 数量:10 FR / 7 NFR / 11 AC
- 待澄清:5 项(Q-6 EXISTING-、Q-8 encoding-conventions.md、Q-9 migration-mapping、Q-10 cache 提示、Q-12 TASK 嵌套前缀)
- 已锁定:Q-7(G4 新嵌套式 `TASK-(REQ|BUG)-\d{5}-\d{5}`)

## 项目现状(本次扫描)

### 项目类型
- Claude Code marketplace + 单 plugin:`code-skills`
- 10 个 code-* 技能(`code-init` / `code-version` / `code-rule` / `code-require` / `code-design` / `code-plan` / `code-it` / `code-unit` / `code-fix` / `code-review`)
- 仓库**不包含**任何源代码、构建系统、测试框架、Lint、包管理

### 旧编码格式的实际嵌入点(扫描结果)
| 文件 / 路径模式 | 含旧格式的位置 | 涉及范围 |
| --- | --- | --- |
| `plugins/code-skills/skills/*/SKILL.md` | 10 个 SKILL.md 全部含旧格式说明 / regex / 示例 | 10 |
| `plugins/code-skills/skills/*/templates/*.md` | 20+ 模板含 `REQ-2026-0001` / `BUG-001` / `REQ-2026-0001-001` 等示例值 | 20+ |
| `plugins/code-skills/skills/code-version/templates/version-RESULT.md` | 看板模板含旧格式字段示例值 | 1 |
| `plugins/code-skills/skills/code-version/templates/assistants-layout.md` | 目录树示例含 `REQ-2026-0001/` / `REQ-2026-0001-001/` | 1(其它技能的同名模板为副本) |
| `plugins/code-skills/README.md` | 中文版工作流管道示例 | 1 |
| `plugins/code-skills/README.en.md` | 英文版工作流管道示例(逐行镜像中文版) | 1 |
| `plugins/code-skills/CLAUDE.md` | 第 24/88/99/100 行 | 1 |
| `./assistants/V0.0.0/require/EXISTING-001 ~ EXISTING-010/` | 基线特例,前缀独立(待 Q-6 决定) | 10 |
| `./assistants/V0.0.0/require/EXISTING-001 ~ EXISTING-010/*/RESULT.md` | 文档内可能含 `REQ-2026-0001` 示例字符串 | 10 |

### 已有模块 / 接口 / 数据模型
- **不适用**:本仓库无应用代码;唯一对外契约是 SKILL.md / 模板 / 看板 / README
- 本需求是"协议文本层面"的字符串批量替换,不涉及代码模块
- 影响的"模块"全部为**文档/模板/示例**,无运行时实体

### 已有第三方依赖
- 0 个(本仓库无第三方依赖,纯文档/清单/技能定义)

### 编码与构建约定
- 无源代码/构建系统
- 文档规范:`doc-conventions.md`(已加载)
- 看板规范:`dashboard-conventions.md`(已加载)
- 技能规范:`skill-conventions.md` / `module-conventions.md`(已加载)
- 协议规范:`marketplace-protocol.md`(已加载)

### 可复用资产
- 全部 10 个技能与 5 个规范文件均**完全可复用**,本需求不修改其中任何文件**的内容结构**,仅改正文文本(非 frontmatter、非模板结构)

## 关键观察
1. 本需求是**纯协议文本横切变更**;核心动作 = "30+ 文件 × 若干处字符串替换"
2. 真正的"技术性"决策是:
   - **编辑粒度**:逐处 Edit vs 模板化批量?(Edit 不可规模化,需按 Grep 命中点逐处修改)
   - **regex 升级**:code-it 的 `^REQ-\d{4}-\d{4}-\d{3}$` → `^TASK-(REQ|BUG)-\d{5}-\d{5}$`;需双路径解析逻辑
   - **TASK 编号分配逻辑**:code-plan 从全局扫描改为"父级内查最大 +1"
   - **Q-12 决定**:本设计**采用默认 (a) 仅数字段**(详见 `clarifications.md` §Q-12)
3. 唯一必须强约束的是"中英 README 同次提交" + "看板模板与 CLAUDE.md 同步"(条件触发)
4. V0.0.0 EXISTING- 基线与本需求**部分解耦**:若 Q-6 = H1(保留)→ 不需动 V0.0.0;若 H2(改)→ V0.0.0 全量迁移
