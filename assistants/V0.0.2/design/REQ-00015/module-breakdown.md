# 模块拆分 — REQ-00015
更新时间:2026-06-06 09:00
版本:V0.0.2

## 新增模块清单

### 模块 1:`code-merge` 技能入口
- **路径**:`plugins/code-skills/skills/code-merge/SKILL.md`
- **状态**:**新增**
- **职责**:1 句话 —— 在 git worktree 模式下,自动完成"提交 → 拉取并合并主干 → 冲突解决(LLM 智能)→ 自检 → 合回主分支"的完整合并流程
- **对外接口**:
  - `Skill: code-merge`(无参) → 默认合并 `origin/main`
  - `Skill: code-merge <branch>` → 合并指定分支(自动补全 `origin/` 前缀)
- **依赖**:
  - 对内其他模块:**0**(纯 CLI 工具)
  - 对外三方:**0**(git 命令由 Claude Code 现场执行)
- **关键决策**:
  - **不**拆分多个子技能(避免破坏 NFR-1 "不产生过程文件")
  - **不**产出 RESULT.md(纯 stdout 输出)
  - **不**写 work-log.md(无过程文件)
- **符合规范条款**:
  - `skill-conventions.md §规则 1`:frontmatter 必含 `name: code-merge` + `description: <完整描述>`
  - `module-conventions.md §规则 1`:无新增子目录(SKILL.md 直接放技能根)
  - `marketplace-protocol.md §规则 1`:`marketplace.json` 追加 `./skills/code-merge`

## 修改模块清单
**0**(本需求不修改任何既有 11 个 `code-*` 技能,严守 NFR-5 / INV-1)

## 复用既有模块
| 既有技能 | 复用方式 | 复用点 |
| --- | --- | --- |
| `code-version` | 间接依赖 | FR-1 步骤 0 读 `.current-version`(沿用既有契约) |
| `code-dashboard` | 算法复用 | FR-6 看板自检复用其"算法 1 + 算法 5"(5 区段表格行计数) |
| `code-it` / `code-plan` | 模式复用 | FR-2 commit 格式 `chore(<scope>): ...`(沿用 V0.0.2 既有模式) |
| 既有 11 个 `code-*` | 风格复用 | stdout 报告格式(`=== xxx 启动 ===` / `✓` / `✗` / `⚠` 前缀) |

## 模块自检
- ✅ 命名符合规范:`code-merge` kebab-case,与其他 11 个 `code-*` 风格一致
- ✅ 目录位置符合规范:`plugins/code-skills/skills/code-merge/SKILL.md` 是既有位置
- ✅ 依赖方向:本技能**0 依赖**其他 `code-*`(避免循环,保持解耦)
- ✅ 无被禁止的模式:**不**调 `code-auto` / `code-publish` / `code-fix`(职责分离)
