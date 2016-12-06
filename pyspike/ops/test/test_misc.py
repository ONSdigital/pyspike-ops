#!/usr/bin/env python
#  coding: UTF-8

import unittest

from pyspike.ops.misc import url_to_project

class PathTests(unittest.TestCase):

    def test_url_to_project(self):
        self.assertEqual(
            "pyspike-app",
            url_to_project("https://github.com/ONSdigital/pyspike-app.git")
        )
