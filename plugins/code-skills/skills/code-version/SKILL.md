---
name: code-version
description: 创建或切换开发版本。给一个版本号,本技能就会把后续所有 `code-*` 的产出都收纳到该版本的工作空间里,并打开一张本版本的进度看板;若该版本已存在则直接切换过去。所有其他 `code-*` 技能都必须先调一次本技能才能工作,也支持随时重跑切换到别的版本。
---

# code-version — 版本管理

## 目标
在 `./assistants/` 之上建立**版本工作空间层**,让所有 `code-*` 技能的产出按版本隔离,每个版本都有独立的:
- 目录空间(`./assistants/<版本号>/...`)
- 进度看板(`./assistants/<版本号>/RESULT.md`)

并在 `./assistants/.current-version` 写入当前激活版本,作为其他技能的"上下文切换点"。

## 适用场景
- 启动一个全新版本(如产品发版、独立功能包、季度迭代)
- 在多个并行版本之间切换
- 归档/回看某个历史版本的完整状态
- 任何 `code-require` / `code-design` / `code-plan` / `code-it` / `code-check` 调用前,先确认/切换当前工作空间

## 不适用
- 已有激活版本且用户想继续在该版本工作(直接调用其他 `code-*` 技能即可,无需重跑本技能)
- 项目级规范相关操作(规范在 `./assistants/rules/`,**不**属于任何版本,跨版本共享)

## 工作目录约定(强制)

```
./assistants/
├── rules/                          # 项目级规范(跨版本共享,本技能只读)
├── .current-version                # 当前激活版本标记文件(本技能写)
└── <版本号>/                        # 版本工作空间(本技能产出/切换)
    ├── RESULT.md                   # 版本开发进度看板
    ├── require/<需求编号>/
    ├── design/<需求编号>/
    ├── plan/<需求编号>/
    ├── code/<任务编码>/
    ├── test/<任务编码>/
    └── review/
        ├── <需求编号>/
        └── <任务编码>/
```

- 路径以**当前工作目录(CWD)**为基准
- `rules/` **不**在版本下,跨版本共享
- `.current-version` 是隐藏风格的纯文本标记,内容只有版本号字符串
- 每个版本工作空间内部结构与本技能无关,完全由后续 `code-*` 技能按需填充
- 本技能**不**修改 `./assistants/rules/` 下的任何内容(只读)

