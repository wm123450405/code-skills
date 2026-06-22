# TASK-REQ-00039-00006 — 修正 REQ-00039 T-2 / T-3 / T-4 评审发现(合并)

- 任务编码:TASK-REQ-00039-00006
- 需求编码:REQ-00039
- 所属版本:V0.0.3
- 任务类型:修改
- **触发/来源:审查改修** ← 关键字段,code-it 据此选择不同的输入源
- 严重程度:必须改(包含 1 项必须改 F-T4-1 + 2 项建议改 F-T2-1 / F-T3-1,合并)
- 触发时间:2026-06-22 16:35
- 触发者:code-check(wangmiao)
- 关联原任务:T-2, T-3, T-4(被审查发现问题的任务)
- 关联评审报告:./assistants/V0.0.3/review/REQ-00039/REVIEW-REPORT.md §5
- 状态:待开始
- 责任人:code-it 执行者
- 当前版本:v1

## 1. 任务概述

修正 REQ-00039 的 T-2 / T-3 / T-4 三个修改任务在评审中发现的 3 项问题:

- **F-T4-1(必须改 / 正确性)**:模板 `code-it/templates/RESULT.md` line 124 标题"## 10. 逻辑行统计(由 code-it 内化,新增," 末尾有未闭合的半角逗号 `,`,需删除为"## 10. 逻辑行统计(由 code-it 内化,新增)"
- **F-T2-1(建议改 / 一致性)**:步骤 8.6.3 E-3 字面与 `logic-loc.md` §函数 2 错误处理**字面**基本一致但**任务级 vs 函数级**职责混淆——建议在 E-3 文案中追加"任务级继续下一文件"
- **F-T3-1(建议改 / 一致性)**:步骤 8.13 "总规模优先,新增次之" 字面描述与 `logic-loc.md` §函数 4 算法**字面**有出入——建议在 `code-check/SKILL.md` 步骤 8.13 把"总规模优先,新增次之"改为"先判 totalLoc,再判 newLoc(两个独立发现,可同时触发)"

修正后达成:模板字面干净(无残留逗号);`code-it` / `code-check` SKILL.md 字面与共享库字面完全对齐。

## 2. 问题清单

### 问题 F-1(原 F-T4-1):模板"## 10. 逻辑行统计"小节标题末尾有未闭合的半角逗号

- **位置**:`plugins/code-skills/skills/code-it/templates/RESULT.md` line 124
- **类别**:正确性
- **严重程度**:**必须改**
- **依据**:
 - 规则:`./assistants/rules/skill-conventions.md §规则 1`(模板字面干净)
 - 设计:`./assistants/V0.0.3/plan/REQ-00039/RESULT.md §4.5`(`code-it/templates/RESULT.md` 修改既有 — 模板字面必须与设计稿一致)
 - 需求:`./assistants/V0.0.3/require/REQ-00039/RESULT.md FR-3`(模板示例展示"## 逻辑行统计"小节格式)
 - 关联原任务:T-4 的 `code/TASK-REQ-00039-00004/RESULT.md §2.1`
- **现象**:
 ```markdown
 ## 10. 逻辑行统计(由 code-it 内化,新增,
 ```
 末尾的半角逗号 `,` 是**残留未删除的字面**,**不**是分隔符(逗号后没有 `注` / `说明` 等内容)
- **问题描述**:模板标题字面是 Markdown 标题(`## ...`),末尾的半角逗号 `,` 是**残留未删除的字面**;会导致下游 `code-it` 步骤 8.6 在复制本小节作为 `code/<task>/RESULT.md` 的"## 逻辑行统计"标题时,字面继承此逗号,产生与既有"## 单元测试"小节命名风格不一致的"## 逻辑行统计(由 code-it 内化,新增," 标题
- **建议改修**:
 ```markdown
 ## 10. 逻辑行统计(由 code-it 内化,新增)
 ```
 末尾无逗号,与既有"## 9. 单元测试(由 code-it 内化)" 等其他小节命名风格一致
- **替代方案**:无 — 必须删除残留逗号

