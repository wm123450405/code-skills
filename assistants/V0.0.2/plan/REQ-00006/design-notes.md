# 设计笔记 — REQ-00006(详细设计阶段)

更新时间:2026-06-04 17:01
版本:V0.0.2

## 1. 详细设计区别于概要设计的核心补充

概要设计已锁定 8 项决策 D-1 ~ D-8(架构层面);详细设计需要在**实现层面**补充:

### DD-1:看板 3 区段的具体解析策略(对应算法 1)

- **概要设计层**:决策 D-2 "按行硬解析"
- **详细设计层**:需要明确 Bash 解析的具体命令链 + 退化路径
- **选定方案**:
  - 区段提取:`sed -n '/^## 需求清单/,/^## /p'`(取到下一个 `## ` 为止);若是末尾区段(如缺陷清单 → 评审发现汇总),`sed` 自然终止
  - 数据行过滤:`grep -E '^\| ' | grep -v '^\|[[:space:]]*---'`(去掉分隔行)+ 显式跳过"统计"行
  - 列值提取:`awk -F '|' '{print $N}'`(N 为该列序号)
  - **退化**:若区段不存在(看板被破坏)→ PreflightChecker 返回"全未解决"(E-2)
- **理由**:Claude 直接调 `Bash` 工具执行,无需额外编程
- **依据规范**:`dashboard-conventions §规则 1` 0 触发

### DD-2:区段中"未完成项"的字符串识别精度

- **概要设计层**:状态判定逻辑(需求/任务/缺陷的"解决"集合)
- **详细设计层**:必须明确**字段名识别**而非"列号位置",因为表格列可能未来扩展
- **选定方案**:
  - 第一步:Read 整个 RESULT.md
  - 第二步:对每个区段:
    - 找到首行(以 `| ` 起始 + 含 `| --- |...|` 分隔的上一行)→ 解析"列名 → 列序号"映射
    - 找到所有数据行(以 `| ` 起始 + 不是分隔行 + 不是统计行)
    - 对每行:按列名取"状态/开发状态/测试状态"字段
  - 第三步:按 needs §8.3 状态判定表生成未完成项
- **理由**:
  - 列号位置容易因 `dashboard-conventions §规则 1` 触发的"新增列"而失效
  - 按列名查找,只要列名不变 → 增加新列不破坏解析
- **依据规范**:NFR-8 与 dashboard 数据源强一致

### DD-3:基线判定的具体目录排序规则

- **概要设计层**:决策 D-3 字典序最小
- **详细设计层**:需要明确:
  - 字典序工具:`sort`(Bash 默认 ASCII 字典序)
  - 排除规则:排除 `rules`、隐藏文件、非目录
- **选定方案**:
  ```bash
  ls -1d ./assistants/*/ | sed 's|.*/\(.*\)/|\1|' | grep -vE '^rules$' | sort | head -1
  ```
  返回字典序最小的版本号(目录名)
- **理由**:遵循需求 NFR-7 规则 1;对当前 V0.0.X 系列字典序 = SemVer 顺序
- **依据规范**:无

### DD-4:placeholder 替换的具体方式

- **概要设计层**:`<本版本号>` / `<源版本>` 自动填充,其他保留
- **详细设计层**:
  - 自动填充范围:**仅** `<本版本号>` 与 `<源版本>`,其余 placeholder 保留
  - 替换工具:`sed -i "s/<本版本号>/${VERSION}/g" path/to/file` 或 Claude 在 Write 时直接渲染
  - **优选**:Claude 在 Write 时直接渲染(无 Bash 子进程,纯模板字符串替换)
- **理由**:简单 + 避免 sed 转义陷阱(版本号含 `.` / `-` 等字符)
- **依据规范**:无

### DD-5:覆盖前的报告"预检"

- **概要设计层**:D-7 始终覆盖 + 在报告中标"将覆盖 N 个文件"
- **详细设计层**:
  - 写入前:`ls -la ./assistants/<版本号>/publish/ 2>/dev/null | grep -E 'DEPLOY|UPDATE|Q&A'.md'` 或 `find publish/ -name '*.md'`
  - 记入内存 → 在 Step 3 报告中输出"已覆盖 N 个文件:[file1, file2, ...]"
