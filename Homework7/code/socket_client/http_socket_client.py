import json
import socket
import time


class HTTPSocketClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connection(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(0.1)
        started = False
        st = time.time()
        while time.time() - st <= 5:
            try:
                self.client.connect_ex((self.host, self.port))
                started = True
                break
            except ConnectionError:
                pass

        if not started:
            raise RuntimeError('App did not started in 5s!')

    def get(self, params):
        self.connection()
        request = f'GET {params} HTTP/1.1\r\nHost:{self.host}\r\n\r\n'
        self.client.send(request.encode())

        total_data = []

        while True:
            data = self.client.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                break

        data = ''.join(total_data).splitlines()
        return json.loads(data[-1])

    def post(self, params, data):
        self.connection()
        body_bytes = data.encode()
        request = f'POST {params} HTTP/1.1\r\nHost:{self.host}\r\nContent-Type: application/json\r\n' \
              f'Content-Length: {len(body_bytes)}\r\n\r\n{data}'
        self.client.send(request.encode())
        total_data = []

        while True:
            data = self.client.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                break
        self.client.close()
        data = ''.join(total_data).splitlines()
        return json.loads(data[-1])

    def put(self, params, data):
        self.connection()
        body_bytes = data.encode()
        request = f'PUT {params} HTTP/1.1\r\nHost:{self.host}\r\nContent-Type: application/json\r\n' \
              f'Content-Length: {len(body_bytes)}\r\n\r\n{data}'
        self.client.send(request.encode())
        total_data = []

        while True:
            data = self.client.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                break

        data = ''.join(total_data).splitlines()
        if len(data) != 0:
            return json.loads(data[-1])
        else:
            return None

    def delete(self, params, data):
        self.connection()
        body_bytes = data.encode()
        request = f'DELETE {params} HTTP/1.1\r\nHost:{self.host}\r\nContent-Type: application/json\r\n' \
              f'Content-Length: {len(body_bytes)}\r\n\r\n{data}'
        self.client.send(request.encode())
        total_data = []

        while True:
            data = self.client.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                break

        data = ''.join(total_data).splitlines()
        if len(data) != 0:
            return json.loads(data[-1])
        else:
            return None
