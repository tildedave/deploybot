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

    def render_environment(self):
        build = self.config.get_environment()
        return self.display_string(build)

    def get_environments(self):
        return self.config.get_environments()

class IndexHandler(tornado.web.RequestHandler):

    def initialize(self, config, loader):
        self.index = Index(config)
        self.loader = loader

    def get(self):
        t = self.loader.load("index.tpl")
        env = self.index.render_environment()
        self.write(t.generate(env=env,
                              environments=self.index.get_environments()))
