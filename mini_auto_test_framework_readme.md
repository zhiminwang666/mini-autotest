# Mini AutoTest Framework (Python + PyTest + CI/CD)

这是一个从 **0 到 1** 搭建的 **Python 自动化测试项目**，覆盖：
- PyTest 测试框架
- API Client 封装 + Fake API（FastAPI）
- 多环境配置（YAML）
- 统一断言（Assertions）
- Allure 测试报告
- GitHub Actions CI
- **Jenkins（Windows）CI Pipeline**

> 目标：让项目 **本地可跑、CI 可复现、报告可展示、面试可讲清**。

---

## 📁 项目结构

```
mini-autotest/
├── api/                    # API 封装层
│   ├── __init__.py
│   ├── client.py           # HTTP Client（requests + Allure step）
│   └── user_api.py         # 业务 API（login / profile）
│
├── config/                 # 多环境配置
│   ├── dev.yaml
│   └── test.yaml
│
├── utils/                  # 工具层
│   ├── __init__.py
│   └── assertion.py        # 统一断言封装
│
├── tests/                  # 测试用例
│   ├── test_login.py
│   └── test_user.py
│
├── fake_api.py             # Fake API（FastAPI）
├── conftest.py             # pytest fixture & 环境加载
├── requirements.txt        # 项目依赖
├── Jenkinsfile              # Jenkins Pipeline（Windows bat）
├── .gitignore
└── README.md
```

---

## 🧪 技术栈

- **Python** 3.9+
- **PyTest**（测试框架）
- **requests**（HTTP 客户端）
- **FastAPI + uvicorn**（Fake API）
- **PyYAML**（环境配置）
- **Allure**（测试报告）
- **GitHub Actions**（CI）
- **Jenkins（Windows）**（企业级 CI）

---

## 🚀 本地运行

### 1️⃣ 创建虚拟环境

```bat
python -m venv .venv
.venv\Scripts\activate
```

### 2️⃣ 安装依赖

```bat
pip install -r requirements.txt
```

### 3️⃣ 启动 Fake API

```bat
uvicorn fake_api:app --host 127.0.0.1 --port 8000
```

### 4️⃣ 运行测试

```bat
pytest -q
```

指定环境：

```bat
pytest --env=dev
```

---

## 🧩 PyTest 设计说明

### Fixture（`conftest.py`）

- `--env` 参数切换环境（dev / test）
- 自动加载 `config/{env}.yaml`
- 提供 `config`、`user_api`、`token` 等 fixture

### 统一断言（`utils/assertion.py`）

- `assert_status_code`
- `assert_json_has_keys`
- `assert_json_key`

👉 减少测试中重复 assert，提高可维护性。

---

## 📊 Allure 报告

### 本地生成

```bat
pytest --alluredir=allure-results
allure serve allure-results
```

报告内容包括：
- Feature / Story
- 测试步骤（API 调用）
- Request / Response 附件

---

## 🔁 GitHub Actions CI

- 代码 push / PR 自动触发
- 创建虚拟环境
- 安装依赖
- 运行 pytest
- 生成 HTML / Allure 结果
- 上传为 CI Artifacts

（可扩展：发布到 GitHub Pages）

---

## 🏗 Jenkins CI（Windows）

### 特点

- 使用 **Jenkinsfile（Pipeline as Code）**
- Windows 节点使用 `bat`
- 自动：
  - 创建 venv
  - 安装依赖
  - 启动 Fake API
  - 运行 pytest
  - 生成 Allure 报告

### Jenkinsfile 核心阶段

- Checkout
- Setup venv & deps
- Start Fake API
- Run tests
- Publish Allure Report

---

## 💡 项目亮点（面试可讲）

- 使用 PyTest + Fixture 设计可复用测试框架
- API Client 与测试解耦
- 支持多环境配置（YAML + CLI 参数）
- 统一断言层，提升可维护性
- Allure 报告可视化测试过程
- **同时支持 GitHub Actions 和 Jenkins CI**
- Windows Jenkins Pipeline 实战经验

---

## 🧭 适用场景

- API 自动化测试
- CI/CD 测试流水线
- 测试 / QA / SDET / 自动化工程师作品集

---

## 📌 后续可扩展

- Jenkins 参数化（dev / test）
- 定时构建（Nightly Regression）
- Docker 化
- 数据驱动测试（CSV / JSON）
- 安全扫描 / 质量门禁

---

> ✨ 这个项目的目标不是“写几个测试”，而是**搭建一套可复现、可演示、可扩展的自动化测试工程**。

