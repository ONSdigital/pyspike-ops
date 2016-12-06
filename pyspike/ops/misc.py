#!/usr/bin/env python
#  coding: UTF-8

from collections import OrderedDict
import os.path

targets = OrderedDict([
    ("pyspike-app", [
        "https://github.com/ONSdigital/pyspike-lib.git",
        "https://github.com/ONSdigital/pyspike-app.git"
    ]),
])

def url_to_project(url):
    return os.path.splitext(os.path.basename(url))[0]

def git_clone(locn, url, branch="master"):
    pass

def git_checkout(locn, url, branch="master"):
    pass
