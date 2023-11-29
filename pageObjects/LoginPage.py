import time
from selenium.webdriver.common.by import By

class LoginPage:
# LoginPage locators

    input_username_xpath = "//input[@id='user-name']"
    input_password_xpath = "//input[@id='password']"
    input_login_xpath = "//input[@id='login-button']"

#ProductPage locators
    btn_reactBurger_xpath = "//button[@id='react-burger-menu-btn']"
    a_logout_xpath= "//a[@id='logout_sidebar_link']"

    def __init__(self,driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.XPATH, self.input_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_username_xpath).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.input_password_xpath).clear()
        self.driver.find_element(By.XPATH,self.input_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.input_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH,self.btn_reactBurger_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.a_logout_xpath).click()









