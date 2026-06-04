# 接口详细规格 — REQ-00004

更新时间:2026-06-04 16:10
版本:V0.0.2

---

## 接口 I-1:CLI 入口(对应 FR-1 / FR-2 / FR-3 / FR-6 / FR-7)

### 形式
Claude Code 技能协议(`/code-<name> <args>`)

### 路径/签名
```
/code-dashboard                           # 总览模式(无参数)
/code-dashboard REQ-NNNNN                # 需求模式(1 个参数)
```

### 入参
| 字段 | 类型 | 必填 | 约束 |
| --- | --- | --- | --- |
| `args[0]` | string | 否 | 0 个参数 → 总览模式;1 个参数 `^REQ-\d{5}$` → 需求模式;1 个参数不匹配 → 错误模式 |
| `args[1+]` | — | — | **不接受**(多余参数 → 错误模式) |

### 出参
**屏幕输出**(无文件返回):
```
=== V0.0.2 开发看板 ===

需求进度
────────
...
(总览模式 4 段 / 需求模式 5 段)
```

### 错误码
**无数字错误码**(本技能无 API 端点,仅屏幕输出)。
错误用 `✗` 前缀标识:
| 错误 | 屏幕文本 | 触发条件 | 对应 AC |
| --- | --- | --- | --- |
| E-1 | `✗ 未检测到激活的版本工作空间` + 引导 | `.current-version` 不存在 | FR-5.AC-5.1/5.2 |
| E-2 | `✗ 版本 <X> 工作空间不存在` + 引导 | 指向不存在版本 | NFR-2 |
| E-3 | `✗ 在 <V> 中未找到需求 <REQ>` + 列表 | 需求模式 + 编号不存在 | FR-6.AC-6.1/6.2 |
| E-4 | `✗ 参数格式错误: <arg>` + 用法示例 | 参数不匹配 `^REQ-\d{5}$` | FR-6.AC-6.3 |
| E-5 | `✗ 看板文件不存在,请先调 code-version` | 主 `RESULT.md` 缺失 | NFR-2 |
| E-6 | `✗ 内部错误: <msg>` | 任何未预期异常 | NFR-2 + FR-7 |

### 示例

**正常 1:总览模式(空版本)**
```
$ /code-dashboard
✗ 未检测到激活的版本工作空间
  请先执行: /code-version <版本号>
  例如: /code-version V0.0.2
```

**正常 2:总览模式(V0.0.2 当前)**
```
$ /code-dashboard
=== V0.0.2 开发看板 ===

需求进度
────────
总计: 10
已完成: ██░░░░░░░░░░ 3
...
下一步建议
──────────
> 建议: 执行 /code-design REQ-00004
> 依据: 需求 REQ-00004 状态=已完成(需求分析)但概要设计=未开始
> 优先级: 高
...
```

**正常 3:需求模式**
```
$ /code-dashboard REQ-00001
=== REQ-00001 进度概览 ===

需求: REQ-00001 Marketplace 根名称添加 -marketplace 后缀
状态: 已完成
概要设计: [已完成] 详细设计: [已完成]
...
```

**异常 1:参数格式错**
```
$ /code-dashboard xxx
✗ 参数格式错误: xxx
  用法:
    /code-dashboard                  # 版本总览
    /code-dashboard REQ-NNNNN        # 需求粒度(5 位数字)
```

**异常 2:需求编号不存在**
```
$ /code-dashboard REQ-99999
✗ 在 V0.0.2 中未找到需求 REQ-99999

V0.0.2 现有需求:
  - REQ-00004
  - REQ-00005
  ...

请检查编号,或省略编号查看版本总览。
```

### 版本策略
- **本技能版本**:`v1`(与 V0.0.2 同周期发布)
- **接口兼容性**:`/code-dashboard` 是新增入口;不破坏任何既有 `code-*` 技能
- **breaking change 政策**:本技能无 v2 协议;若未来扩展(例如 `/code-dashboard --json`),走"增量"路径(在原命令加 flag,旧调用不破坏)

### 兼容策略
- **未来扩展空间**(本设计**不**实现,留作 v2):
  - `/code-dashboard --json`(机器可读输出)
  - `/code-dashboard --filter P0`(只看 P0 缺陷)
  - `/code-dashboard --since 2026-06-01`(看时间范围)

### 依据规范
- `skill-conventions.md §规则 1`:本接口的"元信息声明"在 `SKILL.md` frontmatter 的 `description` 字段
- `encoding-conventions.md §规则 1`:参数格式 `REQ-NNNNN` 严格按权威源
- `doc-conventions.md §规则 1`:本技能**不**新增 README 章节(若改 README,必须中英同次提交)

---

## 接口 I-2:文件契约(只读,对应 FR-2 / FR-3 / NFR-2 / NFR-3)

### 形式
Claude Code 工具 `Read`(单文件读取,直接返回文本)

