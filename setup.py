#!/usr/bin/env python

from setuptools import setup, find_packages

with open("requirements.txt", "r") as FH:
    REQUIREMENTS = FH.readlines()

NAME = 'biolink-model'
VERSION = '3.0.3'

DESCRIPTION = 'Biolink Model: A high level datamodel of biological entities and associations'
URL = 'https://github.com/biolink/biolink-model'
AUTHOR = 'Deepak Unni', 'Sierra Moxon'
EMAIL = 'smoxon@lbl.gov'
REQUIRES_PYTHON = '>=3.7'
LICENSE = 'BSD'

setup(
    name=NAME,
    author=AUTHOR,
    version=VERSION,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license=LICENSE,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    install_requires=[r for r in REQUIREMENTS if not r.startswith("#")],
    keywords='NCATS NCATS-Translator Biolink-Model Biolink LinkML Datamodel',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)