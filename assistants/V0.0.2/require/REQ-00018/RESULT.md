# 需求提示词文档 — REQ-00018(优化 `/code-version` 技能 — 切换版本时同步 CWD 项目描述文件版本号)

- 需求编码:REQ-00018
- 所属版本:V0.0.2
- 文档版本:v1
- 状态:已锁定
- 责任人:wangmiao
- 创建:2026-06-06
- 最近更新:2026-06-06 12:45
- 当前版本:v1
- **主题**(来自用户输入):
  > 优化 `/code-version` 技能,要求切换到新版本时,要修改当前项目和模块相关描述文件(如 pom.xml、package.json、manifest.json 等,项目工程类型或模块工程类型不同修改对应的描述文件)中的各版本号的声明同步

---

## 1. 需求概述

**为谁**:`code-skills` 仓库的 AI 协作者 + 使用 `code-skills` 工作的项目主导者(在调用 `code-version` 切换版本时,期望"切换到新版本"自动同步当前项目/模块的工程描述文件中的版本号声明,避免人工手动修改 pom.xml / package.json / manifest.json 等)。

**解决什么问题**:当前 `code-version` 技能**仅**管理 `./assistants/<版本号>/` 版本工作空间(目录创建 + `.current-version` 切换 + 看板初始化),**不**关心"用户实际工作的项目"(`code-skills` 之外的工程)的描述文件版本号。在以下场景会导致问题:
- **项目版本号陈旧**:用户在用 `code-skills` 管理一个 Node.js 项目,`code-version V0.0.2` 后,`package.json` 仍是 `"version": "0.0.1"` — 与新激活的工作空间不匹配
- **多工程类型**:用户可能用 Maven Java(`pom.xml`)/ Node.js(`package.json`)/ VSCode Extension(`manifest.json` package.json) 等不同工程类型,每个工程的"版本号字段"位置不同
- **CI/批处理场景**:CI 跑 `code-version` 后,期望自动 commit "项目版本号同步"变更,而不是 dirty tree

**带来什么价值**:
1. **通用技能增强**:`code-version` 切换版本后,自动扫描 CWD(当前工作目录)下的工程类型,识别对应的描述文件,同步版本号
2. **项目/模块并行支持**:同时支持"项目"和"模块"两类描述文件(`code-skills` 仓库**不**是项目工程 → 本需求不修改 `code-skills` 自身)
3. **零规范变更**:不修改 9 个其他 `code-*` 技能 / 不修改 `code-skills` 自身 / 不修改 `marketplace.json` / `plugin.json` / README / 中英 CLAUDE.md
4. **屏幕可观测**:每次同步打印 `<文件名>: <旧版本号> → <新版本号>` 日志;未检测到任何已知工程类型时打印 `⚠` 警告但不阻断

## 2. 背景与目标

### 2.1 背景
- `code-version` 是 V0.0.0 起就存在的 8 个 `code-*` 之一;V0.0.1 中 21/21 任务均已 `code-version` 完成
- V0.0.2 中 REQ-00005 / REQ-00009 / REQ-00010 / REQ-00013 / REQ-00017 等多个需求对 9 个 `code-*` 技能做了增强
- 截至 REQ-00018,**尚无**任何需求覆盖"切换版本时同步 CWD 项目工程描述文件"
- CWD 项目类型识别模式沿用 REQ-00009 既有 `Glob` 实践(7 项文件检查)

### 2.2 业务目标
- **G-1**:`code-version` 切换版本后,自动扫描 CWD 下的工程类型,识别对应的描述文件,同步版本号
- **G-2**:"项目"和"模块"两类描述文件**同时**支持(Q3 锁定)
- **G-3**:版本号默认值 = 新激活的 `<版本号>`(Q5 锁定)
- **G-4**:`code-version` 已有"创建新版本" / "切到已有版本" 2 条主路径,**两条**路径都应触发 CWD 同步(FR-1)
- **G-5**:`code-version` **不**修改 `code-skills` 自身(Q1 锁定)— 只在 CWD 是 `code-skills` 仓库根时,与"扫描"模式兼容(扫描会找到 0 个已知工程类型文件 → 走 E-2 警告)
- **G-6**:**不**破坏既有 `code-version` 行为(Q-7 采纳默认)— 切换 / 创建 / 同版本再确认 / 取消等所有情形仍按既有逻辑处理;CWD 同步是**额外**能力,失败不阻断

