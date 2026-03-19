import time

from autoTest_ecshop.pages.buyPage import BuyPage


class TestBuy():
    # @pytest.mark.skip
    def test_buy(self,driver):
        buyPage = BuyPage(driver)
        # 点击结算
        buyPage.click_element(buyPage.settle_loc)
        # 创建订单并支付
        buyPage.order_goods()
        # 实际结果
        actual = buyPage.get_text(buyPage.odSuccess_loc)
        # 预期结果
        expectedRes = "感谢您在本店购物"
        # 断言
        assert expectedRes in actual
        # 退出
        buyPage.click_element(buyPage.logout_loc)
        time.sleep(1)