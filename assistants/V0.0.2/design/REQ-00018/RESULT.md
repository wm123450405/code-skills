# 概要设计 — REQ-00018(优化 `/code-version` 技能 — 切换版本时同步 CWD 项目描述文件版本号)

- 需求编码:REQ-00018
- 所属版本:V0.0.2
- 文档版本:v1
- 状态:已锁定
- 责任人:wangmiao
- 创建:2026-06-06
- 最近更新:2026-06-06 13:00
- 当前版本:v1
- **主题**(来自用户输入):
  > 优化 `/code-version` 技能,要求切换到新版本时,要修改当前项目和模块相关描述文件(如 pom.xml、package.json、manifest.json 等,项目工程类型或模块工程类型不同修改对应的描述文件)中的各版本号的声明同步
- 上游:`./assistants/V0.0.2/require/REQ-00018/RESULT.md`
- 遵循规范:`./assistants/rules/` 下 13 个文件

## 设计目标

- 整体设计目标:`--balanced`
- 维度优先级:
  - 功能性:**高**(FR-1~FR-6 全部完整实现)
  - 扩展性:**—**(本需求不引入架构抽象层,Q-8 派生建议留作 v2 follow-up)
  - 健壮性:**高**(5 类屏幕输出契约全有 + NFR-8 失败不阻断 + 0 命中不报错)
  - 可维护性:**—**(1 个 SKILL.md 追加,不重构既有步骤 1~6)

## 1. 概述

REQ-00018 优化 `code-version` 技能:在步骤 6 之后**追加**"步骤 7 — CWD 描述文件版本号同步",在 CWD 下扫描已知工程类型描述文件(`package.json` / `pom.xml` / `manifest.json` / `Cargo.toml` / `pyproject.toml` / `go.mod`),识别版本号字段,Edit 为新激活的 `<版本号>`。

**核心架构决策**:
1. **增量追加**(沿用 REQ-00005 / REQ-00010 模式):**不**重写 `code-version/SKILL.md` 既有步骤 1~6,只在"## 工作流程"段后追加"## 步骤 7"小节,frontmatter 字节级保留
2. **扫描 6 类描述文件**(FR-1 锁定优先级):`package.json` > `pom.xml` > `manifest.json` > `Cargo.toml` > `pyproject.toml` > `go.mod`
3. **每类文件独立解析契约**(FR-1.AC-1.3):不同文件类型用不同的 Edit 锚点
4. **失败不阻断**(NFR-8 强约束):CWD 同步是辅助能力,任一文件失败**不**影响 `code-version` 退出码
5. **不引入 CLI 参数**(Q-7 采纳默认):`--skip-cwd-sync` 留作 v2 follow-up,本需求**不**实现
6. **不修改 `code-skills` 自身**(Q-1 锁定):本需求 0 修改 `marketplace.json` / `plugin.json` / 其他 SKILL.md / 自身描述文件

## 2. 核心设计决策

### D-1:增量追加(锚点 = "## 工作流程" 段后)

**选择**:Edit 工具在 `code-version/SKILL.md` 锚点 `"## 看板字段约定" 之前` 插入"## 步骤 7 — CWD 描述文件版本号同步(REQ-00018 新增)"小节

**理由**:
- 沿用 REQ-00005 / REQ-00010 既有"增量追加,不改 frontmatter"模式(REQ-00005 NFR-2)
- frontmatter 字节级保留(skill-conventions §规则 1 强约束)
- 既有"步骤 1~6"流程不被打断
- 既有"看板字段约定"段不被干扰

**否决方案**:
- **B 方案**:`Write` 整体重写 `code-version/SKILL.md` → 风险高(破坏 frontmatter / 既有流程),违反 skill-conventions §规则 1

### D-2:扫描优先级(FR-1 锁定)

**选择**:固定优先级 `package.json` → `pom.xml` → `manifest.json` → `Cargo.toml` → `pyproject.toml` → `go.mod`

