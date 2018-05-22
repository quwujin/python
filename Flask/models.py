#! /usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time     : 2018-05-22 15:52
# @Author   : Neo
# @Site     : 
# @File     : models.py
# @Software : PyCharm


class User(object):
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name