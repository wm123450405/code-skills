# REQ-00001 — Marketplace 根名称添加 `-marketplace` 后缀

- 需求编码:REQ-00001(原 REQ-2026-0001,2026-06-03 20:20 按新命名规范提前重命名)
- 所属版本:V0.0.1
- 状态:已澄清(范围已锁定,部分 Q 待澄清)
- 责任人:wangmiao
- 创建:2026-06-03
- 最近更新:2026-06-03 20:20
- 当前版本:v2

---

## 1. 需求概述
把本仓库的 marketplace 标识(`.claude-plugin/marketplace.json` 根 `name`)从 `code-skills` 改为 `code-skills-marketplace`,在概念上把"marketplace(容器)"与"plugin(产品)"区分开,并同步更新所有引用该 marketplace name 的文档(README 中英文版本中的安装命令与说明)。**plugin 本身、目录结构、git 仓库均保持不变**。

## 2. 背景与目标
- **背景**:当前 marketplace 与其唯一的 plugin 共享同名 `code-skills`,导致安装命令 `claude plugin install code-skills@code-skills` 中两段同名,用户难以一眼分辨 "@" 前后分别代表什么角色。用户希望通过后缀显式区分这两个概念。
- **业务目标**:让 marketplace 名称具有自描述性,避免用户在添加 marketplace、安装 plugin、未来加入更多 plugin 时产生混淆。
- **本次目标**:
  1. 将 `marketplace.json` 根 `name` 修改为 `code-skills-marketplace`
  2. 不修改任何 plugin 标识、文件系统目录、git 远端仓库名
  3. 同步更新中英文 README 中所有相关引用,保证仓库与文档自洽
  4. 不打破 `marketplace-protocol`/`doc-conventions`/`dashboard-conventions` 等任何已有规则

## 3. 用户角色与场景

### 角色
- **仓库维护者 / 插件作者**(wangmiao):执行改名与文档同步
- **下游使用者**(通过 `claude plugin marketplace add` 引入本仓库的用户):受 install 命令变化影响,需要按新命令重新安装

### 场景

#### 场景 1:维护者按本需求实施改名(主流程)
- 作为 **仓库维护者**,我想要 **把 marketplace 根 name 加上 `-marketplace` 后缀**,以便 **让 marketplace 与 plugin 的标识在视觉与语义上区分**
- **前置条件**:在 V0.0.1 工作空间;READMEs 与 marketplace.json 已纳入 git 跟踪
- **主流程**:修改 marketplace.json 根 `name` → 全仓库搜索 `code-skills@code-skills` 与"marketplace name"相关引用 → 同步 README.md 与 README.en.md → 提交
- **异常**:若搜索发现其它隐藏引用(如 CLAUDE.md、其它文档),需一并修订;若发现 `plugins[].name` 被无意改动,立即回滚至 `code-skills`(规则强制约束)

#### 场景 2:下游使用者按新命令安装(衍生流程)
- 作为 **下游使用者**,我想要 **按 README 给出的最新命令安装 plugin**,以便 **不被旧命令误导**
- **前置条件**:已读 README 安装段
- **主流程**:`claude plugin marketplace add <git-url>` → `claude plugin install code-skills@code-skills-marketplace` → `/reload-plugins`
- **异常**:已用旧命令注册了 marketplace 的老用户 → 需先 `marketplace remove code-skills`(旧 marketplace name)→ 再按新命令重做(详见 Q-4 待澄清)

## 4. 功能需求(FR)

### FR-1:修改 `marketplace.json` 根 `name` 字段
- **描述**:将 `.claude-plugin/marketplace.json` 中根级 `"name": "code-skills"` 修改为 `"name": "code-skills-marketplace"`
- **入口**:用户在版本 V0.0.1 工作空间内通过 `code-design` → `code-plan` → `code-it` 推进
- **前置条件**:已读取 `assistants/rules/marketplace-protocol.md`,确认改根 `name` 不会触发 `plugins[].name` / `plugin.json` `name` 失配约束
- **主流程**:
  1. 读 `.claude-plugin/marketplace.json`
  2. 仅修改根 `name` 字段值
  3. 校验:文件其它字段(`$schema`、`version`、`description`、`owner.name`、`plugins[*]`)完全未变
