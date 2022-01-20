# -*- coding: utf-8 -*-
'''
Copyright (c) 2022 MeteoSwiss, contributors listed in AUTHORS.

Distributed under the terms of the 3-Clause BSD License.

SPDX-License-Identifier: BSD-3-Clause

This script can be used together with a Github Action to check whether a code version has been
properly incremented.

Created January 2022; F.P.A. Vogt; frederic.vogt@meteoswiss.ch
'''

import argparse
from packaging import version as pversion

def main():
    ''' The main function. '''

    # Use argparse to allow feeding parameters to this script
    parser = argparse.ArgumentParser(description='''Compare the versions between the head and base
                                                 branches of the PR. Fails is Head <= Base.''',
                                     epilog='Feedback, questions, comments: \
                                             frederic.vogt@meteoswiss.ch \n',
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('head', action='store', metavar='version',
                        help='Head version.')

    parser.add_argument('base', action='store', metavar='version',
                        help='Base version.')

    # What did the user type in ?
    args = parser.parse_args()

    # Print the versions fed by the user, for monitoring
    print("Head:", args.head)
    print("Base:", args.base)

    if pversion.parse(args.head) > pversion.parse(args.base):
        print("Version was increased. Well done.")
        return True

    print("Version was not increased ?")
    return False

if __name__ == '__main__':

    main()
