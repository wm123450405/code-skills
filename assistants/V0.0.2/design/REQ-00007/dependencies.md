# 三方依赖评估 — REQ-00007

更新时间:2026-06-05 09:25
版本:V0.0.2

> 遵循规范:`./assistants/rules/dependency-conventions.md`(占位,不影响本评估);`NFR-1 零新增依赖`(强约束)

## 1. 新增依赖评估

**结论:0 新增依赖**(NFR-1 强约束)。

| 依赖名称 | 版本 | 来源 | 必要性 | 评估结果 |
| --- | --- | --- | --- | --- |
| (无) | — | — | — | — |

## 2. 已复用依赖(运行时/工具)

`code-auto` 是**单文件 SKILL.md**(纯 Markdown 文本),运行时**仅依赖** Claude Code 平台已提供的工具集,**不**引入任何外部库:

| 工具 | 提供方 | 用途 | 在 `code-auto` 中出现位置 |
| --- | --- | --- | --- |
| `Skill` 工具 | Claude Code 模型层 | 跨技能调用(6 个子技能) | 工作流步骤 1-6 |
| `Read` 工具 | Claude Code 模型层 | 读 `.current-version` / `plan/PLAN.md` / `review/REVIEW-REPORT.md` | 步骤 0 / 步骤 4 解析 / 步骤 5/6 解析 |
| `Write` 工具 | Claude Code 模型层 | 写 `auto-report.md`(完成时) | 步骤 N(完成分支) |
| `Bash(git pull)` | Claude Code 模型层 | 步骤 0a(沿用 REQ-00005 模式) | 步骤 0a |
| `Glob` / `Grep` | Claude Code 模型层 | 可选(辅助解析) | 步骤 5/6 解析 |

**说明**:以上工具均由 Claude Code 模型层提供,**不**是"三方依赖"(`dependency-conventions` 关注的"库/包"维度)。

## 3. 已复用子技能(被驱动方)

| 子技能 | 提供方 | 调用方式 | 在 `code-auto` 中出现位置 |
| --- | --- | --- | --- |
| `code-require` | 本仓库(已存在) | `Skill` 工具 | 步骤 1 |
| `code-design` | 本仓库(已存在) | `Skill` 工具 | 步骤 2 |
| `code-plan` | 本仓库(已存在) | `Skill` 工具 | 步骤 3 |
| `code-it` | 本仓库(已存在) | `Skill` 工具 | 步骤 4 / 步骤 6 |
| `code-unit` | 本仓库(已存在) | `Skill` 工具 | 步骤 4 / 步骤 6(按需) |
| `code-review` | 本仓库(已存在) | `Skill` 工具 | 步骤 5 |

**说明**:以上均为本仓库内已存在的技能,**不**是"三方依赖",是"被驱动模块"。

## 4. 安全性 / 维护活跃度 / 体积评估

**N/A(无新增依赖,无需评估)。**

## 5. 内部源可复用替代

**N/A(无新增依赖,无需寻找替代)。**

## 6. 协议文件(非依赖,只读引用)

| 文件 | 角色 | 修改行为 |
| --- | --- | --- |
| `./.claude-plugin/marketplace.json` | marketplace 清单 | **不修改**(FR-8.AC-8.3) |
| `./plugins/code-skills/.claude-plugin/plugin.json` | 子插件清单 | **不修改**(FR-8.AC-8.3) |
| `./plugins/code-skills/README.md` + `README.en.md` | 中英 README | "主要能力"段**同次提交追加 1 行**(FR-8.AC-8.5) |

**说明**:本设计**不**修改 marketplace.json / plugin.json,因此**不**触发 `marketplace-protocol.md §规则 1` 的"plugins[].skills 数组追加"约束——但**注意**:本设计新增 1 个 `code-auto` 技能,**未来**应**在同次提交中**更新 `marketplace.json` 的 `plugins[].skills` 数组(由 `code-it` 任务 T-N 在落地时执行);**本设计**仅说明这一动作的**责任在 code-it**,不直接修改 marketplace.json(避免在 `code-design` 阶段越权)。

**调整说明**:本节标记的"未来由 code-it 追加"实际触发 `marketplace-protocol.md §规则 1`(plugins[].skills 追加 1 项 `./skills/code-auto`),由 code-it 任务按规范同次提交,本设计不强约束该任务的具体位置。

## 7. 体积 / 性能影响

| 项 | 影响 |
| --- | --- |
| SKILL.md 文件大小 | 预计 ~600 行 Markdown,约 25 KB(可接受) |
| 运行时内存 | 仅 `code-auto` 自身工作流上下文;不缓存子技能产物(子技能自己写盘) |
| 磁盘写入 | 完成时 1 次 `auto-report.md` 写入(约 2-5 KB) |
| 网络影响 | 步骤 0a `git pull` × 1(沿用 REQ-00005 模式);子技能内部首步 `git pull` × N1+N2+N3(沿用 REQ-00005)— 已在 NFR-4 范围 |
| CPU / 性能 | 无特殊计算;仅文件 I/O + 工具调用 |

## 8. 安全态势

- **`code-auto` 不持有任何凭据**;不读 `.env` / `secrets` 文件
- **`code-auto` 不修改 `.git/`**;沿用子技能各自的 git 行为
- **`code-auto` 不写代码 / 配置 / 数据库**;仅写 `auto-report.md`
- **子技能失败立即中断**(Q-2 锁定 A);不静默继续

## 9. 依赖管理总结

| 维度 | 评估结论 |
| --- | --- |
| 新增依赖 | 0(NFR-1 强约束,100% 合规) |
| 复用既有依赖 | 5 个 Claude Code 工具 + 6 个子技能(全部已存在) |
| 协议文件变更 | 0(`marketplace.json` / `plugin.json` 不动;由 code-it 任务追加 skills[]) |
| 体积影响 | SKILL.md ~25 KB(可接受) |
| 安全态势 | 无新增攻击面 |
