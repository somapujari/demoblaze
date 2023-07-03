from selenium.webdriver.common.by import By


class Login:
    login_id = 'login2'
    username_id = 'loginusername'
    password_id = 'loginpassword'
    login_xpath = '//button[@onclick="logIn()"]'
    verify_login_user_xpath = '//a[@id="nameofuser"]'

    def __init__(self, driver):
        self.driver = driver

    def click_login(self):
        self.driver.find_element(By.ID, self.login_id).click()

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_id).clear()
        self.driver.find_element(By.ID, self.username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_id).clear()
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def click_on_login(self):
        self.driver.find_element(By.XPATH, self.login_xpath).click()


    
