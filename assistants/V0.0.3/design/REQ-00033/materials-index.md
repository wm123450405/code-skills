# 材料登记 — REQ-00033

更新时间:2026-06-15 12:20
版本:V0.0.3
需求编码:REQ-00033

## 1. 项目级规范(本需求相关)

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| skill-conventions.md | 技能 | SKILL.md frontmatter L1-3 字节级保留;`name` 与目录名一致 |
| module-conventions.md | 模块(已弃用,迁 directory-conventions) | 资源放 templates/ / checklists/ / guidelines/ |
| doc-conventions.md | 文档 | README 中英版本结构对仗;主语言版本完整 |
| dashboard-conventions.md | 看板 | 字段扩展三方同步 |
| commit-conventions.md | 提交 | `chore(<skill>):` 前缀 |
| encoding-conventions.md | 编码 | 需求编号 5 位纯数字;接收端可放宽 |
| marketplace-protocol.md | 插件 | plugin.json / marketplace.json 引用一致 |

## 2. 上游需求

- 来源:`./assistants/V0.0.3/require/REQ-00033/RESULT.md`(已存在)
- 版本:V0.0.3(2026-06-15 11:10)
- 提取:4 FR / 11 NFR / 23 AC;1 任务规模;0 触发扩展性

## 3. 项目现状(本次扫描)

### 3.1 待改造文件

| 路径 | 当前状态 | 改造范围 |
| --- | --- | --- |
| `plugins/code-skills/skills/code-require/SKILL.md` | 既有 | §"不要做的事"小节末尾追加 1 条 |

### 3.2 项目类型

- **类型**:Claude Code skills 仓库(元技能仓库)
- **语言**:Markdown(无工程代码)
- **框架**:Claude Code skills 协议

### 3.3 既有可复用资产

- `plugins/code-skills/skills/code-require/SKILL.md` §"不要做的事" 小节已有 8 条硬约束(沿用 BUG-00001 / REQ-00026 / ...);本需求追加 1 条
- `assistants/V0.0.3/RESULT.md` §"需求清单" / §"变更记录"(沿用既有结构)

## 4. 步骤 4 预检(规范 vs 需求冲突)

- 需求要求"修改 SKILL.md"vs `skill-conventions.md` 要求"frontmatter 字节级保留"→ **不冲突**(本需求**不**改 frontmatter,只改 §"不要做的事" 小节末尾)
- 需求要求"不修改 `templates/requirements.md`"vs `module-conventions.md` 要求"资源放 `templates/`"→ **不冲突**(本需求**不**改模板,只改 SKILL.md)
- 需求要求"对偶引用 `code-design`"vs 既有 5 FR 的"不修改其他 11 个 SKILL.md"→ **不冲突**(对偶引用**只**在 `code-require` SKILL.md 内,不修改 `code-design` SKILL.md)
- **结论**:0 冲突,0 待澄清

## 5. 设计目标确认(code-auto 上下文检测到,采纳 `--balanced` 默认 0 问)

- 整体设计目标:`--balanced`
- 维度优先级:功能性 = 低(本需求是"职责边界显式化"型,不是功能性需求)
- 触发条件:小需求(1 任务) + 扩展性不触发 → 0 问(沿用 REQ-00030 FR-2 收敛)

## 6. 关联需求

| 需求 | 关联点 |
| --- | --- |
| BUG-00001 | "不修改 SKILL.md"硬约束范式(§"不要做的事" 段) |
| REQ-00026 | SKILL.md 描述通用化扫除;最小化变更原则 |
| REQ-00030 | 元技能改 + 12 维度评审 + INV 字节级保留 |
| REQ-00031 | 元技能改 /code-plan /code-it /code-unit /code-auto |
| REQ-00032 | `code-require` 屏显契约(锚点不交叉) |
