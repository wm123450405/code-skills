# 材料登记 — REQ-00030

更新时间:2026-06-12 14:25
版本:V0.0.3

## 项目级规范

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `skill-conventions.md §规则 1` | 技能元信息 | SKILL.md 必含 `name`(=目录名,kebab-case) + `description`;frontmatter L1-3 字节级保留 |
| `module-conventions.md §规则 1`(已弃用,沿用历史) | 资源摆放 | 资源文件必须放 `templates/` / `checklists/` / `guidelines/` 子目录,禁止散落 |
| `doc-conventions.md §规则 1` | 文档 | README 多语言版本必须保持结构对仗 |
| `dashboard-conventions.md §规则 1` | 看板 | 看板字段三方同步(本需求不触发字段扩展) |
| `encoding-conventions.md §规则 1/3` | 编码 | 任务编号正则;接收端宽松 `[A-Za-z0-9.\-_]+` |
| `naming-conventions.md` | 命名 | kebab-case 技能目录名 |
| `coding-style.md` | 编码风格 | (本需求不涉及源代码) |
| `commit-conventions.md` | 提交 | `chore(<skill>):` 前缀;格式沿用既有 5 类 |
| `framework-conventions.md` | 框架 | (本仓库无框架) |

## 上游需求

- 来源:`./assistants/V0.0.3/require/REQ-00030/RESULT.md`
- 状态:已完成
- 提取:**8 FR / 6 NFR / 9 AC / 3 待澄清 / 5 关联需求(REQ-00011/14/17/20/23/28/29)**
- 关键交叉点(每条 FR 对应到本设计章节):

| 上游 FR | 概要设计对应章节 | 状态 |
| --- | --- | --- |
| FR-1 步骤 0b 扩展性判定规则 | §3.2 步骤 0b 自适应问路 | 涉及 |
| FR-2 步骤 0b 收紧 | §3.2 步骤 0b 自适应问路 | 涉及 |
| FR-3 设计步骤 9A/10A/11A 输出深度 | §3.3 概设深度收窄 + §5 模块拆分 + §6 接口概要 + §7 数据结构 | 涉及 |
| FR-4 templates/design.md 重写 | §3.4 模板重写 | 涉及 |
| FR-5 code-plan 补做强化 | §3.5 code-plan 补做职责(本设计**不**深入详设,仅标引用) | 涉引用 |
| FR-6 架构骨架触发条件 | §3.6 架构骨架(本设计**不**深入详设,仅标引用) | 涉引用 |
| FR-7 code-check 评审清单新增 3 个校验点 | §3.7 code-check 评审清单 | 涉及 |
| FR-8 扩展性三阶段下沉 | §3.8 扩展性三阶段下沉 | 涉及 |

## 项目现状(本次扫描)

### 项目类型

- **类型**:Claude Code 技能集合 / marketplace 协议布局
- **顶层目录**:
  - `.claude-plugin/marketplace.json`:marketplace 清单
  - `plugins/code-skills/`:本插件本体
  - `assistants/`:版本工作空间(只读,本技能不修改)
- **关键约束**:仓库**不**包含源代码、构建系统、测试框架、Lint 工具或包管理配置(`CLAUDE.md` §"需与用户确认的约定"明确锁定)

### 目录结构(本设计影响面)

| 路径 | 状态 | 职责 |
| --- | --- | --- |
| `plugins/code-skills/skills/code-design/SKILL.md` | **修改** | 步骤 0b / 9A / 10A / 11A 内容修订 |
| `plugins/code-skills/skills/code-design/templates/design.md` | **修改** | §7 / §8 / §9 章节重写 |
| `plugins/code-skills/skills/code-plan/SKILL.md` | **修改** | 步骤 7A / 10A 语义强化 |
| `plugins/code-skills/skills/code-plan/templates/plan.md` | **修改** | §4-§10 章节强约束必填 |
| `plugins/code-skills/skills/code-check/SKILL.md` | **修改** | 评审清单追加 3 个校验点 |
| `plugins/code-skills/skills/code-check/templates/review-checklist.md`(若有) | **修改** | 同步 3 个校验点 |
| 其他 11 个 `code-*` 技能 SKILL.md | 0 改 | INV-3 字节级保留(对照 REQ-00020 既有约束) |
| `plugins/code-skills/skills/code-design/{materials-index,design-notes,module-breakdown,dependencies,related-designs,rule-compliance,clarifications}.md` | 0 改 | 既有模板沿用(本需求不重命名/不移除) |
| `./assistants/rules/*.md` | 0 改 | 跨版本规范,本需求不修改 |
| `marketplace.json` / `plugin.json` / `CLAUDE.md` | 0 改 | INV-3 字节级保留 |
| `README.md` / `README.en.md` | 0 改 | 与本需求无关联(本需求不涉及技能表变化) |

### 已有模块(可复用)

- `code-design/SKILL.md` 步骤 0a / 0b.0 / 0 / 1 / 2 / 3 / 4 / 5 / 6 / 12A / 13A / 14A / 15A / 7B-10B:本设计**不**重写,字节级保留
- `code-plan/SKILL.md` 步骤 0a / 0b.0 / 0b / 0 / 1 / 2 / 3 / 4 / 5 / 6 / 8A / 9A / 11A / 12A / 13A / 14A / 16A / 17A / 18A / 7B-13B:本设计**不**重写
- `code-check/SKILL.md` 既有评审清单:本设计**追加**(不重写)
- `code-design/templates/design.md` §3-§6 / §11-§16:本设计**不**重写
- `code-plan/templates/plan.md` §1-§3 / §13-§15:本设计**不**重写

### 已有接口 / 数据模型 / 第三方依赖

- N/A(本需求不涉及外部接口/数据结构/三方依赖变更;仅修改 SKILL.md 步骤定义与 templates 章节)

### 编码与构建约定

- 沿用既有:`commit-conventions.md` 锁定 `chore(<skill>):` 前缀 + FR/NFR/AC 统计行
- 沿用既有:`skill-conventions §规则 1` 锁定 frontmatter L1-3 字节级保留
- 沿用既有:`dashboard-conventions §规则 1` 锁定看板字段(本需求**不**触发字段扩展)

## 命令行参数

无 `--result` 参数,本轮**不**触发模板填充步骤(沿用 REQ-00007 Q-4)。
