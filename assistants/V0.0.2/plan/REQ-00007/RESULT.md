# REQ-00007 — 详细设计:增加 `/code-auto` 自动开发技能

- 需求编码:`REQ-00007`
- 所属版本:`V0.0.2`
- 上游需求:`./assistants/V0.0.2/require/REQ-00007/RESULT.md`(v1,已锁定,10 FR / 10 NFR / ~40 AC)
- 上游概要设计:`./assistants/V0.0.2/design/REQ-00007/RESULT.md`(v1,已完成首次)
- 遵循规范:`./assistants/rules/` 下 13 个文件(7 强约束 + 6 占位 + 1 DEPRECATED;详见 §3 与 `rule-compliance.md`)
- 状态:已完成(首次详细设计)
- 责任人:wangmiao
- 创建:2026-06-05
- 最近更新:2026-06-05 10:30
- 当前版本:v1

---

## 1. 详细设计概述

在概要设计的基础上,本详细设计把"系统长什么样"细化为"系统怎么写"。核心决策:**5 个任务全部为纯文档型**(写 SKILL.md + 改 JSON + 改 README + 改看板 + 静态自检),0 个代码模块,0 个新依赖,0 个被修改模块(FR-8.AC-8.1 强约束)。`code-auto` 本身是单文件 SKILL.md(~600 行),`auto-report.md` 是运行时由 `code-auto` 在完成时一次性 Write 的产物文件。详细化要点:**(1)** T-001 单任务产 1 个 SKILL.md(Q-P1 锁定 A);**(2)** T-001 步骤 0a 调 `git pull` 与子技能内 0a 重叠(Q-P2 锁定 A);**(3)** 5 任务测试状态全部 `不适用`(Q-P3 锁定 A,本仓库无构建/测试文件)。

---

## 2. 上游引用

### 2.1 需求
- **FR-1** `code-auto` 技能定义与元信息 → §4.1 + §6 模块 M-1
- **FR-2** 接收需求内容 + 启动编排 → §5 算法 1
- **FR-3** 子技能调用顺序与依赖(串行)→ §5 算法 2 + §10 状态机
- **FR-4** 任务循环(对 `PLAN.md` 任务总览的每个任务)→ §5 算法 4
- **FR-5** 评审循环(对 `code-review` 派生任务)→ §5 算法 5
- **FR-6** 用户确认自动化(选推荐项)→ §5 算法 6
- **FR-7** 异常立即中断 + 报告 → §5 算法 7
- **FR-8** 不修改其他 9 个 `code-*` 技能 → §11 修改模块清单(0 个)
- **FR-9** 完整报告(屏幕 + 磁盘)→ §6 接口 4
- **FR-10** 报告留痕 → §6 接口 4 + §7.1

### 2.2 概要设计
- 7 步骤状态机:`§5.1 组件图` + `§6.3 状态机`
- 6 个被驱动子技能(零修改):`§6.2 子技能调用表`
- 2 个模块(M-1 SKILL.md / M-2 auto-report.md):`§4 模块详细化`
- 0 新增依赖 + 0 新增接口:`§10` 总结

### 2.3 规范
- `skill-conventions.md §规则 1`(SKILL.md frontmatter 必含 name+description)
- `module-conventions.md §规则 1`(资源放固定子目录)
- `dashboard-conventions.md §规则 1`(字段约定不扩展)
- `doc-conventions.md §规则 1`(README 中英同次提交 + 对仗)
- `marketplace-protocol.md §规则 1`(`$schema` / `name` / `version` 必填)
- `encoding-conventions.md §规则 1-4`(任务编码双格式兼容正则)
- `migration-mapping.md §规则 1-4`(EXISTING-NNN 不追溯)

---

## 3. 规范遵循

### 3.1 适用的规范文件

