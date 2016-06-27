# coding: utf-8

from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('test.html')


@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))
