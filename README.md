# linestats

[![github](https://img.shields.io/github/release/fpavogt/linestats.svg)](https://github.com/fpavogt/linestats/releases)
[![last-commit](https://img.shields.io/github/last-commit/fpavogt/linestats.svg?colorB=e6c000)](https://github.com/fpavogt/linestats) [![issues](https://img.shields.io/github/issues/fpavogt/linestats.svg?colorB=b4001e)](https://github.com/fpavogt/linestats/issues)
[![pypi](https://img.shields.io/pypi/v/linestats.svg?colorB=<brightgreen>)](https://pypi.python.org/pypi/linestats/)


Ever wanted/needed to know how many lines are empty, comments, docstrings or actual code in some Python scripts of yours ?

Presenting **linestats: a small Python module to count the number of scripted, commented, docstringed, and empty lines in Python code**. Here is what linestats contains *and* what it does: [linestats.txt](https://github.com/fpavogt/linestats/blob/master/linestats.txt)

## Table of contents
- [Installation](#installation)
- [Running](#running)
- [Limitations](#limitations)
- [Changelog](#changelog)
- [Information for dev work](#information-for-dev-work)

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
     - `-s output_file.txt` to save the statistics to file instead of `sys.stdout`,
     - `-v` to print the linestats version, and
     - `-w` to print detailed info for every file.

  * from a Python script/shell:
     ```python3
     import linestats
     from pathlib import Path

     p = Path('some', 'path', 'to', 'dir', 'or', 'file.py')
     s = Path('.', 'output_file.py')

     linestats.extract_line_stats(p, recursive=True, save_to_file=s, verbose=False)
     ```

## Limitations
linestats is extremely basic, and the output should be largely self-explanatory. Still, here are a few aspects to keep in mind when using this code:
1. linestats will only process `.py` files. At present, there is no way to force the processing of other file types.
2. The different lines are counted in the following category order: **docstrings -> comments -> emtpy -> code**.
  Each step feeds the following only with the lines that do not belong to it. This implies, for example, that
    * an empty line inside a docstring is counted as a docstring line,
    * a docstring line starting with `#` is also counted as a docstring line,
    * `a = 4 # A comment on the same line as code` would be counted as a code line, and
    * each line belongs to a single category, is counted once only, so the sum of all the categories adds up to 100%.

## Changelog

See [here](CHANGELOG).

## Information for dev work

### Code of conduct

This project and everyone participating in it is governed by the [linestats Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.
Please report unacceptable behavior to [frederic.vogt@alumni.anu.edu.au](mailto:frederic.vogt@alumni.anu.edu.au).

### Branching model

The `develop` branch is the default one, where all contributions get merged. When a new release is
warranted, a Pull Request to the `master` branch is issued. This implies that the `master` branch
will always reflect the state of the latest release of the code.

Contributors are required to work in their own branches, and issue Pull Requests into the `develop`
branch when appropriate.

The `master` and `develop` branches are protected.


### CI/CD

Automated CI/CD checks are triggered upon Pull Requests being issued towards the `develop` and
`master` branches. At the time being, they are implemented using dedicated Github Actions specified under `.github/workflows`. These checks include:

* code linting using `pylint`
* code testing using `pytest`
* check that the CHANGELOG was updated
* check that the code version was incremented (for PR to `master` only)

### Release mechanism

Assuming the content of `develop` is ready for a release, here are the steps to follow:
1) Issue a PR from `develop` into `master`. Merge it if all looks ok.

   :white_check_mark: The `CI_check_version` Action will run to check that the version has been increased.

2) Create a new release from Github. This step has not been automated yet. Make sure to enter the
   same version number as set in the code !

   :white_check_mark: Upon publication of the release, the `CI_pypi` Action will directly upload the code
   to testpypi and pypi. Make sure it succeeds !