- **分支/异常**:JSON 格式被意外破坏 → 立即回滚至前一状态(`code-it` 阶段使用 Edit 而非 Write,降低风险)
- **数据变化**:仅 `.claude-plugin/marketplace.json` 一处字符串变更;不影响版本工作空间数据
- **来源**:M-2(澄清问答 Q2 选项 A)+ M-3(marketplace.json 现状)

### FR-2:保持其它命名与目录全部不变
- **描述**:**禁止**修改下列任何项:
  - `.claude-plugin/marketplace.json` 的 `$schema`、`version`、`description`、`owner.name`、`plugins[0].name`、`plugins[0].version`、`plugins[0].author.name`、`plugins[0].source`、`plugins[0].keywords`、`plugins[0].skills`
  - `plugins/code-skills/.claude-plugin/plugin.json` 任何字段
  - 文件系统目录(`plugins/code-skills/` 不重命名)
  - git 远端仓库名(`wm123450405/code-skills.git` 不重命名)
- **入口**:作为对 FR-1 的反向约束,贯穿全流程
- **主流程**:在 `code-it` 实施时,执行精确 Edit 操作,且代码评审(`code-review`)逐字段核对未列入"应改"清单的字段未受影响
- **分支/异常**:发现任一禁改项被改动 → 立即回滚
- **数据变化**:无
- **来源**:M-2(澄清问答 Q2 选项 A 显式排除)+ M-8(marketplace-protocol §规则 1 强制约束)

### FR-3:同步更新 `plugins/code-skills/README.md`(中文版)中的安装命令与 marketplace name 引用
- **描述**:在 `plugins/code-skills/README.md` 中:
  - 把所有 `code-skills@code-skills` 形式的安装命令替换为 `code-skills@code-skills-marketplace`
  - 把所有显式表述"marketplace name 是 `code-skills`"或类似含义的文字调整为反映新 name `code-skills-marketplace`
  - 安装命令示例段(当前第 14 行 `claude plugin install code-skills@code-skills`)更新到新值
  - 注释段(当前第 22 行)对 marketplace name 的解释同步
- **入口**:由 `code-it` 实施
- **前置条件**:FR-1 已完成;README.md 与 README.en.md 必须**同次提交**修订(规则强制)
- **主流程**:
  1. 全文检索 `code-skills@code-skills`、`marketplace name` 等关键短语
  2. 逐处评估含义,精确替换或重写
  3. 不修改 README.md 与本次改名无关的章节
- **分支/异常**:若发现 README.md 同时含"plugin install 命令"与"plugin 名"两种 `code-skills` 用法,必须仅替换 marketplace name 维度;plugin name `code-skills` 保持
- **数据变化**:仅 README.md 文本变更
- **来源**:M-5(README.md 现状)+ M-9(doc-conventions §规则 2)

### FR-4:同步更新 `plugins/code-skills/README.en.md`(英文版)中的安装命令与 marketplace name 引用
- **描述**:对应 FR-3 的英文版同步;命令字符串与 FR-3 完全一致(`code-skills@code-skills-marketplace`);英文表述与中文表述结构对仗
- **入口**:由 `code-it` 实施;与 FR-3 在**同一次 commit** 内完成
- **前置条件**:FR-3 改动同时进行
- **主流程**:对照 README.md 改动逐项把英文版同步
- **分支/异常**:任何中文版改动未在英文版同步 = 触发 `doc-conventions §规则 1` 违规;`code-review` 必须并列对比两文件
- **数据变化**:仅 README.en.md 文本变更
- **来源**:M-6(README.en.md 现状)+ M-9(doc-conventions §规则 1)