| 规范文件 | 类别 | 关键约束 | 本详细设计对应章节 |
| --- | --- | --- | --- |
| `./assistants/rules/skill-conventions.md` | 技能编写 | §规则 1:frontmatter 必含 name+description | §4.1 / §6 模块 M-1 |
| `./assistants/rules/module-conventions.md` | 模块规划(DEPRECATED) | §规则 1:资源放固定子目录 | §4 模块 M-1 |
| `./assistants/rules/dashboard-conventions.md` | 看板 | §规则 1:字段约定不扩展 | §11 看板同步 |
| `./assistants/rules/doc-conventions.md` | 文档 | §规则 1:README 中英同次 + 对仗 | §11.2 T-003 |
| `./assistants/rules/marketplace-protocol.md` | Marketplace | §规则 1:skills `./` 路径数组 | §11.1 T-002 |
| `./assistants/rules/encoding-conventions.md` | 编码格式 | §规则 1-4:任务编码双格式正则 | §6 接口 3.2 + §6 接口 3.3 |
| `./assistants/rules/migration-mapping.md` | 编码迁移 | §规则 1-4:EXISTING-NNN 不追溯 | (不触发) |

**占位规范(6 个,不影响)**:`directory-conventions.md` / `coding-style.md` / `commit-conventions.md` / `dependency-conventions.md` / `framework-conventions.md` / `naming-conventions.md`

### 3.2 自检结论

- **完全合规**的章节:§1 / §2 / §3 / §4 / §5 / §6 / §7 / §8 / §9 / §10 / §11 / §12
- **经用户授权偏离**的章节:**0**
- **待澄清冲突**:**0**

> 详细规范遵循记录见 `rule-compliance.md`(本目录)。

---

## 4. 模块详细化

### 4.1 模块 M-1:`code-auto/SKILL.md`(对应概要设计 §7.2)

#### 关键"组件"(SKILL.md 的"伪代码"视角)

| 组件 | 形式 | 职责 | 对应任务 |
| --- | --- | --- | --- |
| frontmatter | YAML | 技能元信息 | T-001 §关键变更 |
| §5 状态机总览 | Mermaid | 7 步骤状态机可视化 | T-001 |
| §6 子技能调用表 | 表格 | 7 步 × 4 列 | T-001 |
| §7 工作流步骤 | 文字 | 步骤 0a / 0 / 1-3 / 4 / 5-6 / 7 详细 | T-001 |
| §8 数据解析 | 锚点字符串 | 任务编码 + 必须改列表解析 | T-001 |
| §10 报告输出 | 模板 | 屏幕 + 磁盘报告格式 | T-001 |

#### 关键"函数"(语义视角)

| "函数" | 触发时机 | 职责 |
| --- | --- | --- |
| `version_detect()` | 步骤 0 | 读 `.current-version` → `<版本号>` |
| `sub_skill_invoke(skill_name, args)` | 步骤 1-6 | 用 `Skill` 工具调子技能,返回成功/失败 |
| `parse_plan_tasks(plan_md_path)` | 步骤 4 前置 | 解析 `PLAN.md` 任务总览 → 任务编码列表 |
| `parse_review_findings(review_report_path)` | 步骤 5/6 | 解析 `REVIEW-REPORT.md` 评审发现汇总 → "必须改"任务列表 |
| `format_progress(line)` | 步骤 1-6 每步 | 打印进度到 stdout |
| `format_completion_report()` | 完成时 | 拼装完整报告 |
| `write_auto_report(content, target_path)` | 完成时 | 写 `auto-report.md`(失败仅警告) |
| `handle_sigint()` | 收到 SIGINT | 打印中止报告 + 退出 130 |
| `handle_sub_skill_failure(step, stderr)` | 子技能退出码 ≠ 0 | 打印中断报告 + 退出 ≠ 0 |

#### 关键"调用顺序"

