#!/usr/bin/env python
"""
Copyright 2015 Optiflows

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
# forked from https://github.com/optiflows/pijon
# backported to run on Python2.7+

from __future__ import absolute_import
from __future__ import unicode_literals

from setuptools import setup, find_packages


with open('DESCRIPTION', 'r') as d:
    long_description = d.read()

setup(
    name='pijon2',
    version='0.2.0',
    description='Tool and library to help with json based schema and data migration.',
    long_description=long_description,
    url='http://www.surycat.com, https://github.com/pombredanne/pijon',
    author='Optiflows R&D, backported to Python 2.7 by pombredanne',
    author_email='rand@surycat.com',
    packages=find_packages(exclude=['tests']),
    license='Apache 2.0',
    scripts=['scripts/pijon'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 2.7',
    ],
)
