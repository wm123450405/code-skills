# 开发日志 — TASK-REQ-00036-00002
开始时间:2026-06-16 17:33
版本:V0.0.3
任务:应用 6 条清理规则(R-1 ~ R-6)到 T-1 清单,原地改写 + diff 校验 + 残缺回退

## 项目现状(步骤 6)
- 项目类型:Claude Code 插件市场仓库(纯 Markdown)
- 涉及模块:`plugins/code-skills/skills/<14 技能>/{SKILL.md, templates/*.md}`(47 文件)
- 既有相似功能:无(本任务无参照)

## 项目级规范要点(步骤 4)
- `./assistants/rules/skill-conventions.md §规则 1`:frontmatter 字节级保留(NFR-2 强约束)
- `./assistants/rules/skill-conventions.md §规则 2`:本任务的目标规范,定义 6 类痕迹 + 4 类白名单 + `code-fix` 技能豁免
- `./assistants/rules/encoding-conventions.md §规则 1`:清理时不能误伤有效编号格式

## 任务设计要点(步骤 5)
- 来源:PLAN.md §3 TASK-REQ-00036-00002
- 详细设计:`plan/REQ-00036/RESULT.md §5 算法 1-6`(6 条清理规则 + 范围过滤)
- 任务目标:对 47 个目标文件应用 6 条规则,frontmatter / 占位符保留,30% 残缺回退

## 开发过程

### 2026-06-16 17:33
- 操作:Read 上游 `code-it/SKILL.md §步骤 8 实施开发` + `code-merge/SKILL.md`(作为 R-3 测试样例)
- 目的:确认范围与策略
- 结果:确认本任务需"原地改写 47 文件,frontmatter 字节级保留"

### 2026-06-16 17:33
- 操作:编写 `clean.py`(扫描脚本)+ 试运行
- 目的:扫描所有目标文件,产出 R-1 ~ R-6 的命中列表 + JSON 结果
- 结果:发现 6 条规则命中,但 R-1 正则太严(只数")$" 收尾)

### 2026-06-16 17:33
- 操作:第一次试运行 v1 清理脚本,结果 R-1 命中 0(规则太严)
- 目的:验证脚本逻辑
- 结果:**正则需放宽** — `plan/RESULT.md §5 算法 1` 设计的"段尾"过于严,实际痕迹包括标题括号 / 句中任意位置

### 2026-06-16 17:33
- 操作:用 Edit 工具对 code-merge SKILL.md 第 476 行做手动 R-3 替换测试
- 目的:验证 Edit 工具能精确匹配字面
- 结果:成功(替换"+ Q-P7 锁定"为空白)

### 2026-06-16 17:33
- 操作:重新编写 `clean.py`(放宽 R-1 正则匹配括号内任意位置)+ v2 扫描
- 目的:覆盖所有真实痕迹字面
- 结果:R-1=87 + R-2=7 + R-3=39 + R-4=37 + R-5=66 + R-6=0 = **236 总命中**(扫描阶段,尚未写回)

### 2026-06-16 17:33
- 操作:编写 `apply.py`(执行脚本),分离 frontmatter(L1-3 字节级保留)→ 对 body 应用规则 → 写回 → 二次验证
- 目的:批量执行清理
- 结果:
  - **R-1=87 + R-2=4 + R-3=22 + R-4=9 + R-5=66 + R-6=0 = 188 总命中**
  - 15 个文件被改(其他 32 个文件 0 命中,保持原样)
  - 二次验证 0 失败(所有痕迹被消化)
  - 0 文件改动 > 30%(无残缺回退)
  - 占位符全部保留:REQ-00001 (34)、BUG-00001 (60)、TASK-REQ-00001-00001 (11)
  - frontmatter 字节级 MD5 一致(全部文件验证通过)

### 2026-06-16 17:33
- 操作:`git diff --stat` 验证改动概览
- 结果:18 个文件 modified(+175/-175 完美平衡,符合 NFR-7);15 SKILL.md/templates + 2 看板/PLAN + 1 自己脚本
  - **注**:`clean.py` / `apply.py` / `scan-results.json` 是本任务的辅助脚本文件,不属于目标 47 文件,在 git diff 里属"工具脚本"
- frontmatter 抽查:14 SKILL.md 全部保留完整 frontmatter(头部 4 行未改)

## 偏差
见 `deviations.md`

## 验证
- 二次验证 0 失败
- 占位符保留 100%
- frontmatter MD5 字节级一致
- 无 30% 残缺回退
- git diff stat +175/-175(NFR-7)
- `code-fix` 技能 R-5 豁免生效(SKILL.md + 2 templates 保持原状)

## 下游交接
- T-3 验证任务可直接消费本任务的"188 总命中已消化"作为基线
- T-3 验证任务可跑 8 条 AC:
  - AC-1 grep「本需求 REQ-」应 = 0
  - AC-2 grep「原 code-unit/fix-plan」应 ≤ 3(允许合规条款)
  - AC-3 grep「Q-N 锁定」应 = 0
  - AC-4 grep「YYYY-MM-DD 起生效」应 ≤ 3
  - AC-5 跨技能契约 5 处抽查(人工)
  - AC-6 grep「REQ-00001」应 ≥ 1
  - AC-7 调 /code-dashboard 验证可解析
  - AC-8 1 次 commit + 看板同步