# 风险分析 — REQ-00015
更新时间:2026-06-06 09:10
版本:V0.0.2

## 异常路径

### 异常 E-M1:不在 worktree
- **描述**:`git rev-parse --git-common-dir == --git-dir`(在主工作区)
- **处理**:打印 `✗ 不在 worktree 中,请先 git worktree add <path> -b <branch>`
- **退出码**:非 0
- **监控**:无(本仓库无运行监控)

### 异常 E-M2:main 分支 dirty(FR-7)
- **描述**:FR-7 `git checkout main` 失败,因为 main dirty
- **处理**:打印 `✗ main 分支 dirty, 请先 git stash 或 git commit`,**不**自动处理
- **退出码**:非 0
- **影响**:本需求 0 派生(用户决策)

### 异常 E-M3:worktree 路径不存在
- **描述**:用户传的 `--worktree` 路径无效
- **处理**:打印 `✗ worktree 路径 <path> 不存在`
- **退出码**:非 0

### 异常 E-M4:主干分支不存在
- **描述**:`git rev-parse --verify origin/main` 失败
- **处理**:打印 `✗ 主干分支 <branch> 不存在, 请检查远端`
- **退出码**:非 0

### 异常 E-M5:pre-commit hook 失败
- **描述**:FR-2 `git commit` 退出码非 0
- **处理**:打印 stderr,**不**重试,提示用户手动
- **退出码**:非 0

### 异常 E-M6:二进制文件冲突
- **描述**:FR-4 识别为二进制(.png/.pdf/.mp4)
- **处理**:留 unmerged + 提示用户手动,**不**阻塞
- **退出码**:0(警告)
- **影响**:用户后续手动 `Edit` + `git add`

### 异常 E-M7:看板自检不一致
- **描述**:FR-6 5 区段中任一不一致
- **处理**:打印详细 `✗` 行,**不**修复,不阻塞
- **退出码**:0(警告)
- **影响**:留 `code-rule` 处理

### 异常 E-M8:参数错
- **描述**:用户传 2+ 个非空参
- **处理**:打印用法 + 退出
- **退出码**:非 0

### 异常 E-M9:主干分支冲突后无法合并(FR-4 全 unmerged)
- **描述**:所有冲突文件都无法 LLM 解决
- **处理**:打印 `✗ 仍有 N 个 unmerged`,提示用户手动
- **退出码**:0(警告)

### 异常 E-M10:git 命令不可用
- **描述**:`git --version` 失败
- **处理**:打印 `✗ 未检测到 git`
- **退出码**:非 0

### 异常 E-M11:Ctrl+C 中止
- **描述**:用户在执行中按 Ctrl+C
- **处理**:立即停止,**不**回滚已 commit(commit 是 git 原子的);打印 `⛔ code-merge 中止`
- **退出码**:130(SIGINT)
- **影响**:可能 worktree 处于中间状态(已 commit / 未 merge),用户手动处理

### 异常 E-M12:worktree 已被 prune
- **描述**:`git worktree list` 中无当前 path
- **处理**:打印 `✗ 当前 worktree 已被 prune`
- **退出码**:非 0

## 安全边界

### 鉴权要求
- **无** —— 本技能**不**涉及鉴权(纯本地 git 操作)

### 输入校验
- **位置参数量**:0 / 1 / 2+(分别走默认 / 解析 / 报错)
- **worktree 路径**:FR-1 自动识别(不需用户传)
- **主干分支存在性**:FR-3 step 1 用 `git rev-parse --verify` 校验
- **二进制文件扩展名**:白名单(`.png` / `.pdf` / `.mp4` / `.mp3` / `.zip` / `.tar.gz` / ...)

### 敏感数据处理
- **无** —— 本技能**不**处理 token / password(纯 git 操作,无 http 请求)

### 审计日志
- **由 git 自身保证**:所有 `git commit` 带 author / timestamp
- **本技能**不打印额外审计日志(stdout 报告供用户审阅即可)

## 性能与资源

### 关键路径预估
| 步骤 | 操作 | 性能预估 |
| --- | --- | --- |
| FR-1 | `git rev-parse` + `git status` | < 1 秒 |
| FR-2 | `git add` + `git commit` | < 5 秒 |
| FR-3 | `git fetch` + `git merge` | 网络依赖(秒级 ~ 分钟级) |
| FR-4 | LLM 智能合并 | 文件数 + 复杂度依赖(秒级 ~ 分钟级) |
| FR-5 | `git status` | < 1 秒 |
| FR-6 | 5 区段扫描 | < 100 ms(纯字符串 + Read) |
| FR-7 | `git checkout` + `git merge` | < 5 秒 |
| FR-8 | 报告打印 | < 1 秒 |

**总耗时预估**:
- **最快场景**(无冲突 + 干净 worktree):~10 秒
- **典型场景**(2~5 文件冲突):~30 秒 ~ 2 分钟
- **最慢场景**(大量冲突 + 复杂合并):~5 ~ 15 分钟

### 资源限制
- **0 内存压力**(纯 IO + LLM 推理)
- **0 磁盘压力**(不持久化)
- **0 CPU 压力**(单线程 + 字符串处理)

### 缓存策略
- **无** —— 每次执行都重读全部数据(避免 stale 状态)

## 回退策略

### 触发条件 + 步骤
| 触发条件 | 回退步骤 | 验证 |
| --- | --- | --- |
| FR-2 commit 失败 | 不重试,用户手动 `git commit` 或 `git reset` | 用户执行后 `git status` |
| FR-3 merge 失败 | 不自动回滚,用户手动 `git merge --abort` | 用户执行后 `git status` |
| FR-4 冲突无法 LLM 解决 | 留 unmerged,用户手动 `Edit` + `git add` | 用户执行后 `git status` |
| FR-7 main 合并失败 | 不自动回滚,用户手动 `git merge --abort` | 用户执行后 `git status` |
| Ctrl+C 中止 | **不**回滚已 commit(commit 是 git 原子的) | 用户手动 `git status` |

**关键原则**:本技能**不**主动回滚任何 git 状态(避免数据丢失)

## 测试要点

### 单元测试
- **0** —— 本仓库纯文档,无可测载体(REQ-00009 守卫判定"不可测")
- 0 单元测试覆盖

### 集成测试
- **0** —— 同上
- 0 集成测试覆盖

### 端到端测试
- **0** —— 同上
- 0 e2e 测试覆盖

### 性能/安全测试
- **0** —— 同上
- 0 perf 测试覆盖

### 静态自检
- **10 项 INV 100% 通过**(T-005 收尾执行):
  - INV-1:不修改其他 11 个 `code-*` SKILL.md
  - INV-2:marketplace.json 仅追加
  - INV-3:plugin.json 0 修改
  - INV-4:0 过程/结果文件(执行阶段)
  - INV-5:不 --squash
  - INV-6:不自动 push / 不自动清理 worktree
  - INV-7:不实现 v1 follow-up
  - INV-8:SKILL.md 不嵌入 git 命令模板
  - INV-9:不调 code-publish / code-auto
  - INV-10:worktree 强约束

### 未来验证
- 用户实际调 `/code-merge` 在 worktree 中跑一次(纯手工)
- 验证 8 FR 全部走通
- 验证 0 触发 `dashboard-conventions §规则 1` 3 处同步
- 验证 10 项 INV 全部通过
