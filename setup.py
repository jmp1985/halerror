#
# Copyright (C) 2019 James Parkhurst
#
# This code is distributed under the BSD license.
#
from setuptools import setup

setup(
    name="halerror",
    version="0.1",
    author="James Parkhurst",
    author_email="james.parkhurst@diamond.ac.uk",
    description="The best Python exception library!",
    license="BSD",
    keywords="HAL-9000",
    packages=["halerror"],
    install_requires=[],
    setup_requires = ["pytest-runner"],
    tests_require = ["pytest", "pytest-cov", "mock"],
    test_suite = "tests",
    classifiers=["License :: OSI Approved :: BSD License"],
)
