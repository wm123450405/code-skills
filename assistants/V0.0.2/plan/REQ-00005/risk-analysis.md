# 风险分析 — REQ-00005

更新时间:2026-06-04 16:30
版本:V0.0.2

> 本文档是"概要设计 §12 风险与缓解" + 需求文档 §9 边界与异常(E-1 ~ E-13)的**详细化**,为每条异常/风险给出:触发条件 → 检测手段 → 处理策略 → 监控指标 → 对应任务。

---

## 1. 异常处理(13 个边界场景)

### 1.1 E-1:FR-2 检测到版本不一致
- **触发条件**:`pulledVersion ≠ intendedVersion`(步骤 0b)
- **检测手段**:`Read .current-version` 两次对比(拉取前 / 拉取后)
- **处理策略**:NFR-3 硬中断 + 弹窗 3 选 1(FR-2.AC-2.3)
  - 选 A → 调 `code-version` 切换 + 提示重跑
  - 选 B → 在本地版本继续
  - 选 C → 取消退出
- **监控指标**:`code-require` 调用频次 × 版本不一致触发率
- **对应任务**:`TASK-REQ-00005-00001`(步骤 0b 部分)
- **回退方式**:用户重选选项 / 重跑 `code-require`
- **代码引用**:`interface-specs.md §步骤 0b` 完整伪代码

### 1.2 E-2:`git pull` 冲突
- **触发条件**:`git pull` 退出码非 0 + stderr 含 "CONFLICT" / "Merge conflict" / "unmerged"
- **检测手段**:`Bash: git pull` + 解析退出码 + 关键词匹配
- **处理策略**:中断 + 列出冲突文件 + 提示"请手动解决冲突后重跑"(Q-2 锁定 A)
- **监控指标**:`git pull` 冲突触发次数
- **对应任务**:`TASK-REQ-00005-00001 / 002 / 003`(步骤 0a 部分)
- **回退方式**:`git status` 查看冲突 → 手动解 → `git add <file>` → `git commit` → 重跑
- **代码引用**:`interface-specs.md §步骤 0a` 完整伪代码

### 1.3 E-3:`git pull` 网络失败
- **触发条件**:`git pull` 退出码非 0 + stderr 含 "Could not resolve host" / "Connection" / "timeout"
- **检测手段**:同上
- **处理策略**:中断 + 提示网络问题 + 列出 remote URL
- **对应任务**:同 E-2
- **回退方式**:检查网络/代理 → 重跑
- **代码引用**:同 E-2

### 1.4 E-4:`git pull` 权限失败
- **触发条件**:`git pull` 退出码非 0 + stderr 含 "Permission denied" / "Authentication failed" / "403"
- **检测手段**:同上
- **处理策略**:中断 + 提示凭据问题
- **对应任务**:同 E-2
- **回退方式**:检查 SSH key / token → 重跑
- **代码引用**:同 E-2

### 1.5 E-5:`git pull` no-op(已是最新)
- **触发条件**:`git pull` 输出 "Already up to date."
- **检测手段**:`Bash: git pull` 退出码 0
- **处理策略**:**静默成功**(不打印额外信息),继续步骤 0b/0
- **对应任务**:同 E-2
- **回退方式**:N/A
- **代码引用**:同 E-2

### 1.6 E-6:FR-2 选 A(切版本)
- **触发条件**:用户选 A
- **检测手段**:`AskUserQuestion` 返回值
- **处理策略**:调独立技能 `code-version <pulledVersion>`(FR-5.AC-5.2)+ 提示"已切到 <version>,请重跑 `code-require`"+ **退出** `code-require`
- **对应任务**:`TASK-REQ-00005-00001`(步骤 0b 部分)
- **回退方式**:用户重跑 `code-require` / 手动切回版本
- **代码引用**:`interface-specs.md §步骤 0b`

### 1.7 E-7:FR-2 选 C(取消)
- **触发条件**:用户选 C
- **处理策略**:退出 `code-require`,无任何文件变更
- **对应任务**:同 E-6
- **回退方式**:N/A
- **代码引用**:同 E-6

### 1.8 E-8:FR-3 末尾无文件变更
- **触发条件**:`git status --porcelain` 输出为空
- **检测手段**:`Bash: git status --porcelain`
- **处理策略**:跳过 commit,打印"无文件变更,跳过末尾提交",退出(NFR-4 幂等)
- **对应任务**:`TASK-REQ-00005-00001 / 002 / 003`(步骤 N 部分)
- **回退方式**:N/A
- **代码引用**:`interface-specs.md §步骤 N`

### 1.9 E-9:FR-3 用户选 C(取消提交)
- **触发条件**:用户选 C
- **处理策略**:跳过 commit,打印"已取消提交,文件保持暂存/工作区状态",退出
- **对应任务**:同 E-8
- **回退方式**:用户手动 `git commit` / `git reset`
- **代码引用**:同 E-8

