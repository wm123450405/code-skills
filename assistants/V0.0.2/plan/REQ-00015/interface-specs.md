# 接口详细规格 — REQ-00015
更新时间:2026-06-06 09:10
版本:V0.0.2

## 接口 1:`code-merge` 技能调用

### 形式
Claude Code Skill 工具调用(用户在前端输入 `/code-merge` 触发)

### 路径/签名
```
/code-merge           # 无参,默认合并 origin/main
/code-merge <branch>  # 1 个参,合并指定分支(自动补全 origin/ 前缀)
```

### 入参
- **位置参**:`<branch>`(可选,string)
  - 不传 → 默认 `origin/main`
  - 传 1 个 → 取该分支(自动补全 `origin/` 前缀)
  - 传 2+ → 报错 + 打印用法(退出码非 0)
- **环境变量**:
  - `CODE_MERGE_SCOPE`(string,默认 `worktree-merge`):commit message 的 scope 段
  - `CODE_MERGE_TARGET`(string,默认 `main`):合并目标主分支名

### 出参
- **stdout**:3 段式报告(启动 / 逐步 / 完成)
- **退出码**:
  - `0` = 全部成功(含非阻塞警告)
  - `非 0` = 致命错误(git 命令失败 / 不在 worktree / 参数错)
  - `130` = SIGINT(Ctrl+C)
- **stderr**:失败时透传 git stderr(用户可读懂)

### 错误码
| 退出码 | 含义 | 触发场景 |
| --- | --- | --- |
| 0 | 成功 | FR-1~FR-8 全部走通(含非阻塞警告) |
| 1 | 通用错误 | (预留) |
| 2 | git pull 失败 | 步骤 0a 失败(沿用 REQ-00005) |
| 5 | 参数错 | 2+ 个非空参(E-M8) |
| 130 | SIGINT | Ctrl+C(E-M11) |
| 其他非 0 | 致命错误 | E-M1/M2/M3/M4/M5/M10/M12 |

### 示例
**正常(S-1 默认场景)**:
```
$ /code-merge
=== code-merge 启动 ===
worktree 路径: /d/workspaces/wm/code-skills-worktree-REQ-00015
源分支: worktree-REQ-00015
默认目标分支: origin/main
[FR-1] 前置检查 ... ✓ 在 worktree 中(dirty 3 文件)
[FR-2] 提交 worktree 内文件 ...
  git add -A → ✓
  git commit -m "chore(worktree-merge): ..." → ✓ hash: abc1234
[FR-3] 拉取并合并主干 ...
  git fetch origin → ✓
  git merge origin/main --no-ff → ✓
[FR-4] 冲突解决(LLM 智能合并)... ✓ 无冲突
[FR-5] 再次确认提交状态 ... ✓ 干净
[FR-6] 看板自检(5 区段)...
  · 需求清单: ✓ 13 行 (一致)
  · 概要设计清单: ✓ 10 行
  · 详细设计与任务计划汇总: ✓ 9 行
  · 任务清单: ✓ 22 行
  · 缺陷清单: ✓ 0 行
  → ✓ 看板自检通过
[FR-7] 合并 worktree 到 main ...
  git checkout main → ✓
  git merge worktree-REQ-00015 --no-ff -m "Merge branch 'worktree-REQ-00015' into main" → ✓ hash: def5678
[FR-8] 退出与清理 ...
  ✓ code-merge 完成
    · worktree: /d/workspaces/wm/code-skills-worktree-REQ-00015
    · 源分支: worktree-REQ-00015
    · 目标分支: main
    · merge commit: def5678
    · 看板自检: ✓ 通过
    · 退出码: 0
```

**冲突场景(S-4)**:
```
[FR-3] 拉取并合并主干 ...
  git merge origin/main --no-ff → ✗ CONFLICT in assistants/V0.0.2/RESULT.md
[FR-4] 冲突解决(LLM 智能合并)...
  · assistants/V0.0.2/RESULT.md: 看板数据 → ✓ 保留双方 + 统计一致
  · plugins/code-skills/skills/code-merge/SKILL.md: 代码 → ✓ 智能合并
  · 退出码: 0(含 1 个 unmerged 文件,留用户手动)
```

**非 worktree(E-M1)**:
```
=== code-merge 启动 ===
worktree 路径: <CWD>
✗ 不在 worktree 中,请先执行:
  git worktree add <path> -b <branch>
  退出码: 非 0
```

### 版本策略
- v1(本需求):worktree 强约束 + 默认 `origin/main` + `--no-ff` + 不自动 push
- v2(follow-up):`--ff-only` / `--target <branch>` / 自动 push / 自动清理 worktree

### 兼容策略
- 既有 11 个 `code-*` 技能**0 修改**(INV-1)
- `marketplace.json` 仅追加,**不**触碰既有字段(INV-2)
- `plugin.json` **0 修改**(INV-3)
- `./assistants/rules/` 13 份规范**0 修改**(INV-4 严守)

### 依据规范
- `skill-conventions.md §规则 1`
- `marketplace-protocol.md §规则 1`
- `commit-conventions.md`(占位,沿用 V0.0.2)
- `naming-conventions.md`

## 接口 2:`marketplace.json` 追加项

### 形式
JSON 协议清单(Claude Code 启动时加载)

### 路径
`.claude-plugin/marketplace.json` § `plugins[0].skills[]` 数组末尾

### 变更
```diff
   "skills": [
     "./skills/code-require",
     "./skills/code-design",
     "./skills/code-plan",
     "./skills/code-it",
     "./skills/code-unit",
     "./skills/code-review",
     "./skills/code-fix",
     "./skills/code-version",
     "./skills/code-init",
     "./skills/code-rule",
-    "./skills/code-auto"
+    "./skills/code-auto",
+    "./skills/code-merge"
   ]
```

### 不变更字段
- `$schema`(保持 `https://anthropic.com/claude-code/marketplace.schema.json`)
- `name`(保持 `code-skills-marketplace`)
- `version`(保持 `0.0.2`)
- `description`
- `owner`
- `plugins[0].name` / `version` / `description` / `author` / `source` / `keywords`

### 验证
- JSON Schema 校验通过
- `plugins[0].version = "0.0.2"` 与 `plugin.json` 同步
- `plugins[0].source = "./plugins/code-skills"` 不变

### 依据规范
- `marketplace-protocol.md §规则 1`(NFR-6 + INV-2)

## 接口 3:`code-merge/SKILL.md` frontmatter

### 形式
YAML frontmatter(Claude Code 技能元信息)

### 内容
```yaml
---
name: code-merge
description: 在 git worktree 模式下自动合并(版本感知)。要求当前在 worktree 中(dirty 自动 commit → 拉取并合并 origin/main → LLM 智能解决冲突(看板数据保留双方 + 顺序 + 统计一致;代码/配置/文档智能合并;二进制留 unmerged)→ 5 区段看板自检 → git merge --no-ff 合回 main)。整个执行过程不产生任何过程文件 / 结果文件(SKILL.md 必产)。无参默认合并 `origin/main`;可用 `<branch>` 改主干;可用 `CODE_MERGE_SCOPE` / `CODE_MERGE_TARGET` 环境变量微调。
---
```

### 必含字段
- `name`:严格 = `code-merge`(kebab-case,与目录名一致)
- `description`:完整描述(目标 + 适用场景 + 主要步骤 + 关键约束)

### 不变更字段
- 无(本技能首次创建)

### 依据规范
- `skill-conventions.md §规则 1`(必须)
