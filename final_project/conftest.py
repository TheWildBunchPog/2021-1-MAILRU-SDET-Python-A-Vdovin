import os

import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from api.client import ApiClient
from mysql.client import MysqlClient
from ui.fixtures import *


def pytest_addoption(parser):
    parser.addoption('--url', default='http://0.0.0.0:8080')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='latest')
    parser.addoption('--selenoid', default='False')


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')
    selenoid = request.config.getoption('--selenoid')
    return {'url': url, 'browser': browser, 'version': version, 'selenoid': selenoid}


@pytest.fixture(scope='function')
def driver(config):
    url = config['url']
    browser = config['browser']
    version = config['version']
    selenoid = config['selenoid']
    if browser == 'chrome':
        if selenoid == 'False':
            manager = ChromeDriverManager(version=version)
            driver = webdriver.Chrome(executable_path=manager.install())
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


def pytest_configure(config):
    if not hasattr(config, "workerinput"):
        os.system('docker-compose up -d')
        while True:
            try:
                requests.get('http://0.0.0.0:8080')
                break
            except requests.exceptions.ConnectionError:
                pass


def pytest_unconfigure(config):
    if not hasattr(config, "workerinput"):
        os.system('docker-compose down')


@pytest.fixture(scope='function')
def api_client():
    return ApiClient()


@pytest.fixture(scope='session')
def mysql_client():
    mysql_client = MysqlClient(user='root', password='pass', db_name='test_app')
    mysql_client.connect()
    yield mysql_client
    mysql_client.connection.close()
