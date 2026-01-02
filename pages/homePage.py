from selenium.webdriver.common.by import By
from autoTest_ecshop.base_page.basePage import BasePage


class HomePage(BasePage):
    # 首页登录按钮定位器
    login_loc = (By.XPATH, '//img[@src="themes/default/images/bnt_log.gif"]')
    logout_loc = (By.LINK_TEXT, '退出')
