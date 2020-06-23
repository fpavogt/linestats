# linestats

[![github](https://img.shields.io/github/release/fpavogt/linestats.svg)](https://github.com/fpavogt/linestats/releases)
[![last-commit](https://img.shields.io/github/last-commit/fpavogt/linestats.svg?colorB=e6c000)](https://github.com/fpavogt/linestats) [![issues](https://img.shields.io/github/issues/fpavogt/linestats.svg?colorB=b4001e)](https://github.com/fpavogt/linestats/issues) 
[![pypi](https://img.shields.io/pypi/v/linestats.svg?colorB=<brightgreen>)](https://pypi.python.org/pypi/linestats/)


Ever wanted/needed to know how many lines are empty, comments, docstrings or actual code in some Python scripts of yours ?

Presenting **linestats: a small Python module to count the number of scripted, commented, docstringed, and empty lines in Python code**. Here is what it contains *and* what it does: [linestats.txt](https://github.com/fpavogt/linestats/blob/master/linestats.txt)

## Table of contents
- [Installation](#installation)
- [Running](#running)
- [Limitations](#limitations)
- [Changelog](#changelog)

## Installation

linestats is available on pypi. The following command should take care of things:
```
pip install linestats
```

Alternatively, you can also get the code from its [dedicated Github repository](https://github.com/fpavogt/linestats).

## Running
Using linestats is fairly straightforward. You can do so (1) in any decent terminal using the in-built entry point, or (2) from within a Python shell by importing the corresponding module. Both methods are the same, and here's how they work:
  * from a terminal: The basic syntax is 
     ```
     linestats -p some/path/to/dir/or/file.py
     ``` 
     This will process the `file.py` (or all `.py`file located at the indicated location, if a directory is specified). The other options are: 
     - `-h` for help,
     - `-r` to run a recursive search for `.py` files in subfolders, 
     - `-s output_file.txt` to save the statistics to file instead of `sys.stdout`, and
     - `-v` to print the linestats version.
  
  * from a Python script/shell: 
     ```python3
     import linestats
     from pathlib import Path
     
     p = Path('some', 'path', 'to', 'dir', 'or', 'file.py')
     s = Path('.', 'output_file.py')
     
     linestats.extract_line_stats(p, recursive=True, save_to_file=s)
     ```

## Limitations
linestats is extremely basic, and the output should be largely self-explanatory. Still, here are a few aspects to keep in mind when using this code:
1. linestats will process `.py` files. At present, there is no way to force the processing of other file types.
2. The different lines are counted in the following category order: **docstrings -> comments -> emtpy -> code**. 
  Each step feeds the following only with the lines that do not belong to it. This implies, for example, that 
    * an empty line inside a docstring is counted as a docstring line,
    * a docstring line starting with `#` is also counted as a docstring line,
    * `a = 4 # A comment on the same line as code` would be counted as a code line, and
    * each line belongs to a single category, is counted once only, so the sum of all the categories adds up to 100%.
 
## Changelog

All notable changes to linestats will be documented below.

The format is inspired from [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

[//]: # (### [Unreleased])
[//]: # (#### Added:)
[//]: # (#### Changed:)
[//]: # (#### Deprecated:)
[//]: # (#### Removed:)
[//]: # (#### Fixed:)
[//]: # (#### Security:)

### [1.0.0]
#### Added
 - [F.P.A. Vogt, 2020-06-20] Add option to save output to file (#2).
 - [F.P.A. Vogt, 2020-06-19] Initial module assembly + Github upload.
#### Fixed:
 - [F.P.A. Vogt, 2020-06-20] Fix bug for scripts with last lines containing only spaces (#2).

