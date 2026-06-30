# 需求提示词文档 — REQ-00044 · 技能系统 v2 大改版

> 上游:`./assistants/V0.0.4/require/REQ-00044/`(材料源自用户对话)
> 遵循规范:`./assistants/rules/`(若存在)

## 1. 需求概述

对现有 `code-skills` 技能系统进行 v2 大改版,将现有 14 个技能缩减为 7 个技能,合并多项能力、重组输出目录结构、新增断点续跑机制、优化版本看板记录逻辑。

(源自:用户对话输入)

## 2. 背景与目标

### 背景
- 现有 14 个技能分散在 5 段主流程(`code-require → code-design → code-plan → code-it → code-check`)中,用户需多次调用
- 产出目录结构复杂(`require/`、`design/`、`plan/`、`code/`、`review/` 等),文件碎片化(多份过程文档)
- 缺乏断点续跑机制,中断后需从头重跑
- 版本看板频繁读写,性能开销大

### 目标
1. 技能合并:14 → 7,降低调用复杂度
2. 目录重组:`req/` + `fix/` 两大目录,统一文档命名
3. 断点续跑:通过 `PROCESS.md` 实现中断恢复
4. 看板简化:仅在创建时追加记录,避免频繁读写
5. 新增 `--auto` 静默模式、`--require`/`--design`/`--summary`/`--template` 导出功能

## 3. 用户角色与场景

- **新项目初始化者**:调 `code-ver` 初始化工程 + 创建首个版本
- **需求开发者**:调 `code-req` 完成从需求分析到代码评审的全流程
- **缺陷修复者**:调 `code-fix` 完成从缺陷登记到修复评审的全流程
- **知识查询者**:调 `code-faq` 查询历史需求/设计,导出文档
- **规范维护者**:调 `code-rule` 维护项目级编码规范
- **分支合并者**:调 `code-merge` 合并 worktree 改动
- **进度查看者**:调 `code-dashboard` 查看版本进度

## 4. 功能需求(FR)

### FR-1: code-ver 技能(版本管理 + 发布 + 初始化)

**合并来源**:`code-version` + `code-publish` + `code-init`

**核心能力**:

| 场景 | 行为 |
| --- | --- |
| 新项目,无 `assistants/` 目录 | 执行 `code-init` 逻辑:扫描现有代码,登记为基线需求,生成 INIT-REPORT.md,创建基线版本 |
| 已初始化,切换版本 | 执行 `code-version` 逻辑:切换 `.current-version` 到目标版本 |
| 当前版本未发布,切换前 | 询问用户是否先执行 `code-publish` 发布当前版本,再切换到目标版本 |

**输入**:版本号(必填,如 `V0.0.5`)或空(初始化)

**输出**:`./assistants/.current-version` 更新,版本工作空间就绪

(源自:用户需求描述 §1)

### FR-2: code-req 技能(需求开发全流程)

**合并来源**:`code-require` + `code-design` + `code-plan` + `code-it` + `code-check`(需求路径)

**核心流程**:需求分析 → 软件设计 → 任务排期 → 编码执行 → 代码审查,串行执行

**交互模式**:
- **默认(交互模式)**:每步完成后与用户确认,再进入下一步
- **`--auto` 模式**:所有 `AskUserQuestion` 自动选推荐项,静默执行

**输入**:需求描述(自然语言)或需求编号(REQ-NNNNN)

**输出目录结构**(新):
```
assistants/<版本号>/req/<REQ-NNNNN>/
├── REQUIRE.md          # 需求分析结果
├── DESIGN.md           # 软件设计(不区分概要/详细)
├── PLAN.md             # 任务排期计划
├── TASK-<序号>.md      # 任务完成结果(每任务 1 份)
├── CHECK.md            # 代码审查结果
├── LOG.md              # 过程记录(非必要不记录)
└── PROCESS.md          # 执行进程(追加式,用于断点续跑)
```

**断点续跑**:`PROCESS.md` 记录当前步骤,中断后重跑从断点继续

(源自:用户需求描述 §2, §4)

### FR-3: code-fix 技能(缺陷修复全流程)

**合并来源**:`code-fix` + `code-plan` + `code-it` + `code-check`(缺陷路径)

**核心流程**:缺陷登记 → 根因分析 → 修复设计 → 任务排期 → 编码执行 → 代码审查,串行执行

