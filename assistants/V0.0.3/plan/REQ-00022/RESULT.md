# 详细设计 — REQ-00022(修改 `/code-review` 技能名称为 `/code-check`)

- 需求编码:REQ-00022
- 所属版本:V0.0.3
- 文档版本:v1
- 状态:已锁定
- 责任人:wangmiao
- 创建:2026-06-07
- 最近更新:2026-06-07
- 当前版本:v1
- **上游需求**:`./assistants/V0.0.3/require/REQ-00022/RESULT.md`(v1,2026-06-07)
- **上游概要设计**:`./assistants/V0.0.3/design/REQ-00022/RESULT.md`(v1,2026-06-07)
- **遵循规范**:`./assistants/rules/` 下 13 个文件(本需求实际触发 4 个)

---

## 设计目标

> 本小节由 `code-plan` 步骤 0b 写入,沿用上游 `design/.../RESULT.md` 的设计目标。

- **回写时间**:2026-06-07
- **回写触发**:`code-plan` 步骤 0b
- **整体目标**:`--balanced`(code-auto 上下文默认;沿用上游概设)
- **7 维度优先级**(code-plan 步骤 0b 默认填充):

| 维度 | 优先级 | 依据 |
| --- | --- | --- |
| **功能性** | 中 | code-auto 上下文默认;本需求改造 11 类引用方 |
| **扩展性** | 不适用 | 本需求为"字面量重命名",不涉及扩展性设计 |
| **健壮性** | 不适用 | 沿用既有 `code-review` 健壮性设计 |
| **可维护性** | 中 | 字面量同步需严格遵循命名一致性,中等维护负担 |
| **封装性** | 不适用 | 沿用既有 |
| **可复用性** | 不适用 | 沿用既有 |
| **可读性** | 中 | 中英文表述不强求统一;字面量可读性中等 |

---

## 1. 详细设计概述

本详细设计在概要设计的基础上,把"硬重命名 + 11 类引用方字面量同步"细化为**可直接执行的 10 个任务**。每条任务对应一个**可独立 git commit / 可独立回滚**的"字面量同步批次"。任务按"由内向外 / 由小到大"组织,保证任一任务失败可回退而不影响后续任务。

**关键决策**:
- 10 个任务按"目录重命名 → JSON 同步 → SKILL.md 同步 → docs 同步 → 校验"5 阶段组织
- 任务粒度 = "1 个文件 / 1 批同质文件"的中等粒度(避免过细导致的"task 数量爆炸")
- 0 个任务涉及源代码改动(本需求纯 SKILL.md / JSON / docs 改动)
- 0 个任务涉及"测试需要=Y"(纯文档改动,无需 code-unit)

---

## 2. 上游引用

### 2.1 上游需求
- `./assistants/V0.0.3/require/REQ-00022/RESULT.md`(v1,2026-06-07)
- 关键摘录:7 FR / 6 NFR / ~33 AC / 9 INV

### 2.2 上游概要设计
- `./assistants/V0.0.3/design/REQ-00022/RESULT.md`(v1,2026-06-07)
- 关键摘录:6 决策(D-1 ~ D-6)+ 9 不变量(INV-1 ~ INV-9)+ 字面量替换矩阵(约 60-90 处)

### 2.3 规范引用
- `skill-conventions §规则 1`:FR-1 触发
- `marketplace-protocol §规则 1`:FR-2 触发
- `doc-conventions §规则 1`:FR-4 触发
- `migration-mapping §规则 5`:FR-5 沿用

---

## 3. 规范遵循

- **完全合规**的章节:§1-§13
- **经用户授权偏离**的章节:无
- **待澄清冲突**:无

---

## 4. 模块详细化(对应概要设计 §3)

### 模块 1:`code-review` 目录重命名(对应 FR-1)
- **关键操作**:
  - `Bash: git mv plugins/code-skills/skills/code-review plugins/code-skills/skills/code-check`
  - `Edit` SKILL.md frontmatter `name: code-review` → `name: code-check`
  - `Edit` SKILL.md H1 标题 `# code-review — ...` → `# code-check — ...`
  - `Grep` + `Edit` 替换全文字面量(~20 处)
- **关键决策**:`git mv` 保留 git blame;`Edit` 失败可回滚到 `git mv` 前
- **错误处理**:`git mv` 失败(权限/文件占用)→ 透传 stderr,中断退出
- **依据规范**:`skill-conventions §规则 1` + FR-1

### 模块 2:JSON 同步(对应 FR-2)
- **关键操作**:
  - `Read .claude-plugin/marketplace.json` + `Edit` 字面量
  - `Read plugins/code-skills/.claude-plugin/plugin.json` + `Edit` 字面量
  - `Bash: jq .` 校验 2 个 JSON 合法性
- **关键决策**:`jq` 校验保证 JSON 语法正确
- **错误处理**:`jq` 失败 → 透传 stderr,中断退出
- **依据规范**:`marketplace-protocol §规则 1` + FR-2

