# 设计笔记 — REQ-00001
更新时间:2026-06-03 20:25
版本:V0.0.1

## 0. 设计范围与定位

**本需求不是"新功能",而是"标识层 breaking change"**。无新增模块、无新增依赖、无新增接口。设计核心是:
1. **编辑策略**:精确 Edit vs 整文件 Write
2. **提交粒度**:单 commit vs 多 commit
3. **验证范围**:Grep 关键短语 + 字段逐项核对
4. **变更传播路径**:从 `.claude-plugin/marketplace.json` → 文档层 → 用户安装命令

## 1. 关键设计问题清单

### Q-1:用什么工具修改 marketplace.json?
- **候选 A**:`Edit` 工具,精确定位根 `name` 行替换
  - ✅ 风险低,只动 1 行字符串
  - ✅ 保持文件其它字段(注释、字段顺序、缩进)完全不变
  - ✅ diff 最小化,便于 code-review
- **候选 B**:`Write` 工具,整文件重写
  - ❌ 风险高,易引入格式漂移(JSON 末尾空行、字段顺序)
  - ❌ diff 含大量无关行
- **选定 A**(理由:FR-1 主流程 §3 显式推荐;`marketplace-protocol.md §规则 1` 不允许未知字段,Edit 避免误增)
- **依据规范**:`marketplace-protocol.md §规则 1`(不引入未知字段)

### Q-2:如何修改 README.md / README.en.md?
- **候选 A**:`Edit` 工具,逐处精确替换
  - ✅ 与 Q-1 同样的"diff 最小化"收益
  - ✅ 保留 README 其它无关内容(对仗结构、版本说明、贡献指南)
- **候选 B**:`Write` 工具,整文件重写
  - ❌ 风险高,易破坏 doc-conventions §规则 1 要求的"中英结构对仗"
- **选定 A**
- **依据规范**:`doc-conventions.md §规则 1`(中英结构对仗 + 同次提交同步)

### Q-3:CLAUDE.md 是否需要改?
- **候选 A**:假定无 marketplace name 引用,跳过
  - ❌ 与 FR-5 显式要求"Grep 检索"不符;风险:遗漏隐藏引用
- **候选 B**:`code-it` 阶段 Grep `code-skills@code-skills`、`marketplace name` 等关键短语;若无命中,在偏差日志注明"已核查,无需修改"
  - ✅ 与 FR-5 主流程完全一致
  - ✅ 即使 0 命中,也留下审计痕迹
- **选定 B**
- **依据规范**:无直接对应规范(纯需求驱动);但符合"可观测性 / 审计"原则(NFR-4)

### Q-4:所有变更是否必须在 1 个 commit 内?
- **候选 A**:4 个文件(1 JSON + 2 README + 1 CLAUDE?)分 4 个 commit
  - ❌ 触发 doc-conventions §规则 1 违规("中英 README 必须同次提交")
  - ❌ 引入中间态(改了 JSON 但 README 未改 → install 命令指向不存在的 marketplace)
- **候选 B**:全部文件在 1 个 commit 内
  - ✅ 满足 doc-conventions §规则 1
  - ✅ 满足 NFR-3(文档同步合规)
  - ✅ git revert 友好(整个改名可 1 个 commit 撤销)
- **选定 B**
- **依据规范**:`doc-conventions.md §规则 1`(同次提交)

### Q-5:marketplace.json 的 `version` 是否升到 1.1.0?
- **候选 A**:保持 1.0.0(REQU 文档默认)
  - ✅ 不破坏 `plugins[].version` 同步约束(marketplace-protocol §规则 1.3)
  - ⚠ 但 `version` 未标识 breaking change,违反"semver 语义化"
- **候选 B**:升到 1.1.0
  - ✅ semver 标识 breaking change
  - ❌ 触发 `plugins[].version` 是否同步升的次生问题(本仓库只有一个 plugin,可保持 1.0.0)
- **现状**:Q-5 待用户澄清,REQU 文档默认 (A)。**本设计采用默认 (A)**,并在 `clarifications.md` 记录"Q-5 未答复,采用默认"
- **依据规范**:`marketplace-protocol.md §规则 1.3`(plugin 同步约束,本需求保持)

### Q-6:README 是否加"老用户迁移指引"小节?
- **候选 A**:不加(REQU 文档默认)
  - ✅ 范围最小化(NFR-5)
  - ⚠ 老用户需自行查阅 commit message / 文档
- **候选 B**:加(NFR-1 breaking change 提示)
  - ✅ 用户体验更友好
  - ❌ 触发 doc-conventions §规则 1 同步(中英都加)
- **现状**:Q-4 待用户澄清,REQU 文档默认 (A)。**本设计采用默认 (A)**,并在 `clarifications.md` 记录"Q-4 未答复,采用默认"
- **依据规范**:`doc-conventions.md §规则 1`(若加,需中英同步)

### Q-7:`marketplace.json` 的 `description` 是否改?
- **候选 A**:不改(REQU 文档默认,基于 Q-2 澄清"仅根 name")
  - ✅ 范围最小化
