# 材料登记 — BUG-00001
更新时间:2026-06-07
版本:V0.0.3

## 项目级规范
| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `skill-conventions.md` | 模块规划 | SKILL.md frontmatter 必含 `name`(与目录名一致)+ `description`(非空自然语言);新增 frontmatter 字段需同步扩展本规则 |
| `module-conventions.md` | 模块规划 | **DEPRECATED(已弃用)**,内容已迁移到 `directory-conventions.md`(2026-06-04 REQ-00003 H2 决策) |
| `directory-conventions.md` | 模块规划 | 替代旧 `module-conventions.md`;本规则 §规则 1 占位待 `code-rule` 填充(本缺陷修复**不**触发本规则新增) |
| `encoding-conventions.md` | 接口定义 | **权威源**定义 3 类编码(REQ-NNNNN / BUG-NNNNN / TASK-(REQ\|BUG)-NNNNN-NNNNN);BUG 路径任务编号强制 5+5 位嵌套式 `TASK-BUG-NNNNN-NNNNN` |
| `dashboard-conventions.md` | 模块规划 | 看板字段扩展(区段/列/枚举)需**同一次提交**同步 `version-RESULT.md` + `CLAUDE.md` + 本规范;**本缺陷修复不触发本规则**(无字段扩展) |
| `doc-conventions.md` | 文档 | README 多语言对仗 + 主语言 README 必含核心小节(简介/安装/使用流程);本缺陷修复**不**改 README |
| `coding-style.md` | 测试 | 占位待填充;本缺陷修复范围是 SKILL.md 文档,**不**涉及源码编码风格 |
| `commit-conventions.md` | 模块规划 | 占位待填充;本缺陷修复产物为 SKILL.md 文档改造,commit message 沿用 `chore(code-it): BUG-00001 ...` |
| `dependency-conventions.md` | 安全 | 占位待填充;本缺陷修复**不**引入新依赖 |
| `framework-conventions.md` | 功能架构 | 占位待填充;本缺陷修复**不**改架构 |
| `naming-conventions.md` | 模块规划 | 占位待填充;本缺陷修复**不**新增命名实体,仅追加 SKILL.md 段落 |
| `migration-mapping.md` | 接口定义 | 旧编码 → 新编码追溯表;**本缺陷修复不涉及编码重命名**(BUG-00001 已是新格式) |
| `marketplace-protocol.md` | 接口定义 | marketplace.json / plugin.json 字段约束;**本缺陷修复不触发本规则**(无 JSON 字段变更) |

**规范遵循结论**:
- 强约束层:`skill-conventions.md` §规则 1(frontmatter 不动)/ `encoding-conventions.md` §规则 1-4(任务编号 5+5 位)/ `dashboard-conventions.md` §规则 1(0 字段扩展,故 0 三同步)
- 弱约束层:其余 5 份占位规范对本修复**不**产生约束
- 0 触发:`code-rule`(本缺陷不新增规范;`skill-responsibility.md` 可选项留作"待 code-plan 设计决策")

## 上游需求
- **来源**(缺陷路径,无 REQ):`./assistants/V0.0.3/fix/BUG-00001/RESULT.md`
- **缺陷原始报告**:code-require/code-design/code-plan/code-fix 不能实际修改代码(职责混淆)
- **严重度**:P0(架构职责分离违反)
- **当前状态**:调查中(2026-06-07 推进,本轮 code-plan 完成后推进至"修复规划中")
- **已含根因假设**:5 条(假设 1-3 原始,假设 4-5 本轮"调查中"补充)

## 上游概要设计
- **不适用**(缺陷路径无 design/ 阶段)
- **本缺陷修复的"概要设计"**:`fix/BUG-00001/RESULT.md §4 修复方案` 5 项方向
  - 方向 1:code-require / code-design / code-plan / code-fix SKILL.md 加"禁止修改 CWD 项目源码"硬约束
  - 方向 2:code-it SKILL.md 加"唯一允许的生产代码改动场景"声明
  - 方向 3:code-unit SKILL.md 加"可改测试代码"声明
  - 方向 4(可选):新增 `rules/skill-responsibility.md` 固化"技能 → 目录映射"约束
  - 方向 5:历史 4 commit 不回滚,仅约束未来

## 项目现状(实现细节)

### 6 个目标 SKILL.md 当前结构(本轮 Read 已确认)

| 技能 | frontmatter(YAML 顶部) | 既有"## 不要做的事"段 |
| --- | --- | --- |
| `code-require` | 已含 `name` + `description` | 含"不调用 ... 不修改 ./assistants/rules/ ..."(V0.0.2 已加) |
| `code-design` | 已含 | 含"不修改其他 10 个 code-* 技能 frontmatter"等(NFR-6 强约束) |
| `code-plan` | 已含 | 含"不修改 frontmatter"等(沿用) |
| `code-fix` | 已含 | 含"不修改其他 code-* 技能负责的文件"等 |
| `code-it` | 已含 | **缺**"唯一可改代码"显式声明(仅在 `code-fix` 流程示例中隐含) |
| `code-unit` | 已含 | **缺**"可改测试代码"显式声明 |

### 历史违规 commit 模式(根因证据)
| commit | 提交类型前缀 | 修改的工程代码 | 应走路径 |
| --- | --- | --- | --- |
| `e69a58a` | `chore(code-require):` | 3 SKILL.md | code-plan → code-it 逐任务 |
| `6dee813` | `chore(code-require):` | 3 SKILL.md | 同上 |
| `3e1573e` | `chore(code-design):` | 1 SKILL.md(47 行) | code-plan → code-it 逐任务 |
| `e568328` | `chore(code-plan):` | 1 SKILL.md(47 行) | 同上 |

**根因正式定稿**(本轮 code-plan 确认):
- **主因(假设 2)**:SKILL.md 流程约束弱化 — 4 个技能"## 不要做的事"段虽有"不修改 X"等条款,但**无**"禁止修改 CWD 项目源码"的**显式硬约束**(本仓库工程代码 = `plugins/code-skills/skills/*/SKILL.md`)
- **辅助(假设 1+3)**:历史惯例 + 未受审查(本修复不追溯历史 commit)
- **辅助(假设 4)**:4 个违规 commit 全部跳过"code-plan 拆任务 → code-it 实施"标准链路,INV-7 隐含约束未被强制
- **辅助(假设 5)**:审计可观察性失配 — 1 commit vs 6 任务的颗粒度漂移(本修复不解决此问题,只通过后续强制"code-it 实施"间接改善)

## 本次变更源(首次规划,无变更)
- 缺陷侧:`fix/BUG-00001/RESULT.md` 状态"调查中",已含 5 条根因假设 + 5 项修复方向
- 代码侧:6 个目标 SKILL.md 当前 frontmatter 与"## 不要做的事"段已 Read 完整(本轮 Read 时已抓取关键约束)
- 规范侧:13 份规范已 Read 完整,0 触发新增/修改

## 命令行参数
- `--result`:无
- `--plan`:无

## 模板填充结果
- 无(无 2 参数)
