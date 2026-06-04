# 模块拆分 — REQ-00006

更新时间:2026-06-04 16:48
版本:V0.0.2

## 1. 模块总览

| 模块 | 路径 | 状态 | 职责 | 对外接口 | 依赖 |
| --- | --- | --- | --- | --- | --- |
| **`code-publish` 技能** | `plugins/code-skills/skills/code-publish/SKILL.md` | **新增** | 整个发布部署技能的入口(SKILL.md frontmatter + 工作流) | Claude Code 协议触发 | `.current-version` / 主看板 |
| **PreflightChecker**(逻辑模块) | SKILL.md §步骤 1 | **新增** | 解析主看板 3 区段,生成"未完成项明细" + 通过/不通过判定 | 输入:看板路径;输出:`{通过: bool, 未完成项: [...], 统计: {...}}` | 看板格式(只读) |
| **BaselineDetector**(逻辑模块) | SKILL.md §步骤 2.0 | **新增** | 识别本版本是否是基线(规则 1:字典序最小) | 输入:版本号;输出:`bool` | `./assistants/<all versions>/` |
| **ManualBuilder**(逻辑模块) | SKILL.md §步骤 2 | **新增** | 根据基线判定结果,选择性生成 DEPLOY.md / UPDATE.md / Q&A.md | 输入:版本号、基线判定;输出:写入文件列表 | DEPLOY/UPDATE/Q&A 模板 |
| **QandaScaffolder**(逻辑模块) | SKILL.md §步骤 2 | **新增** | 若 `assistants/qanda/` 不存在,创建目录 + README.md(本需求顺带) | 输入:无;输出:写入或跳过 | `assistants/qanda/` 目录 |
| **QandaAggregator**(逻辑模块) | SKILL.md §步骤 2 | **新增** | 聚合 `assistants/qanda/*.md`(排除 README)到 Q&A.md | 输入:qanda/ 目录;输出:Q&A.md 内容 | 同上 |
| **ReportFormatter**(逻辑模块) | SKILL.md §步骤 3 | **新增** | 生成给用户的纯文本报告(通过/不通过/基线/qanda 空) | 输入:前 3 模块的结果;输出:多行文本 | 无 |
| **`code-publish/templates/DEPLOY.md`** | `plugins/code-skills/skills/code-publish/templates/DEPLOY.md` | **新增** | 通用部署手册骨架模板 | 文件模板(被复制 + 填充) | 无 |
| **`code-publish/templates/UPDATE.md`** | `plugins/code-skills/skills/code-publish/templates/UPDATE.md` | **新增** | 通用升级手册骨架模板 | 同上 | 无 |
| **`code-publish/templates/Q&A.md`** | `plugins/code-skills/skills/code-publish/templates/Q&A.md` | **新增** | Q&A 模板(占位 + 聚合)| 同上 | 无 |
| **`code-publish/templates/qanda-README.md`** | `plugins/code-skills/skills/code-publish/templates/qanda-README.md` | **新增** | `assistants/qanda/README.md` 的骨架 | 同上 | 无 |
| **`code-publish/templates/assistants-layout.md`** | `plugins/code-skills/skills/code-publish/templates/assistants-layout.md` | **新增** | 沿用其他技能的"工作目录约定"摘要(标准模板) | 同上 | 无 |
| **`assistants/qanda/`** | `./assistants/qanda/` | **新增**(本需求顺带) | 项目级 Q&A 长期沉淀目录 | 被 `code-publish` 聚合 | 无 |
| **`assistants/qanda/README.md`** | `./assistants/qanda/README.md` | **新增**(本需求顺带) | qanda/ 目录用途说明 | 无 | 无 |

## 2. 新增模块详解

### 2.1 模块:`code-publish` 技能(SKILL.md)

- **路径**:`plugins/code-skills/skills/code-publish/SKILL.md`
- **职责**:Claude Code 在用户输入 `/code-publish [版本号]` 时,通过 frontmatter `name: code-publish` + `description: ...` 触发本技能;正文是 Claude 执行的自然语言指令
- **关键设计点**:
  - frontmatter 严格遵循 `skill-conventions.md §规则 1`:`name: code-publish` + 完整 `description`
  - 工作流分 4 大步:步骤 0(版本上下文)→ 步骤 1(前置检查)→ 步骤 2(生成手册)→ 步骤 3(报告)
  - 异常路径用 `不适用` / `中止` 显式标注
