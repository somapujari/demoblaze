import time
from utility.logsgenarator import Loggen
import pytest
from selenium.webdriver.common.by import By
from pageobjects.demoblaze_login import Login
from utility.readpropertie import ConfigRead


class Test_login:
    url = 'https://www.demoblaze.com/'
    username = ConfigRead.get_username()
    password = ConfigRead.get_password()
    logger = Loggen.loggen()

    @pytest.mark.parametrize('username, password', [
        ('vils@123', 'test@12'),
        ('vils@123', 'Test@1235656'),
        ('soma@1', 'test@1234'),
        ('vils@123', 'Test@123')
    ])
    def test_login(self, setup, username, password):
        self.logger.info('test_login statred')
        self.driver = setup
        self.logger.info(f'opening  url = {self.url} ')
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.lg = Login(self.driver)
        self.lg.click_login()
        self.logger.info(f'entering username = {username}')
        self.lg.enter_username(username)
        self.logger.info(f'entering password = {password}')
        self.lg.enter_password(password)
        self.logger.info('clicking log in  button')
        self.lg.click_on_login()
        time.sleep(4)
        self.logger.info('verifying  test_login')
        act_user = self.driver.find_element(By.XPATH, self.lg.verify_login_user_xpath).text
        print(act_user)
        if act_user == 'Welcome'+' '+username:
            assert True
            self.driver.save_screenshot(r'C:\Users\Dell\PycharmProjects\demoblaze\screenshots\loginpass.png')
            self.driver.close()
            self.logger.info('test passed ')
        else:
            self.driver.save_screenshot(r'C:\Users\Dell\PycharmProjects\demoblaze\screenshots\loginfail.png')
            self.logger.info('test failed ')
            self.driver.close()
            assert False
        self.logger.info('test_login completed ')
