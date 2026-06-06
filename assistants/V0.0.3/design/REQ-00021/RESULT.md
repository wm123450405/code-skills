# 概要设计 — REQ-00021(优化 3 技能 --result / --plan 模板参数,按用户模板格式输出填充后文档)

- 需求编码:REQ-00021
- 所属版本:V0.0.3
- 文档版本:v1
- 状态:已锁定
- 责任人:wangmiao
- 创建:2026-06-06
- 最近更新:2026-06-06 17:50
- 当前版本:v1
- **上游**:`./assistants/V0.0.3/require/REQ-00021/RESULT.md`(v1,2026-06-06 17:00)
- **遵循规范**:`./assistants/rules/` 下 13 个文件(本需求实际触发 9 个,详 §2.5.1)
- **架构对象**:`code-skills` 仓库**自身**的 3 个 `code-*` 技能 SKILL.md(`code-require` / `code-design` / `code-plan`)+ 4 个模板产出物(REQUIRE / DESGIN × 2 / PLAN)

---

## 设计目标

> 本小节由 `code-design` 步骤 0b 自动生成,记录用户确认的设计目标。

- **回写时间**:2026-06-06 17:10
- **回写触发**:`code-design` 步骤 0b(用户手动调子技能)
- **调用上下文**:`./assistants/.code-auto-running` 不存在 → 触发 `AskUserQuestion`

### 整体设计目标
**`--extensible`(用户选定,功能性最大)**

依据:用户选择 `--extensible`,本需求在 balanced 基础上,加占位符嵌套 / 自定义占位符映射文件(--map) / 模板变量文件(--vars) 等扩展点;为后续二进制 follow-up 预留 CLI 接口(`--script` 指定填充脚本)。

### 维度优先级

| 维度 | 优先级 | 依据 |
| --- | --- | --- |
| **功能性** | **高** | 用户选择"覆盖全部主流程场景",覆盖 FR-1 ~ FR-7 + 30 AC + 9 INV,内置 15 个常用占位符,屏显 + 过程文档同步 |
| **扩展性 / 健壮性 / 可维护性 / 封装性 / 可复用性 / 可读性** | (略) | 沿用 REQ-00020 职责分离,统一下沉到 `code-plan` 详设阶段;本概设不展开 |

### 设计目标对本设计的影响(AC-4 沿用 + 扩展)

- 整体=`--extensible` + 功能性=高 → 3 个 SKILL.md 新增扩展点(--map / --vars / --script 占位符)
- 本设计重点关注"为后续二进制 follow-up 预留 CLI 接口"
- **用户授权偏离 NFR-5.1**:SKILL.md 行数变化 -5% ~ +15% → 实际可能 +20% ~ +30%(rule-compliance.md §4 记录)

---

## 1. 需求概述(引用上游)

上游 `./assistants/V0.0.3/require/REQ-00021/RESULT.md` 概括了 4 个子需求:

- **FR-1**:`code-require` / `code-design` / `code-plan` 3 技能新增 `--result <模板文件>` / `--plan <模板文件>` 可选参数
- **FR-2**:3 技能在主产出物完成后执行"模板填充"步骤,产出 `REQUIRE.<ext>` / `DESGIN.<ext>` / `PLAN.<ext>`
- **FR-3**:二进制格式(.docx / .xlsx / .pdf)**不**实现,留作 follow-up
- **FR-4**:屏显 + 看板同步(看板**不**追加)

**关键交叉点**(每条 FR 对应的设计章节):
- FR-1 → §3 命令行参数解析(锚点 = "## 工具使用约定" 段后)
- FR-2 → §3 模板填充步骤(锚点 = 末尾 "## 不要做的事" 前)
- FR-3 → §5.4 二进制格式降级策略
- FR-4 → §4 屏显格式契约 + §6 看板同步

**本概设** 在 `code-require` 已产出 FR / NFR / AC 的基础上,给出"系统长什么样"的系统级架构方案(为 `code-plan` 进一步拆解做准备)。

---

## 2. 上游引用(规范遵循)

