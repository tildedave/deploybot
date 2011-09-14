#!/usr/bin/python2.5

import unittest
from mock import Mock
from deploybot.index import Index

class TextIndex(unittest.TestCase):

    def test_renders_known_build(self):
        c = Mock()
        c.get_build = Mock(return_value=None)

        index = Index(c)

        self.assertEquals("Unknown", index.render_build())

    def test_renders_unknown_build(self):
        c = Mock()
        c.get_build = Mock(return_value="EXAMPLE-TRUNK-9000")

        index = Index(c)

        self.assertEquals("EXAMPLE-TRUNK-9000", index.render_build())


    def test_renders_known_plan(self):
        c = Mock()
        c.get_plan = Mock(return_value=None)

        index = Index(c)

        self.assertEquals("Unknown", index.render_plan())

    def test_renders_unknown_plan(self):
        c = Mock()
        c.get_plan = Mock(return_value="EXAMPLE-223-500")

        index = Index(c)

        self.assertEquals("EXAMPLE-223-500", index.render_plan())