### 问题 F-2(原 F-T2-1):步骤 8.6.3 E-3 字面与 `logic-loc.md` §函数 2 错误处理职责混淆

- **位置**:`plugins/code-skills/skills/code-it/SKILL.md` line 762
- **类别**:一致性
- **严重程度**:建议改
- **依据**:
 - 设计:`./assistants/V0.0.3/plan/REQ-00039/RESULT.md §5.5 step 3`(`calcLogicLoc` 任务级聚合隐含"per-file 失败 → 跳过该文件继续")
 - 关联原任务:T-2 的 `code/TASK-REQ-00039-00002/RESULT.md §2.1`
- **现象**:
 ```markdown
 | **E-3** | 变更文件无法访问(权限/不存在) | 跳过该文件 + 屏显警告 |
 ```
- **问题描述**:`code-it` 步骤 8.6.3 E-3 表明"跳过该文件"是步骤 8.6 任务级处理;但 `logic-loc.md` §函数 2 错误处理**没有**"跳过该文件"的语义;两者职责略有混淆——若 `calcLogicLines` 返回 error 对象后,任务级是否仍跳过该文件?(隐含 OK,但字面未明示)
- **建议改修**:
 ```markdown
 | **E-3** | 变更文件无法访问(权限/不存在) | `calcLogicLines` 返回 error 对象,任务级跳过该文件,继续下一文件 + 屏显警告 |
 ```
 明确"per-file 失败不影响其他文件"的语义
- **替代方案**:可不改——`calcLogicLoc` 任务级聚合(详设 §5.5 step 3)隐含"per-file 失败 → 跳过该文件继续",功能上正确;只是字面欠明示

### 问题 F-3(原 F-T3-1):"总规模优先,新增次之" 字面描述与 `logic-loc.md` §函数 4 算法字面有出入

- **位置**:`plugins/code-skills/skills/code-check/SKILL.md` line 440
- **类别**:一致性
- **严重程度**:建议改
- **依据**:
 - 设计:`./assistants/V0.0.3/plan/REQ-00039/RESULT.md §5.6`(`code-check-exceed` 评审级聚合:totalLoc 超返回,newLoc 超返回,null 返回)
 - 关联原任务:T-3 的 `code/TASK-REQ-00039-00003/RESULT.md §2.1`
- **现象**:
 ```markdown
 - 不通过判定(沿用 `logic-loc.md` §函数 4):
 - 总规模超标 ≤10% → "可选"
 - 总规模超标 ≤50% → "建议改"
 - 总规模超标 >50% → "必须改"
 - 新增超标阈值级别同上(**总规模优先,新增次之**)
 ```
- **问题描述**:"总规模优先,新增次之" 在 `code-check` 步骤 8.13 是结论性描述,但 `logic-loc.md` §函数 4 算法是"先 totalLoc 后 newLoc,totalLoc 超则不进入 newLoc 判";两者**字面**有出入——若一个文件 totalLoc 略超阈值(建议改)但 newLoc 远超阈值(必须改),`code-check-exceed` 实际会先返回 totalLoc 的"建议改"发现,**不**返回 newLoc 的"必须改"发现;这与字面表述"总规模优先,新增次之"**矛盾**——"总规模优先"在算法语义上是"短路"而非"级别优先"
- **建议改修**(推荐):
 ```markdown
 - 不通过判定(沿用 `logic-loc.md` §函数 4):
 - 总规模超标 ≤10% → "可选"
 - 总规模超标 ≤50% → "建议改"
 - 总规模超标 >50% → "必须改"
 - 新增超标阈值级别同上(先判 totalLoc,再判 newLoc,两个独立发现可同时触发)
 ```
 把"总规模优先,新增次之"改为"先判 totalLoc,再判 newLoc(两个独立发现,可同时触发)",与 `logic-loc.md` §函数 4 算法字面一致
- **替代方案**:可不改——`code-check-exceed` 实际行为是"totalLoc 超 → 返回;否则 newLoc 超 → 返回;否则 null";"总规模优先"在评审流程上等价于"先看总规模,再看新增";语义可接受,字面欠精确

## 3. 应当改修的文件清单

