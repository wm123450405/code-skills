# 风险分析 — REQ-00012
更新时间:2026-06-05
版本:V0.0.2

## 异常处理

| 异常路径 | 处理策略 | 监控/退出码 |
| --- | --- | --- |
| `./CLAUDE.md` 已存在(E-3) | 中止 + 报错"目标已存在,无法移动" | 退出码 ≠ 0 |
| `plugins/code-skills/CLAUDE.md` 不存在(E-2) | 中止 + 报错"无 CLAUDE.md 可移动" | 退出码 ≠ 0 |
| `./README.md` 已存在(E-4) | 中止 + 报错"目标已存在,无法新建" | 退出码 ≠ 0 |
| `./README.en.md` 已存在(E-5) | 中止 + 报错"目标已存在,无法新建" | 退出码 ≠ 0 |
| `git mv` 失败(权限等,E-6) | 中止 + 报错退出 | 退出码 ≠ 0 |
| 行数超 50(NFR-2) | 中止 + 报错"超出极简约束" | 退出码 ≠ 0 |
| 中英章节不对仗(§规则 1) | 中止 + 报错"结构漂移" | 退出码 ≠ 0 |
| 中英 README 分次提交(违反 §规则 1) | 中止 + 报错"必须同次提交" | 退出码 ≠ 0 |
| 用户希望"移动 + 软链"组合(E-7) | **不**支持(NFR-8 锁) | — |

## 安全边界

**本需求无安全约束**(纯文档变更,无代码执行入口,无密钥,无 API,无数据)。

- 鉴权要求:N/A
- 输入校验:N/A
- 敏感数据处理:N/A
- 审计日志:N/A

## 性能与资源

- 关键路径预估:微秒级(纯本地文件操作)
- 资源限制:N/A
- 缓存策略:N/A

## 回退策略

| 触发条件 | 步骤 | 验证 |
| --- | --- | --- |
| T-001 失败 | `git rm ./README.md` + `git commit --amend`(若 T-002 未完成) | `ls ./README.md` 不存在 |
| T-002 失败 | `git rm ./README.en.md` + `git commit --amend` | `ls ./README.en.md` 不存在 |
| T-003 失败 | `git mv CLAUDE.md plugins/code-skills/CLAUDE.md` + `git commit --amend` | `ls plugins/code-skills/CLAUDE.md` 存在 + `ls ./CLAUDE.md` 不存在 |
| 整体回退 | `git reset --hard HEAD~3`(若未推送) | `git log --oneline` 回到 REQ-00012 前 |

## 测试要点

| 类型 | 范围 | 载体 |
| --- | --- | --- |
| 单元测试 | N/A | 仓库无测试载体,`code-unit` 守卫判定"不可测" |
| 集成测试 | N/A | N/A |
| 端到端测试 | N/A | N/A |
| 验证手段(非自动化) | 6 项 | `ls` / `wc -l` / `wc -c` / `grep` / `git log --follow` / `git status` |
