# 材料登记 — REQ-00018
更新时间:2026-06-06 13:00
版本:V0.0.2
需求编码:REQ-00018

## 项目级规范

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| skill-conventions.md | 技能编写 | SKILL.md 必含 name + description;frontmatter 字节级保留(NFR-7 强约束) |
| module-conventions.md | 模块规划 | (已弃用,内容迁移到 directory-conventions) |
| directory-conventions.md | 目录结构 | 技能资源放固定子目录(templates/ / checklists/ / guidelines/) |
| dependency-conventions.md | 依赖管理 | 零新增依赖优先;新增依赖需评审 |
| dashboard-conventions.md | 看板 | 看板字段扩展需三方同步 |
| encoding-conventions.md | 编码 | REQ / BUG / TASK 编码权威源 |
| commit-conventions.md | 提交 | commit 消息格式约定 |
| doc-conventions.md | 文档 | 文档编写约定 |
| marketplace-protocol.md | marketplace | marketplace.json 既有字段不变 |
| naming-conventions.md | 命名 | 命名约定 |
| coding-style.md | 编码风格 | 编码风格约定 |
| framework-conventions.md | 框架 | 框架使用约定 |
| migration-mapping.md | 迁移 | 跨版本映射 |

## 上游需求

- 来源:`./assistants/V0.0.2/require/REQ-00018/RESULT.md`
- 版本:v1(更新时间 2026-06-06 12:45)
- 提取的 FR / NFR / AC 数量:**6 / 9 / ~30**
- 上游确认状态:已锁定
- 关键决策:2 项已锁定(Q-1 范围 / Q-2 术语),5 项采纳默认(Q-3~Q-7),1 项建议派生(Q-8)

## 项目现状(本次扫描)

### 项目类型
- 类型:Claude Code marketplace 仓库
- 关键产出:`plugins/code-skills/skills/<技能名>/SKILL.md` 12 个
- 构建:无(本仓库不包含源代码、构建系统、测试框架、Lint 工具或包管理配置 — CLAUDE.md 严守)
- 测试:无(本仓库**不**包含任何测试框架)

### 目录结构(顶层)
- `.claude-plugin/marketplace.json` — 插件市场清单
- `plugins/code-skills/` — 插件本体
  - `.claude-plugin/plugin.json` — 插件元信息
  - `README.md` / `README.en.md` — 工作流总览
  - `CLAUDE.md` — 本文件
  - `skills/<技能名>/SKILL.md` — 12 个技能入口
    - `templates/` — 文档模板
    - `checklists/` — 校验清单
    - `guidelines/` — 规则文档

### 已有技能清单(12 个)
| 技能 | SKILL.md 行数 | 本需求影响 |
| --- | --- | --- |
| code-version | 207 | **本需求修改对象** |
| code-init | ... | 不修改 |
| code-rule | ... | 不修改 |
| code-require | ... | 不修改 |
| code-design | ... | 不修改 |
| code-plan | ... | 不修改 |
| code-it | ... | 不修改 |
| code-unit | ... | 不修改 |
| code-fix | ... | 不修改 |
| code-review | ... | 不修改 |
| code-dashboard | ... | 不修改 |
| code-publish | ... | 不修改 |
| code-merge | ... | 不修改 |
| code-auto | ... | 不修改 |

### 受影响模块(本需求只改 1 个)
- `plugins/code-skills/skills/code-version/SKILL.md`(增量追加"步骤 7"小节)

### 已有接口(本需求不新增)
- `code-version` 既无对外 API 端点 / 也无对外函数导出
- 本需求**不**新增 CLI 参数(Q-7 采纳默认,`--skip-cwd-sync` 留作 v2)

### 已有数据模型(本需求不新增)
- 看板模板:`plugins/code-skills/skills/code-version/templates/version-RESULT.md`(**不**修改,NFR-6 严守)

### 已有第三方依赖(本需求不新增)
- 0 三方库依赖
- 0 外部命令依赖

### 编码与构建约定
- 无构建命令(本仓库**不**包含任何构建系统)
- 无测试命令(本仓库**不**包含任何测试框架)
- 验证手段:`Read` / `Grep` 静态检查 + 人工场景验证(S-1 ~ S-8)

## 关键交叉点(每条 FR 对应设计章节)

| FR | 对应设计章节 | 关键决策 |
| --- | --- | --- |
| FR-1(新增步骤 7) | §3.2 步骤 7 子小节结构 / §3.3 关键变更 | D-1 增量追加锚点 |
| FR-2(版本号取值) | §2 D-3 / §7 屏幕输出契约 | 默认 = 新激活的 `<版本号>` |
| FR-3(CWD 路径) | §3.3 关键变更 | 默认 = `process.cwd()` |
| FR-4(不修改 code-skills 自身) | §3.1 受影响文件清单 | 严守 Q-1 锁定 |
| FR-5(屏幕输出契约) | §7 屏幕输出契约 | 5 类输出格式锁定 |
| FR-6(--skip-cwd-sync) | §2 D-5 不引入 CLI 参数 | Q-7 采纳默认 |
| NFR-1(零依赖) | §5 三方依赖评估 | 0 新增依赖 |
| NFR-2(增量改 SKILL.md) | §2 D-1 增量追加 | Edit 锚点 = "## 工作流程" 段后 |
| NFR-3(不修改 12 个其他技能) | §3.1 受影响文件清单 | 严守 |
| NFR-4(不修改 code-skills 自身) | §3.1 受影响文件清单 | 严守 |
| NFR-5(不修改规范) | §11 规范遵循 | 严守 |
| NFR-6(不修改看板模板) | §3.1 受影响文件清单 | 严守 |
| NFR-7(性能 < 5 秒) | §9 性能 | 单文件 ~1 秒,monorepo 10 个 ~5 秒 |
| NFR-8(失败不阻断) | §2 D-4 / §8 边界与异常 | 严守 |
| NFR-9(不参与 REQ-00005 扩展) | §2 D-1 | 本需求是 `code-version`,不是其他技能 |
