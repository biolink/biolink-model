from setuptools import setup

version = '0.0.2'

requires = [
    "marshmallow==3.0.0b8",
    "click",
    "pyyaml==3.12",
    "marshmallow-jsonschema>0",
    "jsonschema>=2.6.0",
    "rdflib",
    "graphviz",
    "pandas",
    "prefixcommons"
    ]

setup(
    name='Biolink Model Generator',
    version= version,
    packages=['kgx'],
    install_requires=requires,
    tests_require=['pytest', 'pytest_logging'],
    scripts=['bin/translator_kgx.py'],
    entry_points="""
        [console_scripts]
        kgx=translator_kgx:cli
    """
)
