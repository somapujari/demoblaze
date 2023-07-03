import time
import pytest
from pageobjects.demoblazeaddtocart import Ad_to_cart
from pageobjects.demoblaze_login import Login
from utility.logsgenarator import Loggen
from utility.readpropertie import ConfigRead


class Test_add_to_cart:
    url = 'https://www.demoblaze.com/'
    username = ConfigRead.get_username()
    password = ConfigRead.get_password()
    name = 'vishal'
    country = 'india'
    city = 'pune'
    creditcard = '1234567890123456'
    month = 'jan'
    year = 2020
    logger = Loggen.loggen()

    def test_AddToCart(self, setup):
        self.logger.info('test_addtocart  started')
        self.driver = setup
        self.logger.info(f'opening url = {self.url}')
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        # self.lg = Login(self.driver)
        # self.lg.click_login()
        # self.lg.enter_username(self.username)
        # self.lg.enter_password(self.password)
        # self.lg.click_on_login()
        self.ad = Ad_to_cart(self.driver)
        self.logger.info('clicking phone pdoiducts')
        self.ad.click_phones()
        self.logger.info('selecting phones')
        self.ad.select_phones()
        self.logger.info('adding to cart')
        self.ad.add_cart()
        # self.ad.verify_added()
        self.logger.info('opening cart')
        self.ad.click_cart()
        self.logger.info('ordering submit')
        self.ad.click_submit_order()
        self.logger.info(f'entering name={self.name}')
        self.ad.input_name(self.name)
        self.logger.info(f'entering country={self.country}')
        self.ad.input_country(self.country)
        self.ad.input_city(self.city)
        self.ad.input_creditcard(self.creditcard)
        self.ad.input_month(self.month)
        self.ad.input_year(self.year)
        self.logger.info('clicking purchase')
        self.ad.click_purchase()
        self.logger.info('verifying order ')
        self.ad.verify_order()
        self.logger.info('reading orderid')
        self.ad.read_id()
        self.ad.click_ok()
        self.logger.info('test_addtocart completed')




