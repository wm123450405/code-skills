# 代码审查 — REQ-OPT-00003 · 移除板块标题序号,引用处同步改为板块标题

> 所属版本:V0.0.6
> 创建时间:2026-07-24 12:00

## 审查范围

`plugins/code-skills/skills/code.new/` 临时目录(41 个文件)的板块标题序号清理 + 正文 § 引用替换结果。

## 审查维度

### 维度 1:正确性(板块标题无序号)
- ✅ `grep -rn '^#+\s+\d' plugins/code-skills/skills/code.new/` = 0 命中
- ✅ `grep -rn '^#+\s+§\d' plugins/code-skills/skills/code.new/` = 0 命中
- 验证:`Found 0 total occurrences across 0 files`

### 维度 2:边界完整性(代码契约同步)
- ✅ `references/_shared/contracts.md` 字段值表(FR_LIST / NFR_LIST / AC_LIST / RELATED)已同步改为 `## 功能需求(FR)` / `## 非功能需求(NFR)` / `## 验收标准(AC)` / `## 关联需求`
- ✅ `references/faq/common.md` 的章节定位(`## 3. 功能需求(FR)` 等)与占位符说明已同步
- ✅ `templates/req/REQUIRE.md` 与 `references/req/require.md` 模板标题已同步去序号

### 维度 3:误删检查(有效内容保留)
- ✅ `references/merge/SKILL.md` 的 `### 自动行为边界(...保留位置)` 板块未动(本 REQ 不涉及该文件)
- ✅ `references/runtime-environment.md` 的「确认提示模板」/「隐私约束」/「适用范围与术语」等 5 个真实清单未动
- ✅ `references/rule/SKILL.md` 中 `references/_shared/contracts.md` 的「/code rule Type A/B/C 写权限」文字描述保留
- ✅ 所有 frontmatter(`.md` 顶部 YAML)未动(NFR-3)

### 维度 4:文档契约
- ✅ `README.md` / `README.en.md` 顶部 `# 1./2./3.` 未动(用户明确)
- ✅ FR-/NFR-/AC-/E-/INV- 设计编号未动(用户明确)
- ✅ TASK-/BUG-/REQ- 编号、commit scope 未动

## 已知遗留

- `references/rule/SKILL.md:144` 中 `opt.md §3.15` 引用保留——`opt.md` 是项目外文档(原 REQ-OPT-00001 输入材料),不在本 REQ 范围

## 审查结论

- **必须改**:0
- **建议改**:0
- **可选改**:0

**审查通过**(临时目录内)。

## ⚠ 事故记录

执行 DONE 阶段"临时目录替换原目录"时,因 mv 命令误操作(目标 `code/` 已存在 → mv 将 `code.new/` 嵌套为 `code/code.new/`,而非覆盖) + 后续 `git reset` + `git checkout` 链式操作,导致:
1. 临时目录 `code.new/` 被嵌套进 `code/` 后,在 checkout 链路中被 `rm -rf` 一并删除
2. 所有 370+ 处清理成果丢失
3. 用户决策"接受现状":不发生代码变更,仅保留文档产物

**本 REQ 代码侧未生效**;清理逻辑已验证正确(临时目录内 grep 验证通过),但需后续会话续跑。

## 行数变化统计(估算)

| 类别 | 数量 |
|------|------|
| `## N.` 标题清理 | ~30 处 |
| `### N.N` 标题清理 | ~50 处 |
| `#### N.N` 标题清理 | ~12 处 |
| `## §N` 标题清理 | ~30 处 |
| `### §N.N` 标题清理 | ~80 处 |
| `#### 9a/9b/9c/9d` 标题清理 | 4 处 |
| `#### 5a/5a-1/5b/5c` 标题清理 | 4 处 |
| `#### 3a/3b` 标题清理 | 2 处 |
| `## §A/§B/§C/§D` 标题清理 | 4 处 |
| `### N. <占位>` 清理 | 4 处 |
| 正文 § 引用清理 | ~150 处 |
| **合计标题+引用清理** | **~370 处** |

## 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-07-24 12:00 | v1 | 初始创建 | 代码审查完成;0 必须改;临时目录 41 文件全清 | wangmiao |