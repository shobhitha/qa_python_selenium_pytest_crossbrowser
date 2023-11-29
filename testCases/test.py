import time

from selenium import webdriver

def test_login_test():
    driver=webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    time.sleep(3)
    driver.close()

