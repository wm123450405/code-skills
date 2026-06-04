# 模块详细化 — REQ-00006

更新时间:2026-06-04 17:01
版本:V0.0.2

## 概要设计 §7.2 各模块的详细化对应

### 模块 1:`code-publish` 技能(SKILL.md)— 对应概要设计 §7.2.1

- **关键类/函数**:无(纯文档型,Claude 在自然语言指令下执行)
- **关键调用顺序**(SKILL.md 中"## 工作流程"小节的展开):
  1. **步骤 0**:`Read .current-version`(无参时)→ 解析 `<版本号>`
  2. **步骤 1**:`Read <版本号>/RESULT.md` → PreflightChecker 算法 → 若不通过 → 跳到步骤 3 报告;否则继续
  3. **步骤 2.0**:`Glob ./assistants/*/` → BaselineDetector 算法 → 得 `{is_baseline, previous_version}`
  4. **步骤 2**:`Bash mkdir -p publish/` → ManualBuilder 算法 → Write DEPLOY.md + [UPDATE.md] + Q&A.md
  5. **步骤 2.5**:`Bash ls qanda/` → QandaScaffolder 算法 → 视情况 `mkdir + Write README.md`
  6. **步骤 2.6**:`Glob qanda/*.md` → QandaAggregator 算法 → 渲染 Q&A.md 内容(交由步骤 2 写入)
  7. **步骤 3**:ReportFormatter 算法 → 多行文本到 stdout
- **内部状态**:无(每次调用都是新一次)
- **并发模型**:单进程,顺序执行(Claude 在 SKILL.md 自然语言中按步骤推进)
- **资源管理**:无连接/锁/缓存;只用文件 IO
- **错误处理范式**:
  - "技能" 不抛异常,所有错误都在自然语言中"报告 + 不留半成品 + 退出"
  - 文件 IO 失败 → 立即报错文本输出 → 技能正常结束(no traceback)
- **日志埋点**:无(用户在终端看到的就是技能的"日志")
- **依据规范**:`skill-conventions.md §规则 1`(frontmatter 必含)+ `module-conventions.md §规则 1`(资源在 templates/)

### 模块 2:PreflightChecker — 对应概要设计 §7.2.2

- **关键类/函数**:
  - `preflight_check(version_number)` → `PreflightResult`(详 design RESULT.md §9)
  - `extract_section(board_content, section_name)` → 区段文本
  - `parse_header_row(section_text)` → `{列名: 列序号}`
  - `parse_data_rows(section_text)` → `list[行字段列表]`
  - `is_resolved(section_name, row, column_map)` → bool
- **关键调用顺序**(伪代码见 design-notes.md §2 算法 1):
  1. Read 看板 → 字符串
  2. 对每个 section_name:extract → parse_header → parse_data
  3. 对每行:is_resolved → 累积 undone
  4. 返回汇总
- **内部状态**:无
- **并发模型**:单线程(顺序处理 3 个区段)
- **资源管理**:1 次 Read 大字符串(看板 < 1 MB,内存安全)
- **错误处理范式**:
  - 看板不存在 → 返回 `{passed: false, reason: "看板不存在", undone: []}`(不抛)
  - 区段不存在 → 该区段视为"全未解决"(退化 E-2)
  - 列名缺失 → 该行视为"未解决"(保守判定)
- **日志埋点**:无(汇总数据在 ReportFormatter 中显示)
- **依据规范**:NFR-2 纯只读 + NFR-8 与 dashboard 一致

### 模块 3:BaselineDetector — 对应概要设计 §7.2.3

- **关键类/函数**:
  - `detect_baseline(target_version)` → `BaselineResult`
