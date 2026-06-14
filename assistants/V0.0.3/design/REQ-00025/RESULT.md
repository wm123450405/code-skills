# 概要设计 — REQ-00025 — 软化编号正则约束,允许用户自定义编号格式(仅前缀固定)

- 需求编码:REQ-00025
- 所属版本:V0.0.3
- 设计目标:`--balanced`(code-auto 上下文检测 DETECTED,自动采纳默认值)
- 维度优先级:功能性=中(默认值;纯软化,非架构层)
- 状态:已锁定
- 责任人:wangmiao
- 创建:2026-06-07
- 最近更新:2026-06-08
- 当前版本:v1(增量更新确认 2026-06-08,无内容变更)

---

## 上游引用

- **来源**:`./assistants/V0.0.3/require/REQ-00025/RESULT.md`
- **FR 数量**:8(FR-1 / FR-2 / FR-3 / FR-4 / FR-5 / FR-6 / FR-7 / FR-8)
- **NFR 数量**:7
- **AC 数量**:8(AC-1~AC-8)
- **关联需求**:REQ-00002(编码权威源初版)/ REQ-00007(模式 B)/ REQ-00024(路径感知)

## 遵循规范

- `./assistants/rules/encoding-conventions.md` §规则 1/2/4(**本需求直接修订**)
- `./assistants/rules/skill-conventions.md` §规则 1:SKILL.md frontmatter 字节级保留
- `./assistants/rules/dashboard-conventions.md` §规则 1:看板字段扩展需 3 文件同步
- 其余 10 份占位规范 0 触发

---

## 1. 设计概述

**目标**:将 `code-skills` 体系的 3 类编号格式(REQ-NNNNN / BUG-NNNNN / TASK-(REQ|BUG)-NNNNN-NNNNN)从"5 位纯数字强约束"软化为"前缀固定 + 后缀自由(字符集 `A-Za-z0-9.\-_`)"。

**核心改造**:
- `encoding-conventions.md` §规则 1 + §规则 2 + §规则 4 软化(默认生成 vs 接收分开)
- 8 个 `code-*` 技能 SKILL.md 字面更新(`code-require` / `code-design` / `code-plan` / `code-it` / `code-unit` / `code-check` / `code-fix` / `code-dashboard`)
- **不**改 5 个其他技能(`code-init` / `code-version` / `code-rule` / `code-publish` / `code-auto`)

**架构影响**:`encoding-conventions.md` 1 处规范修订 + 8 个 SKILL.md 字面更新;0 字段新增,0 触发 `dashboard-conventions §规则 1` 三同步。

## 2. 关键设计决策

### D-1:生成 vs 接收分离

- **决策**:**生成端**继续 5 位纯数字(沿用 INV),**接收端**放宽为前缀 + 后缀两段式
- **理由**:
  - 生成端:本仓库 `code-require` / `code-plan` 自动生成,5 位纯数字是默认值
  - 接收端:第三方平台生成的编号无规律,仅校验前缀
  - 2 段式解析:`id-prefix` + `id-suffix`(后缀字符集 `A-Za-z0-9.\-_`)
- **影响**:0
- **依据规范**:无直接对应;沿用"生成 vs 解析解耦"的隐含原则

### D-2:后缀字符集 `A-Za-z0-9.\-_`

- **决策**:后缀只允许字母 / 数字 / `.` / `-` / `_`
- **理由**:
  - 排除 `/` / `\` 防止路径遍历
  - 排除 `!@#$%^&*()` 避免 OS 文件系统差异
  - 覆盖典型场景:`00001` / `V0.0.1.001` / `2025-Q4-001` / `XYZ_123`
- **影响**:0 既有编号受影响(纯数字 + `.` / `-` / `_` 全部允许)

### D-3:第三方平台前缀登记流程(沿用既有)