**交互模式**:同 `code-req`,默认交互确认,`--auto` 静默

**输入**:缺陷描述(自然语言)或缺陷编号(BUG-NNNNN)

**输出目录结构**(新):
```
assistants/<版本号>/fix/<BUG-NNNNN>/
├── BUG.md              # 缺陷分析(触发条件+可能成因)
├── DESIGN.md           # 软件设计
├── PLAN.md             # 任务排期计划
├── TASK-<序号>.md      # 任务完成结果
├── CHECK.md            # 代码审查结果
├── LOG.md              # 过程记录(非必要不记录)
└── PROCESS.md          # 执行进程(追加式,用于断点续跑)
```

**与 code-req 的差异**:仅 `BUG.md`(缺陷分析)与 `REQUIRE.md`(需求分析)不同,其余文档逻辑一致

(源自:用户需求描述 §3, §4)

### FR-4: code-faq 技能(知识查询 + 文档导出)

**合并来源**:`code-answer`

**核心能力**:
- 跨版本查询需求/缺陷/功能定义
- `--require` + 文件路径:导出需求文档
- `--design` + 文件路径:导出详细设计文档
- `--summary`(与 `--design` 配合):导出概要设计(从 DESIGN.md 提取概要信息)
- `--template` + 文件路径:指定导出模板

**参考文件**:最新输出结构(`REQUIRE.md` / `DESIGN.md` / `PLAN.md` / `TASK-*.md` / `CHECK.md`)

(源自:用户需求描述 §5)

### FR-5: 目录结构重组

**现有目录** → **新目录**:

| 现有 | 新 | 说明 |
| --- | --- | --- |
| `require/<REQ>/RESULT.md` | `req/<REQ>/REQUIRE.md` | 需求分析 |
| `design/<REQ>/RESULT.md` | `req/<REQ>/DESIGN.md` | 软件设计 |
| `plan/<REQ>/RESULT.md` + `PLAN.md` | `req/<REQ>/DESIGN.md` + `PLAN.md` | 设计+排期 |
| `code/<TASK>/RESULT.md` | `req/<REQ>/TASK-<序号>.md` | 任务结果 |
| `review/<REQ>/REVIEW-REPORT.md` | `req/<REQ>/CHECK.md` | 代码审查 |
| `fix/<BUG>/RESULT.md` | `fix/<BUG>/BUG.md` | 缺陷分析 |
| 多份过程文档 | `LOG.md` | 统一过程记录 |

**不变**:`assistants/`、`assistants/<版本号>/`、`assistants/.current-version` 功能不变

(源自:用户需求描述 §4)

### FR-6: PROCESS.md 断点续跑

- 每个需求/缺陷目录包含 `PROCESS.md`
- **追加式记录**:每次进入新步骤时追加一行,记录当前步骤名 + 时间戳
- **不预读**:记录前不单独读取文件内容,直接追加
- **恢复逻辑**:`code-req`/`code-fix` 启动时读取 `PROCESS.md` 最后一行,确定当前步骤,从中断处继续

**PROCESS.md 格式**:
```
2026-06-29 14:00 | REQUIRE | 需求分析开始
2026-06-29 14:15 | REQUIRE | 需求分析完成
2026-06-29 14:20 | DESIGN | 软件设计开始
2026-06-29 14:35 | DESIGN | 软件设计完成
2026-06-29 14:40 | PLAN | 任务排期开始
...
```

(源自:用户需求描述 §4)

### FR-7: 版本看板简化

**现有行为**:各技能频繁读写 `RESULT.md` 的多个区段(需求清单/任务清单/缺陷清单/变更记录等)

**新行为**:
- 仅在需求/缺陷**创建时**追加一行记录,包含:
  - 需求/缺陷编号
  - 标题
  - `PROCESS.md` 的引用路径
- 各技能不再频繁更新看板中的状态/统计数据
- 状态查询改为读取 `PROCESS.md` 最后一行的步骤名

**`RESULT.md` 简化格式**:
```
## 需求清单
| 需求编码 | 标题 | 进度文档 |
| --- | --- | --- |
| REQ-00001 | 用户登录 | [PROCESS.md](req/REQ-00001/PROCESS.md) |

## 缺陷清单
| 缺陷编号 | 标题 | 进度文档 |
| --- | --- | --- |
| BUG-00001 | 空指针崩溃 | [PROCESS.md](fix/BUG-00001/PROCESS.md) |
```

