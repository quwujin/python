#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, url_for, render_template, flash
import base64
import time
import random
from models import User

app = Flask(__name__)
app.secret_key = '123'
# users = {"magigo": ["123456"]}


# def gen_token(uid):
#     token = base64.b64encode(':'.join([str(uid), str(random.random()), str(time.time() + 7200)]))
#     users[uid].append(token)
#     return token
#
#
# def verify_token(token):
#     _token = base64.b64decode(token)
#     if not users.get(_token.split(',')[0])[-1] == token:
#         return -1
#     if float(_token.split(':')[-1]) >= time.time():
#         return 1
#     else:
#         return 0


# @app.route('/')
# def hello_world():
#     return 'Hello World!'


# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     uid, pw = base64.b64decode(request.headers['Authorization'].split(' ')[-1]).split(':')
#     if users.get(uid)[0] == pw:
#         return gen_token(uid)
#     else:
#         return 'error'


@app.route('/test1', methods=['POST', 'GET'])
def test():
    token = request.args.get('token')
    if verify_token(token) == 1:
        return 'data'
    else:
        return 'error'


@app.route('/user/<id>')
def user_id(id):
    return 'hello_user'+id


# @app.route('/query_user')
# def query_user():
#     id1 = request.args.get('id')
#     return 'query user'+id1


# 反向路由
@app.route('/query_url')
def query_url():
    return 'query url:'+url_for('query_user')


@app.route('/')
def hello_world():
    content = "Hello world Neo1"
    return render_template("index.html", content=content)


# 将对象传入前端显示
@app.route('/user')
def user_index():
    user = User(1, 'Neo')
    return render_template("user_index.html", user=user)


# 在前端进行判断对象
@app.route('/query_user/<user_id>')
def query_user(user_id):
    user = None
    if int(user_id) == 1:
        user = User(1, "Neo")
    return render_template("user_id.html", user=user)


# 循环语句
@app.route('/users')
def user_list():
    users = []
    for i in range(1, 11):
        user = User(1, "Neo"+str(i))
        users.append(user)
    return render_template("user_list.html", users=users)


# 页面继承
@app.route('/one')
def one_base():
    return render_template("base_one.html")


@app.route('/two')
def two_base():
    return render_template("base_two.html")


# 异常消息提示
@app.route('/login', methods=['POST'])
def login():
    form = request.form
    username = form.get('username')
    password = form.get('password')

    if not username:
        flash("please input username")
        return render_template("index.html")
    if not password:
        flash("please input password")
        return render_template("index.html")

    if username == "Neo" and password == '123456':
        flash("login success")
        return render_template("index.html")
    else:
        flash("user or password is wrong")
        return render_template("index.html")


# 捕获404错误 主动抛异常引用abort  else: abort(404)
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


if __name__ == '__main__':
    app.run()
