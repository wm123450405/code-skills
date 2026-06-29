---
name: code-it
description: 开发编码。按任务编码取一条任务,读它的详细设计并按规范写代码,保证软件能编译、能启动运行;项目可测时按需写并跑通单元测试。也支持接"缺陷编号"走缺陷修复实施路径,把缺陷从"修复规划中"推进到"修复完成"。在 `code-plan` 之后、`code-check` 之前调用;`code-check` 派生的"审查改修"任务也由本技能执行。
---

# code-it — 开发编码(版本感知)

## 目标
按 `PLAN.md` 中的一条具体任务,产出**可工作、可编译、可启动运行**的代码。保持与详细设计/概要设计/需求的一致性,不偏离任务边界。

## 唯一允许的生产代码改动场景
本技能是本技能库中**唯一**被允许修改 `<本仓库>` 中除了 `./assistants` 目录中的其他代码文件的技能。

## 适用场景
- 任何按 `PLAN.md` 单条任务执行的编码工作
- 重构或特性开发的具体落地
- Bug 修复的具体落地
- `code-check` 派生的"审查改修"任务的执行

## 不适用
- 当前**没有激活的版本工作空间**(请先调 `code-version`)
- 任务尚未在 `PLAN.md` 中存在
- 跨多任务的批量改动(应拆分为多次本技能调用)

## 工作目录约定(强制)

```
./assistants/
├── rules/ # 项目级规范(跨版本,只读)
└── <版本号>/
    ├── RESULT.md # 版本看板(本技能追加"任务清单" / "变更记录")
    ├── require/<需求编号>/RESULT.md # 上游需求(只读)
    ├── design/<需求编号>/RESULT.md # 上游概要设计(只读)
    ├── plan/<需求编号>/RESULT.md # 上游详细设计(只读)
    ├── plan/<需求编号>/PLAN.md # 上游任务计划(只读,本技能更新本任务状态)
    └── code/<任务编码>/ # 本技能产出
        ├── RESULT.md # 改修总结
        ├── work-log.md / compile-and-run.md / deviations.md / test-results.md
```

## 输入
- **任务编码**(必填):格式 `TASK-(REQ|BUG)-<父级>-<任务序号>`
- **上游详细设计**:`plan/<需求编号>/RESULT.md`(触发/来源=审查改修时不读)
- **上游任务计划**:`plan/<需求编号>/PLAN.md`(必须存在)
- **审查改修输入**(仅当触发/来源=审查改修):`review/<任务编码>/RESULT.md`
- **项目级规范**:`./assistants/rules/` 下所有文件
- **当前项目代码**:CWD 下的源文件

## 输出
主产出物:`code/<任务编码>/RESULT.md`(改修总结) + CWD 下的实际代码变更
辅助过程文档:`work-log.md` / `compile-and-run.md` / `deviations.md` / `test-results.md`

## 工具使用约定
- 改代码:`Edit` / `Write`(对 CWD 下源码)
- 读设计/规范/计划:`Read`;探项目代码:`Glob` / `Grep` / `Read`
- 编译/运行/测试:`Bash`
- 与用户澄清:优先 `AskUserQuestion`;只在无法自行判断时用

## 修改文件前必须重读最新内容(强制)

> 详见 references/common.md §5

## 过程文档自适应判定

> 详见 references/common.md §4

## 标题解析

> 详见 references/common.md §12

---

## 工作流程

### 步骤 0a — 前置任务守卫

> 详见 references/common.md §1

### 步骤 0 — 版本上下文检测(强制前置)
1. 读取 `./assistants/.current-version`
2. **文件不存在** → 立即停下,告知用户先调 `code-version`

### 步骤 1 — 收集并解析输入 ID
- 匹配 `TASK-` → 任务分支(步骤 2-16)
- 匹配 `BUG-` → 缺陷分支(步骤 17-25)

### 步骤 2 — 校验任务存在
- 读取 `PLAN.md`,在"任务总览"中查找本任务编号

### 步骤 3 — 定位 / 创建工作目录
- 检查 `code/<任务编码>/` 是否存在,不存在 → `mkdir -p`

### 步骤 4 — 读取项目级规范

> 详见 references/common.md §6

### 步骤 5 — 读取上游文档
- 触发/来源 = 审查改修 → 读 review/<TASK>/RESULT.md
- 其他触发/来源 → 读 plan/<REQ>/RESULT.md(详细设计)

### 步骤 6 — 探索项目代码

> 详见 references/common.md §7

### 步骤 7 — 处理任务前置依赖与状态
- 待开始 → 推进为进行中,更新 PLAN.md
- 进行中/阻塞 → 继续
- 已完成 → 询问是否重做
- 已取消 → 错误

### 步骤 8 — 实施开发

> 详见 references/common.md §8(通用编码原则;审查改修任务特殊规则)

### 步骤 8a — 项目可测性守卫

> 详见 references/common.md §9(7 项检查;守卫通过/不通过流程)

### 步骤 8.5 — 按需写单测

> 详见 references/common.md §10(3 类自动判定;测试框架检测;错误修复循环)

### 步骤 9 — 编译验证

> 详见 references/<语言>.md §2(构建命令检测)
> 详见 references/common.md §11

### 步骤 10 — 启动运行验证

> 详见 references/<语言>.md §4(运行命令检测)
> 详见 references/common.md §11

### 步骤 11 — 测试(若适用)

> 详见 references/<语言>.md §3(测试框架识别)
> 详见 references/common.md §11

### 步骤 12 — 错误修复循环

> 详见 references/common.md §12(最多连续失败 5 次)

### 步骤 13 — 撰写 RESULT.md(改修总结)

> 详见 references/common.md §13

### 步骤 14 — 更新 PLAN.md(标记完成)
- 状态:进行中 → 已完成,填入完成时间和提交哈希

### 步骤 15 — 同步版本看板(强制)
- 更新"任务清单"中本任务行,追加"变更记录"

### 步骤 16 — 完善过程文档与汇报

---

## 缺陷分支

> 详见 references/common.md §14(步骤 17-25)

---

## 衔接
- **下游**:`code-check` 评审;后续任务的 `code-it`
- **上游**:`code-version`(必须);`code-plan` 的 `PLAN.md` / `RESULT.md`;项目级规范

## 不要做的事
- 不要在没有 `./assistants/.current-version` 的情况下继续执行
- 不读上游文档就直接动手
- 在编译/启动/测试有错误的情况下标记任务完成
- 用绕过手段规避错误
- 跨任务做未授权的改动
- 修改 `./assistants/rules/` / `require/` / `design/` / `plan/RESULT.md` 下的任何内容
- 修改 `PLAN.md` 中除本任务状态/完成字段/变更记录之外的任何内容