- **对外接口**:
  - 入口:用户在 Claude Code 中输入 `/code-publish` 或 `/code-publish V0.0.2`
  - 输出:文件系统(publish/ 目录) + 标准输出(报告)
- **依赖**:
  - 读 `.current-version`(若无参数)
  - 读 `./assistants/<版本号>/RESULT.md`(主看板)
  - 读 `./assistants/qanda/*.md`(可选)
  - 读模板 `templates/DEPLOY.md` / `UPDATE.md` / `Q&A.md` / `qanda-README.md`
  - 写 `./assistants/<版本号>/publish/DEPLOY.md` + `UPDATE.md`(条件) + `Q&A.md`
  - 写 `./assistants/qanda/` + `README.md`(条件,首次)
- **理由**:
  - 与已有 10 技能保持一致(都是 SKILL.md + templates/);新增第 11 个技能(目前已有 10 技能 — 见 `code-init/code-version/code-rule/code-require/code-design/code-plan/code-it/code-unit/code-fix/code-review`)
  - 注:用户需求 §G-1 写"第 9 个 `code-*` 技能",实际是第 11 个(算上 `code-init`/`code-version`/`code-rule`/`code-fix`)— 这是**用户口语化表达**,不构成需求变更;本设计沿用"第 9 个 code-* 技能 / 实际为第 11 个"的统一描述,不修正需求 v1
- **符合规范**:
  - `skill-conventions.md §规则 1`:✓ frontmatter 必含 name + description,name=code-publish 与目录同
  - `module-conventions.md §规则 1`:✓ templates/ 子目录摆放模板,不散落

### 2.2 模块:PreflightChecker(SKILL.md §步骤 1 中的逻辑章节)

- **路径**:`SKILL.md` 内"## 步骤 1:前置检查"小节
- **职责**:解析主看板 3 区段(需求清单 / 任务清单 / 缺陷清单),生成"未完成项明细"
- **关键设计点**:
  - 使用 `Read` 一次性读取 `./assistants/<版本号>/RESULT.md`
  - 用 `sed -n '/^## 需求清单/,/^## /p'` 等定位区段(若 Bash 解析)或直接用 Markdown 段落识别(若 LLM 解析)
  - 行解析:正则 `^\| ` 识别表格数据行,跳过分隔行 `^\|---` 和统计行 `^\*\*统计`
  - 状态映射:沿用 needs §8.3 的"解决映射表"
- **对外接口**:无(SKILL.md 内部步骤)
- **依赖**:
  - `Read` 工具
  - 主看板的稳定表格结构(已 V0.0.1 起稳定)
- **理由**:
  - NFR-2 锁定纯只读,所以**只用 Read**,不用 Edit
  - NFR-8 锁定"与 code-dashboard 数据源一致",所以解析规则**与 code-dashboard 共用**同一锚点 + 同一列识别
- **符合规范**:无规范覆盖此模块(占位规范不影响)

### 2.3 模块:BaselineDetector

- **路径**:`SKILL.md` 内"## 步骤 2.0:基线识别"
- **职责**:判定本版本是否是基线(规则 1)
- **关键设计点**:
  - `Glob "./assistants/V*/"` 列出所有版本目录
  - 字典序排序,取最小
  - 若最小 == 本版本号 → 基线;否则非基线
- **对外接口**:无
- **依赖**:`Glob` 工具
- **理由**:NFR-7 锁定规则 1
- **符合规范**:无

### 2.4 模块:ManualBuilder

- **路径**:`SKILL.md` 内"## 步骤 2:生成手册"
- **职责**:根据基线判定 + 前置检查结果,选择性生成 3 份手册
- **关键设计点**:
  - `mkdir -p ./assistants/<版本号>/publish/`(若不存在)
  - 读取模板 → 替换 placeholder(`<本版本号>` / `<源版本>` 用 Bash 字符串替换或 LLM 渲染)→ `Write` 到目标路径
  - 基线版本:跳过 UPDATE.md
  - 已有文件:覆盖(D-7)
  - 写文件前 `ls -la publish/` 检查并报告"将覆盖 N 个文件"
