import traceback

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from autoTest_ecshop.utils.log_util import logger


class BasePage:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 20)

    def find_element(self, locator):
        try:
            logger.debug(f"正在定位元素：{locator}")
            login = self.wait.until(EC.visibility_of_element_located(locator))
            logger.debug(f"元素{locator}定位成功")
            return login
        except:
            logger.error(f"元素{locator}定位失败,错误日志如下\n{traceback.format_exc()}")
            return None

    def find_elements(self, locator):
        try:
            logger.debug(f"正在定位元素：{locator}")
            login = self.wait.until(EC.visibility_of_all_elements_located(locator))
            logger.debug(f"元素{locator}定位成功")
            return login
        except:
            logger.error(f"元素{locator}定位失败,错误日志如下\n{traceback.format_exc()}")

    def click_element(self, locator):
        self.find_element(locator).click()
        logger.debug(f"点击元素{locator}")
        return 0

    # 输入关键字
    def input_data(self, locator, keyword):
        element = self.find_element(locator)
        if element is not None:
            element.clear()
            element.send_keys(keyword)
        return 0

    # 获取文本
    def get_text(self, locator):
        assertText = self.wait.until(EC.visibility_of_element_located(locator))
        return assertText.text

    # 下拉菜单选择
    def select_option(self, locator, text):
        option = self.wait.until(EC.presence_of_element_located(locator))
        Select(option).select_by_visible_text(text)
        return 0
