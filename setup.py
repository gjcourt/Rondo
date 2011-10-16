#!/usr/bin/env python

from setuptools import setup

install_requires = None
with open('requirements.txt', 'r') as reqs:
    install_requires = [line for line in reqs if not line.strip(' \n').startswith('#')]

setup(name='Rondo',
      version='0.1',
      description='Command line music player',
      author='George J Courtsunis',
      author_email='gjcourt@gmail.com',
      install_requires = install_requires,
     )

