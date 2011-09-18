#!/usr/bin/python2.5

import unittest
from deploybot.environments import Environment
from deploybot.environments import Environments
from mock import Mock

class TestEnvironments(unittest.TestCase):
    
    def __env(self, name, deploy_command):
        return { "name" : name, "deploy_command" : deploy_command }

    def test_lists_environments(self):
        envs = [ self.__env("vagrant", "/bin/ls") ]

        config = Mock()
        config.get_environments = Mock(return_value=envs)
        env = Environments(config)

        self.assertEquals(1, len(env.list()))

    def test_sets_build_on_deploy(self):
        env = Environment("vagrant", "/bin/ls")

        env.deploy("EXAMPLE-PLAN", "EXAMPLE-PLAN-56")

        self.assertEquals("EXAMPLE-PLAN-56", env.get_build())

    def test_sets_plan_on_deploy(self):
        env = Environment("staging", "/usr/bin/perl")
        env.deploy("EXAMPLE-PLAN", "EXAMPLE-PLAN-39")

        self.assertEquals("EXAMPLE-PLAN", env.get_plan())