### 1.10 E-10:FR-3 `git commit` 失败
- **触发条件**:`git commit` 退出码非 0(pre-commit hook / 其他)
- **检测手段**:`Bash: git commit` 退出码
- **处理策略**:**不重试**,打印 stderr + 提示手动处理(FR-3.AC-3.6)
- **对应任务**:同 E-8
- **回退方式**:用户查看 pre-commit hook / 手动 `git commit`
- **代码引用**:同 E-8

### 1.11 E-11:FR-2 询问时用户不回答
- **触发条件**:无超时(Claude Code `AskUserQuestion` 总会等到回答)
- **检测手段**:N/A(协议层保证)
- **处理策略**:N/A
- **对应任务**:N/A
- **回退方式**:N/A
- **代码引用**:N/A

### 1.12 E-12:末尾兜底时,git 不存在
- **触发条件**:`git --version` 退出码非 0
- **检测手段**:`Bash: git --version` 退出码
- **处理策略**:中断 + 提示"未检测到 git,本需求需要 git,请先安装 git 后重试"
- **对应任务**:同 E-2
- **回退方式**:安装 git → 重跑
- **代码引用**:同 E-2

### 1.13 E-13:`code-design` / `code-plan` 末尾兜底时,本版本未拉取
- **触发条件**:本仓库环境防御(0a 已拉 → 不应发生)
- **检测手段**:步骤 0a 完成后,`Read .current-version` 应被读取并传递
- **处理策略**:防御性 — 若 `.current-version` 与"步骤 0 读取"不一致,重新走 0b 流程(但 `code-design` / `code-plan` 无 0b,故**仅**打印警告,继续后续流程)
- **对应任务**:同 E-2
- **回退方式**:N/A
- **代码引用**:N/A

---

## 2. 安全边界

### 2.1 鉴权要求
- **本仓库无应用代码**:N/A
- **`git pull` / `git commit`**:依赖系统级 git 凭据(SSH key / token)

### 2.2 输入校验
- **用户输入的"需求编码"**:由"步骤 1 收集需求编码"处理,本需求不新增校验
- **用户输入的"目标版本"**:`code-version` 技能负责校验,本需求不感知

### 2.3 敏感数据处理
- **N/A**:本需求不处理任何敏感数据(无 API、无数据库)

### 2.4 防注入
- **N/A**:本需求无 SQL / NoSQL / 命令注入面(`git commit -m` 用 `shlex.quote` 转义)

### 2.5 审计日志
- **末尾 commit 本身是审计痕迹**:commit message 含统计(N FR / M NFR / K AC)
- **看板"执行的开发命令记录"区段**:本需求不写该区(由 `code-it` 等技能在 `Bash` 调用时填入)

---

## 3. 性能与资源

### 3.1 关键路径耗时目标
- **步骤 0a**:`git pull` 耗时 = 远端 commit 数 × 网络延迟(本仓库通常 < 2 秒)
- **步骤 0b**:`AskUserQuestion` 耗时 = 用户思考时间(本需求**不**优化)
- **步骤 N**:`git add` + `git commit` 耗时 = 文件数 × 写盘速度(本需求文件数 < 10,通常 < 1 秒)
- **整体新增耗时**:`< 5 秒`(不含用户思考时间)

### 3.2 并发上限
- **N/A**:本需求无并发场景(顺序工作流)

### 3.3 资源限制
- **N/A**:本需求不消耗额外资源(无内存/连接/线程)

### 3.4 缓存策略
- **N/A**:本需求不缓存任何数据

### 3.5 批量/异步
- **N/A**:本需求不批处理、也不异步

### 3.6 降级策略
- **N/A**:本需求无降级路径(失败即中断)

---

## 4. 回退策略

### 4.1 单任务回退(单个任务失败)
- **触发条件**:`code-it` 执行某任务时 Edit 失败 / 验证失败
- **步骤**:
  1. `git diff <file>` 查看当前修改
  2. 若未 commit:`git checkout <file>` 回退
  3. 若已 commit:`git revert <commit>` 或 `git reset HEAD~1`(慎用)
- **验证**:`git status --porcelain` 为空

### 4.2 整体回退(整个需求失败)
- **触发条件**:多个任务失败,无法单任务回退
- **步骤**:
  1. `git log` 查看本需求的 commit(通常 1-4 个)
  2. `git revert <commit1> <commit2> ...` 逐个 revert
  3. 或 `git reset <commit-before-REQ-00005>`(慎用,会丢失后续 commit)
- **验证**:`git status --porcelain` 为空 + 3 个 SKILL.md 回到原状

