# 材料登记 — REQ-00013
更新时间:2026-06-05 21:00
版本:V0.0.2

## 项目级规范
| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| skill-conventions.md | 技能元信息 | SKILL.md 必含 name + description frontmatter;name 与目录名一致 |
| module-conventions.md | 资源摆放(已弃用) | 资源放 `templates/` / `checklists/` / `guidelines/` 子目录 |
| directory-conventions.md | 目录结构 | 替代 module-conventions,本轮无新规则 |
| encoding-conventions.md | 编码格式 | 需求/缺陷/任务三类编码权威源(REQ-NNNNN / BUG-NNNNN / TASK-...)|
| dashboard-conventions.md | 看板字段 | 扩展看板字段需 `templates/version-RESULT.md` + CLAUDE.md + 本规范 三方同步 |
| commit-conventions.md | 提交规范 | 占位(本轮不追加)|
| dependency-conventions.md | 依赖管理 | 占位(本轮零依赖)|
| doc-conventions.md | 文档 | 中英 README 同次提交 + 章节对仗 |
| framework-conventions.md | 框架 | 占位(本轮无关)|
| migration-mapping.md | 迁移映射 | 新旧编码追溯(本轮无关)|
| naming-conventions.md | 命名 | 占位(本轮无关)|
| coding-style.md | 编码风格 | 占位(本轮无关)|
| marketplace-protocol.md | 插件协议 | 不动(本轮不修改 marketplace.json / plugin.json)|

## 上游需求
- 来源:./assistants/V0.0.2/require/REQ-00013/RESULT.md
- 版本:v1(2026-06-04 15:25)
- 提取的 FR / NFR / AC 数量:11 FR / 10 NFR / ~30 AC / 9 边界场景
- 关键决策(Q-1~Q-4 已锁):
  - Q-1:从已有内容派生,不新增字段(零规范变更)
  - Q-2:格式 = `REQ-00001 · 标题`(中点 `·` 格式)
  - Q-3:字符数 ≤ 30
  - Q-4:本轮升级 6 技能(3 生成源 + 4 消费方,`code-dashboard` 不变)

## 项目现状(本次扫描)
### 项目类型
- 仓库类型:Claude Code 插件集合(marketplace 协议)
- 语言:Markdown(技能 SKILL.md + 模板 + 文档)
- 框架:Claude Code 技能调度
- 关键依赖:无运行时依赖(本仓库是工具集,无构建/测试)

### 目录结构
- 仓库根:`./`(marketplace 清单)
- 插件本体:`./plugins/code-skills/`
  - `.claude-plugin/plugin.json`
  - `README.md` / `README.en.md` / `CLAUDE.md`
  - `skills/<code-*>/SKILL.md` × 13

### 已有模块
| 模块/路径 | 职责 | 是否可复用 |
| --- | --- | --- |
| `code-require/SKILL.md` | 需求分析(版本感知) | 是(增量追加)|
| `code-plan/SKILL.md` | 详细设计 + 任务计划 | 是(增量追加)|
| `code-fix/SKILL.md` | 缺陷登记与跟踪(支线)| 是(增量追加,本轮首次升级)|
| `code-it/SKILL.md` | 编码实施 | 是(增量追加)|
| `code-unit/SKILL.md` | 单元测试 | 是(增量追加)|
| `code-review/SKILL.md` | 代码评审 | 是(增量追加)|
| `code-auto/SKILL.md` | 编排驱动 | 是(增量追加)|
| `code-dashboard/SKILL.md` | 看板(只读)| 否(NFR-2 不改,看板"标题"列已存在)|
| `code-publish/SKILL.md` | 发布部署 | 部分改(报告升级,NFR-5)|
| `code-version/SKILL.md` | 版本管理 | 否(NFR-6 不改)|
| `code-rule/SKILL.md` | 编码规范 | 否(NFR-6 不改)|

### 已有接口
- 无 API(纯文档型仓库)

### 已有数据模型
- `assistants/V<版本>/RESULT.md`(版本看板):"任务清单"区段已含"标题"列(V0.0.1 起固定)
- `assistants/V<版本>/require/<需求编号>/RESULT.md`:第 1 行 `# 需求提示词文档 — <需求标题>`
- `assistants/V<版本>/plan/<需求编号>/PLAN.md`:任务总览含"标题"列
- `assistants/V<版本>/fix/<缺陷编号>/RESULT.md`:本轮新增"## 缺陷标题"小节

### 已有第三方依赖
- 无

### 编码与构建约定
- `skill-conventions §规则 1`:SKILL.md frontmatter `name` + `description` 必含,字节级保留
- `doc-conventions §规则 1`:中英 README 同次提交,章节对仗
- `dashboard-conventions §规则 1`:看板字段扩展需三方同步
- `marketplace-protocol.md`:不动 marketplace.json / plugin.json