### 2.3 本次目标
- 修改 `plugins/code-skills/skills/code-version/SKILL.md` 正文(不改 frontmatter,不改"步骤 1~6"既有流程)
- 新增"## 步骤 7 — CWD 描述文件版本号同步(REQ-00018 新增)"小节(锚点 = "## 工作流程" 之后 / "## 看板字段约定" 之前)
- 严格遵循 `skill-conventions.md §规则 1`(frontmatter 不变)
- 不修改 9 个其他 `code-*` 技能 / `marketplace.json` / `plugin.json` / 中英 README / 中英 CLAUDE.md / `assistants/rules/`
- 不参与 REQ-00005 的"首步拉取 + 末步提交"扩展(留作 follow-up)

## 3. 用户角色与场景

### 3.1 角色
- **R-1 项目主导者**:在 `code-skills` 管理下,用同一 `code-version` 切换多个工程(Java / Node / VSCode Extension),期望自动同步
- **R-2 长会话 AI**:在多项目间切换,可能误激活错误工程类型
- **R-3 CI/批处理用户**:CI 跑 `code-version` 后,期望自动 commit "项目版本号同步"变更

### 3.2 关键场景

#### S-1:Maven Java 项目切换版本(主流程,扫描命中)
- 假设 CWD = `~/work/my-app/`(Maven Java 项目,`pom.xml` 存在,`<version>0.0.1</version>`)
- 用户输入:`code-version V0.0.3`
- 技能执行:
  1. **步骤 4A** 创建新版本 `V0.0.3` 工作空间
  2. **步骤 7(新增)** CWD 描述文件版本号同步
     - 扫描 CWD → 命中 `pom.xml`
     - 解析 `<version>0.0.1</version>` → 旧版本号 = `0.0.1`
     - 新版本号 = `V0.0.3`(默认值,见 Q5)
     - Edit `pom.xml`:`<version>0.0.1</version>` → `<version>V0.0.3</version>`
     - 屏幕输出 `✓ CWD 描述文件同步:pom.xml: 0.0.1 → V0.0.3`
  3. **步骤 5** 写 `.current-version = V0.0.3`
  4. 退出码 0
- 用户看到:`code-version V0.0.3` 切换完成 + `pom.xml` 已同步(无需手动改)

#### S-2:Node.js 项目切换版本(主流程,扫描命中)
- 假设 CWD = `~/work/my-app/`(Node.js 项目,`package.json` 存在,`"version": "1.0.0"`)
- 用户输入:`code-version V0.0.3`
- 技能执行:
  1. **步骤 4A/4C** 创建/切换版本 `V0.0.3`
  2. **步骤 7(新增)** CWD 同步
     - 扫描 CWD → 命中 `package.json`(优先,Maven 不存在)
     - 解析 `"version": "1.0.0"` → 旧 = `1.0.0`
     - 新版本号 = `V0.0.3`
     - Edit `package.json`:`"version": "1.0.0"` → `"version": "V0.0.3"`
     - 屏幕输出 `✓ CWD 描述文件同步:package.json: 1.0.0 → V0.0.3`
  3. 退出码 0

