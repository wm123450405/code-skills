# 材料登记 — REQ-00038

更新时间:2026-06-22 13:30
版本:V0.0.3

## 1. 项目级规范

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `architecture.md` | 功能架构 | (本仓库无) |
| `module-conventions.md` | 模块规划 | ⚠️ DEPRECATED(已迁移到 `directory-conventions.md`) |
| `api-standards.md` | 接口定义 | (本仓库无) |
| `data-modeling.md` | 数据结构 | (本仓库无) |
| `security.md` | 安全 | (本仓库无) |
| `performance.md` | 性能 | (本仓库无) |
| `testing.md` | 测试 | (本仓库无) |
| `observability.md` | 可观测性 | (本仓库无) |
| `dashboard-conventions.md` | 看板 | 看板字段扩展需三方同步(`templates/version-RESULT.md` + `CLAUDE.md` + 本规范自身);本需求不触发 |
| `doc-conventions.md` | 文档 | README 多语言对仗;本需求不涉及 README 改动 |
| `coding-style.md` | 编码风格 | (读取待补充) |
| `commit-conventions.md` | 提交规范 | `chore(code-it): REQ-00038 ...` 字面格式 |
| `directory-conventions.md` | 目录结构 | 替代旧 `module-conventions.md`(实际内容"待添加",无强制约束) |
| `encoding-conventions.md` | 命名编码 | `^TASK-REQ-\d{5}-\d{5}$` 任务编码格式;接收端放宽为 `[A-Za-z0-9.\-_]+` |
| `framework-conventions.md` | 框架 | (本仓库无外部框架约束) |
| `marketplace-protocol.md` | marketplace | Claude Code 插件市场协议 |
| `migration-mapping.md` | 迁移映射 | (本仓库无迁移历史) |
| `naming-conventions.md` | 命名约定 | kebab-case |
| `skill-conventions.md` | 技能编写 | §规则 1:frontmatter `name`+`description` 必含;§规则 2:SKILL.md / templates/ 中不得含 6 类开发痕迹字面 |
| `dependency-conventions.md` | 依赖管理 | (本仓库无第三方依赖) |

**本需求消费的规范条款**:
- `skill-conventions §规则 1`(frontmatter 字节级保留 — INV-1)
- `skill-conventions §规则 2`(无 6 类开发痕迹 — INV-2 / INV-3 / INV-4)
- `dashboard-conventions §规则 1`(看板字段扩展三方同步 — 本需求 0 触发,看板只追加既有区段内的行)
- `encoding-conventions §规则 1`(任务编码格式 — 接收端放宽正则,本需求不涉及)
- `naming-conventions.md`(kebab-case — INV-1 / INV-4)

## 2. 上游需求

- 来源:`./assistants/V0.0.3/require/REQ-00038/RESULT.md`
- 版本:v1(2026-06-22 13:00)
- 提取的 FR 数量:5(FR-1 模块识别 / FR-2 模块级守卫 / FR-3 模块级单测输出 / FR-4 模板多模块支持 / FR-5 code-plan 字面改写)
- 提取的 NFR 数量:6(NFR-1 性能 / NFR-2 兼容性 / NFR-3 零规范变更 / NFR-4 不归一化 / NFR-5 可追溯 / NFR-6 幂等)
- 提取的 AC 数量:7(AC-1 ~ AC-7,全部对应 FR-1 ~ FR-3 / NFR-2 / NFR-3)

## 3. 项目现状(本次扫描)

### 3.1 项目类型

- 语言:Markdown 自然语言 + Claude Code 技能插件集合
- 框架:Claude Code 技能市场协议(`marketplace-protocol.md`)
- 关键依赖:无

### 3.2 目录结构

- 顶层:`./assistants/<版本>/`、`./plugins/code-skills/skills/<name>/`、`./assistants/rules/`
- 本次扫描范围:`./plugins/code-skills/skills/code-it/` + `./plugins/code-skills/skills/code-plan/` + `./assistants/V0.0.3/require/REQ-00038/`

### 3.3 已有模块

| 模块/路径 | 职责 | 是否可复用 |
| --- | --- | --- |
| `code-it/SKILL.md` § 步骤 8a — 项目可测性守卫 | 7 项守卫检查(REQ-00034 落地) | 是(本需求扩展位置) |
| `code-it/SKILL.md` § 步骤 8.5 — 按需写单测 | 按需写单测(REQ-00034 落地) | 是(本需求扩展位置) |
| `code-it/templates/RESULT.md` § ## 9. 单元测试(由 code-it 内化) | 单元测试结果记录 | 是(本需求追加"## 各模块单测结果"小节) |
| `code-plan/SKILL.md` § ## 步骤 10A 任务拆分 | 任务拆分粒度 | 是(本需求字面改写 1 句) |

### 3.4 已有接口

- `code-it` 步骤 8a 守卫(L555-645):工程根级 7 项守卫
- `code-it` 步骤 8.5 单测输出(L646-715):写单测到 CWD 下项目测试目录
- `code-plan` 任务粒度描述:既有"由 `code-it` 内化(`code-it` 步骤 8a 守卫 + 步骤 8.5 按需写单测)"

### 3.5 已有数据模型

- `code-it` 步骤 8a 守卫结果:`testable: boolean`(工程根级)
- `code-it` 步骤 8.5 单测输出位置:CWD 下项目测试目录

### 3.6 已有第三方依赖

- 无(本仓库是 Claude Code 技能插件集合,无外部运行时依赖)

### 3.7 编码与构建约定

- 提交规范:`chore(<技能>): REQ-NNNNN ...` 字面格式
- 命名约定:kebab-case
- frontmatter:`name` + `description` 必含;`name` 与目录名一致
- SKILL.md / templates/ 不得含 6 类开发痕迹字面(skill-conventions §规则 2)

## 4. 关联材料登记

| 关联 ID | 类型 | 路径 | 关联点 |
| --- | --- | --- | --- |
| REQ-00034 | 设计 | `./assistants/V0.0.3/design/REQ-00034/RESULT.md` | `code-unit` 整合进 `code-it`,7 项守卫工程根级框架 |
| REQ-00031 | 需求 | `./assistants/V0.0.3/require/REQ-00031/RESULT.md` | `code-unit` 退场为可选(沿用) |
| REQ-00037 | 设计 | `./assistants/V0.0.3/design/REQ-00037/RESULT.md` | 缺陷修复流程的状态推进(沿用) |
| BUG-00001 | 缺陷 | `./assistants/V0.0.3/fix/BUG-00001/RESULT.md` | "不修改 SKILL.md"硬约束(沿用) |