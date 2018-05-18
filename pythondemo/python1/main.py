#! /usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time     : 2018-05-17 11:21
# @Author   : Neo
# @Site     : 
# @File     : main.py
# @Software : PyCharm

# for i in range(0, 100):
#     print("1到%d,%s" % (i, "sss"))


class Hello:
    def __init__(self, name):
        self._name = name

    def say_hello(self):
        print("H%s" % self._name)


class Hi(Hello):
    def __init__(self, name):
        Hello.__init__(self, name)

    def say_hi(self):
        print("Hi%s" % self._name)


class HH:
    def sh(self):
        print("self")

# h = Hello('代码')
# h.say_hello()
#
# hi = Hi('apple')
# hi.say_hi()
