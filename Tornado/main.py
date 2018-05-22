#! /usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time     : 2018-05-22 17:04
# @Author   : Neo
# @Site     : 
# @File     : main.py
# @Software : PyCharm

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options

from tornado.options import define, options

define("port", default=8000, type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        arg = self.get_argument('q', 'hello')
        self.write(arg+' world!')


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

    # http: // localhost: 8000 /?q = Neo
    # import tornado.httpserver
    # import tornado.ioloop
    # import tornado.options
    # import tornado.web
    #
    # from tornado.options import define, options
    #
    # define("port", default=8000, help="run on the given port", type=int)
    #
    #
    # class IndexHandler(tornado.web.RequestHandler):
    #     def get(self):
    #         greeting = self.get_argument('greeting', 'Hello')
    #         self.write(greeting + ', welcome you to read: www.itdiffer.com')
    #
    #
    # if __name__ == "__main__":
    #     tornado.options.parse_command_line()
    #     app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    #     http_server = tornado.httpserver.HTTPServer(app)
    #     http_server.listen(options.port)
    #     tornado.ioloop.IOLoop.instance().start()