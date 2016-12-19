#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from codecs import open

from setuptools import find_packages, setup

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read(*paths):
    """Build a file path from *paths and return the contents."""
    with open(os.path.join(*paths), 'r', 'utf-8') as f:
        return f.read()


requires = [
    'Cython==0.25.2',
    'Kivy==1.9.1',
    'Kivy-Garden==0.1.4',
    'requests==2.12.4',
    'bluepy==1.0.5',
]

extras_require = {
    'develop': [
        'twine==1.8.1',
    ],
}


setup(
    name='kivy_blue',
    version='0.1.0',
    description='',
    long_description=read(BASE_DIR, 'README.md'),
    author='Max Brauer',
    author_email='max@max-brauer.de',
    extras_require=extras_require,
    include_package_data=True,
    install_requires=requires,
    license='BSD-3-Clause',
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