- **候选 B**:改(如加"marketplace container"等说明)
  - ❌ 超出 Q-2 选项 A 显式范围
- **现状**:Q-3 待用户澄清,REQU 文档默认 (A)。**本设计采用默认 (A)**
- **依据规范**:无直接对应规范;遵循"最小化"原则(NFR-5)

## 2. 架构图(数据流)

### 2.1 组件图

```
┌──────────────────────────────────────────────────────────────┐
│  marketplace 仓库根 (code-skills/)                           │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ .claude-plugin/marketplace.json                        │  │
│  │ ┌──────────────────────────────────────────────────┐   │  │
│  │ │ $schema  : "https://anthropic.com/...schema"     │   │  │
│  │ │ name     : "code-skills" → "code-skills-        │   │  │
│  │ │            marketplace"    [本需求改]            │   │  │
│  │ │ version  : "1.0.0"                               │   │  │
│  │ │ owner    : { name: "code-skills" }               │   │  │
│  │ │ plugins[]:                                       │   │  │
│  │ │   [0] name: "code-skills" ← [本需求禁止改]      │   │  │
│  │ │       version: "1.0.0"                           │   │  │
│  │ │       source: "./plugins/code-skills"            │   │  │
│  │ │       skills: [...10 个 code-* 技能...]          │   │  │
│  │ └──────────────────────────────────────────────────┘   │  │
│  └────────────────────────────────────────────────────────┘  │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ plugins/code-skills/                                   │  │
│  │  ├── .claude-plugin/plugin.json [本需求禁止改]         │  │
│  │  ├── README.md              [本需求改]                 │  │
│  │  ├── README.en.md           [本需求改,中英同次提交]   │  │
│  │  ├── CLAUDE.md              [本需求 Grep 决定]        │  │
│  │  └── skills/<10 技能>...   [本需求禁止改]             │  │
│  └────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

### 2.2 变更传播路径

```
  .claude-plugin/marketplace.json (根 name 改)
       │
       ├─→ 仓库内文档传播 (本需求同步)
       │     ├─→ plugins/code-skills/README.md (中)
       │     │     • install 命令:`code-skills@code-skills-marketplace`
       │     │     • "marketplace name" 解释段
       │     └─→ plugins/code-skills/README.en.md (英,同次提交)
       │           • 同上
       │
       └─→ 仓库外影响 (不在本需求范围)
             └─→ 已有下游用户
                   • 已注册 `code-skills` → 需 `marketplace remove` + 重新 `add`
```

### 2.3 验证路径

```
1. JSON 字段逐项核对 (.claude-plugin/marketplace.json)
   └─→ grep "name" 文件 → 仅 1 行变更(根 name);plugins[].name 保持
2. README 同步验证
   └─→ grep "code-skills@code-skills" README.md → 0 命中
   └─→ grep "code-skills@code-skills" README.en.md → 0 命中
3. CLAUDE.md 同步验证
   └─→ grep "code-skills@code-skills" CLAUDE.md → 0 命中 或 已改
4. 全局零残留验证
   └─→ grep "code-skills@code-skills" 全仓库 → 仅命中本需求工作目录
5. 不变量验证
   └─→ plugins/code-skills/ 目录名保持
   └─→ git remote -v 无重命名
   └─→ .claude-plugin/marketplace.json 其它字段未变
```

## 3. 关键不变量(本需求严禁破坏)

| 不变量 | 来源 | 验证方式 |
| --- | --- | --- |
| `marketplace.json` 的 `plugins[].name` 保持 `"code-skills"` | `marketplace-protocol.md §规则 1.3` | grep "name" 文件 |
| `plugin.json` 的 `name` 保持 `"code-skills"` | `marketplace-protocol.md §规则 1.3` | grep "name" 文件 |
| `plugins/code-skills/` 目录名保持 | NFR-2 / FR-2 | `ls plugins/` |
| git 远端仓库名保持 | NFR-2 / FR-2 | `git remote -v` |
| `$schema` 字段值不变 | `marketplace-protocol.md §规则 1.1` | grep "$schema" |
| `version` 字段(根)值不变(默认) | Q-5 默认 (A) | grep "version" |
| 全部 SKILL.md / 模板 / 规范文件 / V0.0.0 不变 | FR-7 | `git diff --stat` |

## 4. 备选方案被否决的理由

| 备选方案 | 否决理由 |
| --- | --- |
| 整文件 Write marketplace.json | 风险高、易破坏 JSON 格式 |
| 4 个文件分 4 个 commit | 触发 doc-conventions §规则 1 违规;引入中间态 |
| 改 `plugins[].name` / `plugins/code-skills/` 目录名 | FR-2 显式禁止,触发 breaking change 升级 |
| 升 `version` 到 1.1.0 (Q-5 候选 B) | Q-5 未答复,采用默认 (A) 保持 1.0.0 |
| 加 README 迁移指引小节 (Q-4 候选 B) | Q-4 未答复,采用默认 (A) 不加 |
| 改 marketplace.json `description` (Q-3 候选 B) | Q-3 未答复,采用默认 (A) 不改 |
