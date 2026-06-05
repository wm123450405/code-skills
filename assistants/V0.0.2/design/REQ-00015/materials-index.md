# 材料登记 — REQ-00015
更新时间:2026-06-06 09:00
版本:V0.0.2

## 项目级规范
| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `skill-conventions.md` | 技能元信息 | SKILL.md frontmatter 必含 `name` + `description`;`name` = 目录名(kebab-case) |
| `module-conventions.md` | 技能资源 | **DEPRECATED**(已迁移到 `directory-conventions.md`,本表留作历史参考) |
| `dashboard-conventions.md` | 看板字段 | 看板字段扩展需 3 文件同步(`templates/version-RESULT.md` + `CLAUDE.md` + 本规范) |
| `marketplace-protocol.md` | 协议清单 | `$schema` / `name` / `version` 必填;`plugins[].source` 以 `./` 开头;`skills[]` 是相对路径数组 |
| `encoding-conventions.md` | 编码格式 | REQ/BUG `^[\w-]{5,5}$`;TASK `^TASK-(REQ\|BUG)-\d{5}-\d{5}$` |
| `commit-conventions.md` | 提交 | v1 占位(本需求不依赖具体 commit 规范,但 `code-merge` 与 git 提交相关) |
| `directory-conventions.md` | 目录(替代 module-conventions) | `templates/` / `checklists/` / `guidelines/` 三类子目录(本需求无新增资源) |
| `framework-conventions.md` | 框架 | 不适用(本需求新增 CLI 技能,无运行时框架) |
| `naming-conventions.md` | 命名 | 不适用(本技能无新增命名) |
| `doc-conventions.md` | 文档 | 不适用(本需求不写 README) |
| `dependency-conventions.md` | 依赖 | 不适用(本需求不新增三方依赖) |
| `migration-mapping.md` | 编码迁移 | 不适用(本需求不涉及编码迁移) |
| `coding-style.md` | 代码风格 | 不适用(本需求新增 SKILL.md 纯文档,无源码) |

**遵循规范数量**:13(全部只读引用)

## 上游需求
- 来源:./assistants/V0.0.2/require/REQ-00015/RESULT.md
- 版本:v1(2026-06-05 15:50)
- 提取的 FR / NFR / AC 数量:**8 FR / 10 NFR / 10 大类 AC / 12 边界场景(E-M1~M12)**

## 项目现状(本次扫描)
### 项目类型
- **类型**:Claude Code 插件市场仓库(marketplace)
- **技术栈**:纯文档仓库(Markdown 技能定义 + JSON 协议清单)
- **运行时**:无(技能由 Claude Code 模型层在用户调用时按需解释执行)

### 目录结构
- `plugins/code-skills/skills/<code-*>/` 11 个 `code-*` 技能(本次新增第 12 个 `code-merge`)
- `plugins/code-skills/skills/<code-*>/SKILL.md` 每个技能入口
- `plugins/code-skills/skills/<code-*>/{templates,checklists,guidelines}/` 可选资源子目录
- `.claude-plugin/marketplace.json` marketplace 根清单
- `plugins/code-skills/.claude-plugin/plugin.json` 子插件清单
- `assistants/rules/*.md` 跨版本共享的 13 份项目级规范
- `assistants/V0.0.2/result.md` 当前版本看板
- `assistants/V0.0.2/{require,design,plan,code,test,review,fix}/` 各阶段工作空间

### 已有模块(11 个 `code-*` 技能)
| 技能 | 职责 | 与本需求关联 |
| --- | --- | --- |
| `code-version` | 版本管理(切换/创建工作空间) | **间接**:FR-1 启动时读 `.current-version`(沿用) |
| `code-require` | 需求分析 | **间接**:本需求上游 RESULT.md(本设计是下游) |
| `code-design` | 概要设计 | **直接**:本设计是 code-design 自身产出 |
| `code-plan` | 详细设计 + 任务拆分 | **直接**:本设计是 code-plan 上游 |
| `code-it` | 单任务实施 | **不调**(code-merge 不拆分任务) |
| `code-unit` | 单元测试 | **不调**(code-merge 纯 CLI 操作) |
| `code-review` | 评审 | **不调**(code-merge 不参与评审流) |
| `code-fix` | 缺陷登记 | **不调** |
| `code-publish` | 发布手册 | **不调** |
| `code-dashboard` | 看板聚合 | **间接**:FR-6 看板自检复用其算法 1/4/5 |
| `code-rule` | 编码规范管理 | **不调** |
| `code-auto` | 自动开发编排 | **不调**(NFR-7 锁定 code-auto 不自动调 code-merge) |

### 已有接口
- **入口**:`/code-<skill-name>`(Claude Code 技能调用语法)
- **参数**:由 SKILL.md 描述,本需求新增 `/code-merge [branch]`
- **返回值**:stdout 报告(无返回值,由 Claude Code 解释 stdout 即可)

### 已有数据模型
- **.md 文档**:RESULT.md / PLAN.md / REVIEW-REPORT.md / work-log.md 等
- **.json 协议清单**:marketplace.json / plugin.json
- **本需求新增**:**0** 实体(纯 CLI 操作,无持久化数据模型)

### 已有第三方依赖
- **0**(纯文档仓库,无运行时依赖)

### 编码与构建约定
- **SKILL.md 编写**:遵循 `skill-conventions.md §规则 1`(frontmatter 必含 name + description)
- **资源摆放**:遵循 `module-conventions.md §规则 1`(`templates/` / `checklists/` / `guidelines/` 三类子目录)
- **commit 格式**:沿用 V0.0.2 既有模式 `chore(<scope>): <description>`
- **末尾提交**:沿用 REQ-00005 的"末尾兜底提交"模式(但本需求是 SKILL.md 单文件,不强制末尾提交)

### 复用资产
1. **`code-require` / `code-design` / `code-plan` 步骤 0a**:`git pull` 模式 → **0 复用**(本需求 NFR-4 锁定"在 worktree 中运行",worktree 通常无 upstream)
2. **`code-it` / `code-plan` 步骤 N 末尾兜底提交**:commit 格式 `chore(<scope>): ...` → **复用 commit 格式**(FR-2)
3. **`code-dashboard` 算法 1**(解析 5 区段表格)→ **复用**(FR-6 看板自检)
4. **`code-require` 状态机风格**(Mermaid 流程图)→ **复用**(本设计 §4 状态机)
5. **既有 11 个 `code-*` 的 stdout 报告格式**(`=== xxx 启动 ===` / `✓` / `✗` / `⚠` 前缀)→ **复用**(FR-8 / NFR-8)
6. **`code-publish` PreflightChecker 风格**(逐步推进 + 行级状态)→ **复用**(FR-1 ~ FR-8 各步打印)
