#!/usr/bin/env python
#  coding: UTF-8

import argparse
import logging
import os.path

__doc__ = """
CLI Interface to the pyspike-ops build tool.

Operation via CLI requires a set of common options.
Each subcommand may have extra options, like this::

    pyspike-buiild <common options> SUBCOMMAND <subcommand options>

"""

def add_docker_options(parser):
    parser.add_argument(
        "--input", required=False,
        help="path to docker file")
    return parser

def add_common_options(parser):
    parser.add_argument(
        "--version", action="store_true", default=False,
        help="Print the current version number")
    parser.add_argument(
        "-v", "--verbose", required=False,
        action="store_const", dest="log_level",
        const=logging.DEBUG, default=logging.INFO,
        help="Increase the verbosity of output")
    parser.add_argument(
        "--log", default=None, dest="log_path",
        help="Set a file path for log output")
    return parser

def parser(description=__doc__):
    return argparse.ArgumentParser(
        description,
        fromfile_prefix_chars="@"
    )

def parsers(description=__doc__):
    rv = parser(description)
    rv = add_common_options(rv)
    subparsers = rv.add_subparsers(
        dest="command",
        help="Commands:",
    )
    p = subparsers.add_parser(
        "docker",
        help="Docker operations.",
        description="Operations to work with Docker containers."
    )
    p = add_docker_options(p)
    return (rv, subparsers)

def cli():
    return parsers()[0]
