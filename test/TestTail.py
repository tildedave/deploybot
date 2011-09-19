#!/usr/bin/python2.5

import unittest
from deploybot.tail import Tail
from mock import Mock

class TestTail(unittest.TestCase):

    def test_gets_log_from_config(self):
        config = Mock()
        config.get_deploy_log = Mock(return_value="/tmp/deploy.log")

        tail = Tail(config)
        tail.get_data = Mock()

        tail.get()
        
        tail.get_data.assert_called_with("/tmp/deploy.log")
        
