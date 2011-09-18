#!/usr/bin/python2.5

import tornado.web
import tornado.template
import subprocess
import simplejson as json

class DeployHandler(tornado.web.RequestHandler):

    def initialize(self, config, environments, loader):
        self.config = config
        self.environments = environments
        self.loader = loader

    def post(self):
        plan = self.get_argument("plan")
        build = self.get_argument("build")
        env = self.get_argument("env")

        self.environments.deploy(env, plan, build)
