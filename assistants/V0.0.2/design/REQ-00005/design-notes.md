# 设计笔记 — REQ-00005

更新时间:2026-06-04 16:00
版本:V0.0.2

## 1. 关键设计问题清单

| # | 设计问题 | 归属 | 规范依据 |
| --- | --- | --- | --- |
| **D-1** | "步骤 0a 拉取最新代码"应放在"步骤 0 之前"还是"步骤 0 内"? | 工作流位置 | `skill-conventions.md`(工作流结构惯例) |
| **D-2** | `code-require` 的"步骤 0b 版本对齐检查"如何与"步骤 0a 拉取"协同? | 子流程顺序 | `skill-conventions.md` §"版本感知工作空间" |
| **D-3** | "末尾兜底提交"的文件范围:用 `git status --porcelain` 自动收集,还是技能显式枚举? | 边界 | NFR-4(幂等) + NFR-7(与 code-it 边界) |
| **D-4** | "末尾兜底提交"是否要求用户确认 commit message,还是自动 commit? | 交互 | Q-3 锁定 A(预览 + 确认) |
| **D-5** | "末尾兜底提交"与 `code-it` 内部 commit 的协同模式:取代、并存、还是互斥? | 边界 | Q-4 锁定 B(并存) |
| **D-6** | `code-require` FR-2.AC-2.4 调 `code-version` 是"内联调用"还是"独立技能调用"? | 解耦 | FR-5 锁定"独立技能调用" |
| **D-7** | "步骤 0a 拉取"失败的 3 种情况(冲突 / 网络 / 凭据)如何区分提示? | 错误处理 | NFR-5 + E-2/E-3/E-4 |
| **D-8** | "末尾兜底提交"的 commit message 模板是否需要支持"修改"? | 交互 | Q-3 锁定 A(可修改) |
| **D-9** | `.current-version` 在 `git pull` 之前/之后的对比基准是哪个? | 数据语义 | NFR-8(必须拉取后) |
| **D-10** | "末尾兜底提交"在"git 不存在"时如何处理? | 异常 | E-12 |

## 2. 候选方案与选定

### D-1:步骤 0a 位置

| 方案 | 描述 | 优势 | 劣势 |
| --- | --- | --- | --- |
| **A(选定)** | 步骤 0a(拉取)在步骤 0(版本上下文检测)**之前** | "拉取后"再读 `.current-version`,避免"陈旧上下文"陷阱(NFR-8);语义清晰:"先同步远端,再读本地" | 工作流多一步 |
| B | 步骤 0a 嵌入步骤 0 内(先拉,后读) | 步骤数不变 | 步骤 0 变成"复合步骤",破坏现有"单一职责"风格;`code-require` 需把 0a 嵌进 0,`code-design` 也要嵌 — 重复实现 |
| C | 步骤 0a 作为"步骤 -1" | 显式"前置守卫" | 引入"负数步骤"违反惯用约定 |

**选定 A**:
- 需求文档 §7.1 / §7.2 流程图已明确:步骤 0a → 步骤 0 → 步骤 1 → ... → 步骤 N
- NFR-8 强制"拉取后"状态作为版本对比基准,A 方案满足
- 3 个技能工作流对称(都"先拉,后做"),便于评审 / 维护
- 规范依据:`skill-conventions.md §规则 1` — frontmatter 不变;工作流正文可"追加新编号步骤",不破坏既有结构

### D-2:`code-require` 步骤 0a/0b 协同

| 方案 | 描述 | 优势 | 劣势 |
| --- | --- | --- | --- |
| **A(选定)** | 0a(拉取)→ 0b(版本对齐检查)→ 0(版本上下文检测) | 子流程严格串行,职责单一;0a 是"纯拉取",0b 是"读 + 对比",0 是"沿用 0b 的结果";不重复读 `.current-version` | 多 1 个步骤 |
| B | 0a(拉取)→ 0(版本上下文检测,内含"版本对齐"逻辑) | 步骤数不变 | 把"版本对齐"逻辑塞进"版本上下文检测",语义混杂;`code-design` / `code-plan` 的"步骤 0"会**被迫**也做"版本对齐" — 违反 FR-2("仅 `code-require` 专属") |
| C | 0(版本上下文检测)→ 0a(拉取,内置"重新检测") | "检测 → 同步 → 重新检测"成环 | 复杂,易引入"递归"逻辑;首次检测无意义 |

**选定 A**:
- 需求文档 §7.1 明确"0a → 0b → 0"
- 严格隔离 `code-require` 专属逻辑(0b)与公共逻辑(0),`code-design` / `code-plan` 不受影响
- 规范依据:NFR-8 强约束(拉取后才对比)

### D-3:末尾兜底文件范围收集方式