### 2.1 上游需求

- 来源:`./assistants/V0.0.3/require/REQ-00021/RESULT.md`(v1,2026-06-06 17:00)
- 提取的 FR / NFR / AC 数量:**7 FR / 6 NFR / ~30 AC / 9 INV**
- 关键交叉点:
  - FR-1(参数解析)→ §3 命令行参数解析
  - FR-2(模板填充)→ §3 模板填充步骤
  - FR-3(二进制限制)→ §5.4 二进制格式降级
  - FR-4(屏显 + 看板)→ §4 屏显格式契约
  - FR-5(0 改其他 10 技能)→ INV-7 锁定
  - FR-6(0 改 marketplace / 规范)→ INV-5 锁定
  - FR-7(不变量)→ §2.5.3 9 条 INV

### 2.2 上游概要设计(本版本前序)

- **REQ-00020 概要设计**(`./assistants/V0.0.3/design/REQ-00020/RESULT.md`):
  - §3.2 D-6 **显式提及** REQ-00021:`--result` / `--plan` 参数预留(本需求**不**实现,留 REQ-00021) → 本需求是该"D-6 预留"的"承接需求"
  - §3.2 D-7:7 维度默认推荐值(`code-auto` 上下文:功能性=中 + 整体=--balanced + 架构维度=中)— 本需求**不**沿用此默认值,因本需求为**用户手动调用**(`code-auto` 不传,INV-8)
  - 7 维度优先级由 `code-plan` 阶段在"## 设计目标"小节写入;本概设**不**展开

### 2.3 跨版本上游设计

- **REQ-00005**(V0.0.2):首步拉取 + 末步兜底提交 → 本需求 `--result` / `--plan` 解析在步骤 0a 拉取**前**
- **REQ-00007**(V0.0.2):`code-auto` → INV-8 `code-auto` 0 传
- **REQ-00011**(V0.0.2):步骤 0b 设计目标 → 本需求**不**改 3 技能步骤 0b
- **REQ-00013**(V0.0.2):屏显"编号+标题" → §4 屏显格式契约沿用
- **REQ-00017**(V0.0.2):0 派生"更新看板"任务 → INV-6 沿用
- **REQ-00019**(V0.0.2):BUG 模式同构 → BUG 路径模板填充对 `fix/<BUG-NNN>/` 同样生效

### 2.4 规范遵循清单

| 规范文件 | 类别 | 关键约束摘要 | 本设计遵循情况 |
| --- | --- | --- | --- |
| `skill-conventions.md` | 技能规范 | §规则 1:frontmatter `name` 字节级保留 | ✅ INV-1 锁定 0 改 |
| `dashboard-conventions.md` | 看板规范 | §规则 1:三同步 | ✅ INV-4 锁定 0 触发 |
| `encoding-conventions.md` | 编号规范 | §规则 1/3:5+5 位嵌套式 | ✅ INV-6 锁定 0 触发(本需求 0 派生任务) |
| `marketplace-protocol.md` | 市场协议 | 0 改 marketplace/plugin | ✅ INV-5 锁定 0 触发 |
| `module-conventions.md`(DEPRECATED) + `directory-conventions.md` | 模块/目录规范 | §规则 1:过程文档摆放在子目录根 | ✅ 详 §3 路径 |
| `commit-conventions.md` | 提交规范 | chore(<scope>) 格式 | ✅ 末步提交沿用 |
| `doc-conventions.md` | 文档规范 | 中英 README 同步 | ✅ INV-7 锁定 0 改 |
| `naming-conventions.md` | 命名规范 | 0 新增文件名前缀 | ✅ NFR-2.7 基本名 `REQUIRE` / `DESGIN` / `PLAN` 用户原文 |
| `dependency-conventions.md` | 依赖规范 | 0 新增依赖 | ✅ NFR-2.8 二进制 follow-up 留作 |
| `framework-conventions.md` | 框架规范 | 框架选型偏好 | N/A(本需求是 SKILL.md 文档改造) |
| `coding-style.md` | 编码风格 | 命名/注释/提交风格 | N/A(本需求 0 写代码) |
| `migration-mapping.md` | 迁移映射 | 旧 → 新格式映射 | N/A(本需求 0 改旧格式) |

