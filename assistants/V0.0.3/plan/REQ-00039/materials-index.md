# 材料登记 — REQ-00039

更新时间:2026-06-22 15:00
版本:V0.0.3

## 项目级规范

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `skill-conventions.md` | SKILL.md 编写 | frontmatter L1-3 字节级保留;不得包含开发痕迹 |
| `dashboard-conventions.md` | 看板字段约定 | 字段扩展需三方同步;本需求**不**新增列 |
| `encoding-conventions.md` | 编码格式 | REQ/BUG/TASK 命名;5 位纯数字;接收端宽松正则 |
| `migration-mapping.md` | 编码迁移 | `EXISTING-NNN` 不追溯;新旧编码追溯表 |
| `directory-conventions.md` | 目录与模块 | (待添加占位);`plugins/code-skills/skills/<name>/` 子目录布局 |
| `doc-conventions.md` | 文档编写 | README 多语言对仗 + 主语言完整性 |
| `naming-conventions.md` | 命名 | kebab-case |
| `coding-style.md` | 代码风格 | (本需求是 Markdown 自然语言) |
| `framework-conventions.md` | 框架 | (无框架变更) |
| `dependency-conventions.md` | 依赖 | 本需求**不**新增三方依赖(沿用既有 tokei/cloc 系统命令) |
| `commit-conventions.md` | 提交 | `chore(code-<技能>):` 模式 |
| `marketplace-protocol.md` | marketplace | 协议字段约束;本需求**不**改 `.claude-plugin/` |
| `module-conventions.md` | 模块 | `templates/` 留作历史不删;新模块在 `lib/` |

## 上游需求

- 来源:`./assistants/V0.0.3/require/REQ-00039/RESULT.md`(v1,2026-06-22 14:00)
- 提取:**5 FR / 8 NFR / 8 AC**
- 核心诉求:代码行数限制仅统计实际逻辑行(注释 / 说明 / 空行 / 格式化换行不计入);`code-it` 步骤 8 末尾新增 `calcLogicLoc` 子步骤 + `code-check` 步骤 8 评审新增"代码行数超标"发现维度
- 关键交叉点(每条 FR 对应设计章节):
 - FR-1 逻辑行计算函数 → §6 模块 + §5 算法
 - FR-2 工具集成 tokei/cloc/启发式回退 → §5 算法 + §9 边界
 - FR-3 `code-it` 步骤 8 末尾追加 `calcLogicLoc` → §6 模块 + §10 测试
 - FR-4 `code-check` 步骤 8 评审新增"代码行数超标"发现 → §6 模块
 - FR-5 阈值配置(可选)→ §5 算法 + §7 接口

## 上游概要设计

- 来源:`./assistants/V0.0.3/design/REQ-00039/RESULT.md`(v1,2026-06-22 14:30)
- 提取:**5 模块 / 4 函数 / 1 阈值配置**
- 关键决策:共享库位于 `code-it/lib/`(沿用 `module-conventions §规则 1`);tokei/cloc 检测 + 启发式回退;缺陷分支不触达;默认阈值 500 / 200
- 关键交叉点(每条模块对应本详细设计章节):
 - `logic-loc.md` → §4 模块详细化
 - `logic-loc-defaults.md` → §4 模块详细化
 - `code-it/SKILL.md` 改造 → §4 模块详细化 + §5 算法
 - `code-check/SKILL.md` 改造 → §4 模块详细化 + §5 算法
 - `code-it/templates/RESULT.md` 改造 → §4 模块详细化

## 项目现状(实现细节)

### 命名风格

- SKILL.md frontmatter:`name` / `description` YAML 字段(kebab-case)
- 文档标题:`# <类型> — <标题>`(中文 + 半角破折号 ` — ` + 自由标题)
- 文档头:`- <key>: <value>`(中文 key + 值;沿用既有 11 个标准 key)

### 错误模型

- 本需求是 Markdown 改造,**无**运行时错误
- 屏显错误沿用既有 `⚠` / `✗` / `⛔` 字符(沿用 REQ-00013)

### 既有相似功能

- `code-it` 步骤 8a 项目可测性守卫 7 项检查 → 沿用屏显契约 `=== code-it 守卫通过 ===` / `⏭ code-it 守卫不通过 ===`(本需求 `calcLogicLoc` 沿用相同格式)
- `code-check` 步骤 8.12 行数比例警告 → 沿用屏显契约 `[代码行数超标] <file>`(本需求 §8.13 同构)
- `code-it` 步骤 13 撰写 RESULT.md → 沿用模板"## 单元测试(由 code-it 内化)"小节格式(本需求"## 逻辑行统计(由 code-it 内化)"同构)

### 可复用资产

- 既有 tokei / cloc 系统命令(本仓库**不**安装)
- `code-check` 评审维度速查表(12 维度字节级保留,新增第 13 维度)
- `code-it` 步骤 8a / 8.5 屏显契约(本需求 `calcLogicLoc` 同构沿用)

## 本次变更源(增量更新时)

(无 — 本轮为首次规划)