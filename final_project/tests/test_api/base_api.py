import pytest
from utils.builder import Builder
from mysql.builder import MySQLBuilder


class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client, api_client):
        self.mysql = mysql_client
        self.builder = Builder()
        self.mysql_builder = MySQLBuilder(mysql_client)
        self.client = api_client

    @pytest.fixture(scope='function')
    def new_user(self):
        new_user = self.mysql_builder.add_user()
        yield new_user
        self.mysql_builder.delete_user(new_user.id)
