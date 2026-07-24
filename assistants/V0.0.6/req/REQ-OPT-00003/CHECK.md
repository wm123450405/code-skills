# 代码审查 — REQ-OPT-00003 · 移除板块标题序号,引用处同步改为板块标题

> 所属版本:V0.0.6
> 创建时间:2026-07-24 12:00
> 续跑重审:2026-07-24 13:30

## 审查范围

`plugins/code-skills/skills/code/` 41 个文件的板块标题序号清理 + 正文 § 引用替换结果(本次续跑,直接 Edit 原文件,非临时目录)。

## 审查维度

### 维度 1:正确性(板块标题无序号)
- ✅ `grep -rn '^#+\s+(\d+\.|\d+\.\d|§\d|§\d+\.\d)' plugins/code-skills/skills/code/` = 0 命中
- ✅ `grep -rn '§\d+(\.\d+)*' plugins/code-skills/skills/code/` = 0 命中

### 维度 2:边界完整性(代码契约同步)
- ✅ `references/_shared/contracts.md` 字段值表(FR_LIST / NFR_LIST / AC_LIST / RELATED)已同步改为 `## 功能需求(FR)` / `## 非功能需求(NFR)` / `## 验收标准(AC)` / `## 关联需求`
- ✅ `references/faq/common.md` 的占位符映射(原 §1-§6)已同步改为板块标题(设计概述/模块拆分/接口设计/数据设计/方案选型/关键流程)
- ✅ `templates/req/REQUIRE.md` / `templates/req/DESIGN.md` / `templates/req/TASK.md` / `templates/fix/BUG.md` / 3 个 faq export 模板标题已同步去序号

### 维度 3:误删检查(有效内容保留)
- ✅ `references/merge/SKILL.md` 主体内容未动
- ✅ `references/runtime-environment.md` 的「确认提示模板」/「隐私约束」/「适用范围与术语」5 个真实清单未动
- ✅ `references/rule/SKILL.md` 中「`/code rule` Type A/B/C 写权限」文字描述保留
- ✅ 所有 frontmatter(`.md` 顶部 YAML)未动(NFR-3)

### 维度 4:文档契约
- ✅ `README.md` / `README.en.md` 顶部 `# 1./2./3.` 未动(用户明确)
- ✅ FR-/NFR-/AC-/E-/INV- 设计编号未动(用户明确)
- ✅ TASK-/BUG-/REQ- 编号、commit scope 未动

## 已知遗留

- `references/rule/SKILL.md:144` 中 `opt.md 3.15` 引用保留(去掉 `§` 前缀)——`opt.md` 是项目外文档(原 REQ-OPT-00001 输入材料),不在本 REQ 范围

## 审查结论

- **必须改**:0
- **建议改**:0
- **可选改**:0

**审查通过** — 代码侧全部生效。

## 续跑过程摘要(2026-07-24 13:00-13:30)

本次续跑改用「直接 Edit 原文件」策略,避免上次 mv 误操作:

1. 重新进入 CODING 阶段,记录 PROCESS.md 续跑时间
2. 扫描所有 41 个 md 文件的 `^#+\s+(\d|§)` 与 `§\d+(\.\d+)*` 命中,生成完整清单(~190 处标题 + ~150 处引用)
3. 按 5 任务顺序逐文件 Edit:
   - TASK-00001:契约层 + 6 references 详细流程(~110 处)
   - TASK-00002:6 个 language 适配文件(48 处)
   - TASK-00003:9 个 templates 文件(~50 处)
   - TASK-00004:7 个 SKILL.md + fix-register.md 正文 § 引用(~150 处)
   - TASK-00005:`templates/ver/RESULT.md` 2 处 § 引用
4. 验证:`grep` 全 0 命中

## 行数变化统计

| 类别 | 数量 |
|------|------|
| `## N.` / `## §N` 标题清理 | ~50 处 |
| `### N.N` / `### §N.N` 标题清理 | ~130 处 |
| `#### N.N` 标题清理 | ~15 处 |
| 各种占位符标题清理 | 4 处 |
| 正文 § 引用清理 | ~150 处 |
| **合计** | **~350 处** |

## 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-07-24 12:00 | v1 | 初始创建 | 临时目录内审查通过(代码侧未生效) | wangmiao |
| 2026-07-24 13:30 | v2 | 续跑重审 | 直接 Edit 原文件,350+ 处全部生效,grep 0 命中 | wangmiao |