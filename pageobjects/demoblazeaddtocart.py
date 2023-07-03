from selenium.webdriver.common.by import By


class Ad_to_cart:
    phones_xpath = '''//a[@onclick="byCat('phone')"]'''
    select_phone = '//a[@href="prod.html?idp_=6"]'
    add_xpath = '''//a[@onclick="addToCart(6)"]'''
    cart_id = 'cartur'
    submit_button_xpath = '''//button[@type='button'and @class="btn btn-success"]'''
    name_input_ID = 'name'
    country_input_ID = 'country'
    city_input_ID = 'city'
    creditcard_input_Id = 'card'
    month_input_Id = 'month'
    year_input_id = 'year'
    purchase_click_xpath = '''//button[@onclick="purchaseOrder()"]'''
    verify_order_xpath = '//div[@class="sweet-alert  showSweetAlert visible"]/h2'
    veri_orderid_xpath = '''//div[@class="sweet-alert  showSweetAlert visible"]/p['id']'''
    ok_button_xpath = '//button[@class="confirm btn btn-lg btn-primary"]'

    def __init__(self, driver):
        self.driver = driver

    def click_phones(self):
        self.driver.find_element(By.XPATH, self.phones_xpath).click()

    def select_phones(self):
        self.driver.find_element(By.XPATH, self.select_phone).click()

    def add_cart(self):
        self.driver.find_element(By.XPATH, self.add_xpath).click()

    def verify_added(self):
        add = self.driver.switch_to.alert.get_attribute('value')
        print(add)
        self.driver.switch_to.alert.accept()

    def click_cart(self):
        self.driver.find_element(By.ID, self.cart_id).click()

    def click_submit_order(self):
        self.driver.find_element(By.XPATH, self.submit_button_xpath).click()

    def input_name(self, name):
        self.driver.find_element(By.ID, self.name_input_ID).send_keys(name)

    def input_country(self, country):
        self.driver.find_element(By.ID, self.country_input_ID).send_keys(country)

    def input_city(self, city):
        self.driver.find_element(By.ID, self.city_input_ID).send_keys(city)

    def input_creditcard(self, creditcard):
        self.driver.find_element(By.ID, self.creditcard_input_Id).send_keys(creditcard)

    def input_month(self, month):
        self.driver.find_element(By.ID, self.month_input_Id).send_keys(month)

    def input_year(self, year):
        self.driver.find_element(By.ID, self.year_input_id).send_keys(year)

    def click_purchase(self):
        self.driver.find_element(By.XPATH, self.purchase_click_xpath).click()

    def read_id(self):
        orderid = self.driver.find_element(By.XPATH, self.veri_orderid_xpath).text
        print(orderid)

    def click_ok(self):
        self.driver.find_element(By.XPATH, self.ok_button_xpath).click()

    def verify_order(self):
        act_response = self.driver.find_element(By.XPATH, self.verify_order_xpath).text
        print(act_response)
        if act_response == 'Thank you for your purchase!':
            assert True
            self.driver.save_screenshot(r'C:\Users\Dell\PycharmProjects\demoblaze\screenshots\addtocartpass.png')
        else:
            self.driver.save_screenshot(r'C:\Users\Dell\PycharmProjects\demoblaze\screenshots\addtocartfail.png')
            assert False






