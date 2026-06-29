# Rust 项目参考 — code-design

> 本文件为 code-design 技能提供 Rust 项目的语言差异说明。
> 在步骤 5(探索项目结构)中,当检测到项目语言为 rust 时加载本文件。

## §1 项目结构识别
- 描述文件:`Cargo.toml`(必须)
- 源码目录:`src/`(约定),`main.rs`(入口)或`lib.rs`(库)
- 测试目录:`tests/`(集成测试),`src/` 内 `#[cfg(test)]` 模块(单元测试)

## §2 构建命令检测
- 构建:`cargo build` / `cargo build --release`

## §3 测试框架识别
- 内置:`cargo test`(Rust 内置测试框架)
- 常见扩展:`proptest` / `rstest`

## §4 启动/运行命令检测
- 运行:`cargo run`

## §5 Monorepo 声明文件解析
- `Cargo.toml` > `[workspace]` > `members` 字段

## §6 编码约定
- 文件名:snake_case
- 类型/特征:PascalCase(CamelCase)
- 函数/变量:snake_case
- 常量:UPPER_SNAKE_CASE
- 错误处理:Result<T, E> + ? 运算符

## §7 工具链检测
- 代码行数统计:`tokei`(Rust 原生,优先)
- Lint:`cargo clippy`
- 格式化:`cargo fmt`