```
[启动]
  → version_detect() (步骤 0)
  → sub_skill_invoke("code-require", "<需求>") (步骤 1)
  → sub_skill_invoke("code-design", "REQ-NNNNN") (步骤 2)
  → sub_skill_invoke("code-plan", "REQ-NNNNN") (步骤 3)
  → parse_plan_tasks(plan_path) (步骤 4 前置)
  → for each task:
       sub_skill_invoke("code-it", task) + 可选 sub_skill_invoke("code-unit", task)
  → sub_skill_invoke("code-review", "REQ-NNNNN") (步骤 5)
  → parse_review_findings(review_report_path) (步骤 5 后置)
  → while "必须改" 非空:
       for each derived task:
         sub_skill_invoke("code-it", derived) + 可选 sub_skill_invoke("code-unit", derived)
       sub_skill_invoke("code-review", "REQ-NNNNN")
       parse_review_findings(review_report_path)
  → format_completion_report() (步骤 7 完成分支)
  → write_auto_report(content, auto_report_path) (步骤 7 完成分支)
  → exit 0

(任意步骤) handle_sub_skill_failure() 或 handle_sigint() → exit ≠ 0 / 130
```

#### 内部状态
- **不维护内存状态**(无状态执行器,NFR-8 + Q-11 锁定)
- **不写代码 / 配置 / 数据库**:仅 `Write` 1 个 `auto-report.md`(完成时)
- **不持有任何凭据**

#### 并发模型
- **N/A**:NFR-2 强约束串行
- **无锁 / 无事务 / 无并发原语**

#### 资源管理
- **N/A**:无连接 / 锁 / 缓存
- **单次内存占用**:SKILL.md 上下文 + 子技能输出文本(由 Claude Code 模型层管理)

#### 错误处理范式
- **检测 → 报告 → 退出**(无 try/catch,因 SKILL.md 是 Markdown 而非代码)
- **退出码语义**:
  - `0` = 正常完成
  - `≠ 0` = 子技能异常中断
  - `130` = SIGINT 中止

#### 日志埋点
- **进度输出**(NFR-10):每步打印一行 `[code-auto] 步骤 X/Y:<子技能> <参数>`
- **完成报告**:屏幕 stdout 一次性输出完整报告
- **磁盘留痕**:完成时 `Write` `auto-report.md` 一次性写入
- **不维护日志文件**:无运行日志 / 调试日志

#### 依据规范
- `skill-conventions.md §规则 1`(frontmatter 必含 name+description)
- `module-conventions.md §规则 1`(SKILL.md 在技能根目录)
- `encoding-conventions.md §规则 1-4`(任务编码双格式正则)
- `dashboard-conventions.md §规则 1`(看板解析锚点沿用)

> 详细模块结构见 `module-details.md`(本目录)。

### 4.2 模块 M-2:`auto-report.md`(对应概要设计 §7.3)

#### 路径
`./assistants/<版本号>/require/REQ-NNNNN/auto-report.md`

#### 写入时机(NFR-7 强约束)
- **写入**:`code-auto` 正常完成(全部步骤通过 + 必须改列表空)→ 一次性 `Write`
- **不写入**:子技能退出码 ≠ 0 / SIGINT / 自身崩溃 / `Write` 失败

#### 关键"属性"
- 文件格式:Markdown
- 行数:50-80 行
- 字节数:2-5 KB
- 文件状态:一次性 Write(非增量)
- 同名文件:**覆盖**(NFR-6 强约束)

#### 关键"结构"
详见 `interface-specs.md §1.3` + `data-changes.md §1.1`(标准 schema)。

> 详细模块结构见 `module-details.md`(本目录)。

---

## 5. 算法与逻辑(可直接编码)

### 算法 1:启动解析(FR-2)

```
function algorithm_1_start(input_args):
    # 1. 校验参数
    if input_args is empty:
        print "用法: /code-auto <需求内容>"
        return exit_code = 4
    
    # 2. 拼接参数(若多参数)
    requirement = " ".join(input_args)
    
    # 3. 步骤 0a:git pull
    step_0a_result = run_bash("git pull")
    if step_0a_result.exit_code != 0:
        classify_git_pull_failure(step_0a_result.stderr)
        return exit_code = 2
    
    # 4. 步骤 0:读 .current-version
    version = read_file("./assistants/.current-version")
    if version is None:
        print "未找到 .current-version,请先调 /code-version"
        return exit_code = 3
    
    # 5. 记录起始时间
    start_time = now()
    
    # 6. 进入主循环
    return algorithm_2_main_loop(requirement, version, start_time)
```

