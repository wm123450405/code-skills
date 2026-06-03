# 概要设计 — REQ-00001(Marketplace 根名称添加 `-marketplace` 后缀)

- 需求编码:REQ-00001(原 REQ-2026-0001)
- 所属版本:V0.0.1
- 设计版本:v1
- 状态:已完成(首次设计)
- 责任人:wangmiao
- 创建:2026-06-03
- 最近更新:2026-06-03 20:25
- **上游**:`./assistants/V0.0.1/require/REQ-00001/RESULT.md`(v2,7 FR / 7 NFR / 9 AC / 3 项待澄清)
- **遵循规范**:`./assistants/rules/` 下 5 个文件(详见 §11 与 `rule-compliance.md`)

---

## 1. 设计概述

本需求是 **"标识层 breaking change"**,**不新增任何模块、依赖、接口、数据结构**。设计核心是回答 4 个"如何做"的策略问题:

1. **编辑策略**:`Edit` 精确替换 vs `Write` 整文件重写 → 选 A(详见 §3 Q-1/Q-2)
2. **提交粒度**:单 commit vs 多 commit → 选 1 个 commit(详见 §3 Q-4)
3. **验证范围**:Grep 关键短语 + 字段逐项核对(详见 §4 验证路径)
4. **变更传播路径**:从 `.claude-plugin/marketplace.json` 根 `name` → 文档层 → 用户 install 命令(详见 §2 组件图)

> 本设计是"在 `code-require` 已锁定的范围内,对实施策略与不变量做可执行级细化",不重新讨论"是否改名"或"改什么字段"。

---

## 2. 架构视图

### 2.1 组件图(Mermaid)

```mermaid
graph TB
    subgraph MR["marketplace 仓库根 (code-skills/)"]
        MP[".claude-plugin/marketplace.json<br/>⚠ 改根 name:<br/>code-skills → code-skills-marketplace"]
    end

    subgraph PL["plugins/code-skills/ (目录名保持)"]
        PJ[".claude-plugin/plugin.json<br/>🚫 本需求严禁修改<br/>name=code-skills"]
        RM["README.md<br/>⚠ 改 install 命令 + marketplace name 引用"]
        RE["README.en.md<br/>⚠ 与 README.md 同次提交同步"]
        CL["CLAUDE.md<br/>⚠ Grep 后决定<br/>(若 0 命中,记录'无需修改')"]
        SK["skills/<10 技能>...<br/>🚫 本需求严禁修改 (FR-7)"]
    end

    MP -.->|plugins[0].name<br/>与 plugin.json name 同步| PJ
    MP -.->|"source": "./plugins/code-skills"| PL
    MP -.->|install 命令<br/>code-skills@code-skills-marketplace| RM
    MP -.->|同次提交| RE
    MP -.->|可能影响| CL

    style MP fill:#fff3cd
    style RM fill:#fff3cd
    style RE fill:#fff3cd
    style CL fill:#fff3cd
    style PJ fill:#f8d7da
    style SK fill:#f8d7da
```

> 图例:🟡 黄色=本需求将修改;🔴 红色=本需求严禁修改

### 2.2 变更传播路径

```
.claude-plugin/marketplace.json (根 name 改)
       │
       ├─→ 仓库内文档传播 (本需求同步)
       │     ├─→ plugins/code-skills/README.md (中)
       │     │     • install 命令:code-skills@code-skills-marketplace
       │     │     • "marketplace name" 解释段
       │     └─→ plugins/code-skills/README.en.md (英,同次提交)
       │           • 同上
       │
       └─→ 仓库外影响 (不在本需求范围)
             └─→ 已有下游用户
                   • 已注册 code-skills → 需 marketplace remove + 重新 add
```

### 2.3 验证路径