(源自:用户需求描述 §6)

### FR-8: 保留技能适配

以下 3 个技能保留基本功能,但参考文件更新为最新结构:

| 技能 | 适配内容 |
| --- | --- |
| `code-rule` | 继续维护 `assistants/rules/`,读取新结构下的文件 |
| `code-merge` | 读取 `req/`/`fix/` 下的 `PROCESS.md` 和文档 |
| `code-dashboard` | 读取 `RESULT.md`(简化版) + `PROCESS.md` 展示进度 |

(源自:用户需求描述 §7)

## 5. 非功能需求 / 约束(NFR)

### NFR-1: 向后兼容
- 现有 `assistants/` 下历史数据保留,不强制迁移
- 新版本使用新目录结构,旧版本目录保持不变

### NFR-2: 技能文件精简
- 每个 SKILL.md 保持简洁,复杂逻辑下沉到 `references/`
- 与 `code-req`/`code-fix` 共享的逻辑抽取到公共 `references/`

### NFR-3: 不修改 rules/ 目录
- `assistants/rules/` 继续跨版本共享,由 `code-rule` 维护

### NFR-4: 插件市场兼容
- `.claude-plugin/plugin.json` 和 `marketplace.json` 更新,列出 7 个新技能

## 6. 页面与界面

不涉及 UI 变更。

## 7. 交互逻辑

### code-req 交互流程
```
用户: /code-req "添加用户登录"
AI: [需求分析] 我已理解需求,共提取 5 条 FR,是否继续?
    → 用户确认
AI: [软件设计] 设计完成,涉及 3 个模块,是否继续?
    → 用户确认
AI: [任务排期] 拆分为 3 个任务,是否继续?
    → 用户确认
AI: [编码] TASK-001 完成 ✓, TASK-002 完成 ✓, TASK-003 完成 ✓
AI: [审查] 评审通过,0 条发现
AI: ✓ code-req 完成
```

### code-req --auto 交互流程
```
用户: /code-req "添加用户登录" --auto
AI: [需求分析] 完成(5 FR) → [软件设计] 完成(3 模块) → [任务排期] 完成(3 任务) → [编码] 完成(3/3) → [审查] 通过(0 发现)
AI: ✓ code-req --auto 完成
```

### code-ver 切换版本流程
```
用户: /code-ver V0.0.5
AI: 当前版本 V0.0.4 尚未发布,是否先发布再切换?
    → A. 发布后切换(推荐)
    → B. 直接切换(不发布)
    → C. 取消
```

## 8. 数据与状态

### 技能映射表

| 新技能 | 合并的旧技能 | 新增能力 |
| --- | --- | --- |
| `code-ver` | code-version + code-publish + code-init | 自动判断初始化/切换/发布场景 |
| `code-req` | code-require + code-design + code-plan + code-it + code-check(需求路径) | 交互确认模式 + `--auto` 静默模式 + 断点续跑 |
| `code-fix` | code-fix + code-plan + code-it + code-check(缺陷路径) | 交互确认模式 + `--auto` 静默模式 + 断点续跑 |
| `code-faq` | code-answer | `--require`/`--design`/`--summary`/`--template` 导出 |
| `code-rule` | code-rule(保留) | 适配新文件结构 |
| `code-merge` | code-merge(保留) | 适配新文件结构 |
| `code-dashboard` | code-dashboard(保留) | 读取简化版看板 + PROCESS.md |

### 废弃技能

`code-require`、`code-design`、`code-plan`、`code-it`、`code-check`、`code-auto`、`code-version`、`code-publish`、`code-init`、`code-answer` 共 10 个技能被合并或废弃。

### 新目录结构总览

