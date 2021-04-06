import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    browser = webdriver.Chrome(executable_path='D:\PythonProject\chromedriver.exe')
    browser.get('https://target.my.com/')
    browser.set_window_size(1400, 1000)
    yield browser
    browser.close()
