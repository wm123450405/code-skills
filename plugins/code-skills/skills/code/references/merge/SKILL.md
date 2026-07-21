---
name: code-merge
description: `/code merge` git worktree 自动合回主干。模型在用户在 worktree 内完成开发、要一键合回 main 时调用。**仅限 git worktree** 运行(主工作区调立即报错);FR-1 前置检查 → FR-2 提交未提交文件 → FR-3 fetch + merge → FR-4 LLM 智能解冲突(看板/代码/配置/二进制分类)→ FR-5 二次确认 → FR-6 看板 2 区段自检 → FR-7 `git merge --no-ff` 合回 main。不自动 push / 不自动 remove worktree / 不写任何过程文件。
---

# `/code merge` — Worktree 自动合并

## 目标

在 git worktree 模式下,worktree 内开发 → 主分支合回全自动化:提交 → fetch + merge → LLM 智能解冲突 → 看板自检 → `--no-ff` 合回 main。

## 核心约束

- **仅**在 worktree 模式运行(主工作区直接 E-M1 报错,无 `--no-worktree` 开关)
- **不**写任何过程文件 / 结果文件(NFR-1)
- **不**自动 push / **不**自动 `git worktree remove`
- **不**回滚已 commit
- **不**调任何其他 `/code *` 子技能(INV-9)
- **不**修改既有 SKILL.md / marketplace.json / plugin.json

## 输入

| 参数 | 必填 | 缺省 |
| --- | --- | --- |
| `<branch>` | 否 | `origin/main`(`origin/` 前缀自动补全) |
| `CODE_MERGE_SCOPE` | 否 | `worktree-merge`(commit message `<scope>`) |
| `CODE_MERGE_TARGET` | 否 | `main`(合并目标) |

**`/code merge develop`** = 合并 `origin/develop`。

≥2 个非空参 → E-M8 报错退出。

## 8 个 FR

```
FR-1  worktree 模式识别 + 前置检查    (git-common-dir == git-dir → E-M1)
FR-2  提交 worktree 内未提交文件       (chore(<scope>): merge worktree into <target>)
FR-3  拉取并合并主干分支               (git fetch origin → git merge <target> --no-ff)
FR-4  冲突解决(LLM 智能合并)            # 分类: 看板/代码/配置/文档/二进制
FR-5  再次确认所有文件已提交            (post-merge cleanup)
FR-6  看板自检(需求清单 + 缺陷清单, 非阻塞警告)
FR-7  合并 worktree 到主分支            (git checkout <target> → git merge <worktree-branch> --no-ff)
FR-8  退出与清理                        (0 操作, 屏幕输出最终报告)
```

**FR-4 冲突分类处理**:

| 类型 | 处理 |
| --- | --- |
| 看板数据(RESULT.md / req/ / fix/ 关键文件) | 保留双方数据 + 按时间戳升序 + 重算统计行 |
| 代码(.py / .ts / .go 等) | LLM 读双侧智能合并,优先保留双侧独有逻辑 |
| 配置(.json / .yaml / .toml) | 双侧字段并集去重 |
| 文档(.md) | 同看板数据规则 |
| 二进制(.png / .pdf / .mp4 等) | **不**自动合并,留 unmerged + 提示(E-M6 非阻塞) |

## 退出码

| 码 | 含义 |
| --- | --- |
| 0 | 全部 FR 走通(含非阻塞警告) |
| 非 0 | 致命错误 E-M1/M2/M3/M4/M5/M8/M10/M12 |
| 130 | Ctrl+C(E-M11) |

## 工作目录

```
./assistants/
├── rules/                跨版本共享,只读
├── .current-version      只读(必读,不写)
└── <版本号>/
    └── RESULT.md         只读 + FR-6 扫描
```

**不修改** `./assistants/rules/` 下任何文件 / `<版本号>/RESULT.md` / 既有 SKILL.md / `req/` / `fix/`。

## 工具

- `Bash`: 执行 git 命令
- `Read`: 读 `.current-version` / `RESULT.md` / 冲突文件双方
- `Grep`: 解析 RESULT.md 区段
- `Glob`: 扫描看板数据冲突文件 / 读编码规范
- `Write` / `Edit` / `Skill`: **0 使用**

## 不要做的事

- 在主工作区(非 worktree)运行
- 自动 `git push` / 自动 `git worktree remove`
- 用 `--squash` 合并(必须 `--no-ff`)
- 接受 `--no-worktree` 开关
- 在异常/中止时 flush 任何文件
- 实现 v1 follow-up 项(`--ff-only` / `--target` / 自动 push / 自动 remove / 跨多 worktree / 自检自动修复)
- 调任何其他子技能