# Python 项目参考 — code-design

> 本文件为 code-design 技能提供 Python 项目的语言差异说明。
> 在步骤 5(探索项目结构)中,当检测到项目语言为 python 时加载本文件。

## §1 项目结构识别

### 描述文件特征
- `pyproject.toml`:Python 项目标准描述文件(PEP 518/621)
- `setup.py` / `setup.cfg`:传统 setuptools 配置
- `requirements.txt` / `requirements-dev.txt`:依赖文件
- `Pipfile` / `Pipfile.lock`: Pipenv

### 目录约定
- 源码目录:常见 `src/`、`<package_name>/`
- 测试目录:常见 `tests/`、`test/`
- 虚拟环境:`.venv/`、`venv/`、`env/`

### 包管理器识别
- `pyproject.toml` + `[tool.poetry]` → Poetry
- `Pipfile` → Pipenv
- `requirements.txt` → pip

## §2 构建命令检测

### 构建命令
- Poetry:`poetry build`
- setuptools:`python -m build` 或 `python setup.py sdist bdist_wheel`
- 纯脚本项目:无需构建

## §3 测试框架识别

### 框架检测
- 读取 `pyproject.toml` > `[tool.pytest]` / `[tool.pytest.ini_options]` → pytest
- `[tool.tox]` → tox
- `[tool.nox]` → nox
- `setup.cfg` > `[tool:pytest]` → pytest
- 常见框架:pytest / unittest / nose2

## §4 启动/运行命令检测

- 读取 `pyproject.toml` > `[project.scripts]`(入口点)
- 退化:`python -m <package>` 或 `python <main.py>`

## §5 Monorepo 声明文件解析

- Python 生态中 monorepo 较少见,通常通过 `[tool.poetry.workspace]` 或手动管理多个 `pyproject.toml`

## §6 编码约定

### 命名约定
- 文件名:snake_case
- 类名:PascalCase
- 函数/变量:snake_case
- 常量:UPPER_SNAKE_CASE
- 私有成员:前缀 `_`

### 错误处理风格
- try/except/finally
- 自定义异常类(继承 Exception)
- 上下文管理器(with 语句)

## §7 工具链检测

### 代码行数统计
- 优先:`tokei`
- 退化:`cloc`
- 兜底:heuristic

### Lint/格式化
- Ruff / Flake8(`.flake8` / `ruff.toml`)
- Black(`pyproject.toml` > `[tool.black]`)
- mypy(`pyproject.toml` > `[tool.mypy]`)