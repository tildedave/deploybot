#!/usr/bin/python2.5

import simplejson as json
import subprocess

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

    def get_plan(self):
        return self.plan

    def get_build(self):
        return self.build

class Environments:
    
    def __init__(self, config):
        self.environments = [Environment(config, e["name"], 
                                         e["deploy_command"]) 
                             for e in config.get_environments()]

    def list(self):
        return self.environments

    def deploy(self, env, plan, build):
        for e in self.environments:
            if e.get_name() == env:
                e.deploy(plan, build)
                return