### FR-5:核查并视情况更新 `plugins/code-skills/CLAUDE.md`
- **描述**:全文检索 CLAUDE.md 是否含 marketplace name 字面量引用(如 `code-skills@code-skills`、"marketplace name 是 `code-skills`")
  - 若**有** → 一并同步为新值,在同次提交内
  - 若**无**(仅含结构性叙述如"marketplace 仓库根"等)→ 无需修改,在 `code-it` 实施日志中显式记录"已核查,无需修改"
- **入口**:由 `code-it` 实施
- **主流程**:Grep 检索 → 评估每条命中 → 决定改或不改
- **分支/异常**:不得修改 CLAUDE.md 中与本需求无关的章节
- **数据变化**:CLAUDE.md 可能变更或保持
- **来源**:M-7(CLAUDE.md 现状)+ M-9(doc-conventions §规则 2)

### FR-6:全仓库穷举式检索遗漏引用
- **描述**:在 `code-it` 阶段完成 FR-1 ~ FR-5 后,执行全仓库 Grep:
  - 关键短语:`code-skills@code-skills`(install 命令)、`"name": "code-skills"`(JSON 字段,需区分 marketplace/plugin 维度)
  - 输出每处命中的判定:已改 / 不应改(plugin 维度)/ 遗漏待改
  - 必须确保不存在"应改未改"的遗漏点
- **入口**:由 `code-it` 实施;由 `code-review` 复核
- **主流程**:
  1. Grep `code-skills@code-skills` → 全部应改为 `code-skills@code-skills-marketplace`
  2. Grep `"name": "code-skills"` → 仅 marketplace.json 根行为本次改动点;plugin.json 行与 plugins[].name 行保持
  3. 记录所有判定到 `code/REQ-00001-NN/RESULT.md`(沿用旧任务编码格式 `<需求编号>-<任务序号>`,待 REQ-00002 实施后切换为 `TASK-REQ-00001-NNNNN`)
- **分支/异常**:发现遗漏 → 补改;发现"似应改实不应改"的引用 → 在评审报告中说明保持理由
- **数据变化**:依据检索结果可能产生额外编辑
- **来源**:M-9(doc-conventions §规则 2)+ 分析笔记 R-2

### FR-7:不修改任何 SKILL.md / 模板 / 规范文件
- **描述**:本需求严禁修改:
  - `plugins/code-skills/skills/*/SKILL.md` 任何文件
  - `plugins/code-skills/skills/*/templates/*` 任何模板
  - `./assistants/rules/*` 任何规范文件(包括 `marketplace-protocol.md`)
  - 其它版本目录 `./assistants/V0.0.0/*` 任何文件
- **入口**:作为全流程的反向约束
- **主流程**:`code-review` 必须显式核对未改动列表
- **分支/异常**:发现任一上述文件被改动 → 立即回滚
- **数据变化**:无
- **来源**:M-2(澄清 Q2 选项 A)+ M-8/M-9/M-10(规则强制最小化范围)

## 5. 非功能需求 / 约束(NFR)

### NFR-1(兼容性)
- 本变更属**breaking change**:老用户先前注册的 marketplace 名 `code-skills` 在改名后不再匹配,需先 `claude plugin marketplace remove code-skills` 再按新命令重新 `add` + `install`
- 是否在 README 中加迁移指引 → 见 Q-4

### NFR-2(协议合规)
- 必须严格符合 `./assistants/rules/marketplace-protocol.md §规则 1`:
  - `$schema` 保持原值(必填)
  - `name` 改为 `code-skills-marketplace`(仍为 kebab-case)
  - `version` 保持 `1.0.0`(本规则未要求改 version,但 Q-5 待用户决定是否升 minor)
  - `plugins[].name` 与 `plugins/code-skills/.claude-plugin/plugin.json` 的 `name` 必须**继续一致**(均为 `code-skills`)
  - 不引入未知字段

