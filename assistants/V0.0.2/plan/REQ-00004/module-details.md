# 模块详细化 — REQ-00004

更新时间:2026-06-04 16:10
版本:V0.0.2

> 本文档给出概要设计 §3 模块拆分的"可直接编码级"细化。

---

## 模块 M-1:`code-dashboard` 技能(对应概要设计 §3.1)

### 路径
```
plugins/code-skills/skills/code-dashboard/
└── SKILL.md           # 单文件,无子目录
```

### 关键类/函数(SKILL.md 中以伪代码 / "步骤 N" 段落呈现)
> 本技能是"指令型 Markdown 技能",无运行时类/函数;以下为"步骤 N"中描述的"逻辑实体",由 Claude Code 读取 `SKILL.md` 后在对话中按需实例化。

| 名称 | 类型 | 职责 | 对应设计章节 |
| --- | --- | --- | --- |
| `parseArgs(args)` | 步骤 1 函数 | 参数解析:无参 / `REQ-NNNNN` / 非法 | 算法 0 |
| `readCurrentVersion()` | 步骤 0 函数 | 读 `.current-version`,失败 → 引导退出 | 异常 E-1 / E-2 |
| `parseDashboard(text, mode)` | 步骤 3 函数 | 看板区段解析(单遍扫描 + 行号锚点) | 算法 1 |
| `parseRequirementMode(reqNum)` | 步骤 3 函数(需求模式) | 并行读 3 文件 + 解析任务清单 | 算法 2 |
| `parseTaskId(raw)` | 工具函数 | 任务编号解析(新格式优先 + 旧格式透传) | 算法 4 |
| `aggregate(state, mode)` | 步骤 4 函数 | 聚合计数 + 进度比 | 数据结构 D-3 |
| `renderBar(filled, total)` | 渲染工具 | 固定 12 字符 ASCII 比例条 | 算法 5 |
| `generateSuggestions(state, mode)` | 步骤 5 函数 | 5 类优先级建议,最多 5 条 | 算法 3 |
| `printOutput(segments)` | 步骤 6 函数 | 屏幕打印(不写文件) | NFR-7 |

### 内部状态
**无**(NFR-7 幂等:不维护内部状态,每次调用独立)

### 关键调用顺序(总览模式)
```
步骤 0: readCurrentVersion()
         └─ 失败 → printOutput(guide) + return
步骤 1: parseArgs(args)
         └─ 非法 → printOutput(usage) + return
步骤 2: readMainDashboard()
         └─ 失败 → printOutput(missing-board) + return
步骤 3: parseDashboard(text, "总览")
步骤 4: aggregate(state, "总览")
         + renderBar(...) [段 1 / 段 2]
步骤 5: generateSuggestions(state, "总览")
步骤 6: printOutput(segments) → 屏幕
         return
```

### 关键调用顺序(需求模式)
```
步骤 0: readCurrentVersion()
         └─ 失败 → 同上
步骤 1: parseArgs(args)
         └─ 非法 → 同上
步骤 2a: validateReqExists(reqNum)  [读 require/<REQ>/]
         └─ 不存在 → printOutput(list-reqs) + return
步骤 2b: 并行 read:
         ↘ readMainDashboard()  [看 缺陷清单 筛 关联任务]
         ↘ readRequirementDoc(reqNum)
         ↘ readPlanDoc(reqNum)
步骤 3: parseRequirementMode(...)
步骤 4: aggregate(state, "需求")
步骤 5: generateSuggestions(state, "需求")
步骤 6: printOutput(segments) → 屏幕
         return
```

### 并发模型
- **无并发原语**:所有 IO 由 Claude Code 工具(`Read` / `Glob` / `Grep`)承载
- **并行 Read**:需求模式下,3 个 `Read` 在同一消息块内并发触发(Claude Code 工具本身支持并发调用)

### 资源管理
- **无连接 / 无锁 / 无缓存**(NFR-7 幂等)
- **内存占用**:典型 < 1 MB(单次 1~2 个文件 Read,文本解析在内存)

### 错误处理范式
- **L1 启动错误**(致命,必须退出):
  - `.current-version` 缺失 → `✗ 未检测到激活的版本工作空间` + 引导
  - `.current-version` 指向不存在版本 → `✗ 版本 <X> 工作空间不存在` + 引导
