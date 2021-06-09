from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from api.client import ApiClient
from mysql.client import MysqlClient
from ui.fixtures import *


def pytest_addoption(parser):
    parser.addoption('--url', default='http://0.0.0.0:8080')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--selenoid', default='False')


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    selenoid = request.config.getoption('--selenoid')
    return {'url': url, 'browser': browser, 'selenoid': selenoid}


@pytest.fixture(scope='function')
def driver(config):
    url = config['url']
    browser = config['browser']
    selenoid = config['selenoid']
    if browser == 'chrome':
        if selenoid == 'False':
            driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
        else:
            url = 'http://application:8080'
            caps = {'browserName': browser,
                    'version': '91.0',
                    'sessionTimeout': '2m'}

            driver = webdriver.Remote(selenoid + '/wd/hub', desired_capabilities=caps)
    else:
        raise UnsupportedBrowserException(f' Unsupported browser {browser}')
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def api_client():
    return ApiClient()


@pytest.fixture(scope='session')
def mysql_client():
    mysql_client = MysqlClient(user='root', password='pass', db_name='test_app')
    mysql_client.connect()
    yield mysql_client
    mysql_client.connection.close()
