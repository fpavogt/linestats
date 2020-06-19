# linestats

Ever wanted/needed to know how many lines are empty, comments, docstrings or actual code in some Python scripts of yours ?

Presenting **linestats: a small Python module to count the number of scripted, commented, docstringed, and empty lines in python code**. Here is what it contains *and* what it does:

```
linestats -p . -r

Looking recursively for python script files in .
setup.py
  Total: 69 - Code: 22 [31.9%] - Comment+docstr: 38 [55.1%] - Blank: 9 [13.0%]  
linestats/version.py
  Total: 24 - Code: 1 [4.2%] - Comment+docstr: 22 [91.7%] - Blank: 1 [4.2%]
linestats/__init__.py
  Total: 7 - Code: 2 [28.6%] - Comment+docstr: 3 [42.9%] - Blank: 2 [28.6%]
linestats/linestats.py
  Total: 239 - Code: 100 [41.8%] - Comment+docstr: 100 [41.8%] - Blank: 39 [16.3%]
linestats/__main__.py
  Total: 57 - Code: 4 [7.0%] - Comment+docstr: 49 [86.0%] - Blank: 4 [7.0%]

Grand total: 396 lines in 5 files
    Code: 129 [32.6%]
    Docstrings: 165 [41.7%]
    Comments: 47 [11.9%]
    Empty: 55 [13.9%]
```

## Table of contents
- [Installation](#installation)
- [Running](#running)
- [Changelog](#changelog)

## Installation

Until I get the chance to put this on pypi, you'll need to install this package manually. Here's one way to do so:
  1. Download a compressed copy of the master branch.
  2. Then, in a decent terminal of your choice: 
     ```
     cd some/path/of/your/choice/linestats_master`
     pip install -e .
     ```
     
  3. That's it. If all went well, you should be able to do the following:
     ```
     linestats -v
     ```
  
## Running
Using linestats is fairly straightforward. You can do so (1) in any decent terminal using the in-built entry point, or (2) from within a Python shell by importing the corresponding module. Both methods are the same, and here how they work:
  * from a terminal: The basic syntax is 
     ```
     linestats -p some/path/to/dir/or/file.py
     ``` 
     This which will process the `file.py`, or all `.py`file located at the indicated location. The other options are: `-r`to run a recursive search for .`.py` 
     files in subfolders, and `-v`, to print the linestats version. Type `linestats -h` will get you the help. 
  
  * from a Python script/shell: 
     ```python3
     import linestats
     from pathlib import Path
     
     p = Path('some', 'path', 'to', 'dir', 'or', 'file.py')
     
     linestats.extract_line_stats(p, recursive=True)
     ```


## Changelog

All notable changes to linestats will be documented below.

The format is inspired from [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

### [Unreleased]
#### Added:
#### Changed:
#### Deprecated:
#### Removed:
#### Fixed:
#### Security:

### [1.0.0]
#### Added
 - [F.P.A. Vogt, 2020-06-19] Initial module assembly + Github upload.

