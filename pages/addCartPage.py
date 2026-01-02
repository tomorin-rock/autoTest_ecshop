from selenium.webdriver.common.by import By

from autoTest_ecshop.pages.homePage import HomePage


class AddCartPage(HomePage):
    # 搜索框定位
    search_loc = (By.NAME, 'keywords')
    # 点击搜索按钮
    btn_loc = (By.NAME, 'imageField')
    # 商品元素定位
    good_loc = (By.LINK_TEXT, '诺基亚N85')
    # 加入购物车元素定位
    shopCar_loc = (By.XPATH, '//img[@src="themes/default/images/bnt_cat.gif"]')
    # 加入购物车断言
    cart_actual =  (By.XPATH,'//*[@id="formCart"]/table[2]/tbody/tr/td[1]')

    # 搜索商品并加入购物车
    def add_good_to_cart(self, goodName):
        self.input_data(self.search_loc, goodName)
        self.click_element(self.btn_loc)
        self.click_element(self.good_loc)
        self.click_element(self.shopCar_loc)