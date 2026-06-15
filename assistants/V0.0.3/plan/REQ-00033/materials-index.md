# 材料登记 — REQ-00033

更新时间:2026-06-15 12:30
版本:V0.0.3
需求编码:REQ-00033

## 1. 项目级规范(本需求相关)

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| skill-conventions.md | 技能 | SKILL.md frontmatter L1-3 字节级保留 |
| module-conventions.md | 模块(已弃用) | 资源放 templates/ / checklists/ / guidelines/ |
| doc-conventions.md | 文档 | README 中英版本结构对仗 |
| dashboard-conventions.md | 看板 | 字段扩展三方同步 |
| commit-conventions.md | 提交 | `chore(<skill>):` 前缀 |
| encoding-conventions.md | 编码 | 需求编号 5 位纯数字;接收端可放宽 |
| marketplace-protocol.md | 插件 | plugin.json / marketplace.json 引用一致 |

## 2. 上游需求

- 来源:`./assistants/V0.0.3/require/REQ-00033/RESULT.md`
- 提取:4 FR / 11 NFR / 23 AC;1 任务规模

### 关键交叉点(每条 FR 对应设计章节)

| FR | 设计章节 |
| --- | --- |
| FR-1 `code-require` 0 产出技术选型 | (本设计是"不产出"约束,无算法/接口变更) |
| FR-2 在 `code-require/SKILL.md` §"不要做的事" 追加 1 条 | §3 模块详细化 / §4 算法与逻辑 |
| FR-3 对偶引用 `code-design` 承担技术选型 | §3 模块详细化(措辞内嵌对偶引用) |
| FR-4 不修改其他 11 个 `code-*` 技能 SKILL.md | §10 不变量(INV-4) |

## 3. 上游概要设计

- 来源:`./assistants/V0.0.3/design/REQ-00033/RESULT.md`
- 提取:5 决策 / 9 不变量 / 0 模块 / 0 接口 / 0 数据结构 / 0 依赖
- 整体设计目标:`--balanced`(功能性 = 低)

## 4. 项目现状(实现细节)

- **类型**:Claude Code skills 仓库(元技能仓库)
- **语言**:Markdown(无工程代码)
- **编码风格**:沿用既有 `code-require/SKILL.md` §"不要做的事" 小节列表项风格
- **既有相似功能**:`code-require/SKILL.md` 已有 8 条硬约束列表项(沿用 BUG-00001 / REQ-00026 / ...);本需求追加第 9 条

## 5. 规范 vs 设计冲突(0 冲突)

- 设计要求"修改 SKILL.md"vs `skill-conventions.md` 要求"frontmatter 字节级保留"→ **不冲突**(本设计**不**改 frontmatter)
- 设计要求"不修改 `templates/requirements.md`"vs `module-conventions.md` → **不冲突**
- 0 冲突,0 待澄清

## 6. 本次变更源(本设计不涉及增量,首次设计分支)

不适用(本需求是首次设计,无变更源识别)
