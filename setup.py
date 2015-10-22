#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function

import sys

if sys.version_info < (2, 6):
    print('jizhi requires python2 version >= 2.6.', file=sys.stderr)
    sys.exit(1)

try:
    from setuptools import setup, Command
except ImportError:
    from distutils.core import setup, Command
import subprocess

packages = [
    'jizhi',
]

install_requires = [
    'requests>=2.7.0',
]

long_desc = """The SDK of jizhi api"""

import jizhi
version = jizhi.__version__


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        raise SystemExit(
            subprocess.call([sys.executable,
                             # Turn on deprecation warnings
                             '-Wd',
                             'tests/__init__.py']))


setup(
    name="jizhi",
    version=version,
    description="jizhi api SDK",
    long_description=long_desc,
    author="Jizhi Inc.",
    url="http://www.crowdsdom.com",
    install_requires=install_requires,
    packages=packages,
    keywords="jizhi oauth 2.0 client",
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
    ],
    cmdclass={
        'test': TestCommand
    },
)
