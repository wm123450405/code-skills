# 材料登记 — REQ-00007(详细设计阶段)

更新时间:2026-06-05 09:50
版本:V0.0.2

## 项目级规范

| 规范文件 | 类别 | 关键约束摘要 | 本阶段相关 |
| --- | --- | --- | --- |
| `skill-conventions.md` | 技能编写 | §规则 1:SKILL.md frontmatter 含 name+description,name 与目录名一致 | ✅ 强约束 |
| `module-conventions.md`(DEPRECATED 但沿用) | 模块规划 | §规则 1:templates/checklists/guidelines 固定子目录 | ✅ 强约束 |
| `dashboard-conventions.md` | 看板与版本工作空间 | §规则 1:字段约定扩展需 3 处同步 | ✅ 不触发(不扩展字段) |
| `doc-conventions.md` | 文档编写 | §规则 1:README 中英同次提交 + 结构对仗;§规则 2:README 必须存在 | ✅ 强约束(由 code-it 任务同次提交) |
| `marketplace-protocol.md` | Marketplace 协议 | §规则 1:$schema/name/version 必填;source `./`;skills `./` 路径数组 | ✅ 强约束(由 code-it 任务追加 skills[]) |
| `encoding-conventions.md` | 编码格式 | §规则 1-4:REQ/BUG 5 位;TASK 嵌套 5+5 位;§规则 4 实施流程 | ✅ 强约束(任务编码双格式兼容解析) |
| `migration-mapping.md` | 编码迁移 | §规则 1-4:已落地映射;EXISTING-NNN 不追溯 | ✅ 不触发(不触达历史编码) |
| `directory-conventions.md` | 目录与模块 | 占位 | ❌ 不触发 |
| `coding-style.md` | 代码风格 | 占位 | ❌ 不触发 |
| `commit-conventions.md` | 提交与合并 | 占位(NFR-3 显式不沉淀) | ❌ 不触发 |
| `dependency-conventions.md` | 三方依赖 | 占位(NFR-1 显式零新增依赖) | ❌ 不触发 |
| `framework-conventions.md` | 框架选型 | 占位 | ❌ 不触发 |
| `naming-conventions.md` | 命名风格 | 占位 | ❌ 不触发 |

## 上游需求

- **来源**:`./assistants/V0.0.2/require/REQ-00007/RESULT.md`(v1,已锁定)
- **提取的 FR / NFR / AC**:10 FR / 10 NFR / ~40 AC / 5 锁定(Q-1~Q-5)+ 7 采纳默认(Q-6~Q-12)+ 1 建议派生(Q-13)

## 上游概要设计

- **来源**:`./assistants/V0.0.2/design/REQ-00007/RESULT.md`(v1,已完成首次)
- **提取的模块拆分 / 接口概要 / 数据结构 / 决策**:
  - M-1 `code-auto` SKILL.md(单文件,~600 行,7 步骤状态机)
  - M-2 `auto-report.md`(运行时产物)
  - 6 个子技能零修改(FR-8.AC-8.1)
  - 7 项关键设计决策 D-1~D-7
  - 解析锚点:`^## .*$` + `^\| .* \|$` + 任务编码双格式正则
  - 100% 规范合规

### 关键交叉点(每条 FR 对应的详细设计点)

| FR | 概要设计章节 | 本详细设计章节 |
| --- | --- | --- |
| FR-1 | §7.2 M-1 frontmatter | §4.1 M-1 内部结构 |
| FR-2 | §7 步骤 0 + 输入解析 | §5 算法 1(启动解析) |
| FR-3 | §6.3 状态机 | §5 算法 2~3(主循环)+ §10 状态机 |
| FR-4 | §7 步骤 4 任务循环 | §5 算法 4(任务循环) |
| FR-5 | §7 步骤 5/6 评审循环 | §5 算法 5(评审循环) |
| FR-6 | §6 通用 prompt 约束 | §5 算法 6(选推荐项) |
| FR-7 | §7 步骤 7 异常路径 | §5 算法 7(异常处理) |
| FR-8 | §7 全局(零修改) | §4.3 修改模块清单(0 个) |
| FR-9 | §10 报告输出格式 | §6.1 `auto-report.md` 完整 schema |
| FR-10 | §10.3 写入时机 | §6.1 + §5 算法 7.3 |

## 项目现状(实现细节)

### 命名风格(从既有 11 个 SKILL.md 提取)

- **技能目录名**:kebab-case(`code-init` / `code-version` / `code-rule` / `code-require` / `code-design` / `code-plan` / `code-it` / `code-unit` / `code-fix` / `code-review` / `code-publish`)
- **frontmatter 字段**:`name`(必,kebab-case 与目录名一致)+ `description`(必,自然语言一段话,含"做什么+何时用")
- **章节标题**:H1 主标题 + H2 章节 + H3 子章节(与既有 SKILL.md 风格一致)

### 错误处理范式

- **不修改既有子技能** = `code-auto` 自身的错误处理范式独立定义
- `code-auto` 采用:**检测 → 报告 → 退出**(无 try/catch,因 SKILL.md 是 Markdown 而非代码;错误以**输出文本**形式呈现)
- **退出码语义**:`0` = 完成 / `≠ 0` = 异常中断 / `130` = SIGINT 中止

### 并发原语

- **N/A**:`code-auto` 是单次串行执行,无并发原语(由 NFR-2 强约束)
- **不维护内存状态**:`code-auto` 不缓存子技能产物;每次从文件重新解析(由 NFR-8 + Q-11 锁定)

### 既有相似功能的实现风格(参考)

- `code-publish/SKILL.md`(V0.0.2,475 行,8 任务):章节结构 12 段(目标 / 适用 / 不适用 / 目录 / 输入 / 输出 / 工具 / 工作流 / 看板 / 衔接 / 不要做),**本设计完全沿用**
- `code-require/SKILL.md` / `code-design/SKILL.md` / `code-plan/SKILL.md`:**章节结构同 `code-publish`**,**本设计完全沿用**

### 既有测试用例风格(本仓库无传统单元测试)

- **仓库无构建/测试文件**(代码单元测试状态全部 `不适用`,由 REQ-00009 守卫判定)
- `code-publish` PLAN.md 8 任务测试状态全 `不适用`(纯文档型)
- **本设计 5 个任务全部为"纯文档型"(写 SKILL.md + 改 README + 改 marketplace.json + 同步看板)**,测试状态**默认 `不适用`**

### 可复用的工具函数(本设计 N/A)

- `code-auto` 本身不写代码,无工具函数需求
- 子技能各自的工作流(`code-require` 等)已存在,本设计**零复用工具**(直接调子技能)

## 本次变更源

**N/A(首次详细设计,无变更源对比)**。