#### S-3:monorepo 多描述文件(边界,E-1)
- 假设 CWD = `~/work/my-monorepo/`(monorepo,`package.json` 根 + 多个子项目 `packages/*/package.json`)
- 用户输入:`code-version V0.0.3`
- 技能执行:
  1. **步骤 4A/4C** 创建/切换版本 `V0.0.3`
  2. **步骤 7(新增)** CWD 同步
     - 扫描 CWD → 命中 1 个根 `package.json` + N 个子 `packages/*/package.json`
     - 对**每个**匹配文件 Edit + 屏幕输出
  3. 屏幕输出多行(如 N=3):
     ```
     ✓ CWD 描述文件同步:package.json: 1.0.0 → V0.0.3
     ✓ CWD 描述文件同步:packages/a/package.json: 1.0.0 → V0.0.3
     ✓ CWD 描述文件同步:packages/b/package.json: 1.0.0 → V0.0.3
     ```
- (Q-4 采纳默认,monorepo 不特殊处理)

#### S-4:CWD 无任何描述文件(边界,E-2)
- 假设 CWD = `~/work/random/`(纯文档目录,无 pom.xml / package.json / manifest.json)
- 用户输入:`code-version V0.0.3`
- 技能执行:
  1. **步骤 4A/4C** 创建/切换版本
  2. **步骤 7(新增)** CWD 同步
     - 扫描 CWD → 0 命中
     - 屏幕输出 `⚠ CWD 下未检测到任何已知工程类型描述文件,跳过同步`
     - **不**报错,**不**阻断
  3. 退出码 0

#### S-5:CWD = `code-skills` 仓库根(同 S-4,扫描 0 命中)
- 假设 CWD = `~/work/code-skills/`(本仓库根,无 pom.xml / package.json / manifest.json)
- 用户输入:`code-version V0.0.3`
- 技能执行:同 S-4,屏幕输出 `⚠`,**不**修改 `code-skills` 自身的 `marketplace.json` / `plugin.json`(本需求 0 修改,见 Q1)
- 退出码 0

#### S-6:格式不可解析(边界,E-3)
- 假设 CWD 命中 `package.json` 但**格式非法**(非标准 JSON,如 `package.json` 含未闭合括号)
- 技能执行:
  1. **步骤 4A/4C** 创建/切换版本
  2. **步骤 7(新增)** CWD 同步
     - 扫描 CWD → 命中 `package.json`
     - 尝试解析失败 → 屏幕输出 `⚠ package.json 格式不可解析,跳过`
     - **不**阻断
  3. 退出码 0

#### S-7:描述文件存在但无版本号字段(边界,E-4)
- 假设 CWD 命中 `package.json` 但**缺**`"version"` 字段
- 技能执行:同 S-6,屏幕输出 `⚠ package.json 未找到版本号字段,跳过`,**不**阻断

#### S-8:--skip-cwd-sync 跳过同步(边界,E-5)
- 假设用户输入 `code-version V0.0.3 --skip-cwd-sync`
- 技能执行:步骤 7 **跳过**,**不**扫描 CWD;既有步骤 1~6 完整执行
- 退出码 0
- (Q-7 采纳默认,`--skip-cwd-sync` 是新增 CLI 参数,沿用既有 `--skip-*` 命名约定)

## 4. 功能需求(FR)

