# 模块详细化 — REQ-00015
更新时间:2026-06-06 09:10
版本:V0.0.2

## 模块:`code-merge` 技能入口

### 关键类/函数
本技能**无类/函数**(纯 SKILL.md 文档,Claude Code 模型层在用户调用时按需解释执行)。
SKILL.md 内部**描述**工作流 + 算法 + 边界,**不嵌入**具体 git 命令模板(沿用 NFR-9)。

### 调用顺序
用户调用顺序:
```
/code-merge
  ↓
Claude Code 解释 SKILL.md
  ↓
步骤 0: 读 .current-version (V0.0.2)
  ↓
FR-1 → FR-2 → FR-3 → FR-4(条件)→ FR-5 → FR-6 → FR-7 → FR-8
  ↓
退出码 0 / 非 0
```

### 状态归属
- **本技能内部状态**:无(纯 CLI 操作,无持久化)
- **git 状态**:由 git 自身管理(worktree 模式 + 当前分支)
- **看板状态**:FR-6 复用既有 5 区段(读 / 校验,**不**修改)

### 与概要设计的对应
- 概要设计 §3.1~§3.8 → 本模块 T-001 SKILL.md 12 章节正文
- 概要设计 §4 状态机 → 本模块 T-001 SKILL.md §工作流章节 + 状态机 Mermaid
- 概要设计 §5 接口 → 本模块 T-001 SKILL.md §输入 / §输出
- 概要设计 §6 自检 → 本模块 T-005 收尾

### 符合的规范
- ✅ `skill-conventions.md §规则 1`:frontmatter 必含 `name: code-merge` + `description: <完整描述>`
- ✅ `module-conventions.md §规则 1`:无新增子目录(SKILL.md 直接放技能根)
- ✅ `marketplace-protocol.md §规则 1`:`marketplace.json` 追加 `./skills/code-merge`
- ✅ `encoding-conventions.md §规则 1+3`:任务编号解析复用
- ✅ `commit-conventions.md`:沿用 V0.0.2 既有 `chore(<scope>): ...`
- ✅ `dashboard-conventions.md §规则 1`:0 触发 3 文件同步

### 关键类比(与既有 11 个 `code-*`)
- **风格**:`code-auto/SKILL.md`(574 行,7 步状态机) → 本模块 ~700 行,8 FR 状态机
- **状态机**:`code-require` Mermaid 风格 → 本模块沿用
- **边界异常**:`code-publish` E-M1~Mxx 风格 → 本模块 E-M1~M12
- **报告格式**:`code-auto` `[code-auto]` 前缀 + `=== xxx 启动 ===` → 本模块 `[code-merge]` 前缀 + `=== code-merge 启动 ===`
