#
# Copyright (C) 2019 James Parkhurst
#
# This code is distributed under the BSD license.
#
from setuptools import setup
from os.path import abspath
from os.path import dirname
from os.path import join

def get_readme():
    directory = abspath(dirname(__file__))
    with open(join(directory, 'README.md'), encoding='utf-8') as readme:
        return readme.read()

setup(
    name="halerror",
    version="0.1",
    author="James Parkhurst",
    author_email="james.parkhurst@diamond.ac.uk",
    description="The best Python exception library!",
    long_description=get_readme(),
    license="BSD",
    keywords="HAL-9000",
    packages=["halerror"],
    install_requires=[],
    setup_requires = ["pytest-runner"],
    tests_require = ["pytest", "pytest-cov", "mock"],
    test_suite = "tests",
    classifiers=["License :: OSI Approved :: BSD License"],
)