### NFR-3(文档同步合规)
- 必须严格符合 `./assistants/rules/doc-conventions.md`:
  - §规则 1:README.md 与 README.en.md 同步变更,**同一次 commit**
  - §规则 2:README 中所有命令/路径必须反映改名后的仓库实际状态;不留"指向不存在的 marketplace name"的 install 命令

### NFR-4(可观测性 / 审计)
- 改动必须可追溯:
  - 在 V0.0.1 版本看板的"变更记录"区段追加本需求条目(本技能在收尾时执行)
  - 后续 `code-design` / `code-plan` / `code-it` 各阶段同步在版本看板对应区段登记
  - `code-it` 阶段产出 `code/REQ-00001-NN/RESULT.md`,完整列出每个修改点的 file_path:line_number

### NFR-5(可维护性 / 最小化)
- 不引入任何额外抽象、配置项、参数化命名机制 — 单纯字符串替换
- 不为本需求新增工具脚本、CI 配置或自动化检查

### NFR-6(安全)
- 无新安全面;仅文档与协议清单文本变更
- 不引入鉴权/加密/审计相关变更

### NFR-7(国际化)
- README 英文版必须与中文版语义对仗;不引入新语言版本(超出本需求范围)

## 6. 页面与界面
- **不适用**:本需求不涉及 GUI / Web 页面 / 终端 UI;仅 JSON 协议清单字段与 Markdown 文档文本变更

## 7. 交互逻辑
- **不适用**(本需求是静态文件文本编辑,无交互流程)
- 衍生用户操作流程(NFR-1 兼容性):
  ```
  老用户当前状态:已 marketplace add 并安装 code-skills@code-skills
  ↓
  仓库改名后用户操作:
  1. claude plugin uninstall code-skills@code-skills
  2. claude plugin marketplace remove code-skills
  3. claude plugin marketplace add <git-url>(同 URL,但注册名变 code-skills-marketplace)
  4. claude plugin install code-skills@code-skills-marketplace
  5. /reload-plugins
  ```
  > 是否在 README 中明示该流程 → 见 Q-4

## 8. 数据与状态
- **核心实体**:
  - `marketplace.json`(`$schema`/`name`/`version`/`description`/`owner`/`plugins[]`)— 仅根 `name` 变更
  - `plugin.json`(`$schema`/`name`/`version`/`description`/`author`/`keywords`)— **不变**
  - `README.md` / `README.en.md`(Markdown 文档)— 多处文本变更
- **实体关系**:marketplace `plugins[].name` 1:1 关联 plugin.json `name`(本次保持一致)
- **状态生命周期**:无状态实体(纯静态清单)
- **数据来源**:全部来自仓库本身的版本控制文件
- **数据保留**:历史值在 git 历史中保留,无额外保留策略

## 9. 边界与异常

| 场景 | 处理方式 |
| --- | --- |
| `marketplace.json` 被并发修改 / 未保存 | `code-it` 实施前先 `git status` 确认 working tree clean |
| README.md 中 install 命令出现非标准格式(如反引号位置、跨行) | Grep 命中后人工评估,必要时用更宽的检索模式 |
| Grep 未发现任何 `code-skills@code-skills` 字符串(可能用户已部分手改) | 在 `code-it` 偏差日志记录,继续完成 marketplace.json 改动 |
| CLAUDE.md 含 marketplace name 引用(超出预期) | 按 FR-5 同步;在 `code-it` 工作日志记录 |
| 用户改主意,要求改 owner.name / plugins[].name / 目录名 | **拒绝**在本需求范围内执行,新建 REQ 走完整流程(避免范围蔓延) |
| 改名后 `claude plugin` CLI 安装失败 | 验证 `marketplace.json` JSON 语法,验证 git 远端可达;非本需求职责的环境问题转交用户 |
| README 中存在第三方引用本仓库的命令(如"我们把 code-skills 加入了 X marketplace") | 不属于本仓库自治范围,无法修改第三方引用;在 NFR-1 兼容性中提示 |

