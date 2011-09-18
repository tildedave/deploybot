#!/usr/bin/python2.5

import unittest
from deploybot.environments import Environments
from mock import Mock

class TestEnvironments(unittest.TestCase):
    def test_lists_environments(self):
        envs = [{ "name" : "vagrant", "deploy_command" : "/bin/ls" }]

        config = Mock()
        config.get_environments = Mock(return_value=envs)
        env = Environments(config)

        self.assertEquals(1, len(env.list()))