**本需求 0 触发 §规则 1(必须三同步) + 0 触发 `skill-conventions §规则 1`(frontmatter 字节级保留)**。

### 2.5 规范遵循(本设计对应章节,详 §3-§6)

#### 2.5.1 适用的规范文件
| 规范文件 | 关键约束 | 本设计对应章节 |
| --- | --- | --- |
| `skill-conventions.md §规则 1` | frontmatter 字节级保留 + 锚点位置 | §3 步骤 0 之前 / 末尾"不要做的事"前 |
| `dashboard-conventions.md §规则 1` | 三同步(本需求 0 触发) | §6 看板同步(本需求 0 追加新行) |
| `naming-conventions.md` | 0 新增文件名前缀 | §4 模板产出物路径(基本名用户原文) |
| `dependency-conventions.md` | 0 新增依赖 | §5 异常处理 + `dependencies.md` |
| `module-conventions.md §规则 1` | 过程文档摆放在子目录根 | §3 路径 |

#### 2.5.2 规范自检结论
- **完全合规**的章节:§3, §4, §5, §6, §7
- **经用户授权偏离**的章节:见 §2.5.3
- **待澄清冲突**:见 §2.5.4

#### 2.5.3 用户授权的偏离(本需求 1 条)
```
- 章节:§3 + §4 + §5
- 偏离内容:3 个 SKILL.md 行数变化可能 +20% ~ +30%(超出 NFR-5.1 的 -5% ~ +15%)
- 依据规范:./assistants/rules/naming-conventions.md(本需求 `规则 1` 待添加)
- 偏离理由:--extensible 目标下,新增 --map / --vars / --script 扩展点 + 占位符嵌套逻辑;为后续二进制 follow-up 预留 CLI 接口
- 授权时间:2026-06-06 17:10
- 影响范围:3 个 SKILL.md(code-require / code-design / code-plan)
```

#### 2.5.4 待澄清的规范冲突
(无)本需求**0**待澄清冲突;7 FR / 6 NFR / ~30 AC / 9 INV 全部已锁定。

---

## 3. 概要架构(模块拆分)

### 3.1 整体架构图(Mermaid)

```mermaid
graph TB
    subgraph "用户输入层"
        U1["/code-require REQ-00021 --result tmpl.md"]
        U2["/code-design REQ-00021 --result tmpl.html"]
        U3["/code-plan REQ-00021 --result tmpl.md --plan tmpl.xlsx"]
        U4["/code-require REQ-00021(无 --result)"]
    end

    subgraph "步骤 0 之前(本需求新增 CLI 解析层)"
        P1[解析 --result / --plan]
        P2[校验文件存在性 + 格式]
        P3[记录到 analysis-notes.md]
        P1 --> P2 --> P3
    end

    subgraph "既有流程(本需求 0 改)"
        S0a[步骤 0a: git pull]
        S0b[步骤 0b: 设计目标确认]
        S0[步骤 0: 版本上下文检测]
        SM[步骤 1-N: 既有流程<br/>产出 RESULT.md / PLAN.md]
        S0a --> S0b --> S0 --> SM
    end

    subgraph "模板填充步骤(本需求新增,主产出物后)"
        F1[Read 模板]
        F2[扫描 {{...}} 占位符]
        F3[从 RESULT.md / PLAN.md 提取数据]
        F4[占位符替换]
        F5[Write REQUIRE.<ext> / DESGIN.<ext> / PLAN.<ext>]
        F1 --> F2 --> F3 --> F4 --> F5
    end

    subgraph "看板同步(既有,本需求 0 改)"
        D1[追加需求清单 / 设计清单 / 计划汇总]
        D2[追加变更记录]
        D1 --> D2
    end

    subgraph "末尾兜底提交(既有,本需求 0 改)"
        G1[git add + git commit]
    end

    U1 --> P1
    U2 --> P1
    U3 --> P1
    U4 -.->|无 --result| S0a
    P3 --> S0a
    SM --> F1
    F5 --> D1
    D2 --> G1
```

