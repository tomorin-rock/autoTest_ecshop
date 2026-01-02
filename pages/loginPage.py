from selenium.webdriver.common.by import By

from autoTest_ecshop.base_page.basePage import BasePage
from autoTest_ecshop.pages.homePage import HomePage
from autoTest_ecshop.utils.log_util import logger


class LoginPage(HomePage):
    # 用户名定位器
    username_loc = (By.NAME, 'username')
    # 密码定位器
    password_loc = (By.NAME, 'password')
    # 提交登录
    submit_loc = (By.NAME, 'submit')
    # 登录成功后断言
    loginAssert_loc = (By.XPATH, '//div/p[@style]')




    def login(self,username,password):
        logger.debug(f"输入用户名{username},密码{password}")
        self.input_data(self.username_loc,username)
        self.input_data(self.password_loc,password)
        self.click_element(self.submit_loc)