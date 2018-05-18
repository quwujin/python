#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
import base64
import time
import random

app = Flask(__name__)

users = {"magigo": ["123456"]}


def gen_token(uid):
    token = base64.b64encode(':'.join([str(uid), str(random.random()), str(time.time() + 7200)]))
    users[uid].append(token)
    return token


def verify_token(token):
    _token = base64.b64decode(token)
    if not users.get(_token.split(',')[0])[-1] == token:
        return -1
    if float(_token.split(':')[-1]) >= time.time():
        return 1
    else:
        return 0


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login', methods=['POST', 'GET'])
def login():
    uid, pw = base64.b64decode(request.headers['Authorization'].split(' ')[-1]).split(':')
    if users.get(uid)[0] == pw:
        return gen_token(uid)
    else:
        return 'error'


@app.route('/test1', methods=['POST', 'GET'])
def test():
    token = request.args.get('token')
    if verify_token(token) == 1:
        return 'data'
    else:
        return 'error'


if __name__ == '__main__':
    app.run()
