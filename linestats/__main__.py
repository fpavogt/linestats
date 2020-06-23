# -*- coding: utf-8 -*-
'''
linestats: Python module to count the number of scripted, commented, docstringed, and empty lines in
Python code.

This file handles the high-level entry point for the code.

Copyright (c) 2020 F.P.A. Vogt; frederic.vogt@alumni.anu.edu.au

Distributed under the terms of the GNU General Public License v3.0 or later.

SPDX-License-identifier: GPL-3.0-or-later
'''

import argparse

from .version import __version__
from . import linestats

# Use argparse to make linestats user friendly
parser = argparse.ArgumentParser(description='''Computes the number of blank, comment, ''' +
                                 '''and script lines in a python code. ''',
                                 epilog='Feedback, questions: frederic.vogt@alumni.anu.edu.au \n',
                                 formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('-p', action='store', metavar='path/to/file(s)', default='.',
                    help='location or file to analyze')
parser.add_argument('-r', action='store_true', help='run a recursive search')
parser.add_argument('-s', action='store', metavar='path/to/file.txt', default=None,
                    help='set a filename to store the linestats output')
parser.add_argument('-v', '--version', action='version', version=('linestats %s' % __version__))


def main():
    ''' The main function, offering the entry point to the underlying linestats routine.

    '''

    # What did the user type in ?
    args = parser.parse_args()

    # Feed the info to the routine
    linestats.extract_line_stats(args.p, recursive=args.r, save_to_file=args.s)

# Make it work
if __name__ == "__main__":

    main()