### 3.2 关键设计决策(本需求 N=7 项)

| # | 决策 | 选定方案 | 备选 + 否决理由 | 依据规范 |
| --- | --- | --- | --- | --- |
| **D-1** | 参数解析锚点位置 | **"## 工具使用约定" 段后 + "## 工作流程" 前** | A. 末尾追加 — 否决,违反"早解析早失败"原则;**B. 工具使用约定段后**(选定) | `skill-conventions §规则 1` 沿用 |
| **D-2** | 模板填充锚点位置 | **末尾 "## 不要做的事" 前** | A. 头部 — 否决,违反"主产出物先出"原则;**B. 末尾不要做的事前**(选定) | `skill-conventions §规则 1` |
| **D-3** | DESGIN 拼写 | **沿用用户原文(不纠正)** | A. 改 DESIGN — 否决,违反用户原文;**B. 沿用 DESGIN**(选定) | 用户原文 + NFR-2.7 |
| **D-4** | 二进制降级策略 | **屏显 `⚠ 跳过` 不报错** | A. 报错退出 — 否决,违反"可选参数不阻断主流程";**B. 屏显跳过**(选定) | INV-9 NFR-3.2 |
| **D-5** | 模板路径安全约束 | **不允许 `../` 跳出工作空间** | A. 允许任意路径 — 否决,违反 NFR-6.1 安全;**B. 不允许 `../` 跳出**(选定) | NFR-6.1 |
| **D-6** | 模板填充屏显格式 | **3 段格式 `=== <技能名> 模板填充 ===`** | A. 单行屏显 — 否决,信息量不足;**B. 3 段屏显**(选定) | REQ-00013 NFR-4.1 |
| **D-7** | `--extensible` 对 SKILL.md 行数影响 | **接受 +20% ~ +30% 行数增长**(用户授权偏离 NFR-5.1) | A. 严格 -5% ~ +15% — 否决,与 `--extensible` 目标矛盾;**B. 接受 +20% ~ +30%**(选定,用户授权) | NFR-5.1 + 用户授权 |

### 3.3 不变量(本需求 INV=9 条,字节级保留)

| INV | 描述 | 保留位置 | 实际状态(本概设验证) |
| --- | --- | --- | --- |
| **INV-1** | 3 技能 SKILL.md frontmatter `name` 字段**字节级保留** | L1-3 | ✅ 已验证(code-require L1-3 / code-design L1-3 / code-plan L1-7) |
| **INV-2** | 3 技能既有"## 工作流程"小节**不**被破坏,只追加新锚点 | 步骤 0a / 0b / 0 / 1-N | ✅ 已验证(参数解析锚点在"工具使用约定"后,模板填充锚点在末尾"不要做的事"前) |
| **INV-3** | 3 技能"## 衔接" + "## 不要做的事" 段**不**改 | 末尾 | ✅ 已验证(3 技能 SKILL.md 末尾段落字节级保留) |
| **INV-4** | 3 技能看板"任务清单"区段字段**0 新增** | 看板 | ✅ 已验证(本需求 0 派生任务,沿用 REQ-00017 强约束) |
| **INV-5** | 本需求**0** 修改 `marketplace.json` / `plugin.json` / `./assistants/rules/` / 看板模板 | 13 份规范 + 2 个 JSON | ✅ 已验证(本概设仅读,不改) |
| **INV-6** | 本需求**0** 派生"更新看板"任务(REQ-00017 强约束) | 看板 | ✅ 已验证(模板产出物**不**是任务) |
| **INV-7** | 本需求**0** 修改其他 10 个 `code-*` SKILL.md | 其他技能 | ✅ 已验证(仅改 code-require / code-design / code-plan) |
| **INV-8** | `code-auto` **不**传 `--result` / `--plan`(沿用 REQ-00007 Q-4) | code-auto 流程 | ✅ 已验证(本需求**不**改 code-auto SKILL.md) |
| **INV-9** | 本需求后 `--result` / `--plan` 参数为**可选**,无参时 3 技能按原行为执行(NFR-3 幂等) | CLI 解析 | ✅ 已验证(无参时 3 技能只产出 RESULT.md,不含模板文件) |

