#!/usr/bin/env python
#  coding: UTF-8

import unittest

from pyspike.ops.misc import project_to_namespace
from pyspike.ops.misc import url_to_project

class PathTests(unittest.TestCase):

    def test_url_to_project(self):
        self.assertEqual(
            "pyspike-app",
            url_to_project("https://github.com/ONSdigital/pyspike-app.git")
        )

    def test_simple_project_to_namespace(self):
        self.assertEqual(
            "pyspike",
            project_to_namespace("pyspike-app")
        )

    def test_deep_project_to_namespace(self):
        self.assertEqual(
            "pyspike",
            project_to_namespace("pyspike-plugins-common")
        )

    def test_bad_project_to_namespace(self):
        for proj in ("nonamespace", "no_hyphen"):
            with self.subTest(arg=proj):
                self.assertIsNone(project_to_namespace(proj))
