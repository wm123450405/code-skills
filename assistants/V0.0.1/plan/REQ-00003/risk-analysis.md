# 风险分析 — REQ-00003

更新时间:2026-06-04 09:15
版本:V0.0.1

## 异常处理

| # | 异常路径 | 描述 | 处理策略 | 监控 |
| --- | --- | --- | --- | --- |
| E-1 | Type 识别置信度低 | 关键词不命中 / 多类型同时命中 | `AskUserQuestion` 列出候选,让用户确认 | 无 |
| E-2 | Type B / C 目标小节不存在 | CLAUDE.md 无"## AI 工作约定"小节 / 模板无"## 提示"小节 | 首次创建时,追加小节标题 + 1 个空占位 | 无 |
| E-3 | Type C 内联目标小节不匹配 | 用户指定的二级小节标题拼写错误 | 追问用户重新指定(不自动推断) | 无 |
| E-4 | 6 个新分类文件已存在 | 用户提前建过某个占位文件 | 走现有"追加"流程(不变) | 无 |
| E-5 | `module-conventions.md` 已被用户修改 | 追加 DEPRECATED 标记时,文件已被改 | `Read` 后 `Edit` 精准定位头部追加,不影响其他内容 | 无 |
| E-6 | `code-rule/SKILL.md` frontmatter 被外部修改 | INV-5 边界(本需求不改 frontmatter) | `Read` 后 `Edit` 仅改正文段,frontmatter 段一字不动 | 无 |
| E-7 | Type A 步骤 5 澄清字段失败 | 用户不愿意回答强制级别 | 沿用默认"参考"(Reference),记录到来源 | 无 |
| E-8 | 6 commit 中任一失败 | 中途出错导致部分 commit 落地 | 按 INV-1/3/4/5/6/7 验证不变量,失败则回退 | `git log --oneline` |

## 安全边界

| # | 边界 | 描述 | 依据 |
| --- | --- | --- | --- |
| S-1 | Type B 仅追加 | `code-rule` 处理 Type B 时,只**追加**到 CLAUDE.md 末尾的"AI 工作约定"小节,不修改任何其他小节(INV-3) | REQU FR-5 + FR-10 |
| S-2 | Type C 仅追加 | `code-rule` 处理 Type C 时,只**追加**到模板末尾或内联位置,不修改任何其他内容(INV-4) | REQU FR-6 + FR-10 |
| S-3 | 9 个其他 SKILL.md 零变更 | `code-rule` 不得修改其他 9 个 `code-*` 技能的 SKILL.md(包括 frontmatter) | REQU FR-9 |
| S-4 | marketplace.json / plugin.json 零变更 | `code-rule` 不得修改这两个文件 | REQU FR-9 |
| S-5 | 工作文件零变更 | `code-rule` 不得修改 `assistants/V0.0.0/` / `assistants/V0.0.1/` 下的任何工作文件 | REQU FR-9 |
| S-6 | `module-conventions.md` 仅追加标记 | 该文件**不删除**,只追加 DEPRECATED 标记 | design Q-8=H2 + INV-7 |
| S-7 | 输入校验 | 用户描述经关键词扫描 + 置信度评估后,才进入子流程;模糊描述必追问 | REQU FR-7 |
| S-8 | 审计日志 | `code-rule` 在每个类型处理完成后,在内部会话状态记录关键变更点(目标文件、插入位置、内容摘要) | REQU NFR-5 |

## 性能与资源

| # | 关注点 | 描述 | 处理 |
| --- | --- | --- | --- |
| P-1 | 关键路径预估 | `code-rule` 处理 1 条规则的关键路径 = 类型识别(< 1 秒) + 写文件(< 1 秒);无外部 IO | 用户感知无延迟 |
| P-2 | 资源限制 | 无(纯 Markdown 文件处理) | N/A |
| P-3 | 缓存策略 | 无(每次都是用户触发) | N/A |
| P-4 | 并发 | N/A(单文件串行追加) | REQU 7.2 |

## 回退策略

| # | 触发条件 | 回退步骤 | 验证 |
| --- | --- | --- | --- |
| R-1 | commit 1(SKILL.md 扩展)出错 | `git revert <commit>` 撤回 SKILL.md 变更 | `Read SKILL.md` 验证回到原状 |
| R-2 | commit 2(6 个新占位)出错 | `git revert <commit>` 撤回 6 个新文件 | `Bash ls assistants/rules/` 验证文件数 |
| R-3 | commit 3(module-conventions DEPRECATED)出错 | `git revert <commit>` 撤回 DEPRECATED 标记 | `Read module-conventions.md` 验证无 DEPRECATED 段 |
| R-4 | commit 4(templates/rule.md 扩展)出错 | `git revert <commit>` 撤回扩展 | `Read templates/rule.md` 验证回到原状 |
| R-5 | commit 5(CLAUDE.md 新小节)出错 | `git revert <commit>` 撤回小节 | `git diff CLAUDE.md` 验证 clean |
| R-6 | 6 commit 全部失败 | `git reset --hard <pre-commit-hash>` 全部回退 | `git log` 验证回到起点 |
| R-7 | INV-3 违反(Type B 重写) | 立即 `git revert commit 5` + 在 `clarifications.md` 记录事故 | `git diff CLAUDE.md` 应无"-"行 |
| R-8 | INV-5 违反(改了 marketplace.json) | 立即 `git checkout marketplace.json` + 在 `clarifications.md` 记录事故 | `git status` 应仅显示预期文件 |

## 测试要点

> 本需求**无编程逻辑**,所有测试均为**手工** + `git diff` 验证。无单元测试。

| # | 测试 | 验证内容 | 通过条件 | 关联任务 |
| --- | --- | --- | --- | --- |
| T-1 | Type A 现有流程回归 | 旧 `code-rule` 调用("函数命名用 camelCase")仍归类到命名相关 | 流程与 v0 一致 | T-007 |
| T-2 | Type A 6 分类识别 | 6 描述各命中 6 类 | 6 规则落到 6 文件 | T-002 |
| T-3 | Type A 条件性追问 | 描述触发"现在需要/未来占位/跳过" | 3 选项呈现 | T-002 |
| T-4 | Type A 占位模式 | 选"未来占位" → 创建空骨架 | 文件仅含分类标题 + 占位 | T-002 |
| T-5 | Type B 末尾追加 | 触发 Type B → CLAUDE.md 末尾新增"AI 工作约定" | 纯追加,无删除 | T-005 |
| T-6 | Type C 末尾追加 | 触发 Type C + 末尾 → 模板末尾新增"## 提示" | 纯追加 | (本 plan 不实施) |
| T-7 | Type C 内联 | 触发 Type C + 内联 + 指定小节 | 精确插入 | (本 plan 不实施) |
| T-8 | 类型识别 | 3 类典型 + 1 类模糊 | 高置信度自动,低置信度追问 | T-001 |
| T-9 | 边界 | 跑完整流程,`git status` 仅显示预期文件 | 不触及 marketplace.json / plugin.json / 其他 SKILL.md | T-007 |
| T-10 | 工作目录约定更新 | SKILL.md 目录树显示 11 个新分类 | 不含 module-conventions.md | T-001 |

**自动化测试**:**无**(本需求是技能扩展,无运行时)

**单元测试**:**不适用**(所有任务测试状态=不适用,见 INV-10)
