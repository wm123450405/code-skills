# 详细设计 — REQ-00001(Marketplace 根名称添加 `-marketplace` 后缀)

- 需求编码:REQ-00001(原 REQ-2026-0001)
- 所属版本:V0.0.1
- 计划版本:v1
- 状态:已完成(首次计划)
- 责任人:wangmiao
- 创建:2026-06-03
- 最近更新:2026-06-03 20:30
- **上游需求**:`./assistants/V0.0.1/require/REQ-00001/RESULT.md`(v2,7 FR / 7 NFR / 9 AC / 3 项待澄清)
- **上游概要设计**:`./assistants/V0.0.1/design/REQ-00001/RESULT.md`(v1,7 设计决策,4 文件变更集,11 条不变量)
- **遵循规范**:`./assistants/rules/` 下 5 个文件(详见 §12 与 `rule-compliance.md`)

---

## 1. 概述

本计划是 `code-require` → `code-design` → **`code-plan`** 链路的第三步,把概要设计的"系统长什么样"落地为"如何具体改 + 哪些任务可被独立追踪"。

**核心目标**:把 4 个文件的具体修改点(精确到行号)与 4 个可独立执行的任务关联起来,任何任务的开发/测试状态变化都能在版本看板追溯。

**与概要设计的关系**:本计划不重新讨论"改什么字段",只细化"如何改、谁先谁后、失败怎么回退"。

---

## 2. 上游引用

| 来源 | 路径 | 版本 | 提取要点 |
| --- | --- | --- | --- |
| 需求 | `require/REQ-00001/RESULT.md` | v2 | 7 FR / 7 NFR / 9 AC |
| 概要设计 | `design/REQ-00001/RESULT.md` | v1 | 4 文件变更集 / 7 决策 / 11 不变量 |
| 概要过程文档 | `design/REQ-00001/{clarifications,design-notes,module-breakdown,dependencies,related-designs,rule-compliance,materials-index}.md` | v1 | Q 默认值 / 模块清单 / 依赖盘点 / 关联设计 / 规范遵循 |

**规范引用**:见 `rule-compliance.md`。

---

## 3. 模块详细化

### 3.1 `.claude-plugin/marketplace.json`

| 路径 | 字段 | 改前 | 改后 |
| --- | --- | --- | --- |
| `$.name` | 根 name | `"code-skills"` | `"code-skills-marketplace"` |

**唯一变更**:第 3 行(典型 2 空格缩进)由 `    "name": "code-skills",` 变为 `    "name": "code-skills-marketplace",`。

**严禁变更**:其它所有字段,特别是:
- `$.$schema`(规则 1.1 必填)
- `$.version`(Q-5 默认 A 保持 1.0.0)
- `$.description`(Q-3 默认 B 不改)
- `$.owner.name`(保持)
- `$.plugins[0].name`(规则 1.3 同步,严禁改)
- `$.plugins[0].version`(保持 1.0.0)
- `$.plugins[0].source`(保持)
- `$.plugins[0].skills`(保持 10 项)
- `$.plugins[0].keywords`(保持 10 项)

详见 `module-details.md` §模块 1。

### 3.2 `plugins/code-skills/README.md`

| 行号(预期) | 改前 | 改后 |
| --- | --- | --- |
| 14 | `` `claude plugin install code-skills@code-skills` `` | `` `claude plugin install code-skills@code-skills-marketplace` `` |
| 22 | `marketplace name 是 \`code-skills\`` | `marketplace name 是 \`code-skills-marketplace\`` |

**注**:行号以 `code-it` 实施时 Read 实际文件为准;若用户已部分手改,行号可能偏移。`code-it` 阶段必须用 Grep 定位实际行号。

详见 `module-details.md` §模块 2。

### 3.3 `plugins/code-skills/README.en.md`

| 行号(预期) | 改前 | 改后 |
| --- | --- | --- |
| 14 | `claude plugin install code-skills@code-skills` | `claude plugin install code-skills@code-skills-marketplace` |
| 22 | `marketplace name \`code-skills\`` | `marketplace name \`code-skills-marketplace\`` |

详见 `module-details.md` §模块 3。

### 3.4 `plugins/code-skills/CLAUDE.md`

**默认 0 变更**。T-003 任务仅做 Grep 核查:
- 关键词 1:`code-skills@code-skills`
- 关键词 2:`marketplace name`
- 预期:0 命中(由 REQU M-7 材料登记明示)

若 Grep 命中超出预期,按 FR-5 同步,记录到 `code-it` 工作日志。

详见 `module-details.md` §模块 4。

---

## 4. 算法与逻辑(详细化)

### 4.1 替换算法(所有 3 文件 Edit 操作统一)

```
对每个目标文件 F:
  1. Read F 全文
  2. 定位改前字符串 P(精确字面量匹配)
  3. 用 Edit 工具:
     old_string = P
     new_string = P 的改后版本
  4. 验证:Read F 全文,确认 P 已不在,改后字符串已存在
  5. 验证:Grep 全文,确认其它无关内容未受影响
```

### 4.2 验证算法

