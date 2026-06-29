# Node.js/TypeScript 项目参考 — code-design

> 本文件为 code-design 技能提供 Node.js/TypeScript 项目的语言差异说明。
> 在步骤 5(探索项目结构)中,当检测到项目语言为 nodejs 时加载本文件。

## §1 项目结构识别

### 描述文件特征
- `package.json`:Node.js 项目根描述文件,必含 `name` 和 `version` 字段
- `tsconfig.json`:TypeScript 配置(可选,存在则判定为 TypeScript 项目)
- `node_modules/`:依赖目录,通常被 `.gitignore`

### 目录约定
- 源码目录:常见 `src/`、`lib/`、`app/`
- 测试目录:常见 `test/`、`tests/`、`__tests__/`
- 构建输出:常见 `dist/`、`build/`、`out/`

### 包管理器识别
- `package-lock.json` → npm
- `yarn.lock` → yarn
- `pnpm-lock.yaml` → pnpm

## §2 构建命令检测

### 构建命令
- 优先:读取 `package.json` > `scripts.build`
- 退化:TypeScript 项目 → `npx tsc`;无 TypeScript → 跳过编译

### 常见构建模式
- `tsc` / `tsc -p tsconfig.json`(TypeScript)
- `webpack` / `vite build` / `esbuild`(打包工具)
- `next build` / `nuxt build`(框架)

## §3 测试框架识别

### 框架检测
- 读取 `package.json` > `scripts.test`
- 读取 `package.json` > `devDependencies` 或 `dependencies`
- 常见框架:`jest` / `vitest` / `mocha` / `jasmine` / `ava`

## §4 启动/运行命令检测

- 读取 `package.json` > `scripts.start` 或 `scripts.dev`
- 退化:`node <入口文件>`(从 `package.json` > `main` 推断)

## §5 Monorepo 声明文件解析

### 声明文件
- `pnpm-workspace.yaml`:读取 `packages` 字段
- `package.json` > `workspaces`:读取 `packages` 数组
- `lerna.json`:读取 `packages` 字段
- `nx.json` / `turbo.json`:读取 workspace 配置

## §6 编码约定

### 命名约定
- 文件名:kebab-case 或 camelCase
- 类名:PascalCase
- 函数/变量:camelCase
- 常量:UPPER_SNAKE_CASE

### 错误处理风格
- try/catch + async/await
- 自定义错误类(继承 Error)
- Express 风格中间件错误处理

## §7 工具链检测

### 代码行数统计
- 优先:`tokei`(Rust 实现,性能好)
- 退化:`cloc`(Perl 实现)
- 兜底:heuristic(按行计数)

### Lint/格式化
- ESLint(`.eslintrc.*` / `eslint.config.*`)
- Prettier(`.prettierrc.*`)