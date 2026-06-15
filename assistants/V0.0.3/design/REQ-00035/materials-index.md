# 材料登记 — REQ-00035
更新时间:2026-06-15 19:05
版本:V0.0.3

## 项目级规范

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| encoding-conventions.md | 编码格式 | REQ-NNNNN / TASK-(REQ\|BUG)-\d{5}-\d{5} / BUG-NNNNN;接收端宽松 |
| dashboard-conventions.md | 看板解析 | `^## .*$` 定位 + `^\| .* \|$` 匹配;三同步规则 |
| skill-conventions.md | 技能 SKILL.md | 锚点(不修改 frontmatter / 不修改既有章节) |
| module-conventions.md | 模块边界 | 改既有模块不改边界;新增模块需登记 |
| doc-conventions.md | 文档 | 变更记录 / 模板规范 |
| marketplace-protocol.md | marketplace 协议 | plugins/ 子目录布局;不直接改 marketplace.json 在本需求 |
| migration-mapping.md | 旧→新映射 | 既有迁移约定,本需求不触发 |

## 上游需求

- 来源:./assistants/V0.0.3/require/REQ-00035/RESULT.md
- 版本:v1(2026-06-15)
- 提取的 FR / NFR / AC 数量:8 FR / 9 NFR / 22 AC

## 项目现状(本次扫描)

### 项目类型
- 元技能仓库(marketplace 协议):plugins/code-skills/skills/<skill>/SKILL.md
- 14 个技能(9 主流程 + 5 支线/编排)
- 5 个主流程技能需要改造:`code-require` / `code-design` / `code-plan` / `code-it` / `code-check`

### 目录结构
```
code-skills/
├── .claude-plugin/marketplace.json
├── plugins/code-skills/
│   ├── .claude-plugin/plugin.json
│   ├── README.md / README.en.md
│   ├── CLAUDE.md
│   └── skills/<14 个>/SKILL.md
├── assistants/
│   ├── .current-version
│   ├── rules/<7 个规范>.md
│   └── V0.0.3/{require,design,plan,code,review,fix}
```

### 已有模块(本设计涉及改写)

| 模块/路径 | 职责 | 改写方式 |
| --- | --- | --- |
| code-require/SKILL.md | 需求分析 | 加步骤 0a(过程文档判定) + 条件化步骤 8A/10A |
| code-design/SKILL.md | 概要设计 | 加步骤 0a.5(过程文档判定) |
| code-plan/SKILL.md | 详细设计 | 加步骤 0a.5(过程文档判定) |
| code-it/SKILL.md | 任务实施 | 加步骤 0a(任务级过程文档判定) |
| code-check/SKILL.md | 评审 | 加步骤 0a(评审级过程文档判定) + 新增 8.13 评审维度 |
| code-auto/SKILL.md | 编排 | 子技能调用表"备注"列加 1 行 |
| code-dashboard/SKILL.md | 看板 | 解析锚点小节加 1 条兼容说明 |
| 5 模板新增 | process-doc-decisions.md | 全新文件 × 5 技能 |

### 已有接口
- 不涉及(本设计不引入新外部接口)

### 已有数据模型
- 不涉及(本设计不引入新数据模型,沿用 markdown 文件 + frontmatter 范式)

### 已有第三方依赖
- 不涉及(本设计不新增依赖)

### 编码与构建约定
- 沿用 ./assistants/rules/{encoding-conventions,skill-conventions,doc-conventions}.md
