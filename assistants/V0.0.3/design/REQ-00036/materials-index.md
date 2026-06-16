# 材料登记 — REQ-00036

更新时间:2026-06-16 17:33
版本:V0.0.3

## 项目级规范
| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `./assistants/rules/skill-conventions.md` §规则 1 | SKILL.md 编写 | YAML frontmatter 必含 `name` + `description`;`name` 与目录名一致 |
| `./assistants/rules/module-conventions.md` §规则 1 | 模块规划 | 资源放 `templates/` / `checklists/` / `guidelines/` 子目录(本仓库旧规,已被 `directory-conventions` 替代) |
| `./assistants/rules/directory-conventions.md` §规则 1 | 目录与模块 | (待添加,占位规则) |
| `./assistants/rules/dashboard-conventions.md` §规则 1 | 看板/工作空间 | 字段扩展三方同步(本设计 0 触发) |
| `./assistants/rules/doc-conventions.md` §规则 1, §规则 2 | 文档编写 | README 多语言对仗 + 主语言完整性(SKILL.md 不属 README) |
| `./assistants/rules/encoding-conventions.md` §规则 1, §规则 1.5, §规则 2, §规则 3, §规则 4 | 编码格式 | REQ/BUG/TASK 命名;5 位纯数字;接收端宽松正则 |
| `./assistants/rules/naming-conventions.md` §规则 1 | 命名 | (待添加,占位规则) |
| `./assistants/rules/coding-style.md` §规则 1 | 代码风格 | (待添加,占位规则) |
| `./assistants/rules/framework-conventions.md` §规则 1 | 框架 | (待添加,占位规则) |
| `./assistants/rules/dependency-conventions.md` §规则 1 | 依赖 | (待添加,占位规则) |
| `./assistants/rules/commit-conventions.md` §规则 1 | 提交 | (待添加,占位规则) |
| `./assistants/rules/marketplace-protocol.md` §规则 1 | marketplace | (待添加,占位规则) |
| `./assistants/rules/migration-mapping.md` §规则 1 | 编码迁移 | 新旧编码追溯(本设计 0 改) |

## 上游需求
- 来源:./assistants/V0.0.3/require/REQ-00036/RESULT.md
- 版本:v1(2026-06-16 17:33)
- 提取的 FR / NFR / AC 数量:8 FR / 10 NFR / 8 AC

## 项目现状(本次扫描)

### 项目类型
- **类型**:Claude Code 插件市场仓库(`code-skills` 插件本体)
- **技术栈**:Markdown(纯文档);Git 作为版本控制;`/plugin` + `/reload-plugins` 作为 Claude Code 接入方式

### 目录结构(本设计相关)
```
plugins/code-skills/
├── .claude-plugin/
│   └── plugin.json
├── README.md
├── README.en.md
└── skills/                           ← 本设计清理范围
    ├── code-answer/SKILL.md
    ├── code-auto/SKILL.md + templates/
    ├── code-check/SKILL.md + templates/ + checklists/
    ├── code-dashboard/SKILL.md
    ├── code-design/SKILL.md + templates/
    ├── code-fix/SKILL.md + templates/
    ├── code-init/SKILL.md + templates/
    ├── code-it/SKILL.md + templates/ + guidelines/
    ├── code-merge/SKILL.md
    ├── code-plan/SKILL.md + templates/
    ├── code-publish/SKILL.md + templates/
    ├── code-require/SKILL.md + templates/
    ├── code-rule/SKILL.md + templates/
    └── code-version/SKILL.md + templates/
```

### 已有模块
(本设计 0 新增 / 0 修改代码模块;只修改文档)

### 已有接口
(无)

### 已有数据模型
(无)

### 已有第三方依赖
(无 — 纯 Markdown 仓库)

### 编码与构建约定
- 单文件最大行数:历史经验 ~ 1100 行(`code-plan` 接近阈值)
- frontmatter:必须 `name` + `description`(沿用 `skill-conventions §规则 1`)
- 章节编号:`##` / `###` / `####` 三级;步骤编号 `### 步骤 N`(N 为整数)
- 表格:标准 Markdown 表格,`|` 分隔

## 命令行参数
(无)
