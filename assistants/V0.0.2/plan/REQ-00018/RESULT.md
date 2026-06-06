# 详细设计 — REQ-00018(优化 `/code-version` 技能 — 切换版本时同步 CWD 项目描述文件版本号)

- 需求编码:REQ-00018
- 所属版本:V0.0.2
- 文档版本:v1
- 状态:已锁定
- 责任人:wangmiao
- 创建:2026-06-06
- 最近更新:2026-06-06 13:15
- 当前版本:v1
- **主题**(来自用户输入):
  > 优化 `/code-version` 技能,要求切换到新版本时,要修改当前项目和模块相关描述文件(如 pom.xml、package.json、manifest.json 等,项目工程类型或模块工程类型不同修改对应的描述文件)中的各版本号的声明同步
- 上游:
  - 需求:`./assistants/V0.0.2/require/REQ-00018/RESULT.md`(v1)
  - 概要设计:`./assistants/V0.0.2/design/REQ-00018/RESULT.md`(v1)
- 遵循规范:`./assistants/rules/` 下 13 个文件

## 设计目标

- 整体设计目标:`--balanced`(沿用 design)
- 维度优先级:
  - 功能性:**高**
  - 扩展性:**—**
  - 健壮性:**高**
  - 可维护性:**—**

## 1. 概述

### 1.1 目标

把概要设计"步骤 7 — CWD 描述文件版本号同步"落地为:
1. **详细设计**:给出可直接编码的 7 步算法伪代码 + 6 类描述文件解析契约 + 5 类屏幕输出
2. **编码计划**:拆分为 **2 个任务**(1 SKILL.md 增量追加 + 1 INV 自检收尾),严守 REQ-00017"1 任务 = 1 实际产出"约束

### 1.2 范围

- 涉及文件:1 个修改 + 0 新增 — `plugins/code-skills/skills/code-version/SKILL.md`
- 不修改:其他 12 个 `code-*` SKILL.md / `marketplace.json` / `plugin.json` / README / CLAUDE.md / 13 份规范 / 看板模板
- 不引入:0 新增依赖 / 0 新增文件 / 0 新增 CLI 参数

### 1.3 与概要设计的关系

100% 沿用概要设计 5 决策 + 8 边界 + 5 屏幕输出契约 + 13 规范 0 冲突。本详细设计聚焦"7 步算法伪代码 + 6 类描述文件解析细节 + 任务拆分依据"。

## 2. 上游引用

- 需求:6 FR / 9 NFR / ~30 AC
- 概要设计:5 决策 D-1~D-5 / 8 边界 E-1~E-8
- 关键交叉点:详 `materials-index.md §关键交叉点`

## 3. 模块详细化

### 3.1 唯一修改的模块:`plugins/code-skills/skills/code-version/SKILL.md`

| 属性 | 值 |
| --- | --- |
| 路径 | `plugins/code-skills/skills/code-version/SKILL.md` |
| 状态 | 修改既有 |
| 锚点(语义化) | `plugins/code-skills/skills/code-version/SKILL.md` §工作流程 段后 / §看板字段约定 段前 |
| 关键变更 | 插入"## 步骤 7 — CWD 描述文件版本号同步(REQ-00018 新增)"小节,含 7 子节 |
| 状态归属 | 既有 `code-version` 技能 |
| 依赖 | 既有 0 对内依赖 |
| 符合规范 | skill-conventions §规则 1(frontmatter 字节级保留)/ module-conventions §规则 1(不新增资源文件) |

### 3.2 步骤 7 子小节结构(7 子节)