| 方案 | 描述 | 优势 | 劣势 |
| --- | --- | --- | --- |
| **A(选定)** | `git status --porcelain` 全量收集 | 自动覆盖所有变更(含本技能**间接**产生的文件);与"无变更时跳过"语义一致(NFR-4);不依赖"显式枚举" | 可能误纳"非本技能产生的文件"(如用户在另一终端 `git pull` 后产生的新 dirty) |
| B | 技能显式枚举"本技能本次产生的文件" | 范围精确 | 易遗漏(本技能运行时间长,中间可能派生文件);维护成本高 |
| C | 用 `git diff --name-only HEAD` 替代 `--porcelain` | 只看"已暂存 + 工作区" | 语义相同(`--porcelain` 已含),无差异 |

**选定 A**:
- NFR-4 要求"无变更时跳过",`git status --porcelain` 行为最自然
- 误纳"非本技能文件"在本仓库语境下基本不存在(用户长会话内极少并行操作)
- 规范依据:NFR-4(幂等 / 不空 commit)+ NFR-7(与 `code-it` 边界 — `code-it` 内部 commit 完成的文件**不会**出现在 `git status --porcelain` 中,因为 `code-it` 已 commit)

### D-4:commit message 生成方式

| 方案 | 描述 | 优势 | 劣势 |
| --- | --- | --- | --- |
| **A(选定)** | 技能自动生成 + 预览 + 用户确认(Q-3 锁定 A) | 用户有最终决定权;不阻塞;符合"AI 协作"惯例 | 多 1 次交互 |
| B | 技能自动生成 + 不询问,直接 commit | 0 交互 | 用户失去控制;commit message 可能语义不准 |
| C | `git add` 后留空,让用户自己写 commit | 最灵活 | 用户在长会话中可能忘;打破"AI 协作"惯例 |

**选定 A**:
- Q-3 已锁定 A
- NFR-6 要求"格式与 V0.0.1 实践一致",自动生成可保证一致性

### D-5:与 `code-it` 内部 commit 的协同

| 方案 | 描述 | 优势 | 劣势 |
| --- | --- | --- | --- |
| A | 去掉 `code-it` 内部 commit,末尾统一 | 单一提交点 | 改 `code-it` 行为,违反 FR-4(不修改 `code-it`) |
| **B(选定)** | 保留 `code-it` 内部 commit,本需求末尾兜底提交与之并存(Q-4 锁定 B) | 职责清晰:`code-it` 管"任务级代码",末尾兜底管"过程文件 + 看板" | 可能有"重复 commit"风险(`code-it` 已 commit 的文件**不会**再次进入 `git status --porcelain`,因为已 commit) |
| C | 二者共存,末尾 commit 跳过已 commit 的文件 | 与 B 等价(B 的实现方式就是"自然跳过") | 概念上多余,实现上 B 已经覆盖 |

**选定 B**:
- Q-4 已锁定 B
- `code-it` 内部 commit 后,文件进入 git history,**不再**是 working tree dirty;`git status --porcelain` 自然不列出 — 实现层面 B = C,无需特判
- 规范依据:`marketplace-protocol.md §规则 1` — 协议层文件不动;FR-4 显式禁止修改 `code-it`

### D-6:`code-version` 调用形式

| 方案 | 描述 | 优势 | 劣势 |
| --- | --- | --- | --- |
| **A(选定)** | 独立技能调用(FR-5.AC-5.2 锁定) | 隔离性强,`code-version` 失败不影响 `code-require` 整体;符合 Claude Code 技能体系 | 多一次技能切换 |
| B | 内联调用(在同一上下文内直接执行 `code-version` 的命令) | "原子性" | 破坏技能边界;`code-version` 可能写文件,污染 `code-require` 上下文;违反 FR-5 |

**选定 A**:
- FR-5.AC-5.2 显式要求"独立技能调用"
- 与"长会话 / 多设备"场景下"用户随时可重跑 `code-require`"的语义契合

### D-7:拉取失败区分

| 方案 | 描述 | 优势 | 劣势 |
| --- | --- | --- | --- |
| **A(选定)** | 按 git 退出码 + stderr 关键词分类(冲突 / 网络 / 凭据) | 用户看到具体原因,处理有方向 | 需要解析 stderr |
| B | 统一提示"`git pull` 失败" | 简单 | 用户无法判断是冲突 / 网络 / 凭据 |

**选定 A**:
- NFR-5 显式要求"stderr 透传",A 方案在透传基础上加"前置分类提示",更好
- 需求文档 §9 E-2 / E-3 / E-4 已列 3 种情况的预期提示语

### D-8:commit message 是否支持修改

| 方案 | 描述 | 优势 | 劣势 |
| --- | --- | --- | --- |
| **A(选定)** | 弹 3 选项:确认 / 修改 / 取消(Q-3 锁定 A) | 用户有最终决定权 | 多 1 个选项 |
| B | 仅"确认 / 取消" | 简化 | 用户无法调整语义 |

**选定 A**:
- Q-3 已锁定 A
- 与 D-4 协同

### D-9:版本对比基准

