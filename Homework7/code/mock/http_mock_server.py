import json
import os
import subprocess
import sys
import threading
import settings
from http.server import BaseHTTPRequestHandler, HTTPServer


repo_root = os.path.abspath(os.path.join(__file__, os.pardir))


class MockHandleRequests(BaseHTTPRequestHandler):
    users = None
    good_responses = json.dumps({'status': 'ok'}).encode()
    fail_responses = json.dumps({'status': 'fail'}).encode()
    timeout_responses = json.dumps({'status': 'timeout'}).encode()

    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self._set_headers(200)
            self.wfile.write(self.good_responses)
        elif self.path == '/users':
            self._set_headers(200)
            self.wfile.write(json.dumps(self.users).encode())
        else:
            self._set_headers(500)
            self.wfile.write(b'error')

    def do_POST(self):
        content_len = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_len).decode()
        if post_body:
            if self.headers['Content-Type'] == 'application/json':
                json_body = json.loads(post_body)
                if json_body:
                    self.users.append(json_body)
                    self._set_headers(200)
                    self.wfile.write(self.good_responses)
        else:
            self._set_headers(400)
            self.wfile.write(self.fail_responses)

    def do_PUT(self):
        content_len = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_len).decode()
        if post_body:
            if self.headers['Content-Type'] == 'application/json':
                json_body = json.loads(post_body)
                if json_body and len(self.users) != 0:
                    name = json_body['name']
                    surname = json_body['surname']
                    for d in self.users:
                        if name != d['name'] and surname != d['surname']:
                            d['surname'] = surname
                            d['name'] = name
                        elif name == d['name']:
                            d['surname'] = surname
                        elif surname == d['surname']:
                            d['name'] = name
                    self._set_headers(200)
                    self.wfile.write(self.good_responses)
        else:
            self._set_headers(400)
            self.wfile.write(self.fail_responses)

    def do_DELETE(self):
        content_len = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_len).decode()
        if post_body:
            if self.headers['Content-Type'] == 'application/json':
                json_body = json.loads(post_body)
                if json_body:
                    self.users.pop(self.users.index(json_body))
                    self._set_headers(200)
                    self.wfile.write(self.good_responses)
        else:
            self._set_headers(400)
            self.wfile.write(self.fail_responses)


class SimpleMockHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.stop_server = False
        self.handler = MockHandleRequests
        self.handler.users = []
        self.server = HTTPServer((self.host, self.port), self.handler)

    def start(self):
        self.server.allow_reuse_address = True
        th = threading.Thread(target=self.server.serve_forever)
        th.start()

        mock_path = os.path.join(repo_root, 'http_mock_server.py')

        mock_out = open('/tmp/mock_stdout.log', 'w')
        mock_err = open('/tmp/mock_stderr.log', 'w')
        subprocess.Popen([sys.executable, mock_path], stdout=mock_out, stderr=mock_err)

        return self.server

    def stop(self):
        self.server.server_close()
        self.server.shutdown()


if __name__ == '__main__':
    server = SimpleMockHTTPServer(settings.MOCK_HOST, settings.MOCK_PORT)
    server.start()