- **对外接口**:无
- **依赖**:`Bash`(mkdir / ls)、`Read`(模板)、`Write`(目标文件)
- **理由**:FR-2 / FR-3 / FR-4 / NFR-6
- **符合规范**:无

### 2.5 模块:QandaScaffolder

- **路径**:`SKILL.md` 内"## 步骤 2.5:创建 qanda/ 骨架(条件)"
- **职责**:若 `assistants/qanda/` 不存在,创建目录 + 写入 README.md
- **关键设计点**:
  - `ls assistants/qanda/` 检测存在性
  - 不存在 → `mkdir -p` + `Write` README.md(来自 `templates/qanda-README.md`)
  - 存在 → 跳过
  - 失败(权限等) → 不阻塞整体流程(FR-7.AC-7.4)
- **对外接口**:无
- **依赖**:`Bash`(mkdir / ls)、`Read`(模板)、`Write`(README.md)
- **理由**:FR-6
- **符合规范**:无

### 2.6 模块:QandaAggregator

- **路径**:`SKILL.md` 内"## 步骤 2.6:聚合 Q&A 内容"
- **职责**:遍历 `assistants/qanda/*.md`(排除 README),聚合到 Q&A.md
- **关键设计点**:
  - `Glob "./assistants/qanda/*.md"`,过滤掉 `README.md`
  - 空列表 → 写"占位"模板(AC-5.1 / AC-5.2)
  - 非空 → 每个文件读内容 + 加 `## <文件名去后缀>` + `> 来源:qanda/<文件名>` 标注(AC-5.4)
- **对外接口**:无
- **依赖**:`Glob`、`Read`、`Write`
- **理由**:FR-5
- **符合规范**:无

### 2.7 模块:ReportFormatter

- **路径**:`SKILL.md` 内"## 步骤 3:报告"
- **职责**:生成最终给用户的多行纯文本报告
- **关键设计点**:
  - 4 种报告模板(对应 §S-1 / §S-2 / §S-3 / §S-4 / §S-5)
  - 每种含:`✓`/`✗`/`⚠` 图标 + 统计 + 建议下一步
  - 直接由 Claude 输出(无文件写入)
- **对外接口**:终端文本输出
- **依赖**:前 6 个模块的结果汇总
- **理由**:FR-9 / NFR-9
- **符合规范**:无

### 2.8 模板:DEPLOY.md(`templates/DEPLOY.md`)

- **路径**:`plugins/code-skills/skills/code-publish/templates/DEPLOY.md`
- **职责**:全新部署手册骨架(REQ-00006 §6.1 节选)
- **关键设计点**:
  - 完整 8 章节结构:概述 / 打包(3 选 1)/ 获取成果物 / 上传 / 初始化(4 子节)/ 启动 / 首次进入 / 验证清单
  - placeholder 风格:`<本版本号>` / `<打包方式>` 等用尖括号包裹
  - 默认示例:每节至少 1 个可执行示例(占位)
  - 文首"使用说明"段
- **对外接口**:被 ManualBuilder 读取并写到 `publish/DEPLOY.md`
- **依赖**:无
- **理由**:FR-3
- **符合规范**:无

### 2.9 模板:UPDATE.md(`templates/UPDATE.md`)

- **路径**:`plugins/code-skills/skills/code-publish/templates/UPDATE.md`
- **职责**:从上一版本升级手册骨架(REQ-00006 §6.2 节选)
- **关键设计点**:
  - 章节结构 = DEPLOY.md + 新增 §8 回滚方案
  - placeholder:`<源版本>` / `<本版本号>`(由 ManualBuilder 自动填充)
- **对外接口**:被 ManualBuilder 读取并写到 `publish/UPDATE.md`
- **依赖**:无
- **理由**:FR-4
- **符合规范**:无

### 2.10 模板:Q&A.md(`templates/Q&A.md`)

- **路径**:`plugins/code-skills/skills/code-publish/templates/Q&A.md`
- **职责**:Q&A 手册的"占位模板"骨架
- **关键设计点**:
  - 文首"## 占位:常见问题(待补充)"段
  - 提示"请先在 assistants/qanda/ 中添加 Q&A 内容,再重跑"
  - 当 QandaAggregator 有内容时,会**在占位段之前**插入聚合的章节
