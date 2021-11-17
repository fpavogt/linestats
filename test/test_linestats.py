# -*- coding: utf-8 -*-
'''
linestats: Python module to count the number of scripted, commented, docstringed, and empty lines in
Python code.

Copyright (c) 2020-2021 F.P.A. Vogt; frederic.vogt@alumni.anu.edu.au

Distributed under the terms of the GNU General Public License v3.0 or later.

SPDX-License-identifier: GPL-3.0-or-later
'''

from linestats import count_docstrings, count_comments, count_empty

def test_count_docstrings():
    """ Test the docstrings function """

    msg = ['"""','a','#', '"""', '1', '2', '#']
    counter, _ = count_docstrings(msg)
    assert counter == 4

def test_count_comments():
    """ Test the comments function """

    msg = ['#', '1', '2', '#', '#', '"""']
    counter, _ = count_comments(msg)
    assert counter == 3

def test_count_empty():
    """ test the empty function """

    msg = ['', '           ', '#', '"""', '', '\n', '    \n', '"""']
    counter, _ = count_empty(msg)
    assert counter == 5
