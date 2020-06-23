# -*- coding: utf-8 -*-
'''
linestats: Python module to count the number of scripted, commented, docstringed, and empty lines in
python code.

This file contains the main setup for the linestats package.

Copyright (c) 2020 F.P.A. Vogt; frederic.vogt@alumni.anu.edu.au

Distributed under the terms of the GNU General Public License v3.0 or later.

SPDX-License-identifier: GPL-3.0-or-later
'''

import os
from setuptools import setup # Always prefer setuptools over distutils

# Extract the version from the version file
v = open(os.path.join('.', 'linestats', 'version.py'))
version = [l.split("'")[1] for l in v.readlines() if '__version__' in l][0]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='linestats',
      version=version,
      author='F.P.A. Vogt',
      author_email='frederic.vogt@alumni.anu.edu.au',
      packages=['linestats',],
      url='https://github.com/fpavogt/linestats',
      download_url='https://github.com/fpavogt/linestats/archive/master.zip',
      license='GNU General Public License v3 or later (GPLv3+)',
      description='Python module to count the number of scripted, commented, docstringed, and' + \
                  ' empty lines in Python code.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      python_requires='>=3',
      install_requires=[],

      entry_points={'console_scripts': ['linestats=linestats.__main__:main']},

      classifiers=[# How mature is this project? Common values are
                   #   3 - Alpha
                   #   4 - Beta
                   #   5 - Production/Stable
                   'Development Status :: 4 - Beta',

                   # Indicate who your project is intended for
                   #'Intended Audience :: Science/Research',
                   #'Topic :: Scientific/Engineering :: Astronomy',

                   # Pick your license as you wish (should match "license" above)
                   'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

                   # Specify the Python versions you support here. In particular, ensure
                   # that you indicate whether you support Python 2, Python 3 or both.
                   'Programming Language :: Python :: 3.8',
                   ],

      include_package_data=False, # So that non .py files make it onto pypi, and then back !
      #package_data={'example_files':['example_files/*'],
      #              'docs':['../docs/build']
      #             }
      )