```
1. JSON 字段逐项核对 (.claude-plugin/marketplace.json)
   └─→ grep "name" 文件 → 仅 1 行变更(根 name);plugins[].name 保持

2. README 同步验证
   └─→ grep "code-skills@code-skills" README.md → 0 命中
   └─→ grep "code-skills@code-skills" README.en.md → 0 命中

3. CLAUDE.md 同步验证
   └─→ grep "code-skills@code-skills" CLAUDE.md → 0 命中 或 已改

4. 全局零残留验证
   └─→ grep "code-skills@code-skills" 全仓库 → 仅命中本需求工作目录

5. 不变量验证
   └─→ plugins/code-skills/ 目录名保持
   └─→ git remote -v 无重命名
   └─→ .claude-plugin/marketplace.json 其它字段未变
```

---

## 3. 关键设计决策(对应 design-notes.md)

### Q-1:`marketplace.json` 用什么工具修改?
- **选定**:`Edit` 工具,精确定位根 `name` 行替换
- **理由**:风险低,只动 1 行字符串;保持文件其它字段(注释、字段顺序、缩进)完全不变;diff 最小化,便于 code-review
- **规范依据**:`marketplace-protocol.md §规则 1`(不引入未知字段);`§规则 1.1`(`$schema` 必填保持)

### Q-2:`README.md` / `README.en.md` 如何修改?
- **选定**:`Edit` 工具,逐处精确替换
- **理由**:与 Q-1 同等的"diff 最小化"收益;保留 README 其它无关内容(对仗结构、版本说明、贡献指南)
- **规范依据**:`doc-conventions.md §规则 1`(中英结构对仗 + 同次提交同步)

### Q-3:`CLAUDE.md` 是否需要改?
- **选定**:`code-it` 阶段 Grep `code-skills@code-skills`、`marketplace name` 等关键短语;若无命中,在偏差日志注明"已核查,无需修改"
- **理由**:与 FR-5 主流程完全一致;即使 0 命中,也留下审计痕迹(NFR-4)
- **规范依据**:无直接对应规范(纯需求驱动);符合"可观测性 / 审计"原则(NFR-4)

### Q-4:所有变更是否必须在 1 个 commit 内?
- **选定**:**全部文件在 1 个 commit 内**
- **理由**:满足 `doc-conventions.md §规则 1` 同次提交要求;满足 NFR-3(文档同步合规);不引入中间态(改了 JSON 但 README 未改 → install 命令指向不存在的 marketplace);git revert 友好(整个改名可 1 个 commit 撤销)
- **规范依据**:`doc-conventions.md §规则 1`(同次提交)

### Q-5:`marketplace.json` 的 `version` 是否升 1.1.0?
- **现状**:Q-5 待用户澄清,REQU 文档默认 (A)
- **本设计采用默认 (A)**:保持 `1.0.0`
- **理由**:不破坏 `plugins[].version` 同步约束(`marketplace-protocol.md §规则 1.3`);breaking change 可在 commit message 中显式标注,无需 `version` 字段强制
- **回退路径**:若用户在 `code-plan` 前回答"升 1.1.0",需新增 FR-8 + AC-10;且需评估 `plugins[].version` 是否同步升(联动问题)
- **规范依据**:`marketplace-protocol.md §规则 1.3`(plugin 同步约束)

### Q-6:README 是否加"老用户迁移指引"小节?
- **现状**:Q-4(REQU 文档编号)待用户澄清,REQU 文档默认 (A)
- **本设计采用默认 (A)**:不加
- **理由**:范围最小化(NFR-5);避免触发 `doc-conventions.md §规则 1` 同步负担;NFR-1 兼容性段落(`§7 交互逻辑`)已详细列出老用户的 5 步操作流程
- **回退路径**:若用户在 `code-plan` 前回答"加迁移指引",需新增 FR-8 + AC-10
- **规范依据**:`doc-conventions.md §规则 1`(若加,需中英同步)

### Q-7:`marketplace.json` 的 `description` 是否改?
- **现状**:Q-3(REQU 文档编号)待用户澄清,REQU 文档默认 (B)
- **本设计采用默认 (B)**:不改
- **理由**:范围最小化(NFR-5);`marketplace-protocol.md §规则 1.6` 不允许引入未知字段,description 虽已存在,改其内容需说明必要性;当前 description 已能表达"工具集合 + 版本感知工作空间",与改名无关
- **回退路径**:若用户在 `code-plan` 前回答"改 description",需新增 FR-8 + AC-10
- **规范依据**:`marketplace-protocol.md §规则 1.6`(不引入未知字段)

