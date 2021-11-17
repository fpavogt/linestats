# -*- coding: utf-8 -*-
# pylint: disable=C0114
'''
linestats: Python module to count the number of scripted, commented, docstringed, and empty lines in
Python code.

Copyright (c) 2020-2021 F.P.A. Vogt; frederic.vogt@alumni.anu.edu.au

Distributed under the terms of the GNU General Public License v3.0 or later.

SPDX-License-identifier: GPL-3.0-or-later
'''

# Make it easier to access the linestats functions

from .version import __version__
from .linestats import *
