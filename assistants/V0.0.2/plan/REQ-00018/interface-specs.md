# 接口详细规格 — REQ-00018
更新时间:2026-06-06 13:15
版本:V0.0.2
需求编码:REQ-00018

## 总览:本需求 0 新增接口

| 维度 | 数量 |
| --- | --- |
| 新增 REST 端点 | 0 |
| 新增 gRPC 方法 | 0 |
| 新增 CLI 参数 | 0(Q-7 采纳默认) |
| 新增函数导出 | 0 |
| 新增事件 | 0 |

## 既有接口(本需求不修改)

`code-version` 既有 0 个对外接口(无 REST / 无 gRPC / 无 SDK 导出)。本需求是优化技能行为,不改既有接口契约。

## 内部函数契约(7 步算法实现)

### 函数 1:`step7_syncCwdVersionFiles(newVersion, cwd)`

- **形式**:内部函数(伪代码,本需求不强制实现,仅供 `code-it` 实施参考)
- **入参**:
  - `newVersion: string` — 新激活的版本号
  - `cwd: string` — 当前工作目录(默认 = `process.cwd()`)
- **出参**:无(副作用 = 屏幕输出 + 写文件)
- **错误处理**:无抛出,所有错误走 `⚠` 屏幕输出
- **依据规范**:NFR-8 失败不阻断

### 函数 2:`parseVersionField(filename, content)`

- **形式**:内部函数
- **入参**:
  - `filename: string` — 文件名(用于区分解析策略)
  - `content: string` — 文件内容
- **出参**:`string | null` — 版本号字符串,或 null(未找到)
- **错误处理**:无抛出(无 try-catch),返回 null 即代表"未找到"
- **6 类解析策略**:
  - `package.json` / `manifest.json`:正则 `"version"\s*:\s*"([^"]+)"`(JSON 字段)
  - `pom.xml`:正则 `<version>([^<]+)<\/version>`(XML 字段)
  - `Cargo.toml` / `pyproject.toml`:正则 `^version\s*=\s*"([^"]+)"` 多行模式(TOML 字段)
  - `go.mod`:N/A,直接走 `⚠` 跳过(Go 用 git tag)

### 函数 3:`replaceVersionField(filename, content, newVersion)`

- **形式**:内部函数
- **入参**:
  - `filename: string` — 文件名
  - `content: string` — 文件内容
  - `newVersion: string` — 新版本号
- **出参**:`string` — 替换后的文件内容
- **错误处理**:无抛出
- **6 类替换策略**:
  - `package.json` / `manifest.json`:字符串替换 `"version"\s*:\s*"[^"]+"`
  - `pom.xml`:字符串替换 `<version>[^<]+<\/version>`
  - `Cargo.toml` / `pyproject.toml`:多行模式替换 `^version\s*=\s*"[^"]+"`
  - `go.mod`:N/A(不进入本函数)

## 屏幕输出契约(5 类)

| ID | 触发条件 | 输出格式 |
| --- | --- | --- |
| 成功 | Edit 成功 | `✓ CWD 描述文件同步:<filename>: <旧版本号> → <新版本号>` |
| 0 命中 | Glob 0 命中 | `⚠ CWD 下未检测到任何已知工程类型描述文件,跳过同步` |
| 解析失败 | 格式不可解析 | `⚠ <filename> 格式不可解析,跳过` |
| 缺版本号 | `parseVersionField` 返回 null | `⚠ <filename> 未找到版本号字段,跳过` |
| go.mod 命中 | Go 模块 | `⚠ go.mod 无版本号字段(Go 用 git tag),跳过` |

## 错误码

本需求 0 引入错误码(无对外 API,无 CLI 错误码)。

## 版本策略

- `code-version` 既有版本策略:`vMAJOR.MINOR.PATCH`(无强制约束)
- 本需求同步规则:新激活的 `<版本号>` 作为"新版本号",**直接**写入描述文件(不做版本号规范化,如 `V0.0.3` 直接写,不做 `0.0.3` 转换)

## 兼容策略

- **向后兼容**:本需求**不**修改既有"步骤 1~6"流程,既有调用方无感知
- **向前兼容**:本需求**不**引入新 CLI 参数,既有调用方无需适配
- **错误兼容**:本需求**不**改变退出码(NFR-8 失败不阻断,退出码仍 0)