**理由**:
- 需求原文列举顺序(`pom.xml` / `package.json` / `manifest.json`)
- `package.json` 优先(覆盖 Node.js / VSCode Extension / npm package 3 类场景,使用面最广)
- monorepo 场景下"所有匹配的描述文件都改"(Q-4 采纳默认),无优先级冲突

**否决方案**:
- **B 方案**:同时编辑 6 类 → monorepo 场景下行为不可预测(N 个匹配全改)
- **C 方案**:按文件大小优先 → 没有合理依据

### D-3:Edit 锚点(每类文件独立)

**选择**:每类描述文件用不同的"版本号字段"锚点(FR-1.AC-1.3 锁定的 6 类锚点)

| 描述文件 | 解析锚点 | Edit 模式 |
| --- | --- | --- |
| `package.json` | `"version": "<旧版本号>"` | Edit 单行 JSON 字段 |
| `pom.xml` | `<version><旧版本号></version>` | Edit 单行 XML 字段 |
| `manifest.json` | `"version": "<旧版本号>"` | Edit 单行 JSON 字段 |
| `Cargo.toml` | `version = "<旧版本号>"` | Edit 单行 TOML 字段 |
| `pyproject.toml` | `version = "<旧版本号>"` | Edit 单行 TOML 字段 |
| `go.mod` | N/A | **不**修改,屏幕输出 `⚠` |

**理由**:
- 字段锚点与既有"### 7.3 描述文件解析契约"完全对齐(需求文档 §7.3)
- `go.mod` 不用字段(Go 用 git tag)

**否决方案**:
- **B 方案**:用 JSON 解析器 / XML 解析器 → 引入新依赖(违反 NFR-1 零依赖);对 monorepo 多 package.json 场景处理复杂

### D-4:失败不阻断(NFR-8 强约束)

**选择**:CWD 同步是辅助能力,任一文件失败 / 0 命中 / 解析失败 / 缺版本号字段 / 无写权限 / Edit 失败 → 屏幕打印 `⚠`,**不**影响 `code-version` 退出码(仍 0)

**理由**:
- `code-version` 主职责是"切版本",CWD 同步是辅助能力
- 沿用既有 `code-version` "步骤 6 验证与汇报" 的"汇报"风格(已存在各种 `⚠` 屏幕输出)

**否决方案**:
- **B 方案**:失败就报错退出 → 与 `code-version` 主流程耦合过紧,违反"主职责 + 辅助能力"分层

### D-5:不引入 CLI 参数(Q-7 采纳默认)

**选择**:`--skip-cwd-sync` / `--cwd=<path>` / `--version-string=<str>` 3 个参数**全部**留作 v2 follow-up,本需求**不**实现

**理由**:
- 需求文档 §12 Q-7 明确"本需求不实现 `--skip-cwd-sync`,留作 v2 follow-up"
- 沿用既有 `--skip-*` 命名约定(v2 再实现)
- 避免本需求"功能膨胀"影响 review 收敛速度

**否决方案**:
- **B 方案**:本需求实现 `--skip-cwd-sync` → Q-7 明确反对,引入未澄清的边界(用户何时用)

## 3. 模块与文件影响

### 3.1 受影响文件清单(本需求只改 1 个文件)

| 文件 | 状态 | 变更类型 | 涉及小节 |
| --- | --- | --- | --- |
| `plugins/code-skills/skills/code-version/SKILL.md` | **修改** | 增量追加 | 锚点 = "## 工作流程" 段后 / "## 看板字段约定" 段前,新增"## 步骤 7 — CWD 描述文件版本号同步(REQ-00018 新增)"小节 |

**明确不修改**(Q-1 锁定 + NFR-3~NFR-6):
- 其他 12 个 `code-*` SKILL.md
- `marketplace.json` / `plugin.json`
- `README.md` / `README.en.md` / `CLAUDE.md`
- `./assistants/rules/` 13 份规范
- `plugins/code-skills/skills/code-version/templates/version-RESULT.md`

### 3.2 步骤 7 子小节结构(注入到 SKILL.md)