> Q-3 / Q-4 / Q-5 三个待澄清项的完整处理过程见 `clarifications.md`。

---

## 4. 模块清单(对应 module-breakdown.md)

本需求**不新增、不修改任何应用模块**(本仓库无应用代码)。变更仅限于 4 个文件:

| # | 文件 | 状态 | 变更类型 | 详见 |
| --- | --- | --- | --- | --- |
| 1 | `.claude-plugin/marketplace.json` | 修改 | 字符串 1 行替换(根 `name`) | `module-breakdown.md` §1 |
| 2 | `plugins/code-skills/README.md` | 修改 | 字符串多处替换(命令 + 解释) | `module-breakdown.md` §2 |
| 3 | `plugins/code-skills/README.en.md` | 修改 | 字符串多处替换,与中文版**同次提交** | `module-breakdown.md` §3 |
| 4 | `plugins/code-skills/CLAUDE.md` | **可能修改** | `code-it` 阶段 Grep 后决定;若 0 命中,记录"已核查,无需修改" | `module-breakdown.md` §4 |

### 4.1 强约束不动的文件

| 文件 / 目录 | 约束来源 |
| --- | --- |
| `plugins/code-skills/.claude-plugin/plugin.json` 任何字段 | `marketplace-protocol.md §规则 1.3`(marketplace 与 plugin 的 `name` 必须保持一致) |
| `plugins/code-skills/` 目录 | NFR-2(协议合规);FR-2 显式禁止 |
| git 远端仓库名 | NFR-2(协议合规);FR-2 显式禁止 |
| 10 个 SKILL.md / 模板 | FR-7(本需求严禁修改);`skill-conventions.md §规则 1` |
| 5 个规范文件 | FR-7(本需求严禁修改) |
| V0.0.0 基线 | FR-7(本需求严禁修改) |
| `.claude/` 本地配置 | 不在 `git` 跟踪范围 |

---

## 5. 关键不变量(本需求严禁破坏)

| 不变量 | 来源 | 验证方式 |
| --- | --- | --- |
| `marketplace.json` 的 `plugins[].name` 保持 `"code-skills"` | `marketplace-protocol.md §规则 1.3` | `grep "name" .claude-plugin/marketplace.json` |
| `plugin.json` 的 `name` 保持 `"code-skills"` | `marketplace-protocol.md §规则 1.3` | `grep "name" plugins/code-skills/.claude-plugin/plugin.json` |
| `plugins/code-skills/` 目录名保持 | NFR-2 / FR-2 | `ls plugins/` |
| git 远端仓库名保持 | NFR-2 / FR-2 | `git remote -v` |
| `$schema` 字段值不变 | `marketplace-protocol.md §规则 1.1` | `grep "$schema" .claude-plugin/marketplace.json` |
| `version` 字段(根)值不变 = `1.0.0` | Q-5 默认 (A) | `grep "version" .claude-plugin/marketplace.json` |
| 全部 SKILL.md / 模板 / 规范文件 / V0.0.0 不变 | FR-7 | `git diff --stat` |

---

## 6. 接口与数据结构(对应 FR-1 / FR-2 / FR-8 / FR-9)

### 6.1 marketplace.json 字段表(本需求变更)

