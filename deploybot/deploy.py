#!/usr/bin/python2.5

import tornado.web
import tornado.template

class DeployHandler(tornado.web.RequestHandler):

    def initialize(self, config, environments, loader):
        self.config = config
        self.environments = environments
        self.loader = loader

    def post(self):
        plan = self.get_argument("plan")
        build = self.get_argument("build")
        env = self.get_argument("env")

        result = self.environments.deploy(env, plan, build)

        response = {}
        response["success"] = (result == 0)
        self.write(response)

