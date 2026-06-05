# 接口详细规格 — REQ-00012
更新时间:2026-06-05
版本:V0.0.2

**本需求无 API / 函数 / RPC / 事件接口**。所有"接口"均为 Markdown 内部相对链接。

## 接口:根 README → 详细 README

- **形式**:Markdown 相对链接
- **来源**:`./README.md`(中文)+ `./README.en.md`(英文)
- **目标**:`./plugins/code-skills/README.md`
- **形式**:`[📖 详细文档](./plugins/code-skills/README.md)`(中文版)/ `[📖 Detailed Documentation](./plugins/code-skills/README.md)`(英文版)
- **示例**:
  ```markdown
  ## 📖 详细文档
  完整技能说明、安装细节、版本管理:[./plugins/code-skills/README.md](./plugins/code-skills/README.md)
  ```
- **错误处理**:无(若 `plugins/code-skills/README.md` 不存在,GitHub 渲染会显示 404 — 已在 `plugins/code-skills/README.md` 存在的 38,247 bytes 上验证)
- **版本策略**:N/A(无版本号)
- **兼容策略**:N/A(项目内相对链接)
- **依据规范**:`doc-conventions §规则 2`(详细文档链)

## 接口:`git mv` 命令

- **形式**:Bash 命令
- **路径**:`git mv <old> <new>`
- **入参**:
  - `<old>` = `plugins/code-skills/CLAUDE.md`
  - `<new>` = `CLAUDE.md`
- **出参**:git status 显示 `renamed: plugins/code-skills/CLAUDE.md -> CLAUDE.md`
- **错误码**:
  - 退出码 0:成功
  - 退出码 128(源不存在) / 退出码 ≠ 0(权限等):失败
- **示例**:
  ```bash
  git mv plugins/code-skills/CLAUDE.md CLAUDE.md
  ```
- **依据规范**:NFR-3(git mv 保留 blame)