## 输入
- **版本号**(必填):用户口头或文本指定
  - 格式不强求,推荐 `vMAJOR.MINOR.PATCH`(如 `v1.0.0`)或日期风格(`2026-Q2`、`2026-06`)
  - **禁止**与现有版本号同名又不指定清理策略(下文会询问)
  - 不允许包含路径分隔符(`/`、`\`)

## 输出
主产出物:
- 切换:`./assistants/.current-version` 被覆写为新版本号
- 新建:`./assistants/<版本号>/` 目录 + `./assistants/<版本号>/RESULT.md` 看板

辅助过程文档:无(看板本身就是核心产出)

## 工具使用约定
- 读目录:`Glob "./assistants/*"`
- 读标记文件:`Read "./assistants/.current-version"`(若存在)
- 写标记文件:`Write "./assistants/.current-version"`
- 建目录:`Bash: mkdir -p`
- 初始化看板:`Write "./assistants/<版本号>/RESULT.md"`(基于 `templates/version-RESULT.md`)
- 与用户澄清:优先 `AskUserQuestion`;自然语言兜底

---

## 工作流程

### 步骤 1 — 收集版本号
1. 若用户未提供,主动询问:
   - 提示用户可输入版本号,或选择"列出已有版本"
2. 用户回复后:
   - 校验:不能为空,不能含 `/` / `\`
   - 格式不强求,但**记录用户实际使用的字符串**作为规范
3. 若用户希望"列出已有版本":
   - `Glob "./assistants/*"` 列出
   - 过滤掉 `rules/` 和 `.current-version`
   - `Read .current-version`(若存在)得知当前激活版本
   - 用 `AskUserQuestion` 给出选项列表,让用户选择切换目标
   - 用户选完后,把选中的版本号作为本技能的目标

### 步骤 2 — 检测版本工作空间
1. 检查 `./assistants/<版本号>/` 是否存在
2. 同时读取 `./assistants/.current-version`(若存在),得知当前激活版本
3. **四种情形**:
   - **A. 目标版本不存在 + 当前也无激活版本** → 首次创建
   - **B. 目标版本不存在 + 当前已有激活版本** → 创建新版本(可能意味着版本切换 + 新建,或当前版本已交付)
   - **C. 目标版本已存在 + 与当前激活版本不同** → 切换
   - **D. 目标版本已存在 + 与当前激活版本相同** → 同版本再确认

### 步骤 3 — 询问/确认操作意图

按情形分支:

#### 情形 A:首次创建
- 直接进入步骤 4A(创建新版本,初始化看板)
- 无需确认

#### 情形 B:从已有版本切到新版本
- 用 `AskUserQuestion` 询问:
  > 检测到当前激活版本为 `<旧版本>`,你提供的是新版本 `<新版本>`。
  > - A. 创建新版本 `<新版本>` 并切换(旧版本保留,可后续切换回去)
  > - B. 我搞错了,旧版本是 `<旧版本>`,目标应是 `<旧版本>`,不切换
  > - C. 取消

#### 情形 C:切换到已有版本
- 用 `AskUserQuestion` 询问:
  > 目标版本 `<版本号>` 已存在。当前激活版本: `<当前>`。
  > - A. 切换到 `<版本号>`(后续 `code-*` 技能操作均落在此版本)
  > - B. 我搞错了,应切换到 `<当前>`(不动)
  > - C. 取消

#### 情形 D:同版本再确认
- 用 `AskUserQuestion` 询问:
  > 目标版本 `<版本号>` 已是当前激活版本。
  > - A. 确认,继续在此版本工作(无需任何改动)
  > - B. 我要重新初始化此版本的看板(会覆盖现有 `RESULT.md`,请提前备份)
  > - C. 取消

### 步骤 4A — 创建新版本工作空间
1. `Bash: mkdir -p "./assistants/<版本号>/"`
2. 检查 `./assistants/<版本号>/RESULT.md`:
   - 不存在 → 基于 `templates/version-RESULT.md` 写入初版
   - 已存在(理论上"新版本"不该有,除非是并发竞争) → 询问用户
3. 在 `RESULT.md` 的"版本信息"区填入:
   - 版本号
   - 创建时间
   - 创建人(待用户填写或暂记 `<unknown>`)
4. 在"变更记录"中追加第一条:
   ```
   YYYY-MM-DD HH:mm  初始化  创建版本 <版本号> 工作空间
   ```

### 步骤 4C — 切换到已有版本
1. **不**触碰该版本目录下任何文件
2. 只更新 `.current-version`

### 步骤 4D — 同版本再确认
- 选 A → 不做任何文件操作
- 选 B → 同步骤 4A 的 2-4 步(用模板覆盖现有 RESULT.md,变更记录首条标注"重新初始化")

### 步骤 5 — 更新当前激活版本标记
- 无论 A/B/C/D 结果如何,只要决定激活此版本,都执行:
  - `Write "./assistants/.current-version"`,内容 = `<版本号>\n`
  - 若已存在 → **覆盖**(因为切换动作就是更新)

### 步骤 6 — 验证与汇报
1. `Read "./assistants/.current-version"` 再次确认内容
2. `Bash: ls "./assistants/<版本号>/"` 列出该版本下当前内容
3. `Read "./assistants/<版本号>/RESULT.md"` 头部确认看板可读
4. 向用户汇报:
   - **当前激活版本**:`<版本号>`
   - **工作空间根目录**:`./assistants/<版本号>/`
   - **看板位置**:`./assistants/<版本号>/RESULT.md`
   - **该版本下当前已有内容**:列出
   - **下一步建议**:
     - 创建首个需求 → 调 `code-require`
     - 已有需求 → 调 `code-design` / `code-plan` / 等

---

## 步骤 7 — CWD 描述文件版本号同步(REQ-00018 新增)

> 本小节在"步骤 6 验证与汇报"完成后追加,扫描 CWD 下的已知工程类型描述文件,同步版本号到新激活的 `<版本号>`。
> 本步骤是辅助能力,失败不阻断 `code-version` 主流程(NFR-8 强约束)。

### 7.1 目标

- 在 CWD(`process.cwd()`)下扫描 6 类已知工程类型描述文件(`package.json` / `pom.xml` / `manifest.json` / `Cargo.toml` / `pyproject.toml` / `go.mod`)
- 解析每个命中文件的"版本号"字段
- Edit 替换为新激活的 `<版本号>`(默认 = 步骤 1 收集的版本号;FR-2 锁定)
- 屏幕输出 5 类契约之一(`✓` 成功 / `⚠` 0 命中 / `⚠` 解析失败 / `⚠` 缺版本号字段 / `⚠` go.mod)
- 失败不阻断,退出码仍 0(NFR-8 强约束)

### 7.2 触发条件

- 步骤 3 决定激活此版本后(情形 A / B / C / D 任意一种,选 A / B / C 触发,选 C 取消时**不**触发)
- 步骤 1-6 完整执行成功
- **(v2 follow-up)** 用户可显式传 `--skip-cwd-sync` 跳过本步骤(本需求**不**实现,Q-7 采纳默认)

### 7.3 算法

```ts
// 7 步伪代码(沿用概要设计 D-3:Read + Edit + 行匹配,0 新增依赖)
function step7_syncCwdVersionFiles(newVersion: string, cwd: string): void {
  // 步骤 7.1:解析 argv(本需求 0 CLI 参数,Q-7)
  // (留作 v2 follow-up:`--skip-cwd-sync` / `--cwd` / `--version-string`)

  // 步骤 7.2:Glob 6 类描述文件(优先级固定)
  const descriptorFiles = [
    'package.json',     // 1) Node.js / VSCode Extension / npm
    'pom.xml',          // 2) Maven Java
    'manifest.json',    // 3) Web App / PWA
    'Cargo.toml',       // 4) Rust
    'pyproject.toml',   // 5) Python
    'go.mod',           // 6) Go(无版本号字段,仅跳过)
  ]
  const matched: string[] = descriptorFiles
    .map(f => `${cwd}/${f}`)
    .filter(p => fileExists(p))

  // 步骤 7.3:0 命中处理
  if (matched.length === 0) {
    console.log('⚠ CWD 下未检测到任何已知工程类型描述文件,跳过同步')
    return  // 不阻断
  }

  // 步骤 7.4:对每个命中文件处理
  for (const filePath of matched) {
    const filename = basename(filePath)
    try {
      // 7.4.1:go.mod 特殊处理(Go 用 git tag)
      if (filename === 'go.mod') {
        console.log(`⚠ ${filename} 无版本号字段(Go 用 git tag),跳过`)
        continue
      }

      // 7.4.2:Read 内容
      const content = readFile(filePath)

      // 7.4.3:解析版本号(根据文件类型)
      const oldVersion = parseVersionField(filename, content)

      // 7.4.4:缺版本号字段
      if (oldVersion === null) {
        console.log(`⚠ ${filename} 未找到版本号字段,跳过`)
        continue
      }

      // 7.4.5:Edit 替换版本号
      const newContent = replaceVersionField(filename, content, newVersion)

      // 7.4.6:写回文件
      writeFile(filePath, newContent)

      // 7.4.7:屏幕输出成功
      console.log(`✓ CWD 描述文件同步:${filename}: ${oldVersion} → ${newVersion}`)
    } catch (err) {
      // 7.4.8:失败不阻断
      console.log(`⚠ ${filename} 格式不可解析,跳过`)
      continue
    }
  }
}

// 解析版本号字段(每类文件独立正则)
function parseVersionField(filename: string, content: string): string | null {
  switch (filename) {
    case 'package.json':
    case 'manifest.json':
      // JSON: "version": "x.y.z"
      const m1 = content.match(/"version"\s*:\s*"([^"]+)"/)
      return m1 ? m1[1] : null

    case 'pom.xml':
      // XML: <version>x.y.z</version>
      const m2 = content.match(/<version>([^<]+)<\/version>/)
      return m2 ? m2[1] : null

    case 'Cargo.toml':
    case 'pyproject.toml':
      // TOML: version = "x.y.z"
      const m3 = content.match(/^version\s*=\s*"([^"]+)"/m)
      return m3 ? m3[1] : null

    default:
      return null
  }
}

