#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages


def required(fname):
    return filter(lambda x: not x.startswith('-'), open(fname).readlines())

setup(
    name='randomchuck',
    version='0.1.0',
    description="Flask-Python server that returns a random json formatted \
                 Chuck Norris quote on request.",
    long_description="",
    author="Patilla Code",
    author_email='patillacode@gmail.com',
    packages=find_packages('src', exclude=[
        "*.tests", "*.tests.*", "tests.*", "tests",
        "*.ez_setup", "*.ez_setup.*", "ez_setup.*", "ez_setup",
        "*.examples", "*.examples.*", "examples.*", "examples",
    ]),
    namespace_packages=[
        'app',
    ],
    package_dir={
        '': 'src'
    },
    include_package_data=True,
    install_requires=required('requirements.txt'),
    license="",
    zip_safe=False,
    keywords='',
    classifiers=[
        "Programming Language :: Python",
    ],
    test_suite='nose.collector',
    # tests_require=required('requirements-dev.txt')
)
