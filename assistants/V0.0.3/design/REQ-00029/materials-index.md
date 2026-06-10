# 材料登记 — REQ-00029
更新时间:2026-06-10 11:30
版本:V0.0.3

## 项目级规范
| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `skill-conventions.md` | 技能规范 | SKILL.md frontmatter 字节级保留(name + description) |
| `module-conventions.md` | 技能规范 | 技能资源摆放(`templates/` / `guidelines/` / `checklists/`);无子目录 |
| `dashboard-conventions.md` | 看板规范 | 看板字段扩展需三方同步(`version-RESULT.md` + `CLAUDE.md` + 本规则) |
| `doc-conventions.md` | 文档规范 | 标题 + 区段 + 表格;变更记录;不臆造 |
| `encoding-conventions.md` | 编码规范 | 任务编号正则(`^TASK-(REQ|BUG)-\d{5}-\d{5}$` / `^(REQ|BUG)-\d{5}-\d{5}$` 双格式兼容) |
| `naming-conventions.md` | 命名规范 | kebab-case;具体规则沿用 |
| `coding-style.md` | 编码风格 | 简洁;自解释命名 |
| `commit-conventions.md` | 提交规范 | `chore(<scope>): <msg>` 格式 |
| `directory-conventions.md` | 目录规范 | 路径以 CWD 为基准 |

## 上游需求
- 来源:`./assistants/V0.0.3/require/REQ-00029/RESULT.md`
- 版本:v1(2026-06-10 11:00)
- FR:8 条 / NFR:7 条 / AC:8 条 / 待澄清:3 条(沿用既有)

## 项目现状(本次扫描)

### 项目类型
- 类型:Claude Code marketplace 插件仓库(`code-skills`)
- 技能数:11 个 `code-*` 技能 + `code-publish` + `code-dashboard` + `code-answer` = 13 个

### 改造目标文件
- `plugins/code-skills/skills/code-dashboard/SKILL.md`(454 行,3 大段:§输出 + §工作流程 + §附录 A/B/C)
- **改造锚点**:
  - L77-99 §输出 总览契约样例 → 改
  - L101-107 §输出 退化 + 总行数说明 → 改
  - L182-200 §工作流程 步骤 4 段 1 总开发进度 → 改
  - L202-228 §工作流程 步骤 4 段 2 各状态占比 → 改
  - L230-243 §工作流程 步骤 4 段 3 高优缺陷 → 改
  - L245-267 §工作流程 步骤 4 段 4 后续操作建议 → 改
  - L269-273 §工作流程 步骤 4 段 5 需求模式 → 改
- **不改锚点**:L1-3 frontmatter、L109-121 工具使用约定、L275-301 步骤 5 建议生成、L303-306 步骤 6 屏显、L402-420 附录 A、L422-435 附录 B、L437-453 附录 C

### 已有相关技能(本需求横向)
- code-version / code-require / code-design / code-plan / code-it / code-unit / code-fix / code-check / code-auto / code-publish / code-answer — 11 个,**0 改**

### 编码与构建约定
- 本仓库无构建系统,无 lint,无 test 框架(沿用 CLAUDE.md "需与用户确认的约定")
- 提交:`chore(<scope>): <msg>` 格式

## 设计阶段材料登记
- 设计阶段未发现新外部材料
- 所有决策依据:REQ-00029/RESULT.md(8 FR / 8 AC)+ 用户澄清记录 + dashboard-conventions.md + skill-conventions.md