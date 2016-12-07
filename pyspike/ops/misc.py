#!/usr/bin/env python
#  coding: UTF-8

from collections import OrderedDict
import logging
import os.path
import subprocess

targets = OrderedDict([
    ("pyspike-app", [
        "https://github.com/ONSdigital/pyspike-lib.git",
        "https://github.com/ONSdigital/pyspike-app.git"
    ]),
])

def url_to_project(url):
    return os.path.splitext(os.path.basename(url))[0]

def git_clone(locn, url, branch="master"):
    log = logging.getLogger("pyspike.git_clone")
    proc = subprocess.run(["git", "clone", url])
    if proc.returncode in (128, ):
        log.warning("Failed to clone {0}.".format(url))
        return False
    else:
        log.info("{0} succeeded.".format(" ".join(proc.args)))
        return True

def git_checkout(locn, url, branch="master"):
    log = logging.getLogger("pyspike.git_clone")
    proc = subprocess.run(["git", "checkout", url])
    if proc.returncode in (128, ):
        log.warning("Failed to clone {0}.".format(url))
        return False
    else:
        log.info("{0} succeeded.".format(" ".join(proc.args)))
        return True

def git_pull(locn, project, branch="master"):
    log = logging.getLogger("pyspike.git_pull")
    path = os.path.join(locn, project)
    os.chdir(path)
    try:
        proc = subprocess.run(["git", "pull", "origin", branch])
        if proc.returncode in (128, ):
            log.warning("Failed to pull branch {0}.".format(branch))
            return False
        else:
            log.info("{0} succeeded.".format(" ".join(proc.args)))
            return True
    finally:
        os.chdir(locn)

