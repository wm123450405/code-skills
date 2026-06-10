# 关联设计 — REQ-00029
更新时间:2026-06-10 11:30
版本:V0.0.3

## 1. 同版本关联设计

| 关联设计 | 版本 | 关联点 | 对本需求的影响 |
| --- | --- | --- | --- |
| REQ-00026 技能描述通用化扫除 | V0.0.3 | code-dashboard description 段去 `<本仓库>` 占位符 | 0 改 frontmatter(INV-1) |
| REQ-00028 新增 code-answer 技能 | V0.0.3 | 与 code-dashboard 横向正交(只读查询 vs 看板上报) | 0 改 code-answer SKILL.md |

## 2. 跨版本关联设计

| 关联设计 | 版本 | 关联点 | 对本需求的影响 |
| --- | --- | --- | --- |
| REQ-00023 简化 /code-dashboard 输出为 4 段 | V0.0.2 | code-dashboard 当前总览 4 段格式 + 屏显 ≤ 12 行约束 | 本需求**部分回退**(5 类状态压缩 + 进度条解释行删除 + 建议单行),但 4 段结构保留(用户澄清) |
| REQ-00025 任务编号双正则兼容 | V0.0.2 | code-dashboard §附录 A 双正则透传 | 0 改(INV-2 字节级保留) |

## 3. 规则层关联

| 规则文件 | 关联点 | 对本需求的影响 |
| --- | --- | --- |
| `dashboard-conventions.md §规则 1` | 看板字段扩展需三方同步 | 本需求 0 改字段(INV-4),不触发本规则 |
| `skill-conventions.md §规则 1` | SKILL.md frontmatter 字节级保留 | INV-1 锁定 frontmatter 0 改 |
| `module-conventions.md §规则 1` | 技能资源摆放 | 本需求 0 加新资源(纯 SKILL.md 改造) |
| `encoding-conventions.md §规则 1` | 任务编号正则 | INV-2 锁定 |
| `doc-conventions.md` | 文档格式 | 本需求遵循(标题 + 区段 + 表格) |

## 4. 横向正交技能

| 技能 | 关联 | 影响 |
| --- | --- | --- |
| code-version | 提供 `.current-version` | 0 改 |
| code-require | 产出 `require/<REQ>/RESULT.md` | 0 改 |
| code-design | 产出 `design/<REQ>/RESULT.md` | 0 改 |
| code-plan | 产出 `plan/<REQ>/PLAN.md` | 0 改 |
| code-it | 推进"任务清单" | 0 改 |
| code-unit | 推进"测试状态" | 0 改 |
| code-fix | 推进"缺陷清单" | 0 改 |
| code-check | 推进"评审发现汇总" | 0 改 |
| code-auto | 编排者 | 0 改 |
| code-publish | 发布手册 | 0 改 |
| code-answer | 只读查询(REQ-00028 新增) | 0 改 |