| 路径 | 字段 | 类型 | 改前值 | 改后值 | 变更 |
| --- | --- | --- | --- | --- | --- |
| `$.name` | 根 name | string | `"code-skills"` | `"code-skills-marketplace"` | **改** ✅ |
| `$.$schema` | 协议 schema | string | `"https://anthropic.com/.../marketplace.schema.json"` | (不变) | 保持 |
| `$.version` | 根 version | string | `"1.0.0"` | (不变,默认) | 保持 |
| `$.description` | 根 description | string | (现状) | (不变,默认) | 保持 |
| `$.owner.name` | 根 owner.name | string | `"code-skills"` | (不变) | 保持 |
| `$.plugins[0].name` | plugin name | string | `"code-skills"` | (不变) | 保持 |
| `$.plugins[0].version` | plugin version | string | `"1.0.0"` | (不变) | 保持 |
| `$.plugins[0].author.name` | author | string | `"wangmiao"` | (不变) | 保持 |
| `$.plugins[0].source` | plugin 路径 | string | `"./plugins/code-skills"` | (不变) | 保持 |
| `$.plugins[0].keywords` | keywords | string[] | (10 项) | (不变) | 保持 |
| `$.plugins[0].skills` | skills 列表 | string[] | (10 项) | (不变) | 保持 |

### 6.2 plugin.json 字段表(严禁修改)

> `plugins/code-skills/.claude-plugin/plugin.json` 任何字段**严禁修改**(FR-2 / `marketplace-protocol.md §规则 1.3`)。

### 6.3 README 中需要替换的字面量清单(待 `code-it` 阶段 `Grep` 确认)

| 字面量(改前) | 字面量(改后) | 适用文件 | 维度 |
| --- | --- | --- | --- |
| `code-skills@code-skills` | `code-skills@code-skills-marketplace` | README.md, README.en.md | install 命令 |
| "marketplace name 是 `code-skills`"或类似表述 | "marketplace name 是 `code-skills-marketplace`" | README.md, README.en.md | 解释段 |
| plugin name `code-skills` | (不变) | README.md, README.en.md | plugin 维度,保持 |

---

## 7. 三方依赖

**本需求不新增任何第三方依赖**。详细评估见 `dependencies.md`。

- 第三方运行时依赖:0(本仓库无 Node.js / Python / Go 等代码)
- 第三方构建工具:0
- 第三方测试框架:0
- 第三方 Lint 工具:0
- Claude Code 协议依赖:2(隐式)— `marketplace.json` / `plugin.json` 的 `$schema` 引用官方 JSON Schema(本需求不改 `$schema` 字段)

---

## 8. 关联设计

| 关联设计 | 关联点 | 影响 | 备注 |
| --- | --- | --- | --- |
| (本设计为首个,无同版本其他设计) | — | — | — |
| 跨版本(V0.0.0) | — | — | V0.0.0 仅 `require/EXISTING-NNN/`,无 `design/` 子目录 |

### 横向关联需求

| 关联需求 | 关联点 | 对本设计的影响 |
| --- | --- | --- |
| **REQ-00002**(编码统一) | REQ-00002 v2 锁定 TASK 编码为 `TASK-REQ-<REQ 数字段>-NNNNN`,并计划在 `code-it` 阶段清理 SKILL.md / 模板 / README / CLAUDE.md 中残留的 `REQ-2026-0001` 字符串 | **弱**:本设计产出的 `code/REQ-00001-NN/RESULT.md` 等下游路径(在 `code-it` 阶段产生)届时可能需要再补一次小批量重命名(从 `<REQ-00001>-NN` → `TASK-REQ-00001-NNNNN`);但本设计的概要设计阶段不涉及此维度(任务拆分在 `code-plan` 阶段) |
| V0.0.0 EXISTING-001 ~ EXISTING-010 | V0.0.0 基线需求的 10 个 `RESULT.md` 中含大量 `REQ-2026-0001` 示例字符串 | **弱**:本需求 FR-7 显式禁止修改 V0.0.0;这些旧示例字符串在 REQ-00002 实施阶段统一清理 |

详见 `related-designs.md`。

---

## 9. 验收标准覆盖矩阵

> 全部 9 条 AC 由 `code-it` / `code-review` 阶段执行,本设计不重复展开。

