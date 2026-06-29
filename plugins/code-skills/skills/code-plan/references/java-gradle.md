# Java(Gradle) 项目参考 — code-design

> 本文件为 code-design 技能提供 Java(Gradle) 项目的语言差异说明。
> 在步骤 5(探索项目结构)中,当检测到项目语言为 java-gradle 时加载本文件。

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
- 同 java-maven.md §6

## §7 工具链检测
- 同 java-maven.md §7