# 模块拆分 — REQ-00007

更新时间:2026-06-05 09:20
版本:V0.0.2

> 遵循规范:`./assistants/rules/module-conventions.md §规则 1`(资源须放固定子目录 templates/ / checklists/ / guidelines/);`skill-conventions.md §规则 1`(SKILL.md frontmatter 必含 name + description)

## 1. 模块总览

| # | 模块名 | 路径 | 状态 | 职责 | 对外接口 | 依赖 | 关键决策 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| M-1 | `code-auto` | `plugins/code-skills/skills/code-auto/SKILL.md` | **新增** | 编排者,串行驱动 6 子技能 + 评审循环 + 自动选推荐项 | `Skill` 工具调用(被用户触发);不暴露其他对外接口 | `Skill(code-require)` / `Skill(code-design)` / `Skill(code-plan)` / `Skill(code-it)` / `Skill(code-unit)` / `Skill(code-review)` | 单文件技能,无子目录(无模板/清单/规则) |
| M-2 | `auto-report.md`(运行时产物) | `./assistants/<版本号>/require/REQ-NNNNN/auto-report.md` | **新增**(运行时) | 完整执行报告留痕 | N/A(产物文件,非模块) | M-1 | 完成时由 M-1 写入;异常/中止时不写(NFR-7) |

**说明**:
- **新增模块 = 1 个文件**(`SKILL.md`)+ **运行时产物 = 1 个文件**(`auto-report.md`)
- **修改模块 = 0 个**(严格遵循 FR-8.AC-8.1)
- **复用模块 = 6 个子技能**(`code-require` / `code-design` / `code-plan` / `code-it` / `code-unit` / `code-review`)
- **复用既有数据源 = 3 个**:`.current-version` / `plan/PLAN.md` / `review/REVIEW-REPORT.md`

## 2. 模块 M-1 详细定义 — `code-auto`

### 2.1 路径
`plugins/code-skills/skills/code-auto/SKILL.md`(新文件,预计 ~600 行)

### 2.2 frontmatter(Q-A1 锁定 A 风格,严格遵循 `skill-conventions §规则 1`)
```yaml
---
name: code-auto
description: 自动开发编排(版本感知)。接收 1 个需求内容,按 `code-require` → `code-design` → `code-plan` → `code-it`(+ `code-unit` 条件)→ `code-review` 循环(派生任务自动修复)的固定顺序,串行驱动 6 个子技能完成完整开发周期,过程中所有 `AskUserQuestion` 自动选推荐项,完全无需用户确认;支持 `Ctrl+C` 中止 + 异常立即中断 + 完成时输出报告到 `auto-report.md`。在 `code-version` 之后、其他 `code-*` 之前作为顶层入口使用;也可用作"从需求到代码 + 单测 + 评审全自动跑通"的一键命令。
---
```

### 2.3 内部结构(Q-A1 锁定 A:显式状态机 + 子技能调用表)

| 章节 | 内容 | 关联规范 |
| --- | --- | --- |
| §1 目标 | 一句话讲清"做什么、何时用" | `skill-conventions §规则 1`(description 完整) |
| §2 适用场景 | 适用 / 不适用 | NFR-1/3/4(零依赖、不 commit、不引入批量模式) |
| §3 工作目录约定 | 强制 `./assistants/.current-version` + `.current-version` 不存在时中止 | FR-2(接收需求内容) |
| §4 输入与输出 | 输入 = 1 个字符串参数;输出 = 屏幕报告 + 磁盘 `auto-report.md` | FR-2 / FR-9 / FR-10 |
| §5 状态机总览 | Mermaid 状态机图(7 步 + 评审循环) | Q-A1 锁定 A |
| §6 子技能调用表 | 7 步 × (调谁 / 传什么 / 期望产物 / 失败处理) | Q-A1 锁定 A |
| §7 工作流步骤 | 步骤 0a / 0 / 1 / 2 / 3 / 4 / 5 / 6 详细描述 | FR-3 ~ FR-7 |
| §8 数据解析 | PLAN.md 任务总览解析 + REVIEW-REPORT.md"必须改"解析 | FR-4.AC-4.1 + FR-5.AC-5.6 + D-3 选定 A |
| §9 中断与异常 | SIGINT + 子技能退出码 ≠ 0 + 报告留痕 | FR-7 / NFR-7 / E-1 ~ E-10 |
| §10 报告输出 | 屏幕 + `auto-report.md`(完成时) | FR-9 / FR-10 |
| §11 边界与异常 | E-1 ~ E-10 | §9 边界(需求文档直接搬) |
| §12 上下游衔接 | 上游 = `code-version`(激活版本);下游 = `code-dashboard` / `code-publish`(建议) | NFR-9 / Q-6 |
| §13 关联需求 | REQ-00004 / 05 / 06 / 08 / 09 / 10 / 11 | NFR-9 |
| §14 工具使用约定 | 调子技能用 `Skill` 工具;读文件用 `Read`;写报告用 `Write` | `skill-conventions`(沿用) |
| §15 变更记录 | 留空,首版 | — |

