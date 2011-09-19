#!/usr/bin/python2.5

import unittest
from mock import Mock
from deploybot.index import Index

class TextIndex(unittest.TestCase):

    def test_renders_unknown_environment(self):
        c = Mock()
        c.get_environment = Mock(return_value=None)

        index = Index(c)

        self.assertEquals("Unknown", index.render_environment())

    def test_renders_known_environment(self):
        c = Mock()
        c.get_environment = Mock(return_value="MegaProduction")

        index = Index(c)

        self.assertEquals("MegaProduction", index.render_environment())