- **对外接口**:被 QandaAggregator + ManualBuilder 联合渲染并写到 `publish/Q&A.md`
- **依赖**:无
- **理由**:FR-5
- **符合规范**:无

### 2.11 模板:qanda-README.md(`templates/qanda-README.md`)

- **路径**:`plugins/code-skills/skills/code-publish/templates/qanda-README.md`
- **职责**:`./assistants/qanda/README.md` 的骨架
- **关键设计点**:
  - 说明 4 项:目录用途 / 命名建议 / 引用规范 / 维护方式
- **对外接口**:被 QandaScaffolder 读取并写到 `./assistants/qanda/README.md`
- **依赖**:无
- **理由**:FR-6 AC-6.2
- **符合规范**:无

### 2.12 模板:assistants-layout.md(`templates/assistants-layout.md`)

- **路径**:`plugins/code-skills/skills/code-publish/templates/assistants-layout.md`
- **职责**:沿用其他技能的"工作目录约定"摘要(标准技能资产)
- **关键设计点**:复制 `code-version/templates/assistants-layout.md` 的内容,加上 publish/ + qanda/ 段
- **对外接口**:供查阅(不被自动消费)
- **依赖**:无
- **理由**:与其他技能保持一致(`code-version` / `code-design` / `code-fix` / `code-rule` 都有此文件)
- **符合规范**:`module-conventions.md §规则 1`(templates/ 子目录)

## 3. 复用既有模块

| 既有模块 | 复用方式 | 引用位置 |
| --- | --- | --- |
| `code-version/.current-version` 读取范式 | 沿用相同 `Read "./assistants/.current-version"` | `code-version/SKILL.md` 步骤 1 |
| `code-version/templates/version-RESULT.md` 看板结构 | **只读**作为解析锚点参考 | `plugins/code-skills/skills/code-version/templates/version-RESULT.md:1-200` |
| `code-design/templates/assistants-layout.md` 范式 | 复制到本技能的同名文件 | 各技能 templates/ 下都有 |

## 4. 修改既有模块

- **0 个**(NFR-8 + FR-8 显式约束)
- 特别声明:
  - **不**修改 `marketplace.json` / `plugin.json`(FR-8.AC-8.1)— 注:这意味着新技能 `code-publish` **不**会出现在 marketplace 的 `plugins[].skills[]` 列表中,需要在 v2 由独立任务补全;**本设计不阻塞**该决策(留作 follow-up,见 RESULT.md §11)
  - **不**修改其他 10 个 `code-*` SKILL.md(FR-8.AC-8.2)
  - **不**修改 `./assistants/rules/` 下任何规范(FR-8.AC-8.3)
  - **不**填充 `commit-conventions.md §规则 1`(FR-8.AC-8.4)
  - **不**追加 `CLAUDE.md` "AI 工作约定" 小节(Q-8 默认)

## 5. 模块自检(对照 `module-conventions.md §规则 1`)

| 项 | 规范要求 | 本设计 | 合规 |
| --- | --- | --- | --- |
| `templates/` 子目录 | 文档模板放在此 | DEPLOY/UPDATE/Q&A/qanda-README/assistants-layout 5 份模板均在 `templates/` | ✓ |
| `checklists/` 子目录 | 校验清单放在此 | 本技能**不**含校验清单(只检查 3 区段,逻辑在 SKILL.md 内) | ✓(空目录不强制存在) |
| `guidelines/` 子目录 | 强制规则文档放在此 | 本技能**不**强制额外规则(规则全在 SKILL.md 内) | ✓(空目录不强制存在) |
| SKILL.md 在技能根目录 | 是 | `code-publish/SKILL.md`(根) | ✓ |
| 资源散落仓库其它位置 | 禁止 | 0 散落 | ✓ |

**结论**:0 不合规项。

## 6. 模块自检(对照 `skill-conventions.md §规则 1`)

| 项 | 规范要求 | 本设计 | 合规 |
| --- | --- | --- | --- |
| YAML frontmatter | 必须 | SKILL.md 顶部 | ✓ |
| `name` 字段 | 必填,等于目录名 | `name: code-publish`,目录 = `code-publish` | ✓ |
| `description` 字段 | 必填,非空非占位 | 完整描述(目标 + 适用场景 + 关键产出) | ✓ |

**结论**:0 不合规项。
