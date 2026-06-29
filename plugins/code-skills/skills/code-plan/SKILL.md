---
name: code-plan
description: 详细设计与编码计划。把概要设计落到"可以直接编码"的颗粒度:补齐算法、数据结构、接口细节,并把整项工作拆成一条条可独立追踪的任务,交给 `code-it` 逐条执行;支持增量更新已完成任务的测试状态。也支持接"缺陷编号"走修复方案路径。
---

# code-plan — 详细设计 & 编码计划(版本感知)

## 目标
把概要设计"系统长什么样"落地为**两件事**:
1. **详细设计**:`RESULT.md` —— 给出可直接编码的算法逻辑、伪代码、完整数据结构变化、接口入参/出参/异常/安全细节
2. **编码计划**:`PLAN.md` —— 把详细设计拆分为可独立执行、可追踪状态的任务

## 适用场景
- 跨多文件/多模块的改动
- 需要多人协作或分阶段交付的任务
- 任何在动手编码前希望降低返工成本的场景

## 不适用
- 当前**没有激活的版本工作空间**(请先调 `code-version`)
- 需求或概要设计尚未就绪
- 已知明确的、只涉及单一文件/单一函数的修改
- 紧急线上修复(走 hotfix 流程)

## 工作目录约定(强制)

```
./assistants/
├── rules/ # 项目级规范,跨版本共享,只读
└── <版本号>/
    ├── RESULT.md # 版本看板(本技能追加区段)
    ├── require/<需求编码>/RESULT.md # 上游需求,只读
    ├── design/<需求编码>/RESULT.md # 上游概要设计,只读
    └── plan/<需求编码>/
        ├── RESULT.md # 详细设计
        ├── PLAN.md # 编码计划
        └── ... (过程文档)
```

- 路径以**当前工作目录(CWD)**为基准
- **本技能不修改** `rules/`、`<版本号>/require/<编号>/`、`<版本号>/design/<编号>/` 下任何内容,只读
- `RESULT.md` 与 `PLAN.md` **必须**保持一致

## 输入
- **需求编码**(必填):格式 `REQ-<后缀>`;缺陷编码 `BUG-<后缀>`
- **上游需求**:`./assistants/<版本号>/require/<需求编码>/RESULT.md`(必须存在)
- **上游概要设计**:`./assistants/<版本号>/design/<需求编码>/RESULT.md`(必须存在)
- **项目级规范**:`./assistants/rules/` 下所有文件
- **当前项目代码**:CWD 下的源文件

## 输出
主产出物:`RESULT.md`(详细设计) + `PLAN.md`(编码计划)
辅助过程文档:`materials-index.md` / `design-notes.md` / `module-details.md` / `interface-specs.md` / `data-changes.md` / `risk-analysis.md` / `rule-compliance.md` / `clarifications.md`

## 工具使用约定
- 读激活版本:`Read "./assistants/.current-version"`
- 读上游:`Read` require/ + design/
- 读规范:`Glob "./assistants/rules/**/*"` + `Read`
- 探项目代码:`Glob` / `Grep` / `Read`
- 写文档:`Write`(首次)/ `Edit`(增量)
- 与用户澄清:优先 `AskUserQuestion`;自然语言兜底

## 过程文档自适应判定

> 详见 references/common.md §4

## 标题解析

> 详见 references/common.md §12

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
3. 验证 `require/<REQ>/RESULT.md` 与 `design/<REQ>/RESULT.md` 都存在

### 步骤 1 — 收集输入 ID 并判定路径
- 匹配 `REQ-` → 需求分支(步骤 2-18A)
- 匹配 `BUG-` → 缺陷分支(步骤 19-28)

### 步骤 2 — 定位 / 创建工作目录
- 检查 `./assistants/<版本号>/plan/<需求编码>/` 是否存在,不存在 → `mkdir -p`

### 步骤 3 — 读取项目级规范

> 详见 references/common.md §6

### 步骤 4 — 读取上游需求与概要设计
1. `Read require/<REQ>/RESULT.md` —— 提取 FR / NFR / AC
2. `Read design/<REQ>/RESULT.md` —— 提取模块拆分 / 接口概要 / 数据结构
3. 预检规范 vs 设计冲突

### 步骤 5 — 探索项目代码

> 详见 references/common.md §7

### 步骤 6 — 检查 RESULT.md / PLAN.md 是否存在
- 都不存在 → 首次设计(7A–18A)
- 都存在 → 增量更新(7B–13B)

### 步骤 7A — 首次:详细化设计

> 详见 references/common.md §8(逐模块展开:类/函数/算法/数据结构/接口/风险)

### 步骤 8A — 澄清冲突与不确定项

> 详见 references/common.md §8

### 步骤 9A — 测试策略推导

> 详见 references/common.md §8

### 步骤 10A — 任务拆分

> 详见 references/common.md §9(核心原则:按功能点拆分;架构任务触发条件;双状态字段;触发/来源字段;按设计目标调整粒度)

### 步骤 11A — 任务依赖与里程碑
- 明确每条任务的前置任务;识别里程碑;用 Mermaid 绘制任务依赖图

### 步骤 12A — 检索关联编码计划
- `Glob "./assistants/<版本号>/plan/*/PLAN.md"`(同版本)

### 步骤 13A — 与用户对齐计划(可选)

### 步骤 14A — 撰写 RESULT.md

> 详见 references/common.md §10(14 章节结构)

### 步骤 15A — 撰写 PLAN.md

> 详见 references/common.md §10(8 章节结构)

### 步骤 16A — 同步版本看板(强制)
1. 更新"详细设计与任务计划汇总" 2. 追加"任务清单" 3. 追加"里程碑" 4. 追加"变更记录"

### 步骤 17A — 交叉验证
- RESULT.md 与 PLAN.md 互相校验

### 步骤 18A — 完善过程文档与汇报

### 步骤 7B-13B — 增量更新

> 详见 references/common.md §11

### 步骤 7C — 仅补 PLAN.md

> 详见 references/common.md §11

---

## 缺陷分支

> 详见 references/common.md §12

---

### 步骤 N — 末尾兜底提交

> 详见 references/common.md §13

---

## 衔接
- **下游**:`code-it` 按 `PLAN.md` 执行;`code-check` 评审
- **上游**:`code-version`(必须);`code-require`/`code-design` 的 RESULT.md;项目级规范

## 不要做的事
- 不修改 `<本仓库>` 中除了 `./assistants` 目录中的其他代码文件
- 不要在没有 `./assistants/.current-version` 的情况下继续执行
- 不读上游就直接做规划
- 在不读取现有 RESULT.md/PLAN.md 的情况下重写整个文件
- 重新分配已有任务的编号
- 修改已完成任务的描述或状态(只能追加"修改类"任务)
- 让 RESULT.md 与 PLAN.md 不一致
- 静默违反规范
- 一次性抛出所有澄清问题
- 修改 `./assistants/<版本号>/require/<编号>/`、`design/<编号>/`、`rules/` 下的任何内容(只读)
- 修改 `./assistants/<版本号>/RESULT.md` 中非本技能负责的区段