### 4.3 紧急回退(末尾 commit 失败后)
- **触发条件**:E-10 触发(末尾 commit 失败,文件已暂存)
- **步骤**:
  1. `git status` 查看暂存文件
  2. 修复 pre-commit hook 失败原因
  3. `git commit -m "<original message>"` 重试
  4. 若仍失败:`git reset HEAD <files>` 取消暂存 + `git checkout <files>` 回退
- **验证**:同上

---

## 5. 测试要点

### 5.1 单元测试
- **N/A**:本仓库无应用代码,无单元测试(`CLAUDE.md` 显式说明)
- **`code-unit` 阶段会按 REQ-00009 守卫判定"项目可测性"**:本仓库无构建/测试文件 → 守卫判定"不可测" → 测试状态 = `不适用`,**不**写 `test/.../RESULT.md`
- **本计划所有任务测试状态 = `不适用`**:因本需求只改 Markdown 文档,不写可执行代码

### 5.2 集成测试
- **N/A**:同上

### 5.3 端到端测试
- **手工验证**:`code-it` 阶段按任务详情中的"操作步骤"逐条执行
- **核心场景手工覆盖**:
  - 场景 S-1(多设备,版本不一致)→ 选 A/B/C 三种路径都要验证
  - 场景 S-2(本地一致,正常流程)→ 步骤 0a → 步骤 0b(无弹窗)→ 步骤 N
  - 场景 S-3(冲突)→ 中断 + 报错
  - 场景 S-4(S-1 ~ S-4 简化首步)→ 跳过 0b,只走 0a
  - 场景 S-5(无变更)→ 步骤 N 跳过
  - 场景 S-6(commit 失败)→ 透传 stderr

### 5.4 性能/压力测试
- **N/A**:本需求不涉及性能瓶颈

### 5.5 安全测试
- **N/A**:本需求不涉及鉴权/注入

### 5.6 回归测试
- **`code-review` 阶段执行**:评审本需求的 3 个 SKILL.md 修改是否符合"frontmatter 字节级保留"等不变量
- **建议回归项**(供 `code-review` 阶段评审):
  - 3 个 SKILL.md 的 frontmatter 与 `git show HEAD~1:<file>` 对比(应一致)
  - 4 个未触达技能 SKILL.md(`code-version` / `code-it` / `code-unit` / `code-review`)与 `git show HEAD~1:<file>` 对比(应一致)
  - `marketplace.json` / `plugin.json` 与 `git show HEAD~1:<file>` 对比(应一致)
  - CLAUDE.md / README*.md 与 `git show HEAD~1:<file>` 对比(应一致)
  - 13 个规范文件与 `git show HEAD~1:<file>` 对比(应一致)

---

## 6. 风险汇总(继承概要设计 §12)

| 风险 | 可能性 | 影响 | 缓解措施 | 回退方案 |
| --- | --- | --- | --- | --- |
| `git pull` 自动合并产生"未预期冲突" | 中 | 中 | Q-2 锁定 A + E-2 | 用户手动解冲突 |
| `code-require` 拉取后版本不一致,询问时用户错过 | 低 | 低 | E-11 协议保证 | 用户主动取消或重选 |
| 末尾兜底误纳"非本技能产生"的文件 | 低 | 低 | 本仓库长会话单用户 | 用户取消 commit + `git reset` |
| `git commit` pre-commit hook 失败 | 中 | 中 | E-10 不重试 + 透传 | 用户手动处理 |
| 3 技能"步骤 0a"实现不一致 | 中 | 中 | `module-details.md §1.2.2` 给出统一伪代码 | 派生"代码评审"任务 |
| 末尾 commit 误把 `.current-version` 变更纳入 | 中 | 低 | `.current-version` 由 `code-version` 自身 commit | N/A |
| 用户连续多次 commit,产生"无变更"步骤 | 低 | 低 | NFR-4 幂等保护 | N/A |
| `code-version` 调用失败 | 低 | 中 | FR-5.AC-5.2 独立调用隔离 | 用户手动切版本 |
| CLAUDE.md 长期不沉淀"AI 工作约定" | 中 | 中 | Q-10 留 follow-up | N/A |
| `commit-conventions.md` 长期不填充 | 中 | 低 | Q-9 留 follow-up | N/A |
| **`code-unit` 守卫判定本仓库"不可测",导致本计划任务的"测试状态"无法推进** | 高 | 低 | 本计划所有任务测试状态 = `不适用`(已知) | N/A |
| **`code-review` 评审发现"3 技能步骤 0a 实现不一致"** | 中 | 中 | `module-details.md §1.2.2 / §2.2.1 / §3.2.1` 给出统一伪代码 + `code-plan` 任务 T-001/002/003 应同时落地 | 派生"统一实现"任务 |
