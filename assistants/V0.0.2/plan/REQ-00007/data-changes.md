# 数据结构完整变更 — REQ-00007

更新时间:2026-06-05 10:10
版本:V0.0.2

## 1. 新增实体:`auto-report.md` 内容结构(运行时产物)

### 1.1 实体总览
| 字段 | 类型 | 约束 | 索引 | 说明 |
| --- | --- | --- | --- | --- |
| `# auto-report — REQ-NNNNN(<需求标题>)` | H1 | 必填 | — | 报告标题 |
| `- 需求编码:REQ-NNNNN` | list item | 必填,5 位纯数字 | — | 需求编码(沿用 `encoding-conventions §规则 1`) |
| `- 所属版本:<版本号>` | list item | 必填,kebab-case(允许字母+数字+`.`) | — | 来自 `.current-version` |
| `- code-auto 起始时间:YYYY-MM-DD HH:mm` | list item | 必填,ISO 8601 简写 | — | 步骤 0a 开始时记录 |
| `- code-auto 结束时间:YYYY-MM-DD HH:mm` | list item | 必填,ISO 8601 简写 | — | 步骤 7 完成时记录 |
| `- 总状态:✓ 完成` | list item | 必填,枚举:`✓ 完成` / `⏹ 用户中止` / `✗ 子技能异常` | — | 终态 |
| `- 总子技能调用次数:N` | list item | 必填,正整数 | — | 6 个子技能调用次数之和 |

### 1.2 关系
- **N/A**:本仓库无数据库,`auto-report.md` 是单文件,无关系
- **关联文件**:
  - `./assistants/<版本号>/require/REQ-NNNNN/RESULT.md`(同目录,需求产物)
  - `./assistants/<版本号>/design/REQ-NNNNN/RESULT.md`(上游概要设计)
  - `./assistants/<版本号>/plan/REQ-NNNNN/{RESULT,PLAN}.md`(上游详细设计)

### 1.3 存储选型
- **文件**:`auto-report.md`(Markdown 文本)
- **理由**:本仓库所有产物均为 Markdown 文件(约定俗成);`code-publish` 的 `publish/DEPLOY.md` / `UPDATE.md` / `Q&A.md` 同理

### 1.4 迁移脚本
- **N/A**:`auto-report.md` 是**新建文件**,不涉及迁移
- **首次创建**:由 `code-auto` 步骤 7 完成分支的 `Write` 工具创建
- **重复执行覆盖**:同名文件直接覆盖(`Write` 工具的默认行为)

### 1.5 依据规范
- `encoding-conventions.md §规则 1`(需求编码格式)
- NFR-6(幂等覆盖语义)
- NFR-7(写入时机)

---

## 2. 修改实体:`marketplace.json`

### 2.1 实体总览
| 字段 | 类型 | 约束 | 变更类型 | 说明 |
| --- | --- | --- | --- | --- |
| `plugins[].skills` | string array | 必填,相对路径以 `./` 开头 | **修改**(追加 1 项) | 在末尾追加 `./skills/code-auto` |

### 2.2 当前值
```json
{
  "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
  ...
  "plugins": [
    {
      ...
      "skills": [
        "./skills/code-require",
        "./skills/code-design",
        "./skills/code-plan",
        "./skills/code-it",
        "./skills/code-unit",
        "./skills/code-review",
        "./skills/code-fix",
        "./skills/code-version",
        "./skills/code-init",
        "./skills/code-rule"
      ]
    }
  ]
}
```

### 2.3 变更后值
```json
{
  ...
  "plugins": [
    {
      ...
      "skills": [
        "./skills/code-require",
        "./skills/code-design",
        "./skills/code-plan",
        "./skills/code-it",
        "./skills/code-unit",
        "./skills/code-review",
        "./skills/code-fix",
        "./skills/code-version",
        "./skills/code-init",
        "./skills/code-rule",
        "./skills/code-auto"     ← 新增
      ]
    }
  ]
}
```

