---
name: code-design
description: 概要设计。在需求文档的基础上,结合项目实际情况和编码规范,给出系统级的架构方案(模块划分、接口形态、关键流程、方案选型),作为后续拆任务、编码的依据;已存在概要设计时支持增量更新。需要在 `code-version` 之后、`code-plan` 之前调用,上游是 `code-require` 的产出。
---

# code-design — 概要设计(版本感知)

## 目标
回答"系统长什么样"。在 `code-require` 的需求基础上,结合**当前项目实际状况**(语言/框架/既有模块/既有接口),并**严格遵循 `./assistants/rules/` 下的项目级编码规范**,给出可被评审、可被 `code-plan` 进一步拆解的系统级架构方案。

## 适用场景
- 新模块/新服务的架构设计
- 跨模块的方案选型
- 重大重构的方案论证
- 需求变更后重新评估设计
- 项目级规范新增/修订后,需要重新校准已有设计

## 不适用
- 当前**没有激活的版本工作空间**(请先调 `code-version`)
- 需求尚未通过 `code-require` 形成 RESULT.md
- 已知明确的、只涉及单一文件/单一函数的修改
- 紧急线上修复(走 hotfix 流程)

## 工作目录约定(强制)

```
./assistants/
├── rules/ # 项目级规范,跨版本共享,本技能只读
└── <版本号>/
    ├── RESULT.md # 版本看板(本技能追加"概要设计清单" / "变更记录")
    ├── require/<需求编码>/RESULT.md # 上游,本技能只读
    └── design/<需求编码>/
        ├── RESULT.md # 本技能产出
        └── ... (过程文档)
```

- 路径以**当前工作目录(CWD)**为基准
- **本技能不修改** `./assistants/rules/`、`./assistants/<版本号>/require/<需求编码>/`、`./assistants/<版本号>/RESULT.md` 中非本技能负责的区段,只读

## 输入
- **需求编码**(必填):格式 `REQ-<后缀>`,默认 5 位纯数字
- **上游需求**:`./assistants/<版本号>/require/<需求编码>/RESULT.md`(必须存在)
- **项目级规范**:`./assistants/rules/` 下所有文件
- **当前项目代码**:CWD 下的所有源文件、配置文件、文档

## 输出
主产出物:`./assistants/<版本号>/design/<需求编码>/RESULT.md`
辅助过程文档:`materials-index.md` / `design-notes.md` / `module-breakdown.md` / `dependencies.md` / `related-designs.md` / `rule-compliance.md` / `clarifications.md`

## 工具使用约定
- 读激活版本:`Read "./assistants/.current-version"`
- 读需求:`Read "./assistants/<版本号>/require/<需求编码>/RESULT.md"`
- 读规范:`Glob "./assistants/rules/**/*"` 列出规范文件,逐一 `Read`
- 探项目结构:`Glob` / `Grep` / `Read`
- 与用户澄清:优先 `AskUserQuestion`;自然语言兜底
- 写文档:`Write`(首次)/ `Edit`(增量)

## 过程文档自适应判定

> 详见 references/common.md §4

## 修改文件定位的语义化约定

> 详见 references/common.md §5

## 命令行参数解析

> 详见 references/common.md §13

---

## 工作流程

### 步骤 0a — 拉取最新代码

> 详见 references/common.md §1

### 步骤 0b.0 — 调用上下文检测

> 详见 references/common.md §2

### 步骤 0b — 设计目标确认

> 详见 references/common.md §3

### 步骤 0 — 版本上下文检测(强制前置)
1. 读取 `./assistants/.current-version`
2. **文件不存在** → 立即停下,告知用户先调 `code-version`
3. 读取内容,记为 `<版本号>`,后续所有路径用 `assistants/<版本号>/...`
4. 验证 `./assistants/<版本号>/require/<需求编码>/RESULT.md` 存在

### 步骤 1 — 收集需求编码
- 若用户未提供,主动询问
- 校验 `./assistants/<版本号>/require/<需求编码>/RESULT.md` **必须存在**

