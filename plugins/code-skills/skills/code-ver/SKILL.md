---
name: code-ver
description: 版本管理。创建和切换开发版本,发布项目新版本。
---

# code-ver — 版本管理

## 目标
提供版本工作空间的**全生命周期管理**:
- **新项目**:扫描现有代码,登记基线,建立版本工作空间
- **版本切换**:在多个版本之间切换,可选先发布当前版本
- **发布检查**:检查版本是否可发布,生成部署手册

## 适用场景
- 新项目首次接入 `code-skills` 体系
- 启动一个全新版本(如产品发版、独立功能包、季度迭代)
- 在多个并行版本之间切换
- 开发周期末,准备发布到生产环境
- 任何 `code-req` / `code-fix` 调用前,先确认/切换当前工作空间

## 不适用
- 已有激活版本且用户想继续在该版本工作(直接调用其他 `code-*` 技能即可)
- 项目级规范相关操作(规范在 `./assistants/rules/`,调用 `code-rule`)

## 工作目录约定(强制)

```
./assistants/
├── rules/                  # 项目级规范(跨版本共享,本技能只读)
├── .current-version        # 当前激活版本标记文件(本技能写)
└── <版本号>/               # 版本工作空间
    ├── RESULT.md           # 版本开发进度看板(简化版)
    └── req/<需求编号>/     # 需求工作目录(code-req 产出)
```

- 路径以**当前工作目录(CWD)**为基准
- `rules/` **不**在版本下,跨版本共享
- `.current-version` 是纯文本标记,内容只有版本号字符串
- 本技能**不**修改 `./assistants/rules/` 下的任何内容(只读)
- 本技能**不**修改 `<本仓库>` 中除了 `./assistants` 目录中的其他代码文件