### 2.4 兼容性策略
- **追加不修改已有项**:Claude Code 加载时按数组顺序,新增项在末尾不影响已有项
- **JSON Schema 校验**:仍然合法(`marketplace-protocol §规则 1` 6 不允许未知字段)
- **`.current-version` 不变**:Claude Code 重启后才会重读 marketplace.json(由 Claude Code 自身行为决定)

### 2.5 排序约定
- 现有数组**未严格按字母序**:`./skills/code-fix` 在 `./skills/code-review` 之后,`./skills/code-version` 在 `./skills/code-fix` 之后
- **本设计**:**沿用现有顺序**,在末尾追加(保持与既有顺序一致,不重排既有项)

### 2.6 依据规范
- `marketplace-protocol.md §规则 1`:
  - `.5` `plugins[].skills` 必须是相对路径数组,以 `./` 开头
  - `.6` 不允许未知字段
  - `.3` `plugins[].version` 与 `plugin.json` 一致(本变更不动)

---

## 3. 修改实体:`plugins/code-skills/README.md`

### 3.1 实体总览
| 字段 | 类型 | 约束 | 变更类型 | 说明 |
| --- | --- | --- | --- | --- |
| `## 主要能力` 区段的技能清单 | Markdown table | 必填,与 `README.en.md` 同次提交 | **修改**(追加 1 行) | 在末尾追加 `code-auto` 行 |

### 3.2 追加行格式(中英对仗)
**中文版**(`plugins/code-skills/README.md`):
```markdown
| `code-auto` | 自动开发编排(接收需求内容,串行驱动 6 个子技能 + 评审循环,完全无人确认) | 调一次 `/code-auto` 即可跑通完整开发周期 |
```

**英文版**(`plugins/code-skills/README.en.md`):
```markdown
| `code-auto` | Automated development orchestration (drives 6 sub-skills serially + review loop, fully non-interactive) | Invoke `/code-auto` once to run a full development cycle |
```

### 3.3 兼容性策略
- **追加不修改已有行**:10 行 → 11 行(其他 10 行字节级保留)
- **中英对仗自检**:H2 数量 / 表格列数 / 表格行数全部一致
- **同次提交**:`git commit` 中同时含 2 个文件(违反 `doc-conventions §规则 1` 视为本规则违反)

### 3.4 依据规范
- `doc-conventions.md §规则 1`(中英同次提交 + 结构对仗)
- `doc-conventions.md §规则 2`(README 必须存在并持续维护)

---

## 4. 修改实体:`plugins/code-skills/README.en.md`

同 §3,英文版,严格对仗(略,详见 §3)。

---

## 5. 修改实体:`assistants/V0.0.2/RESULT.md`

### 5.1 实体总览
| 区段 | 变更类型 | 变更内容 |
| --- | --- | --- |
| 文档头 | 修改 | `最近更新:2026-06-05 09:40 → 10:15` |
| 版本信息 | 修改 | `最近更新` 同步 |
| 详细设计与任务计划汇总 | **追加** | 1 行 REQ-00007 |
| 任务清单 | **追加** | 5 行(T-001 ~ T-005) |
| 里程碑 | **追加** | 2 个(M-1 文档就绪 + M-2 本需求可发布) |
| 变更记录 | **追加** | 1 行 |

### 5.2 详细变更清单(详见 `tasks` 步骤 16A)
- **详细设计与任务计划汇总**:1 行
- **任务清单**:5 行(T-001 ~ T-005)
- **里程碑**:2 个
- **变更记录**:1 行
- **文档头/版本信息**:2 处

### 5.3 兼容性策略
- **追加不修改已有行**:看板已有 70+ 行变更记录,本设计追加 1 行
- **责任划分**:本技能负责"详细设计与任务计划汇总" / "任务清单" / "里程碑" / "变更记录" 区段(已在 CLAUDE.md 文档头明文规定)