| 方案 | 描述 | 优势 | 劣势 |
| --- | --- | --- | --- |
| **A(选定)** | "拉取后"状态(在 0a 完成后立即 Read `.current-version`) | NFR-8 强约束,语义清晰 | 必须在 0a 之后**立即**读,不能缓存 |
| B | "拉取前"状态 | 简单 | 与"用户实际感知的工作版本号"可能脱节(0a 已覆盖) |
| C | "拉取前 + 拉取后"双读 | 容错 | 多余(拉取前状态对决策无价值) |

**选定 A**:
- NFR-8 强制要求
- 需求文档 §NFR-8 关键实现明确指出"git pull 完成后**立即** Read .current-version"

### D-10:`git` 不存在处理

| 方案 | 描述 | 优势 | 劣势 |
| --- | --- | --- | --- |
| **A(选定)** | 启动时探测 `git --version`,失败 → 中断 + 提示"本需求需要 git" | 早失败,避免后续奇怪错误 | 多 1 步探测 |
| B | 不探测,直接 `git pull` 失败再处理 | 少 1 步 | 错误信息不友好 |

**选定 A**:
- 需求文档 §9 E-12 显式要求
- "早失败"是良好工程实践

## 3. 关键不变量(本设计严禁破坏)

| 不变量 | 来源 | 验证方式 |
| --- | --- | --- |
| 3 个 SKILL.md 的 YAML frontmatter 完全不变 | `skill-conventions.md §规则 1` + FR-6.AC-6.x + NFR-2 | `git diff <SKILL.md>` 顶部 ~10 行无变化 |
| 4 个未触达技能(`code-version` / `code-it` / `code-unit` / `code-review`)的 SKILL.md 完全不变 | FR-4 + FR-5 | `git diff` 该 4 个文件无输出 |
| `marketplace.json` / `plugin.json` 任何字段不变 | FR-6.AC-6.1 + `marketplace-protocol.md §规则 1` | `git diff .claude-plugin/ plugins/code-skills/.claude-plugin/` 无输出 |
| `commit-conventions.md` 规则 1 不被本需求填充 | NFR-6 | `git diff commit-conventions.md` 无输出 |
| `code-dashboard` / `code-publish` / `code-auto` 等其他技能不被波及 | REQ-00004 / 00006 / 00007 边界继承 | 那些技能的 SKILL.md 不在 `git diff` 范围 |
| `code-require` 拉取后**立即**读 `.current-version` 作版本对比基准 | NFR-8 | SKILL.md 工作流步骤描述中显式列出"读取拉取后版本" |
| `code-it` 内部 commit 行为不变 | FR-4 + Q-4 锁定 B | `code-it/SKILL.md` 不在 `git diff` 范围;末尾兜底流程不感知 `code-it` 状态 |

## 4. 关键工作流约束(本设计采纳清单)

| 规范条款 | 触发的工作流约束 | 本设计的实现 |
| --- | --- | --- |
| `skill-conventions.md §规则 1`(frontmatter 不变) | 不修改 YAML 头部 | `code-require/SKILL.md` 等 3 个文件**只改正文**,frontmatter 字节级一致 |
| `dashboard-conventions.md §规则 1`(看板字段约定扩展需三同步) | 不扩展字段(本需求只追加"概要设计清单"一条记录 + "变更记录"一条记录) | 看板同步走现有"概要设计清单" + "变更记录"区段,无新字段 |
| `marketplace-protocol.md §规则 1`(不引入未知字段) | 不改 `marketplace.json` / `plugin.json` | FR-6 显式禁止 |
| `doc-conventions.md §规则 1`(README 中英同次提交) | 本需求**不**写 README(留 follow-up) | 工作流步骤描述中"末尾兜底提交"覆盖的"过程文件 + 结果文件"**不**含 README |
| `commit-conventions.md`(占位) | 不直接填充规则 | NFR-6 显式留 follow-up;末尾 commit message 沿用 V0.0.1 实践 |

## 5. 风险与缓解(详细见 RESULT.md §12)

| 风险 | 可能性 | 影响 | 缓解 | 回退 |
| --- | --- | --- | --- | --- |
| `git pull` 自动合并产生"未预期冲突" | 中 | 中 | Q-2 锁定 A(中断 + 报错退出) | 用户手动解冲突后重跑 |
| `code-require` 拉取后版本不一致,询问时用户错过 | 低 | 低 | `AskUserQuestion` 必须答,无超时(E-11) | 用户主动取消或重选 |
| 末尾兜底误纳"非本技能产生"的文件 | 低 | 低 | 本仓库长会话单用户,基本无并发 | 用户取消 commit,手动 `git reset` |
| `git commit` pre-commit hook 失败 | 中 | 中 | E-10 显式不重试,stderr 透传 | 用户手动处理 |
| 3 技能"步骤 0a"实现不一致 | 中 | 中 | 需求文档 §7.1 / §7.2 流程图已统一,`code-plan` 阶段强校验对称性 | 派生"代码评审"任务,统一实现 |
| 末尾 commit 误把 `.current-version` 变更纳入 | 中 | 低 | `.current-version` 在 `code-require` FR-2 选 A 时**也会**被 `code-version` 切换 — 由 `code-version` 自己的 commit 处理(本设计不感知) | N/A |
