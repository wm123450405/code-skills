# Java(Maven) 项目参考 — `/code req`

> 本文件为 `/code req` 子命令提供 Java(Maven) 项目的语言差异说明。
> 在 CODING 阶段(步骤 4.2)中,当检测到项目语言为 java-maven 时加载本文件。

## 项目结构识别
- 描述文件:`pom.xml`(必须)
- 源码目录:`src/main/java/`(约定)
- 测试目录:`src/test/java/`(约定)
- 资源目录:`src/main/resources/`

## 构建命令检测
- 构建:`mvn compile` / `mvn package` / `mvn install`

## 测试框架识别
- 读取 `pom.xml` > `<dependencies>` 中测试框架
- 常见框架:JUnit 4/5 / TestNG
- 运行:`mvn test`

## 启动/运行命令检测
- 运行:`mvn exec:java` 或 `java -jar <jar>`
- Spring Boot:`mvn spring-boot:run`

## Monorepo 声明文件解析
- `pom.xml` > `<modules>` 字段(Maven 多模块项目)

## 编码约定
- 文件名:与 public 类名一致(PascalCase)
- 类/接口:PascalCase
- 方法/变量:camelCase
- 常量:UPPER_SNAKE_CASE
- 包名:lowercase.dot.separated

## 工具链检测
- 代码行数统计:`tokei` / `cloc`
- 静态分析:SpotBugs / Checkstyle / PMD

## 编码规范读取

> 本文件提供语言层面的默认约定。在 CODING 阶段,还须额外读取 `./assistants/rules/` 下的项目级编码规范(如 `coding-style.md`、`naming-conventions.md`),项目级规范优先级高于本文件的默认约定。