### FR-1:新增"步骤 7 — CWD 描述文件版本号同步"
- **描述**:`code-version` 在"步骤 6 验证与汇报"**之后**,新增"步骤 7"扫描 CWD 下的工程类型描述文件,同步版本号
- **触发条件**:`code-version` 步骤 3 决定激活此版本后(情形 A / B / C / D 任意一种,选 A/B/C 时触发;选 C 取消时**不**触发);另支持 `--skip-cwd-sync` CLI 参数(选 D 同版本再确认时仍触发,因为仍可能需要同步)
- **AC**:
  - AC-1.1:在 `code-version/SKILL.md` 步骤 6 之后显式列出"步骤 7"
  - AC-1.2:CWD 扫描使用 `Glob`,支持以下文件(按优先级):
    1. `package.json`(Node.js / VSCode Extension / npm)
    2. `pom.xml`(Maven Java)
    3. `manifest.json`(Web App / PWA)
    4. `Cargo.toml`(Rust)
    5. `pyproject.toml`(Python)
    6. `go.mod`(Go)
  - AC-1.3:对每个命中文件 Edit 修改"版本号"字段:
    - `package.json`:`"version": "<旧版本号>"` → `"version": "<新版本号>"`
    - `pom.xml`:`<version><旧版本号></version>` → `<version><新版本号></version>`
    - `manifest.json`:`"version": "<旧版本号>"` → `"version": "<新版本号>"`
    - `Cargo.toml`:`version = "<旧版本号>"` → `version = "<新版本号>"`
    - `pyproject.toml`:`version = "<旧版本号>"` → `version = "<新版本号>"`
    - `go.mod`:**N/A** — Go 模块用 git tag,无版本号字段(命中后**不**修改,屏幕输出 `⚠ go.mod 无版本号字段,跳过`)
  - AC-1.4:屏幕输出契约(每次同步一行):
    ```
    ✓ CWD 描述文件同步:<filename>: <旧版本号> → <新版本号>
    ```
  - AC-1.5:0 命中时屏幕输出 `⚠ CWD 下未检测到任何已知工程类型描述文件,跳过同步`(E-2)
  - AC-1.6:解析失败时屏幕输出 `⚠ <filename> 格式不可解析,跳过`(E-3)
  - AC-1.7:缺版本号字段时屏幕输出 `⚠ <filename> 未找到版本号字段,跳过`(E-4)
  - AC-1.8:不修改 frontmatter;不修改"步骤 1~6"既有内容(增量追加)
  - AC-1.9:失败不阻断(E-2/E-3/E-4 都不影响退出码)

### FR-2:版本号取值规则
- **描述**:CWD 同步时,"新版本号"取自哪里
- **优先级**(从高到低):
  1. 用户通过 `code-version <版本号> --version-string=<自定义>` 显式指定(Q-5 留作 v2 follow-up,**本需求不实现** `--version-string` 参数,默认走下一条)
  2. 默认 = 新激活的 `<版本号>`(本需求默认值)
- **AC**:
  - AC-2.1:本需求默认值 = 新激活的 `<版本号>`(从 `<版本号>` 参数或 `.current-version` 取)
  - AC-2.2:屏幕输出"新版本号"在 `<新版本号>` 字段

### FR-3:CWD 路径确定
- **描述**:`code-version` 步骤 7 用哪个 CWD?
- **优先级**:
  1. 用户通过 `code-version <版本号> --cwd=<path>` 显式指定(Q-5 留作 v2 follow-up,**本需求不实现** `--cwd` 参数,默认走下一条)
  2. 默认 = CWD 进程实际工作目录(`process.cwd()`)
- **AC**:
  - AC-3.1:本需求默认 CWD = `process.cwd()`
  - AC-3.2:屏幕输出**不**显式打印 CWD(若用户需要查看可 `pwd`)

### FR-4:不修改 `code-skills` 自身 + 零规范变更
- **描述**:本需求**不**修改 `code-skills` 自身任何文件
- **AC**:
  - AC-4.1:`code-skills` 仓库根**不**新增 `package.json` / `pom.xml` / `manifest.json` 等描述文件
  - AC-4.2:CWD = `code-skills` 仓库根时,扫描**0 命中** + 屏幕输出 `⚠`,**不**尝试修改 `marketplace.json` / `plugin.json`(本需求 0 修改 `code-skills` 自身)
  - AC-4.3:**不**修改 9 个其他 `code-*` 技能 SKILL.md
  - AC-4.4:**不**修改 `marketplace.json` / `plugin.json` / `README.md` / `README.en.md` / `CLAUDE.md`(本需求 0 修改)
  - AC-4.5:**不**修改 `./assistants/rules/` 13 份规范