- **决策**:用户调 `code-rule` 登记新前缀(如 `JIRA- → 等价 REQ-`)
- **理由**:
  - **不**在 `code-rule` 中**新增**契约(本需求 NFR 强约束)
  - 既有 `code-rule` 追加规范时,只需在 `encoding-conventions.md` §规则 1.5 写 1 行
  - 沿用既有"登记即生效"模式
- **影响**:0 既有流程破坏

### D-4:屏显保留完整编号(不截断 30 字符)

- **决策**:标题若 > 30 字符仍按 `truncateTitle` 截断;编号本身保留完整(不截断)
- **理由**:
  - 30 字符限制是针对**标题**的可读性约束,不是**编号**的合规约束
  - 编号本身需要完整保留(便于审计 + 跨平台追溯)
- **影响**:0

### D-5:0 破坏性变更(纯加法)

- **决策**:既有 `REQ-00001` / `BUG-00001` 继续可用(纯数字符合新字符集)
- **理由**:
  - 新正则 `[A-Za-z0-9.\-_]+` 是旧正则 `\d{5}` 的**超集**
  - 0 既有编号受影响
- **影响**:0 兼容性破坏

### D-6:8 个相关技能 SKILL.md 字面更新(本需求精确范围)

- **决策**:仅更新 8 个相关技能 SKILL.md
- **依据**:`require/REQ-00025/RESULT.md §10 NFR-1` 强约束
- **修改列表**:
  - `code-require/SKILL.md`:步骤 1 编码格式 + 工具使用约定
  - `code-design/SKILL.md`:步骤 2 + 步骤 3 校验放宽
  - `code-plan/SKILL.md`:步骤 2 / 步骤 9B / §步骤 10A 任务拆分
  - `code-it/SKILL.md`:步骤 1 / 步骤 7 解析 + 生成逻辑分离
  - `code-unit/SKILL.md`:步骤 2 校验放宽
  - `code-check/SKILL.md`:步骤 2 解析放宽
  - `code-fix/SKILL.md`:步骤 1 解析放宽
  - `code-dashboard/SKILL.md`:算法 4 解析放宽
- **不修改**:
  - `code-init` / `code-version` / `code-rule` / `code-publish` / `code-auto`:与编号格式无关
- **影响**:8 个文件 + 1 规范 = 9 文件改动

## 3. 模块拆分

| 模块 | 路径 | 状态 | 职责 | 依赖 |
| --- | --- | --- | --- | --- |
| **encoding-conventions.md** | `./assistants/rules/encoding-conventions.md` | **修改** | 3 类编码权威源(§规则 1/2/4) | (无) |
| **code-require/SKILL.md** | `plugins/code-skills/skills/code-require/SKILL.md` | **修改** | 需求分析 | `code-design` / `code-plan` |
| **code-design/SKILL.md** | `plugins/code-skills/skills/code-design/SKILL.md` | **修改** | 概要设计 | `code-require` / `code-plan` |
| **code-plan/SKILL.md** | `plugins/code-skills/skills/code-plan/SKILL.md` | **修改** | 详细设计 + 任务计划 | `code-it` / `code-check` |
| **code-it/SKILL.md** | `plugins/code-skills/skills/code-it/SKILL.md` | **修改** | 实施开发 | `code-unit` / `code-check` |
| **code-unit/SKILL.md** | `plugins/code-skills/skills/code-unit/SKILL.md` | **修改** | 单元测试 | `code-it` |
| **code-check/SKILL.md** | `plugins/code-skills/skills/code-check/SKILL.md` | **修改** | 代码评审 | `code-it` |
| **code-fix/SKILL.md** | `plugins/code-skills/skills/code-fix/SKILL.md` | **修改** | 缺陷登记 + 跟踪 | `code-plan` / `code-it` |
| **code-dashboard/SKILL.md** | `plugins/code-skills/skills/code-dashboard/SKILL.md` | **修改** | 只读看板 | (无) |

## 4. 接口(本需求涉及)

### 接口:`code-*` 技能 SKILL.md 编号解析函数族

