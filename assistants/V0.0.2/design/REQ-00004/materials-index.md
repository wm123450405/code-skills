# 材料登记 — REQ-00004

更新时间:2026-06-04 15:50
版本:V0.0.2

## 项目级规范
扫描源:`./assistants/rules/**/*`(13 个文件,2026-06-04 15:50)

| 规范文件 | 类别 | 关键约束摘要 | 对本设计的影响 |
| --- | --- | --- | --- |
| `skill-conventions.md` | 技能元信息 | `SKILL.md` 必含 `name` + `description`,`name` 与目录名 kebab-case 严格一致 | **直接约束**:新增 `code-dashboard` 技能必须遵循 |
| `module-conventions.md`(DEPRECATED) | 模块规划 | 资源放 `templates/` / `checklists/` / `guidelines/` 子目录(已迁移到 `directory-conventions.md`) | 仍可读作历史参考;本设计以 `directory-conventions.md` 为权威源 |
| `directory-conventions.md` | 目录与模块 | 由 `REQ-00003` 替代旧 `module-conventions.md`,目前 §规则 1 占位(待添加) | 本设计在 `module-breakdown.md` 中按"既有惯例"落地,等正式规则生效再校准 |
| `dashboard-conventions.md` | 看板与版本 | §规则 1:看板字段约定扩展需 3 文件同步(`version-RESULT.md` + `CLAUDE.md` + 本规范自身) | **不触发**:`code-dashboard` 纯只读,不写看板,不在本需求扩展字段 |
| `encoding-conventions.md` | 编码格式 | §规则 1/3:`REQ-NNNNN` / `TASK-(REQ|BUG)-NNNNN-NNNNN`,5 位纯数字;NFR-3 必须同时识别旧格式 `REQ-NNNNN-NNNNN` | **直接约束**:`code-dashboard` 任务编号解析逻辑严格遵循 |
| `commit-conventions.md` | 提交与合并 | §规则 1 占位(待添加) | 本设计在 `code-design` 阶段不写 commit,但下游 `code-it` 须遵循 |
| `coding-style.md` | 代码风格 | §规则 1 占位(待添加) | 暂无可遵循细则;`code-dashboard` 是 Markdown/指令型技能,无编程语言约束 |
| `naming-conventions.md` | 语言与命名 | §规则 1 占位(待添加) | 同上 |
| `framework-conventions.md` | 框架选型 | §规则 1 占位(待添加) | 不适用(`code-dashboard` 是指令型技能,无框架) |
| `dependency-conventions.md` | 三方依赖 | §规则 1 占位(待添加);NFR-1 已锁零外部依赖 | NFR-1 直接落定零依赖;`dependencies.md` 评估为"零新增" |
| `doc-conventions.md` | 文档编写 | §规则 1:README 中英同次提交结构对仗;§规则 2:核心小节必覆盖 | **条件触发**:若改 `plugins/code-skills/README.md` + `README.en.md`(可选,非必须),必须同次提交 |
| `marketplace-protocol.md` | Marketplace 协议 | §规则 1:`marketplace.json` + `plugin.json` 字段约束、版本同步、`$schema` 必填 | **直接约束**:NFR-6 锁定**不修改** marketplace.json / plugin.json |
| `migration-mapping.md` | 编码迁移 | 旧编码 → 新编码映射;§规则 4:EXISTING-NNN 不追溯 | `code-dashboard` 不参与编码迁移;透传显示旧字面 |

> 6 个占位规则(commit / coding-style / naming / framework / dependency / directory §1)在 `2026-06-04 10:45` 创建时尚未填充,后续由 `code-rule` 维护。本设计在引用处显式标注"无细则,以既有惯例落地"。

## 上游需求
- 来源:`./assistants/V0.0.2/require/REQ-00004/RESULT.md`
- 版本:v1(已锁定,2026-06-04 12:50)
- 提取:10 FR / 7 NFR / 30 AC / 3 项已锁定 Q-1~Q-3 / 2 项采纳默认 Q-4~Q-5 / 2 项未采用 Q-7~Q-8

## 项目现状(本次扫描)

### 项目类型
- 类型:Claude Code marketplace 仓库(单插件 `code-skills`)
- "代码"主体:`plugins/code-skills/skills/*/SKILL.md`(10 个,均 Markdown 指令型技能)
- 无源代码、构建系统、测试框架、Lint 工具或包管理配置(由 `CLAUDE.md` 显式声明)

### 目录结构
```
code-skills/                                ← marketplace 仓库根
├── .claude-plugin/
│   └── marketplace.json                    # 列 10 个技能(不含 code-dashboard)
└── plugins/
    └── code-skills/                        # 插件本体
        ├── .claude-plugin/
        │   └── plugin.json
        ├── README.md / README.en.md        # 工作流总览与技能表(中英)
        ├── CLAUDE.md                       # 仓库级 AI 约定
        └── skills/
            ├── code-init/  code-version/  code-rule/
            ├── code-require/  code-design/  code-plan/
            ├── code-it/  code-unit/  code-fix/  code-review/
            # ↑ 10 个 code-* 技能,无 code-dashboard
```

