#!/usr/bin/env python
#  coding: UTF-8

from collections import OrderedDict
import logging
import os.path
import subprocess
import sys

targets = OrderedDict([
    ("pyspike-app", [
        "https://github.com/ONSdigital/pyspike-lib.git",
        "https://github.com/ONSdigital/pyspike-app.git"
    ]),
])

def url_to_project(url):
    return os.path.splitext(os.path.basename(url))[0]

def project_to_namespace(proj):
    bits = proj.split("-")
    return bits[0] if len(bits) > 1 else None

def git_clone(locn, url, branch="master"):
    log = logging.getLogger("pyspike.git_clone")
    proc = subprocess.run(["git", "clone", url])
    if proc.returncode in (0, ):
        log.info("{0} succeeded.".format(" ".join(proc.args)))
        return True
    else:
        log.warning("Failed to clone {0}.".format(url))
        return False

def git_checkout(locn, project, branch="master"):
    log = logging.getLogger("pyspike.git_checkout")
    path = os.path.join(locn, project)
    os.chdir(path)
    try:
        proc = subprocess.run(["git", "checkout", branch])
        if proc.returncode in (0, ):
            log.info("{0} succeeded.".format(" ".join(proc.args)))
            return True
        else:
            log.warning("Failed to checkout {0}.".format(url))
            return False
    finally:
        os.chdir(locn)

def git_pull(locn, project, remote="origin", branch="master"):
    log = logging.getLogger("pyspike.git_pull")
    path = os.path.join(locn, project)
    os.chdir(path)
    try:
        proc = subprocess.run(["git", "pull", remote, branch])
        if proc.returncode in (0, ):
            log.info("{0}: {1} succeeded.".format(project, " ".join(proc.args)))
            return True
        else:
            log.warning("Failed to pull branch {0} for {1}.".format(branch, project))
            return False
    finally:
        os.chdir(locn)

def pip_install(locn, project):
    log = logging.getLogger("pyspike.pip_install")
    path = os.path.join(locn, project)
    os.chdir(path)
    try:
        pip = os.path.join(*os.path.split(sys.executable)[:-1], "pip")
        proc = subprocess.run([pip, "install", "."])
        if proc.returncode in (0, ):
            log.info("{0}: {1} succeeded.".format(project, " ".join(proc.args)))
            return True
        else:
            log.warning("Failed to install {0}.".format(project))
            return False
    finally:
        os.chdir(locn)

def pip_uninstall(locn, project):
    log = logging.getLogger("pyspike.pip_uninstall")
    path = os.path.join(locn, project)
    os.chdir(path)
    try:
        pip = os.path.join(*os.path.split(sys.executable)[:-1], "pip")
        proc = subprocess.run([pip, "uninstall", "-y", project])
        if proc.returncode in (0, ):
            log.info("{0}: {1} succeeded.".format(project, " ".join(proc.args)))
            return True
        else:
            log.warning("Failed to uninstall {0}.".format(project))
            return False
    finally:
        os.chdir(locn)
