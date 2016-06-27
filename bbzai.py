from flask import Flask
from flask_socketio import SocketIO

import leancloud

leancloud.init("3searoQGvzcFv2N1S4mj0yKU-gzGzoHsz", "TYSYkoSOHab4uPqfV7Af7uRg")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    socketio.run(app)
