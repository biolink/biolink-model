---
nav_order: 2
---

# Installation and Usage Notes

## Installation
The `biolink-model` software requires Python 3.7 and greater because it makes extensive
`dataclasses` library.  The standard approach is to:
1) Install python 3.7 or greater on your machine (see: [http://python.org/]()) for details.
    ```bash
    > python -V
    Python 3.7.3
    ```
2) Create and activate a virtual environment.
    ```bash
    > cd biolink-model
    biolink-model > pipenv install biolink-model
    biolink-model > pipenv shell
    (biolink-model) biolink-model >
    ```
    
4) Verify that the install worked
    ```bash
    (biolink-model) biolink-model > tox
    (biolink-model) biolink-model >
  ```