- **理由**:用户透明
- **依据规范**:无

### DD-6:Q&A.md 聚合的 Markdown 章节生成规则

- **概要设计层**:全部聚合 + 每节"来源"标注
- **详细设计层**:
  - Glob `./assistants/qanda/*.md`,**排除 README.md(大小写不敏感)**
  - 排序:按文件名字典序(确保幂等)
  - 章节生成:
    ```markdown
    ## <文件名去后缀(支持中文)>
    > 来源:qanda/<文件名>
    
    <文件全文>
    ```
  - 若 0 个非 README 文件 → 渲染占位章节
- **理由**:AC-5.4
- **依据规范**:无

### DD-7:错误处理的具体退出行为

- **概要设计层**:§6.3 E-1 ~ E-10
- **详细设计层**:
  - **E-1 不通过**:不退出进程(技能正常结束);只是不进入 Step 2
  - **E-2 看板缺区段**:不通过分支 + 在报告中标"看板不完整"
  - **E-5 无 .current-version + 无参数**:技能立即结束 + 文本提示 `请先调 /code-version`(模仿其他 7 版本感知技能)
  - **E-7 publish/ 写入失败**:报错 + 立即退出(留 partial 文件由用户清理,但不留模板未替换的 placeholder)
- **理由**:`code-it` / `code-auto` 通过技能"是否产生预期文件"判断成功,而不是退出码;但 SKILL.md 中**明示**"失败时不留半成品"
- **依据规范**:无

### DD-8:幂等性的精确语义

- **概要设计层**:NFR-6 始终覆盖
- **详细设计层**:
  - "重跑后状态等同初次跑" = 输出文件**字节级一致**(只要输入相同)
  - 输入:`<版本号>/RESULT.md`(看板状态) + `<版本号>` + `./assistants/qanda/*.md`
  - 副产物:运行时间戳(在 Q&A.md / 报告中) → 这会破坏字节级幂等
  - **决策**:**时间戳只出现在报告中,不写入 publish/ 任何文件**;publish/ 下 3 份手册"内容"幂等
- **理由**:用户重跑后 `git diff publish/` 应该是 0 改动(若上游无变化)
- **依据规范**:NFR-6

## 2. 关键算法的伪代码(供 RESULT.md §5 引用)

### 算法 1:PreflightChecker(伪代码)

```
function preflight_check(version_number):
    board_path = "./assistants/" + version_number + "/RESULT.md"
    board_content = Read(board_path)
    if board_content is null:
        return { passed: false, reason: "看板不存在", undone: [] }
    
    sections = {
        "需求清单": extract_section(board_content, "需求清单"),
        "任务清单": extract_section(board_content, "任务清单"),
        "缺陷清单": extract_section(board_content, "缺陷清单"),
    }
    
    undone = []
    stats = { 需求: {总: 0, 未完成: 0}, 任务: ..., 缺陷: ... }
    
    for section_name, section_text in sections:
        if section_text is null:
            stats[section_name].未完成 = stats[section_name].总  // 退化
            continue
        
        column_map = parse_header_row(section_text)
        rows = parse_data_rows(section_text)  // 跳过分隔行 + 统计行
        stats[section_name].总 = len(rows)
        
        for row in rows:
            if not is_resolved(section_name, row, column_map):
                undone.push({
                    类型: section_name,
                    编码: row[column_map["需求编码" | "任务编号" | "缺陷编号"]],
                    标题: row[column_map["标题"]],
                    当前状态: extract_current_status(section_name, row, column_map),
                    期望状态: expected_status(section_name),
                })
                stats[section_name].未完成 += 1
    
    return { passed: len(undone) == 0, undone, stats }

function is_resolved(section_name, row, column_map):
    if section_name == "需求清单":
        return row[column_map["状态"]].startswith("已完成")  // 容忍"已完成(需求分析)" 等后缀
    if section_name == "任务清单":
        dev = row[column_map["开发状态"]]
        test = row[column_map["测试状态"]]
        return dev == "已完成" and test in {"已运行-通过", "不适用"}
    if section_name == "缺陷清单":
        return row[column_map["状态"]] == "已修复"
```

