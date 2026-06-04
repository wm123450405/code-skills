# 工作目录布局参考 — code-publish

> `code-publish` 技能工作目录约定。**本技能在 `code-version` 定义的版本工作空间层之上工作**,
> 负责"开发完成 → 部署上线"环节的 3 份手册(DEPLOY.md / UPDATE.md / Q&A.md)产出到 `publish/`。
>
> 完整的"工作空间层"定义见 `code-version` 技能;**本文件只描述 `code-publish` 特有的扩展**(`publish/` + `qanda/` 两个路径)。

## 整体布局

```
<项目根目录>/
├── assistants/
│   ├── rules/                          ← 项目级规范(跨版本共享,只读)
│   │   ├── architecture.md
│   │   ├── module-conventions.md
│   │   ├── api-standards.md
│   │   └── ...
│   ├── .current-version                ★ 当前激活版本标记文件
│   │                                    (由 code-version 写入;code-publish 只读)
│   │
│   ├── qanda/                          ★ 项目级 Q&A 长期沉淀(跨版本共享)
│   │   │                                (本技能顺带创建,见 AC-6.1~6.3)
│   │   ├── README.md                    ← 目录用途说明(本技能首次调用时创建)
│   │   └── <主题>.md                   ← 用户后续添加的 Q&A 文件
│   │                                    (例:deploy-faq.md / db-init-faq.md)
│   │
│   ├── v1.0.0/                         ← 版本工作空间 1(由 code-version 创建)
│   │   ├── RESULT.md                   ★ 版本开发进度看板
│   │   │                                (本技能只读消费 3 区段,见 SKILL.md "## 看板字段约定")
│   │   ├── require/                    ← code-require 产出
│   │   ├── design/                     ← code-design 产出
│   │   ├── plan/                       ← code-plan 产出
│   │   ├── code/                       ← code-it 产出
│   │   ├── test/                       ← code-unit 产出
│   │   ├── review/                     ← code-review 产出
│   │   │
│   │   └── publish/                    ★ 本技能产出(可写,见 FR-2)
│   │       ├── DEPLOY.md                ← 全新部署手册骨架(始终生成)
│   │       ├── UPDATE.md                ← 升级部署手册骨架(基线版本跳过)
│   │       └── Q&A.md                   ← Q&A 手册(从 qanda/ 聚合)
│   │
│   ├── v1.1.0/                         ← 版本工作空间 2(并行或后续)
│   │   ├── RESULT.md
│   │   ├── ...
│   │   └── publish/
│   │       └── ...
│   │
│   └── <其他历史/并行版本>/
│       └── ...
│
├── src/                                # 用户的项目源码(由 code-it 修改)
├── tests/                              # 用户的测试代码(由 code-unit 修改)
└── ...
```

## code-publish 的特定扩展

### 1. `qanda/` — 项目级 Q&A 长期沉淀(新增)

```
assistants/qanda/
├── README.md                            # 目录说明(由本技能首次创建,内容来自 templates/qanda-README.md)
└── <主题>.md                           # 用户添加的 Q&A 文件
```

**职责**:
- **本技能首次调用时**若 `qanda/` 不存在 → `mkdir -p` + 写入 `README.md`(模板来自 `templates/qanda-README.md`)
- 之后每次调本技能 → 检查 `qanda/` 是否存在(已存在则跳过 README 创建)
- 读 `qanda/*.md`(排除 `README.md`)聚合到 `<版本号>/publish/Q&A.md`

**对其他技能**:此目录是项目级共享,跨所有版本;**其他 `code-*` 技能**不读不写本目录。

**维护方式**:**暂时人工整理**(Q-2 锁定 A);未来 v2 可能由独立技能管理。

### 2. `<版本号>/publish/` — 本技能产出(新增)

```
<版本号>/publish/
├── DEPLOY.md                            # 全新部署手册骨架(始终生成)
├── UPDATE.md                            # 升级部署手册骨架(基线版本跳过)
└── Q&A.md                               # Q&A 手册(从 qanda/ 聚合)
```

**职责**:
- 每次调本技能 + 前置检查通过时,生成 2 或 3 份手册到 `publish/`:
  - **DEPLOY.md** —— 全新部署场景的步骤手册
  - **UPDATE.md** —— 仅当本版本非基线时生成(基线跳过)
  - **Q&A.md** —— 始终生成;内容来自 `qanda/*.md` 聚合
- 模板来自 `templates/DEPLOY.md` / `UPDATE.md` / `Q&A.md`
- 写入前 `ls` 检测已有文件 → 在报告中提示"已覆盖 N 个文件"
- 覆盖是允许的(NFR-6 幂等);用户应 git diff 审阅后再手动 commit(NFR-3)

**对其他技能**:此目录**仅**本技能写;其他 `code-*` 技能不读不写(本版本产物)。

