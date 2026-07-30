# AGENTS.md for biolink-model

Schema and generated objects for biolink data model and upper ontology


## Repo management

This repo uses `uv` for managing dependencies. Never use commands like `pip` to add or manage dependencies.
`uv run` is the best way to run things, unless you are using a `makefile` target

`mkdocs` is used for documentation.## This is a LinkML Schema repository

Layout:

 * `biolink_model.yaml` - LinkML source schema (edit this)
 * `project` - derived files (do not edit these directly, they are derived from the LinkML)
 * `src/docs` - source markdown for documentation
 * `docs` - derived docs - do NOT edit these directly
 * `src/data/examples/{valid,invalid}` - example data files
    * always include positive examples of each class in the `valid` subfolder
    * include negative examples for unit tests and to help illustrate pitfalls
    * format is `ClassName-{SOMENAME}.yaml`
 * `examples` - derived examples. Do not edit these directly

Building and testing:

* `make --help` to see all commands
* `make gen-project` to generate `project` files
* `make test` to test schema and pos/neg examples

These are wrappers on top of existing linkml commands such as `gen-project`, `linkml-convert`, `linkml-run-examples`.
You can run the underlying commands (with `uv run ...`) but in general justfile targets should be favored.

Best practice:

* For full documentation, see https://linkml.io/linkml/
* For schemas with polymorphism, consider using field `type` marked as a `type_designator: true`
* Include meaningful descriptions of each element
* always edit biolink-model.yaml in the root of the project.
* map to standards where appropriate (e.g. dcterms)
* Never guess OBO term IDs. Always use the OLS API to look for relevant ontology terms
* be proactive in using due diligence to do deep research on the domain, and look at existing standards
