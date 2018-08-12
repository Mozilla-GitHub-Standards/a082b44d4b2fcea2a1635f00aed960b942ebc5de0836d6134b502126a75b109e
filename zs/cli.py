#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
sys.dont_write_bytecode = True

SCRIPT_FILE = os.path.abspath(__file__)
SCRIPT_NAME = os.path.basename(SCRIPT_FILE)
SCRIPT_PATH = os.path.dirname(SCRIPT_FILE)
if os.path.islink(__file__):
    REAL_FILE = os.path.abspath(os.readlink(__file__))
    REAL_NAME = os.path.basename(REAL_FILE)
    REAL_PATH = os.path.dirname(REAL_FILE)

NAME, EXT = os.path.splitext(SCRIPT_NAME)

from ruamel import yaml
from argparse import ArgumentParser, RawDescriptionHelpFormatter

def main(args=None):
    args = args if args else sys.argv[1:]
    parser = ArgumentParser(
        description=__doc__,
        formatter_class=RawDescriptionHelpFormatter,
        add_help=False)
    parser.add_argument(
        '--config',
        metavar='FILEPATH',
        default='~/.config/%(NAME)s/%(NAME)s.yml' % globals(),
        help='default="%(default)s"; config filepath')
    ns, rem = parser.parse_known_args(args)
    try:
        config = yaml.safe_load(open(ns.config))
    except FileNotFoundError as er:
        config = dict()
    parser = ArgumentParser(
        parents=[parser])
    parser.set_defaults(**config)
    parser.add_argument(
        '--firstname',
        help='default="%(default)s"; first name')
    parser.add_argument(
        '--lastname',
        help='default="%(default)s"; last name')
    parser.add_argument(
        '--age',
        help='default="%(default)s"; age')
    ns = parser.parse_args(rem)
    print(ns)

if __name__ == '__main__':
    main()