- **形式**:伪代码 / 正则字面量
- **入参**:`<input>`(用户输入字符串)
- **出参**:布尔(`true` = 合法编号)
- **示例**:
  - `^REQ-\d{5}$`(旧)→ `^REQ-[A-Za-z0-9.\-_]+$`(新)
  - `^BUG-\d{5}$`(旧)→ `^BUG-[A-Za-z0-9.\-_]+$`(新)
  - `^TASK-(REQ|BUG)-\d{5}-\d{5}$`(旧)→ `^TASK-(REQ|BUG)-[A-Za-z0-9.\-_]+-[A-Za-z0-9.\-_]+$`(新)

## 5. 数据结构(本需求涉及)

- **核心实体**:`id-prefix` × `id-suffix` → `完整编号`
  - `id-prefix` (3 类):`REQ-` / `BUG-` / `TASK-REQ-` / `TASK-BUG-`
  - `id-suffix` (1+ 位,字符集 `A-Za-z0-9.\-_`)

## 6. 算法(本需求核心)

```
parseID(raw, type):
  // type: 'REQ' | 'BUG' | 'TASK-REQ' | 'TASK-BUG'

  if type == 'REQ':
    m = match(/^REQ-([A-Za-z0-9.\-_]+)$/, raw)
  elif type == 'BUG':
    m = match(/^BUG-([A-Za-z0-9.\-_]+)$/, raw)
  elif type in ['TASK-REQ', 'TASK-BUG']:
    prefix = type == 'TASK-REQ' ? 'TASK-REQ-' : 'TASK-BUG-'
    m = match(new RegExp('^' + prefix + '([A-Za-z0-9.\-_]+)-([A-Za-z0-9.\-_]+)$'), raw)

  if m:
    return { valid: true, prefix: type, suffix: m[1] (or [m[1], m[2]]) }
  return { valid: false }
```

```
generateID(type):
  // 沿用既有 5 位纯数字
  next = (last + 1).zfill(5)
  return type + '-' + next
```

## 7. 异常处理