### 算法 2:BaselineDetector

```
function detect_baseline(target_version):
    all_dirs = Glob("./assistants/*/")
    versions = [
        basename(dir) for dir in all_dirs
        if basename(dir) != "rules"
        and not basename(dir).startswith(".")
    ]
    sorted_versions = sort_ascii(versions)
    min_version = sorted_versions[0]
    
    is_baseline = (target_version == min_version)
    previous_version = null
    if not is_baseline:
        idx = sorted_versions.index(target_version)
        previous_version = sorted_versions[idx - 1] if idx > 0 else null
    
    return { is_baseline, previous_version }
```

### 算法 3:ManualBuilder

```
function build_manuals(version_number, baseline_result):
    publish_dir = "./assistants/" + version_number + "/publish/"
    Bash("mkdir -p " + publish_dir)
    
    existing = Bash("ls -1 " + publish_dir + " 2>/dev/null | grep -E '(DEPLOY|UPDATE|Q&A)\\.md$'")
    overwritten = []
    
    // DEPLOY.md(始终)
    deploy_template = Read("plugins/code-skills/skills/code-publish/templates/DEPLOY.md")
    deploy_content = deploy_template.replace("<本版本号>", version_number)
    if "DEPLOY.md" in existing:
        overwritten.push("DEPLOY.md")
    Write(publish_dir + "DEPLOY.md", deploy_content)
    
    // UPDATE.md(非基线)
    if not baseline_result.is_baseline:
        update_template = Read("plugins/code-skills/skills/code-publish/templates/UPDATE.md")
        update_content = update_template
            .replace("<本版本号>", version_number)
            .replace("<源版本>", baseline_result.previous_version)
        if "UPDATE.md" in existing:
            overwritten.push("UPDATE.md")
        Write(publish_dir + "UPDATE.md", update_content)
    
    return { written: ..., overwritten }
```

### 算法 4:QandaScaffolder + QandaAggregator + ReportFormatter

(详见 SKILL.md 步骤 2.5 / 2.6 / 3 自然语言指令;伪代码省略,与上 3 算法相似结构)

## 3. 任务拆分原则的具体应用

### 3.1 拆分维度

- **按"文件"切分**:每个独立文件 = 1 任务(SKILL.md / 5 模板 / qanda 骨架)
- **按"功能"切分**:可选 README 双语同步 = 1 任务(`doc-conventions §规则 1` 强制同次提交)
- **按"自检"切分**:不变量自检 + 看板同步 = 1 任务(收尾,确保 0 偏离)

### 3.2 任务依赖

- 模板任务(T-002 ~ T-006)**独立可并行**(只写文件,不互相依赖)
- SKILL.md 任务(T-001)**依赖** 所有模板存在(因为 SKILL.md 中会引用模板路径)
- 收尾任务(T-007)**依赖** 全部前置任务
- 双 README 任务(T-008)**独立**,可与 T-001 ~ T-007 并行

### 3.3 任务粒度

- 每条任务 0.5 ~ 1 天可完成
- 8 条任务总估算:~3 天

### 3.4 任务编号
- 沿用 `encoding-conventions.md §规则 1 / §规则 3`:`TASK-REQ-00006-NNNNN`
- T-001 ~ T-008 实际编号:`TASK-REQ-00006-00001` ~ `TASK-REQ-00006-00008`
- **特别注意**:看板"任务清单"区段在 V0.0.1 中使用过 `REQ-00001-001` 形式(3 位),V0.0.2 起应改用 5 位嵌套式,但需求 v1 §E-9 显式说"看板'任务清单'含旧格式任务编号(REQ-NNNNN-NNNNN)视为字符串处理"
- **本计划决策**:**沿用新格式 `TASK-REQ-00006-NNNNN`**(完整 5 位嵌套式),与 V0.0.2 看板的统一格式对齐;PLAN.md 内任务编号字段使用此格式
