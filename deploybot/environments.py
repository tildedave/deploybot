#!/usr/bin/python2.5

import simplejson as json

class Environment:
    def __init__(self, name, deploy_command):
        self.name = name
        self.deploy_command = deploy_command
        self.build = None
        self.plan = None

    def deploy(self, plan, build):
        self.build = build
        self.plan = plan

    def get_plan(self):
        return self.plan

    def get_build(self):
        return self.build

class Environments:
    
    def __init__(self, config):
        env_list = config.get_environments()
        self.environments = [Environment(e["name"], e["deploy_command"]) 
                             for e in env_list]

    def list(self):
        return self.environments