### 2.4 状态机(Q-A1 锁定 A:显式状态机)

```
[启动]
  ↓
[步骤 0a:git pull] ──────┐
  ↓ (成功)               │ (失败 → E-2/3/4 报错退出)
[步骤 0:读 .current-version] ──┐
  ↓ (成功)               │ (失败 → E-1 提示调 code-version)
[步骤 1:Skill(code-require, "<需求>")]
  ↓ (返回 REQ-NNNNN)
[步骤 2:Skill(code-design, REQ-NNNNN)]
  ↓ (返回产出)
[步骤 3:Skill(code-plan, REQ-NNNNN)]
  ↓ (返回 plan/{RESULT,PLAN}.md)
[步骤 4:任务循环]
  ↓ 对 plan/PLAN.md 任务总览每个任务:
     - Skill(code-it, <任务编码>)
     - 若 code-it 输出含"测试需要=Y":
       Skill(code-unit, <任务编码>)
  ↓ (所有任务完成)
[步骤 5:Skill(code-review, REQ-NNNNN)]
  ↓ (返回 REVIEW-REPORT.md)
[解析"必须改"列表]
  ├─ 空 → [完成 + 写 auto-report.md] → [退出 0]
  └─ 非空 → [步骤 6:派生任务循环]
              ↓ 对每个派生任务:
                 - Skill(code-it, <派生任务编码>)
                 - 若需要:Skill(code-unit, <派生任务编码>)
              → 回到步骤 5
```

### 2.5 子技能调用表(Q-A1 锁定 A)

| 步骤 | 子技能 | 输入参数 | 期望产物 | 失败处理 | 关联 FR |
| --- | --- | --- | --- | --- | --- |
| 0a | (git pull) | — | 仓库最新代码 | 报错退出(E-2/3/4) | 沿用 REQ-00005 模式 |
| 0 | (读 .current-version) | — | `<版本号>` | 提示调 `code-version`(E-1) | FR-3.AC-3.1 前置 |
| 1 | `code-require` | `"<原需求内容>"` | `require/REQ-NNNNN/RESULT.md` | 中断 + 报告 | FR-3.AC-3.1 |
| 2 | `code-design` | `REQ-NNNNN` | `design/REQ-NNNNN/RESULT.md` | 中断 + 报告 | FR-3.AC-3.1 |
| 3 | `code-plan` | `REQ-NNNNN` | `plan/REQ-NNNNN/{RESULT,PLAN}.md` | 中断 + 报告 | FR-3.AC-3.1 |
| 4 | `code-it` | `TASK-REQ-NNNNN-NNNNN` | `code/TASK-.../RESULT.md` | 中断 + 报告 | FR-4.AC-4.2 |
| 4 | `code-unit` | `TASK-REQ-NNNNN-NNNNN` | `test/TASK-.../RESULT.md` | 中断 + 报告 | FR-4.AC-4.2(条件) |
| 5 | `code-review` | `REQ-NNNNN` | `review/REQ-NNNNN/REVIEW-REPORT.md` | 中断 + 报告 | FR-5.AC-5.1 |
| 6 | `code-it` | `<派生任务编码>` | `code/.../RESULT.md` | 中断 + 报告 | FR-5.AC-5.3 |
| 6 | `code-unit` | `<派生任务编码>` | `test/.../RESULT.md` | 中断 + 报告 | FR-5.AC-5.3(条件) |

### 2.6 步骤 4 条件判断(FR-4.AC-4.2 + FR-4.AC-4.3)

```
读 code-it 返回输出:
  若含 "测试需要=Y" / "需要测试" / "需补单测" → 调 code-unit
  否则 → 跳过 code-unit
```

> 备注:`code-it` 当前 SKILL.md 输出的"测试需要"判定锚点待 `code-plan` 阶段细化;本设计仅约定"code-auto 接收任意 '测试需要=Y' 字符串即触发 code-unit",与 `code-it` 实际输出对齐的责任在 `code-plan` / `code-it` 内部约定,不在本设计范围。

### 2.7 步骤 5/6 循环(FR-5.AC-5.1 ~ AC-5.6 + D-3 选定 A)

```
读 review/REQ-NNNNN/REVIEW-REPORT.md:
  解析"评审发现汇总"区段(锚点:^## 评审发现汇总$ + 表格行 ^\| .* \|$)
  筛选"级别=必须改" + "状态≠已处理"的行
  提取每行的"任务编码"列(若有;无则视为"无派生任务,结束")
  ↓
  若列表空 → 结束
  若非空 → 对每条派生任务 → 调 code-it / code-unit → 回到步骤 5
```

