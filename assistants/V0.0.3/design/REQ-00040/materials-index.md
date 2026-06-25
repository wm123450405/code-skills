# 材料登记 — REQ-00040

更新时间:2026-06-25
版本:V0.0.3

## 项目级规范

| 规范文件 | 类别 | 关键约束摘要 | 触发? |
| --- | --- | --- | --- |
| `coding-style.md` | 命名 / 风格 | 占位(规则 1 待添加);SKILL.md 是自然语言,代码风格不直接约束 | ❌ |
| `commit-conventions.md` | 提交 | 占位(规则 1 待添加);沿用既有 `chore(code-it): ...` / `chore(code-design): ...` 前缀 | ⚠️ 软(本设计**不**新增规则) |
| `dashboard-conventions.md` | 看板 | §规则 1:看板字段扩展需三同步(模板 + CLAUDE.md + dashboard-conventions);本设计**不**新增看板列(产物放 `fix/<BUG-NNN>/reproduce/` 子目录),**0 触发** | ❌(0 触发) |
| `dependency-conventions.md` | 三方依赖 | 占位(规则 1 待添加);本设计**0 新增三方依赖**(playwright/puppeteer/headless-chrome 仅是"运行时探测",非项目级依赖) | ❌(0 新增) |
| `directory-conventions.md` | 目录 | §规则 1 占位(待添加);沿用 `code-fix/templates/` 既有目录布局;**不**新增目录(`reproduce/` 子目录在 `fix/<BUG-NNN>/` 内,符合 `assistants-layout.md` 既有"fix/BUG-NNN/ 下子目录"约定) | ⚠️ 软 |
| `doc-conventions.md` | 文档 | README 多语言对仗;**0 触发**(本需求不涉及 README) | ❌ |
| `encoding-conventions.md` | 编码格式 | §规则 1:3 类编码(REQ/BUG/TASK)正则;**不**触发(本需求不新增编码格式,沿用既有 BUG-NNNNN 5 位纯数字) | ❌ |
| `framework-conventions.md` | 架构 | 框架级约束;**不**触发(本需求是技能库内部,非项目架构) | ❌ |
| `marketplace-protocol.md` | 插件市场 | marketplace.json / plugin.json 元信息;**不**触发(本需求不涉及插件清单) | ❌ |
| `migration-mapping.md` | 迁移映射 | 旧→新编码追溯;**不**触发(本需求不涉及编码迁移) | ❌ |
| `module-conventions.md` | 模块 | ⚠️ **DEPRECATED**(已迁移到 `directory-conventions.md`);本设计**不**引用此规范 | ❌ |
| `naming-conventions.md` | 命名 | 占位(规则 1 待添加);`reproduce/` 子目录名遵循既有"小写 + 复数"风格 | ⚠️ 软 |
| `skill-conventions.md` | 技能 | §规则 1:SKILL.md frontmatter(name + description)必含;§规则 2:SKILL.md / templates/ 不得含开发痕迹字面(6 类强约束) | ✅ **强**(§规则 1 字节级保留;§规则 2 本设计**不**在产物 SKILL.md / 模板中写"本需求 REQ-00040 新增"等字面) |

## 上游需求

- 来源:`./assistants/V0.0.3/require/REQ-00040/RESULT.md`
- 版本:v1(2026-06-25)
- 提取:6 FR / 10 NFR / 12 AC / 4 待澄清(全部为可接受默认)

## 项目现状(本次扫描)

### 项目类型
- 仓库:Claude Code `code-skills` 插件市场仓库
- 主体:Markdown 技能库(14 个 `code-*` 技能)+ 项目级规范(13 份)
- 改造目标:`code-fix` 技能(纯登记型,V0.0.3 REQ-00027 落地;状态推进路径 V0.0.3 REQ-00037 收敛)

### 目录结构(`code-fix` 子树)
```
plugins/code-skills/skills/code-fix/
├── SKILL.md           # 技能入口(431 行;frontmatter L1-3 字节级保留)
├── templates/         # 技能产出物模板
│ ├── assistants-layout.md  # 目录结构说明(沿用 V0.0.1 风格,**不**列 reproduce/ 子目录)
│ ├── bug.md           # 缺陷详情模板(60 行,含文档头/缺陷描述/根因分析/修复方案/修复实施/验证结果/修复日志/关联项/变更记录 9 区段)
│ └── fix-registry.md  # 缺陷总览模板(100 行,7 列表格;**不**新增列)
```

### 已有模块
| 模块/路径 | 职责 | 是否可复用 |
| --- | --- | --- |
| `code-fix/SKILL.md` | 缺陷登记与跟踪(纯登记型) | 是(主改造对象) |
| `code-fix/templates/bug.md` | 缺陷详情模板 | 是(主改造对象) |
| `code-fix/templates/fix-registry.md` | 缺陷总览模板 | 是(沿用,**不**新增列) |
| `code-fix/templates/assistants-layout.md` | 目录结构说明 | **是**(需追加 `reproduce/` 子目录说明) |
| `code-it/lib/logic-loc.md` | 共享库(代码逻辑行计算) | 不可复用(本需求**不**涉及代码逻辑行) |

### 已有接口
- 内部:`code-fix` 步骤 0~10 工作流(纯 Markdown 流程,无 API)
- 上下游:`code-plan` / `code-it` / `code-check`(本需求不修改其接口)

### 已有数据模型
- 状态机(REQ-00037 收敛):`待处理` / `待开发` / `开发中` / `待审查` / `已完成`(5 新字面)+ 10 老字面(不归一化)
- 文档头字段(`bug.md` 现有 11 字段):本需求**新增 2 字段**(复现方式 / 产物路径)

### 已有第三方依赖
- **项目级**:**0 个三方依赖**(本仓库不引入 npm / pip 等包管理)
- **运行时探测**:`playwright` / `puppeteer` / `headless-chrome` 仅作为"启动命令探测"的可选项,**不**作为项目级依赖

### 编码与构建约定
- SKILL.md:**纯 Markdown**,无代码逻辑
- 模板:`<占位符>` 风格,沿用既有 `<bugNum>` / `<command>` / `<时间>` 命名
- 注释:中文 + 英文混排;段尾 / 段中 **不**写"(本需求 REQ-XXXXX 新增)" 类字面(沿用 `skill-conventions §规则 2`)
- 末尾提交:沿用 V0.0.1 实践,1 次 `chore(code-design):` + 1 次 `chore(code-plan):` + N 次 `chore(code-it):` 串行