| AC | 对应需求 | 由谁验证 | 验证方式 |
| --- | --- | --- | --- |
| AC-1 | FR-1, FR-2 | code-it + code-review | diff 审阅 + JSON 字段逐项核对 |
| AC-2 | FR-2 | code-review | `git diff plugins/code-skills/.claude-plugin/plugin.json` 无输出 |
| AC-3 | FR-2 | code-review | `ls plugins/` + `git remote -v` |
| AC-4 | FR-3 | code-review | Grep README.md |
| AC-5 | FR-4, NFR-3 | code-review | 并列 diff + 章节对比 |
| AC-6 | FR-5 | code-it + code-review | Grep CLAUDE.md + 工作日志 |
| AC-7 | FR-6 | code-it + code-review | Grep 全仓库 |
| AC-8 | FR-7 | code-review | `git diff --stat` 整体审阅 |
| AC-9 | NFR-4 | code-it 收尾 | 读 V0.0.1/RESULT.md |

---

## 10. 边界与异常

| 场景 | 处理方式 |
| --- | --- |
| `marketplace.json` 被并发修改 / 未保存 | `code-it` 实施前先 `git status` 确认 working tree clean |
| README.md 中 install 命令出现非标准格式(如反引号位置、跨行) | Grep 命中后人工评估,必要时用更宽的检索模式 |
| Grep 未发现任何 `code-skills@code-skills` 字符串(可能用户已部分手改) | 在 `code-it` 偏差日志记录,继续完成 marketplace.json 改动 |
| CLAUDE.md 含 marketplace name 引用(超出预期) | 按 FR-5 同步;在 `code-it` 工作日志记录 |
| 用户改主意,要求改 owner.name / plugins[].name / 目录名 | **拒绝**在本需求范围内执行,新建 REQ 走完整流程(避免范围蔓延) |
| 改名后 `claude plugin` CLI 安装失败 | 验证 `marketplace.json` JSON 语法,验证 git 远端可达;非本需求职责的环境问题转交用户 |
| README 中存在第三方引用本仓库的命令 | 不属于本仓库自治范围,无法修改第三方引用;在 NFR-1 兼容性中提示 |

---

## 11. 规范遵循

**无偏离、无冲突、无授权偏离**。详细记录见 `rule-compliance.md`。

| 规范文件 | 关联强度 | 适用条款 |
| --- | --- | --- |
| `./assistants/rules/marketplace-protocol.md` | **强** | §规则 1(协议字段约束) |
| `./assistants/rules/doc-conventions.md` | **强** | §规则 1(README 中英同次提交);§规则 2(命令反映实际状态) |
| `./assistants/rules/dashboard-conventions.md` | 弱(不触发) | §规则 1(本需求不改看板字段约定) |
| `./assistants/rules/module-conventions.md` | 弱(不触发) | §规则 1(本需求不改技能资源) |
| `./assistants/rules/skill-conventions.md` | 弱(不触发) | §规则 1(本需求不改 SKILL.md) |

### 11.1 规范触发的关键工作流约束(本设计采纳清单)

| 规范条款 | 触发的工作流约束 | 本设计的实现 |
| --- | --- | --- |
| `marketplace-protocol.md §规则 1.1`(`$schema` 必填) | 改根 name 时不可误删 `$schema` 字段 | `code-it` 阶段 Edit 前 Read 全文,锁定仅改 1 行 |
| `marketplace-protocol.md §规则 1.2`(name kebab-case) | 改后仍为 kebab-case | `code-skills-marketplace` ✅ |
| `marketplace-protocol.md §规则 1.3`(plugin 同步) | plugin `name` 与 `version` 保持 | FR-2 显式禁止修改 |
| `marketplace-protocol.md §规则 1.4`(`source` 以 `./` 开头) | 保持 | 不改 |
| `marketplace-protocol.md §规则 1.5`(`skills` 相对路径数组) | 保持 | 不改 |
| `marketplace-protocol.md §规则 1.6`(不引入未知字段) | 不增字段 | Edit 工具仅改值,不动结构 |
| `doc-conventions.md §规则 1`(README 中英同次提交) | 1 个 commit 内同步 | `design-notes.md` §Q-4 选定单 commit |
| `doc-conventions.md §规则 2`(命令反映实际状态) | README 命令必须可用 | 本需求的目标就是让命令反映新 name |

