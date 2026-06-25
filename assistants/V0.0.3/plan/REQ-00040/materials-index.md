# 材料登记 — REQ-00040

更新时间:2026-06-25
版本:V0.0.3

## 项目级规范

| 规范文件 | 类别 | 关键约束摘要 | 触发? |
| --- | --- | --- | --- |
| `coding-style.md` | 命名 / 风格 | 占位(规则 1 待添加);SKILL.md 是自然语言,代码风格不直接约束 | ❌ |
| `commit-conventions.md` | 提交 | 占位(规则 1 待添加);沿用既有 `chore(code-it): ...` / `chore(code-design): ...` / `chore(code-plan): ...` 前缀 | ⚠️ 软 |
| `dashboard-conventions.md` | 看板 | §规则 1:看板字段扩展需三同步;本设计**不**新增看板列(产物放 `fix/<BUG-NNN>/reproduce/` 子目录),**0 触发** | ❌(0 触发) |
| `dependency-conventions.md` | 三方依赖 | 占位(规则 1 待添加);本设计**0 新增三方依赖** | ❌(0 新增) |
| `directory-conventions.md` | 目录 | §规则 1 占位;沿用 `code-fix/templates/` 既有目录布局;`reproduce/` 子目录在 `fix/<BUG-NNN>/` 内(运行时) | ⚠️ 软 |
| `doc-conventions.md` | 文档 | README 多语言对仗;**0 触发** | ❌ |
| `encoding-conventions.md` | 编码格式 | §规则 1:3 类编码(REQ/BUG/TASK)正则;**不**触发(本需求**不**新增编码格式) | ❌ |
| `framework-conventions.md` | 架构 | 框架级约束;**不**触发 | ❌ |
| `marketplace-protocol.md` | 插件市场 | marketplace.json / plugin.json 元信息;**不**触发 | ❌ |
| `migration-mapping.md` | 迁移映射 | 旧→新编码追溯;**不**触发 | ❌ |
| `module-conventions.md` | 模块 | ⚠️ **DEPRECATED**;**不**引用 | ❌ |
| `naming-conventions.md` | 命名 | 占位(规则 1 待添加);`reproduce/` 命名遵循"小写 + 复数"风格 | ⚠️ 软 |
| `skill-conventions.md` | 技能 | §规则 1:SKILL.md frontmatter(name + description)必含;§规则 2:SKILL.md / templates/ 不得含开发痕迹字面(6 类强约束) | ✅ **强**(§规则 1 字节级保留;§规则 2 本设计**不**在产物 SKILL.md / 模板中写"本需求 REQ-00040 新增"等字面) |

## 上游需求

- 来源:`./assistants/V0.0.3/require/REQ-00040/RESULT.md`
- 版本:v1(2026-06-25)
- 提取:6 FR / 10 NFR / 12 AC

### 关键交叉点(每条 FR 对应的设计章节)

| FR | 上游字面摘要 | 本详设对应章节 |
| --- | --- | --- |
| FR-1 | 步骤 0 末尾追加"项目可启动性探测" 子节 | §4.1 + `module-details.md §模块 1` |
| FR-2 | 步骤 6 末尾追加"复现产物登记" 子节 | §4.2 + `module-details.md §模块 2` |
| FR-3 | 3 类产物收集(日志/截图/交互数据) | §5 算法 + `interface-specs.md` §3 个接口 |
| FR-4 | 产物子目录 `fix/<BUG-NNN>/reproduce/` | §4.3 + `module-details.md §模块 3` |
| FR-5 | `bug.md` 模板新增"## 复现产物登记" 区段 | §6.1 + `module-details.md §模块 4` |
| FR-6 | 文档头新增 2 字段(复现方式/产物路径) | §6.2 + `module-details.md §模块 4` |

## 上游概要设计

- 来源:`./assistants/V0.0.3/design/REQ-00040/RESULT.md`
- 版本:v1(2026-06-25)
- 设计目标:`--balanced`(功能性=高,扩展性=低,健壮性=中,可维护性=中,封装性=不适用,可复用性=不适用,可读性=高)

### 关键交叉点(每条决策对应的详设章节)