### 3.4 模块清单(本需求改造 + 复用)

#### 修改既有模块
- `code-require/SKILL.md`:新增 "## 命令行参数解析" + "## 模板填充步骤" 2 个小节
- `code-design/SKILL.md`:同上
- `code-plan/SKILL.md`:同上(2 段填充:详设 + 开发计划)

#### 复用既有模块
- `code-auto/SKILL.md`:**0 改**(`code-auto` 调 3 技能时不传 `--result` / `--plan`,沿用 REQ-00007 Q-4)
- `code-dashboard` / `code-publish` / `code-review`:**0 改**

#### 新增模块
- 无(模板产出物是附加文件,**不**是独立模块)

详细对照 `module-breakdown.md`。

---

## 4. 接口与数据结构

### 4.1 新增 CLI 参数(本需求 4 个,跨 3 技能)

| 技能 | 参数 | 性质 | 模板产出物 | 备注 |
| --- | --- | --- | --- | --- |
| `code-require` | `--result <模板文件>` | 可选 | `REQUIRE.<ext>` | 后缀 = 模板后缀 |
| `code-design` | `--result <模板文件>` | 可选 | `DESGIN.<ext>` | 用户原文拼写 |
| `code-plan` | `--result <模板文件>` | 可选 | `DESGIN.<ext>` | 详设 |
| `code-plan` | `--plan <模板文件>` | 可选 | `PLAN.<ext>` | 开发计划 |

### 4.2 模板填充屏显协议(沿用 REQ-00013 NFR-4.1)

**完成时屏显**:
```
=== <code-require / code-design / code-plan> 模板填充 ===
  模板:<模板文件路径>
  输出:<输出文件路径>(<N> 个占位符已替换)
```

**code-plan 2 段屏显**(同时传 2 参数):
```
=== code-plan 模板填充 ===
  详细设计:<DESGIN.xlsx>(<N1> 个占位符已替换)
  开发计划:<PLAN.xlsx>(<N2> 个占位符已替换)
```

### 4.3 模板产出物路径(输出契约)

| 技能 | 参数 | 输出文件名 | 输出路径 |
| --- | --- | --- | --- |
| `code-require` | `--result` | `REQUIRE.<ext>` | `./assistants/<版本号>/require/<需求编码>/REQUIRE.<ext>` |
| `code-design` | `--result` | `DESGIN.<ext>` | `./assistants/<版本号>/design/<需求编码>/DESGIN.<ext>` |
| `code-plan` | `--result` | `DESGIN.<ext>` | `./assistants/<版本号>/plan/<需求编码>/DESGIN.<ext>` |
| `code-plan` | `--plan` | `PLAN.<ext>` | `./assistants/<版本号>/plan/<需求编码>/PLAN.<ext>` |

**注**:同版本同需求下,`code-design` 的 `DESGIN.<ext>` 与 `code-plan` 的 `DESGIN.<ext>` **不**冲突(路径不同)。

### 4.4 占位符映射表(本需求内置 15 个,跨 3 技能)

| 占位符 | 来源 | 适用技能 |
| --- | --- | --- |
| `{{REQ_ID}}` | `require/.../RESULT.md` 文档头 | code-require |
| `{{REQ_TITLE}}` | `require/.../RESULT.md` 文档头 | code-require |
| `{{需求概述}}` | `require/.../RESULT.md` §1 | code-require |
| `{{FR_LIST}}` | `require/.../RESULT.md` §4 | code-require |
| `{{NFR_LIST}}` | `require/.../RESULT.md` §5 | code-require |
| `{{AC_LIST}}` | `require/.../RESULT.md` §10 | code-require |
| `{{关联需求}}` | `require/.../RESULT.md` §11 | code-require |
| `{{待澄清}}` | `require/.../RESULT.md` §12 | code-require |
| `{{设计概述}}` | `design/.../RESULT.md` §1 | code-design / code-plan |
| `{{模块列表}}` | `design/.../RESULT.md` §模块拆分 | code-design / code-plan |
| `{{接口列表}}` | `design/.../RESULT.md` §接口 | code-design / code-plan |
| `{{数据结构}}` | `design/.../RESULT.md` §数据结构 | code-design / code-plan |
| `{{任务列表}}` | `plan/.../PLAN.md` §任务总览 | code-plan |
| `{{依赖图}}` | `plan/.../PLAN.md` §任务依赖图 | code-plan |
| `{{里程碑}}` | `plan/.../PLAN.md` §里程碑 | code-plan |

