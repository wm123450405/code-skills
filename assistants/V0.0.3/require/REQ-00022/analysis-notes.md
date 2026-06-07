# 分析笔记 — REQ-00022
更新时间:2026-06-06 17:55
版本:V0.0.3

## 用户输入(原始)
> 修改 `/code-review` 技能名称为 `/code-check`

## 关键疑点(待澄清,4 个)

1. **别名兼容**:是否保留 `/code-review` 作为别名(向后兼容)?
   - **不保留**(硬重命名):用户输入 `/code-review` 报"未知技能"错误
   - **保留别名**(软重命名):用户输入 `/code-review` 仍可工作(通过 symlink / 双 frontmatter / 文档约定)

2. **目录重命名**:是否同步重命名 `plugins/code-skills/skills/code-review/` 目录为 `code-check/`?
   - **同步重命名**(完整重命名):目录名 + 文件名 + frontmatter 一致
   - **仅改 frontmatter**(保留目录名):目录名仍是 `code-review/`,但 frontmatter `name: code-check`(**违反** `skill-conventions §规则 1`:`name` 与目录名必须一致)

3. **历史产物目录**:`assistants/<version>/review/...` 是**产出物类型**目录(不是技能名),是否同步改为 `check/`?
   - **不重命名**:`review/` 目录保留(历史快照,沿用 `migration-mapping §规则 5`)
   - **重命名**:会破坏 V0.0.2 全部历史 review 产物(12 个 REQ-XXXX 的 REVIEW-REPORT.md)

4. **marketplace / plugin JSON 同步**:是否同步改 `.claude-plugin/marketplace.json` + `plugins/code-skills/.claude-plugin/plugin.json` 中所有 `code-review` 字面量?
   - **同步改**:`skills[]` 路径 + `keywords[]` 关键词 + `description` 字符串
   - **不改**:违反 `marketplace-protocol §规则 1`(`skills[]` 路径必须指向实际存在的目录)

## 候选方案权衡(已锁定)

### 方案 A:仅改 SKILL.md frontmatter(不推荐)
- 优点:变更面最小(1 个文件)
- 缺点:违反 `skill-conventions §规则 1`(`name: code-check` 但目录名 `code-review/`)
- 决策:**不采纳**

### 方案 B:硬重命名(目录 + SKILL.md + JSON)
- 优点:严格遵循 `skill-conventions §规则 1` + `marketplace-protocol §规则 1`;零歧义
- 缺点:用户需主动改输入习惯(`/code-review` 报错);历史文档中"code-review"字面量需选择性更新
- 决策:**采纳**(用户原文是"修改名称",未提"保留别名";沿用 `naming-conventions` 0 容忍拼写漂移)

### 方案 C:软重命名(目录 + SKILL.md + 别名)
- 优点:向后兼容;不影响历史调用
- 缺点:需要双 frontmatter 或 symlink 机制;增加维护成本;`skill-conventions §规则 1` 不接受双 `name` 字段
- 决策:**不采纳**(本仓库无 symlink 工具链,且 `skill-conventions §规则 1` 锁定 name 单值)

## 临时假设(待用户确认)

- 用户的"修改名称" = 硬重命名(方案 B)
- 仓库根 `README.md` / `README.en.md` 中"code-review"字面量**同步改**(沿用 `doc-conventions §规则 2` 完整性约束)
- 13 份项目级规范(`./assistants/rules/*.md` + `CLAUDE.md`)中"code-review"字面量**同步改**(避免规范引用断裂)
- V0.0.2/V0.0.3 历史 `review/` 目录**不**重命名(目录名是"产出物类型",沿用 `migration-mapping §规则 5` 历史快照)
- V0.0.2/V0.0.3 历史 review 产物内"code-review"字面量**不**追溯替换(沿用 `migration-mapping §规则 5`)

## 关键交叉点(本需求 11 类引用方)

| 引用方 | 文件类型 | 处理策略 |
| --- | --- | --- |
| `code-review/SKILL.md` | 技能入口 | **重命名目录** + 改 frontmatter + 改 H1 标题 |
| `.claude-plugin/marketplace.json` | marketplace 清单 | `skills[]` 路径 + `keywords[]` + `description` 全部同步改 |
| `plugins/code-skills/.claude-plugin/plugin.json` | plugin 清单 | `keywords[]` + `description` 同步改 |
| 10 个其他 SKILL.md 的 `description` 字段 | 技能入口 | 同步改(下游引用) |
| `plugins/code-skills/README.md` / `README.en.md` | 仓库级 README | 同步改(沿用 `doc-conventions`) |
| 仓库根 `README.md` / `README.en.md` | 仓库级 README | 同步改(沿用 `doc-conventions`) |
| `CLAUDE.md` | 项目级规则 | 同步改(避免引用断裂) |
| 13 份项目级规范(`./assistants/rules/*.md`) | 规范文件 | 同步改(避免规范引用断裂) |
| `templates/version-RESULT.md` 等 6 个模板 | 技能模板 | 同步改(沿用 `module-conventions §规则 1`) |
| V0.0.2/V0.0.3 历史 `review/REQ-NNNN/*` 产物 | 评审历史产物 | **不**追溯替换(沿用 `migration-mapping §规则 5` 历史快照) |
| V0.0.2/V0.0.3 历史 `code/...` / `plan/...` 产物 | 任务历史产物 | **不**追溯替换(同上) |

## 下一轮要深挖的方向

- 确认方案 B vs C(硬重命名 vs 软重命名)— 待 AskUserQuestion
- 确认仓库根 README 是否同步改
- 确认 13 份项目级规范是否同步改
