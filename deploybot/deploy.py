#!/usr/bin/python2.5

import tornado.web
import tornado.template
import subprocess
import simplejson as json

class DeployHandler(tornado.web.RequestHandler):

    def initialize(self, config, loader):
        self.config = config
        self.loader = loader
        self.deployer = Deployer(config)

    def post(self):
        plan = self.get_argument("plan")
        build = self.get_argument("build")
        self.deployer.deploy(plan, build)

class Deployer:

    def __init__(self, config):
        self.config = config

    def deploy(self, plan, build):
        deploy_cmd = self.config.get_deploy_command()
        deploy_log = self.config.get_deploy_log()

        self.config.set_plan(plan)
        self.config.set_build(build)

        return self.execute(deploy_cmd, build, deploy_log)

    def execute(self, cmd, build, log):
        print "Launching %s, outputting to %s" % (cmd, log)

        logfile = file(log, "w")
        p = subprocess.Popen([ cmd, build ], 
                             stdout=logfile,
                             stderr=logfile,
                             close_fds=True)
        p.communicate()
        return cmd