### 文件 1:`plugins/code-skills/skills/code-it/templates/RESULT.md`

- **关联问题**:F-1(必须改)
- **当前状态**:
 ```markdown
 ## 10. 逻辑行统计(由 code-it 内化,新增,
 ```
 line 124 末尾有未闭合的半角逗号 `,`
- **应改为**:
 ```markdown
 ## 10. 逻辑行统计(由 code-it 内化,新增)
 ```
 line 124 末尾无逗号
- **理由**:模板字面残留;下游 `code-it` 步骤 8.6 复制模板时会继承此逗号,产生与既有"## 单元测试"小节命名风格不一致的标题
- **改动范围**:只改 line 124 标题末尾的半角逗号(删除 1 个字符)

### 文件 2:`plugins/code-skills/skills/code-it/SKILL.md`

- **关联问题**:F-2(建议改)
- **当前状态**:
 ```markdown
 | **E-3** | 变更文件无法访问(权限/不存在) | 跳过该文件 + 屏显警告 |
 ```
 line 762
- **应改为**:
 ```markdown
 | **E-3** | 变更文件无法访问(权限/不存在) | `calcLogicLines` 返回 error 对象,任务级跳过该文件,继续下一文件 + 屏显警告 |
 ```
- **理由**:明确"per-file 失败不影响其他文件"的语义,与 `logic-loc.md` §函数 2 错误处理字面区分("函数级" vs "任务级")
- **改动范围**:只改 line 762 的 E-3 行处理列

### 文件 3:`plugins/code-skills/skills/code-check/SKILL.md`

- **关联问题**:F-3(建议改)
- **当前状态**:
 ```markdown
 - 新增超标阈值级别同上(**总规模优先,新增次之**)
 ```
 line 440
- **应改为**:
 ```markdown
 - 新增超标阈值级别同上(先判 totalLoc,再判 newLoc,两个独立发现可同时触发)
 ```
- **理由**:与 `logic-loc.md` §函数 4 算法字面一致;避免"总规模优先"在算法语义上是"短路"而非"级别优先"的歧义
- **改动范围**:只改 line 440 的"总规模优先,新增次之"描述

## 4. 不需要做的(避免越界)

- 不重构与本任务无关的代码(即使看起来不顺眼)
- 不修改接口签名(除非 F-X 显式要求)
- 不修改测试代码(除非 F-X 显式要求)
- 不动 `plan/REQ-00039/RESULT.md`(那是上游设计,本任务是实现层)
- 不动 `code/TASK-REQ-00039-00002/00003/00004/RESULT.md`(那是历史档案)
- 不重写 `code-it/SKILL.md` 步骤 8.6 整体 / `code-check/SKILL.md` 步骤 8.13 整体 / `code-it/templates/RESULT.md` "## 10. 逻辑行统计"小节整体 — 只改 F-X 显式指出的字面
- 不动 `logic-loc.md` / `logic-loc-defaults.md`(共享库是 single source of truth,只改调用方字面以对齐)
- **不要扩展任务范围**:即使在改修过程中发现其他问题,记到 `deviations.md`,不擅自修复
- 不修改 frontmatter(L1-3 字节级保留,沿用 NFR-3)
- 不修改既有"## 工作流程"小节 / "## 不要做的事"小节 / 既有章节

## 5. 验证手段

- **单元测试**:N/A(本仓库不可测,沿用 V0.0.3 修订)
- **静态校验**:
 1. `grep -n "^## 10\. 逻辑行统计" plugins/code-skills/skills/code-it/templates/RESULT.md` — 确认 line 124 标题末尾**无**逗号
 2. `grep -n "总规模优先" plugins/code-skills/skills/code-check/SKILL.md` — 确认**无**命中(已替换为"先判 totalLoc,再判 newLoc")
 3. `grep -n "E-3" plugins/code-skills/skills/code-it/SKILL.md | head -5` — 确认 line 762 E-3 处理列字面已更新
- **手工验证步骤**:
 1. 读 line 124 模板标题,确认末尾无逗号
 2. 读 `code-it/SKILL.md` 步骤 8.6.3 E-3,确认处理列字面已更新
 3. 读 `code-check/SKILL.md` 步骤 8.13 不通过判定,确认"总规模优先"已替换
