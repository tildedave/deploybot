#!/usr/bin/python2.5

import simplejson as json
import subprocess
import tornado.web

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
    def __init__(self, config, name, deploy_command):
        self.config = config
        self.name = name
        self.deploy_command = deploy_command
        self.build = None
        self.plan = None

    def deploy(self, plan, build):
        self.build = build
        self.plan = plan

        self.execute(self.deploy_command, build, 
                     self.config.get_deploy_log())

    def execute(self, cmd, build, log):
        print "Launching %s, outputting to %s" % (cmd, log)

        logfile = file(log, "w")
        p = subprocess.Popen([ cmd, build ], 
                             stdout=logfile,
                             stderr=logfile,
                             close_fds=True)
        p.communicate()
        return cmd

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
        self.environments = [Environment(config, e["name"], 
                                         e["deploy_command"]) 
                             for e in config.get_environments()]

    def list(self):
        return self.environments

    def deploy(self, env, plan, build):
        e = self.get(env)
        if e: 
            self.config.set_environment(env)
            e.deploy(plan, build)
    
    def get(self, env):
        for e in self.environments:
            if e.get_name() == env:
                return e

        return None