| 上游决策 | 决策字面 | 本详设对应章节 |
| --- | --- | --- |
| D-1 | 启动能力自动探测 | §4.1 步骤 0 末尾子节(伪代码) |
| D-2 | 产物放 `fix/<BUG-NNN>/reproduce/` 子目录 | §4.3 产物子目录结构 |
| D-3 | 复现动作不触发状态推进 | §9 状态机(沿用 REQ-00037) |
| D-4 | 失败降级链 | §7 异常处理(8 边界) |
| D-5 | 截图工具链式降级 | §5.2 截图采集算法 |
| D-6 | `bug.md` 新区段插入位置 | §6.1 模板扩展点 |
| D-7 | 文档头新增 2 字段 | §6.2 文档头扩展 |
| D-8 | 同步更新 `assistants-layout.md` | §6.3 目录结构说明同步 |
| D-9 | 不新建 `code-fix/lib/` 共享库 | §4 SKILL.md 内联伪代码(无 lib 目录) |
| D-10 | `reproduce/` 不加 `.gitignore` | §10 NFR-9 不修改项目配置 |

### 10 项不变量(INV)

- INV-1~3:`code-fix/SKILL.md` frontmatter / 既有"## 工作流程" 步骤 0 主体 / 步骤 1~10 主体 / "## 不要做的事" 字节级保留
- INV-4:`bug.md` 既有 9 区段字节级保留;**只**在文档头表追加 2 行 + 在"## 缺陷描述" 段后插入"## 复现产物登记" 区段
- INV-5:历史 5 个 BUG 的 `fix/<BUG-NNN>/RESULT.md` 字节级保留
- INV-6:`code-fix` 初始态 = `待处理`,状态推进路径字节级保留
- INV-7:`fix/RESULT.md` 总览表 7 列 + 看板"缺陷清单" 区段 8 列字节级保留
- INV-8:`code-fix/SKILL.md` / `bug.md` 模板**不**含 6 类开发痕迹字面

## 项目现状(实现细节)

### `code-fix/SKILL.md` 关键锚点

| 锚点 | 行号 | 用途 |
| --- | --- | --- |
| 步骤 0 第 4 项 | line 181 | **本轮**追加"项目可启动性探测" 子节(在 line 181 后,line 182 `### 步骤 1` 前) |
| 步骤 6 末尾注释 | line 305 | **本轮**追加"复现产物登记" 子节(在 line 305 前,line 306 空行前) |
| 步骤 6 主体(line 277-305) | — | 字节级保留(不修改) |
| 步骤 0 主体(line 177-181) | — | 字节级保留(不修改) |
| frontmatter(L1-3) | — | 字节级保留(NFR-3) |
| "## 不要做的事" 段 | line 418+ | 字节级保留(NFR-3) |

### `bug.md` 模板关键锚点

| 锚点 | 行号 | 用途 |
| --- | --- | --- |
| 文档头"## 文档头" 表 | line 8-22 | **本轮**追加 2 行(复现方式 / 产物路径)(在 line 22 后,line 24 `### 状态枚举` 前) |
| "## 缺陷描述" 段后 + `---` 分隔符前 | line 60 | **本轮**追加"## 复现产物登记" 区段(在 line 60 前,line 61 `## 根因分析` 前) |
| 既有 9 区段 | — | 字节级保留(INV-4) |

### `assistants-layout.md` 关键锚点

| 锚点 | 行号 | 用途 |
| --- | --- | --- |
| `fix/<BUG-NNN>/` 子目录列表(line 16-19) | — | **本轮**追加 `reproduce/` 行(在 investigation.md / fix-plan.md 等之间) |

### 命名 / 错误 / 并发约定

- **命名风格**:`fix-plan.md` / `fix-work-log.md` 等以 `fix-` 前缀与主流程区分;本需求沿用相同风格,`reproduce/` 命名(小写 + 复数)
- **错误模型**:`code-fix` 沿用 NFR-4 失败降级模式(屏显 `⚠` + 记录原因 + 继续登记),**不**抛异常
- **并发模型**:无(本需求**不**涉及并发);子进程运行由 `code-fix` 步骤 6 末尾子节独立计时,60s 超时后终止
- **既有相似实现**:`code-it/lib/logic-loc.md` 共享库(FR-2 `tokei/cloc/heuristic` 链式降级);本需求**不**新建 `code-fix/lib/`,沿用"SKILL.md 内联伪代码" 模式(参 D-9)

## 本次变更源(首次设计)

| 变更源 | 检测方式 | 变化列表 |
| --- | --- | --- |
| 需求侧 | 上游 `require/REQ-00040/RESULT.md` | 首次创建(无变更) |
| 概要设计侧 | 上游 `design/REQ-00040/RESULT.md` | 首次创建(无变更) |
| 规范侧 | `./assistants/rules/` 对比 | 0 变更(13 份规范未动) |
| 代码侧 | 重跑项目探索(`code-fix` 子树) | 0 变更 |
