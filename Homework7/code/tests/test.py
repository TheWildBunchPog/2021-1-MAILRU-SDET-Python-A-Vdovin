import json
import pytest
import settings
from mock.http_mock_server import SimpleMockHTTPServer
from socket_client.http_socket_client import HTTPSocketClient
from app import app
from utils.builder import Builder


class TestMockServer:

    @pytest.fixture(scope='function')
    def mock(self):
        server = SimpleMockHTTPServer(settings.MOCK_HOST, settings.MOCK_PORT)
        server.start()
        yield server
        server.stop()

    @pytest.fixture(scope='session')
    def app(self):
        application = app.run_app(settings.APP_HOST, settings.APP_PORT)
        yield application
        socket = HTTPSocketClient(settings.APP_HOST, settings.APP_PORT)
        socket.get('/shutdown')

    @pytest.fixture(scope='session')
    def socket(self):
        socket = HTTPSocketClient(settings.APP_HOST, settings.APP_PORT)
        yield socket

    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        self.builder = Builder()

    def test_mock_work(self, socket, mock, app):
        resp = socket.get('/')
        assert resp['status'] == 'ok'

    def test_get_user(self, socket, mock, app):
        new_user = {"name": self.builder.first_name(), "surname": self.builder.last_name()}
        user = json.dumps(new_user)
        resp = socket.post('/users/add', user)
        assert resp['status'] == 'ok'
        users = socket.get('/users')
        assert new_user == users[0]

    def test_add_user(self, socket, mock, app):
        new_user = {"name": self.builder.first_name(), "surname": self.builder.last_name()}
        user = json.dumps(new_user)
        resp = socket.post('/users/add', user)
        assert resp['status'] == 'ok'
        users = socket.get('/users')
        assert users[0]['name'] == new_user['name'] and users[0]['surname'] == new_user['surname']

    def test_update_user(self, socket, mock, app):
        new_user_1 = {"name": self.builder.first_name(), "surname": self.builder.last_name()}
        user = json.dumps(new_user_1)
        resp = socket.post('/users/add', user)
        assert resp['status'] == 'ok'
        new_user_2 = {"name": self.builder.first_name(), "surname": self.builder.last_name()}
        user = json.dumps(new_user_2)
        resp = socket.put('/users/update', user)
        assert resp['status'] == 'ok'
        users = socket.get('/users')
        assert users[0]['name'] == new_user_2['name'] and users[0]['surname'] == new_user_2['surname']

    def test_delete_user(self, socket, mock, app):
        new_user_1 = {"name": self.builder.first_name(), "surname": self.builder.last_name()}
        user_1 = json.dumps(new_user_1)
        resp_1 = socket.post('/users/add', user_1)
        assert resp_1['status'] == 'ok'
        new_user_2 = {"name": self.builder.first_name(), "surname": self.builder.last_name()}
        user_2 = json.dumps(new_user_2)
        resp_2 = socket.post('/users/add', user_2)
        assert resp_2['status'] == 'ok'
        new_user_3 = {"name": self.builder.first_name(), "surname": self.builder.last_name()}
        user_3 = json.dumps(new_user_3)
        resp_3 = socket.post('/users/add', user_3)
        assert resp_3['status'] == 'ok'
        resp_delete = socket.delete('/users/delete', user_3)
        assert resp_delete['status'] == 'ok'
        users = socket.get('/users')
        assert new_user_3 not in users
