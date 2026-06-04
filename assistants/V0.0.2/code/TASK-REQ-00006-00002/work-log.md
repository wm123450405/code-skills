# 开发日志 — TASK-REQ-00006-00002

开始时间:2026-06-04 17:32
版本:V0.0.2
任务标题:`[新增] 写 templates/DEPLOY.md 模板(8 章节 + placeholder + 默认示例)`
触发/来源:需求新增

## 项目现状(步骤 6 记录)

- **项目类型**:Claude Code Marketplace 插件(`code-skills`),纯文档型
- **语言**:Markdown + JSON
- **构建命令**:**无**(纯文档)
- **既有模板**(参考):10 个 `code-*` 技能中,**有 5 个**带 `templates/` 子目录,模板内容均用 `<placeholder>` 风格 + 完整章节结构 + 默认示例:
  - `code-version/templates/version-RESULT.md`(看板模板,顶层结构)
  - `code-version/templates/assistants-layout.md`(工作目录约定)
  - `code-design/templates/design.md`(概要设计模板,14 章节)
  - `code-fix/templates/bug.md`(缺陷详情模板)
  - `code-fix/templates/fix-registry.md`(缺陷总览)
- **既有模板的"实现风格"**:
  - **kebab-case** 命名(如 `version-RESULT.md` `design.md`)
  - **`<placeholder>` 包裹**待补全字段
  - 完整章节结构(每章节独立可执行)
  - 每个需要用户决策的节点提供**默认示例**(占位但可执行)
  - 文首有"使用说明"或"提示"段
- **DEPLOY.md 模板的特殊性**:**运行时由 `code-publish` 复制 + 替换 `<本版本号>`**(详 SKILL.md 步骤 2.3)

## 项目级规范要点(步骤 4 记录)

- `./assistants/rules/module-conventions.md` §规则 1:**强约束**(本任务强约束)
  - 模板文件**必须**在 `plugins/code-skills/skills/<技能名>/templates/` 子目录
  - kebab-case 命名 `<用途>.md`
  - 本任务的路径 = `plugins/code-skills/skills/code-publish/templates/DEPLOY.md` ✓
- 其他 12 个规范文件:占位或不相关,**不影响本任务**

## 任务设计要点(步骤 5 记录)

### PLAN.md §3 任务详情(T-002 摘要)

- **类型**:新增
- **触发/来源**:需求新增
- **目标**:创建通用全新部署手册骨架模板(8 章节 + placeholder + 默认示例)
- **涉及文件**:新建 `plugins/code-skills/skills/code-publish/templates/DEPLOY.md`
- **前置任务**:无(独立任务)
- **关键变更**:
  - 8 大章节结构:概述 / 打包(3 子节) / 获取成果物 / 上传服务器 / 初始化系统(4 子节) / 启动运行 / 首次进入软件系统 / 验证清单
  - 文首"使用说明"段:警示 `⚠ 本手册为通用发布部署骨架,请手动补全所有 <placeholder> 后再按步骤执行`(AC-3.3)
  - 每节至少 1 个"最常见部署方式"默认示例(AC-3.2)
  - placeholder 集合:自动填充 `<本版本号>`(由 `code-publish` 替换);用户补全 `<打包方式>` / `<output>` / `<source_dir>` / `<image_name>` / `<version>` / `<环境依赖>` / `<DB 脚本路径>` / `<初始化数据脚本>` / `<配置文件路径>` / `<key>` / `<value>` / `<启动命令>` / `<首次访问 URL>` / `<默认账号>` 等(AC-3.1)
- **依据规范**:`module-conventions.md §规则 1`

### 详细设计 §4 模块 8(本任务的主依据)

- **职责**:全新部署手册骨架模板
- **路径**:`plugins/code-skills/skills/code-publish/templates/DEPLOY.md`
- **内容结构**:见 needs §6.1 节选(8 章节)
- **关键字段**:详 `data-changes.md §4.1`
- **依据规范**:无

### 详细设计 §6.5 写侧数据格式

详 `data-changes.md §4.1`:
- 8 章节顺序固定
- placeholder 集合固定
- 依赖 placeholder 替换方式(由 `code-publish` 在运行时执行,见 `interface-specs.md §1`)

## 开发过程

### 2026-06-04 17:32
- **操作**:验证 PLAN.md + 准备目录 + 推进状态
- **结果**:成功(T-002 存在,触发/来源=需求新增,无前置任务)
- **状态推进**:PLAN.md 中 T-002 "待开始" → "进行中"

### 2026-06-04 17:33
- **操作**:读取详细设计 §4 模块 8 + §6.5 + needs §6.1
- **结果**:成功(8 章节结构与 placeholder 集合全部明确)