```
## 步骤 7 — CWD 描述文件版本号同步(REQ-00018 新增)

### 7.1 目标
[1 段说明]

### 7.2 触发条件
- 步骤 3 决定激活此版本后(情形 A/B/C/D 任意一种,选 A/B/C 时触发;选 C 取消时不触发)

### 7.3 算法
[7 步伪代码]

### 7.4 通过条件
- 成功:屏幕输出 1+ 行 ✓ 日志
- 0 命中:屏幕输出 ⚠
- 失败不阻断(NFR-8):退出码仍 0

### 7.5 屏幕输出契约
[5 类输出格式:✓ / ⚠0 命中 / ⚠解析失败 / ⚠缺版本号字段 / ⚠go.mod]

### 7.6 边界与异常
[E-1 ~ E-8 共 8 个边界场景]

### 7.7 性能
[单文件 ~1 秒,monorepo 10 个文件 ~5 秒]

### 7.8 与步骤 1~6 协同
[不修改既有步骤 1~6 的语义]
```

### 3.3 关键变更(锚点 = SKILL.md 既有"## 工作流程"段后)

```ts
// 在 plugins/code-skills/skills/code-version/SKILL.md 锚点 "## 看板字段约定" 之前插入
// 不修改 frontmatter(L1-3 字节级保留)
// 不修改既有"## 工作流程"小节
// 不修改既有"## 看板字段约定"小节
// 新增"## 步骤 7 — CWD 描述文件版本号同步(REQ-00018 新增)"小节
```

## 4. 接口与数据结构

### 4.1 接口契约(本技能对外无新接口)

`code-version` 本需求**不**新增对外接口(无 CLI 参数 / 无新 API 端点 / 无新函数导出)。

**输入**(沿用既有):
- 版本号(命令行参数 / 用户交互)
- CWD 路径(沿用既有 `process.cwd()`,**不**新增 `--cwd` 参数)

**输出**(沿用既有 + 新增):
- 既有:`./assistants/.current-version` 更新 + `./assistants/<版本号>/` 创建/切换
- 新增:屏幕输出"## 步骤 7" 5 类契约(FR-5 锁定)

### 4.2 数据结构(本需求不引入新数据结构)

| 数据 | 用途 | 状态 |
| --- | --- | --- |
| 描述文件版本号 | 解析 CWD 描述文件得到 | 临时(只在步骤 7 内部用) |
| 新版本号 | 取自新激活的 `<版本号>` | 临时(沿用既有 `<版本号>` 变量) |

**不引入**新数据模型 / 不修改既有数据结构 / 不修改 `RESULT.md` 看板模板(NFR-6 严守)。

## 5. 三方依赖评估(NFR-1 强约束)

**结论**:**0 新增依赖**。

**评估明细**:
- 工具:`Bash` / `Read` / `Glob` / `Grep` / `Edit` / `Write`(全部既有,无新增)
- 库:无(不引入 JSON 解析器 / XML 解析器 / TOML 解析器,改用 `Read` + `Edit` + 行匹配)
- 命令:无(不调用 jq / xmllint / python 等外部命令)

**理由**:沿用 REQ-00009 NFR-1 既有"零新增依赖"模式,符合 dependency-conventions 既有约束。

## 6. 关联设计

