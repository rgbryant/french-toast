#!/usr/bin/env python
# pylint: disable=missing-docstring
from __future__ import absolute_import

from setuptools import setup, find_packages

setup(
    name='french-toast',
    version='0.1.0',
    description='Code for AWS lambda that will hook into Alexa.',
    url='https://github.com/rgbryant/french-toast',
    packages=find_packages(),
    python_requires='>=3.0',
    install_requires=[
        "requests>=2.18.4, <3.0",
        "lxml>=4.2.1, <5"
    ],
)
