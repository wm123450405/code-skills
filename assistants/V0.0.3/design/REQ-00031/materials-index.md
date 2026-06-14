# 材料登记 — REQ-00031

更新时间:2026-06-12 15:25
版本:V0.0.3

## 项目级规范

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| skill-conventions.md | 技能 | SKILL.md frontmatter L1-3 字节级保留 |
| module-conventions.md | 模块 | 资源文件放 templates/ 子目录(DEPRECATED) |
| doc-conventions.md | 文档 | README 多语言对仗 |
| dashboard-conventions.md | 看板 | 看板字段三方同步 |
| commit-conventions.md | 提交 | `chore(<skill>):` 前缀 |
| encoding-conventions.md | 编码 | 5 位纯数字生成端 + 字符集放宽接收端 |
| naming-conventions.md | 命名 | 沿用 kebab-case(目录) / 中英混排(标题) |

## 上游需求

- 来源:./assistants/V0.0.3/require/REQ-00031/RESULT.md
- 版本:v1(2026-06-12 15:13)
- 提取的 FR / NFR / AC 数量:**7 FR / 5 NFR / 3 大类共 20 AC / 5 Q(全部已澄清)**

## 项目现状(本次扫描)

### 项目类型
- 仓库:Claude Code plugin 仓库(marketplace 协议)
- 语言:Markdown(元技能定义) + 少量 JSON / YAML
- 关键依赖:无(本仓库不声明任何工具链)

### 目录结构(被改文件相关)
- `plugins/code-skills/skills/code-plan/SKILL.md` — 待修改(§步骤 10A 任务粒度原则)
- `plugins/code-skills/skills/code-it/SKILL.md` — 待修改(## 目标)
- `plugins/code-skills/skills/code-unit/SKILL.md` — 待修改(## 目标)
- `plugins/code-skills/skills/code-auto/SKILL.md` — 待修改(§步骤 4 任务循环 步骤 4.b)
- `plugins/code-skills/skills/code-plan/templates/plan.md` — 待修改(任务类型 + 测试状态字段)

### 已有模块
| 模块/路径 | 职责 | 是否可复用 |
| --- | --- | --- |
| code-plan §步骤 10A "任务拆分原则" | 定义任务粒度(0.5-2 天 / 可独立验证 / 1 个功能点) | 需扩展(追加"完成定义含编译/运行" + 移除 `测试` 类型) |
| code-it §步骤 9-12 | 编译/启动/测试验证 + 错误修复循环 | 字节级保留(本需求只改文档头) |
| code-unit §步骤 0-15 | 单元测试编写 + 执行 | 字节级保留(本需求只改文档头) |
| code-auto §步骤 4 任务循环 | 串行调 code-it + 条件调 code-unit | 需改写(步骤 4.b "按需调用" → "恒等跳过") |

### 已有接口
- 任务粒度接口(由 `code-plan` 步骤 10A 定义)→ `code-it` 消费
- 任务循环接口(由 `code-auto` 步骤 4 定义)→ `code-it` / `code-unit` 消费
- 评审接口(由 `code-check` §8.7 定义)→ 任务"测试状态"消费

### 已有数据模型
- `PLAN.md 任务总览.任务类型` 候选集 6 类 → 收窄为 5 类
- `PLAN.md 任务总览.测试状态` 枚举 6 个 → 收窄为 2 个

### 已有第三方依赖
- 无(INV-8 字节级沿用)

### 编码与构建约定
- 沿用既有 Markdown 风格(代码块、表格、列表、锚点)
- 文档头 frontmatter L1-3 字节级保留(INV-1)
- "## 不要做的事" 小节字节级保留(INV-2)
- 既有"## 工作流程"步骤字节级保留(INV-3)
