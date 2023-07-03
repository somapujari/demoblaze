import time
from utility.readpropertie import ConfigRead
from pageobjects.signin import Signin
from utility.logsgenarator import Loggen


class Test_signup:
    url = ConfigRead.get_application_url()
    username = ConfigRead.get_username()
    password = ConfigRead.get_password()
    logger = Loggen.loggen()

    def test_signup(self, setup):
        self.logger.info('test_signup started')
        self.driver = setup
        self.logger.info(f'entering url= {self.url}')
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.si = Signin(self.driver)
        self.si.click_signup_link()
        self.logger.info(f'entering username= {self.username}')
        self.si.in_username(self.username)
        self.logger.info(f'entering password= {self.password}')
        self.si.in_password(self.password)
        self.si.click_signup_register()
        time.sleep(2)
        self.logger.info('verifying test signup')
        text = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        print(text)
        if text == 'Sign up successful.':
            assert True
            self.logger.info('test sign up passed')
            self.driver.save_screenshot(r'C:\Users\Dell\PycharmProjects\demoblaze\screenshots\signuppass.png')
        else:
            self.logger.info('test signup failed')
            self.driver.save_screenshot(r'C:\Users\Dell\PycharmProjects\demoblaze\screenshots\signupfail.png')
            assert False
        self.logger.info('test_signup is completed')







