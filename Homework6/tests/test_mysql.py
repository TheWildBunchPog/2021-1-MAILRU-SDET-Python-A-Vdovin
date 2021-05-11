import pytest

from mysql.builder import MySQLBuilder
from mysql.script import *
from mysql.models import *


class MySQLBase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql = mysql_client
        self.mysql_builder = MySQLBuilder(mysql_client)


class TestMysql(MySQLBase):

    def test_total(self):
        # Общее количество запросов
        self.mysql_builder.add_total_requests(total_requests())
        total = self.mysql.session.query(TotalRequests).all()
        print(total)
        assert len(total) == 1

    def test_type_requests(self):
        # Общее количество запросов по типу
        self.mysql_builder.add_total_requests_by_type(total_requests_by_type())
        type_requests = self.mysql.session.query(TotalRequestsByType).all()
        print(len(type_requests))
        assert len(type_requests) == 5

    def test_most_frequent(self):
        # Топ 10 самых частых запросов
        self.mysql_builder.add_top_most_frequent_queries(top_most_frequent_queries())
        most_frequent = self.mysql.session.query(TopMostFrequentQueries).all()
        print(len(most_frequent))
        assert len(most_frequent) == 10

    def test_top_client_error(self):
        # Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой
        self.mysql_builder.add_top_requests_by_size_with_client_error(top_requests_by_size_with_client_error())
        top_client_error = self.mysql.session.query(TopRequestsBySizeWithClientError).all()
        print(len(top_client_error))
        assert len(top_client_error) == 5

    def test_top_server_error(self):
        # Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой
        self.mysql_builder.add_top_users_by_number_requests_with_server_error(top_users_by_number_requests_with_server_error())
        top_server_error = self.mysql.session.query(TopUsersByNumberRequestsWithServerError).all()
        print(len(top_server_error))
        assert len(top_server_error) == 5