```
1. JSON 字段验证(T-001 后):
   Grep "name" .claude-plugin/marketplace.json
   ├─→ 根 name 行: code-skills-marketplace ✅
   ├─→ owner.name 行: code-skills (保持) ✅
   ├─→ plugins[0].name 行: code-skills (保持) ✅

2. README 验证(T-002 后):
   Grep "code-skills@code-skills-marketplace" README.md → ≥ 1 命中
   Grep "code-skills@code-skills-marketplace" README.en.md → ≥ 1 命中
   Grep "code-skills@code-skills" README.md → 0 命中
   Grep "code-skills@code-skills" README.en.md → 0 命中

3. CLAUDE.md 验证(T-003 后):
   Grep "code-skills@code-skills" plugins/code-skills/CLAUDE.md → 0 命中
   Grep "marketplace name" plugins/code-skills/CLAUDE.md → 0 命中(或记录"无需修改")

4. 全仓库验证(T-004 后):
   Grep "code-skills@code-skills" 全仓库 → 仅命中本需求工作目录
   ├─→ require/REQ-00001/* (历史) ✅
   ├─→ design/REQ-00001/* (历史) ✅
   ├─→ plan/REQ-00001/* (本计划) ✅
   ├─→ code/REQ-00001-NNN/* (待 T-N 产出) ✅
   └─→ 不应出现于:
       - marketplace.json ✅
       - README.md ✅
       - README.en.md ✅
       - plugin.json ✅
       - CLAUDE.md ✅
       - SKILL.md / 模板 ✅
       - 5 个规范文件 ✅
       - V0.0.0 基线 ✅
```

### 4.3 提交算法

```bash
git add .claude-plugin/marketplace.json \
        plugins/code-skills/README.md \
        plugins/code-skills/README.en.md
# CLAUDE.md 不主动 add(默认 0 变更)

git commit -m "chore(marketplace): rename root name code-skills → code-skills-marketplace

BREAKING CHANGE: 已 marketplace add code-skills 的用户需:
  1. claude plugin marketplace remove code-skills
  2. claude plugin marketplace add <git-url>
  3. claude plugin install code-skills@code-skills-marketplace

关联需求: REQ-00001"

git push
```

---

## 5. 数据结构完整变更

详见 `data-changes.md`。摘要:
- `.claude-plugin/marketplace.json`:1 字段值变更
- `plugins/code-skills/README.md`:2 行字面量变更
- `plugins/code-skills/README.en.md`:2 行字面量变更
- `plugins/code-skills/CLAUDE.md`:0 字段(默认)

---

## 6. 接口细节

详见 `interface-specs.md`。摘要:
- **marketplace 根 name 字段**:`"code-skills"` → `"code-skills-marketplace"`
- **install 命令**(用户外部接口):`code-skills@code-skills` → `code-skills@code-skills-marketplace`

**版本策略**:marketplace.json 根 `version` 保持 `1.0.0`(Q-5 默认 A)。
**兼容策略**:`plugins[].name` 保持 `code-skills`(plugin 标识独立,无兼容问题)。

---

## 7. 异常处理

详见 `risk-analysis.md`。关键风险:
- **E-1**:Edit 误改 `plugins[].name` → 预防:Edit 前 Read 全文,锁定 old_string 唯一
- **E-3**:README 中英不一致 → 预防:code-review 并列 diff
- **E-4**:working tree 不干净 → 预防:`git status` 检查
- **E-5**:用户已部分手改 → 应对:偏差日志记录,继续
- **E-7**:rename 影响老用户 → 应对:commit message 显式标注 BREAKING CHANGE

**回退策略**:`git revert <commit-hash>` 1 个 commit 全部回退。

---

## 8. 安全要求

本需求不涉及鉴权、加密、审计日志、应用层安全。安全相关的关键点:
- commit message 显式标注 BREAKING CHANGE(下游用户可见)
- 不引入新依赖,无供应链风险
- 不修改 `.claude/` 本地配置(不在 git 跟踪)

---

## 9. 状态机/流程

本需求的状态机极简:

```
[待开始]
   │ T-001 / T-002 / T-003 / T-004 任一启动
   ▼
[进行中]
   │ Edit 完成 + Grep 验证通过
   ▼
[已完成(开发)]
   │ code-review 验证通过
   ▼
[已完成(测试)] ← 本需求不适用单元测试,开发完成即测试完成
```

**任务级双状态**:
- 开发状态:`待开始` → `进行中` → `已完成`
- 测试状态:`不适用`(纯文档任务,无单元测试)

---

## 10. 性能与资源

N/A(纯字符串替换,无性能瓶颈)。

---

## 11. 测试要点

本需求**纯文档/字符串层变更**,无应用代码,无单元测试。`code-unit` 阶段对本需求所有任务标记为 `不适用`。

**替代验证手段**(覆盖原"测试要点"角色):
- 字节级 diff 审阅
- Grep 关键短语验证
- JSON 字段逐项核对
- 中英 README 并列 diff 对照
- 整体 `git diff --stat` 审阅
- 11 条不变量自检

详见 `risk-analysis.md` §"替代验证手段"。

---

## 12. 规范遵循

继承概要设计 `rule-compliance.md` 全部结论。本计划无新增偏离、无新增冲突。详见 `rule-compliance.md`。

---

## 13. 待澄清/未决项

继承概要设计 §13,3 项 Q 均采用 REQU 文档默认值(Q-3 B / Q-4 A / Q-5 A)。本计划阶段不主动追问。详见 `clarifications.md`。

---

## 14. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-03 20:30 | v1 | 计划新增 | 完成首次详细设计与任务拆分:4 个任务(`REQ-00001-001` ~ `REQ-00001-004`),每个含 file_path:line_number 精确到行;8 个过程文档就绪;继承概要设计 7 决策 + 11 不变量;Q-3/Q-4/Q-5 采用 REQU 文档默认;单 commit 提交,无新增依赖,无偏离规范 | wangmiao |