| 关联设计 | 关联点 | 对本设计的影响 | 链接 |
| --- | --- | --- | --- |
| **REQ-00005**(V0.0.2) | 优化 `code-require` / `code-design` / `code-plan` 3 个技能;**NFR-2** 强约束"不破坏 frontmatter" | **0 冲突**(本需求沿用同样的"增量追加,不改 frontmatter"模式 — D-1 选定 A) | [design/REQ-00005/RESULT.md](../REQ-00005/RESULT.md) |
| **REQ-00009**(V0.0.2) | `code-unit` 步骤 0a Glob 检查项目可测性;**NFR-1 零新增依赖** | **0 冲突**(本需求**也**用 `Glob` 扫描 CWD 文件,与 REQ-00009 模式一致 — D-5 选定 A 零依赖) | [design/REQ-00009/RESULT.md](../REQ-00009/RESULT.md) |
| **REQ-00015**(V0.0.2) | `code-merge` 技能加入 marketplace;**NFR-3** marketplace 既有字段不变 | **0 冲突**(本需求**不**修改 `marketplace.json` / `plugin.json` / `code-skills` 自身产物 — Q1 锁定) | [design/REQ-00015/RESULT.md](../REQ-00015/RESULT.md) |
| **REQ-00017**(V0.0.2) | `code-plan` 不拆"更新看板"任务;**强约束** "1 任务 = 1 实际产出" | **0 冲突**(本需求拆任务时**不**包含"更新看板"派生任务,严守 REQ-00017) | [design/REQ-00017/RESULT.md](../REQ-00017/RESULT.md) |

## 7. 屏幕输出契约(FR-5 锁定)

| 场景 | 屏幕输出格式 |
| --- | --- |
| 成功(`package.json` / `pom.xml` / `manifest.json` / `Cargo.toml` / `pyproject.toml` 命中) | `✓ CWD 描述文件同步:<filename>: <旧版本号> → <新版本号>` |
| 0 命中(CWD 无任何已知描述文件) | `⚠ CWD 下未检测到任何已知工程类型描述文件,跳过同步` |
| 解析失败(非 JSON / 非标准 XML / 非标准 TOML) | `⚠ <filename> 格式不可解析,跳过` |
| 缺版本号字段(`package.json` 缺 `"version"`) | `⚠ <filename> 未找到版本号字段,跳过` |
| `go.mod` 命中(Go 用 git tag) | `⚠ go.mod 无版本号字段(Go 用 git tag),跳过` |

**输出格式不变量**:
- `✓` 开头 = 成功
- `⚠` 开头 = 警告(失败 / 跳过)
- 单行 / 不分页 / UTF-8

## 8. 边界与异常(E-1 ~ E-8)

| ID | 场景 | 处理 |
| --- | --- | --- |
| **E-1** | CWD 下有多个描述文件(monorepo) | 修改**所有**匹配的描述文件,屏幕打印每行 |
| **E-2** | CWD 下找不到任何描述文件 | 屏幕打印 `⚠ ... 跳过同步`,不报错不阻断 |
| **E-3** | 描述文件存在但格式不可解析 | 屏幕打印 `⚠ <filename> 格式不可解析,跳过` |
| **E-4** | 描述文件存在但**无**版本号字段 | 屏幕打印 `⚠ <filename> 未找到版本号字段,跳过` |
| **E-5** | `--skip-cwd-sync` CLI 参数指定 | (本需求**不**实现,留作 v2 follow-up — Q-7) |
| **E-6** | `go.mod` 命中 | 屏幕打印 `⚠ go.mod 无版本号字段(Go 用 git tag),跳过` |
| **E-7** | 描述文件无写权限(只读) | 屏幕打印 `⚠ <filename> 无写权限,跳过`(本需求可选支持,不影响主流程) |
| **E-8** | 描述文件被另一个进程修改(并发) | Edit 可能失败 → 屏幕打印 `⚠ <filename> Edit 失败(<错误>),跳过` |

## 9. 性能(NFR-7)

| 文件数 | 估算耗时 |
| --- | --- |
| 0 文件 | < 0.5 秒(纯 Glob 扫描) |
| 1 个文件 | < 1 秒 |
| 5 个文件(monorepo 中等) | < 3 秒 |
| 10 个文件(monorepo 大型) | < 5 秒(NFR-7 上限) |
| > 20 个文件 | 退化,屏幕打印 `⚠ 同步耗时较长` 但不阻断 |

## 10. 测试要点