## 3. 模块 M-2 详细定义 — `auto-report.md`

### 3.1 路径
`./assistants/<版本号>/require/REQ-NNNNN/auto-report.md`

### 3.2 写入时机(FR-9.AC-9.4 + FR-10.AC-10.1 + NFR-7)
- **写入**:`code-auto` 正常完成 → 一次性 Write
- **不写入**:子技能异常 / SIGINT 中止 / `code-auto` 自身崩溃(避免半成品)

### 3.3 内容结构(FR-9 报告字段)
```markdown
# auto-report — REQ-NNNNN(<需求标题>)

- 需求编码:REQ-NNNNN
- 所属版本:V0.0.2
- code-auto 起始时间:YYYY-MM-DD HH:mm
- code-auto 结束时间:YYYY-MM-DD HH:mm
- 总状态:✓ 完成 / ⏹ 用户中止 / ✗ 子技能异常
- 总子技能调用次数:N

## 执行摘要
| 子技能 | 调用次数 |
| --- | --- |
| code-require | 1 |
| code-design | 1 |
| code-plan | 1 |
| code-it | N1 |
| code-unit | N2 |
| code-review | N3 |

## 最终状态
- REQ-NNNNN 状态:已完成 / 进行中 / 阻塞
- 任务清单:TASK-... × N,均已完成 / 部分完成
- 缺陷:0 / N
- 派生任务:N,均已完成 / 部分完成

## 后续建议(完成时)
- 执行 /code-dashboard 查看完整状态
- 执行 /code-publish 生成发布手册

## 剩余工作(中断时)
- 已完成:...
- 未完成:...
```

## 4. 自检 — `module-conventions §规则 1` 逐条对照

| 条款 | 本设计响应 | 合规 |
| --- | --- | --- |
| 资源须放 `templates/` / `checklists/` / `guidelines/` 固定子目录 | `code-auto/` 无子目录(无任何资源文件) | ✅ |
| `SKILL.md` 本身放在技能根目录 | `code-auto/SKILL.md` 在根目录 | ✅ |
| 资源类型不在三类中(临时草稿/工具脚本)→ 设计评审决定 | 本设计**无**临时草稿,**无**工具脚本 | ✅(不触发) |
| 例外:临时草稿放 `drafts/` 子目录 + 标注"草稿,未生效" | 本设计无草稿 | ✅(不触发) |

**结论:M-1 模块 100% 合规 module-conventions §规则 1。**

## 5. 自检 — `skill-conventions §规则 1` 逐条对照

| 条款 | 本设计响应 | 合规 |
| --- | --- | --- |
| YAML frontmatter 开头 | `name: code-auto` + `description: ...` | ✅ |
| `name` = 目录名 kebab-case | `code-auto` = 目录名 `code-auto` | ✅ |
| `description` 完整自然语言 | 一段完整描述(目标 + 适用场景 + 触发条件) | ✅ |
| `description` 不空 / 不占位 / 不堆砌关键词 | 描述涵盖"自动驱动 + 评审循环 + 完全无人确认" | ✅ |

**结论:M-1 frontmatter 100% 合规 skill-conventions §规则 1。**

## 6. 复用既有模块清单(6 个子技能)

| 模块 | 调用次数 | 复用方式 | 兼容性约束 |
| --- | --- | --- | --- |
| `code-require` | 1 次/执行 | `Skill` 工具,传 `<需求内容>` | 接受任意字符串,无参数限制 |
| `code-design` | 1 次/执行 | `Skill` 工具,传 `REQ-NNNNN` | 已接受 5 位格式(REQ-00001 等) |
| `code-plan` | 1 次/执行 | `Skill` 工具,传 `REQ-NNNNN` | 同上 |
| `code-it` | N1 次/执行(任务数 + 派生任务数) | `Skill` 工具,传 `TASK-...` 或 `REQ-...-...` 旧格式 | 沿用 `encoding-conventions §规则 1-4` + `code-dashboard NFR-3` 兼容策略 |
| `code-unit` | N2 次/执行(按需) | `Skill` 工具,传 `TASK-...` | 同上 |
| `code-review` | N3 次/执行(1 + 评审循环) | `Skill` 工具,传 `REQ-NNNNN` | 沿用 `code-review` 既有"必须改"档(FR-5.AC-5.6) |

**兼容性结论**:6 个子技能**无需任何修改**(FR-8.AC-8.1 + NFR-4 强约束)。

## 7. 修改既有模块清单

**0 个**(严格遵循 FR-8.AC-8.1)。
