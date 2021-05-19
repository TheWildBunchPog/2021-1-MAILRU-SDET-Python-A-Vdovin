import json
import pytest
import settings
from mock.http_mock_server import SimpleMockHTTPServer
from socket_client.http_socket_client import HTTPSocketClient
from app import app


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

    def test_mock_work(self, socket, mock, app):
        resp = socket.get('/')
        assert resp['status'] == 'ok'

    def test_get_user(self, socket, mock, app):
        new_user = {"name": "Alex", "surname": "Ivanov"}
        user = json.dumps({"name": "Alex", "surname": "Ivanov"})
        resp = socket.post('/users/add', user)
        assert resp['status'] == 'ok'
        users = socket.get('/users')
        assert new_user == users[0]

    def test_add_user(self, socket, mock, app):
        user = json.dumps({"name": "Anton", "surname": "Kozlov"})
        resp = socket.post('/users/add', user)
        assert resp['status'] == 'ok'
        users = socket.get('/users')
        assert users[0]['name'] == 'Anton' and users[0]['surname'] == 'Kozlov'

    def test_update_user(self, socket, mock, app):
        user = json.dumps({"name": "Anton", "surname": "Popov"})
        resp = socket.post('/users/add', user)
        assert resp['status'] == 'ok'
        user = json.dumps({"name": "Artur", "surname": "Petrov"})
        resp = socket.put('/users/update', user)
        assert resp['status'] == 'ok'
        users = socket.get('/users')
        assert users[0]['name'] == 'Artur' and users[0]['surname'] == 'Petrov'

    def test_delete_user(self, socket, mock, app):
        user1 = json.dumps({"name": "Anton", "surname": "Popov"})
        resp1 = socket.post('/users/add', user1)
        assert resp1['status'] == 'ok'
        user2 = json.dumps({"name": "Alex", "surname": "Ivanov"})
        resp2 = socket.post('/users/add', user2)
        assert resp2['status'] == 'ok'
        user3 = json.dumps({"name": "Artur", "surname": "Petrov"})
        resp3 = socket.post('/users/add', user3)
        assert resp3['status'] == 'ok'
        resp_delete = socket.delete('/users/delete', user3)
        assert resp_delete['status'] == 'ok'
        users = socket.get('/users')
        assert {"name": "Artur", "surname": "Petrov"} not in users
