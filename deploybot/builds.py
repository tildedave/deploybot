#!/usr/bin/python2.5

import tornado.web

class BuildHandler(tornado.web.RequestHandler):
    
    def initialize(self, config, api):
        self.config = config
        self.api = api

    def get(self, plan):
        result = self.api.get("build/%s?expand=builds[0:5].build" % plan)
        self.write(result)