## 10. 验收标准(AC)

### AC-1:marketplace.json 根 `name` 已改且仅改此处
- **对应需求**:FR-1, FR-2
- **验证方式**:diff 审阅 + JSON 字段逐项核对
- **步骤**:
  1. `git diff .claude-plugin/marketplace.json` 查看变更
  2. 确认变更仅为根 `"name": "code-skills"` → `"name": "code-skills-marketplace"` 一行
  3. 其它字段(`$schema`/`version`/`description`/`owner.name`/`plugins[*]`)逐项对比改前快照,确认无变化
- **预期结果**:diff 输出仅显示 1 行 `-` + 1 行 `+`,且变更内容符合 FR-1 描述
- **优先级**:高

### AC-2:plugin.json 完全未改动
- **对应需求**:FR-2
- **验证方式**:`git diff plugins/code-skills/.claude-plugin/plugin.json`
- **步骤**:执行 diff 命令
- **预期结果**:无输出(无变更)
- **优先级**:高

### AC-3:仓库目录与 git 远端未改名
- **对应需求**:FR-2
- **验证方式**:
  - `ls plugins/` 应包含 `code-skills/`(不含 `code-skills-marketplace/`)
  - `git remote -v` 不应出现重命名远端
- **预期结果**:目录与远端均保持原值
- **优先级**:高

### AC-4:中文版 README.md 中所有相关引用已同步
- **对应需求**:FR-3
- **验证方式**:Grep + 人工核对
- **步骤**:
  1. `Grep "code-skills@code-skills"` README.md → 0 命中(应全部已改为 `code-skills@code-skills-marketplace`)
  2. 人工读 README.md 中"安装"与"marketplace name 解释"两段,确认语义自洽
- **预期结果**:无残留旧 marketplace name 引用;新 install 命令完整可执行
- **优先级**:高

### AC-5:英文版 README.en.md 与中文版结构对仗且引用同步
- **对应需求**:FR-4, NFR-3
- **验证方式**:并列 diff + 章节对比
- **步骤**:
  1. 把 README.md 与 README.en.md 的二级标题列出,确认完全对仗(每节都有对应)
  2. 把 install 命令与 marketplace name 引用并列对比,确认两文件均使用新值
  3. 确认两文件在**同一次 commit** 内变更
- **预期结果**:结构对仗 + 引用同步 + 单次 commit
- **优先级**:高

### AC-6:CLAUDE.md 已核查并(如需要)同步
- **对应需求**:FR-5
- **验证方式**:Grep + 工作日志确认
- **步骤**:
  1. `Grep "code-skills@code-skills"` CLAUDE.md
  2. 若命中 → 确认已改为新值
  3. 若 0 命中 → 在 `code-it` 偏差/工作日志注明"已核查,CLAUDE.md 无需修改"
- **预期结果**:CLAUDE.md 不残留旧 marketplace name 字面量引用,或有明确"无需修改"记录
- **优先级**:中

### AC-7:全仓库穷举式检索零遗漏
- **对应需求**:FR-6
- **验证方式**:Grep 全仓库
- **步骤**:
  1. `Grep "code-skills@code-skills"` 全仓库 → 应仅命中本需求工作文件(本 RESULT.md、过程文档)
  2. `Grep "marketplace.*code-skills"` 全仓库(排除版本工作空间与本需求文档) → 命中点逐一核对
- **预期结果**:仓库内除本需求工作目录外,所有面向最终用户的文档与配置均使用 `code-skills-marketplace`
- **优先级**:高

