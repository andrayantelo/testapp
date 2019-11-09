#!/usr/bin/env python3
# coding: utf8

from setuptools import setup


setup(name='testapp',
      version='0.0.1',
      author='Andrea Anaya',
      url='https://github.com/andrayantelo/testapp',
      description="A simple guestbook",
      py_modules=['testapp'],
      install_requires=[flask, flask-wtf, flask-bootstrap, flask-sqlalchemy],
      classifiers=[
          "Development Status :: 3 - Alpha",
          ],
      )
