import pytest
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from ui.pages.registration_page import RegistrationPage


class UnsupportedBrowserException(Exception):
    pass


@pytest.fixture(scope='function')
def base_page(driver):
    return BasePage(driver)


@pytest.fixture(scope='function')
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope='function')
def registration_page(driver):
    return RegistrationPage(driver)


@pytest.fixture(scope='function')
def main_page(driver):
    return MainPage(driver)