```
assistants/
├── rules/                    # 跨版本规范(code-rule 维护)
├── .current-version          # 当前激活版本
└── <版本号>/
    ├── RESULT.md             # 简化版看板
    ├── req/                  # 需求管理
    │   └── <REQ-NNNNN>/
    │       ├── REQUIRE.md    # 需求分析
    │       ├── DESIGN.md     # 软件设计
    │       ├── PLAN.md       # 任务排期
    │       ├── TASK-<序号>.md # 任务结果
    │       ├── CHECK.md      # 代码审查
    │       ├── LOG.md        # 过程记录(可选)
    │       └── PROCESS.md    # 执行进程
    └── fix/                  # 缺陷管理
        └── <BUG-NNNNN>/
            ├── BUG.md        # 缺陷分析
            ├── DESIGN.md     # 软件设计
            ├── PLAN.md       # 任务排期
            ├── TASK-<序号>.md # 任务结果
            ├── CHECK.md      # 代码审查
            ├── LOG.md        # 过程记录(可选)
            └── PROCESS.md    # 执行进程
```

## 9. 边界与异常

- **E-1: 历史数据兼容**:旧版本目录(`require/`/`design/`/`plan/`/`code/`/`review/`/`fix/`)不迁移,新技能仅操作新目录结构
- **E-2: PROCESS.md 缺失**:`code-req`/`code-fix` 启动时未找到 `PROCESS.md` → 视为新需求/缺陷,从头开始
- **E-3: --auto 与 SIGINT**:`--auto` 模式下 Ctrl+C 中断,`PROCESS.md` 已记录当前步骤,下次可续跑
- **E-4: code-faq 导出模板不存在**:屏显警告,跳过模板填充,输出无模板格式
- **E-5: code-ver 无 assistants/ 目录**:自动判断为新项目,执行 code-init 逻辑
- **E-6: 旧格式 RESULT.md 被 code-dashboard 读取**:降级处理,展示"旧格式,建议升级"

## 10. 验收标准(AC)

### AC-1: 技能数量
- `plugins/code-skills/skills/` 下仅有 7 个技能目录

### AC-2: code-ver 三合一
- 新项目执行 `code-ver` → 完成初始化 + 创建版本
- 已初始化项目执行 `code-ver V0.0.5` → 切换到 V0.0.5
- 当前版本未发布时切换 → 询问是否先发布

### AC-3: code-req 全流程
- 默认模式下每步确认后继续
- `--auto` 模式下静默完成全流程
- `PROCESS.md` 记录每步进度

### AC-4: code-fix 全流程
- 默认模式下每步确认后继续
- `--auto` 模式下静默完成全流程
- 产出 `BUG.md`(非 `REQUIRE.md`)

### AC-5: 目录结构
- 新需求产出在 `req/<REQ-NNNNN>/` 下
- 新缺陷产出在 `fix/<BUG-NNNNN>/` 下
- 文档命名符合新规范

### AC-6: PROCESS.md 断点续跑
- `code-req` 中断后重跑,从 `PROCESS.md` 记录的步骤继续
- `code-fix` 中断后重跑,从 `PROCESS.md` 记录的步骤继续

### AC-7: code-faq 导出
- `--require` 导出需求文档
- `--design` 导出详细设计
- `--summary` 导出概要设计(从 DESIGN.md 提取)
- `--template` 指定模板

### AC-8: 看板简化
- `RESULT.md` 仅在需求/缺陷创建时追加一行
- 状态查询通过 `PROCESS.md` 完成

### AC-9: 保留技能
- `code-rule`、`code-merge`、`code-dashboard` 正常可用
- 读取的文件路径更新为最新结构

## 11. 关联需求

| 关联需求 | 版本 | 关联点 |
| --- | --- | --- |
| REQ-00041 | V0.0.4 | 技能多语言模块化重构,新技能继承 references/ 架构 |
| REQ-00042 | V0.0.4 | 代码产出中禁止包含追踪编号,新技能继承此约束 |
| REQ-00043 | V0.0.4 | 移除 fix-plan.md 废弃引用,新技能不再引用 |

## 12. 待澄清 / 未决项

1. **旧技能目录处理**:旧技能 SKILL.md 是删除还是保留为历史?
2. **旧版本数据迁移**:V0.0.0~V0.0.4 的历史数据是否需要迁移到新结构?
3. **code-auto 废弃**:`code-auto` 被 `code-req --auto` 和 `code-fix --auto` 取代,是否完全删除?
4. **编码规范规则**:`assistants/rules/` 下的规范文件是否需要更新以匹配新结构?

## 13. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-29 00:00 | v1 | 初始创建 | 需求分析完成,共 8 条 FR / 4 条 NFR / 9 条 AC | wangmiao |