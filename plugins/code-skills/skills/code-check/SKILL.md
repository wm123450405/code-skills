---
name: code-check
description: 代码检查与评审。系统化扫一遍某个需求(或缺陷)下的所有任务,对照需求、设计、编码规范发现缺陷,给出"必须改 / 建议改 / 可选"三档意见,并把必须改的拆成可派工的"审查改修"任务交给 `code-it` 去修。也可以接"缺陷编号"对单次缺陷修复做收尾检查。在 `code-it` 之后调用,常用于合入主干前的最后一道关卡。
---

# code-check — 代码检查(版本感知)

## 目标
在代码合并前**系统化发现缺陷**,把可执行、可追溯、可派工的评审意见转交给 `code-it` 处理,使代码质量与设计/需求/规范保持一致。

## 适用场景
- 任何进入主干/共享分支的 PR/MR
- 重大重构、关键路径变更、安全敏感改动
- 整个需求的代码全部就绪后做整体评审
- 单个任务的增量评审

## 不适用
- 当前**没有激活的版本工作空间**(请先调 `code-version`)
- 需求尚未在 PLAN.md 中拆分任务
- 任务的开发状态全部为 `待开始` 或 `已取消`

## 工作目录约定(强制)

```
./assistants/
├── rules/ # 项目级规范(跨版本,只读)
└── <版本号>/
    ├── RESULT.md # 版本看板(本技能追加区段)
    ├── require/<需求编号>/RESULT.md # 上游需求(只读)
    ├── design/<需求编号>/RESULT.md # 上游概要设计(只读)
    ├── plan/<需求编号>/RESULT.md # 上游详细设计(只读)
    ├── plan/<需求编号>/PLAN.md # 上游任务计划(只读,本技能追加新任务)
    ├── code/<任务编码>/RESULT.md # code-it 产出(只读)
    └── review/
        ├── <需求编号>/REVIEW-REPORT.md # 整体评审报告
        └── <新任务编码>/RESULT.md # 改修要求(给 code-it 消费)
```

## 输入
- **需求编码**(必填):格式 `REQ-<后缀>`;也支持 `BUG-<后缀>`
- **上游需求/设计/计划**:`require/` / `design/` / `plan/` 下对应文档
- **代码改修正文**:`code/<任务编码>/RESULT.md`
- **项目级规范**:`./assistants/rules/` 下所有文件
- **当前项目代码**:CWD 下的源文件(实际评审对象)

## 输出
主产出物:`review/<需求编号>/REVIEW-REPORT.md`(整体评审报告) + `review/<新任务编码>/RESULT.md`(改修要求)
辅助过程文档:`work-log.md` / `review-checklist-applied.md` / `findings-no-task.md`

## 工具使用约定
- 读上游:`Read` require/ / design/ / plan/ / code/
- 读规范:`Glob "./assistants/rules/**/*"` + `Read`
- 读源码:`Glob` / `Grep` / `Read`
- 写文档:`Write` / `Edit`
- 与用户澄清:优先 `AskUserQuestion`

## 过程文档自适应判定

> 详见 references/common.md §4

## 标题解析

> 详见 references/common.md §12

---

## 工作流程

### 步骤 0 — 版本上下文检测(强制前置)
1. 读取 `./assistants/.current-version`
2. **文件不存在** → 立即停下,告知用户先调 `code-version`

### 步骤 1 — 收集需求编码
- 校验 `require/<REQ>/RESULT.md` 与 `plan/<REQ>/PLAN.md` 都存在

### 步骤 1.5 — 模式选择
- 无参 → 整版本模式
- REQ-NNNNN → 单需求模式
- BUG-NNNNN → 单缺陷模式

> 整版本模式详见 references/common.md §3

### 步骤 2 — 定位 / 创建工作目录
- 检查 `review/<需求编号>/` 是否存在,不存在 → `mkdir -p`

### 步骤 3 — 读取项目级规范

> 详见 references/common.md §6

### 步骤 4 — 读取上游文档
依次:require/RESULT.md → design/RESULT.md → plan/RESULT.md → plan/PLAN.md

### 步骤 5 — 列出待评审任务
筛选:开发状态 ∈ {已完成, 进行中} ∧ 测试状态 ∈ {已运行-通过, 已运行-失败, 不适用}

### 步骤 6 — 读取代码改修正文
- 读 code/<TASK>/RESULT.md + unit-test-results.md
- 读 CWD 实际源码

### 步骤 7 — 加载评审清单
- 优先:`./assistants/rules/review-checklist.md`
- 兜底:本技能内置 `checklists/review-checklist.md`

### 步骤 8 — 逐任务评审

> 详见 references/common.md §8(14 维度:正确性/规范/设计/安全/性能/可维护性/测试/一致性/上下游/详设完整性/概设越界/行数比例/代码行数超标/过程文档适配性)

### 步骤 9 — 分类发现,决定是否派生
- 必须改 → 派生"审查改修"任务
- 建议改 → 询问用户
- 可选 → 记录到 findings-no-task.md

### 步骤 10 — 分配新任务编号并更新 PLAN.md

> 详见 references/common.md §10

### 步骤 11 — 撰写 review/RESULT.md

> 详见 references/common.md §11(按 templates/REVIEW-FIX.md 结构)

### 步骤 12 — 撰写整体 REVIEW-REPORT.md

> 详见 references/common.md §12(按 templates/REVIEW-REPORT.md 结构)

### 步骤 13 — 同步版本看板(强制)
1. 更新任务清单(追加派生任务)
2. 追加评审发现汇总
3. 追加派生任务记录
4. 追加缺陷清单(若有严重缺陷)
5. 追加变更记录

### 步骤 14 — 完善过程文档

### 步骤 15 — 汇报

---

## 评审维度速查

> 详见 references/common.md §14(P0-P3 优先级排序)

---

## 衔接
- **下游**:`code-it` 消费 `review/<新任务编码>/RESULT.md` 执行"审查改修"任务
- **上游**:`code-version`(必须);`code-it` 的产出 + 需求/设计/计划文档

## 不要做的事
- 不要在没有 `./assistants/.current-version` 的情况下继续执行
- 不读上游文档就直接评审
- 评审时改 CWD 下的源码(那是 code-it 的工作)
- 评审时改 plan/RESULT.md / code/RESULT.md
- 把发现的"建议改"全部强派生为任务(询问用户)
- 在 PLAN.md 中修改除"追加新任务"之外的任何内容
- 跳过 `./assistants/rules/review-checklist.md`(若存在)而只用内置清单
- 给出模糊批评(必须给出可执行建议)
- 把 review/RESULT.md 写成"建议改用更安全的写法"这种程度(必须具体到文件+改修方案)
- 修改 `./assistants/<版本号>/RESULT.md` 中非本技能负责的区段