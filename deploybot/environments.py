#!/usr/bin/python2.5

import simplejson as json
import tornado.web

from fabric_deployer import FabricDeployer

class EnvironmentHandler(tornado.web.RequestHandler):
    
    def initialize(self, config, environments):
        self.config = config
        self.envs = environments

    def get(self, env):
        if len(env) is 0:
            self.write(json.dumps([e.render() for e in self.envs.list()]))
            return

        e = self.envs.get(env)
        self.write(json.dumps(e.render()))

class Environment:
    def __init__(self, config, name, deployer):
        self.config = config
        self.name = name
        self.deployer = deployer
        self.build = None
        self.plan = None

    def deploy(self, plan, build):
        self.build = build
        self.plan = plan

        return self.deployer.deploy(build, self.config.get_deploy_log())

    def get_name(self):
        return self.name

    def get_deploy_command(self):
        return self.deploy_command

    def get_plan(self):
        return self.plan

    def get_build(self):
        return self.build

    def render(self):
        return {
            "name" : self.name,
            "plan" : self.render_status(self.plan),
            "build" : self.render_status(self.build)
            }

    def render_status(self, obj):
        if obj is None:
            return "Unknown"

        return obj

class Environments:

    def __init__(self, config):
        self.config = config
        self.environments = [Environment(config, 
                                         e["name"], 
                                         FabricDeployer(e["fabric"]))
                             for e in config.get_environments()]

    def list(self):
        return self.environments

    def deploy(self, env, plan, build):
        e = self.get(env)
        if e: 
            self.config.set_environment(env)
            return e.deploy(plan, build)

        return None
    
    def get(self, env):
        for e in self.environments:
            if e.get_name() == env:
                return e

        return None

