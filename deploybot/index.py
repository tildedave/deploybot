#!/usr/bin/python2.5

import tornado.web
import tornado.template

class Index:
    def __init__(self, config):
        self.config = config

    def display_string(self, s):
        if (s is None):
            return "Unknown"
        return s

    def render_build(self):
        build = self.config.get_build()
        return self.display_string(build)

    def render_plan(self):
        build = self.config.get_plan()
        return self.display_string(build)

class IndexHandler(tornado.web.RequestHandler):

    def initialize(self, config, loader):
        self.index = Index(config)
        self.loader = loader

    def get(self):
        t = self.loader.load("index.tpl")
        self.write(t.generate(build=self.index.render_build(),
                              plan=self.index.render_plan()))
