from setuptools import setup


NAME = 'biolink_model'
DESCRIPTION = 'A high level datamodel of biological entities and associations'
URL = 'https://github.com/biolink/biolink-model'
AUTHOR = 'Harold Solbrig'
EMAIL = 'solbrig@jhu.edu'
REQUIRES_PYTHON = '>=3.7'
VERSION = '0.0.1'
LICENSE = 'CC0 1.0 Universal'

REQUIRED = [
    "biolinkml>=1.3.8"
]

EXTRAS = {}


setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    license=LICENSE,
    packages=['biolink'],
    keywords='BioLink Datamodel NCATS NCATS-Translator',
    classifiers=[
        'Intended Audience :: Developers'
        'Intended Audience :: Science/Research',
        'Intended Audience :: Healthcare Industry',
        'Topic :: Scientific/Engineering :: Bio-informatics',
        'License :: CC0 1.0 Universal (CC0 1.0)',
        'Programming Language :: Python :: 3'
    ],
    install_requires=REQUIRED,
    extras_require=EXTRAS
)
