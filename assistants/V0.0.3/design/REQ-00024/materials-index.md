# 材料登记 — REQ-00024
更新时间:2026-06-07
版本:V0.0.3

## 项目级规范
| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `skill-conventions.md` | 模块规划 | SKILL.md frontmatter 必含 `name` + `description`;本需求 0 修改 frontmatter(INV 严守) |
| `module-conventions.md` | 模块规划 | DEPRECATED(已迁至 `directory-conventions.md`);0 触发 |
| `directory-conventions.md` | 模块规划 | 占位待填;本需求 0 触发 |
| `encoding-conventions.md` | 接口定义 | 3 类编码权威源(REQ-NNNNN / BUG-NNNNN / TASK-(REQ\|BUG)-NNNNN-NNNNN);本需求 0 触发 |
| `dashboard-conventions.md` | 模块规划 | 看板字段扩展需 3 文件同步;0 字段扩展,0 三同步 |
| `doc-conventions.md` | 文档 | README 多语言对仗;0 触发 |
| `coding-style.md` | 测试 | 占位;SKILL.md 是自然语言 0 触发 |
| `commit-conventions.md` | 模块规划 | 占位;commit message 沿用 `chore(code-plan): ...` |
| `dependency-conventions.md` | 安全 | 占位;0 新依赖 |
| `framework-conventions.md` | 功能架构 | 占位;0 架构变更 |
| `naming-conventions.md` | 模块规划 | 占位;0 新增命名实体 |
| `migration-mapping.md` | 接口定义 | EXISTING-NNN 不追溯;0 触发 |
| `marketplace-protocol.md` | 接口定义 | marketplace.json 字段约束;0 JSON 变更 |

## 上游需求
- 来源:./assistants/V0.0.3/require/REQ-00024/RESULT.md
- 版本:v1(2026-06-07)
- 提取:9 FR / 6 NFR / 8 AC / 4 Q

## 项目现状(本次扫描)

### 项目类型
- 语言/框架:Markdown(纯文档项目)
- 关键依赖:无运行时依赖
- 技能家族:`plugins/code-skills/skills/` 下 14 个 `code-*` 技能 + `code-auto` 编排者

### 目录结构
- `plugins/code-skills/skills/<skill-name>/SKILL.md` + `templates/` + `checklists/` + `guidelines/`
- `assistants/<version>/` 版本工作空间:`require/` / `design/` / `plan/` / `code/` / `test/` / `review/` / `fix/`

### 已有模块
| 模块 | 职责 | 是否可复用 |
| --- | --- | --- |
| `code-auto/SKILL.md` | 6 步状态机 + 子技能编排 | **修改**(本需求) |
| 其他 13 个 `code-*` SKILL.md | 各自职责 | **不修改** |

### 已有数据模型
- `path-detection-result`(本需求新增,见设计 §5)

### 编码与构建约定
- 沿用既有:`chore(code-xxx):` commit message 前缀
- SKILL.md 修订锚点:在 `## 工具使用约定` 段后 + `## 工作流程` 段前
- frontmatter 字节级保留
