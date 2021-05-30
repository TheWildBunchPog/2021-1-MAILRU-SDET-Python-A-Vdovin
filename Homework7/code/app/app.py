import threading
from flask import Flask, request, jsonify
import settings
from socket_client.http_socket_client import HTTPSocketClient

app = Flask(__name__)
sock = None
app_data = {}


def run_app(host, port):
    server = threading.Thread(target=app.run, kwargs={
        'host': host,
        'port': port
    })
    server.start()

    return server


def shutdown_app():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


def client():
    sock = HTTPSocketClient(settings.MOCK_HOST, settings.MOCK_PORT)
    return sock


@app.route('/shutdown')
def shutdown():
    shutdown_app()
    return jsonify({'status': 'fail'}), 500


@app.route('/')
def mock_work():
    try:
        mock_response = client().get('/')
    except ConnectionRefusedError as e:
        return jsonify({"status": "fail"}), 500
    if mock_response['status'] == 'ok':
        return jsonify({"status": "ok"}), 200
    else :
        return jsonify({"status": "fail"}), 400


@app.route('/users/add', methods=["POST"])
def add_user():
    mock_response = client().post('/', request.data.decode())
    if mock_response['status'] == 'ok':
        return jsonify({"status": "ok"}), 200
    else:
        return jsonify({"status": "fail"}), 400


@app.route('/users/update', methods=["PUT"])
def update_user():
    mock_response = client().put('/', request.data.decode())
    if mock_response and mock_response['status'] == 'ok':
        return jsonify({"status": "ok"}), 200
    else:
        return jsonify({"status": "fail"}), 400


@app.route('/users/delete', methods=["DELETE"])
def delete_user():
    mock_response = client().delete('/', request.data.decode())
    if mock_response and mock_response['status'] == 'ok':
        return jsonify({"status": "ok"}), 200
    else:
        return jsonify({"status": "fail"}), 400


@app.route('/users', methods=["GET"])
def get_users():
    mock_response = client().get('/users')
    if mock_response:
        return jsonify(mock_response), 200
    else:
        return jsonify({"status": "fail"}), 400


if __name__ == '__main__':
    run_app(settings.APP_HOST, settings.APP_PORT)
