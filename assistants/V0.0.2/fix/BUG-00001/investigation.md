# 调查笔记 — BUG-00001

## 调查时间
2026-06-06 13:45

## 缺陷
code-auto 调用子技能时子技能仍会手动选择架构设计目标

## 初步根因分析

### 关键事实

1. **`code-auto` D-8 零修改契约保持**:`code-auto` 不向子技能传任何特殊参数(沿用 V0.0.1 既有 + REQ-00007 锁定)
2. **`code-auto` 期望"完全无人确认"**:用户使用 `/code-auto "<需求>"` 时,**所有** `AskUserQuestion` 应被自动选推荐项(沿用 code-auto §"子技能 prompt 模板"约束:"若 Claude Code 在执行过程中触发 `AskUserQuestion`,总选第一项(标注 (推荐) / (Recommended) 的项);不向用户提问")
3. **子技能侧**:`code-design` 步骤 0b 触发 `AskUserQuestion` 1-5 问(沿用 REQ-00011 / REQ-00018 既有),子技能**没有**"调用上下文检测"机制

### 根因

`code-auto` 的"自动选推荐项"约束**只在 `code-auto` 自己的 prompt 模板中声明**(子技能 prompt 模板注入),但子技能**本身**在执行 `AskUserQuestion` 时没有"我在被 `code-auto` 调用吗?"的检测逻辑。

这导致:
- `code-auto` 调用 `code-design` 时,`code-design` 不知道自己在被 `code-auto` 调用
- `code-design` 触发 `AskUserQuestion`,用户被迫手动选
- `code-auto` 的"完全无人确认"约束被破坏

### 候选修复方案

#### 方案 A:子技能自动检测(用户回答采纳)
- **核心思路**:子技能在步骤 0b 触发 `AskUserQuestion` 前,先检测"调用上下文"——若检测到自己在被 `code-auto` 调用,则**跳过** `AskUserQuestion`,直接采纳**默认值 / 推荐项**写入 RESULT.md
- **检测机制**(候选):
  - 方案 A1:检查 `process.env.CODE_AUTO_MODE` 环境变量 — 需要 `code-auto` 启动时设该变量(但 D-8 零修改契约规定 `code-auto` 不向子技能传任何特殊参数,设环境变量是否算"传特殊参数"有争议)
  - 方案 A2:检查 argv 是否含 `code-auto` 子串(可识别 `claude` CLI 调用栈)— 不稳定,依赖外部 CLI 实现
  - 方案 A3:检查 CWD 是否有 `code-auto` 留下的脏标记文件(例如 `./assistants/.code-auto-running` — `code-auto` 启动时 `touch` 该文件,退出时 `rm` — 沿用 "脏标记" 模式)— 子技能 Read 该文件存在即认为在被 code-auto 调用
  - 方案 A4:检查父进程命令行(需 `ps` 等)— Windows 兼容性差
- **推荐方案 A3**:沿用 V0.0.1 既有的"脏标记文件"模式(例如 V0.0.1 步骤 0a 拉取阶段的 `.git/index.lock` 检查类似思路)
- **优点**:与 D-8 零修改契约兼容(脏标记文件是"状态文件",**不**是"prompt 参数");跨平台兼容;稳定可靠
- **缺点**:脏标记文件需 `code-auto` 启动时 `touch` + 退出时 `rm`(子技能只 Read,既不 `touch` 也不 `rm`,职责清晰)

#### 方案 B:隐式环境变量
- **核心思路**:`code-auto` 启动时设 `process.env.CODE_AUTO_MODE=1`,子技能 Read 该环境变量
- **优点**:实现简单
- **缺点**:违反 D-8 零修改契约(设环境变量是"传特殊参数"的一种形式)

#### 方案 C:两者都实现
- 方案 A3(脏标记)作为默认,环境变量作为可覆盖(用于 CI / 批处理场景强制开启)

### 初步选定

**方案 A3**(脏标记文件)— 与 D-8 零修改契约兼容,跨平台兼容,稳定可靠。

**待 `code-plan BUG-00001` 详细规划 + `code-design BUG-00001` 概要设计后最终确认**。

## 涉及的文件清单(初步)

- **不修改**:`code-auto/SKILL.md`(D-8 零修改契约保持)
- **修改**:
  - `code-design/SKILL.md`(步骤 0b 增加"调用上下文检测"分支)
  - `code-plan/SKILL.md`(步骤 0b 增加"调用上下文检测"分支)
  - 其他 8 个 `code-*` 技能 SKILL.md(可能需要增加"调用上下文检测"分支,取决于具体问路场景)
  - `code-auto/SKILL.md`(**需要修改**:在步骤 0 + 步骤 7 末尾增加 `touch ./assistants/.code-auto-running` + `rm ./assistants/.code-auto-running` — 严格意义上违反 D-8 零修改契约,**需 D-8 修订**)

## 备注

- D-8 修订:从"完全不向子技能传任何特殊参数"修订为"不向子技能传 prompt 参数(状态文件除外)"
- 这是一个**D-8 契约修订**类缺陷,需要在 `code-plan BUG-00001` 阶段明确 D-8 修订内容