**生命周期**:与版本同步(本版本发版后,publish/ 内的手册可独立提交 / 修改 / 重新生成)。

### 3. `<版本号>/RESULT.md` — 本技能只读消费

**职责**:
- 读 `需求清单` / `任务清单` / `缺陷清单` 3 区段(NFR-2 纯只读)
- 解析为 PreflightChecker 的输入
- **不**修改 `RESULT.md` 任何区段(不触发 `dashboard-conventions.md §规则 1`)

**看板区段**与本技能的责任划分:
- 本技能**不**追加"概要设计清单" / "任务清单" / "变更记录"等区段
- 本技能**不**触发看板块的任何修改
- 版本看板"任务清单"中本技能的 8 条任务(T-001~T-008)由 `code-it` 在每条任务执行时更新

### 4. `.current-version` — 本技能只读消费

**职责**:
- 缺省位置参数时,读取此文件获取当前激活版本号
- 校验版本号格式(不允许含 `/` `\` `..`)
- **不**修改此文件(由 `code-version` 维护)

## 关键点

### 1. 5 类资源与 4 类读/写角色

| 资源 | 路径模式 | 本技能的读/写角色 | 谁负责写 |
| --- | --- | --- | --- |
| 项目级规范 | `./assistants/rules/<file>.md` | **只读** | `code-rule` |
| 激活版本标记 | `./assistants/.current-version` | **只读**(缺省参数时) | `code-version` |
| Q&A 沉淀 | `./assistants/qanda/<file>.md` | **读 + 顺带写**(`README.md` 首次创建) | 本技能 + 用户 |
| 版本看板 | `./assistants/<版本号>/RESULT.md` | **只读** | `code-version` + 各种 `code-*` |
| 版本产物 | `./assistants/<版本号>/publish/<file>.md` | **写** | 本技能 |

### 2. 模板的双向引用

- **本技能**(`SKILL.md` + 5 模板)有**两处**描述同一组目录:
  - `SKILL.md` 的"## 工作目录约定"小节(简版,~40 行)
  - `assistants-layout.md` 的"## 整体布局"小节(详版,本文)
- 两文档**内容一致**但**用途不同**:
  - `SKILL.md` 是技能入口;目录树是"## 工作目录约定"小节
  - `assistants-layout.md` 是标准技能资产;目录树是"## 整体布局"独立小节
- **变更时需同步**:改一处 → 改另一处(本任务执行时**已对齐**)

### 3. 本技能"可写目录"边界

| 目录 | 写场景 | 写内容 | 频率 |
| --- | --- | --- | --- |
| `qanda/README.md` | 首次创建 `qanda/` 时 | 模板 `qanda-README.md` | 一次 |
| `<版本号>/publish/DEPLOY.md` | 每次发布前置检查通过 | 模板 `DEPLOY.md` + `<本版本号>` 替换 | 每次发布 |
| `<版本号>/publish/UPDATE.md` | 每次发布前置检查通过 + 非基线 | 模板 `UPDATE.md` + `<本版本号>` + `<源版本>` 替换 | 每次非基线发布 |
| `<版本号>/publish/Q&A.md` | 每次发布前置检查通过 | 占位模板 + 聚合 `qanda/*.md` | 每次发布 |

## 多版本隔离

- 不同版本的 `assistants/<version>/` 完全独立,互不污染
- `publish/` 是**版本内**目录(不跨版本共享)
- 切换版本 = 改 `.current-version`,不影响历史版本的 `publish/`
- 删除/归档版本 = 删除/移动 `<version>/` 目录;`publish/` 随之删除(本技能不提供)

## 跨技能协作:本技能的"只读"角色

`code-publish` 是**纯只读**技能:
- 读:`.current-version` / `<版本号>/RESULT.md` 3 区段 / `qanda/*.md` / 5 份模板
- 写:`qanda/README.md`(首次)+ `<版本号>/publish/3 份手册`
- 写`:不修改` `RESULT.md` / `rules/` / 其他 10 个 `code-*` 技能 / `marketplace.json` / `plugin.json` / `CLAUDE.md` / `commit-conventions.md`

其他技能的看板同步(本技能**不**参与):
- `code-require` → 需求清单 + 变更记录
- `code-design` → 概要设计清单 + 变更记录
- `code-plan` → 详细设计与任务计划汇总 + 任务清单(首次登记) + 变更记录
- `code-it` → 任务清单(开发状态) + 缺陷清单 + 变更记录
- `code-unit` → 任务清单(测试状态) + 缺陷清单 + 变更记录
- `code-review` → 评审发现汇总 + 派生任务记录 + 缺陷清单 + 变更记录
- `code-fix` → 缺陷清单 + 变更记录

## 多项目隔离

不同项目的 `assistants/` 完全独立。