### 路径/签名
| 调用 | 路径 | 何时调用 |
| --- | --- | --- |
| 步骤 0 | `./assistants/.current-version` | 总是 |
| 步骤 2a | `./assistants/<版本号>/require/<需求编号>/RESULT.md` | 需求模式 |
| 步骤 2b(总览) | `./assistants/<版本号>/RESULT.md` | 总览模式 |
| 步骤 2b(需求) | `./assistants/<版本号>/require/<需求编号>/RESULT.md` | 需求模式 |
| 步骤 2b(需求) | `./assistants/<版本号>/plan/<需求编号>/PLAN.md` | 需求模式 |
| 解析时参考 | `./assistants/rules/encoding-conventions.md` | 工具集内置知识(本技能不实际 Read) |

### 入参
无(Claude Code 工具的 `file_path` 字段,本技能内部使用)

### 出参
```
{
  "text": string,            // 文件全文(单次 Read 返回)
  "truncated": boolean       // 实际未截断(RESULT.md < 1MB,无需 offset/limit)
}
```

### 错误码
| 工具错误 | 处理 |
| --- | --- |
| `file_not_found` | L2 退化(显示 `✗ 看板文件不存在` + 退出) |
| `permission_denied` | L3 兜底(显示 `✗ 内部错误: 权限不足` + 退出) |
| 其他 | L3 兜底 |

### 示例
```
Read("./assistants/.current-version")
→ "V0.0.2\n"

Read("./assistants/V0.0.2/RESULT.md")
→ "# 版本开发进度看板 — V0.0.2\n...\n"(典型 ~300 行)
```

### 版本策略
- **文件格式稳定**:看板 7 区段结构由 `code-version/templates/version-RESULT.md` 锁定
- **本技能解析器**:
  - 按 `^## .*$` 定位区段(不假设区段顺序)
  - 按 `^\| .* \|$` 匹配表格行 + `|` 切分列(不假设列数,只按列名定位)
  - 缺失区段 / 列错位 / 字段缺失 → 退化显示

### 兼容策略
- **看板字段约定扩展触发**:`dashboard-conventions §规则 1` 要求 3 文件同步
- **本技能应对**:解析器按"列名"定位,不假设"列数";即使未来新增列,本技能仍可工作(忽略未识别列)
- **breaking 风险**:若未来看板区段标题改名(`## 需求清单` → `## 需求总览`),本技能需 `code-design` 增量更新

### 依据规范
- `dashboard-conventions.md §规则 1`:本技能**不**扩展看板字段
- `encoding-conventions.md §规则 3`:任务编号解析严格按嵌套式

---

## 接口 I-3:数据契约(内部数据结构,对应 FR-4 / NFR-3)

### 形式
**内存数据结构**(JS 对象字面,无外部 schema)

### 路径/签名
无外部路径;本节定义"步骤 3 解析结果 → 步骤 4 渲染 / 步骤 5 建议生成"之间的数据流

### 入参
**`ParseResult`**(步骤 3 输出):
```ts
{
  mode: "总览" | "需求" | "错误",
  version: string,                 // "V0.0.2"
  reqNum: string | null,           // 需求模式时 = "REQ-00001",否则 null
  requirements: RequirementRow[],  // 总览模式
  tasks: TaskRow[],                // 总览模式
  bugs: BugRow[],                  // 总览模式 + 需求模式(关联任务筛)
  targetReq: RequirementDetail | null,  // 需求模式
  error: ErrorInfo | null          // 错误模式
}
```

### 出参
**`RenderSegment[]`**(步骤 4 输出):
```ts
[
  { title: "需求进度", lines: string[] },
  { title: "任务进度", lines: string[] },
  { title: "缺陷(高优先级)", lines: string[] },
  { title: "下一步建议", lines: string[] }
]
```

### 错误码
无(内部数据流,不暴露)

### 示例
```js
// 总览模式(V0.0.2 当前)
{
  mode: "总览",
  version: "V0.0.2",
  requirements: [
    { id: "REQ-00004", title: "添加 /code-dashboard...", status: "已完成(需求分析)", design: "已完成", plan: "—" },
    ...
  ],
  tasks: [],
  bugs: []
}

// 需求模式(REQ-00001)
{
  mode: "需求",
  version: "V0.0.2",
  reqNum: "REQ-00001",
  targetReq: {
    id: "REQ-00001",
    title: "Marketplace 根名称添加 -marketplace 后缀",
    status: "已完成",
    design: "已完成",
    plan: "已完成",
    tasks: [
      { taskId: { format: "old", type: "REQ", parentNum: "00001", taskNum: "00001", displayId: "REQ-00001-001" },
        title: "改 marketplace.json 根 name", devStatus: "已完成", testStatus: "不适用" },
      ...
    ]
  },
  bugs: []
}
```

### 版本策略
- **本数据结构为内部**:不暴露给外部,不参与序列化/反序列化
- **稳定性**:本技能不维护 ABI(无版本号)

### 兼容策略
- **无外部消费者**:不需兼容处理

### 依据规范
- `encoding-conventions.md §规则 3`:任务编号解析结果(`TaskId`)严格按 4 字段结构
