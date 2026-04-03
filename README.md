# ECShop 自动化测试项目

## 项目简介

这是一个基于 Python + Selenium + Pytest + Allure 框架的 ECShop 电商网站自动化测试项目。项目实现了登录、添加购物车、购买商品等核心功能的自动化测试，并生成美观的 Allure 测试报告。

## 项目结构

```
autoTest_ecshop/
├── base_page/          # 基础页面类
│   └── basePage.py     # 基础页面操作方法
├── pages/              # 页面类
│   ├── loginPage.py    # 登录页面
│   ├── addCartPage.py  # 购物车页面
│   ├── buyPage.py      # 购买页面
│   └── homePage.py     # 首页
├── testCases/          # 测试用例
│   ├── test_01_login.py    # 登录测试
│   ├── test_02_addCart.py  # 添加购物车测试
│   └── test_03_buy.py      # 购买流程测试
├── utils/              # 工具类
│   ├── log_util.py     # 日志工具
│   ├── readFile.py     # 文件读取工具
│   └── getPath.py      # 路径工具
├── data/               # 测试数据
│   └── login.yml       # 登录测试数据
├── reports/            # 测试报告
├── temp/               # 临时数据
├── logs/               # 日志文件
├── conftest.py         # pytest 配置文件
├── runMain.py          # 主运行文件
└── pytest.ini          # pytest 配置文件
```

## 技术栈

- **Python 3.12**
- **Selenium** - 浏览器自动化测试工具
- **Pytest** - 测试框架
- **Allure** - 测试报告生成工具
- **YAML** - 测试数据管理

## 环境搭建

### 1. 安装 Python

确保安装了 Python 3.12 或更高版本。

### 2. 安装依赖包

```bash
pip install selenium pytest allure-pytest pyyaml
```

### 3. 安装 Allure 命令行工具

- 下载 Allure 命令行工具：https://github.com/allure-framework/allure2/releases
- 解压并将 bin 目录添加到系统环境变量中

### 4. 配置测试环境

- 修改 `conftest.py` 文件中的测试网址：
  ```python
  url = "http://192.168.28.1/ecshop/"  # 修改为你的 ECShop 网站地址
  ```

- 修改 `data/login.yml` 文件中的测试数据：
  ```yaml
  loginInfos:
    - ["username1", "password1", "登录成功"]
    - ["username2", "password2", "登录成功"]
  ```

## 运行测试

### 方法一：直接运行 runMain.py

```bash
python runMain.py
```

该脚本会执行以下操作：
1. 运行所有测试用例并生成 Allure 原始数据
2. 生成 Allure 测试报告
3. 自动打开测试报告

### 方法二：使用 pytest 命令运行

```bash
# 运行所有测试并生成报告
pytest --alluredir=./temp
allure generate ./temp -o reports
allure open reports

# 运行指定测试文件
pytest testCases/test_01_login.py --alluredir=./temp
```

## 测试功能

### 1. 登录测试
- 测试不同用户的登录功能
- 验证登录成功后的提示信息

### 2. 添加购物车测试
- 搜索商品并添加到购物车
- 验证购物车页面是否正确显示

### 3. 购买流程测试
- 从购物车结算
- 填写订单信息并支付
- 验证订单是否成功创建

## 测试报告

测试完成后，会在 `reports` 目录生成 Allure 测试报告，报告包含：
- 测试执行结果概览
- 详细的测试步骤
- 失败用例的截图
- 测试执行时间统计

## 日志管理

测试过程中的日志会记录在 `logs` 目录中，按日期命名，方便问题排查。

## 注意事项

1. 确保 ECShop 网站可以正常访问
2. 确保浏览器驱动与浏览器版本匹配
3. 测试前请确保测试数据的准确性
4. 如需修改测试流程，请修改相应的页面类和测试用例

## 扩展建议

1. 添加更多测试场景，如：
   - 商品搜索测试
   - 用户注册测试
   - 个人中心功能测试
   - 订单管理测试

2. 优化测试框架：
   - 添加数据驱动测试
   - 实现测试用例的参数化
   - 增加测试环境的配置管理
   - 实现测试结果的邮件通知

## 许可证

本项目仅供学习和参考使用。

## 作者

- 项目创建时间：2026年
- 测试框架：Python + Selenium + Pytest + Allure