### FR-5:屏幕输出契约
- **描述**:步骤 7 屏幕输出格式
- **AC**:
  - AC-5.1:成功:`✓ CWD 描述文件同步:<filename>: <旧版本号> → <新版本号>`(每行一个文件)
  - AC-5.2:0 命中:`⚠ CWD 下未检测到任何已知工程类型描述文件,跳过同步`
  - AC-5.3:解析失败:`⚠ <filename> 格式不可解析,跳过`
  - AC-5.4:缺版本号字段:`⚠ <filename> 未找到版本号字段,跳过`
  - AC-5.5:go.mod 命中:`⚠ go.mod 无版本号字段(Go 用 git tag),跳过`

### FR-6:--skip-cwd-sync 跳过参数
- **描述**:用户可通过 `--skip-cwd-sync` 参数跳过步骤 7
- **AC**:
  - AC-6.1:`code-version <版本号> --skip-cwd-sync` → 步骤 7 **不**执行,屏幕输出 `⚠ CWD 描述文件同步已跳过(--skip-cwd-sync)`
  - AC-6.2:不影响其他步骤(步骤 1~6 完整执行)
  - AC-6.3:不影响退出码(仍 0)

## 5. 非功能需求 / 约束(NFR)

### NFR-1:零新增依赖
- **描述**:不引入新依赖;复用既有 `Bash` / `Read` / `Glob` / `Grep` / `Edit` / `Write` 工具
- **强制级别**:必须

### NFR-2:增量修改 SKILL.md
- **描述**:`code-version/SKILL.md` 修改方式为 **Edit 工具追加"步骤 7"小节**,不重写稳定章节
- **强制级别**:必须
- **理由**:避免破坏现有 frontmatter / 既有"步骤 1~6"流程 / 看板字段约定段

### NFR-3:不修改 9 个其他 `code-*` 技能
- **描述**:`code-require` / `code-design` / `code-plan` / `code-it` / `code-unit` / `code-review` / `code-fix` / `code-dashboard` / `code-publish` / `code-auto` / `code-init` / `code-rule` 等 12 个技能 SKILL.md **不**被本需求修改
- **强制级别**:必须

### NFR-4:不修改 `code-skills` 自身
- **描述**:`marketplace.json` / `plugin.json` / `README.md` / `README.en.md` / `CLAUDE.md` 等 5 个 `code-skills` 自身文件 **不**被本需求修改
- **强制级别**:必须

### NFR-5:不修改规范
- **描述**:`./assistants/rules/` 13 份规范 **不**被本需求修改
- **强制级别**:必须

### NFR-6:不修改 `version-RESULT.md` 看板模板
- **描述**:`plugins/code-skills/skills/code-version/templates/version-RESULT.md` **不**被本需求修改
- **强制级别**:必须
- **理由**:本需求是优化技能行为,不动看板模板

### NFR-7:性能
- **描述**:步骤 7 同步耗时 < 5 秒(单描述文件 ~1 秒;monorepo 10 个文件 ~5 秒)
- **强制级别**:必须

### NFR-8:失败不阻断
- **描述**:步骤 7 中任意文件解析失败 / 缺版本号字段 / 0 命中 / `--skip-cwd-sync` 都**不**影响 `code-version` 退出码(仍 0)
- **强制级别**:必须
- **理由**:`code-version` 主职责是"切版本",CWD 同步是辅助能力,不应因辅助失败阻塞主流程

### NFR-9:不参与 REQ-00005 的"首步拉取 + 末步提交"扩展
- **描述**:本需求**不**触发 REQ-00005 的扩展(本技能是 `code-version`,不是其他技能)
- **强制级别**:必须

## 6. 页面与界面(输出形态)

### 6.1 成功场景(S-1 / S-2 / S-3)

```
✓ CWD 描述文件同步:package.json: 1.0.0 → V0.0.3
```

### 6.2 0 命中(S-4 / S-5)

```
⚠ CWD 下未检测到任何已知工程类型描述文件,跳过同步
```

### 6.3 解析失败(S-6)

