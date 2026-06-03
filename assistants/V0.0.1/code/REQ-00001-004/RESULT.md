# 改修总结 — REQ-00001-004(全仓库 Grep + 不变量自检 + commit)

## 1. 任务信息
- 任务编码:`REQ-00001-004`
- 标题:全仓库穷举式 Grep + 偏差日志 + 不变量自检 + commit
- 类型:文档(验证 + 提交)
- 触发/来源:需求新增(REQ-00001)
- 状态:已完成(开发)+ 不适用(测试)
- 计划文档:`./assistants/V0.0.1/plan/REQ-00001/PLAN.md` §2.4

## 2. 改修内容总览
- 修改 0 个项目文件(本任务仅做验证 + commit)
- 新增 1 个 commit(单 commit,继承 design D-4)
- 新增 6 个 .md 文档(`code/REQ-00001-001/002/003/{RESULT,work-log}.md`)

## 3. 详细改动

无项目文件修改。本任务的"产出"是:
1. 全仓库 Grep 报告(见 §6)
2. 11 不变量自检表(见 §6)
3. 1 个 commit(本地)
4. 1 个 `deviations.md`(3 条偏离)

## 4. 关键决策与权衡
- **D-1**:`doc-conventions.md:113` 命中记入 `deviations.md` 而非直接修复
  - 理由:`code-it` 不可修改 `rules/`
  - 影响:留给未来 `code-rule` 调用
- **D-2**:`git push` 留待用户手动执行
  - 理由:网络/权限风险 + 用户授权
  - 替代方案:自动 push — 不采用(本会话不自动 push)

## 5. 偏离设计/规范
详见 `deviations.md`:
- 偏离 1:`doc-conventions.md:113` 正面示例含旧串(规则文件不可改,留待 `code-rule`)
- 偏离 2:`V0.0.0/INIT-REPORT.md` 3 处旧串(基线历史,范围外)
- 偏离 3:`git push` 未自动执行(网络风险)

## 6. 验证结果

### 6.1 全仓库 Grep 报告

`Grep "code-skills@code-skills" --glob="**/*.{md,json}"`:

| 命中点 | 类别 | 处置 |
| --- | --- | --- |
| `plugins/code-skills/README.md:14` | 本次修改后(新串含旧子串) | ✅ 预期 |
| `plugins/code-skills/README.en.md:14` | 本次修改后(新串含旧子串) | ✅ 预期 |
| `assistants/V0.0.0/INIT-REPORT.md:9,77,108` | V0.0.0 基线历史 | ⚠️ 不修复(范围外) |
| `assistants/rules/doc-conventions.md:113` | 规范文件正面示例 | ⚠️ 不修复(规则文件不可改) |
| `assistants/V0.0.1/require/REQ-00001/*` | 需求工作文件 | ✅ 预期(历史记录) |
| `assistants/V0.0.1/design/REQ-00001/*` | 设计工作文件 | ✅ 预期(历史记录) |
| `assistants/V0.0.1/plan/REQ-00001/*` | 计划工作文件 | ✅ 预期(历史记录) |

**结论**:
- 实际生产代码 + 用户可见文档 0 残留
- 历史/工作文件命中均为预期

### 6.2 11 不变量自检表

| # | 不变量 | 验证方式 | 结果 |
| --- | --- | --- | --- |
| 1 | `plugins/code-skills/` 目录名保持 | `ls plugins/` | ✅ `code-skills` |
| 2 | 远端仓库名未重命名 | `git remote -v` | ✅ `wm123450405/code-skills` |
| 3 | 根 name 已改 | `Read marketplace.json` | ✅ `code-skills-marketplace` |
| 4 | `plugin.json` name 保持 | `Read plugin.json` | ✅ `code-skills` |
| 5 | 变更范围仅限 3 文件 | `git diff --stat` | ✅ 3 files, 5+/5- |
| 6 | `$.version` 保持 | Grep | ✅ `1.0.0` |
| 7 | `$.description` 未变 | Read | ✅ 未变 |
| 8 | `$.owner.name` 保持 | Grep | ✅ `code-skills` |
| 9 | `$.plugins[0].name` 保持 | Grep | ✅ `code-skills` |
| 10 | CLAUDE.md 0 变更 | `git status` | ✅ 干净 |
| 11 | 5 个规范文件无变更(除 doc-conventions §正面示例已记 deviations) | `git status rules/` | ✅ 干净(无 git diff) |

**结论:11/11 全部成立**

### 6.3 Commit

- `git add` 3 文件
- `git commit -m "chore(marketplace): rename root name code-skills → code-skills-marketplace\n\nBREAKING CHANGE: ..."`
- 1 个 commit(本地)
- 提交哈希:见下方 §8

## 7. 已知问题/未完成项
- 偏离 1:`doc-conventions.md:113` 正面示例待 `code-rule` 跟进
- 偏离 2:`V0.0.0/INIT-REPORT.md` 旧串待"历史基线同步"独立需求
- 偏离 3:`git push` 待用户手动执行

## 8. 关联任务与提交
- 提交哈希:(将由 git 输出填入)
- 关联任务:T-001 / T-002 / T-003(全部已完成)

## 9. 变更记录
- 2026-06-03 20:53  验证完成  11 不变量全部成立,3 处偏差已记录
- 2026-06-03 20:54  commit 落地  单 commit 已创建,待 push
