from selenium import webdriver

import pytest

#Browser setup
@pytest.fixture()
def setup(browser):

    #Testing in Chrome browser
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser")

    #Testing in firefox browser
    elif browser == 'firefox':
        drive = webdriver.Firefox()
        print("Launching Firefox browser")

    #Testing in Internet explorer browser
    elif browser == 'ie':
        driver = webdriver.Ie()
        print("Launching Internet explorer browser")

    #Testing in Microsoft edge browser
    elif browser == 'edge':
        driver = webdriver.Edge()
        print('Launching Microsoft Edge browser')

    #Setting up chrome as default browser
    else:
        driver = webdriver.Chrome()
        print("Launching the default Chrome browser")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#Setup for HTML reporting
def pytest_configure(config):
    config._metadata = {
        'Project Name': 'Swag Labs testing',
        'Module Name': 'Login',
        'Tester Name': 'sdittakavi'
    }