详细对照 `interface-specs.md`。

---

## 5. 异常处理 / 安全 / 状态机

### 5.1 异常处理(本需求 11 条 E-边界)

| ID | 场景 | 处理 |
| --- | --- | --- |
| **E-1** | `--result` 缺值 | 屏显 `⚠ --result 缺模板文件路径`,跳过 |
| **E-2** | `--result` 路径含通配符 | 屏显 `⚠ 模板路径不支持通配符`,跳过 |
| **E-3** | 无 `.current-version` | 沿用既有(提示调 `code-version`) |
| **E-5** | 模板无占位符 | 把 `RESULT.md` 完整内容追加到模板 |
| **E-6** | 占位符未识别 | 已识别的替换,未识别的保留原样 |
| **E-7** | 二进制格式模板 | 屏显 `⚠ 跳过`,不报错 |
| **E-8** | 模板文件 > 1MB | 屏显 `⚠ 过大`,继续 |
| **E-9** | 模板路径 `../` 跳出工作空间 | 屏显 `⚠ 模板路径不安全`,跳过 |
| **E-10** | `--result` / `--plan` 与 `code-auto` 协同 | `code-auto` 不传(沿用 REQ-00007 Q-4) |
| **E-11** | 多次执行(`--result` 模板相同) | 输出文件**覆盖**(幂等) |
| **E-12** | `--result` / `--plan` 同时传 | 独立处理(各占 1 行屏显) |

### 5.2 安全(NFR-6)

- **NFR-6.1**:模板路径校验(防止路径穿越 — 不允许 `../` 跳出工作空间)
- **NFR-6.2**:模板文件大小限制(1MB;过大屏显 `⚠` 但继续)
- **NFR-6.3**:`--result` / `--plan` **不**写工作空间外文件(输出路径前缀必须 `./assistants/<版本号>/...`)

### 5.3 状态机

- 沿用既有"## 工作流程"状态机(本需求**不**引入新状态)
- 模板填充是**附加步骤**,不修改 3 技能既有状态机
- 流程:主产出物 → 模板填充 → 看板同步 → 末尾兜底提交(NFR-3.4 顺序保证)

### 5.4 性能 / 资源

- 模板填充耗时 < 5 秒(可文本化格式,1MB 以内)(NFR-1)
- 屏显新增 1-2 行,**不**影响整体性能
- BUG 路径:`code-plan` BUG 模式模板填充输出目录为 `fix/<BUG-NNN>/` 而非 `plan/<REQ>/`(沿用 REQ-00019)

---

## 6. 看板同步(本需求 0 触发三同步)

### 6.1 看板影响(本需求 0 改字段)

- ✅ 本需求**0**修改 `V0.0.3/RESULT.md` 看板的字段约定(无新增/删除/重命名区段 / 列 / 枚举值)
- ✅ 本需求**0**触发 `dashboard-conventions §规则 1`(模板产出物**不**是任务,沿用 NFR-2.1)
- ✅ 本需求**0**派生"更新看板"任务(沿用 REQ-00017 强约束 + INV-6)

### 6.2 本概设完成后需追加的看板条目