### 模块 3:10 个其他 SKILL.md description 同步(对应 FR-3)
- **关键操作**:
  - `Grep -l "code-review" plugins/code-skills/skills/*/SKILL.md` 定位 10 个文件
  - `Read` + `Edit` 每个 SKILL.md 的 description 字段
- **关键决策**:只改 `description` 字段,**不**改 `name` 字段(避免引入额外变更)
- **依据规范**:FR-3 + INV-1

### 模块 4:仓库级 README + CLAUDE.md 同步(对应 FR-4)
- **关键操作**:
  - 仓库根 `README.md` / `README.en.md`
  - `plugins/code-skills/README.md` / `README.en.md`
  - `CLAUDE.md`
- **关键决策**:中英同步改,严格遵循 `doc-conventions §规则 1` 对仗
- **依据规范**:`doc-conventions §规则 1` + FR-4

### 模块 5:13 份项目级规范同步(对应 FR-4)
- **关键操作**:`Grep -l` + `Read` + `Edit` 13 份 `./assistants/rules/*.md`
- **关键决策**:只改引用字面量,**不**改规范条款本身
- **依据规范**:FR-4

### 模块 6:6 个技能模板同步(对应 FR-4)
- **关键操作**:`Grep -l` + `Read` + `Edit` 6 份 `plugins/code-skills/skills/*/templates/*.md`
- **关键决策**:只改引用字面量
- **依据规范**:FR-4

### 模块 7:V0.0.3 当前激活看板同步(对应 FR-4)
- **关键操作**:`Read` + `Edit` V0.0.3/RESULT.md 中 6 处规范引用
- **关键决策**:`code-check` 写入方 / `code-check` 派生改修任务 等描述同步改
- **依据规范**:FR-4

### 模块 8:校验(本概设新增,对应 AC-1.4 / AC-2.2 / AC-2.4 / AC-3.1 / AC-4.1 ~ 4.8)
- **关键操作**:
  - `Grep "code-review" plugins/code-skills/skills/code-check/SKILL.md` 应**无**匹配
  - `Grep "code-review" .claude-plugin/marketplace.json` 应**无**匹配
  - `Grep "code-review" plugins/code-skills/.claude-plugin/plugin.json` 应**无**匹配
  - `Grep "code-review" plugins/code-skills/skills/*/SKILL.md` 应**仅**匹配 `code-check/SKILL.md`
  - `Grep "code-review" README.md README.en.md plugins/code-skills/README.md plugins/code-skills/README.en.md` 应**无**匹配
  - `Grep "code-review" CLAUDE.md` 应**无**匹配
  - `Grep "code-review" assistants/rules/*.md` 应**无**匹配(本需求范围内)
  - `Grep "code-review" plugins/code-skills/skills/*/templates/*.md` 应**无**匹配
  - `Grep "code-review" assistants/V0.0.3/RESULT.md` 应**无**匹配
  - `Grep "code-review" assistants/V0.0.0/ assistants/V0.0.1/ assistants/V0.0.2/ assistants/V0.0.3/review/` 应**命中**(历史不追溯)

---

## 5. 算法与逻辑

### 算法 1:`code-review` → `code-check` 字面量替换(核心)

```
function renameCodeReview(workingDir):
  # 1. 目录重命名
  if exists(workingDir + "/plugins/code-skills/skills/code-review"):
    Bash: git mv code-review code-check
  else:
    log("⚠ 目录不存在,可能已重命名")
    return ERROR

  # 2. 改 SKILL.md frontmatter
  content = Read(code-check/SKILL.md)
  content = content.replace("name: code-review", "name: code-check")
  Write(code-check/SKILL.md, content)

  # 3. 改 H1 标题
  content = Read(code-check/SKILL.md)
  content = content.replace("# code-review — ", "# code-check — ")
  Write(code-check/SKILL.md, content)

  # 4. 替换全文"code-review"字面量(保留中点"·"等)
  Bash: grep -l "code-review" code-check/SKILL.md
  # 已知:全文 ~20 处字面量
  # 逐处 Edit 替换
```

### 算法 2:JSON 字面量同步

```
function syncJSON():
  # marketplace.json
  content = Read(.claude-plugin/marketplace.json)
  content = content.replace('"code-review"', '"code-check"')  # keywords + description
  content = content.replace('./skills/code-review', './skills/code-check')  # skills[] path
  Write(.claude-plugin/marketplace.json, content)
  Bash: jq . .claude-plugin/marketplace.json  # 校验

  # plugin.json
  content = Read(plugins/code-skills/.claude-plugin/plugin.json)
  content = content.replace('"code-review"', '"code-check"')  # keywords
  content = content.replace("code-review", "code-check")  # description
  Write(plugins/code-skills/.claude-plugin/plugin.json, content)
  Bash: jq . plugins/code-skills/.claude-plugin/plugin.json
```

### 算法 3:批量字面量同步(10 个其他 SKILL.md / 13 份规范 / 6 个模板 / 4 个 README / CLAUDE.md)

