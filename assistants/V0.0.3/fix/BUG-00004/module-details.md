# 模块详细化 — BUG-00004

更新时间:2026-06-22 20:30
版本:V0.0.3

## 模块 1:`code-it/SKILL.md` §过程文档判定接入

- **路径**:`plugins/code-skills/skills/code-it/SKILL.md`
- **关键类/函数**:本仓库**无**类/函数(纯 Markdown 技能定义)
- **关键子步骤**:
 - `### 步骤 8.7 — 过程文档自适应判定执行`(新增):
 - **目标**:把"## 过程文档自适应判定"章节(line 101-138)定义的判定准则**物化**为可执行的 `decisions` 字典
 - **输入**:`taskNum` / `taskType` / `changedFiles` / `testable`(从步骤 0~8.6 累积)
 - **输出**:`decisions: { workLog, compileAndRun, deviations, testResults, unitTestResults, kanbanChangeLog, processDocDecisions }` 各为 `'生成' \| '不生成'`
 - **执行流**:
 1. 物化 `decisions`(伪代码见 RESULT.md §5 算法 1)
 2. 屏显契约:`✓ code-it 过程文档判定完成:生成 N / 跳过 M`(沿用既有"执行流程"小节 7 步)
 3. 若 `decisions.processDocDecisions == '生成'` → `Write code/<任务>/process-doc-decisions.md`
 - **状态归属**:`decisions` 是**运行时变量**(不持久化到文件)
 - **错误处理范式**:`process-doc-decisions.md` 写入失败 → 屏显 `⚠`,不阻断(沿用 E-1)
 - **日志埋点**:`✓ code-it 过程文档判定完成:生成 N / 跳过 M`
- `### 步骤 9 编译验证`(改造):
 - **改造点**:开头加守卫 `if decisions.compileAndRun == '不生成': log('⏭ 步骤 9 跳过'); return`
 - **既有逻辑**(字节级保留):"检测构建命令 / 执行构建 / 记录到 `compile-and-run.md` / 失败处理 / 同步到版本看板"
- `### 步骤 10 启动运行验证`(改造):
 - **改造点**:开头加守卫 `if decisions.compileAndRun == '不生成': log('⏭ 步骤 10 跳过'); return`
 - **既有逻辑**(字节级保留):"检测运行命令 / 执行 / 验证启动成功 / 记录到 `compile-and-run.md` / 同步 / 失败处理"
- `### 步骤 11 测试`(改造):
 - **改造点**:开头加守卫 `if decisions.testResults == '不生成': log('⏭ 步骤 11 跳过'); return`
 - **既有逻辑**(字节级保留):"检测测试命令 / 执行 / 记录到 `test-results.md` / 同步 / 失败处理"
- `### 步骤 13 撰写 RESULT.md`(改造):
 - **改造点**:末尾追加"## 8. 过程文档清单"区段(伪代码见 RESULT.md §5 算法 3)
 - **既有 7 段**(字节级保留):"任务信息 / 改修内容总览 / 详细改动 / 关键决策 / 偏离 / 验证结果 / 已知问题 / 关联任务"
- `### 步骤 16 完善过程文档与汇报`(改造):
 - **改造点**:末尾追加"已生成的过程文档清单" + "已跳过(不生成)的过程文档清单" 2 段
 - **既有 5 段**(字节级保留):"收尾 work-log.md / compile-and-run.md / deviations.md / test-results.md / 向用户汇报"
- **关键调用顺序**:
 1. 步骤 0(版本上下文检测)
 2. 步骤 0a(前置任务守卫,任务分支)
 3. 步骤 1-7(读上游 + 处理前置)
 4. 步骤 8(实施开发)
 5. 步骤 8a(项目可测性守卫)
 6. 步骤 8.5(按需写单测)
 7. 步骤 8.6(逻辑行统计)
 8. **步骤 8.7(本需求新增,过程文档自适应判定执行)** ← 关键改造点
 9. 步骤 9(编译验证,本需求开头加守卫)
 10. 步骤 10(启动验证,本需求开头加守卫)
 11. 步骤 11(测试,本需求开头加守卫)
 12. 步骤 12(错误修复循环)
 13. 步骤 13(写 RESULT.md,本需求末尾追加"## 8. 过程文档清单"区段)
 14. 步骤 14-15(同步 PLAN.md + 看板)
 15. 步骤 16(汇报,本需求末尾追加"已生成/已跳过"列表)
- **并发模型**:N/A
- **资源管理**:N/A
- **错误处理范式**:`process-doc-decisions.md` 写入失败 → 屏显 `⚠`,不阻断(沿用 E-1)
- **日志埋点**:`✓ code-it 过程文档判定完成:生成 N / 跳过 M`
- **依据规范**:`skill-conventions §规则 1/2` + `dashboard-conventions §规则 1`
- **与概要设计的对应**:无上游概要设计(本需求是缺陷修复,直接基于 `fix/BUG-00004/RESULT.md §根因分析`)

## 模块 2:`code-it/templates/RESULT.md` 模板改造

- **路径**:`plugins/code-skills/skills/code-it/templates/RESULT.md`
- **关键章节**(改造):"## 8. 过程文档清单" 区段(line 124 附近)
- **改造点**:在原"过程文档清单"段**末尾**追加"决策依据"子表
- **既有章节**(字节级保留):"## 1 ~ ## 7" + "## 9. 单元测试" + "## 10. 逻辑行统计(由 code-it 内化)" + "## 11. 变更记录"
- **不变量**:
 1. **不**修改章节编号(## 1 ~ ## 11 字节级保留)
 2. **不**触发 `dashboard-conventions §规则 1` 三同步(模板是 skill 内部,非看板字段)
 3. **不**修改 frontmatter(模板**无** frontmatter,N/A)
- **依据规范**:`skill-conventions §规则 1/2`

## 模块 3:6 个技能旁路验证(纯静态校验)

- **路径**:`plugins/code-skills/skills/{code-require,code-design,code-check,code-plan,code-fix,code-init,code-rule}/SKILL.md`(只读,不改)
- **验证产出**:`assistants/V0.0.3/fix/BUG-00004/side-skill-verification.md`(由 T-004 产出)
- **关键验证项**(每技能 1 行):
 1. 过程文档表位置 + 行号
 2. "始终生成"类目数量
 3. "条件生成 / 不适用"类目数量
 4. 是否有 ≥ 2 个"不适用"分支同时触发的场景
 5. 实际过度生成风险(`高` / `中` / `低` / `无`)
- **不变量**:
 1. **不**修改任何 6 个技能 SKILL.md
 2. **不**新增依赖
 3. **不**触发 `dashboard-conventions §规则 1` 三同步
- **依据规范**:`skill-conventions §规则 1/2`
