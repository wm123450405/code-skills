# 目录与模块规范(Directory Conventions)

> 本规范文件由 `code-rule` 技能维护,所有 `code-*` 技能在执行时会读取本文件作为强制约束。
> 最后更新:2026-06-04 10:45
> 适用版本:跨所有版本共享(项目级)

## 适用场景

本规范文件覆盖**目录结构 / 模块划分 / 文件组织**相关规则。涉及"代码放在哪里 / 模块边界 / 包结构"等项目级结构决策时查阅本文件。

> **迁移说明**:本文件替代旧 `module-conventions.md`(已迁移)。新规则请直接追加到本文件。

## 强制级别约定

本文件中各规则的强制级别逐条标注(参见各"规则 N"小节的"强制级别"字段),本文件头部不统一声明。

---

## 规则 1:版本工作空间与技能目录结构

### 条款

本仓库采用 **版本感知工作空间** 模式,所有开发产出物按版本隔离:

**版本工作空间**(`assistants/<版本号>/`):
```
assistants/<版本号>/
├── RESULT.md              # 版本看板(简化版,仅需求清单+缺陷清单)
├── req/<REQ>/             # 需求路径(code-req 产出)
│   ├── REQUIRE.md         # 需求分析
│   ├── DESIGN.md          # 软件设计
│   ├── PLAN.md            # 任务排期
│   ├── PROCESS.md         # 执行进度(阶段追踪:INIT→REQUIRE→DESIGN→PLAN→CODING→CHECK→DONE)
│   ├── TASK-N.md          # 任务完成报告(N=1,2,...)
│   └── CHECK.md           # 代码审查
└── fix/<BUG>/             # 缺陷路径(code-fix 产出)
    ├── BUG.md             # 缺陷分析
    ├── DESIGN.md          # 修复方案设计
    ├── PLAN.md            # 修复任务排期
    ├── PROCESS.md         # 修复进度(阶段追踪:INIT→DESIGN→PLAN→CODING→CHECK→DONE)
    ├── TASK-N.md          # 修复任务报告
    └── CHECK.md           # 修复审查
```

**技能目录**(`plugins/code-skills/skills/`):
```
plugins/code-skills/skills/
├── code-ver/       # 版本管理(合并 code-version + code-publish + code-init)
├── code-req/       # 需求开发全流程(合并 code-require + code-design + code-plan + code-it + code-check)
├── code-fix/       # 缺陷修复全流程
├── code-faq/       # 知识查询与导出(原 code-answer)
├── code-rule/      # 编码规范管理(项目级共享)
├── code-merge/     # Worktree 自动合并
└── code-dashboard/ # 开发看板(只读)
```

### 强制级别
- 必须

### 适用范围
- 所有 `code-*` 技能在读写版本工作空间时
- 所有 `code-*` 技能在引用其他技能时
- 新版本初始化时由 `code-ver` 按此结构创建

### 正面示例
- `code-req REQ-00001` → 产出 `req/REQ-00001/REQUIRE.md`、`DESIGN.md`、`PLAN.md`、`PROCESS.md`、`TASK-*.md`、`CHECK.md`
- `code-fix BUG-00001` → 产出 `fix/BUG-00001/BUG.md`、`DESIGN.md`、`PLAN.md`、`PROCESS.md`、`TASK-*.md`、`CHECK.md`

### 反面示例
- 在 `req/` 下创建 `RESULT.md`(旧命名,应使用 `REQUIRE.md`)
- 在 `fix/` 下创建 `RESULT.md`(旧命名,应使用 `BUG.md`)
- 使用旧路径 `require/`、`design/`、`plan/`、`code/`、`review/`(已废弃)

### 例外
- 历史版本(V0.0.0~V0.0.3)使用旧目录结构(`require/`/`design/`/`plan/`/`code/`/`review/`),不追溯迁移

### 关联规范
- `./assistants/rules/encoding-conventions.md`(编码格式定义)
- `./assistants/rules/skill-conventions.md`(技能编写规范)
- `./assistants/rules/dashboard-conventions.md`(看板规范)

### 来源
- 由 `code-it` 在 `TASK-REQ-00044-00008` 中填充(2026-06-30)
- 上游追溯:`./assistants/V0.0.4/design/REQ-00044/RESULT.md` §2 模块拆分