### 步骤 2 — 定位 / 创建工作目录
- 检查 `./assistants/<版本号>/design/<需求编码>/` 是否存在,不存在 → `mkdir -p`

### 步骤 3 — 读取项目级规范

> 详见 references/common.md §6(步骤 3 通用流程)

### 步骤 4 — 读取需求分析结果
1. `Read "./assistants/<版本号>/require/<需求编码>/RESULT.md"`
2. 提取 FR / NFR / AC / 页面与交互 / 关联需求 / 待澄清
3. 预检规范 vs 需求冲突

### 步骤 5 — 探索项目结构与已有代码

> **语言检测**:详见 references/<语言>.md §1
> **通用流程**:详见 references/common.md §7

### 步骤 6 — 检查 RESULT.md 是否存在
- **不存在** → 首次设计(步骤 7A–15A)
- **存在** → 增量更新(步骤 7B–10B)

### 步骤 7A — 首次设计:架构方案构思

> 详见 references/common.md §8

### 步骤 8A — 澄清冲突与不确定项

> 详见 references/common.md §8

### 步骤 9A — 模块拆分

> 详见 references/common.md §8(模块拆分 5 列,下沉到 code-plan 的不展开)

### 步骤 10A — 接口与数据结构

> 详见 references/common.md §8(接口概要 + 数据结构,下沉到 code-plan 的不展开)

### 步骤 11A — 三方依赖评估

> 详见 references/common.md §8(4 项/依赖,下沉到 code-plan 的不展开)

### 步骤 12A — 检索关联概要设计
1. `Glob "./assistants/<版本号>/design/*/RESULT.md"`(同版本)
2. (可选,跨版本) `Glob "./assistants/*/design/*/RESULT.md"`
3. 在 `related-designs.md` 记录关联点

### 步骤 13A — 撰写 RESULT.md

> 详见 references/common.md §8(按 templates/design.md 结构,关键原则)

### 步骤 14A — 同步版本看板(强制)
1. 定位"概要设计清单"区段,追加/更新本设计行
2. 在"变更记录"追加设计新增条目

### 步骤 15A — 完善过程文档与汇报
- 收尾过程文档,向用户汇报核心架构决策、模块清单、关联设计、看板更新点

### 步骤 7B — 增量更新:识别变更源

> 详见 references/common.md §9(4 类变更源:需求侧/代码侧/规范侧/设计侧)

### 步骤 8B — 局部更新 RESULT.md

> 详见 references/common.md §9

### 步骤 9B — 重做规范自检

> 详见 references/common.md §9

### 步骤 10B — 同步版本看板与补充过程文档

> 详见 references/common.md §9

---

### 步骤 N — 末尾兜底提交

> 详见 references/common.md §10

---

## 衔接
- **下游**:`code-plan` 消费本阶段 `RESULT.md` 做实施计划
- **上游**:`code-version`(必须有激活版本);`code-require` 的 `RESULT.md`;项目级规范
- **横向**:通过 `related-designs.md` 与同版本下其他概要设计(可选:跨版本)形成引用网

## 不要做的事
- 不修改 `<本仓库>` 中除了 `./assistants` 目录中的其他代码文件
- 不要在没有 `./assistants/.current-version` 的情况下继续执行
- 不读上游 `RESULT.md` 就直接做设计
- 不读 `./assistants/rules/` 就直接做设计(在用户未授权跳过的情况下)
- 不探索项目现状就假设是"绿地项目"
- 在不读取现有 `RESULT.md` 的情况下重写整个文件
- 在材料不足以佐证时臆造接口签名或数据结构
- 静默违反规范(必须显式记录"用户授权的偏离"或"待澄清冲突")
- 一次性抛出所有澄清问题
- 修改 `./assistants/<版本号>/require/<需求编码>/` 或 `./assistants/rules/` 下的任何内容(只读)
- 修改 `./assistants/<版本号>/RESULT.md` 中"概要设计清单" / "变更记录"以外的区段