- **关键调用顺序**(伪代码见 design-notes.md §2 算法 2):
  1. Glob ./assistants/*/
  2. 过滤 + 排序
  3. 比较 target == min
  4. 若非基线,前一版本 = sorted[idx-1]
- **内部状态**:无
- **并发模型**:单线程
- **资源管理**:无
- **错误处理范式**:
  - Glob 0 结果 → 不可能(至少有 <target_version> 自身)
  - target_version 不在 sorted 中 → 报错 + 退出(看板路径与版本号不一致,严重异常)
- **日志埋点**:无
- **依据规范**:NFR-7 规则 1

### 模块 4:ManualBuilder — 对应概要设计 §7.2.4

- **关键类/函数**:
  - `build_manuals(version_number, baseline_result)` → `ManualBuildResult`
  - `write_one_manual(template_path, target_path, replacements)` → bool
- **关键调用顺序**:
  1. mkdir publish/
  2. ls publish/ → existing 列表
  3. Read DEPLOY.md template → 替换 → Write target
  4. (非基线)Read UPDATE.md template → 替换 → Write target
  5. (Q&A.md 由 QandaAggregator 已渲染) Write target
- **内部状态**:无
- **并发模型**:顺序写入 3 文件
- **资源管理**:文件 IO(每个 < 10 KB,无压力)
- **错误处理范式**:
  - mkdir 失败 → 报错 + 退出(E-7)
  - Write 失败 → 报错 + 退出,不写下一个(避免半成品)
- **日志埋点**:无
- **依据规范**:FR-2 / FR-3 / FR-4 / NFR-6

### 模块 5:QandaScaffolder — 对应概要设计 §7.2.5

- **关键类/函数**:
  - `scaffold_qanda()` → `{qanda_status: '已存在' | '本次创建' | '创建失败'}`
- **关键调用顺序**:
  1. ls qanda/ → 检测
  2. 不存在 → mkdir + Write README.md(从 templates/qanda-README.md)
  3. 失败 → 不阻塞,标记状态
- **内部状态**:无
- **并发模型**:单线程
- **资源管理**:无
- **错误处理范式**:
  - mkdir 失败 → 标记 `creation_failed = true`,继续 Step 2.6(Q&A.md 仍生成占位)
  - Write README.md 失败 → 同上
- **日志埋点**:无
- **依据规范**:FR-6 + FR-7.AC-7.4

### 模块 6:QandaAggregator — 对应概要设计 §7.2.6

- **关键类/函数**:
  - `aggregate_qanda()` → 渲染后的 Q&A.md 内容字符串
- **关键调用顺序**:
  1. Glob qanda/*.md
  2. 过滤 README.md(大小写不敏感)
  3. 按文件名排序
  4. 若空 → 用占位模板原样返回
  5. 非空 → 占位模板 + 每文件渲染"## <名> + 来源 + 全文"
- **内部状态**:无
- **并发模型**:单线程(顺序读多个文件)
- **资源管理**:每个文件 < 100 KB(假设);累积内存 < 10 MB
- **错误处理范式**:
  - 单文件读取失败 → 跳过该文件 + 在 Q&A.md 中加 `> 警告:无法读取 qanda/<名>`
- **日志埋点**:无
- **依据规范**:FR-5 + AC-5.4

### 模块 7:ReportFormatter — 对应概要设计 §7.2.7

- **关键类/函数**:
  - `format_report(preflight_result, baseline_result, manual_result, qanda_result)` → 多行文本
  - `format_pass_report(...)` / `format_fail_report(...)` / `format_baseline_report(...)` / `format_qanda_empty_report(...)`
- **关键调用顺序**:
  1. 根据 4 个输入选择模板
  2. 渲染字符串
  3. 通过 SKILL.md 的"输出"段直接显示
- **内部状态**:无
- **并发模型**:单线程
- **资源管理**:无
- **错误处理范式**:无(此模块本身不应失败)
- **日志埋点**:无(本身就是日志输出)
- **依据规范**:FR-9 + NFR-9

## 模板模块

### 模板 1:`templates/DEPLOY.md`

- **内容结构**:见 needs §6.1 节选(8 章节)
- **关键字段**:`<本版本号>` 由 Claude 替换;其余 `<打包方式>` / `<output>` / `<server>` / 等保留
- **依据规范**:无

### 模板 2:`templates/UPDATE.md`

- **内容结构**:见 needs §6.2 节选(8 章节,§8 回滚为新增)
- **关键字段**:`<本版本号>` + `<源版本>` 自动替换
- **依据规范**:无

### 模板 3:`templates/Q&A.md`

- **内容结构**:见 needs §6.3 节选(占位章节 + 提示)
- **关键字段**:`<本版本号>` 自动替换
- **依据规范**:无

### 模板 4:`templates/qanda-README.md`

- **内容结构**:
  - "# `assistants/qanda/` — 项目级 Q&A 长期沉淀目录"
  - "## 用途"
  - "## 文件命名建议"
  - "## 引用规范"
  - "## 维护方式"
- **关键字段**:无(纯静态)
- **依据规范**:FR-6 AC-6.2

### 模板 5:`templates/assistants-layout.md`

- **内容结构**:沿用其他技能的同名模板,补充 `publish/` 与 `qanda/` 路径段
- **关键字段**:无
- **依据规范**:无
