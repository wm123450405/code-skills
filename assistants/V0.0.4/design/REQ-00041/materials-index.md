# 材料登记 — REQ-00041
更新时间:2026-06-29 13:50
版本:V0.0.4

## 项目级规范

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| skill-conventions.md | 技能编写 | SKILL.md 必须含 name + description;不得包含开发痕迹(6 类) |
| encoding-conventions.md | 编码格式 | REQ-5 位纯数字;BUG-5 位纯数字;TASK 嵌套式 |
| directory-conventions.md | 目录结构 | 规则 1 待添加(空占位) |
| framework-conventions.md | 框架规范 | 规则 1 待添加(空占位) |

## 上游需求

- 来源:./assistants/V0.0.4/require/REQ-00041/RESULT.md
- 版本:V0.0.4(2026-06-29)
- 提取的 FR / NFR / AC:8 FR / 5 NFR / 10 AC
- 关键设计目标:`--extensible`(完整覆盖 6 类语言 + 4 技能全重构)

## 项目现状(本次扫描)

### 项目类型
- 语言:Markdown(纯文档项目,无源代码)
- 框架:Claude Code 技能系统(marketplace 协议)
- 关键依赖:无

### 目录结构
```
plugins/code-skills/skills/
├── code-design/SKILL.md(~669 行)
├── code-plan/SKILL.md(~1187 行)
├── code-it/SKILL.md(~1551 行)
├── code-check/SKILL.md(~703 行)
└── ... (其他 6 个技能)
```

### 已有模块
| 模块/路径 | 职责 | 是否可复用 |
| --- | --- | --- |
| code-design/SKILL.md | 概要设计技能 | 需修改(精简) |
| code-plan/SKILL.md | 详细设计技能 | 需修改(精简) |
| code-it/SKILL.md | 开发编码技能 | 需修改(精简) |
| code-check/SKILL.md | 代码评审技能 | 需修改(精简) |

### 已有接口
- 无(纯文档项目,无 API)

### 已有数据模型
- 无(纯文档项目)

### 已有第三方依赖
- 无

### 编码与构建约定
- 技能文件:Markdown + YAML frontmatter
- 路径约定:skills/<技能名>/SKILL.md
- 辅助资源:同目录下 templates/ / checklists/ / guidelines/ 子目录