- **输入**:`input_args`(string[])
- **输出**:`exit_code`(int)+ 屏幕进度
- **复杂度**:O(1)
- **依赖**:`run_bash` / `read_file` / `print` / `now`(Claude Code 平台工具)
- **关键决策**:`step_0a` 与子技能内 0a 重叠(Q-P2 锁定 A,接受冗余)
- **边界条件**:参数缺失 / `.current-version` 缺失 / `git pull` 失败
- **对应任务**:T-001(SKILL.md §7 步骤 0a + 0)

### 算法 2:主循环(FR-3)

```
function algorithm_2_main_loop(requirement, version, start_time):
    # 1. 步骤 1:code-require
    print_progress("步骤 1/6:code-require")
    result = skill_invoke("code-require", requirement)
    if not result.success: return handle_sub_skill_failure(1, result.stderr)
    req_id = parse_req_id_from_result(result)  # 解析 "REQ-NNNNN"
    
    # 2. 步骤 2:code-design
    print_progress("步骤 2/6:code-design")
    result = skill_invoke("code-design", req_id)
    if not result.success: return handle_sub_skill_failure(2, result.stderr)
    
    # 3. 步骤 3:code-plan
    print_progress("步骤 3/6:code-plan")
    result = skill_invoke("code-plan", req_id)
    if not result.success: return handle_sub_skill_failure(3, result.stderr)
    
    # 4. 步骤 4:任务循环
    algorithm_4_task_loop(req_id, version)
    
    # 5. 步骤 5/6:评审循环
    algorithm_5_review_loop(req_id, version)
    
    # 6. 步骤 7:报告
    return algorithm_7_report(req_id, version, start_time, "完成")
```

- **输入**:`requirement`(string)+ `version`(string)+ `start_time`(datetime)
- **输出**:`exit_code` = 0
- **复杂度**:O(N_task + N_review_loop × N_derived)
- **依赖**:`skill_invoke` / `print_progress`
- **关键决策**:严格串行,每步等子技能返回(NFR-2 + Q-7)
- **边界条件**:子技能退出码 ≠ 0 → 中断(FR-7.AC-7.1)
- **对应任务**:T-001(SKILL.md §7 步骤 1-7)

### 算法 3:解析任务编码(FR-4.AC-4.1,沿用 `code-dashboard NFR-3`)

```
function algorithm_3_parse_task_ids(plan_md_path):
    content = read_file(plan_md_path)
    
    # 锚点 1:定位"任务总览"区段
    section = extract_section(content, "^## 任务总览$")
    if section is None:
        raise "未找到 '任务总览' 区段"
    
    # 锚点 2:解析表格行
    rows = parse_table_rows(section)
    
    # 双格式兼容正则
    new_format = r"^TASK-(REQ|BUG)-\d{5}-\d{5}$"
    old_format = r"^(REQ|BUG)-\d{5}-\d{5}$"
    
    task_ids = []
    for row in rows:
        first_col = row[0]  # 任务编码列
        if re.match(new_format, first_col):
            task_ids.append(first_col)
        elif re.match(old_format, first_col):
            task_ids.append(first_col)  # 旧格式透传
        # else: 跳过(非任务编码行,如表头)
    
    return task_ids
```

- **输入**:`plan_md_path`(string)
- **输出**:`task_ids`(string[])
- **复杂度**:O(N_rows)
- **依赖**:`read_file` / `re.match`
- **关键决策**:新格式优先 + 旧格式透传(沿用 `code-dashboard NFR-3`)
- **边界条件**:文件不存在 / 缺区段 / 无任务编码行
- **对应任务**:T-001(SKILL.md §8.1)

