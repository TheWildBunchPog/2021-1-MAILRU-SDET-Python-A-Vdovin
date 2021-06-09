import pytest
from utils.builder import Builder
from mysql.builder import MySQLBuilder
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from ui.pages.registration_page import RegistrationPage


class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request, mysql_client):
        self.driver = driver
        self.config = config
        self.builder = Builder()
        self.mysql_builder = MySQLBuilder(mysql_client)
        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.login_page: LoginPage = request.getfixturevalue('login_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.registration_page: RegistrationPage = request.getfixturevalue('registration_page')

    @pytest.fixture(scope='function')
    def new_user(self):
        new_user = self.mysql_builder.add_user()
        yield new_user
        self.mysql_builder.delete_user(new_user.id)

    @pytest.fixture(scope='function')
    def auto(self):
        new_user = self.mysql_builder.add_user()
        yield self.login_page.login(new_user.username, new_user.password)
        self.mysql_builder.delete_user(new_user.id)
