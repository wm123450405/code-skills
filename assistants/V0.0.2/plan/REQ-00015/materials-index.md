# 材料登记 — REQ-00015
更新时间:2026-06-06 09:10
版本:V0.0.2

## 项目级规范
| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `skill-conventions.md` | 技能元信息 | SKILL.md frontmatter 必含 `name` + `description` |
| `module-conventions.md` | 技能资源 | **DEPRECATED**(已迁移到 `directory-conventions.md`) |
| `dashboard-conventions.md` | 看板字段 | 看板字段扩展需 3 文件同步(本需求不触发) |
| `marketplace-protocol.md` | 协议清单 | `$schema` / `name` / `version` 必填;`plugins[].source` 以 `./` 开头 |
| `encoding-conventions.md` | 编码格式 | REQ/BUG `^[\w-]{5,5}$`;TASK `^TASK-(REQ\|BUG)-\d{5}-\d{5}$` |
| `commit-conventions.md` | 提交 | 占位,本需求沿用 V0.0.2 既有 `chore(<scope>): ...` |
| `directory-conventions.md` | 目录 | `templates/` / `checklists/` / `guidelines/` 三类子目录(本需求无新增资源) |
| `framework-conventions.md` | 框架 | 不适用(纯 CLI) |
| `naming-conventions.md` | 命名 | 不适用 |
| `doc-conventions.md` | 文档 | 不适用 |
| `dependency-conventions.md` | 依赖 | 0 新增三方依赖 |
| `migration-mapping.md` | 编码迁移 | 不适用 |
| `coding-style.md` | 代码风格 | 不适用(纯文档) |

**遵循规范数量**:13(全部只读引用)

## 上游需求
- 来源:./assistants/V0.0.2/require/REQ-00015/RESULT.md (v1)
- 提取的 FR / NFR / AC 数量:**8 FR / 10 NFR / 10 大类 AC / 12 边界场景**
- 关键交叉点(每条 FR 对应的设计章节):
  - FR-1 → 设计 §3.1
  - FR-2 → 设计 §3.2
  - FR-3 → 设计 §3.3
  - FR-4 → 设计 §3.4
  - FR-5 → 设计 §3.5
  - FR-6 → 设计 §3.6
  - FR-7 → 设计 §3.7
  - FR-8 → 设计 §3.8

## 上游概要设计
- 来源:./assistants/V0.0.2/design/REQ-00015/RESULT.md (v1)
- 提取的模块拆分 / 接口概要 / 数据结构 / 决策:
  - **1 模块新增**:`code-merge` 技能入口(0 模块修改 / 0 三方依赖)
  - **接口**:新增 SKILL.md(`name: code-merge` + `description: <完整>`)
  - **接口**:marketplace.json 追加 `./skills/code-merge`
  - **决策**(8 项 D-1~D8,沿用概要设计):工作流描述 vs 命令模板 / LLM 现场智能合并 / worktree 强约束 / `--no-ff` / 自检不修复 / 二进制留 unmerged
  - **不变量**(10 项 INV-1~10):严守 13 份项目级规范

## 项目现状(实现细节)
### 命名风格
- 技能名 kebab-case(`code-merge`)
- 函数名 camelCase(truncateTitle / formatReqTitle 等沿用 REQ-00013 风格)
- 文件名 lowercase-with-hyphen

### 错误模型
- stdout 报告:`✓` 成功 / `✗` 失败 / `⚠` 警告(NFR-8)
- 退出码:0 = 全部成功(含警告)/ 非 0 = 致命 / 130 = SIGINT
- LLM 现场分析冲突时,语义冲突无法解决 → 留 unmerged + 提示

### 并发原语
- 不适用(本技能是串行 git 命令,无并发)

### 既有相似功能的实现风格
- **code-publish** SKILL.md:`PreflightChecker` 风格(逐步推进 + 行级状态)
- **code-auto** SKILL.md:`=== xxx 启动 ===` 报告 + `[code-auto]` 前缀进度日志
- **code-require** SKILL.md:状态机 Mermaid 风格 + 边界异常 E-N 列表

### 既有测试用例的风格与覆盖度
- 0 测试用例(本仓库纯文档,无测试载体 — REQ-00009 守卫判定"不可测")

### 可复用的工具函数/中间件
- **看板解析**:`code-dashboard` 算法 1/4/5(本设计 FR-6 复用)
- **commit 格式**:`chore(<scope>): <description>`(本设计 FR-2 复用)
- **错误信息风格**:既有 11 个 `code-*` 的 `✓`/`✗`/`⚠` 前缀(本设计 NFR-8 复用)
- **任务编号解析**:`encoding-conventions §规则 1+3` 嵌套式正则(本设计 FR-6 复用)

## 关联编码计划(同版本)
- **plan/REQ-00007/PLAN.md**(`code-auto` 5 任务):参考其任务粒度(2 SKILL.md 修改 + marketplace.json + README + 看板同步 + 收尾)
- **plan/REQ-00016/PLAN.md**(`code-design` / `code-plan` 快模式 4 任务):参考其任务粒度(2 SKILL.md + 1 看板 + 1 收尾)

**0 冲突**(本需求不与既有计划交互)