### 已有模块
| 技能 | 路径 | 职责 | 与本设计的关系 |
| --- | --- | --- | --- |
| `code-version` | `skills/code-version/` | 读 `.current-version`,创建/切换版本工作空间 | 本设计**第一步**(步骤 0)与其前置契约一致 |
| `code-require` | `skills/code-require/` | 需求分析 → `require/REQ-NNNNN/RESULT.md` | 上游;看板"需求清单"区段由其写入 |
| `code-design` | `skills/code-design/` | 概要设计 → `design/REQ-NNNNN/RESULT.md` | **本技能自身**;其骨架是本设计参照 |
| `code-plan` | `skills/code-plan/` | 详细设计 + 任务拆分 → `plan/REQ-NNNNN/` | 看板"任务清单"区段由其写入(双状态模型) |
| `code-it` | `skills/code-it/` | 任务开发编码,推进"开发状态" | 看板"任务清单"开发状态由其推进 |
| `code-unit` | `skills/code-unit/` | 单元测试,推进"测试状态" | 看板"任务清单"测试状态由其推进 |
| `code-fix` | `skills/code-fix/` | 缺陷登记 → `fix/BUG-NNNNN/RESULT.md` | 看板"缺陷清单"由其写入 |
| `code-review` | `skills/code-review/` | 代码评审(只读型) | 本设计**正交参照对象**:`code-dashboard` 与其同为"只读"型,工具集一致 |
| `code-rule` | `skills/code-rule/` | 编码规范管理 → `rules/*.md` | 不直接相关;但 `code-dashboard` 自身不写规范 |
| `code-init` | `skills/code-init/` | 项目初始化(基线) | 不相关;V0.0.0 后已不使用 |

### 已有接口
- **CLI 入口**:每个 `SKILL.md` 通过 Claude Code 技能协议暴露,用户以 `/code-<name>` 形式调用
- **数据契约**:
  - 看板 `<版本号>/RESULT.md` 7 个固定区段(文档头 / 版本信息 / 里程碑 / 需求清单 / 概要设计清单 / 任务清单 / 缺陷清单 / 评审发现汇总 / 派生任务记录 / 执行的开发命令记录 / 变更记录 / 索引)
  - 区段"## 标题"是锚点(与 §8.2 需求定义一致)
  - 表格列固定(详见 `version-RESULT.md` 模板)
- **状态枚举**:
  - 需求:5 状态(`待开始 / 进行中 / 已完成 / 已取消 / 阻塞`)
  - 任务开发:6 状态(加 `待重新评估`)
  - 任务测试:6 状态(加 `不适用 / 阻塞`)
  - 缺陷:4 严重度(P0 / P1 / P2 / P3)

### 已有数据模型
- 无显式数据模型(无 DB / ORM);"数据"为 Markdown 文本 + 表格行
- 编码权威源:`./assistants/rules/encoding-conventions.md` + `migration-mapping.md`

### 已有第三方依赖
- 0 个运行时依赖(由 `plugin.json` 的 `keywords` 与 `CLAUDE.md` 共同确认;`dependencies` 字段未声明)
- 工具链:`Read` / `Glob` / `Grep` / `Edit` / `Write` / `Bash`(Claude Code 内置)

### 编码与构建约定
- "代码"=Markdown 文档;无构建/编译
- 提交:`commit-conventions.md` 暂未填充;V0.0.1 既有 commit 走 `feat(...)` / `chore(...)` / `fix(...)` conventional 风格(由 `git log` 推断,非强约束)

### 规范 vs 现状偏离
- `module-conventions.md` 顶部显式标注 **DEPRECATED**(已迁移到 `directory-conventions.md`),但 `directory-conventions.md` §规则 1 仍占位(`2026-06-04 10:45` 创建后未填充) — 现状是"以 `module-conventions.md` 既有 §规则 1 为落地依据",等 `directory-conventions.md` 正式生效再校准。本设计在 `module-breakdown.md` 显式标注此偏离。
- `code-review` SKILL.md frontmatter `description` 字段出现 `<version>` 字面(笔误,应为 `<版本号>`)— 与 `skill-conventions §规则 1` 不冲突(无"无错字"要求),但有碍阅读;本设计**不**修复(超出 REQ-00004 范围,留作 follow-up)。
- `README.md` / `README.en.md` 描述的技能清单(8 ~ 10 个)已随 V0.0.1 REQ-00002 / REQ-00003 落地;**不**触发 `doc-conventions §规则 1`(本需求可选改 README,但本设计**建议不改**,避免与 V0.0.2 其他需求并发;若改必须中英同次提交)。

## 跨版本 design/ 目录
- `./assistants/V0.0.2/design/` — **空**(V0.0.2 首个 design,即本设计)
- `./assistants/V0.0.1/design/` — 3 个完整设计包(REQ-00001 / 00002 / 00003),均按本骨架结构产出
- `./assistants/V0.0.0/design/` — **不存在**

## 关联需求
详见 `related-requirements.md`。