### 算法 4:任务循环(FR-4)

```
function algorithm_4_task_loop(req_id, version):
    plan_path = f"./assistants/{version}/plan/{req_id}/PLAN.md"
    task_ids = algorithm_3_parse_task_ids(plan_path)
    
    print_progress(f"任务循环({len(task_ids)} 个)")
    for i, task_id in enumerate(task_ids):
        # 步骤 4.1:code-it
        print_progress(f"{i+1}/{len(task_ids)}:code-it {task_id}")
        result = skill_invoke("code-it", task_id)
        if not result.success:
            return handle_sub_skill_failure(f"4.{i+1}.it", result.stderr)
        
        # 步骤 4.2:code-unit(条件触发)
        if "测试需要=Y" in result.stdout:
            print_progress(f"{i+1}/{len(task_ids)}:code-unit {task_id}")
            result = skill_invoke("code-unit", task_id)
            if not result.success:
                return handle_sub_skill_failure(f"4.{i+1}.unit", result.stderr)
        else:
            print_progress(f"{i+1}/{len(task_ids)}:code-unit {task_id} ✓ (跳过,无需测试)")
    
    return success
```

- **输入**:`req_id`(string)+ `version`(string)
- **输出**:`success` / `handle_sub_skill_failure()`
- **复杂度**:O(N_task × code-it 平均耗时)
- **依赖**:算法 3 + `skill_invoke`
- **关键决策**:`code-unit` 触发条件 = `code-it` 输出含"测试需要=Y"(`code-it` 内部约定,本设计不修改)
- **边界条件**:`code-it` 失败 / `code-unit` 失败 / `PLAN.md` 缺失
- **对应任务**:T-001(SKILL.md §7 步骤 4)

### 算法 5:评审循环(FR-5,无轮数上限 Q-1 锁定 A)

```
function algorithm_5_review_loop(req_id, version):
    review_round = 0
    while True:
        review_round += 1
        
        # 步骤 5:code-review
        print_progress(f"code-review {req_id}(第 {review_round} 轮)")
        result = skill_invoke("code-review", req_id)
        if not result.success:
            return handle_sub_skill_failure(5, result.stderr)
        
        # 解析"必须改"列表
        review_path = f"./assistants/{version}/review/{req_id}/REVIEW-REPORT.md"
        must_fix = algorithm_6_parse_must_fix(review_path)
        
        if not must_fix:
            print_progress(f"第 {review_round} 轮:无'必须改' → 结束")
            return success  # 退出循环
        
        # 步骤 6:派生任务循环
        print_progress(f"第 {review_round} 轮:'必须改'任务 {len(must_fix)} 个")
        for i, derived_id in enumerate(must_fix):
            print_progress(f"{i+1}/{len(must_fix)}:code-it {derived_id}")
            result = skill_invoke("code-it", derived_id)
            if not result.success:
                return handle_sub_skill_failure(f"6.{i+1}.it", result.stderr)
            
            # 条件触发 code-unit
            if "测试需要=Y" in result.stdout:
                result = skill_invoke("code-unit", derived_id)
                if not result.success:
                    return handle_sub_skill_failure(f"6.{i+1}.unit", result.stderr)
        
        # 回到步骤 5(无轮数上限)
```

- **输入**:`req_id`(string)+ `version`(string)
- **输出**:`success` / `handle_sub_skill_failure()`
- **复杂度**:O(N_round × N_derived × code-it 平均耗时)
- **依赖**:算法 6 + `skill_invoke`
- **关键决策**:**无 `break`**(Q-1 锁定 A);接受"修改引入新问题"风险
- **边界条件**:`code-review` 失败 / `REVIEW-REPORT.md` 缺失 / 派生任务失败
- **对应任务**:T-001(SKILL.md §7 步骤 5/6)

### 算法 6:解析"必须改"列表(FR-5.AC-5.6)

