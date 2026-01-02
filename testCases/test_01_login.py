import time

import allure
import pytest
from autoTest_ecshop.pages.loginPage import LoginPage
from autoTest_ecshop.utils.readFile import read_file


# 登录
class TestLogin():
    test_users = read_file("login.yml").get("loginInfos")

    @allure.epic("ecshop_v1.0")
    @allure.feature("用户管理")
    @allure.story("登录")
    @pytest.mark.parametrize("username,password,expectedRes",test_users)
    def test_login(self, driver, username, password, expectedRes):
        allure.dynamic.title(f"使用用户名{username}，密码{password}")
        # 实例化登录页面
        loginPage = LoginPage(driver)
        # 点击登录按钮,进行登录
        loginPage.click_element(loginPage.login_loc)
        # 输入用户名和密码进行登录
        loginPage.login(username,password)
        # loginPage.login("nige1", "123456")
        # 实际结果
        actual = loginPage.get_text(loginPage.loginAssert_loc)
        # 断言
        # expectedRes = "登录成功"
        assert expectedRes == actual
        # 退出
        # loginPage.click_element(loginPage.logout_loc)
        time.sleep(1)
