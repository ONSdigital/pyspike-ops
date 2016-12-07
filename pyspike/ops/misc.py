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
    if proc.returncode in (0, ):
        log.info("{0} succeeded.".format(" ".join(proc.args)))
        return True
    else:
        log.warning("Failed to clone {0}.".format(url))
        return False

def git_checkout(locn, url, branch="master"):
    log = logging.getLogger("pyspike.git_clone")
    proc = subprocess.run(["git", "checkout", url])
    if proc.returncode in (0, ):
        log.info("{0} succeeded.".format(" ".join(proc.args)))
        return True
    else:
        log.warning("Failed to clone {0}.".format(url))
        return False

def git_pull(locn, project, branch="master"):
    log = logging.getLogger("pyspike.git_pull")
    path = os.path.join(locn, project)
    os.chdir(path)
    try:
        proc = subprocess.run(["git", "pull", "origin", branch])
        if proc.returncode in (0, ):
            log.info("{0}: {1} succeeded.".format(project, " ".join(proc.args)))
            return True
        else:
            log.warning("Failed to pull branch {0} for {1}.".format(branch, project))
            return False
    finally:
        os.chdir(locn)

