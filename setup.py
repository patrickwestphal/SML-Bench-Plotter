#!/usr/bin/env python

from distutils.core import setup

setup(name='SML-Bench Plotter',
      version='0.1',
      author='Patrick Westphal',
      author_email='patrick.westphal@informatik.uni-leipzig.de',
      packages=[],
      install_requires=[
            'matplotlib==3.1.0',
      ],
      scripts=[
            'bin/plotfscore',
            'bin/plotaccuracy',
      ],
)