### AC-8:未修改任何 SKILL.md / 模板 / 规范文件 / V0.0.0
- **对应需求**:FR-7
- **验证方式**:`git diff --stat` 整体审阅
- **步骤**:
  1. 执行 `git diff --stat`
  2. 确认变更文件集合仅包含:`.claude-plugin/marketplace.json`、`plugins/code-skills/README.md`、`plugins/code-skills/README.en.md`、(可能)`plugins/code-skills/CLAUDE.md`、本 V0.0.1 工作空间产出物
  3. 不应出现 `plugins/code-skills/skills/**`、`plugins/code-skills/skills/*/templates/**`、`assistants/rules/**`、`assistants/V0.0.0/**` 的变更
- **预期结果**:变更文件集合严格在白名单内
- **优先级**:高

### AC-9:版本看板已同步更新
- **对应需求**:NFR-4
- **验证方式**:`Read assistants/V0.0.1/RESULT.md`
- **步骤**:
  1. 确认"需求清单"含本需求条目(状态=已完成,关联文档链接正确)
  2. 确认"变更记录"含本次需求新增的条目
  3. 后续 `code-design` / `code-plan` / `code-it` / `code-review` 在各自阶段持续追加
- **预期结果**:版本看板与工作目录文件保持一致
- **优先级**:高

## 11. 关联需求

| 关联需求编码 | 关联点 | 对本需求的影响 | 链接 |
| --- | --- | --- | --- |
| — | 本版本(V0.0.1)首个需求,V0.0.0 基线全部 EXISTING-NNN 均与本次改名无强耦合 | 无 | 详见 `related-requirements.md` |

> 详细扫描结果与关联规范约束见 [related-requirements.md](./related-requirements.md)

## 12. 待澄清 / 未决项

| 编号 | 问题 | 影响范围 | 阻塞方 | 期望回复时间 |
| --- | --- | --- | --- | --- |
| Q-3 | 是否需要同步更新 `.claude-plugin/marketplace.json` 的 `description` 字段(当前为英文简介,可能在 marketplace 列表 UI 中展示)? | 非阻塞;若改,新增小规模 FR | 用户 | `code-design` 前确认 |
| Q-4 | 是否需要在 README.md / README.en.md 中追加"老用户迁移指引"小节,明示从 `@code-skills` 改为 `@code-skills-marketplace` 的步骤? | 非阻塞;若加,新增 FR-8;若不加,在 commit message 中提及 breaking change | 用户 | `code-design` 前确认 |
| Q-5 | 是否需要把 `marketplace.json` 的 `version` 从 `1.0.0` 升到 `1.1.0`(以语义化版本标识 breaking change)?注意 plugin.json `version` 是独立轴,本次默认保持 `1.0.0` | 非阻塞;若升,新增 1 项 FR + 1 项 AC | 用户 | `code-design` 前确认 |

> 这些项不阻塞进入 `code-design`;但建议在进入 `code-design` 前回答,以便概要设计完整覆盖。

## 13. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-03 20:10 | v1 | 初始创建 | 完成首次需求澄清:确定需求编码 REQ-2026-0001、改名范围为"仅 marketplace.json 根 name"、产出 7 条 FR / 7 条 NFR / 9 条 AC / 3 项待澄清 | wangmiao |
| 2026-06-03 20:20 | v2 | 重命名 | 按用户指令提前采用新命名规范:目录 `./assistants/V0.0.1/require/REQ-2026-0001/` → `REQ-00001/`;文档内"需求编码"、title、`code/<task>` 路径中的旧编码同步更新;**历史变更记录(v1 条目)保留原字面值**作为审计线索。本需求标题、范围、FR/NFR/AC、Q-3/Q-4/Q-5 均未变化。**说明**:本重命名为 REQ-00002 FR-6 的部分提前落地,仅完成"目录+本工作空间内引用"维度;SKILL.md / 模板 / README / CLAUDE.md 中的旧编码引用仍由 REQ-00002 `code-it` 阶段统一清理 | wangmiao |