```
⚠ package.json 格式不可解析,跳过
```

### 6.4 缺版本号字段(S-7)

```
⚠ package.json 未找到版本号字段,跳过
```

### 6.5 go.mod(S-1 变体)

```
⚠ go.mod 无版本号字段(Go 用 git tag),跳过
```

### 6.6 --skip-cwd-sync(E-5)

```
⚠ CWD 描述文件同步已跳过(--skip-cwd-sync)
```

## 7. 交互逻辑

### 7.1 启动流程(改后)

```
[用户输入 /code-version <版本号>]
  ↓
[步骤 1: 收集版本号]
  ↓
[步骤 2: 检测版本工作空间]
  ↓
[步骤 3: 询问/确认操作意图]
  ↓
[步骤 4A/4C/4D: 创建/切换/再确认]
  ↓
[步骤 5: 更新 .current-version]
  ↓
[步骤 6: 验证与汇报]
  ↓
[步骤 7(新增): CWD 描述文件版本号同步] ─────┐
  ↓ (默认)                                      │ (--skip-cwd-sync / 0 命中 / 失败)
[退出 0]                                         │
                                                 │
[屏幕输出 + 退出 0] ←───────────────────────────┘
```

### 7.2 CWD 同步算法(Q-1 / Q-5 锁定)

```
[步骤 7 算法]
  ↓
[检查 --skip-cwd-sync 参数]
  ├─ true → 屏幕输出 `⚠ CWD 描述文件同步已跳过(--skip-cwd-sync)` → 退出
  └─ false → 继续
  ↓
[Glob CWD 已知描述文件]
  (优先级:package.json / pom.xml / manifest.json / Cargo.toml / pyproject.toml / go.mod)
  ↓
[对每个命中文件]
  ├─ 解析失败 → 屏幕输出 `⚠ <filename> 格式不可解析,跳过` → 继续下一文件
  ├─ 缺版本号字段(go.mod) → 屏幕输出 `⚠ go.mod 无版本号字段,跳过` → 继续下一文件
  ├─ 成功 → Edit 替换版本号 → 屏幕输出 `✓ CWD 描述文件同步:<filename>: <旧> → <新>` → 继续下一文件
  └─ 其他 → 屏幕输出 `⚠ <filename> 未知错误,跳过` → 继续下一文件
  ↓
[0 命中] → 屏幕输出 `⚠ CWD 下未检测到任何已知工程类型描述文件,跳过同步`
  ↓
[退出 0](失败不阻断)
```

### 7.3 描述文件解析契约

| 描述文件 | 解析锚点 | Edit 模式 |
| --- | --- | --- |
| `package.json` | `"version": "<旧版本号>"` | Edit 单行 JSON 字段 |
| `pom.xml` | `<version><旧版本号></version>` | Edit 单行 XML 字段 |
| `manifest.json` | `"version": "<旧版本号>"` | Edit 单行 JSON 字段(同 `package.json`) |
| `Cargo.toml` | `version = "<旧版本号>"` | Edit 单行 TOML 字段 |
| `pyproject.toml` | `version = "<旧版本号>"` | Edit 单行 TOML 字段(同 `Cargo.toml`) |
| `go.mod` | N/A | **不**修改 |

## 8. 数据与状态

### 8.1 描述文件版本号字段对照表

| 描述文件 | 类型 | 版本号字段 | 解析复杂度 |
| --- | --- | --- | --- |
| `package.json` | JSON | `"version": "x.y.z"` | O(n) JSON 扫描 |
| `pom.xml` | XML | `<version>x.y.z</version>` | O(n) XML 扫描 |
| `manifest.json` | JSON | `"version": "x.y.z"` | O(n) JSON 扫描 |
| `Cargo.toml` | TOML | `version = "x.y.z"` | O(n) TOML 扫描 |
| `pyproject.toml` | TOML | `version = "x.y.z"` | O(n) TOML 扫描 |
| `go.mod` | TOML-like | N/A(用 git tag) | **不**修改 |

