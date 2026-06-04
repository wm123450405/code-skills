# 偏离记录 — REQ-00001-005
版本:V0.0.1

## 偏离 1:0 文件变更(任务"已无修可改")
- **类别**:**任务范围收缩**(审查改修的合理分叉)
- **依据**:
  - 审查要求:`./assistants/V0.0.1/review/REQ-00001-005/RESULT.md` §3 F-1
    > 若用户实际将 GitHub 仓库从 `code-skills` 重命名为 `code-skills-marketplace`:URL 必须同步
    > 若用户未重命名 GitHub 仓库(仅 marketplace name 改了):URL 保持原样
  - 规范要求:`./assistants/rules/doc-conventions.md §规则 2` README 与代码现状同步
- **实际做法**:
  - 通过 `WebFetch https://github.com/wm123450405/code-skills` 确认 GitHub 仓库名仍为 `code-skills`
  - 通过 `git remote -v` 确认本地 origin URL 仍为 `git@github.com:wm123450405/code-skills.git`
  - 结论:GitHub 仓库**未**重命名,审查要求的"分叉"指向"保持原样"
  - 因此:**不动任何文件**,L11 URL `https://github.com/wm123450405/code-skills.git` 保持原样
- **偏离理由**:
  - review/RESULT.md §3 F-1 已显式给出分叉授权,本任务严格遵循
  - 盲目改为 `code-skills-marketplace.git` 会让 URL 指向**不存在的仓库**,违反 `doc-conventions.md §规则 2`(README 与代码现状同步)
  - 用户二次确认(AskUserQuestion):"保持原样 `code-skills`(推荐)"
- **影响**:
  - 代码无变更 → 无 diff,无 commit(提交哈希为"不提交")
  - 需求 REQ-00001 的"目标 3:同步更新中英文 README 中所有相关引用"已完全满足
  - L11 的 GitHub URL 在 marketplace 根名变更后**仍正确**(marketplace name 与仓库名解耦;前者只在 `claude plugin install @<name>` 用,后者只在 `marketplace add <url>` 用)
- **授权**:
  - 用户在 review/RESULT.md §3 F-1 预先授权(显式分叉)
  - 用户在 `code-it` 实施阶段二次确认(AskUserQuestion 2026-06-04 11:54)
- **时间**:2026-06-04 11:54