| 维度 | 验证方法 | 通过标准 |
| --- | --- | --- |
| 单文件命中 | 在临时目录创建 `package.json` + `pom.xml`,调 `code-version V0.0.3` | 屏幕输出 2 行 `✓`,2 个文件 `version` 字段更新 |
| 0 命中 | 在临时目录(空),调 `code-version V0.0.3` | 屏幕输出 1 行 `⚠ CWD 下未检测到...`,退出码 0 |
| 解析失败 | 在临时目录创建非法 `package.json`,调 `code-version V0.0.3` | 屏幕输出 1 行 `⚠ package.json 格式不可解析...`,退出码 0 |
| 缺版本号字段 | 在临时目录创建 `package.json` 无 `version` 字段,调 `code-version V0.0.3` | 屏幕输出 1 行 `⚠ package.json 未找到版本号字段...`,退出码 0 |
| `go.mod` | 在临时目录创建 `go.mod`,调 `code-version V0.0.3` | 屏幕输出 1 行 `⚠ go.mod 无版本号字段...`,退出码 0 |
| 失败不阻断 | 在临时目录创建非法 `package.json`,调 `code-version V0.0.3` | 步骤 7 失败但 `.current-version = V0.0.3` 仍被写入,退出码 0 |
| frontmatter 保留 | 调 `code-version V0.0.3` 后 `Read` SKILL.md L1-3 | L1-3 字节级与本需求前一致 |
| 既有步骤 1~6 不变 | 调 `code-version V0.0.3` 后 `Read` SKILL.md "## 工作流程" 小节 | 与本需求前一致 |

## 11. 规范遵循

- ✅ **skill-conventions §规则 1**(SKILL.md 必含 name + description,frontmatter 字节级保留)— **D-1 严守**
- ✅ **module-conventions §规则 1**(资源放固定子目录)— 本需求**不**新增资源文件,沿用既有 SKILL.md 锚点
- ✅ **dependency-conventions**(零新增依赖)— **NFR-1 严守**
- ✅ **commit-conventions**(commit 消息格式)— 由 `code-it` / `code-auto` 末步兜底,本设计**不**直接涉及
- ✅ **encoding-conventions**(任务编号正则)— 本需求**不**涉及任务编号(由 `code-plan` 决定)
- ✅ **dashboard-conventions §规则 1**(看板字段扩展需三方同步)— 本需求**不**扩展看板字段,严守

## 12. 待澄清 / 未决项

| 编号 | 内容 | 状态 |
| --- | --- | --- |
| Q-1 | 需求范围:通用技能增强 + 扫描 CWD,不改 `code-skills` 自身 | **已锁定**(用户回答 A) |
| Q-2 | 术语:`manifest.json`(社区主流拼写) | **已锁定**(用户回答 A) |
| Q-3 | 项目/模块两类描述文件同时支持 | 采纳默认(同时改,按需) |
| Q-4 | monorepo 不特殊处理 | 采纳默认(Glob 找到的全改) |
| Q-5 | 版本号默认值 = 新激活的 `<版本号>` | 采纳默认 |
| Q-6 | 0 命中不报错不阻断 | 采纳默认(屏幕 `⚠`) |
| Q-7 | `--skip-cwd-sync` 不实现 | 采纳默认(留作 v2 follow-up) |
| Q-8 | 派生建议:`code-rule` 沉淀 `cwd-sync-conventions.md` + `code-version` 升级接受 CLI 参数 | 留作 follow-up(本需求**不**派生任务) |

## 13. 变更记录

| 时间 | 版本 | 变更摘要 | 变更人 |
| --- | --- | --- | --- |
| 2026-06-06 13:00 | v1 | 初始创建:5 决策 / 8 边界 / 1 文件修改 / 0 文件新增 / 0 新增依赖;沿用 REQ-00005 / REQ-00010 "增量追加,不改 frontmatter"模式;沿用 REQ-00009 "零新增依赖 + Glob 模式";Q-1 锁定"通用技能增强 + 扫描 CWD,不改 code-skills 自身";Q-2 锁定"manifest.json";Q-7 采纳默认"不实现 --skip-cwd-sync";NFR-8 失败不阻断;本设计严守 NFR-3/4/5/6 不修改其他 12 个 SKILL.md / marketplace / README / 规范 / 看板模板 | wangmiao |
