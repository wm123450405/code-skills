# 发布部署手册 — <本版本号>

> ⚠ **本手册为通用发布部署骨架**,由 `code-publish` 技能从 `<本仓库>/skills/code-publish/templates/DEPLOY.md` 复制生成。
>
> **请先手动补全所有 `<placeholder>`(除 `<本版本号>` 外),再按本手册的步骤执行部署。**
>
> 本手册**默认提供"最常见部署方式"的占位示例**(tar.gz 打包 + systemd 启动 + MySQL 数据库);若你的软件形态不同(目录/镜像/Python/Java/...),请按需调整各章节示例。

---

## 1. 概述

- **版本号**:<本版本号>(由 `code-publish` 自动填充)
- **目标环境**:<生产 / 预发 / 测试>
- **发布时间**:<YYYY-MM-DD>
- **发布者**:<执行部署的人员>
- **软件名**:<你的软件名,如 myapp / web-portal / ...>

---

## 2. 打包

请根据你的软件形态,选择**下列一种**打包方式(可多选,但需在不同节点执行):

### 2.1 软件包方式(默认 — 适合大多数后端服务)

```bash
# 默认示例:tar.gz 打包
# <source_dir> = 编译后或构建后的目录(例如:dist/ / build/ / target/)
# <output>    = 输出的压缩包路径(例如:myapp-v0.0.0.tar.gz)

tar -czf <output>.tar.gz <source_dir>

# 校验(可选)
sha256sum <output>.tar.gz > <output>.tar.gz.sha256
```

### 2.2 目录方式(适合无需压缩的小型部署)

直接拷贝 `<source_dir>` 到目标服务器的目标路径(通常用 `rsync` / `scp -r`):

```bash
# 默认示例:rsync 同步
rsync -avz --delete <source_dir>/ <user>@<server>:/path/to/dest/
```

### 2.3 镜像方式(适合容器化部署)

```bash
# 默认示例:Docker 镜像打包
# <image_name> = 镜像名(例如:myapp)
# <version>    = 镜像 tag(例如:v0.0.0)
# <output>     = 保存到本地的 tar 路径(例如:myapp-v0.0.0-docker.tar)

docker build -t <image_name>:<version> .
docker save -o <output>.tar <image_name>:<version>

# 上传并加载(在目标服务器上)
# docker load -i <output>.tar
```

---

## 3. 获取成果物

<列出本版本的所有发布物,例如:>

```
dist/
├── <output>.tar.gz
├── <output>.tar.gz.sha256
└── checksums.txt
```

- **主成果物**:<主文件名,如 myapp-v0.0.0.tar.gz>
- **校验文件**:<校验文件名,如 myapp-v0.0.0.tar.gz.sha256>
- **附加文件**:<如有 db/schema.sql / docs/release-notes.md / ...>
- **存储位置**:<本地路径或内部包仓库地址>

---

## 4. 上传服务器(可选)

> 若打包方式已是 2.3 镜像方式且直接在目标服务器上 `docker load`,可跳过本节。

```bash
# 默认示例:scp 上传
# <user>   = 服务器登录用户(例如:deploy)
# <server> = 服务器地址(例如:192.168.1.100 或 deploy-prod-01.example.com)
# /path/to/dest/ = 目标部署目录(例如:/opt/releases/)

scp <output>.tar.gz <user>@<server>:/path/to/dest/
scp <output>.tar.gz.sha256 <user>@<server>:/path/to/dest/

# 验证上传完整性
ssh <user>@<server> "cd /path/to/dest/ && sha256sum -c <output>.tar.gz.sha256"
```

---

## 5. 初始化系统

> 本节**仅在首次部署或重大升级时执行**;后续发版(同版本号下的小版本)只需重新打包 + 替换主程序。

### 5.1 环境准备

<列出运行本软件所需的运行时依赖,例如:>

- **操作系统**:<Linux 发行版与版本,如 Ubuntu 22.04 / CentOS 9>
- **运行时**:<如 Java 17 / Python 3.11 / Node 20 / OpenJDK 21 / ...>
- **包管理器**:<如 apt / yum / dnf / pip / npm / ...>
- **系统服务**:<如 systemd / supervisord / docker / ...>
- **其他依赖**:<如 imagemagick / ffmpeg / ...>

**安装命令(默认示例)**:

```bash
# Ubuntu/Debian 系
sudo apt update && sudo apt install -y <runtime-package-name>

# CentOS/RHEL 系
sudo dnf install -y <runtime-package-name>
```

### 5.2 数据库建表语句执行

> 若本软件**不依赖数据库**,可跳过本节(并删除 5.3)。

```sql
-- <建表语句路径>:<server_path>/db/schema.sql
-- 默认示例:MySQL
-- <server_path> = 实际在服务器上的目录(例如:/opt/releases/myapp-v0.0.0/db/)

mysql -u<user> -p<passwd> <dbname> < <server_path>/db/schema.sql
```

