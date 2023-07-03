from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        option = webdriver.ChromeOptions()
        option.binary_location = r'C:\Users\Dell\AppData\Local\Google\Chrome\Application\chrome.exe'
        path = r'C:\Users\Dell\AppData\Local\Programs\Python\Python310\chromedriver.exe'
        service = Service(path)
        service.start()
        driver = webdriver.Chrome(service=service, options=option)
        return driver
    else:
        driver = webdriver.Firefox()
        return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")
