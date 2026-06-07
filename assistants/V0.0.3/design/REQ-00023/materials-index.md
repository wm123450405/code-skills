# 材料登记 — REQ-00023
更新时间:2026-06-07
版本:V0.0.3

## 项目级规范
| 规范文件 | 类别 | 关键约束摘要 | 本需求触发 |
| --- | --- | --- | --- |
| dashboard-conventions.md | 看板 | §规则 1:看板字段约定扩展需多文件同步(version-RESULT.md + CLAUDE.md + 本规范) | **不**触发(本需求零新增看板字段) |
| skill-conventions.md | 技能 | §规则 1:SKILL.md frontmatter 同步扩展 | **不**触发(本需求仅改既有 SKILL.md,不改 frontmatter) |
| module-conventions.md | 模块 | §规则 1:技能资源摆放 | **不**触发(无新增模块) |
| encoding-conventions.md | 编码 | §规则 1+3:任务编号双格式(新 TASK-(REQ|BUG)-NNNNN-NNNNN / 旧 (REQ|BUG)-NNNNN-NNNNN) | 沿用,本需求解析时不归一化(AC-1.1 用例) |
| doc-conventions.md | 文档 | 文档措辞约定 | 沿用 |
| naming-conventions.md | 命名 | 文件/目录命名 | 沿用,本需求零新增 |
| directory-conventions.md | 目录 | 目录结构 | 沿用,本需求零新增 |
| framework-conventions.md | 框架 | 框架选择 | 沿用,本需求零新增 |
| dependency-conventions.md | 依赖 | 依赖管理 | 沿用,本需求零新增 |
| commit-conventions.md | 提交 | 提交消息 | 沿用 `chore(code-design): <需求编码> ...` |
| coding-style.md | 编码 | 编码风格 | 沿用,本需求零源码 |
| marketplace-protocol.md | 协议 | Claude Code marketplace 协议 | 沿用,本需求零改动 |
| migration-mapping.md | 迁移 | V0.0.0~V0.0.2 历史 0 追溯 | 沿用,本需求零追溯 |

**触发判定小结**:本需求**不**触发 `dashboard-conventions §规则 1` 三同步(INV-8 锁定 0 新增字段);**不**触发 `skill-conventions §规则 1` 同步(INV-1 + INV-2 锁定 frontmatter 字节级保留);零模块新增;零依赖新增。

## 上游需求
- 来源:./assistants/V0.0.3/require/REQ-00023/RESULT.md
- 创建时间:2026-06-07
- 提取的 FR / NFR / AC 数量:6 FR / 9 NFR / 8 AC / 9 INV / 3 待澄清 Q
- 关键约束:零新增看板字段(沿用 dashboard-conventions §规则 1 触发判定);零修改其他 12 个 `code-*` 技能 SKILL.md(沿用 NFR-6)

## 项目现状(本次扫描)

### 项目类型
- 类型:Claude Code 技能集合(marketplace 协议布局)
- 语言:Markdown(技能定义 + 模板 + 指南)+ JSON(marketplace.json / plugin.json)
- 关键依赖:无 NPM / Python 依赖;`code-*` 技能由 Claude Code 平台托管

### 目录结构
```
code-skills/                          ← marketplace 仓库根
├── .claude-plugin/marketplace.json
└── plugins/code-skills/              ← 插件本体
    ├── .claude-plugin/plugin.json
    ├── CLAUDE.md
    ├── README.md / README.en.md
    └── skills/                       ← 14 个 code-* 技能
        ├── code-auto / code-check / code-dashboard / ...
        ├── code-dashboard/           ← 本需求改造对象
        │   ├── SKILL.md              ← 总览模式改造范围
        │   ├── guidelines/           ← 指南(本需求零改)
        │   └── templates/            ← 模板(本需求零改)
        └── ...
```

### 已有模块(本需求相关)
| 模块/路径 | 职责 | 是否可复用 |
| --- | --- | --- |
| `code-dashboard/SKILL.md` | 看板技能(总览 + 需求模式) | **修改既有**(本需求对象) |
| `code-dashboard/SKILL.md` §附录 A 任务编号解析(算法 4) | parseTaskId 双格式 | 复用,零改 |
| `code-dashboard/SKILL.md` §附录 B ASCII 比例条(算法 5) | renderBar 12 字符 | 复用,零改 |
| `code-dashboard/SKILL.md` §附录 C 建议数据结构 | Suggestion 3 字段 | 复用,补 1 段(零结构变更) |

### 已有第三方依赖
**无**(本仓库是 Claude Code 技能集合,零外部代码依赖)

### 编码与构建约定
- SKILL.md 全部用 Markdown + YAML frontmatter(L1-3 字节级保留)
- 技能间用 `Skill` 工具调用,零 IPC
- 所有 `code-*` 技能均版本感知(读 `./assistants/.current-version`)
- 提交消息约定 `chore(<技能>): <需求编码> <标题>`

## 命令行参数
- 本次未传 `--result`(code-auto 上下文自动跳过,沿用 REQ-00007 Q-4)
- `--result` 缺省行为:本技能只产出 `RESULT.md`,**不**产出 `DESGIN.<ext>`

## 模板填充结果
- 未触发(无 `--result` 参数)