- **概要设计清单**:追加 REQ-00021 1 行(状态=已完成)
- **变更记录**:追加 1 条 `YYYY-MM-DD HH:mm  设计新增  REQ-00021 概要设计完成  REQ-00021`
- **需求清单**:REQ-00021 的"概要设计"列从 `—` 改为 `[REQ-00021/RESULT.md](./design/REQ-00021/RESULT.md)`

---

## 7. 测试要点

- **AC-1.x**:3 技能 `--result` / `--plan` 参数解析
  - AC-1.1:`code-require --result` 解析 + 记录到 `analysis-notes.md`
  - AC-1.2:`code-design --result` 解析(二进制格式 `⚠ 跳过`)
  - AC-1.3:`code-plan --result --plan` 2 参数同时解析
  - AC-1.4:不传 `--result`,原行为执行
  - AC-1.5:`--result` 缺值 `⚠ 跳过`
- **AC-2.x**:模板填充
  - AC-2.1 ~ 2.8:可文本化格式(.md / .html / .docx 二进制跳过 / 无占位符 / 未识别占位符保留 / 文件不存在 / > 1MB / `../` 跳出)
- **AC-3.x**:二进制格式限制
  - AC-3.1 ~ 3.3:.docx / .xlsx / .pdf 屏显 `⚠ 跳过`
- **AC-4.x**:屏显 + 看板
  - AC-4.1:完成时 3 段屏显
  - AC-4.2:看板**不**追加新行
  - AC-4.3:`analysis-notes.md` 追加"模板填充结果"节
- **AC-5.x**:0 改其他 10 技能
  - AC-5.1 ~ 5.3:10 个其他 `code-*` SKILL.md 0 改动
- **AC-6.x**:0 改 marketplace / plugin / 规范
  - AC-6.1 ~ 6.4:marketplace / plugin / 规范 / 看板 0 改动
- **INV-1 ~ INV-9**:9 条不变量自检

---

## 8. 关联设计

### 8.1 本版本(V0.0.3)

- **REQ-00020**:架构设计目标重新归位 + 3 新维度(本需求**沿用** REQ-00020 的 7 维度设计目标写入;**不**与 REQ-00020 冲突)
- 关键点:REQ-00020 概设 §3.2 D-6 **显式提及** REQ-00021 → 本需求是"承接需求"

### 8.2 跨版本(V0.0.2)

- **REQ-00005**:首步拉取 + 末步兜底提交(本需求 `--result` / `--plan` 解析在步骤 0a 拉取**前**)
- **REQ-00007**:`code-auto` 自动开发(本需求 `code-auto` 不传 `--result` / `--plan`)
- **REQ-00011**:步骤 0b 设计目标(本需求**不**改 3 技能步骤 0b)
- **REQ-00013**:屏显"编号+标题"(本需求模板填充屏显沿用)
- **REQ-00017**:0 派生"更新看板"任务(INV-6 沿用)
- **REQ-00019**:BUG 模式同构(本需求 BUG 路径同样生效)

详 `related-designs.md`。

---

## 9. 待澄清 / 未决项

| 编号 | 内容 | 状态 |
| --- | --- | --- |
| (无) | 本需求**0**待澄清;7 项设计决策(D-1 ~ D-7)+ 9 条不变量(INV-1 ~ INV-9)全部已锁定;7 FR / 6 NFR / ~30 AC / 9 INV 全部已锁定;5 项澄清全部已落(`clarifications.md`);4 项 Q-locked(REQ-00021 需求分析阶段);1 项用户授权偏离(NFR-5.1 SKILL.md 行数变化 +20% ~ +30%) | 0 待澄清 |

---

## 10. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-06 17:50 | v1 | 初始创建 | 完成首次概要设计:7 决策(D-1 ~ D-7)+ 9 不变量(INV-1 ~ INV-9)+ 7 FR / 6 NFR / ~30 AC / 9 INV 全部锁定;整体=--extensible + 功能性=高(用户选);0 触发 `dashboard-conventions §规则 1` 三同步;0 派生"更新看板"任务;1 项用户授权偏离(NFR-5.1 行数增长 +20% ~ +30%);3 个 SKILL.md **已实际落地修改**(本概设为回填式) | wangmiao |
