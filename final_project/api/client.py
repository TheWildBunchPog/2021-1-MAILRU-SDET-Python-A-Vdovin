import requests
import json
from urllib.parse import urljoin


class ApiClient:

    def __init__(self):
        self.base_url = 'http://0.0.0.0:8080'
        self.session = requests.Session()

    def _request(self, method, location, headers=None, data=None):
        url = urljoin(self.base_url, location)

        response = self.session.request(method, url, headers=headers, data=data)
        return response

    def login(self, username, password):
        location = 'login'

        data = {'username': username,
                'password': password,
                'submit': 'Login'}

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'http://127.0.0.1:8080/login'
        }

        response = self._request('POST', location, data=data, headers=headers)
        return response

    def logout(self):
        location = 'logout'

        response = self._request('GET', location)
        return response

    def add_user(self, username, password, email):
        location = 'api/add_user'

        data = {
            'username': username,
            'password': password,
            'email': email
        }
        data = json.dumps(data)

        response = self._request('POST', location, data=data)
        return response

    def registration(self, username, password, email):
        location = 'reg'

        data = {
            "username": username,
            "email": email,
            "password": password,
            "confirm": password,
            "term": "y",
            "submit": "Register"
        }

        response = self._request('POST', location, data=data)
        return response

    def delete_user(self, username):
        location = f'api/del_user/{username}'

        response = self._request('GET', location)
        return response

    def block_user(self, username):
        location = f'api/block_user/{username}'

        response = self._request('GET', location)
        return response

    def unblock_user(self, username):
        location = f'api/accept_user/{username}'

        response = self._request('GET', location)
        return response

    def status(self):
        location = 'status'

        response = self._request('GET', location)
        return response
