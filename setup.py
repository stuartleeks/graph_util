#!/usr/bin/env python

from setuptools import find_packages
from setuptools import setup

PROJECT = "graphutil"
VERSION = "0.0.1"

try:
    long_description = open("README.md", "rt").read()
except IOError:
    long_description = ""

setup(
    name=PROJECT,
    version=VERSION,
    description="Util to explore MS Graph API",
    long_description=long_description,
    author="Stuart Leeks",
    author_email="stuartle@microsoft.com",
    # url='',
    # download_url='',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Intended Audience :: Developers",
        "Environment :: Console",
    ],
    platforms=["Any"],
    scripts=[],
    provides=[],
    install_requires=[
        "azure-identity==1.12.0",
        "msgraph-core==0.2.2",
        "click==8.1.3",
        "jmespath==1.0.1",
        "tabulate==0.8.10",
        "pygments==2.13.0",
    ],
    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": ["graphutil = graphutil.app:cli"],
    },
    zip_safe=False,
)
