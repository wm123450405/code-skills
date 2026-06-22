# 材料登记 — REQ-00039

更新时间:2026-06-22 14:30
版本:V0.0.3

## 项目级规范

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `skill-conventions.md` | SKILL.md 编写 | frontmatter L1-3 字节级保留;不得包含开发痕迹 |
| `dashboard-conventions.md` | 看板字段约定 | 字段扩展需三方同步;本需求**不**新增列 |
| `encoding-conventions.md` | 编码格式 | REQ/BUG/TASK 命名;5 位纯数字;接收端宽松正则 |
| `migration-mapping.md` | 编码迁移 | `EXISTING-NNN` 不追溯;新旧编码追溯表 |
| `directory-conventions.md` | 目录与模块 | (待添加占位);`plugins/code-skills/skills/<name>/` 子目录布局 |
| `doc-conventions.md` | 文档编写 | README 多语言对仗 + 主语言完整性 |
| `naming-conventions.md` | 命名 | (待添加占位) |
| `coding-style.md` | 代码风格 | (待添加占位);本需求是 Markdown 自然语言 |
| `framework-conventions.md` | 框架 | (待添加占位);无框架变更 |
| `dependency-conventions.md` | 依赖 | (待添加占位);本需求**不**新增依赖(沿用既有 tokei/cloc 系统命令) |
| `commit-conventions.md` | 提交 | `chore(code-<技能>):` 模式 |
| `marketplace-protocol.md` | marketplace | 协议字段约束;本需求**不**改 `.claude-plugin/` |
| `module-conventions.md` | 模块 | `templates/` 留作历史不删(本需求**不**触碰);新模块按命名规范 |

## 上游需求

- 来源:`./assistants/V0.0.3/require/REQ-00039/RESULT.md`(v1,2026-06-22 14:00)
- 提取:**5 FR / 8 NFR / 8 AC**
- 核心诉求:代码行数限制仅统计实际逻辑行(注释 / 说明 / 空行 / 格式化换行不计入);`code-it` 步骤 8 末尾新增 `calcLogicLoc` 子步骤 + `code-check` 步骤 8 评审新增"代码行数超标"发现维度
- 关键约束:tokei/cloc 检测 + 启发式回退;缺陷分支不触达;阈值可配置

## 项目现状(本次扫描)

### 项目类型

- **语言**:Markdown(技能插件定义)+ YAML(frontmatter)
- **框架**:Claude Code skills marketplace(沿用既有)
- **关键依赖**:**无新增依赖**(沿用既有 tokei/cloc 系统命令,本仓库不安装)

### 目录结构

```
plugins/code-skills/skills/
├── code-it/
│   ├── SKILL.md         (1167 行,待改造 — 步骤 8 末尾追加)
│   └── templates/
│       └── RESULT.md     (待改造 — 新增"## 逻辑行统计"示例)
├── code-check/
│   └── SKILL.md          (683 行,待改造 — 步骤 8.13 新增 + 评审维度速查表)
└── ...其他 9 个 code-* 技能(本需求**不**改动)
```

### 已有模块(可复用)

| 模块/路径 | 职责 | 是否可复用 |
| --- | --- | --- |
| `code-it/SKILL.md` §"步骤 8a 项目可测性守卫" | 项目可测性守卫 7 项检查 | 是 — 本需求**不**修改,沿用 7 项检查字面 |
| `code-it/SKILL.md` §"步骤 8.5 按需写单测" | 按需写单测 3 类任务自动判定 | 是 — 本需求**不**修改 |
| `code-check/SKILL.md` §"步骤 8.12 行数比例警告" | design/plan 文档行数比警告 | 是(部分)— 字节级沿用格式,扩展为代码行数 |
| `code-check/SKILL.md` §"## 评审维度速查表" | P0 ~ P3 共 12 维度 | 是(部分)— 字节级保留,新增第 13 维度 |
| `code-it/SKILL.md` §"步骤 13 撰写 RESULT.md" | 模板 7 字段格式 | 是 — 本需求在模板新增"## 逻辑行统计"小节(沿用既有"## 单元测试"模式) |
| `code-it/SKILL.md` §"步骤 7 处理任务前置依赖与状态" | 任务状态推进 | 是 — `calcLogicLoc` 在步骤 8 末尾,**不**触达步骤 7 |

### 已有数据模型

- 本需求**不**新增数据模型(沿用既有 Markdown 文件结构)
- 新增 1 节:"## 逻辑行统计"小节(`code/<task>/RESULT.md` 内)

### 编码与构建约定

- 本仓库是 Markdown 自然语言,**无**构建/运行/测试命令
- 改动通过 `git diff --stat` 静态校验
- 测试状态统一填 `不适用`(沿用 V0.0.3 修订)
- 提交沿用 `chore(code-<技能>):` 模式

### 工具检测

- `tokei`:本环境**未**安装 → 启发式回退会立即生效
- `cloc`:本环境**未**安装 → 启发式回退会立即生效
- 启发式精度 ~95%(沿用上游 RESULT.md §FR-2)

### 关联既有改造(避免冲突)

| REQ | 改造位置 | 冲突风险 |
| --- | --- | --- |
| REQ-00038 | `code-it/SKILL.md` 步骤 8a / 8.5(模块级单测) | **不冲突**(本需求改步骤 8 末尾,REQ-00038 改步骤 8a / 8.5) |
| REQ-00037 | `code-it/SKILL.md` §缺陷分支 17-25 | **不冲突**(本需求缺陷分支不触达 NFR-8) |
| REQ-00034 | `code-it/SKILL.md` 步骤 8a / 8.5(原 `code-unit` 整合) | **不冲突**(沿用原 7 项检查 + 3 类任务判定) |