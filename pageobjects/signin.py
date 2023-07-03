from selenium.webdriver.common.by import By
from selenium import webdriver


driver = webdriver.Chrome()


class Signin:
    sign_uplink_xpath = "//a[@id='signin2']"
    username_id = 'sign-username'
    password_id = 'sign-password'
    signup_xpath = "//button[contains(text(),'Sign up')]"

    def __init__(self, driver):
        self.driver = driver

    def click_signup_link(self):
        self.driver.find_element(By.XPATH, self.sign_uplink_xpath).click()

    def in_username(self, username):
        # self.driver.find_element(By.ID, self.username_id).clear()
        self.driver.find_element(By.ID, self.username_id).send_keys(username)

    def in_password(self, password):
        # self.driver.find_element(By.ID, self.password_id).clear()
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def click_signup_register(self):
        self.driver.find_element(By.XPATH, self.signup_xpath).click()
