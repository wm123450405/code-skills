# 澄清记录 — REQ-00005(设计阶段)

更新时间:2026-06-04 16:00
版本:V0.0.2

> 本文件记录**概要设计(code-design)阶段**新增的澄清/确认项。
> 上游澄清见 `./assistants/V0.0.2/require/REQ-00005/clarifications.md`(Q-1 ~ Q-8)。

## 2026-06-04 16:00(本轮)

### 状态总览
- **无新阻塞项**:`code-require` 阶段已锁定 Q-1 / Q-2 / Q-3 / Q-4 全部 4 项,`code-design` 阶段无需重复澄清
- **无规范 vs 需求冲突**:13 个规范文件中,**无任何一条**与本需求"末尾 commit 模板"或"步骤 0a/0b 工作流"直接冲突 — 因 `commit-conventions.md` 是占位(NFR-6 显式不直接填充),`skill-conventions.md §规则 1` 由 NFR-2 严格遵守
- **无设计不确定项**:10 个关键设计问题(D-1 ~ D-10)均在 `design-notes.md` §2 给出 ≥2 个候选 + 选定方案 + 否决理由,无需用户二次决策

### 设计阶段对上游澄清的继承与扩展

| 上游 Q | 上游锁定 | 设计阶段继承 | 设计阶段扩展 |
| --- | --- | --- | --- |
| Q-1(版本不一致时选哪个版本) | A:询问用户二选一 | 完整继承为 FR-2.AC-2.3 的 3 选 1 弹窗 | — |
| Q-2(`git pull` 失败处理) | A:中断 + 报错退出 | 完整继承为 E-2 / E-3 / E-4 三种提示 | D-7 进一步分类提示语(冲突 / 网络 / 凭据) |
| Q-3(commit message 生成) | A:技能自动生成 + 预览 + 确认 | 完整继承为 FR-3.AC-3.3 + AC-3.4 | D-8 进一步明确"3 选项:确认 / 修改 / 取消" |
| Q-4(`code-it` 与末尾 commit 边界) | B:保留 code-it 内部 commit,本需求末尾兜底与之并存 | 完整继承为 FR-4.AC-4.2 + NFR-7 | D-5 进一步明确"实现层面 B = C(`git status --porcelain` 自然不列已 commit 文件)" |
| Q-5(`commit-conventions.md` 规则沉淀) | 未采用(留 follow-up) | 完整继承 NFR-6 | — |
| Q-6(`.gitignore` 与"不应提交的文件") | 采纳默认(严格遵循项目根 `.gitignore`) | 完整继承为 D-3 选定 A 的前提 | — |
| Q-7(CLAUDE.md "AI 工作约定"追加) | 未采用(留 follow-up) | 完整继承为 FR-6.AC-6.2 + NFR-6 | — |
| Q-8(`commit-conventions.md` 占位下 commit 格式) | 采纳默认(沿用 V0.0.1 实践 `chore(<scope>): <subject>`) | 完整继承为 NFR-6 | D-4 选定 A 自动生成该格式 |

### 待澄清(留 follow-up,非本设计阻塞)

#### Q-9(本轮新增,留 follow-up):`commit-conventions.md` 规则填充
- **背景**:本需求**间接**需要 `commit-conventions.md` 规则 1 填充(末尾 commit message 格式 `chore(<scope>): <subject>`),但 NFR-6 显式不在本需求中填充
- **建议回退路径**:由 `code-review` 阶段派生"用 `code-rule` 沉淀 commit 规则"任务(类似 REQ-00001-005 / REQ-00002-009 模式),由 `code-it` 实施
- **状态**:不阻塞本设计;不阻塞 `code-plan` 阶段

#### Q-10(本轮新增,留 follow-up):`plugins/code-skills/CLAUDE.md` 的"AI 工作约定"小节
- **背景**:本需求改变了 3 个技能的工作流(新增"步骤 0a" + "步骤 0b" + "步骤 N"),理论上应在 `CLAUDE.md` "AI 工作约定"小节追加"调用 `code-require` / `code-design` / `code-plan` 前需先 `git pull`"等指引
- **建议回退路径**:由 `code-rule` 沉淀(类型 B,触发 `dashboard-conventions §规则 1` 三方同步)
- **状态**:不阻塞本设计;不阻塞 `code-plan` 阶段

#### Q-11(本轮新增,留 follow-up):中英 README 同步
- **背景**:本需求改变了 3 个技能步骤,`README.md` / `README.en.md` 的"使用说明"小节有"工作流"相关描述(详见 README §安装 / §使用说明),按 `doc-conventions §规则 1` 应同步
- **建议回退路径**:由 `code-rule` 沉淀(类型 B,触发 `doc-conventions §规则 1` 中英同次提交)
- **状态**:不阻塞本设计;不阻塞 `code-plan` 阶段
- **注意**:FR-6.AC-6.3 显式声明"本需求**不**主动写 README(由 `code-rule` 沉淀)"

### 设计阶段无新增冲突

- 规范 vs 需求:13 个规范文件全部"不冲突"(`commit-conventions.md` 占位 + NFR-6 显式延后)
- 需求 vs 需求:无内部矛盾(FR-2 选 A 调 `code-version`,与 FR-5 不修改 `code-version` 兼容 — `code-version` 是"被调用方"而非"被修改方")
- 代码 vs 需求:无矛盾(本仓库无应用代码;`code-it` 内部 commit 与末尾兜底并存,D-5 选定 B)
- 设计 vs 设计:无矛盾(10 个设计问题 D-1 ~ D-10 全部闭环)
