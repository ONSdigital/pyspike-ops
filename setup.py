#!/usr/bin/env python
# encoding: UTF-8

import ast
from setuptools import setup
import os.path

try:
    import pyspike.ops.__version__ as version
except ImportError:
    # Pip evals this file prior to running setup.
    # This causes ImportError in a fresh virtualenv.
    version = str(ast.literal_eval(
                open(os.path.join(os.path.dirname(__file__),
                "pyspike", "ops", "__init__.py"),
                'r').read().split("=")[-1].strip()))

__doc__ = open(os.path.join(os.path.dirname(__file__), "README.rst"),
               "r").read()

setup(
    name="pyspike-ops",
    version=version,
    description="PoC for container deployment of Python3 apps. Ops package.",
    author="D Haynes",
    author_email="tundish@thuswise.org",
    url="https://github.com/ONSdigital/pyspike-ops",
    long_description=__doc__,
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License"
    ],
    namespace_packages=["pyspike"],
    packages=[
        "pyspike.ops",
        "pyspike.ops.test"
    ],
    package_data={
        "pyspike.ops": [
            "doc/*.rst",
            "doc/_templates/*.css",
            "doc/html/*.html",
            "doc/html/*.js",
            "doc/html/_sources/*",
            "doc/html/_static/*",
        ],
        "pyspike.ops.test": [
            "*.json",
        ],
    },
    install_requires=[],
    extras_require={
        "dev": [
            "pep8>=1.6.2",
        ],
        "docbuild": [
            "babel>=2.2.0",
            "sphinx-argparse>=0.1.15",
            "sphinxcontrib-seqdiag>=0.8.4",
            "sphinx_rtd_theme>=0.1.9"
        ],
    },
    entry_points={
        "console_scripts": [
            "pyspike-build = pyspike.ops.main:run",
        ],
    },
    zip_safe=False
)