### 8.2 任务编号解析(沿用 `code-dashboard` NFR-3)

```text
新格式正则: ^TASK-(REQ|BUG)-(\d{5})-(\d{5})$
旧格式正则: ^(REQ|BUG)-(\d{5})-(\d{5})$
```

### 8.3 屏幕输出格式(沿用 REQ-00013 NFR-3)

```ts
function truncateTitle(title: string, maxLen: number = 30): string {
  if ([...title].length <= maxLen) return title
  return [...title].slice(0, maxLen).join('') + '...'
}
```

## 9. 边界与异常

| ID | 场景 | 处理 |
| --- | --- | --- |
| E-1 | CWD 下有多个描述文件(单仓多项目 / monorepo) | 修改**所有**匹配的描述文件,屏幕打印每个文件的修改日志 |
| E-2 | CWD 下找不到任何描述文件 | 屏幕打印 `⚠ CWD 下未检测到任何已知工程类型描述文件,跳过同步`,不报错不阻断 |
| E-3 | 描述文件存在但格式不可解析(非 JSON / 非标准 XML / 非标准 TOML) | 屏幕打印 `⚠ <文件> 格式不可解析,跳过`,继续处理其他文件 |
| E-4 | 描述文件存在但**无**"版本号"字段(罕见,可能 `package.json` 缺 `"version"`) | 屏幕打印 `⚠ <文件> 未找到版本号字段,跳过`,继续处理其他文件 |
| E-5 | 用户通过 `code-version --skip-cwd-sync` 指定 | 跳过 CWD 同步,只切版本 |
| E-6 | go.mod 命中 | 屏幕打印 `⚠ go.mod 无版本号字段(Go 用 git tag),跳过`(Go 模块用 git tag,无版本号字段) |
| E-7 | 描述文件无写权限(只读) | 屏幕打印 `⚠ <文件> 无写权限,跳过`,继续处理其他文件(E-8 边界) |
| E-8 | 描述文件被另一个进程修改(并发) | Edit 可能失败 → 屏幕打印 `⚠ <文件> Edit 失败(<错误>),跳过`,继续处理其他文件 |

## 10. 验收标准(AC 总览)

按 FR 编号归类,合计 ~30 条:

- **FR-1**(9 条):AC-1.1 ~ AC-1.9
- **FR-2**(2 条):AC-2.1 ~ AC-2.2
- **FR-3**(2 条):AC-3.1 ~ AC-3.2
- **FR-4**(5 条):AC-4.1 ~ AC-4.5
- **FR-5**(5 条):AC-5.1 ~ AC-5.5
- **FR-6**(3 条):AC-6.1 ~ AC-6.3
- **NFR-1**(1 条):零依赖
- **NFR-2**(1 条):增量改
- **NFR-3**(1 条):不修改 12 个其他技能
- **NFR-4**(1 条):不修改 `code-skills` 自身
- **NFR-5**(1 条):不修改规范
- **NFR-6**(1 条):不修改看板模板
- **NFR-7**(1 条):性能 < 5 秒
- **NFR-8**(1 条):失败不阻断
- **NFR-9**(1 条):不参与 REQ-00005 扩展

**总计**:约 30 条 AC。

## 11. 关联需求

