#!/usr/bin/python2.5

import unittest
from deploybot.environments import Environment
from deploybot.environments import Environments
from mock import Mock

class TestEnvironments(unittest.TestCase):
    
    def __dummy_fabric_data(self):
        return {
            "fabfile" : "awesome_fabfile.py"
            }

    def __env(self, name):
        return { "name" : name, "fabric" : self.__dummy_fabric_data() }

    def test_lists_environments(self):
        envs = [ self.__env("vagrant") ]

        config = Mock()
        config.get_environments = Mock(return_value=envs)
        config.get_deploy_log = Mock()

        envs = Environments(config)

        self.assertEquals(1, len(envs.list()))

    def test_gets_environment(self):
        envs = [ self.__env("vagrant") ]
        config = Mock()
        config.get_environments = Mock(return_value=envs) 

        envs = Environments(config)

        self.assertTrue(envs.get("vagrant") is not None)
       

    def test_deploys_to_environments(self):
        envs = [ self.__env("vagrant") ]
        config = Mock()
        config.get_environments = Mock(return_value=envs)

        envs = Environments(config)
        env = envs.list()[0]
        env.deploy = Mock()

        envs.deploy("vagrant", "EXAMPLE-PLAN", "EXAMPLE-PLAN-56")

        env.deploy.assert_called_with("EXAMPLE-PLAN", "EXAMPLE-PLAN-56")


    def test_sets_environment_on_deploy(self):
        envs = [ self.__env("production") ]
        config = Mock()
        config.get_environments = Mock(return_value=envs)
        config.set_environment = Mock()

        envs = Environments(config)
        env = envs.list()[0]
        env.deploy = Mock()

        envs.deploy("production", "EXAMPLE-PLAN", "EXAMPLE-PLAN-56")
        config.set_environment.assert_called_with("production")

    def test_sets_build_on_deploy(self):
        config = Mock()
        config.get_deploy_log = Mock()

        deployer = Mock()
        env = Environment(config, "vagrant", deployer)

        env.deploy("EXAMPLE-PLAN", "EXAMPLE-PLAN-56")

        self.assertEquals("EXAMPLE-PLAN-56", env.get_build())

    def test_sets_plan_on_deploy(self):
        config = Mock()
        config.get_deploy_log = Mock()

        deployer = Mock()
        env = Environment(config, "staging", deployer)

        env.deploy("EXAMPLE-PLAN", "EXAMPLE-PLAN-39")

        self.assertEquals("EXAMPLE-PLAN", env.get_plan())

    def test_deploys_with_expected_arguments(self):
        config = Mock()
        config.get_deploy_log = Mock(return_value="/tmp/deploy.log")

        env = Environment(config, "production", "wget")
        env.deployer = Mock()
        env.deployer.deploy = Mock()

        env.deploy("EXAMPLE-PLAN", "EXAMPLE-PLAN-123")

        env.deployer.deploy.assert_called_with("EXAMPLE-PLAN-123", "/tmp/deploy.log")





