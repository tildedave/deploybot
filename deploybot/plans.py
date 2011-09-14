#!/usr/bin/python2.5

import tornado.web

class PlanHandler(tornado.web.RequestHandler):
    
    def initialize(self, config, api):
        self.config = config
        self.api = api


    def get(self):
        project = self.config.get_bamboo_project()
        url = "project/%s?expand=plans" % project
        self.write(self.api.get(url))