| 异常路径 | 处理 |
| --- | --- |
| 编号含非法字符(`/` / `\` / `!` 等) | 屏显 `⚠ 编号含非法字符: <char>` |
| 编号超长(> 200 字符) | 接受(OS 文件系统层有 255 字符限制) |
| 编号后缀全 0(如 `REQ-0000`) | 接受(后缀"0000"是合法 4 位字符) |
| 第三方平台前缀未登记 | 屏显 `⚠ 前缀 <X>- 未登记`,引导调 `code-rule` |

## 8. 安全要求

- 路径遍历防护:后缀字符集排除 `/` / `\`,不解析 `..`
- 无敏感数据泄露
- 屏显只显示编号 + 标题,不显示任何用户输入原文

## 9. 状态机/流程

(沿用既有 `code-*` 技能状态机,本需求**不**新增状态机)

## 10. 性能与资源

- 正则匹配性能:旧 `\d{5}` vs 新 `[A-Za-z0-9.\-_]+` 性能相当(< 0.001ms 级)
- 0 性能影响
- 0 资源影响

## 11. 测试要点

### 11.1 单元测试(本仓库 0 测试框架,验证手段 = 静态校验 + 手动调用)

| 测试 ID | 描述 | 验证方式 |
| --- | --- | --- |
| U-1 | 既有 5 位纯数字继续工作 | 调 `code-require REQ-00020`(已存在 RESULT.md) |
| U-2 | Jira 风格 `JIRA-123` 解析(需先 `code-rule` 登记) | 调 `code-rule` 登记 + 调 `code-require JIRA-123` |
| U-3 | `JIRA-V0.0.1.001` 解析(多 `.` 后缀) | 调 `code-require JIRA-V0.0.1.001` |
| U-4 | `JIRA-2025-Q4-001` 解析(多 `-` 后缀) | 调 `code-require JIRA-2025-Q4-001` |
| U-5 | 非法前缀 `PROJ-123` 拒绝 | 调 `code-require PROJ-123` |
| U-6 | 非法后缀 `REQ-a/b` 拒绝 | 调 `code-require REQ-a/b` |
| U-7 | 后缀空 `REQ-` 拒绝 | 调 `code-require REQ-` |
| U-8 | 8 项 AC 静态校验全通过 | `git diff` + `Grep` |

## 12. 规范遵循(13 份规范自检)

| 规范 | 触发? | 结论 |
| --- | --- | --- |
| `skill-conventions.md §规则 1` | ✅ 强 | 8 个 SKILL.md frontmatter 字节级保留(INV 严守) |
| `module-conventions.md` | ❌ | DEPRECATED,本修复不引用 |
| `directory-conventions.md` | ❌ | 占位待填,本修复不触发 |
| `encoding-conventions.md §规则 1-4` | ✅ 强 | 本需求**直接修订**(1 处新增 §规则 1.5) |
| `dashboard-conventions.md §规则 1` | ❌ | 0 字段扩展,0 三同步 |
| `doc-conventions.md §规则 1-2` | ❌ | 本修复不涉及 README |
| `coding-style.md` | ❌ | 占位,SKILL.md 是自然语言不涉及代码风格 |
| `commit-conventions.md` | ⚠️ 软 | 沿用 `chore(code-xxx):` 格式 |
| `dependency-conventions.md` | ❌ | 0 新依赖 |
| `framework-conventions.md` | ❌ | 0 架构变更 |
| `naming-conventions.md` | ❌ | 0 新增命名实体 |
| `migration-mapping.md` | ❌ | 0 编码重命名 |
| `marketplace-protocol.md` | ❌ | 0 JSON 字段变更 |

**自检结论**:1 强约束触发修订(encoding-conventions.md),7 强约束严守(其他 8 个 SKILL.md),0 软约束变更。

## 13. 关联设计

| 关联设计 | 关联点 |
| --- | --- |
| REQ-00002(编码权威源初版) | 本设计是 REQ-00002 的"放宽版";保留 REQ-00002 既定契约 |
| REQ-00007(code-auto 模式 B) | 0 直接影响 |
| REQ-00024(路径感知) | 本需求放宽"需求编号"字面 → 路径感知可识别任意前缀的需求(如 `JIRA-123`) |

## 14. 待澄清 / 未决项

| 编号 | 问题 | 默认决策(本轮锁定) | 后续触发 |
| --- | --- | --- | --- |
| Q-1 | `code-publish` 同步改造? | **否**(`code-publish` 接受版本号,无编号依赖) | 2026-06-10(可推迟) |
| Q-2 | 中文 / Unicode 字符? | **否**(ASCII 字符集,避免 OS 差异) | 同上 |
| Q-3 | 跨版本工作空间携带? | **否**(沿用既有"每版本独立") | 同上 |
| Q-4 | `code-dashboard` 双正则兼容? | **是**(本需求已包含,AC-7 已覆盖) | 锁定 |

## 15. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-07 | v1 | 初始创建 | code-design 完成 REQ-00025 概要设计(15 章节;1 规范修订 + 8 SKILL.md 字面更新;0 字段扩展;0 派生"更新看板"任务) | wangmiao |
| 2026-06-08 | v1 | 增量更新确认 | code-design 增量更新(no-op):需求侧 v1 未变;规范侧 13 份 0 变化(encoding-conventions.md 未软化 — 留待 code-plan/code-it 落地);代码侧 8 个 in-scope SKILL.md 仍含旧 5 位正则(留待 code-plan/code-it 落地);设计侧 0 修订;唯一动作 = 版本看板"变更记录"追加 1 行 + 概要设计清单状态保持"已完成";0 字段扩展,0 §规则 1 三同步,0 派生"更新看板"任务;design/.../RESULT.md §15 追加 1 行 | wangmiao |