```
## 步骤 7 — CWD 描述文件版本号同步(REQ-00018 新增)

### 7.1 目标
- 在 code-version 步骤 6 之后,扫描 CWD 下的已知工程类型描述文件,同步版本号到新激活的 <版本号>
- CWD = process.cwd()(FR-3 锁定)
- <新版本号> 默认 = 新激活的 <版本号>(FR-2 锁定)

### 7.2 触发条件
- 步骤 3 决定激活此版本后(情形 A/B/C/D 任意一种,选 A/B/C 触发,选 C 取消时不触发)
- 步骤 1-6 完整执行成功

### 7.3 算法
[7 步伪代码,见 §4]

### 7.4 通过条件
- 成功:屏幕输出 1+ 行 ✓ 日志(每行一个文件)
- 0 命中:屏幕输出 1 行 ⚠ 日志
- 解析失败 / 缺版本号字段 / go.mod:屏幕输出对应 ⚠ 日志
- 失败不阻断(NFR-8):退出码仍 0

### 7.5 屏幕输出契约(5 类)
[见 §6 屏幕输出契约]

### 7.6 边界与异常(E-1 ~ E-8)
[见 §8 边界与异常]

### 7.7 性能(NFR-7)
- 单文件 ~1 秒
- 5 个文件 ~3 秒
- 10 个文件 ~5 秒(NFR-7 上限)
```

## 4. 算法与逻辑(7 步伪代码)

```ts
// 步骤 7 算法伪代码(沿用概要设计 D-3 解析模式:Read + Edit + 行匹配)
function step7_syncCwdVersionFiles(newVersion: string, cwd: string): void {
  // 步骤 7.1:解析 argv
  // (本需求不实现 --skip-cwd-sync,Q-7 采纳默认)
  // (本需求不实现 --cwd 参数,FR-3 锁定默认 = process.cwd())

  // 步骤 7.2:Glob 6 类描述文件
  const descriptorFiles = [
    'package.json',
    'pom.xml',
    'manifest.json',
    'Cargo.toml',
    'pyproject.toml',
    'go.mod',
  ]
  const matched: string[] = []
  for (const f of descriptorFiles) {
    const path = `${cwd}/${f}`
    if (fileExists(path)) matched.push(path)
  }

  // 步骤 7.3:0 命中处理
  if (matched.length === 0) {
    console.log('⚠ CWD 下未检测到任何已知工程类型描述文件,跳过同步')
    return  // 不阻断
  }

  // 步骤 7.4:对每个命中文件处理
  for (const filePath of matched) {
    try {
      const filename = path.basename(filePath)
      const content = readFile(filePath)

      // 7.4.1:go.mod 特殊处理(Go 用 git tag)
      if (filename === 'go.mod') {
        console.log(`⚠ ${filename} 无版本号字段(Go 用 git tag),跳过`)
        continue
      }

      // 7.4.2:解析版本号(根据文件类型)
      const oldVersion = parseVersionField(filename, content)

      // 7.4.3:缺版本号字段
      if (oldVersion === null) {
        console.log(`⚠ ${filename} 未找到版本号字段,跳过`)
        continue
      }

      // 7.4.4:Edit 替换版本号
      const newContent = replaceVersionField(filename, content, newVersion)

      // 7.4.5:写回文件
      writeFile(filePath, newContent)

      // 7.4.6:屏幕输出成功
      console.log(`✓ CWD 描述文件同步:${filename}: ${oldVersion} → ${newVersion}`)
    } catch (err) {
      // 7.4.7:失败不阻断
      console.log(`⚠ ${path.basename(filePath)} 格式不可解析,跳过`)
      continue
    }
  }
}

// 解析版本号字段(每类文件独立)
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

## 5. 数据结构完整变更

**本需求不引入新数据结构**。

| 既有数据 | 用途 | 状态 |
| --- | --- | --- |
| `<版本号>` | 步骤 1 收集的版本号 | 既有,本需求沿用 |
| `.current-version` | 步骤 5 写入 | 既有,本需求**不**修改 |
| `<版本号>/RESULT.md` | 版本看板 | 既有,本需求**不**扩展字段(NFR-6 严守) |

## 6. 接口细节

**本需求不引入新接口**(沿用 `code-version` 既有 0 个对外接口)。

| 维度 | 状态 |
| --- | --- |
| 新增 REST 端点 | **0** |
| 新增 gRPC 方法 | **0** |
| 新增 CLI 参数 | **0**(Q-7 采纳默认,`--skip-cwd-sync` 留作 v2) |
| 新增函数导出 | **0** |
| 新增事件 | **0** |

## 7. 异常处理(8 边界)

| ID | 触发条件 | 屏幕输出 | 阻断? |
| --- | --- | --- | --- |
| **E-1** | monorepo 多个匹配 | 每行 `✓` | 否 |
| **E-2** | 0 命中 | `⚠ CWD 下未检测到...` | 否 |
| **E-3** | 格式不可解析(非 JSON/XML/TOML) | `⚠ <filename> 格式不可解析` | 否 |
| **E-4** | 缺版本号字段 | `⚠ <filename> 未找到版本号字段` | 否 |
| **E-5** | `--skip-cwd-sync` | (本需求不实现,Q-7) | (留作 v2) |
| **E-6** | `go.mod` 命中 | `⚠ go.mod 无版本号字段` | 否 |
| **E-7** | 描述文件无写权限 | `⚠ <filename> 无写权限,跳过` | 否 |
| **E-8** | 并发修改导致 Edit 失败 | `⚠ <filename> Edit 失败(<错误>)` | 否 |

**总览**:**0 阻断 + 0 异常退出**。所有边界走 `⚠` 屏幕输出 + 继续流程。

## 8. 安全要求

- ✅ **无新输入校验需求**:本需求只读 CWD 已知描述文件,无外部输入
- ✅ **无新鉴权需求**:本需求是本地文件操作,无需鉴权
- ✅ **无新审计日志需求**:本需求是辅助能力,无需审计
- ✅ **无新敏感数据处理**:本需求处理版本号字符串(非敏感)

## 9. 状态机 / 流程

```
[code-version 步骤 1-6 完成]
  ↓
