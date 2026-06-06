# 模块详细化 — REQ-00018
更新时间:2026-06-06 13:15
版本:V0.0.2
需求编码:REQ-00018

## 模块:`code-version` 步骤 7

- **路径**:`plugins/code-skills/skills/code-version/SKILL.md` §工作流程 段后 / §看板字段约定 段前
- **状态**:修改既有(沿用 REQ-00010 增量追加模式)
- **关键类/函数**:
  - `step7_syncCwdVersionFiles(newVersion: string, cwd: string): void`
  - `parseVersionField(filename: string, content: string): string | null`
  - `replaceVersionField(filename: string, content: string, newVersion: string): string`
- **调用顺序**:
  1. `code-version` 步骤 6 完成后调用
  2. 步骤 7 → 解析 argv(0 CLI 参数,本需求) → Glob 6 类 → 0 命中处理 → 逐文件处理
  3. 每文件:`go.mod` 特殊处理 → `parseVersionField` → `replaceVersionField` → 写回文件
- **状态归属**:既有 `code-version` 技能
- **与概要设计的对应**:§3 核心设计决策
- **符合的规范**:skill-conventions §规则 1 / module-conventions §规则 1

## 子小节结构(7 个)

```
## 步骤 7 — CWD 描述文件版本号同步(REQ-00018 新增)

### 7.1 目标
[1 段说明步骤 7 做什么 / 触发条件 / 退出码语义]

### 7.2 触发条件
[步骤 3 决定激活此版本后,选 A/B/C 触发]

### 7.3 算法
[7 步伪代码 + 6 类描述文件解析契约]

### 7.4 通过条件
[成功 / 0 命中 / 失败不阻断]

### 7.5 屏幕输出契约
[5 类格式]

### 7.6 边界与异常
[E-1 ~ E-8 共 8 个]

### 7.7 性能
[单文件 ~1 秒;monorepo 10 个 ~5 秒]
```

## 状态机(7 步)

```
[code-version 步骤 1-6 完成]
  ↓
[7.1 解析 argv(本需求 0 CLI 参数)]
  ↓
[7.2 Glob 6 类描述文件]
  ↓
[7.3 0 命中?]
  ├─ yes → 屏幕输出 ⚠ → 退出 0
  └─ no → [7.4 对每命中文件]
           ├─ go.mod → 屏幕输出 ⚠ → 继续
           ├─ 解析失败 → 屏幕输出 ⚠ → 继续
           ├─ 缺版本号 → 屏幕输出 ⚠ → 继续
           ├─ 成功 → Edit + 屏幕输出 ✓ → 继续
           └─ Edit 失败 → 屏幕输出 ⚠ → 继续
  ↓
[退出 0](NFR-8)
```

## 与概要设计 §3.1 / §3.3 的对应

- §3.1 受影响文件清单:本模块 = `plugins/code-skills/skills/code-version/SKILL.md`(状态 = 修改既有)
- §3.2 步骤 7 子小节结构:7 子节(本设计 §3.1 详)
- §3.3 关键变更:锚点 = "## 工作流程" 段后 / "## 看板字段约定" 段前
