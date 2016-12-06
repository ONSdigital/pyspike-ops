#!/usr/bin/env python
#   coding: UTF-8

import logging
from logging.handlers import WatchedFileHandler
import sys

import pyspike.ops.cli


def main(args):

    log = logging.getLogger("pyspike")
    log.setLevel(args.log_level)

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)-7s %(name)s|%(message)s")
    ch = logging.StreamHandler()

    if args.log_path is None:
        ch.setLevel(args.log_level)
    else:
        fh = WatchedFileHandler(args.log_path)
        fh.setLevel(args.log_level)
        fh.setFormatter(formatter)
        log.addHandler(fh)
        ch.setLevel(logging.WARNING)

    ch.setFormatter(formatter)
    log.addHandler(ch)

    if not args.command:
        log.info("No command supplied.")

    elif args.command == "docker":
        log.info("Docker command supplied.")

    log.info(sys.executable)
    return 0

def run():
    p, subs = maloja.cli.parsers()
    args = p.parse_args()
    rv = 0
    if args.version:
        sys.stdout.write(pyspike.ops.__version__ + "\n")
    else:
        rv = main(args)

    if rv == 2:
        sys.stderr.write("\n Missing command.\n\n")
        p.print_help()

    sys.exit(rv)

if __name__ == "__main__":
    run()