### 5.4 依据规范
- `dashboard-conventions.md §规则 1`(字段约定不扩展,本设计只追加行)

---

## 6. 新增实体:`code-auto` SKILL.md(物理文件)

### 6.1 实体总览
| 字段 | 类型 | 约束 | 说明 |
| --- | --- | --- | --- |
| 路径 | string | 必填 | `plugins/code-skills/skills/code-auto/SKILL.md` |
| 行数 | integer | 600 ± 20% | 预计 480 ~ 720 行 |
| 字节数 | integer | ~25 KB | Markdown 文本 |
| frontmatter | YAML | 必填 | `name: code-auto` + 完整 description |

### 6.2 frontmatter schema
```yaml
---
name: code-auto
description: 自动开发编排(版本感知)。接收 1 个需求内容,按 `code-require` → `code-design` → `code-plan` → `code-it`(+ `code-unit` 条件)→ `code-review` 循环(派生任务自动修复)的固定顺序,串行驱动 6 个子技能完成完整开发周期,过程中所有 `AskUserQuestion` 自动选推荐项,完全无需用户确认;支持 `Ctrl+C` 中止 + 异常立即中断 + 完成时输出报告到 `auto-report.md`。在 `code-version` 之后、其他 `code-*` 之前作为顶层入口使用;也可用作"从需求到代码 + 单测 + 评审全自动跑通"的一键命令。
---
```

### 6.3 章节结构
详见 `module-details.md` 章节表(15 章节 + 行数预算)。

### 6.4 兼容性策略
- **新建文件,无兼容性问题**
- **不修改其他 11 个 SKILL.md**(FR-8.AC-8.1)

### 6.5 依据规范
- `skill-conventions.md §规则 1`(frontmatter 必含 name+description)
- `module-conventions.md §规则 1`(SKILL.md 在技能根目录,无子目录)

---

## 7. 数据迁移 / 灰度 / 回滚

### 7.1 迁移
- **N/A**:`code-auto` 是**全新**技能,无历史数据需迁移
- **N/A**:`auto-report.md` 是**全新**文件类型,无历史数据

### 7.2 灰度
- **N/A**:`code-auto` 是**按需触发**技能(用户调才跑),无需灰度
- **回滚 = 禁用**:用户**不调** `code-auto` 即可视为"灰度关闭"

### 7.3 回滚方案
**3 步回滚**(任一时刻可执行):
1. `git revert <提交哈希>`(提交整体回滚)
2. 或手动删除:
   - `rm plugins/code-skills/skills/code-auto/SKILL.md`
   - `Edit marketplace.json` 移除 `./skills/code-auto` 行
   - `Edit README.md` + `README.en.md` 移除 `code-auto` 行
3. **用户可见影响**:Claude Code 重启后不再能调 `code-auto`(marketplace.json 生效)

**回滚无副作用**:
- 6 个子技能 SKILL.md **字节级保留**(FR-8.AC-8.1)
- 看板"概要设计清单" / "详细设计与任务计划汇总" / "任务清单" 可保留为历史(无需删除)
- 已写的 `auto-report.md` 文件可保留(无副作用)

---

## 8. 总结

| # | 实体 | 状态 | 变更字段 | 对应任务 |
| --- | --- | --- | --- | --- |
| 1 | `auto-report.md` | 新增(运行时) | (新建) | T-001(运行时) |
| 2 | `marketplace.json` | 修改 | `plugins[].skills` 追加 1 项 | T-002 |
| 3 | `README.md`(中文) | 修改 | 技能清单追加 1 行 | T-003 |
| 4 | `README.en.md`(英文) | 修改 | 技能清单追加 1 行 | T-003 |
| 5 | `V0.0.2/RESULT.md` | 修改 | 4 区段追加 + 文档头 2 处 | T-004 |
| 6 | `code-auto/SKILL.md` | 新增 | (新建) | T-001 |

**0 个数据库表变更,0 个字段类型变更,0 个索引变更**。