| 关联需求 | 关联点 | 对本需求的影响 | 来源 |
| --- | --- | --- | --- |
| **REQ-00005**(V0.0.2) | 优化 `code-require` / `code-design` / `code-plan` 3 个技能,增量追加 | NFR-2:本需求沿用"增量追加,不破坏 frontmatter"模式 | `./assistants/V0.0.2/require/REQ-00005/RESULT.md` |
| **REQ-00009**(V0.0.2) | `code-unit` 步骤 0a Glob 检查项目可测性 | NFR-1:本需求沿用 `Glob` 模式,零新增依赖 | `./assistants/V0.0.2/require/REQ-00009/RESULT.md` |
| **REQ-00013**(V0.0.2) | 6 技能启用"编号+标题"显示 | §8.3 沿用 `truncateTitle` 字符数 ≤ 30 约束(本需求**不**直接复用工具函数,仅参考) | `./assistants/V0.0.2/require/REQ-00013/RESULT.md` |
| **REQ-00015**(V0.0.2) | `code-merge` 技能加入 marketplace | NFR-4:本需求**不**修改 `code-skills` 自身,沿用 REQ-00015 严守"marketplace 既有字段不变" | `./assistants/V0.0.2/require/REQ-00015/RESULT.md` |
| **REQ-00017**(V0.0.2) | `code-plan` 不拆"更新看板"任务 | 本轮不拆任务,留作 `code-plan` 决定;沿用 REQ-00017 严守 | `./assistants/V0.0.2/require/REQ-00017/RESULT.md` |

## 12. 待澄清 / 未决项(本轮未处理 / 留作默认)

### Q-3:`code-version` 切换版本时,是否同时修改"项目"和"模块"两类描述文件?
- **状态**:采纳默认(同时改,按需)
- **回退路径**:v2 由 `code-rule` 评估是否拆分为"项目级"和"模块级"两组配置

### Q-4:CWD 项目类型扫描,是否包含单仓库多项目(monorepo)?
- **状态**:采纳默认(不特殊处理 monorepo,沿用 `Glob` 找到的所有匹配描述文件)
- **回退路径**:v2 由 `code-rule` 评估是否需要 `--monorepo` 参数或自动检测

### Q-5:修改描述文件时,版本号取自哪里?
- **状态**:采纳默认(默认 = 新激活的 `<版本号>`)
- **回退路径**:v2 由 `code-version` 接受 `--version-string` 参数覆盖

### Q-6:若 CWD 找不到任何描述文件,如何处理?
- **状态**:采纳默认(屏幕打印 `⚠`,不报错不阻断)
- **回退路径**:v2 由 `code-rule` 评估是否需要 `--strict` 参数

### Q-7:`code-version` 接受 `--skip-cwd-sync` 参数跳过 CWD 同步
- **状态**:采纳默认(本需求**不**实现 `--skip-cwd-sync` 参数,留作 v2 follow-up,沿用既有 `--skip-*` 命名约定)
- **回退路径**:v2 由 `code-version` 接受 `--skip-cwd-sync` 参数

### Q-8(新增):派生任务预警
- **建议派生**:
  - "用 `code-rule` 沉淀 `cwd-sync-conventions.md`(CWD 描述文件同步约定,工程类型 → 描述文件映射表)"
  - "`code-version` 升级:接受 `--cwd=<path>` / `--version-string=<str>` / `--skip-cwd-sync` 等 CLI 参数"
  - "`code-rule` 沉淀'步骤 N 守卫/扩展'统一模式"
- **状态**:本需求不阻塞

## 13. 变更记录

| 时间 | 版本 | 变更摘要 | 变更人 |
| --- | --- | --- | --- |
| 2026-06-06 12:45 | v1 | 初始创建:6 FR / 9 NFR / ~30 AC / 8 个边界场景;2 项已锁定 Q-1(范围:通用技能增强 + 扫描 CWD)+ Q-2(术语:manifest.json 社区主流拼写);5 项采纳默认 Q-3~Q-7;1 项建议派生 Q-8;用户原文 1 处笔误已纠正(`mainfest.json` → `manifest.json`);Q-1 锁定"通用技能增强 + 扫描 CWD 项目类型,**不**修改 `code-skills` 自身";Q-2 锁定"manifest.json(社区主流拼写)";NFR-4 与 NFR-5 严守"零修改"约束;NFR-8 失败不阻断(`code-version` 主职责是"切版本",CWD 同步是辅助能力);本需求**不**拆任务,留作 `code-plan` 决定 | wangmiao |
