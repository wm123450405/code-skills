# 模块拆分 — REQ-00026

更新时间:2026-06-08 12:30
版本:V0.0.3

## 1. 新增模块清单
无(本需求不新增任何模块)

## 2. 修改模块清单
| 模块 / 路径 | 状态 | 职责 | 对外契约 | 关键决策 | 符合规范 |
| --- | --- | --- | --- | --- | --- |
| `plugins/code-skills/skills/code-require/SKILL.md` | 修改(描述性段落) | 需求分析技能契约 | frontmatter / 描述段落 | `plugins/code-skills/...` → `<本仓库>/...`(仅描述段) | `skill-conventions.md §规则 1` 满足(name 不变) |
| `plugins/code-skills/skills/code-design/SKILL.md` | 修改(描述性段落) | 概要设计技能契约 | 同上 | 同上 | 同上 |
| `plugins/code-skills/skills/code-plan/SKILL.md` | 修改(描述性段落) | 详细设计技能契约 | 同上 | 同上 | 同上 |
| `plugins/code-skills/skills/code-it/SKILL.md` | 修改(描述性段落) | 开发编码技能契约 | 同上 | 同上 | 同上 |
| `plugins/code-skills/skills/code-unit/SKILL.md` | 修改(描述性段落) | 单元测试技能契约 | 同上 | 同上 | 同上 |
| `plugins/code-skills/skills/code-check/SKILL.md` | 修改(描述性段落) | 代码评审技能契约 | 同上 | 同上 | 同上 |
| `plugins/code-skills/skills/code-fix/SKILL.md` | 修改(描述性段落) | 缺陷登记技能契约 | 同上 | 同上 | 同上 |
| `plugins/code-skills/skills/code-publish/SKILL.md` | 修改(描述性段落) | 发布部署技能契约 | 同上 | 同上 | 同上 |
| `plugins/code-skills/skills/code-rule/SKILL.md` | 修改(描述性段落 + L336/363/370) | 编码规范管理技能契约 | 同上 | 同上 + CLAUDE.md 字面替换 | 同上 |
| `plugins/code-skills/skills/code-init/SKILL.md` | 修改(描述性段落) | 工程初始化技能契约 | 同上 | 同上 | 同上 |
| `plugins/code-skills/skills/code-publish/templates/DEPLOY.md` | 修改(头部 L3) | 发布手册模板 | 模板文件 | 字面替换 | `doc-conventions.md §规则 1` 满足(本仓库根 CLAUDE.md 不动) |
| `plugins/code-skills/skills/code-publish/templates/UPDATE.md` | 修改(头部 L3) | 升级手册模板 | 模板文件 | 字面替换 | 同上 |
| `plugins/code-skills/skills/code-publish/templates/qanda-README.md` | 修改(L133) | Q&A README 模板 | 模板文件 | 字面替换 | 同上 |
| `plugins/code-skills/skills/code-init/templates/INIT-REPORT.md` | 修改(L3/L8) | 初始化报告模板 | 模板文件 | "本项目" → "本仓库" | 同上 |

## 3. 复用模块清单
全部 10 个 SKILL.md 的 frontmatter(FR-N / §... 引用结构)复用既有,0 新增。

## 4. 自检

### 4.1 `module-conventions.md` 命名 / 目录位置 / 依赖方向
- 全部修改都在原文件原位置进行,**不**移动文件、**不**改目录结构
- 无新增依赖

### 4.2 `skill-conventions.md §规则 1`
- 10 个 SKILL.md 的 frontmatter `name` 与目录名**完全一致**(沿用既有),0 改 frontmatter

### 4.3 `doc-conventions.md §规则 1`
- 本需求**不**改 README,**不**触发多语言对仗规则

## 5. 关键决策总结
- **改 13 个文件**:10 SKILL.md + 3 templates + 1 INIT-REPORT
- **0 新增模块**:不改文件结构
- **0 改 frontmatter**:遵循 `skill-conventions.md §规则 1`
- **0 改 README**:遵循 `doc-conventions.md §规则 1`(本仓库自定)