- **回退方式**:`Bash: git revert HEAD`(单 commit 模式)

## 6. 关联依据汇总

| 类型 | 路径 | 章节 |
| --- | --- | --- |
| 规则 | `./assistants/rules/skill-conventions.md` | §规则 1(模板字面干净) |
| 规则 | `./assistants/rules/skill-conventions.md` | §规则 1(frontmatter L1-3 字节级保留) |
| 设计 | `./assistants/V0.0.3/plan/REQ-00039/RESULT.md` | §4.5(`code-it/templates/RESULT.md` 修改既有) |
| 设计 | `./assistants/V0.0.3/plan/REQ-00039/RESULT.md` | §5.5(`calcLogicLoc` 任务级聚合) |
| 设计 | `./assistants/V0.0.3/plan/REQ-00039/RESULT.md` | §5.6(`code-check-exceed` 评审级聚合) |
| 设计 | `./assistants/V0.0.3/plan/REQ-00039/RESULT.md` | §5.1 ~ §5.4(4 函数伪代码) |
| 需求 | `./assistants/V0.0.3/require/REQ-00039/RESULT.md` | FR-3(`code-it` 步骤 8 末尾追加 `calcLogicLoc` 子步骤) |
| 需求 | `./assistants/V0.0.3/require/REQ-00039/RESULT.md` | FR-4(`code-check` 步骤 8 评审新增"代码行数超标"发现) |
| 共享库 | `./plugins/code-skills/skills/code-it/lib/logic-loc.md` | §函数 2(错误处理) + §函数 4(`code-check-exceed` 算法) |
| 共享库 | `./plugins/code-skills/skills/code-it/lib/logic-loc-defaults.md` | §默认值(500 / 200)+ §阈值级别 |
| 原任务改修正文 | `./assistants/V0.0.3/code/TASK-REQ-00039-00002/RESULT.md` | §2.1(步骤 8.6 子步骤) |
| 原任务改修正文 | `./assistants/V0.0.3/code/TASK-REQ-00039-00003/RESULT.md` | §2.1(步骤 8.13 子步骤) |
| 原任务改修正文 | `./assistants/V0.0.3/code/TASK-REQ-00039-00004/RESULT.md` | §2.1(模板新增"## 10. 逻辑行统计"小节) |
| 评审报告 | `./assistants/V0.0.3/review/REQ-00039/REVIEW-REPORT.md` | §5(派生的新任务列表)+ §8(整体结论) |
| 评审日志 | `./assistants/V0.0.3/review/REQ-00039/work-log.md` | §任务评审结果(T-2 / T-3 / T-4 详情) |
| 评审清单 | `./assistants/V0.0.3/review/REQ-00039/review-checklist-applied.md` | §检查项应用汇总 |

## 7. 完成定义(DoD)

- [ ] F-1:删除 `code-it/templates/RESULT.md` line 124 末尾的半角逗号 `,`
- [ ] F-2:更新 `code-it/SKILL.md` line 762 E-3 处理列字面
- [ ] F-3:更新 `code-check/SKILL.md` line 440 "总规模优先,新增次之" 字面
- [ ] frontmatter L1-3 字节级保留(对照 `code-it/SKILL.md` + `code-check/SKILL.md` 修改前)
- [ ] 既有"## 工作流程"小节 / "## 不要做的事"小节 / 既有章节字节级沿用
- [ ] `code-it/lib/logic-loc.md` + `code-it/lib/logic-loc-defaults.md` **无修改**(共享库是 single source of truth)
- [ ] 静态校验通过:3 项 grep 命令全部命中预期
- [ ] `deviations.md` 已记录任何额外发现
- [ ] `RESULT.md` 已更新本任务的完成总结

## 8. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-22 16:35 | v1 | 初始创建 | 由 code-check 派生,合并 T-2 / T-3 / T-4 评审发现 = 1 必须改(F-T4-1)+ 2 建议改(F-T2-1 / F-T3-1);3 文件改动 | wangmiao |