**说明**:
- `<user>` = 数据库用户(首次部署建议用 `root`,后续可改专用用户)
- `<passwd>` = 数据库密码(**不要提交到 git**)
- `<dbname>` = 数据库名(例如 `myapp_prod`)

### 5.3 数据库初始化数据

> 若本软件**无预置数据**(纯用户生成),可跳过本节。

```sql
-- <初始化数据路径>:<server_path>/db/init-data.sql

mysql -u<user> -p<passwd> <dbname> < <server_path>/db/init-data.sql
```

**典型内容**:
- 字典表 / 配置表 / 默认管理员账号
- 首次发布的初始数据

### 5.4 配置修改

<配置文件路径>(默认示例):`/etc/myapp/config.yaml`

**修改项清单**(按需增删):

- 修改项 1:`<key>` = `<value>` — 说明(例如:`server.port = 8080`)
- 修改项 2:`<key>` = `<value>` — 说明(例如:`db.url = jdbc:mysql://localhost:3306/myapp_prod`)
- 修改项 3:`<key>` = `<value>` — 说明(例如:`logging.level = INFO`)

**配置模板位置**:`<server_path>/config-template.yaml`(随发布物一并上传,作为参考)

---

## 6. 启动运行

> 本节假设本软件以 **systemd 服务**形式运行(Linux 主流);其他方式(Docker / supervisord / 直接 nohup)请按需调整。

```bash
# 默认示例:systemd 启动

# 1. 复制 service 文件
sudo cp <server_path>/deploy/myapp.service /etc/systemd/system/

# 2. 重新加载 systemd
sudo systemctl daemon-reload

# 3. 启动服务
sudo systemctl start myapp

# 4. 设置开机自启(可选)
sudo systemctl enable myapp

# 5. 查看状态
sudo systemctl status myapp
```

**其他启动方式**(如使用):

- **Docker**:`docker run -d --name myapp -p 8080:8080 <image_name>:<version>`
- **nohup 直接启动**:`nohup <启动命令> > /var/log/myapp.log 2>&1 &`
- **Docker Compose**:`docker compose -f docker-compose.yml up -d`

---

## 7. 首次进入软件系统

- **访问 URL**:`<http://server:port>`(例如 `http://192.168.1.100:8080`)
- **默认账号**:`<admin / root / ...>`(由 5.3 初始化数据预设)
- **默认密码**:`<...>`(**首次登录后立即修改**;不要保留在文档中)
- **HTTPS 配置**:<如有,提供证书路径与配置说明;如无,标注"建议加 HTTPS">
- **首次操作建议**:
  - 修改默认管理员密码
  - 配置 SMTP(若需要邮件通知)
  - 配置备份策略(数据库 + 配置文件)
  - 配置监控(进程存活 / 接口探活 / 日志告警)

---

## 8. 验证清单

部署完成后,**逐项勾选**以下清单;所有项必须为 `[x]` 才能视为发布成功。

- [ ] **服务进程已启动**:`systemctl status myapp` 显示 `active (running)`
- [ ] **服务开机自启已配置**:`systemctl is-enabled myapp` 返回 `enabled`
- [ ] **数据库连接正常**:服务日志中无 "Connection refused" / "DB timeout" 等错误
- [ ] **数据库表已创建**:用 SQL 客户端连入,检查关键表存在
- [ ] **关键 API 可访问**:`curl http://<server>:<port>/health` 返回 `200 OK`
- [ ] **关键页面可访问**:浏览器打开主页,无 5xx 错误
- [ ] **默认账号已修改密码**:用默认账号登录后,跳转到改密页或菜单,成功修改
- [ ] **配置文件已锁定权限**:`chmod 600 /etc/myapp/config.yaml` + `chown root:root`
- [ ] **日志路径可写**:`/var/log/myapp/` 目录存在且 myapp 用户可写
- [ ] **磁盘空间充足**:`df -h` 检查 / /var / 数据库目录,余量 > 20%
- [ ] **防火墙规则已更新**:`<port>` 端口已在入站规则中开放
- [ ] **备份策略已就位**:数据库每日自动备份 + 至少保留 7 天
- [ ] **监控告警已就位**:进程挂掉 / 接口 5xx 告警已配置
- [ ] **日志无 ERROR**:`journalctl -u myapp --since "1 minute ago" | grep ERROR` 为空
- [ ] **回滚方案已知**:见 [`UPDATE.md`](./UPDATE.md) 第 8 节"回滚方案"(如本版本非基线)

---

## 附录:发布后通知(可选)

发布成功后,建议通知相关方:

- 内部 IM / 邮件群:`<内部群组>`
- 客户 / 用户(若是 C 端):`<邮件模板 / 公告链接>`
- 运维值班:`<oncall 联系人>`

> 本附录**不强制**;仅在"对用户可见的发版"时需要。
