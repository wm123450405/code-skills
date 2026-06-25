# 工作日志 — TASK-REQ-00040-00004

开始时间:2026-06-25
版本:V0.0.3
任务编码:TASK-REQ-00040-00004
任务标题:[修改] assistants-layout.md 同步追加 reproduce/ 子目录行
触发/来源:详细设计

## 项目现状(步骤 6 记录)

### 项目类型
- 仓库:`code-skills` Claude Code 插件市场仓库
- 主体:Markdown 技能库(14 个 `code-*` 技能)
- 改造目标:`code-fix/templates/assistants-layout.md`(目录结构说明模板)

### 既有 `assistants-layout.md` 现状(T-001/T-002/T-003 完成后)
- 文档(line 1-38)含 3 段:目录结构(line 7-23 ASCII 树)/ 关键约束(line 25-30)/ 文件名约定(line 32-37)
- 目录树(line 7-23)展示 `code-fix` 维护的 `fix/<BUG-NNN>/` 子目录结构,BUG-00001 完整列(line 12-19)7 子文件 + BUG-00002 简略占位(line 20-22)
- T-001/T-002/T-003 完成后,**当前 7 子文件**(line 13-19)是 BUG-00001 子目录的完整列表;本任务**新增 1 行**(reproduce/)插入到 line 19 后 + line 20 前,line 20 起 BUG-00002 简略占位结构保留

### 既有相似功能(REQ-00037 沿用)
- `code-fix` 是纯登记型(沿用 REQ-00027 / REQ-00037)
- `code-fix` 状态推进路径沿用 REQ-00037

## 项目级规范要点(步骤 4 记录)

13 份项目级规范全部沿用,**0 触发**新增约束:

- `skill-conventions §规则 1`:SKILL.md frontmatter 必含;**强约束** 字节级保留;模板**不**含 frontmatter 但**0 触发**(沿用)
- `skill-conventions §规则 2`:SKILL.md / templates/ 不得含 6 类开发痕迹字面;**强约束** 本任务**不**在 `assistants-layout.md` 中写"本需求 REQ-00040 新增" 等字面
- `dashboard-conventions §规则 1`:看板字段扩展需三同步;**0 触发**
- `encoding-conventions §规则 1-4`:3 类编码正则;**0 触发**
- `module-conventions §规则 1`(DEPRECATED):**0 触发**
- `directory-conventions`(规则 1 占位):**0 触发**
- `dependency-conventions.md`(规则 1 占位):**0 触发**
- `commit-conventions.md`(规则 1 占位):**0 触发**

## 任务设计要点(步骤 5 记录)

### PLAN.md §3 任务详情(沿用)
- 目标:在 `code-fix/templates/assistants-layout.md` §"## 目录结构" 段,`fix/<BUG-NNN>/` 子目录列表中追加 `reproduce/` 行
- 涉及文件:`plugins/code-skills/skills/code-fix/templates/assistants-layout.md`
- 关键变更:在 BUG-00001 子目录列表末尾(line 19 `deviations.md` 后)追加 1 行 `│ └── reproduce/ # 复现产物(由 code-fix 步骤 6 末尾生成,可选)`
- 边界与异常:模板**不**含开发痕迹字面
- 验证手段:静态校验(新行存在 + 既有结构完整)

### 详细设计 §4.5(沿用)
- 模块 5:`assistants-layout.md` 同步更新
- 路径:`fix/<BUG-NNN>/` 子目录列表 line 19 后
- 关键变更字面:`│ └── reproduce/ # 复现产物(由 code-fix 步骤 6 末尾生成,可选)`
- 不修改:顶层目录结构 + 其他 6 个 `code-fix` 子目录(`RESULT.md` / `investigation.md` / `fix-plan.md` 等,沿用)

## 开发过程

### 2026-06-25 14:45
- **操作**:`Read assistants-layout.md` 完整内容 + `Bash: grep -n` 验证 line 10-22 子目录列表位置
- **目的**:验证修改前的字面,作为 `Edit` 的精确锚点
- **结果**:成功(line 12 是 BUG-00001 头;line 13-19 是 BUG-00001 子目录 7 行;line 20 是 BUG-00002 头;line 21 是 `│ └── ...` 占位;line 22 是 `└── ...`)

### 2026-06-25 14:46
- **操作**:`Edit assistants-layout.md` 在 BUG-00001 子目录列表末尾(line 19 `deviations.md` 后 + line 20 `BUG-00002/` 前)追加 1 行 `reproduce/`
- **目的**:落地 D-8 / PLAN.md T-004 关键变更
- **结果**:成功(新行 line 20 插入,line 21 变为 BUG-00002 头,后续 line 26 关键约束 / line 33 文件名约定仅位置后移 1 行,字面未变)

### 2026-06-25 14:47
- **操作**:`Bash: grep -n` 验证 + `Bash: grep -c "本需求 REQ-00040" / "沿用原"` 校验零开发痕迹
- **目的**:验证 reproduce/ 行位置正确 + 既有结构完整 + 零开发痕迹字面
- **结果**:
 - reproduce/ 行(line 20)位置正确
 - 既有结构完整(line 12 BUG-00001 头 + line 21 BUG-00002 头 + line 26 关键约束 + line 33 文件名约定)
 - 0 命中"本需求 REQ-00040" / "沿用原" / "Q-X 锁定" 等开发痕迹字面

## 过程产物

- `work-log.md`:本文档(始终生成)
- `deviations.md`:0 偏离(始终生成)
- `unit-test-results.md`:占位(本任务不涉及函数级代码改动)
- `compile-and-run.md`:**不生成**(纯 Markdown 改造)
- `test-results.md`:**不生成**(测试状态 = 不适用)
- `process-doc-decisions.md`:本决策文件(有"不生成"项,需写)

## 结论

T-004 核心改动完成。BUG-00001 子目录列表末尾追加 1 行 `reproduce/`;既有 7 子文件 + 关键约束 + 文件名约定 段全部字节级保留;AC-7 / AC-11 静态校验通过(下一步 T-005 端到端验证时复核)。