### 2026-06-04 17:34
- **操作**:写 `plugins/code-skills/skills/code-publish/templates/DEPLOY.md`
- **结果**:成功
- **文件大小**:待写完后核实(预计 ~150 行)
- **关键自检**:
  - 8 大章节齐全 ✓(按 data-changes.md §4.1 顺序)
  - placeholder 风格一致 ✓(全部用 `<placeholder>` 包裹)
  - 默认示例齐全 ✓(每章节至少 1 个可执行示例,AC-3.2)
  - 文首"使用说明"段 ✓(AC-3.3)
  - `<本版本号>` 仅出现在 H1 与第 1 节(供 `code-publish` 自动替换,detail design DD-4)

### 关键决策与权衡

#### 决策 IT-1:H1 标题格式
- **选定**:`# 发布部署手册 — <本版本号>`
- **理由**:`code-publish` 替换 `<本版本号>` 后变成 `# 发布部署手册 — V0.0.2`,用户即时可见
- **依据**:data-changes.md §4.1 章节 1 概述

#### 决策 IT-2:第 2 节"打包"分 3 个子节(2.1/2.2/2.3)
- **选定**:沿用 needs §6.1 的 3 子节(软件包 / 目录 / 镜像)
- **理由**:三种打包方式互斥但常见,子节并列让用户"按需选其一"
- **依据**:needs §6.1 + NFR-5(通用性优先)

#### 决策 IT-3:第 5 节"初始化系统"分 4 个子节
- **选定**:沿用 needs §6.1 的 4 子节(5.1 环境准备 / 5.2 DB 建表 / 5.3 DB 初始化数据 / 5.4 配置修改)
- **理由**:这 4 步在生产环境首次部署时**几乎都是必须的**;分开能让用户**逐步**完成
- **依据**:needs §6.1 + FR-3 AC-3.2(每节至少 1 个默认示例)

#### 决策 IT-4:每个 SQL 段加注释行说明路径
- **选定**:`5.2 / 5.3` 子节使用 `sql` 代码块 + 第 1 行 `-- <建表语句路径>:...` 注释
- **理由**:SQL 文件实际在服务器上;注释提示用户"把路径替换成自己的"
- **依据**:NFR-9(可读性优先)

#### 决策 IT-5:第 6 节"启动运行"默认示例用 systemd
- **选定**:`systemctl start myapp; systemctl status myapp`
- **理由**:systemd 是 Linux 服务器最常见的服务管理器;`tar.gz` + systemd 是"软件包方式"的最常见搭配
- **依据**:NFR-5 通用性 + AC-3.2

#### 决策 IT-6:第 8 节"验证清单"用 Markdown checkbox
- **选定**:`- [ ] 服务进程已启动` 等格式
- **理由**:Markdown 原生 checkbox,在 GitHub / IDE 中可勾选;用户可复制为 issue 模板
- **依据**:NFR-9(可读性优先)

#### 决策 IT-7:不预设具体的"目标环境" / "软件名"
- **选定**:`<生产 / 预发 / 测试>` / `myapp`(仅在 systemd + scp + config 路径中作为示例)
- **理由**:NFR-5 通用性 + Q-4 锁定 C(用户必须自己补全)
- **依据**:NFR-5

#### 决策 IT-8:不在模板中写"如需 HTTPS / 防火墙 / 负载均衡等"等高级话题
- **选定**:模板聚焦"最常见部署方式";高级话题留作 v2 扩展
- **理由**:AC-3.2 要求"每节至少 1 个默认示例";"最常见"已经覆盖 80% 场景
- **依据**:NFR-5 通用性

### 验证手段(本任务的"测试"等价物)

| 验证项 | 期望 | 实际 |
| --- | --- | --- |
| 8 大章节齐全(1~8) | ✓ | 8 节齐全 |
| 2 节有 3 子节(2.1/2.2/2.3) | ✓ | 齐全 |
| 5 节有 4 子节(5.1/5.2/5.3/5.4) | ✓ | 齐全 |
| 8 节"验证清单"用 checkbox | ✓ | 5 个 `- [ ]` |
| 文首"使用说明"段 | ✓ | 警示段 |
| `<本版本号>` placeholder | ✓ | 在 H1 + 概述节 |
| 至少 1 个默认示例每节(AC-3.2) | ✓ | 全部满足 |
| 不修改其他 10 个 `code-*` 技能 | ✓(仅新文件) | ✓ |
| 不修改 `rules/` | ✓ | ✓ |
| 不修改 CLAUDE.md / README | ✓ | ✓ |
