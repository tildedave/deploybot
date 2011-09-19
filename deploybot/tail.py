#!/usr/bin/python2.5

import simplejson as json
import tornado.web

class TailHandler(tornado.web.RequestHandler):
    def initialize(self, config):
        self.tail = Tail(config)

    def get(self):
        self.write(self.tail.get())


class Tail:

    def __init__(self, config):
        self.config = config

    def get(self):
        return self.get_data(self.config.get_deploy_log())

    def get_data(self, f):
        return open(f).read()