```
function algorithm_6_parse_must_fix(review_path):
    content = read_file(review_path)
    
    # 锚点 1:定位"评审发现汇总"区段
    section = extract_section(content, "^## 评审发现汇总$")
    if section is None:
        raise "未找到 '评审发现汇总' 区段"
    
    # 锚点 2:解析表格行
    rows = parse_table_rows(section)
    
    # 筛选:级别=必须改 且 状态≠已处理
    must_fix = []
    for row in rows:
        # 表格列假设:级别 / 状态 / 任务编码 / ...
        level = row.get("级别", "")
        status = row.get("状态", "")
        task_id = row.get("任务编码", "")
        
        if level == "必须改" and status != "已处理" and task_id:
            must_fix.append(task_id)
    
    return must_fix
```

- **输入**:`review_path`(string)
- **输出**:`must_fix`(string[])
- **复杂度**:O(N_rows)
- **依赖**:`read_file` / `re.match` / `parse_table_rows`
- **关键决策**:沿用 `code-dashboard` 解析锚点 + `code-publish` PreflightChecker 锚点(NFR-5/6 强约束)
- **边界条件**:文件不存在 / 缺区段 / 无"必须改"行
- **对应任务**:T-001(SKILL.md §8.2)

### 算法 7:异常处理(FR-7)

```
function algorithm_7_report(req_id, version, start_time, status):
    # 1. 拼装报告
    end_time = now()
    summary = {
        "需求编码": req_id,
        "所属版本": version,
        "code-auto 起始时间": start_time,
        "code-auto 结束时间": end_time,
        "总状态": status,  # ✓ 完成 / ⏹ 用户中止 / ✗ 子技能异常
        "总子技能调用次数": count_skill_invocations()
    }
    
    # 2. 屏幕输出报告
    print_format_report(summary)
    
    # 3. 仅在 status="完成" 时写盘
    if status == "完成":
        target_path = f"./assistants/{version}/require/{req_id}/auto-report.md"
        write_result = write_file(target_path, format_md_report(summary))
        if not write_result.success:
            # E-10:警告不中断
            print_warning(f"⚠ auto-report.md 写入失败({write_result.error}),报告仅输出在屏幕")
    
    # 4. 退出码
    if status == "完成":
        return exit_code = 0
    elif status == "用户中止":
        return exit_code = 130
    else:  # "子技能异常"
        return exit_code = 1
```

- **输入**:`req_id` + `version` + `start_time` + `status`
- **输出**:`exit_code`
- **复杂度**:O(1)
- **依赖**:`now` / `print` / `write_file`
- **关键决策**:完成时写 / 中止时不写(NFR-7)+ 写入失败警告不中断(D-6)
- **边界条件**:`Write` 工具失败
- **对应任务**:T-001(SKILL.md §7 步骤 7)

---

## 6. 数据结构完整变更(概要,详见 `data-changes.md`)

### 6.1 新增实体

| 实体 | 字段数 | 主键 | 索引 | 迁移需求 | 对应任务 |
| --- | --- | --- | --- | --- | --- |
| `auto-report.md`(运行时) | ~15 字段 | 无 | 无 | N/A(新建) | T-001 |
| `code-auto/SKILL.md` | (新文件) | 无 | 无 | N/A(新建) | T-001 |

### 6.2 修改实体

| 实体 | 变更字段 | 索引 | 兼容策略 | 对应任务 |
| --- | --- | --- | --- | --- |
| `marketplace.json` | `plugins[].skills` 末尾追加 1 项 | 无 | 追加不修改 | T-002 |
| `README.md`(中文) | "主要能力"段表格追加 1 行 | 无 | 追加不修改 | T-003 |
| `README.en.md`(英文) | "主要能力"段表格追加 1 行 | 无 | 追加不修改 | T-003 |
| `V0.0.2/RESULT.md` | 4 区段追加 + 文档头 2 处 | 无 | 追加不修改 | T-004 |

