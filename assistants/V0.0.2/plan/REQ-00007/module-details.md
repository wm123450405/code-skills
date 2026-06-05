# 模块详细化 — REQ-00007

更新时间:2026-06-05 10:00
版本:V0.0.2

## 模块:M-1 `code-auto/SKILL.md`(对应概要设计 §7.2)

### 路径
`plugins/code-skills/skills/code-auto/SKILL.md`(新文件,预计 ~600 行 Markdown)

### 关键"组件"(SKILL.md 的"伪代码"视角)
本设计无传统代码模块,SKILL.md 内部的"组件"是**章节 + 状态机 + 子技能调用表**:

| 组件 | 形式 | 职责 |
| --- | --- | --- |
| frontmatter | YAML | 技能元信息(技能名 + 描述) |
| §5 状态机总览 | Mermaid | 7 步骤状态机可视化 |
| §6 子技能调用表 | 表格 | 7 步 × 4 列 |
| §7 工作流步骤 | 文字 | 步骤 0a / 0 / 1-3 / 4 / 5-6 / 7 详细 |
| §8 数据解析 | 锚点字符串 | 任务编码 + 必须改列表解析规则 |
| §10 报告输出 | 模板 | 屏幕 + 磁盘报告格式 |

### 关键"函数"(语义视角)

| "函数" | 触发时机 | 职责 |
| --- | --- | --- |
| `version_detect()` | 步骤 0 | 读 `.current-version` → `<版本号>` |
| `sub_skill_invoke(skill_name, args)` | 步骤 1-6 | 用 `Skill` 工具调子技能,返回成功/失败 |
| `parse_plan_tasks(plan_md_path)` | 步骤 4 前置 | 解析 `PLAN.md` 任务总览 → 任务编码列表 |
| `parse_review_findings(review_report_path)` | 步骤 5/6 | 解析 `REVIEW-REPORT.md` 评审发现汇总 → "必须改"任务列表 |
| `format_progress(line)` | 步骤 1-6 每步 | 打印进度到 stdout |
| `format_completion_report()` | 完成时 | 拼装完整报告 |
| `write_auto_report(content, target_path)` | 完成时 | 写 `auto-report.md`(失败仅警告) |
| `handle_sigint()` | 收到 SIGINT | 打印中止报告 + 退出 130 |
| `handle_sub_skill_failure(step, stderr)` | 子技能退出码 ≠ 0 | 打印中断报告 + 退出 ≠ 0 |

### 关键"调用顺序"(对应状态机)

```
[启动]
  → version_detect() (步骤 0)
  → sub_skill_invoke("code-require", "<需求>") (步骤 1)
  → sub_skill_invoke("code-design", "REQ-NNNNN") (步骤 2)
  → sub_skill_invoke("code-plan", "REQ-NNNNN") (步骤 3)
  → parse_plan_tasks(plan_path) (步骤 4 前置)
  → for each task:
       sub_skill_invoke("code-it", task) + 可选 sub_skill_invoke("code-unit", task)
  → sub_skill_invoke("code-review", "REQ-NNNNN") (步骤 5)
  → parse_review_findings(review_report_path) (步骤 5 后置)
  → while "必须改" 非空:
       for each derived task:
         sub_skill_invoke("code-it", derived) + 可选 sub_skill_invoke("code-unit", derived)
       sub_skill_invoke("code-review", "REQ-NNNNN")
       parse_review_findings(review_report_path)
  → format_completion_report() (步骤 7 完成分支)
  → write_auto_report(content, auto_report_path) (步骤 7 完成分支)
  → exit 0

(任意步骤) handle_sub_skill_failure() 或 handle_sigint() → exit ≠ 0 / 130
```

### 内部状态
- **不维护内存状态**:`code-auto` 是无状态执行器;每次从文件重新解析(NFR-8 + Q-11 锁定)
- **不写代码 / 配置 / 数据库**:仅 `Write` 1 个 `auto-report.md`(完成时)
- **不持有任何凭据**

### 并发模型
- **N/A**:NFR-2 强约束串行
- **无锁 / 无事务 / 无并发原语**

### 资源管理
- **N/A**:无连接 / 锁 / 缓存
- **单次内存占用**:SKILL.md 上下文 + 子技能输出文本(由 Claude Code 模型层管理)

### 错误处理范式
- **不修改既有子技能** = `code-auto` 自身的错误处理范式独立定义
- **检测 → 报告 → 退出**(无 try/catch,因 SKILL.md 是 Markdown 而非代码)
- **退出码语义**:
  - `0` = 正常完成
  - `≠ 0` = 子技能异常中断
  - `130` = SIGINT 中止

### 日志埋点
- **进度输出**(NFR-10):每步打印一行 `[code-auto] 步骤 X/Y:<子技能> <参数>`
- **完成报告**:屏幕 stdout 一次性输出完整报告
- **磁盘留痕**:完成时 `Write` `auto-report.md` 一次性写入
- **不维护日志文件**:无运行日志 / 调试日志

### 依据规范
- `skill-conventions.md §规则 1`(frontmatter 必含 name+description)
- `module-conventions.md §规则 1`(SKILL.md 在技能根目录)
- `encoding-conventions.md §规则 1-4`(任务编码双格式正则)
- `dashboard-conventions.md §规则 1`(看板解析锚点沿用)

---

## 模块:M-2 `auto-report.md`(对应概要设计 §7.3)

### 路径
`./assistants/<版本号>/require/REQ-NNNNN/auto-report.md`

### 写入时机(NFR-7 强约束)
- **写入**:`code-auto` 正常完成(全部步骤通过 + 必须改列表空)→ 一次性 `Write`
- **不写入**:子技能退出码 ≠ 0 / SIGINT / 自身崩溃 / `Write` 失败

### 关键"属性"

| 属性 | 值 |
| --- | --- |
| 文件格式 | Markdown |
| 行数 | 50-80 行(中等规模报告) |
| 字节数 | 2-5 KB |
| 文件状态 | 一次性 Write(非增量) |
| 同名文件 | **覆盖**(NFR-6 强约束 `code-publish` 已确认的"幂等"模式一致) |

### 关键"结构"
详见 `interface-specs.md §1.3` + `data-changes.md §1.1`(标准 schema)。

### 与 M-1 的关系
- **M-1 在完成时调用 M-2 的 `write_auto_report(content, target_path)` 函数**
- **M-1 不感知 M-2 的内部结构**(单向数据流:M-1 输出字符串 → M-2 写盘)

### 依据规范
- `doc-conventions.md`(辅助手段,非强约束)
- NFR-7 强约束(中止时不写)

---

## 自检 — 与概要设计 §7 模块划分的对应

| 概要设计章节 | 本设计章节 | 任务编号 |
| --- | --- | --- |
| §7.1 模块总览 | (沿用) | T-001 |
| §7.2 M-1 详细 | 本文档"模块 M-1" | T-001 |
| §7.3 M-2 详细 | 本文档"模块 M-2" | T-001(运行时) |

**结论:本详细设计与概要设计 100% 一致,无新增模块,无模块拆分变化。**
