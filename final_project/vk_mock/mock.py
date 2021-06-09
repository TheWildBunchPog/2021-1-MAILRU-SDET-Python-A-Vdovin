import threading
from flask import Flask, request, jsonify

app = Flask(__name__)

VK_HOST, VK_PORT = 'mock_vk', 5555
users = {}


def run_app():
    server = threading.Thread(target=app.run, kwargs={
        'host': VK_HOST,
        'port': VK_PORT
    })

    server.start()
    return server


def shutdown_app():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_app()


@app.route('/vk_id/<username>')
def get_id_by_username(username):
    if username in users:
        return jsonify({'vk_id': users[username]}), 200
    else:
        return jsonify({}), 404


@app.route('/vk_id/add_user', methods=['POST'])
def post_user():
    name = request.form.get("name")
    id = request.form.get("id")
    users.update({name: id})
    return "OK"


if __name__ == '__main__':
    run_app()
