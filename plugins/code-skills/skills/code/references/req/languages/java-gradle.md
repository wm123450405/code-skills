# Java(Gradle) 项目参考 — code-req

> 本文件为 code-req 技能提供 Java(Gradle) 项目的语言差异说明。
> 在 CODING 阶段(步骤 4.2)中,当检测到项目语言为 java-gradle 时加载本文件。

## §1 项目结构识别
- 描述文件:`build.gradle` 或 `build.gradle.kts`(必须)
- 源码目录:`src/main/java/`(约定)
- 测试目录:`src/test/java/`(约定)

## §2 构建命令检测
- 构建:`gradle build` / `gradle compileJava`

## §3 测试框架识别
- 读取 `build.gradle` > `dependencies` 中测试框架
- 常见框架:JUnit 4/5 / TestNG / Spock
- 运行:`gradle test`

## §4 启动/运行命令检测
- 运行:`gradle run` 或 `java -jar <jar>`
- Spring Boot:`gradle bootRun`

## §5 Monorepo 声明文件解析
- `settings.gradle` > `include` 声明(Gradle 多项目)

## §6 编码约定
- 文件名:与 public 类名一致(PascalCase)
- 类/接口:PascalCase
- 方法/变量:camelCase
- 常量:UPPER_SNAKE_CASE
- 包名:lowercase.dot.separated

## §7 工具链检测
- 代码行数统计:`tokei` / `cloc`
- Lint:Checkstyle / SpotBugs

## §8 编码规范读取

> 本文件提供语言层面的默认约定。在 CODING 阶段,还须额外读取 `./assistants/rules/` 下的项目级编码规范(如 `coding-style.md`、`naming-conventions.md`),项目级规范优先级高于本文件的默认约定。