## 输入
- **版本号**(可选):格式不强求,推荐 `vMAJOR.MINOR.PATCH`(如 `v1.0.0`)
  - 缺省时:进入场景检测,根据 `assistants/` 是否存在决定初始化/切换
  - 不允许包含路径分隔符(`/`、`\`)
- **--publish**(可选):仅执行发布检查,不切换版本

## 输出
主产出物:
- 切换:`./assistants/.current-version` 被覆写为新版本号
- 新建:`./assistants/<版本号>/` 目录 + `./assistants/<版本号>/RESULT.md` 看板
- 初始化:`./assistants/<版本号>/INIT-REPORT.md` + `require/EXISTING-NNN/` 基线需求
- 发布:`./assistants/<版本号>/publish/DEPLOY.md` + `UPDATE.md` + `FAQ.md`

## 工具使用约定
- 读目录:`Glob` / `Bash: ls`
- 读标记文件:`Read "./assistants/.current-version"`
- 读规范:`Glob "./assistants/rules/**/*"` + `Read`(发布检查时读取编码规范)
- 写标记文件:`Write "./assistants/.current-version"`
- 建目录:`Bash: mkdir -p`
- 写文档:`Write`(首次)/ `Edit`(增量)
- 与用户澄清:优先 `AskUserQuestion`;自然语言兜底

---

## 工作流程

### 步骤 0 — 场景检测(强制前置)

> 详见 references/common.md §1

1. 检测 `assistants/` 目录是否存在
2. 检测 `.current-version` 是否存在
3. 解析用户输入(版本号 / --publish)
4. 判定场景:
   - `assistants/` 不存在 → **新项目初始化**(步骤 1A-8A)
   - `assistants/` 存在 + 无 `.current-version` → **补初始化**(步骤 1A-8A)
   - 用户传 `--publish` → **发布检查**(步骤 1C-5C)
   - 用户传版本号 → **版本切换**(步骤 1B-6B)
   - 无参数 → 列出已有版本,让用户选择(切换/初始化/发布)

### 步骤 1A — 收集初始版本号

> 详见 references/common.md §2.1

- 默认:`V0.0.0`
- 校验:非空,不含 `/` `\` `:` `*` `?` `"` `<` `>` `|`
- 不与已有版本重名

### 步骤 2A — 创建 assistants/ 骨架

> 详见 references/common.md §2.2

- 创建 `assistants/`、`assistants/rules/`、`assistants/<版本号>/` 目录
- 不覆盖已存在文件

### 步骤 3A — 写入 .current-version

> 详见 references/common.md §2.3

- `Write "./assistants/.current-version"`,内容 = `<版本号>\n`

### 步骤 4A — 写入版本看板 RESULT.md

> 详见 references/common.md §2.4

- 基于简化版 RESULT.md 模板(仅需求清单 + 缺陷清单)
- 填写版本信息、里程碑、变更记录

### 步骤 5A — 分析现有代码

> 详见 references/common.md §2.5

- 识别项目类型、目录结构、入口与主流程
- 识别已有模块、数据模型、第三方依赖
- 识别编码与构建约定

### 步骤 6A — 生成 INIT-REPORT.md

> 详见 references/common.md §2.6

- 项目概述、技术栈、目录结构、核心模块、入口与主流程
- 外部接口、数据模型、构建与运行、测试情况
- 可复用资产、已知问题/技术债

### 步骤 7A — 生成现有功能需求清单

> 详见 references/common.md §2.7

- 按功能拆分(M 个 `EXISTING-NNN`)
- 编号:`EXISTING-NNN`,从 `EXISTING-001` 开始
- 每份 `RESULT.md` 描述功能的现有实现

### 步骤 8A — 引导用户补齐编码规范

> 详见 references/common.md §2.8

- 检查 `rules/` 是否为空
- 若空,建议调 `code-rule`

---

### 步骤 1B — 版本切换:读当前版本

> 详见 references/common.md §3.1

1. `Read "./assistants/.current-version"` → 当前激活版本
2. 校验目标版本号合法性
3. 四种情形:
   - **A. 目标版本不存在 + 当前也无激活版本** → 首次创建
   - **B. 目标版本不存在 + 当前已有激活版本** → 创建新版本
   - **C. 目标版本已存在 + 与当前激活版本不同** → 切换
   - **D. 目标版本已存在 + 与当前激活版本相同** → 同版本再确认

### 步骤 2B — 检查是否需要发布

> 详见 references/common.md §3.2

- 若当前版本有活跃内容(需求清单非空 / 任务清单非空)
- 询问用户:是否先发布当前版本?
  - A. 先发布当前版本,再切换
  - B. 直接切换(不发布)
  - C. 取消

### 步骤 3B — 执行发布(若用户选择)

> 详见 references/common.md §4

- 走发布检查流程(步骤 1C-5C)
- 若发布不通过,询问是否仍要切换

### 步骤 4B — 创建/切换到目标版本

> 详见 references/common.md §3.3

- 情形 A/B:创建新版本工作空间,写入 .current-version
- 情形 C:只更新 .current-version
- 情形 D:不做任何文件操作

### 步骤 5B — CWD 描述文件版本号同步

> 详见 references/common.md §5

### 步骤 6B — 验证与汇报

> 详见 references/common.md §3.4

---

### 步骤 1C — 发布前置检查

> 详见 references/common.md §4.1

- 解析 RESULT.md 的需求清单 / 任务清单 / 缺陷清单
- 判定:需求=已完成, 任务=可发布, 缺陷=已修复
- 通过 → 进入步骤 2C
- 不通过 → 输出未完成项明细,退出

### 步骤 2C — 基线识别

> 详见 references/common.md §4.2

- 列出所有版本,字典序排序
- 本版本 = 最小 → 基线(跳过 UPDATE.md)

### 步骤 3C — 生成部署手册

> 详见 references/common.md §4.3

- 始终生成:DEPLOY.md
- 非基线:UPDATE.md
- 始终生成:FAQ.md(聚合 `faq/` 目录)

### 步骤 4C — 创建 faq/ 骨架

> 详见 references/common.md §4.4

- 若 `assistants/faq/` 不存在 → 创建 + README.md

### 步骤 5C — 报告

> 详见 references/common.md §4.5

---

## 衔接
- **下游**:`code-req`(需求开发)、`code-fix`(缺陷修复)、`code-rule`(编码规范)
- **上游**:无,通常由用户直接发起
- **横向**:`./assistants/rules/` 跨所有版本共享

## 不要做的事
- 不要在 `./assistants/rules/` 下创建版本子目录
- 不要在版本号中使用 `/` `\` 空格
- 不要在用户没确认的情况下覆盖现有 `RESULT.md`
- 不要在切版本时删除其他版本的目录
- 不要修改项目源代码(初始化时只读分析)
- 不要把分析结果写进 CWD 根目录
- 不要给"现有功能"捏造未实现的细节
- 不要在发布检查通过前生成部署手册