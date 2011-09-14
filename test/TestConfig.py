#!/usr/bin/python2.5

import unittest
import ConfigParser

from deploybot.config import Config

class TestConfig(unittest.TestCase):

    def test_gets_deploy_command(self):
        parser = ConfigParser.RawConfigParser()
        parser.set("DEFAULT", "deploy_command", "/bin/ls")
        
        config = Config(parser)

        self.assertEquals("/bin/ls", config.get_deploy_command())

    def test_gets_deploy_log(self):
        parser = ConfigParser.RawConfigParser()
        parser.set("DEFAULT", "deploy_log", "/tmp/deploy.log")

        config = Config(parser)

        self.assertEquals("/tmp/deploy.log", config.get_deploy_log())

    def test_gets_bamboo_api_root(self):
        parser = ConfigParser.RawConfigParser()
        parser.add_section("Bamboo")
        parser.set("Bamboo", "api_root", 
                         "http://api.example.com/kittens")

        config = Config(parser)

        self.assertEquals("http://api.example.com/kittens", 
                          config.get_bamboo_api_root())

    def test_gets_bamboo_credentials(self):
        parser = ConfigParser.RawConfigParser()
        parser.add_section("Bamboo")
        parser.set("Bamboo", "user", "bamboouser")
        parser.set("Bamboo", "password", "ilovebees")
        
        config = Config(parser)
        
        self.assertEquals("bamboouser", config.get_bamboo_api_user())
        self.assertEquals("ilovebees", config.get_bamboo_api_password())
