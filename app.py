# coding: utf-8

from flask import Flask, render_template
from flask_sockets import Sockets

app = Flask(__name__)
sockets = Sockets(app)


@app.route('/')
def index():
    return render_template('test.html')


@sockets.route('/echo')
def echo_socket(ws):
    print 'aaaaa'
    while True:
        message = ws.receive()
        ws.send(message)
