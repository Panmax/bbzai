# coding: utf-8

import random
import json

from flask import Flask, render_template, redirect, request
from flask_login import LoginManager, login_required, login_user, current_user

from leancloud import Query, User as LUser

from models.user import _User, WaitUser, PlayingUser

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    try:
        user = Query(_User).get(user_id)
    except Exception, e:
        print e
    else:
        return user

app = Flask(__name__)

app.secret_key = 'hard to guess string'
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app)


def random_username():
    name = ''
    for _ in range(6):
        i = random.randint(1, 9)
        name += str(i)
    return name


@app.route('/login')
def login():
    username = None
    while True:
        username = random_username()
        try:
            user = LUser()
            user.set_username(username)
            user.set_password('123456')
            user.sign_up()
        except:
            pass
        else:
            break
    user = Query(_User).equal_to('username', username).first()
    login_user(user, remember=True)
    return redirect(request.args.get('next', '/'))


@app.route('/')
@login_required
def index():
    return render_template('index.html')


@app.route('/j/ready', methods=['POST'])
@login_required
def j_ready():
    wait_users = Query(WaitUser).not_equal_to('user', current_user).find()
    if not wait_users:
        wait_users = Query(WaitUser).equal_to('user', current_user).find()
        if not wait_users:
            wait_user = WaitUser()
            wait_user.set('user', current_user)
            wait_user.save()
    else:
        wait_user = wait_users[0]
        pu = PlayingUser()
        pu.set('user1', current_user)
        pu.set('user2', wait_user.user)
        pu.save()
        wait_user.destroy()
    return 'ok'


@app.route('/j/action', methods=['POST'])
@login_required
def j_action():
    data = request.form
    action = data.get('action')
    q1 = Query(PlayingUser).equal_to('user1', current_user)
    q2 = Query(PlayingUser).equal_to('user2', current_user)
    playing = Query(PlayingUser).or_(q1, q2).first()
    print playing
    around = playing.around
    actions = playing.actions
    action_map = actions[around-1]
    if current_user.username not in action_map:
        action_map[current_user.username] = action
        if len(action_map) == 2:
            playing.around += 1
            actions.append({})
        playing.actions = actions
        playing.save()
    return 'ok'


@app.route('/j/hello')
@login_required
def j_hello():
    result = {
        'playing': False
    }
    q1 = Query(PlayingUser).equal_to('user1', current_user)
    q2 = Query(PlayingUser).equal_to('user2', current_user)
    try:
        playing = Query(PlayingUser).or_(q1, q2).first()
        result['playing'] = True
        actions = playing.actions
        result['actions'] = actions[:-1]
    except:
        pass

    return json.dumps(result)
