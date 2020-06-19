# -*- coding: utf-8 -*-
'''
linestats: Python module to count the number of scripted, commented, docstringed, and empty lines in
python code.

This file contains the core functions.

Created April 2020, Frédéric Vogt: frederic.vogt@alumni.anu.edu.au
---
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from pathlib import Path


def count_docstrings(lines):
    ''' Counts docstrings and remove them from the line list.

    Args:
        lines (list[str]): list of the code lines (in order!)

    Returns:
        int, list[str]: number of docstring lines, list of the code lines with all the docstrings
                        removed

    '''

    lines_minus_docstr = []
    counter = 0
    in_docstr = False

    # Go through each line in order
    for line in lines:

        #Look for the docstring tag
        if line.strip(' ')[:3] in ["'''", '"""']:
            in_docstr = ~in_docstr
            counter += 1
            continue

        # If I am in a docstring, count the extra lines
        if in_docstr:
            counter += 1
        # Else, keep the line for latter
        else:
            lines_minus_docstr += [line]

    # A small sanity check before closing
    if len(lines_minus_docstr) != len(lines) - counter:
        raise Exception('Ouch! Something is very wrong here!')

    return counter, lines_minus_docstr

def count_comments(lines):
    ''' Counts commented lines, i.e. lines starting with #

    Args:
        lines (list[str]): list of the code lines

    Returns:
        int, list[str]: number of commented lines, list of the code lines with all the comments
                        removed.

    Caution:
        This will look for all lines starting with #, including inside docstrings ! If you care
        about this, you should remove these first using `count_docstrings()`to avoid confusion.

    '''

    counter = 0
    lines_minus_comm = []

    for line in lines:
        if line.strip(' ')[0] == '#':
            counter += 1
        else:
            lines_minus_comm += [line]

    # A small sanity check before closing
    if len(lines_minus_comm) != len(lines) - counter:
        raise Exception('Ouch! Something is very wrong here!')

    return counter, lines_minus_comm

def count_empty(lines):
    ''' Counts empty lines.

    Args:
        lines (list[str]): list of the code lines

    Returns:
        int, list[str]: number of empty lines, list of the code lines with all the empty ones
                        removed.

    Caution:
        This will look for all the empty lines, including inside docstrings !
        If you care about this, you should remove these first using `count_docstrings()` to avoid
        confusion.

    '''

    counter = 0
    lines_minus_empty = []

    for line in lines:
        if line.strip(' ') == '\n':
            counter += 1
        else:
            lines_minus_empty += [line]

    # A small sanity check before closing
    if len(lines_minus_empty) != len(lines) - counter:
        raise Exception('Ouch! Something is very wrong here!')

    return counter, lines_minus_empty

def extract_line_stats(search_path, recursive=False):
    ''' Computes the number of blank, commented, docstringed and actual code lines in python code.

    The code can process either a specific .py file, or, if a directory name if given, all the .py
    files within it (including the options of making a recursive search).

    Args:
        search_path (pathlib.Path, str): path to file or folder to process.
        recursive (bool): if True, will run a recursive search for .py files in subfolders.

    Raises:
        Exception: If the search_path is invalid

    Todo:
        * Add a proper logger, to chose to send the output to file
        * Add test functions
    '''

    # Clean the prompt
    print(' ')

    # Prepare some variables.
    file_total = 0
    grand_total = 0
    code_total = 0
    comm_total = 0
    empty_total = 0
    docstr_total = 0

    # If I got a string, turn this into a path
    if isinstance(search_path, str):
        search_path = Path(search_path)

    elif not isinstance(search_path, type(Path('.'))):
        raise Exception('Ouch ! Type %s for search_path is invalid.' % (type(search_path)))

    # Was a single file specified ?
    if search_path.is_file():
        fnlist = [search_path]

    # Was I given a proper directory ?
    elif search_path.is_dir():
        if recursive:
            txt = 'recursively'
            mthd = '**/*'
        else:
            txt = ''
            mthd = '*'

        print('Looking %s for python script files in %s' % (txt, search_path))
        fnlist = search_path.glob(mthd)

    else:
        raise Exception('Please specify a valid path or a filename')

    # Now go through each file and extract the line statistics
    for file_path in fnlist:

        # Make sure I'm only touching regular files ...
        if not file_path.is_file():
            #print('%s is not a file. Skipping it ...' % (file_path))
            continue

        # Only deal with .py files
        if file_path.suffix != '.py':
            print('%s does not look like Python code. Skipping it ...' % (file_path))
            continue

        # Very well, let's extract the file lines.
        this_file = open(file_path, 'r')
        lines = this_file.readlines()
        this_file.close()

        # I have a code file, so let's count it
        file_total += 1

        # Get the total line count
        total_lines = len(lines)
        grand_total += total_lines

        # Track the docstrings
        docstr, lines_minus_docstr = count_docstrings(lines)
        docstr_total += docstr

        # Now the comments (feed it all except the docstrings, to avoid counting these twice)
        comm, lines_minus_comm = count_comments(lines_minus_docstr)
        comm_total += comm

        # And finally count the blank lines
        empty, _ = count_empty(lines_minus_comm)
        empty_total += empty

        code = total_lines - empty - docstr - comm
        code_total += code

        print(file_path)
        print('  Total: %i - Code: %i [%.1f%%] - Comment+docstr: %i [%.1f%%] - Blank: %i [%.1f%%]' %
              (total_lines, code, 100*code/total_lines, comm+docstr, 100*(comm+docstr)/total_lines,
               empty, 100*empty/total_lines))

    print(' ')
    print('Grand total: %i lines in %i files' % (grand_total, file_total))
    if grand_total > 0:
        print('    Code: %i [%.1f%%]' % (code_total, code_total/grand_total*100))
        print('    Docstrings: %i [%.1f%%]' % (docstr_total, docstr_total/grand_total*100))
        print('    Comments: %i [%.1f%%]' % (comm_total, comm_total/grand_total*100))
        print('    Empty: %i [%.1f%%]' % (empty_total, empty_total/grand_total*100))
    print(' ')
    