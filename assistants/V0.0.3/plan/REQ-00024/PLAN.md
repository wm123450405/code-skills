# 编码计划 — REQ-00024

- 需求编码:REQ-00024
- 计划标题:`code-auto` 步骤 1 改造:用路径感知替代 `from` 关键字
- 状态:待 code-it 实施
- 所属版本:V0.0.3
- 整体设计目标:`--balanced`(从 `design/REQ-00024/RESULT.md` 沿用)
- 维度优先级:功能性=中(沿用)
- 任务总数:**1**(纯文档型,测试状态=不适用)

---

## 1. 任务总览

| 任务编号 | 需求 | 类型 | 触发/来源 | 标题 | 开发状态 | 测试状态 | 涉及文件 | 关联任务 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TASK-REQ-00024-00001 | REQ-00024 | 修改 | 详细设计 | [修改] code-auto 步骤 1:用路径感知替代 from 关键字 | 已完成 | 不适用 | plugins/code-skills/skills/code-auto/SKILL.md §输入与输出 + §工作流步骤 步骤 1 + §边界与异常 | REQ-00024 |

**统计**:
- 总任务数:1
- 真正可发布数(开发=已完成 ∧ 测试∈{已运行-通过, 不适用}):1
- 开发已完成 / 未完成:1 / 0
- 测试已通过 / 不适用 / 未编写:0 / 1 / 0
- 任务颗粒度:1 任务 = 1 SKILL.md 改造(沿用 `--balanced` 默认粒度;功能性=中,**不**展开为多任务)
- 0 派生"更新看板"任务(沿用 REQ-00017 强约束)

---

## 2. 任务详情

### 2.1 TASK-REQ-00024-00001 · [修改] code-auto 步骤 1:用路径感知替代 from 关键字

- **目标**:修改 `code-auto/SKILL.md`,将步骤 1 的"正则匹配 `^from REQ-\d{5}$` 关键字"逻辑改造为"路径感知判定"(`Bash: test -d <path>` 文件/文件夹存在性)
- **涉及文件**:
  - `plugins/code-skills/skills/code-auto/SKILL.md > §输入与输出(模式识别子表)`
  - `plugins/code_skills/skills/code-auto/SKILL.md > §工作流步骤 步骤 1`
  - `plugins/code_skills/skills/code-auto/SKILL.md > §边界与异常`
- **关键变更**(3 处):
  1. **§输入与输出**:
     - 删除:模式 A / 模式 B 二元划分 + 关键字 `from` 解析规则
     - 替换为:4 模式定义(`req-skip-require` / `req-run-require` / `fix-skip-require` / `req-content`)
  2. **§工作流步骤 步骤 1**:
     - 删除:正则 `^from REQ-\d{5}(\s+(.*))?$` 匹配逻辑
     - 替换为:路径感知判定(2-3 次 `Bash: test -d` 命令,详见 `plan/REQ-00024/RESULT.md §算法 1`)
     - 屏显契约:3 行"路径感知判定"前缀(沿用既有 3 行风格)
  3. **§边界与异常**:
     - 删除:E-15 / E-16 / E-17
     - 新增:E-18 / E-19
- **边界与异常**:
  - frontmatter(`name: code-auto` + `description`)字节级保留(INV-16 强约束)
  - 既有 6 步状态机(步骤 0a → 0 → 1 → 2 → 3 → 4 → 5 → 6 → 7)不变
  - 既有 6 子技能调用表不变
  - 既有 `auto-report.md` 模板字节级不变
- **验证手段**:
  - **AC-1**:4 种输入场景(`/code-auto REQ-99999` 第 1/2 次 / `/code-auto BUG-99999` / `/code-auto 自然语言`)屏显模式名与判定一致
  - **AC-2**:`/code-auto from REQ-00020` 整串视为需求内容(破坏性变更验证)
  - **AC-3**:屏显 3 行前缀与契约一致
  - **AC-4**:退出码 5 不再触发;3 / 4 沿用
  - **AC-5**:`git diff` 校验其他 9 个 `code-*` SKILL.md 字节级不变
  - **AC-6**:6 步状态机 + 6 任务循环 + 评审循环均不变
  - **AC-7**:`auto-report.md` 模板字节级不变
  - **AC-8**:文档中"模式 A / 模式 B"字面引用清理(除历史变更记录外)
- **回退方式**:`git checkout HEAD~1 -- plugins/code_skills/skills/code-auto/SKILL.md`(单文件回退)

---

## 3. 任务依赖图

```
[T-1: code-auto/SKILL.md 改造]
```

- **说明**:单任务,无依赖
- **Mermaid 源**:
  ```mermaid
  graph LR
    T1[T-1: code-auto/SKILL.md 改造]
  ```

---

## 4. 里程碑

- **M-REQ-00024**:REQ-00024 全部任务(本计划)
  - 完成定义:1 任务开发状态=已完成 ∧ 测试状态=不适用 ∧ AC-1~8 全部通过
  - 状态:待开始(本计划)
  - 计划时间:2026-06-07
  - 实际完成:—

---

## 5. 状态管理规则

- **双状态字段**(本任务):开发状态 + 测试状态
- **本计划初始化**:
  - T-1:开发状态=`待开始`(初值),测试状态=`不适用`(纯文档任务)
- **测试状态推进路径**:纯文档任务**不**会推到"已运行-通过",**只**有 1 种终态 = `不适用`
- **真正可发布判定**:开发状态=已完成 ∧ 测试状态=不适用

---

## 6. 关联计划

| 关联项 | 路径 | 关联方式 |
| --- | --- | --- |
| 需求 | `require/REQ-00024/RESULT.md` | 上游,本计划的需求来源 |
| 概要设计 | `design/REQ-00024/RESULT.md` | 上游,本计划的设计依据 |
| 7 份过程文档 | `plan/REQ-00024/{materials-index,module-details,interface-specs,data-changes,risk-analysis,rule-compliance,design-notes}.md` | 本计划的辅助文档 |
| V0.0.3 看板 | `RESULT.md §任务清单` | 本计划完成后由 code-it 同步 |
| REQ-00007 计划 | `plan/REQ-00007/PLAN.md`(若存在) | 撤销关键字逻辑;0 直接影响 |

---

## 7. 变更记录

| 时间 | 变更类型 | 变更摘要 | 关联项 |
| --- | --- | --- | --- |
| 2026-06-07 | 计划完成 | code-plan 完成 REQ-00024 详细设计 + 1 任务拆分(`code-auto/SKILL.md` 改造);0 派生"更新看板"任务;6 步状态机不变;9 个其他 code-* 技能字节级 0 变化 | REQ-00024 |
| 2026-06-07 | 任务完成 | TASK-REQ-00024-00001 实施完成(开发状态:已完成;8 项 AC 全通过;commit 待末尾兜底) | TASK-REQ-00024-00001 |
