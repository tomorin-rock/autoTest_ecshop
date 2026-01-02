import time

import allure
import pytest

from autoTest_ecshop.pages.addCartPage import AddCartPage


class TestAddCart:
    @allure.epic("ecshop_v1.0")
    @allure.feature("购物车管理")
    @allure.story("添加购物车")
    @allure.title("添加购物车")
    # @pytest.mark.skip
    def test_add_cart(self, driver):
        # 在搜索框中输入
        addCartPage = AddCartPage(driver)
        # 搜索商品加入购物车
        addCartPage.add_good_to_cart("诺基亚")
        """"""
        actual = addCartPage.get_text(addCartPage.cart_actual)
        exceptedRes = "购物金额"
        assert exceptedRes in actual
        # addCartPage.fill_form("安徽", "安庆", "迎江区",
        #                    "倪哥", "倪家村", 12341111)
        time.sleep(1)