### 11.2 待澄清项的默认值均未触发规范违反

| Q | 默认值 | 规范层面是否合规 |
| --- | --- | --- |
| Q-3 (description 是否改) | 不改 | ✅ 符合 `marketplace-protocol.md §规则 1.6`(不引入未知字段;description 字段已存在) |
| Q-4 (README 迁移指引) | 不加 | ✅ 符合 `doc-conventions.md §规则 1`(不增加就无需同步);`§规则 2` 仍满足(命令反映实际) |
| Q-5 (version 升 1.1.0) | 保持 1.0.0 | ✅ 符合 `marketplace-protocol.md §规则 1.3`(plugin 同步约束,本仓库 plugin 仍是 1.0.0) |

---

## 12. 与下游的衔接

### 12.1 `code-plan` 阶段输入
- 本设计 RESULT.md
- 7 个过程文档(`materials-index.md` / `design-notes.md` / `module-breakdown.md` / `dependencies.md` / `related-designs.md` / `rule-compliance.md` / `clarifications.md`)
- 待用户答复的 3 项 Q(Q-3 / Q-4 / Q-5),由 `code-plan` 阶段开始前最终确认

### 12.2 `code-plan` 阶段产出
- `code/REQ-00001-NN/RESULT.md`(N 个任务改修正文,每个含 file_path:line_number)
- `plan/REQ-00001/PLAN.md`(任务清单)
- 注意:本设计采用旧任务编码格式 `<需求编号>-<任务序号>`(如 `REQ-00001-01`),与 REQ-00002 v2 锁定的 `TASK-REQ-00001-NNNNN` 新格式**并存但待 REQ-00002 实施后切换**(详见 §8 关联设计)

### 12.3 任务拆分预想(供 `code-plan` 参考)

| 任务编码 | 标题 | 主要修改文件 |
| --- | --- | --- |
| `REQ-00001-01` | 改 marketplace.json 根 name + 全局 Grep 验证 | `.claude-plugin/marketplace.json` |
| `REQ-00001-02` | 同步中英 README + Grep 验证 | `plugins/code-skills/README.md`, `README.en.md` |
| `REQ-00001-03` | 核查 CLAUDE.md(可能 0 修改) | `plugins/code-skills/CLAUDE.md` |
| `REQ-00001-04` | 全仓库穷举式 Grep + 偏差日志 | (不修改文件,产出 RESULT.md) |

> 注:任务编号为预想,实际以 `code-plan` 阶段拆分为准。

---

## 13. 待澄清 / 未决项

| 编号 | 问题 | 影响范围 | 阻塞方 | 期望回复时间 |
| --- | --- | --- | --- | --- |
| Q-3 | `.claude-plugin/marketplace.json` 的 `description` 字段是否同步更新? | 本设计采用默认 (B) 不改;若改,新增 FR-8 + AC-10 | 用户 | `code-plan` 前确认 |
| Q-4 | README.md / README.en.md 是否追加"老用户迁移指引"小节? | 本设计采用默认 (A) 不加;若加,新增 FR-8 + AC-10,触发 doc-conventions §规则 1 同步 | 用户 | `code-plan` 前确认 |
| Q-5 | `marketplace.json` 的 `version` 是否从 `1.0.0` 升到 `1.1.0`? | 本设计采用默认 (A) 保持 1.0.0;若升,需评估 `plugins[].version` 是否联动升 | 用户 | `code-plan` 前确认 |

> 这 3 项**不阻塞** `code-plan` 阶段;用户随时可改主意,本设计已记录回退路径(详见 §3 Q-5/Q-6/Q-7)。

---

## 14. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-03 20:25 | v1 | 设计新增 | 完成首次概要设计:锁定 4 文件变更集(1 JSON + 2 README + 1 CLAUDE?),7 项设计决策(Q-1~Q-7 全部采用 Edit + 单 commit + 3 项 Q 默认值),关键不变量 7 条,规范遵循 100% 合规;Q-3/Q-4/Q-5 三个待澄清项采用 REQU 文档默认值 | wangmiao |