### 6.3 数据迁移
- **N/A**:`code-auto` 是全新技能,无历史数据需迁移
- **回滚方案**:`git revert` 或手动删除 4 处文件(`data-changes.md §7.3`)

---

## 7. 接口细节(概要,详见 `interface-specs.md`)

### 7.1 接口总览

| 接口名 | 形式 | 状态 | 对应任务 | 依据规范 |
| --- | --- | --- | --- | --- |
| 1. `code-auto` 触发 | `Skill` 工具 | 新增 | T-001 | `skill-conventions §规则 1` |
| 2. 子技能调用 | `Skill` 工具 × 6 | 复用(零修改) | T-001 | `module-conventions §规则 1` |
| 3. 数据源读取 | `Read` 工具 × 3 | 复用 | T-001 | `encoding-conventions §规则 1-4` |
| 4. 磁盘写入 | `Write` 工具 | 新增 | T-001(运行时) | NFR-6/7 |
| 5. `marketplace.json` 修改 | `Edit` 工具 | 修改 1 处 | T-002 | `marketplace-protocol §规则 1` |
| 6. 中英 README 修改 | `Edit` 工具 × 2 | 修改 1 处 | T-003 | `doc-conventions §规则 1` |
| 7. 看板同步 | `Edit` 工具 × 5 | 修改 4 区段 | T-004 | `dashboard-conventions §规则 1` |

### 7.2 关键决策

- **退出码语义**:`0` = 完成 / `1` = 子技能异常 / `2` = 步骤 0a 失败 / `3` = 步骤 0 失败 / `4` = 缺参数 / `130` = SIGINT
- **覆盖语义**:`auto-report.md` 同名文件**覆盖**(NFR-6 强约束)
- **同次提交**:`marketplace.json` / `README.md` / `README.en.md` / `RESULT.md` **可**在不同 commit(各自独立任务),但**不可**改一半就停
- **写入时机**:`auto-report.md` **仅在完成时** Write;异常/中止/自身崩溃时**均不写**(NFR-7 强约束)

---

## 8. 异常处理(概要,详见 `risk-analysis.md`)

按 E-1 ~ E-13 异常路径组织(沿用需求 §9):
- **E-1** 无 `.current-version` → 提示 + 退出 3
- **E-2/3/4** `git pull` 失败(冲突/网络/凭据)→ 退出 2
- **E-5** 子技能退出码 ≠ 0 → 中断 + 报告 + 退出 1
- **E-6** SIGINT → 中止 + 报告 + 退出 130
- **E-7** 评审循环无收敛 → 持续循环(Q-1)
- **E-8** 子技能耗时过长 → 接受 + Ctrl+C
- **E-9** 自身崩溃 → 部分报告 + 不写 `auto-report.md`
- **E-10** `auto-report.md` 写入失败 → 警告不中断
- **E-11/12** `PLAN.md` / `REVIEW-REPORT.md` 缺失 → 中断 + 报告
- **E-13** 缺参数 → 提示 + 退出 4

---

## 9. 安全要求

- **鉴权**:N/A(`code-auto` 由 Claude Code 模型层触发)
- **授权**:N/A(无细粒度授权检查)
- **输入校验**:`<需求内容>` / `<版本号>` / `<需求编码>` / `<任务编码>`(沿用 `encoding-conventions §规则 1-4`)
- **敏感数据处理**:**不读**任何 `secrets` / `.env` / `id_rsa` / `token`;**不写**敏感数据到 `auto-report.md`;**不打印**敏感数据到屏幕
- **防注入**:N/A(本仓库无 SQL/NoSQL/反序列化)
- **审计**:进度日志 + 完成报告 + 看板变更记录
- **依据规范**:`marketplace-protocol §规则 1` + `encoding-conventions §规则 1-4`

---

## 10. 状态机 / 流程(对应概要设计 §5.3)

### 10.1 主状态机

