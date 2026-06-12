# 材料登记 — REQ-00031

更新时间:2026-06-12 15:13
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

- 来源:用户口头需求(2026-06-12 15:11)
  - "优化 `/code-plan` 规划任务时,每个任务应该确保编译或运行成功,而不是单独规划一个编译运行检测的任务,也不需要在任务阶段编写单元测试功能。"
- 补充澄清(2026-06-12 15:18,用户原文):
  - "/code-unit 技能的作用就是单纯的编写单元测试和执行测试"
  - "/code-it 技能就是编码,并确保正常编译运行"
  - "功能明确,界限清晰"
  - "/code-plan 任务规划只规划编码部分,不包含规划单元测试部分"
  - "单元测试技能是根据不同项目可选使用的"

## 项目现状(本次扫描)

### 项目类型
- 仓库:Claude Code plugin 仓库(marketplace 协议)
- 语言:Markdown(元技能定义) + 少量 JSON / YAML
- 关键依赖:无(本仓库不声明任何工具链)

### 关键文件清单(被改)
- `plugins/code-skills/skills/code-plan/SKILL.md` §步骤 10A"任务拆分原则" + §"任务双状态字段"
- `plugins/code-skills/skills/code-it/SKILL.md` 文档头 "## 目标" 小节
- `plugins/code-skills/skills/code-unit/SKILL.md` 文档头 "## 目标" 小节
- `plugins/code-skills/skills/code-auto/SKILL.md §步骤 4 任务循环` 子节
- `plugins/code-skills/skills/code-plan/templates/plan.md` "任务类型" / "测试状态" 字段

### 既有相关 REQ
- REQ-00030(本版本):优化 `/code-design` 与 `/code-plan` 职责分离 — **本需求的"姐妹需求"**
- REQ-00020(V0.0.2):`code-design` / `code-plan` 步骤 0b 7 维度问路
- REQ-00014(V0.0.2):架构骨架作为首个任务
- REQ-00017(V0.0.2):拆任务约束(实际产出候选集)
- REQ-00007(V0.0.2):`code-auto` 任务循环原 "code-unit 是否调用" 逻辑
