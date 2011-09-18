#!/usr/bin/python2.5

import unittest
import ConfigParser

from deploybot.config import Config

class TestConfig(unittest.TestCase):

    def test_gets_deploy_command(self):
        json = """
{
   "deploy_command": "/bin/ls"
}
"""
        config = Config(json)

        self.assertEquals("/bin/ls", config.get_deploy_command())

    def test_gets_deploy_log(self):
        json = """
{
   "deploy_log" : "/tmp/deploy.log"
}
"""
        config = Config(json)

        self.assertEquals("/tmp/deploy.log", config.get_deploy_log())

    def test_gets_bamboo_api_root(self):
        json = """
{
   "bamboo" : {
      "api_root" : "http://api.example.com/kittens"
   }
}
"""
        config = Config(json)

        self.assertEquals("http://api.example.com/kittens", 
                          config.get_bamboo_api_root())

    def test_gets_bamboo_credentials(self):
        json = """
{
  "bamboo" : {
    "user": "bamboouser",
    "password": "ilovebees"
  }
}
"""        
        config = Config(json)
        
        self.assertEquals("bamboouser", config.get_bamboo_api_user())
        self.assertEquals("ilovebees", config.get_bamboo_api_password())
