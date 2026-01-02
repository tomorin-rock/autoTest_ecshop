from selenium.webdriver.common.by import By

from autoTest_ecshop.pages.addCartPage import AddCartPage


class BuyPage(AddCartPage):
    # 结算中心按钮元素定位
    settle_loc = (By.XPATH, '//img[@src="themes/default/images/checkout.gif"]')
    # 表单填写
    province_loc = (By.NAME, 'province')
    city_loc = (By.NAME, 'city')
    district_loc = (By.NAME, 'district')
    name_loc = (By.NAME, 'consignee')
    address_loc = (By.NAME, 'address')
    tel_loc = (By.NAME, 'tel')
    # 点击配送
    submit_loc = (By.NAME, 'Submit')
    # 配送方式元素定位
    shipping_loc = (By.XPATH, '//input[@name="shipping" and @value="5"]')
    # 付款方式元素定位
    payment_loc = (By.XPATH, '//input[@name="payment" and @value="2"]')
    # 提交订单元素定位
    subOrder_loc = (By.XPATH, '//input[@src="themes/default/images/bnt_subOrder.gif"]')
    # 购物成功断言
    odSuccess_loc = (By.XPATH, '//*[contains(@class, "flowBox")]/h6[1]')
    # 断言
    logout_loc = (By.LINK_TEXT, '退出')

    # 填写表单点击配送(如果用户没有购物过，需要填写)
    def fill_form(self, province, city, district, name, address, tel):
        self.select_option(self.shopCar_loc, province)
        self.select_option(self.shopCar_loc, city)
        self.select_option(self.shopCar_loc, district)
        self.input_data(self.name_loc, name)
        self.input_data(self.address_loc, address)
        self.input_data(self.tel_loc, tel)
        self.click_element(self.submit_loc)

    # 订单创建和支付
    def order_goods(self):
        self.click_element(self.shipping_loc)
        self.click_element(self.payment_loc)
        self.click_element(self.subOrder_loc)