```
[*] --> 启动解析 : algorithm_1
启动解析 --> 主循环 : algorithm_2
主循环 --> 任务循环 : algorithm_4
任务循环 --> 评审循环 : algorithm_5
评审循环 --> 任务循环 : 派生任务完成
评审循环 --> 报告 : 必须改列表空
任务循环 --> 报告 : 任务全部完成
主循环 --> 报告 : 异常
报告 --> [*] : exit

note right of 报告
  status="完成" → Write auto-report.md + exit 0
  status="用户中止" → 不写 + exit 130
  status="子技能异常" → 不写 + exit 1
end note
```

### 10.2 内部状态

`code-auto` 是**无状态执行器**:
- 不维护内存计数器(Q-A2 锁定 C,仅屏幕打印"第 N 轮")
- 不缓存子技能产物
- 不持久化任何状态(用户重跑 = 从头开始,NFR-8 + Q-11 锁定)

---

## 11. 性能与资源

- **关键路径耗时**:`code-auto` 整体执行由子技能耗时决定;典型场景 30-60 分钟,大需求数小时
- **并发上限**:N/A(NFR-2 强约束串行)
- **资源限制**:Claude Code 上下文 token 上限(由 Claude Code 模型层管理)
- **缓存策略**:N/A(无状态执行器)
- **批量/异步**:N/A(严格串行)
- **降级策略**:N/A(异常即中断 + Ctrl+C 中止)

---

## 12. 测试要点(概要,详见 `risk-analysis.md §5`)

- **单元测试**:**N/A**(本仓库无构建/测试文件,REQ-00009 守卫判定"不可测")
- **集成测试**:4 场景(S-1 顺利 / S-2 评审循环 / S-3 子技能失败 / S-4 用户中止)
- **端到端测试**:沿用集成测试场景
- **性能/压力测试**:N/A
- **安全测试**:N/A(本设计无安全攻击面)
- **回归测试**:6 子技能零修改 = 既有测试通过即可
- **静态自检**:T-005 实施 8 项不变量自检(详 `design-notes.md §详细化不变量`)
- **测试状态**:5 任务全部 `不适用`(Q-P3 锁定 A,本仓库无传统单测载体)

---

## 13. 关联编码计划

- `PLAN.md` 中本详细设计对应 **5 个任务**(T-001 ~ T-005)
- 关键任务对应:
  - **T-001** ↔ 本设计 §4.1(模块 M-1 详细)+ §5(算法 1-7)
  - **T-002** ↔ 本设计 §6.2(marketplace.json 修改)+ §7.1(接口 5)
  - **T-003** ↔ 本设计 §6.2(中英 README 修改)+ §7.1(接口 6)
  - **T-004** ↔ 本设计 §6.2(看板同步)+ §7.1(接口 7)
  - **T-005** ↔ 本设计 §11(自检)+ §12(测试要点)

---

## 14. 待澄清 / 未决项(本轮未处理 / 留作默认)

| 编号 | 问题 | 影响范围 | 阻塞方 | 期望回复时间 | 状态 |
| --- | --- | --- | --- | --- | --- |
| Q-13(转出) | 用 `code-rule` 沉淀 `auto-conventions.md` | 留作 follow-up | `code-review` 决定 | N/A | 由 code-review 派生 |
| Q-A2(继承) | 评审轮次不落盘,仅屏幕 | 本设计 §10.2 | (本轮已锁定 C) | 已锁定 | N/A |

---

## 15. 变更记录

| 时间 | 版本 | 变更摘要 | 变更人 |
| --- | --- | --- | --- |
| 2026-06-05 10:30 | v1 | 初始创建:1 个模块(M-1 SKILL.md)+ 1 个运行时产物(M-2 auto-report.md)+ 7 个算法(可编码)+ 4 个接口契约;100% 规范合规,0 偏离 0 冲突;5 个任务全部纯文档型,测试状态全部 `不适用`(Q-P3 锁定 A);T-001 单任务产 1 个文件(Q-P1 锁定 A);T-001 步骤 0a 调 `git pull`(Q-P2 锁定 A) | wangmiao |
