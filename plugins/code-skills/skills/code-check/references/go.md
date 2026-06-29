# Go 项目参考 — code-design

> 本文件为 code-design 技能提供 Go 项目的语言差异说明。
> 在步骤 5(探索项目结构)中,当检测到项目语言为 go 时加载本文件。

## §1 项目结构识别
- 描述文件:`go.mod`(必须)
- 源码目录:项目根或 `cmd/` / `internal/` / `pkg/`(约定)
- 测试文件:`*_test.go`(与源文件同目录)

## §2 构建命令检测
- 构建:`go build ./...` 或 `go build -o <output> <package>`

## §3 测试框架识别
- 内置:`go test ./...`(Go 内置 testing 包)
- 常见扩展:`testify` / `ginkgo`

## §4 启动/运行命令检测
- 运行:`go run .` 或 `go run <main-package>`

## §5 Monorepo 声明文件解析
- Go 生态中 monorepo 通过 `go.mod` module 路径 + 子目录组织,无独立声明文件

## §6 编码约定
- 文件名:snake_case 或 lowercase
- 类型/接口:PascalCase(导出)/camelCase(非导出)
- 函数/变量:camelCase
- 错误处理:显式 `if err != nil` 模式

## §7 工具链检测
- 代码行数统计:`tokei` / `cloc`
- Lint:`golangci-lint`
- 格式化:`go fmt` / `gofmt`