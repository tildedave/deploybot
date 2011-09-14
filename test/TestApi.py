#!/usr/bin/python2.5

import unittest
from utils import ANY
from deploybot.api import BambooApi

from mock import Mock

class TestApi(unittest.TestCase):
    
    def test_correct_uri(self):
        api_root = "https://api.example.com"
        config = Mock()
        config.get_bamboo_api_root = Mock(return_value=api_root)

        api = BambooApi(config)
        api.request = Mock()
        result = api.get("/puppies?name=Lassie")

        expected_url = "https://api.example.com/puppies?name=Lassie&os_authType=basic"
        api.request.assert_called_with(url=expected_url,
                                       auth=ANY, headers=ANY)

    def test_correct_auth(self):
        config = Mock()
        config.get_bamboo_api_user = Mock(return_value="bamboo")
        config.get_bamboo_api_password = Mock(return_value="pikachu")

        api = BambooApi(config)
        api.request = Mock()
        result = api.get("/plans")

        api.request.assert_called_with(url=ANY, headers=ANY,
                                       auth=("bamboo", "pikachu"))

    def test_correct_headers(self):
        config = Mock()

        api = BambooApi(config)
        api.request = Mock()

        result = api.get("/builds")

        api.request.assert_called_with(url=ANY, auth=ANY,
                                       headers={
                "Content-Type": "application/json",
                "Accept" : "application/json"
        })
