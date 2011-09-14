#!/usr/bin/python2.5

import unittest
from mock import Mock
from deploybot.deploy import Deployer
from deploybot.config import Config

class TestDeployer(unittest.TestCase):
    
    def test_sets_plan(self):
        config = Config(Mock())
        deployer = Deployer(config)
        deployer.execute = Mock()
        
        deployer.deploy("EXAMPLE-TRUNK", "EXAMPLE-TRUNK-5444")

        self.assertEquals("EXAMPLE-TRUNK", config.get_plan())
    
    def test_sets_build(self):
        config = Config(Mock())
        deployer = Deployer(config)
        deployer.execute = Mock()
        
        deployer.deploy("EXAMPLE-2026", "EXAMPLE-2026-45")

        self.assertEquals("EXAMPLE-2026-45", config.get_build())

    def test_runs_deploy_command(self):
        config = Mock()
        config.get_deploy_command = Mock(return_value="/bin/deploy.sh")
        config.get_deploy_log = Mock(return_value="/tmp/deploy.log")
        deployer = Deployer(config)
        deployer.execute = Mock()

        deployer.deploy("EXAMPLE-TRUNK", "EXAMPLE-TRUNK-5444")

        deployer.execute.assert_called_with("/bin/deploy.sh", "EXAMPLE-TRUNK-5444", 
                                            "/tmp/deploy.log")