- **L2 数据错误**(可降级,继续渲染):
  - 看板文件缺失 → `✗ 看板文件不存在` + 退出
  - 区段缺失(## 需求清单 等)→ 显示 `(无)`
  - 表格列错位 → 退化到原始 markdown 块
  - 字段值缺失 → 显示 `?`
- **L3 异常兜底**:
  - 任何未预期错误 → `✗ 内部错误: <msg>` + 退出

### 日志埋点
- **无结构化日志**(NFR-7 幂等,不写文件)
- **屏幕输出即"日志"**:错误用 `✗` 前缀,建议用 `>` 前缀,数字用 `█` / `░` / `▓`

### 依据规范
- `skill-conventions.md §规则 1`:frontmatter 必含 name + description
- `module-conventions.md §规则 1`:本模块**不**新增子目录(无独立资源,授权偏离 A-1)
- `marketplace-protocol.md §规则 1`:不动 marketplace.json / plugin.json(走 Claude Code 技能自动发现协议)
- `encoding-conventions.md §规则 3`:任务编号解析用嵌套式正则

---

## 模块 M-2:`code-review` 行为契约(复用,对应概要设计 §3.2)

### 路径
`plugins/code-skills/skills/code-review/SKILL.md`(只读)

### 复用点
- **只读契约**:工具集 `Read` / `Glob` / `Grep`,不写任何文件
- **状态机范式**:"读区段 → 解析 → 聚合 → 渲染 → 输出"5 步
- **NFR-7 幂等**:多次执行结果完全相同

### 详细化(差异点)
| 维度 | `code-review` | `code-dashboard` |
| --- | --- | --- |
| 工具集 | `Read` / `Glob` / `Grep` | **同**(完全一致) |
| 数据源 | `PLAN.md` + `code/<TASK>/RESULT.md` | `RESULT.md` + 需求模式 2 子文件 |
| 输出形态 | `REVIEW-REPORT.md` + 派生改修 | **屏幕输出**(NFR-7,无文件) |
| 错误处理 | 写入 `findings-no-task.md` | **屏幕显示** `✗` + 退出 |
| 状态 | 写 `任务清单` / `评审发现汇总` / `派生任务记录` | **不写**任何文件 |

### 依据规范
- `skill-conventions.md §规则 1`:本模块**不修改**其 frontmatter(NFR-6 严守)

---

## 后续任务预想(供 `code-plan` 拆分,本模块对应 T-001)

`code-plan` 阶段将本模块拆分为以下任务:
- **T-001** `[新增] 写 plugins/code-skills/skills/code-dashboard/SKILL.md`(本技能主体,**必须**)
  - 涉及文件:`plugins/code-skills/skills/code-dashboard/SKILL.md`(新增)
  - 关键变更:YAML frontmatter + 12 节正文(目标 / 适用 / 不适用 / 目录 / 输入 / 输出 / 工具 / 步骤 / 边界 / 衔接 / 不要做)
  - 验证手段:静态检查(`Read` frontmatter + 节标题顺序);手动调用 2 种模式 × 4 种状态场景

- **T-002**(可选) `[修改] plugins/code-skills/CLAUDE.md 追加"指引 N: code-dashboard 行为约定"段`
  - 涉及文件:`plugins/code-skills/CLAUDE.md`(修改 1 段)
  - 关键变更:在"AI 工作约定"小节末尾追加 1 段(展示策略 + 建议策略 + 解析锚点)
  - 验证手段:`Read` CLAUDE.md 确认段存在;`Grep` 关键字命中
  - **触发条件**:用户授权才落地;本设计**建议不**触发(留作 `code-rule` 沉淀)

- **T-003**(可选) `[修改] plugins/code-skills/README.md + README.en.md 技能清单各 +1 行`
  - 涉及文件:`plugins/code-skills/README.md` + `plugins/code-skills/README.en.md`(各修改 1 行)
  - 关键变更:技能清单追加 `code-dashboard` 一行(中英对仗)
  - 验证手段:`Read` 两文件确认中英同次提交 + 结构对仗(`doc-conventions §规则 1`)
  - **触发条件**:用户授权才落地;必须中英同次提交
