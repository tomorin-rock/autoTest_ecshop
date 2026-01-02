import allure
import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
    # 打开浏览器进入测试首页
    driver = webdriver.Edge()
    url = "http://192.168.28.1/ecshop/"
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # 获取钩子函数的执行结果
    outcome = yield
    report = outcome.get_result()

    # 只在测试用例执行失败时截图
    if report.when == "call" and report.outcome == "failed":
        # 从测试用例的参数中获取 driver
        driver = item.funcargs.get("driver")
        if driver:
            # 截图并附加到 Allure 报告
            allure.attach(
                driver.get_screenshot_as_png(),
                name="失败截图",
                attachment_type=allure.attachment_type.PNG
            )