```
function batchReplace(fileList, from, to):
  for file in fileList:
    content = Read(file)
    if not content.includes(from):
      log(f"⚠ {file} 不含 {from},跳过")
      continue
    newContent = content.replaceAll(from, to)
    if newContent == content:
      log(f"⚠ {file} 替换后无变化")
    Write(file, newContent)
```

---

## 6. 数据结构完整变更(本需求 0)

- **0** 新增实体
- **0** 修改实体
- **0** 数据迁移

---

## 7. 接口细节(本需求 0 新增)

### 7.1 接口总览

| 接口 | 状态 | 备注 |
| --- | --- | --- |
| `/code-check` | 新增(由 `/code-review` 改名) | 硬重命名,FR-1 |
| `/code-review` | 废弃 | 硬重命名后报"未知技能" |

### 7.2 关键决策
- **硬重命名**:`/code-review` → `/code-check`,**不**保留别名
- 用户输入 `/code-review` → Claude Code 路由层报"未知技能"错误

---

## 8. 异常处理

| 异常 | 处理 |
| --- | --- |
| `git mv` 失败 | 透传 stderr,中断退出 |
| `Edit` 失败 | 透传 stderr,中断退出 |
| `jq` 校验失败 | 透传 stderr,中断退出 |
| `Grep` 残留(本需求范围内) | 屏幕输出未替换列表,提示手动处理 |
| 用户输入 `/code-review` | Claude Code 路由层报"未知技能" |

---

## 9. 安全要求

- **鉴权**:`git push` 需要用户授权(由 git 层处理)
- **输入校验**:`/code-check` 参数格式沿用既有(需求编码 `REQ-NNNNN`)
- **敏感数据**:本需求**0**涉及
- **防注入**:本需求**0**涉及
- **审计**:commit message 严格遵循 `chore(<scope>): <subject>` 格式

---

## 10. 状态机 / 流程

- 沿用既有"## 工作流程"状态机(本需求**0**引入新状态)
- `code-check` 状态机与 `code-review` 完全一致

---

## 11. 性能与资源

- 关键路径耗时目标:< 5 秒(10 个任务总耗时)
- 并发上限:本需求**不**涉及并发
- 资源限制:无
- 缓存策略:无
- 批量/异步:无
- 降级策略:无

---

## 12. 测试要点

- **AC-1.x**:技能入口硬重命名(4 条)
- **AC-2.x**:JSON 同步(4 条)
- **AC-3.x**:10 个其他 SKILL.md(3 条)
- **AC-4.x**:README + 规范 + 模板 + 看板(8 条)
- **AC-5.x**:历史不追溯(2 条)
- **AC-6.x**:行为不变(3 条)
- **INV-1 ~ INV-9**:9 条不变量自检

---

## 13. 关联编码计划

PLAN.md 中本详细设计对应的所有任务编号:TASK-REQ-00022-00001 ~ TASK-REQ-00022-00010(共 10 个任务)

| 任务编号 | 任务标题 | 对应设计点 |
| --- | --- | --- |
| TASK-REQ-00022-00001 | [重命名] code-review/ → code-check/(目录 + frontmatter + H1 + 全文字面量) | FR-1 |
| TASK-REQ-00022-00002 | [字面量改] .claude-plugin/marketplace.json 全部同步改 | FR-2 |
| TASK-REQ-00022-00003 | [字面量改] plugins/code-skills/.claude-plugin/plugin.json 全部同步改 | FR-2 |
| TASK-REQ-00022-00004 | [字面量改] 10 个其他 SKILL.md 的 description 字段同步 | FR-3 |
| TASK-REQ-00022-00005 | [字面量改] 仓库根 2 README + 仓库内 2 README 同步 | FR-4 |
| TASK-REQ-00022-00006 | [字面量改] CLAUDE.md 同步 | FR-4 |
| TASK-REQ-00022-00007 | [字面量改] 13 份项目级规范同步 | FR-4 |
| TASK-REQ-00022-00008 | [字面量改] 6 个技能模板同步 | FR-4 |
| TASK-REQ-00022-00009 | [字面量改] V0.0.3 当前激活看板同步 | FR-4 |
| TASK-REQ-00022-00010 | [校验] Grep 全范围校验(本需求范围内 0 残留 + 历史不追溯) | AC-1.4 / AC-2.2 / AC-2.4 / AC-3.1 / AC-4.1 ~ 4.8 / AC-5.1 / AC-5.2 |

---

## 14. 待澄清 / 未决项

| 编号 | 内容 | 状态 |
| --- | --- | --- |
| (无) | 本需求**0**待澄清;6 决策 + 9 不变量 + 10 任务全部已锁定;7 FR / 6 NFR / ~33 AC / 9 INV 全部已锁定 | 0 待澄清 |

---

## 15. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-07 | v1 | 初始创建 | 完成首次详细设计,对应 PLAN.md v1 的 10 个任务(全部开发=已完成,测试=不适用);7 维度优先级已确认(功能性=中,其余=N/A 或沿用);0 派生"更新看板"任务(沿用 REQ-00017 强约束) | wangmiao |
