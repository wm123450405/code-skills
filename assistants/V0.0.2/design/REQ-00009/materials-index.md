# 材料登记 — REQ-00009
更新时间:2026-06-05 17:10
版本:V0.0.2

## 项目级规范
| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `skill-conventions.md` | 技能编写 | §规则 1:frontmatter 必含 name+description,name=目录名 |
| `module-conventions.md` | 模块规划(DEPRECATED) | §规则 1:资源放固定子目录(templates/checklists/guidelines) |
| `dashboard-conventions.md` | 看板与版本工作空间 | §规则 1:字段约定扩展需 3 处同步(本需求不触发) |
| `doc-conventions.md` | 文档编写 | §规则 1:中英同次提交;§规则 2:核心小节覆盖 |
| `marketplace-protocol.md` | Marketplace 协议 | §规则 1:skills 数组以 `./` 开头 |
| `encoding-conventions.md` | 编码格式 | §规则 1-4:任务编号 5+5 位嵌套式 |
| `migration-mapping.md` | 编码迁移 | §规则 1-4:EXISTING-NNN 不追溯 |

**占位规范(6 个,不影响)**:`directory-conventions.md` / `coding-style.md` / `commit-conventions.md` / `dependency-conventions.md` / `framework-conventions.md` / `naming-conventions.md`

## 上游需求
- 来源:`./assistants/V0.0.2/require/REQ-00009/RESULT.md`
- 版本:v1(已锁定)
- 提取的 FR / NFR / AC 数量:**7 FR / 8 NFR / ~25 AC**
- 3 项已锁定(Q-1/Q-2/Q-3)+ 4 项采纳默认(Q-4/Q-5/Q-6/Q-7)+ 1 项建议派生(Q-8)

## 项目现状(本次扫描)
### 项目类型
- 语言/框架:纯 Markdown 文档型项目(无源代码 / 无构建 / 无测试框架)
- 关键依赖:Claude Code 工具集(`Skill` / `Read` / `Edit` / `Bash` / `Glob` / `Grep` / `Write`)

### 目录结构
```
code-skills/                                  # marketplace 仓库根
├── .claude-plugin/marketplace.json
├── assistants/                               # 版本工作空间
│   ├── rules/                                # 项目级规范(跨版本,本技能只读)
│   ├── .current-version
│   └── V0.0.2/                               # 当前激活版本
│       ├── RESULT.md                         # 版本看板
│       ├── require/REQ-00009/RESULT.md       # 本需求上游
│       └── ...(其他需求产物)
├── plugins/code-skills/                      # 插件本体
│   └── skills/
│       ├── code-init/                        # 工程初始化
│       ├── code-version/                     # 版本管理
│       ├── code-rule/                        # 编码规范
│       ├── code-require/                     # 需求分析
│       ├── code-design/                      # 概要设计
│       ├── code-plan/                        # 详细设计 / 实施计划
│       ├── code-it/                          # 开发编码
│       ├── code-unit/                        # 单元测试 ← 本需求修改目标
│       ├── code-fix/                         # 缺陷登记
│       └── code-review/                      # 代码评审
│       └── (新) code-merge/                  # 缺陷合并(V0.0.2)
│       └── (新) code-auto/                   # 自动开发编排(V0.0.2)
```

### 已有模块(code-unit 自身)
- 路径:`plugins/code-skills/skills/code-unit/`
- 现有文件:
  - `SKILL.md`(453 行,frontmatter + 17 章节)
  - `templates/RESULT.md`(测试改修总结模板)
  - `templates/test-spec.md`(测试规格模板)
  - `templates/assistants-layout.md`(工作空间范式文档)
- 既有"步骤 0" = 版本上下文检测(读 `.current-version`)
- 既有"步骤 1-16" = 完整单测流程(从收集任务编码到更新看板)
- 既有 E-1~E-7 = 边界场景(无 `.current-version` / 任务不存在 / 开发未完成 / 阻塞 / 等)

### 已有接口(code-unit 入口)
- `Skill: code-unit <任务编码>` — 由用户或 `code-auto` 调用
- 输入:任务编码(格式 `TASK-(REQ|BUG)-\d{5}-\d{5}`)
- 输出:
  - `test/<任务编码>/RESULT.md`(+ 4 份过程文档)
  - `PLAN.md` 中本任务"测试状态"字段推进
  - `RESULT.md` 看板"任务清单"区段对应行更新
- 退出码:0(成功)/ ≠ 0(失败)

### 已有数据模型
- 看板"任务清单"区段列:任务编号 / 需求 / 类型 / 触发/来源 / 标题 / 开发状态 / 测试状态 / 涉及文件 / 完成时间 / 提交哈希 / 关联任务
- 测试状态枚举:`未编写` / `已编写` / `已运行-通过` / `已运行-失败` / `不适用` / `阻塞`(V0.0.1 既有)

### 已有第三方依赖
- **0** 第三方依赖(纯 Claude Code 工具集)

### 编码与构建约定
- SKILL.md 章节结构:frontmatter + 17 章节(目标 / 适用场景 / 不适用 / 目录约定 / 输入 / 输出 / 工具 / 工作流步骤 / 过程文档格式 / 衔接 / 不要做的事)
- 既有"步骤 X"命名约定:数字 + 中文标题(本需求沿用)
- 既有"步骤 0a"模式(沿用 REQ-00005 / REQ-00010 的命名):首步 + 子步骤,用于"在主步骤之前的辅助检查"

### 可复用资产
- 既有"步骤 0"代码(版本上下文检测)— **不**修改,本需求在"步骤 0"**之前**插入"步骤 0a"
- 既有"步骤 1-16"代码(单测流程)— **不**修改,本需求守卫通过后直接走原流程
- 既有"测试状态"字段写入路径(`code-unit` 步骤 14)— 沿用,本需求守卫不通过时复用同一写入路径
- 既有"不适用"枚举(V0.0.1 模板)— 沿用,本需求**不**新增枚举值
