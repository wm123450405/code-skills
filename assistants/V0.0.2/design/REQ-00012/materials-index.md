# 材料登记 — REQ-00012
更新时间:2026-06-05
版本:V0.0.2

## 项目级规范
| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| doc-conventions.md | 文档 | §规则 1:中英 README 同次提交 + 章节对仗;§规则 2:核心小节覆盖(主语言版本) |
| commit-conventions.md | 提交 | 占位规则(本次无直接约束,NFR-7 要求 1 行 message 习惯) |
| directory-conventions.md | 目录 | 占位规则(本次无直接约束) |
| skill-conventions.md | 技能 | 规则 1:技能元信息一致性(本次不涉及) |
| module-conventions.md | 模块 | 模块边界(本次不涉及) |
| naming-conventions.md | 命名 | 命名约定(本次不涉及) |
| 其他 7 个规范 | 编码/数据/依赖 | 本次不涉及 |

## 上游需求
- 来源:./assistants/V0.0.2/require/REQ-00012/RESULT.md
- 版本:v1(2026-06-04 15:11)
- 提取的 FR / NFR / AC 数量:7 FR / 8 NFR / 约 25 AC

## 项目现状(本次扫描)
### 项目类型
- 仓库类型:Claude Code marketplace 仓库
- 语言:Markdown(纯文档类) + YAML 配置
- 框架:N/A(本需求不涉及代码)

### 目录结构(本需求相关部分)
```
D:\Workspaces\wm\code-skills\         # 仓库根
├── .claude/
├── .claude-plugin/
├── .git/                              # 仓库根无 README.md / CLAUDE.md
├── .gitignore
├── assistants/
│   ├── .current-version                # V0.0.2
│   ├── rules/                          # 13 个规范文件
│   └── V0.0.2/
│       ├── require/REQ-00012/RESULT.md
│       └── design/REQ-00012/RESULT.md  # 本次新建
└── plugins/
    └── code-skills/                    # 插件本体
        ├── .claude-plugin/
        ├── CLAUDE.md                   # 9,418 bytes(本次 git mv 源)
        ├── README.md                   # 38,247 bytes(保留)
        ├── README.en.md                # 41,949 bytes(保留)
        └── skills/                     # 11 个 SKILL.md(本次不修改)
```

### 已有模块(代码视角)
- **本需求零代码模块**,所有变更均为 Markdown 文档

### 已有接口
- **本需求零 API 变更**

### 已有数据模型
- **本需求零数据模型变更**

### 已有第三方依赖
- **本需求零依赖变更**(NFR-1)

### 编码与构建约定
- commit 消息遵循 `commit-conventions.md`(虽为占位,但 NFR-7 锁定 1 行 message 习惯)
