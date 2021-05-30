import pytest

from mysql.client import MysqlClient


@pytest.fixture(scope='session')
def mysql_client():
    mysql_client = MysqlClient(user='root', password='pass', db_name='TEST_SQL')
    mysql_client.connect()
    yield mysql_client
    mysql_client.connection.close()


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        mysql_client = MysqlClient(user='root', password='pass', db_name='TEST_SQL')
        mysql_client.recreate_db()

        mysql_client.connect()
        mysql_client.create_total_requests()
        mysql_client.create_total_requests_by_type()
        mysql_client.create_top_most_frequent_queries()
        mysql_client.create_top_requests_by_size_with_client_error()
        mysql_client.create_top_users_by_number_requests_with_server_error()

        mysql_client.connection.close()
