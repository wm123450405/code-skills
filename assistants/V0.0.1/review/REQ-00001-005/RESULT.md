# 审查改修要求 — REQ-00001-005(同步中英 README 中 GitHub URL 仓库名)

## 1. 任务信息

- **任务编码**:`REQ-00001-005`
- **标题**:同步中英 README 中 GitHub URL 仓库名(审查派生)
- **类型**:修改
- **触发/来源**:**审查改修**(由 `code-review REQ-00001` 派生)
- **触发时间**:2026-06-04 10:35
- **严重程度**:**建议改**(必须改的派生)

## 2. 触发的原任务

| 原任务 | 状态 | 关联性 |
| --- | --- | --- |
| `REQ-00001-002`(同步中英 README) | 已完成 | T-002 改了 install 命令 + 描述句,但**未**改 L11 的 `claude plugin marketplace add <github-url>` 中 GitHub 仓库 URL |

## 3. 问题清单

### F-1:GitHub 仓库 URL 未与 marketplace name 同步
- **位置**:
  - `plugins/code-skills/README.md:11` — `claude plugin marketplace add https://github.com/wm123450405/code-skills.git`
  - `plugins/code-skills/README.en.md:11` — `claude plugin marketplace add https://github.com/wm123450405/code-skills.git`
- **类别**:一致性 / 规范
- **描述**:`marketplace.json` 根 `name` 字段已从 `code-skills` 改为 `code-skills-marketplace`(由 REQ-00001-001 完成),但 README 中的 `claude plugin marketplace add <github-url>` 仍指向 `code-skills.git` 仓库名。
  - **若用户实际将 GitHub 仓库从 `code-skills` 重命名为 `code-skills-marketplace`**:URL 必须同步
  - **若用户未重命名 GitHub 仓库(仅 marketplace name 改了)**:URL 保持原样
- **建议改修**:
  - 询问用户 GitHub 仓库是否已重命名
  - 若是 → URL 改为 `https://github.com/wm123450405/code-skills-marketplace.git`
  - 若否 → 在 `deviations.md` 记录"GitHub 仓库未重命名,URL 保持原样"作为合理偏离

## 4. 应当改修的文件

| 文件 | 现状 | 应改为 | 理由 |
| --- | --- | --- | --- |
| `plugins/code-skills/README.md:11` | `https://github.com/wm123450405/code-skills.git` | 询问用户后确定(`code-skills-marketplace.git` 或保持原样) | marketplace name 与仓库名应一致(若仓库已重命名) |
| `plugins/code-skills/README.en.md:11` | 同上 | 同上 | 中英对仗(`doc-conventions.md §规则 1`) |

## 5. 验证手段

- 询问用户后,根据回答决定具体改法
- 若修改:`git diff --stat` 中英两侧行数一致(中英对仗)
- `Grep "code-skills.git" plugins/code-skills/README.md` 应有 0 或 1 命中(取决于用户决定)

## 6. 关联依据

- 规范:`doc-conventions.md §规则 1`(中英对仗)+ `doc-conventions.md §规则 2`(README 与代码现状一致)
- 需求:REQ-00001 目标 3 "同步更新中英文 README 中所有相关引用,保证仓库与文档自洽"
- 设计:REQ-00001 design D-3 "install 命令与 marketplace name 同步"
- 详细设计:plan/REQ-00001/PLAN.md §2.2 表格"install 命令已改"

## 7. 不需要做的

- **不**修改 marketplace.json(由 T-001 完成,无变更)
- **不**修改 install 命令 `claude plugin install code-skills@code-skills-marketplace`(由 T-002 完成,无变更)
- **不**修改 CLAUDE.md(0 命中核查由 T-003 完成,本任务不涉及)
- **不**重命名本地目录(本地目录名 `code-skills` 保留,符合"不修改目录结构"约束)
- **不**自动假设 GitHub 仓库已重命名(必须询问用户)