[步骤 3 激活此版本:情形 A/B/C 触发,情形 C 取消跳过]
  ↓
[步骤 7 触发]
  ↓
[7.1 解析 argv(本需求 0 CLI 参数)]
  ↓
[7.2 Glob 6 类描述文件]
  ↓
[7.3 0 命中?]
  ├─ yes → 屏幕输出 ⚠ → 退出 0
  └─ no → [7.4 对每命中文件]
           ├─ go.mod → 屏幕输出 ⚠ → 继续
           ├─ 解析失败 → 屏幕输出 ⚠ → 继续
           ├─ 缺版本号 → 屏幕输出 ⚠ → 继续
           ├─ 成功 → Edit + 屏幕输出 ✓ → 继续
           └─ Edit 失败 → 屏幕输出 ⚠ → 继续
  ↓
[退出 0](NFR-8 失败不阻断)
```

## 10. 性能与资源(NFR-7)

| 场景 | 文件数 | 估算耗时 |
| --- | --- | --- |
| 空 CWD | 0 | < 0.5 秒(纯 Glob) |
| 单描述文件 | 1 | < 1 秒 |
| monorepo 中等 | 5 | < 3 秒 |
| monorepo 大型 | 10 | < 5 秒(NFR-7 上限) |

**无资源限制**:
- 内存:< 10 MB(只读 1 个文件,内存占用可忽略)
- CPU:< 1 %(纯文本匹配)
- 网络:0
- 磁盘 IO:每文件 1 次 Read + 1 次 Write(共 2 IOPS)

## 11. 测试要点

> 仓库**无**测试框架(CLAUDE.md 严守),验证靠**静态 Read + 人工场景验证**。

| 场景 | 验证方法 | 通过标准 |
| --- | --- | --- |
| **S-1** Maven Java 项目 | 临时目录创建 `pom.xml` + `<version>0.0.1</version>`,调 `code-version V0.0.3` | 屏幕输出 1 行 `✓`,`pom.xml` `<version>` → `V0.0.3` |
| **S-2** Node.js 项目 | 临时目录创建 `package.json` + `"version": "1.0.0"`,调 `code-version V0.0.3` | 屏幕输出 1 行 `✓`,`package.json` `version` → `V0.0.3` |
| **S-3** monorepo | 临时目录创建 `package.json` 根 + `packages/*/package.json` | 每文件 1 行 `✓` |
| **S-4** 0 命中 | 临时目录(空),调 `code-version V0.0.3` | 屏幕输出 1 行 `⚠ CWD 下未检测到...`,退出 0 |
| **S-5** `code-skills` 仓库根 | CWD = `code-skills/`,调 `code-version V0.0.3` | 同 S-4,0 命中(无 `package.json` / `pom.xml` 等) |
| **S-6** 格式不可解析 | 临时目录创建非法 `package.json`,调 `code-version V0.0.3` | 屏幕输出 1 行 `⚠ package.json 格式不可解析...`,退出 0 |
| **S-7** 缺版本号字段 | 临时目录创建 `package.json` 无 `version`,调 `code-version V0.0.3` | 屏幕输出 1 行 `⚠ package.json 未找到版本号字段...`,退出 0 |
| **S-8** `go.mod` | 临时目录创建 `go.mod`,调 `code-version V0.0.3` | 屏幕输出 1 行 `⚠ go.mod 无版本号字段...`,退出 0 |
| **失败不阻断** | S-6 场景同时验证 | `.current-version = V0.0.3` 仍被写入,退出 0 |
| **frontmatter 保留** | 调 `code-version V0.0.3` 后 `Read` SKILL.md L1-3 | L1-3 字节级与本需求前一致 |
| **既有步骤 1~6 不变** | 调 `code-version V0.0.3` 后 `Read` SKILL.md "## 工作流程" 小节 | 与本需求前一致 |
| **NFR-1 零依赖** | `grep -E "(import|require).*new" SKILL.md` | 0 命中新依赖 |

## 12. 规范遵循

| 规范文件 | 自检 | 备注 |
| --- | --- | --- |
| skill-conventions §规则 1 | ✅ | frontmatter L1-3 字节级保留(NFR-2 严守) |
| module-conventions §规则 1 | ✅ | 不新增资源文件,锚点对齐"## 工作流程" 段后 |
| dependency-conventions | ✅ | 0 新增依赖(NFR-1 严守) |
| dashboard-conventions §规则 1 | ✅ | 不扩展看板字段,0 触发 3 处同步 |
| encoding-conventions | ✅ | 任务编号 `TASK-REQ-00018-00001~00002` 严格 5+5 位 |
| commit-conventions | ✅ | 由 `code-it` / `code-auto` 末步兜底 |
| doc-conventions | ✅ | SKILL.md 行数变化在 ±20% 范围(详 T-001 deviations) |
| marketplace-protocol | ✅ | 不修改 `marketplace.json` / `plugin.json`(NFR-4 严守) |
| naming-conventions | ✅ | 函数名 `parseVersionField` / `replaceVersionField` kebab-case |
| coding-style | ✅ | 沿用现有 SKILL.md 风格(伪代码 + 屏幕输出契约) |
| framework-conventions | ✅ | 不涉及 |
| migration-mapping | ✅ | 不涉及跨版本 |
| directory-conventions | ✅ | 不新增子目录 |

**总览**:**13 份规范全部严守,0 冲突 / 0 偏离 / 0 授权**。

## 13. 待澄清 / 未决项

| 编号 | 内容 | 状态 |
| --- | --- | --- |
| (无) | 本设计**不**提出新澄清,所有 5 项决策 + 8 项边界 + 6 类描述文件锚点均**已锁定** | 0 待澄清 |

## 14. 变更记录

| 时间 | 版本 | 变更摘要 | 变更人 |
| --- | --- | --- | --- |
| 2026-06-06 13:15 | v1 | 初始创建:7 步算法伪代码 + 6 类描述文件解析契约 + 8 边界 + 5 类屏幕输出;**2 个任务** — T-001 SKILL.md 增量追加 + T-002 INV 自检收尾;沿用概要设计 5 决策;13 份规范 0 冲突 0 偏离;0 触发 `dashboard-conventions §规则 1` 3 处同步;0 派生"更新看板"任务 REQ-00017 严守;任务测试状态 = `不适用`(纯文档,仓库无测试框架) | wangmiao |