// Edit 替换版本号
function replaceVersionField(filename: string, content: string, newVersion: string): string {
  switch (filename) {
    case 'package.json':
    case 'manifest.json':
      return content.replace(/"version"\s*:\s*"[^"]+"/, `"version": "${newVersion}"`)

    case 'pom.xml':
      return content.replace(/<version>[^<]+<\/version>/, `<version>${newVersion}</version>`)

    case 'Cargo.toml':
    case 'pyproject.toml':
      return content.replace(/^version\s*=\s*"[^"]+"/m, `version = "${newVersion}"`)

    default:
      return content
  }
}
```

### 7.4 通过条件

- 成功:屏幕输出 1+ 行 `✓` 日志(每行一个文件)
- 0 命中:屏幕输出 1 行 `⚠` 日志
- 解析失败 / 缺版本号字段 / `go.mod` 命中 / 无写权限 / Edit 失败:屏幕输出对应 `⚠` 日志
- **失败不阻断**(NFR-8 强约束):退出码仍 0

### 7.5 屏幕输出契约(5 类)

| 场景 | 输出格式 |
| --- | --- |
| 成功 | `✓ CWD 描述文件同步:<filename>: <旧版本号> → <新版本号>` |
| 0 命中 | `⚠ CWD 下未检测到任何已知工程类型描述文件,跳过同步` |
| 解析失败 | `⚠ <filename> 格式不可解析,跳过` |
| 缺版本号字段 | `⚠ <filename> 未找到版本号字段,跳过` |
| `go.mod` 命中 | `⚠ go.mod 无版本号字段(Go 用 git tag),跳过` |

### 7.6 边界与异常(E-1 ~ E-8)

| ID | 场景 | 处理 |
| --- | --- | --- |
| **E-1** | CWD 下有多个描述文件(monorepo) | 修改**所有**匹配的描述文件,屏幕打印每行 |
| **E-2** | CWD 下找不到任何描述文件 | 屏幕打印 `⚠ CWD 下未检测到任何已知工程类型描述文件,跳过同步`,不报错 |
| **E-3** | 描述文件存在但格式不可解析(非 JSON / 非标准 XML / 非标准 TOML) | 屏幕打印 `⚠ <filename> 格式不可解析,跳过`,继续处理其他文件 |
| **E-4** | 描述文件存在但**无**"版本号"字段(如 `package.json` 缺 `"version"`) | 屏幕打印 `⚠ <filename> 未找到版本号字段,跳过`,继续处理其他文件 |
| **E-5** | `--skip-cwd-sync` CLI 参数 | (本需求**不**实现,Q-7 采纳默认,留作 v2 follow-up) |
| **E-6** | `go.mod` 命中(Go 用 git tag) | 屏幕打印 `⚠ go.mod 无版本号字段(Go 用 git tag),跳过` |
| **E-7** | 描述文件无写权限(只读) | 屏幕打印 `⚠ <filename> 无写权限,跳过`,继续处理其他文件 |
| **E-8** | 描述文件被另一个进程修改(并发) | Edit 可能失败 → 屏幕打印 `⚠ <filename> Edit 失败(<错误>),跳过`,继续处理其他文件 |

### 7.7 性能(NFR-7)

- 单文件 ~1 秒(`Read` + `Edit` + `Write` 三步,网络/磁盘 IO 0)
- monorepo 5 个文件 ~3 秒
- monorepo 10 个文件 ~5 秒(NFR-7 上限)
- > 20 个文件:退化,屏幕打印 `⚠ 同步耗时较长` 但不阻断

---

## 看板字段约定(version-RESULT.md)

`./assistants/<版本号>/RESULT.md` 是**整个版本开发周期的总览**。
所有 `code-*` 技能在工作推进时,都会**同步更新**对应区段,保持单一事实来源。

完整结构见 `templates/version-RESULT.md`,核心区段:

| 区段 | 主要写入方 | 用途 |
| --- | --- | --- |
| 版本信息 | `code-version`(首次) | 版本号、创建/最近更新时间、负责人、状态 |
| 需求清单 | `code-require` | 本版本所有需求的状态(待开始/进行中/已完成/已取消) |
| 概要设计清单 | `code-design` | 本版本所有概要设计的状态 |
| 详细设计与任务计划汇总 | `code-plan` | 本版本所有详细设计+计划的状态,及对应的任务总数 |
| 任务清单 | `code-plan` 首次登记,`code-it` 持续更新(含步骤 8.5 自含按需写单测) | 每条任务的开发状态 + 测试状态(双轴) |
| 缺陷清单 | `code-check` 派生 / `code-it` 直接报告 | 缺陷编号、严重度、状态、关联任务 |
| 评审发现汇总 | `code-check` | 评审发现(分级别)及其处理状态 |
| 派生任务记录 | `code-check` 派生改修任务时 | "审查改修"任务记录(任务编号、关联原任务、来源) |
| 里程碑 | `code-plan` 设立,各技能推进 | 本版本的关键里程碑及完成定义 |
| 变更记录 | 所有技能 | 时间、变更类型、变更摘要、变更人 |

**重要约束**:
- 其他 `code-*` 技能只能**追加/更新自己负责的区段**,**不重写**整个看板
- 若发现看板的字段约定不足,先在"变更记录"追加"看板字段扩展"条目,再改

---

## 衔接

- **下游**:所有 `code-*` 技能在执行前都应读取 `./assistants/.current-version` 确认工作空间
- **上游**:无,通常由用户直接发起(每次进入项目或需要切换版本时)
- **横向**:`./assistants/rules/` 跨所有版本共享

## 不要做的事
- 不要在 `./assistants/rules/` 下创建版本子目录(规范是跨版本共享的)
- 不要在版本号中使用 `/` `\` 空格
- 不要在用户没确认的情况下覆盖现有 `RESULT.md`
- 不要在切版本时删除其他版本的目录(版本归档是独立操作)
- 不要在本技能中处理具体的需求/设计/任务(那是其他 `code-*` 的工作)
