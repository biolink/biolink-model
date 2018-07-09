# Installation and Usage Notes

## Installation
The `biolink-model` software requires Python 3.6 and greater because it makes extensive
`dataclasses` library.  The standard approach is to:
1) Install python 3.6 or greater on your machine (see: [http://python.org/]()) for details.
    ```bash
    > python -V
    Python 3.6.4
    ```
2) Create and activate a virtual environment.
    ```bash
    > pip install virtualenv
    > virtualenv biolink_venv
    Using base prefix '/Library/Frameworks/Python.framework/Versions/3.6'
    New python executable in biolink_env/bin/python3.6
    Also creating executable in biolink_env/bin/python
    Installing setuptools, pip, wheel...done.
    > . biolink_venv/bin/activate
    (biolink_venv) >
    ```
3) Download and install biolink-model
    ```bash
    (biolink_venv) > pip install git+https://github.com/biolink/biolink-model.git
    Collecting git+https://github.com/biolink/biolink-model.git
    Cloning https://github.com/biolink/biolink-model.git to /private/var/folders/9r/b4ptppwd2g12t45151svr49w0000gn/T/pip-req-build-rxs6fzx3
    Collecting click>=6.7 (from Biolink-Model-Generator==0.0.3)
    ...
    Installing collected packages: click, PyYAML, jsonasobj, jsonschema, pyparsing, six, isodate, rdflib, graphviz, chardet, urllib3, idna, certifi, requests, argh, pathtools, watchdog, portalocker, cachier, prefixcommons, rdflib-jsonld, antlr4-python3-runtime, PyJSG, PyShExC, ShExJSG, dataclasses, Biolink-Model-Generator
    Successfully installed Biolink-Model-Generator-0.0.3 PyJSG-0.6.0 PyShExC-0.3.4 PyYAML-3.12 ShExJSG-0.2.1 antlr4-python3-runtime-4.7.1 argh-0.26.2 cachier-1.2.2 certifi-2018.4.16 chardet-3.0.4 click-6.7 dataclasses-0.6 graphviz-0.8.3 idna-2.7 isodate-0.6.0 jsonasobj-1.2.1 jsonschema-2.6.0 pathtools-0.1.2 portalocker-1.2.1 prefixcommons-0.1.7 pyparsing-2.2.0 rdflib-4.2.2 rdflib-jsonld-0.4.0 requests-2.19.0 six-1.11.0 urllib3-1.23 watchdog-0.8.3
    (biolink_venv) >
    ```
4) Verify that the install worked
    ```bash
    (biolink_venv) > gen-markdown --help
    Usage: gen-markdown [OPTIONS] YAMLFILE

      Generate markdown documentation of a biolink model
    
    Options:
      -d, --dir TEXT      Output directory
      -f, --format [md]   Output format
      -c, --classes TEXT  Class(es) to emit
      -i, --img           Download YUML images to 'image'
                          directory
      --noimages          Do not (re-)generate images
      --help              Show this message and exit.
    (biolink_venv) >
  ```

## Usage
(Fill me in)