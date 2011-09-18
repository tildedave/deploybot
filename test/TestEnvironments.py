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
        config.get_deploy_log = Mock()

        envs = Environments(config)

        self.assertEquals(1, len(envs.list()))

    def test_gets_environment(self):
        envs = [ self.__env("vagrant", "/bin/ls") ]
        config = Mock()
        config.get_environments = Mock(return_value=envs) 

        envs = Environments(config)

        self.assertEquals("/bin/ls", envs.get("vagrant").get_deploy_command())
       

    def test_deploys_to_environments(self):
        envs = [ self.__env("vagrant", "/bin/ls") ]
        config = Mock()
        config.get_environments = Mock(return_value=envs)

        envs = Environments(config)
        env = envs.list()[0]
        env.deploy = Mock()

        envs.deploy("vagrant", "EXAMPLE-PLAN", "EXAMPLE-PLAN-56")

        env.deploy.assert_called_with("EXAMPLE-PLAN", "EXAMPLE-PLAN-56")

    def test_sets_build_on_deploy(self):
        config = Mock()
        config.get_deploy_log = Mock()

        env = Environment(config, "vagrant", "/bin/ls")
        env.execute = Mock()

        env.deploy("EXAMPLE-PLAN", "EXAMPLE-PLAN-56")

        self.assertEquals("EXAMPLE-PLAN-56", env.get_build())

    def test_sets_plan_on_deploy(self):
        config = Mock()
        config.get_deploy_log = Mock()

        env = Environment(config, "staging", "/usr/bin/perl")
        env.execute = Mock()

        env.deploy("EXAMPLE-PLAN", "EXAMPLE-PLAN-39")

        self.assertEquals("EXAMPLE-PLAN", env.get_plan())

    def test_deploys_with_expected_arguments(self):
        config = Mock()
        config.get_deploy_log = Mock(return_value="/tmp/deploy.log")

        env = Environment(config, "production", "wget")
        env.execute = Mock()

        env.deploy("EXAMPLE-PLAN", "EXAMPLE-PLAN-123")

        env.execute.assert_called_with("wget", "EXAMPLE-PLAN-123", 
                                            "/tmp/deploy.log")

