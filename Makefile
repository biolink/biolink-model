SRC_DIR = model
SCHEMA_DIR = $(SRC_DIR)
SOURCE_FILES := $(shell find $(SCHEMA_DIR) -name '*.yaml')
SCHEMA_NAMES = $(patsubst $(SCHEMA_DIR)/%.yaml, %, $(SOURCE_FILES))

SCHEMA_NAME = biolink-model
SCHEMA_SRC = $(SCHEMA_DIR)/$(SCHEMA_NAME).yaml
#TGTS = graphql jsonschema docs shex owl csv  python
TGTS = jsonschema
ARTIFACT_TGTS = python jsonschema jsonld-context python sqlddl owl shex
JAVA_GEN_OPTS = --output_directory org/alliancegenome/curation/model --package org.alliancegenome.curation.model
DDL_GEN_OPTS = --sqla-file target/sqla-files/


all: clean gen stage
artifacts: clean-artifacts gen-artifacts stage-artifacts
gen: $(patsubst %,gen-%,$(TGTS))
.PHONY: all gen clean t echo test install gh-deploy clean-artifacts clean-doc clean-artifacts gen-artifacts clean-docs .FORCE

docs:
	mkdir -p $@
	mkdir -p $@/images
	mkdir -p $@/types

clean-docs:
	rm -rf docs/images/*
	rm -rf docs/types/*
	rm -rf docs/

docs:
	mkdir -p $@
	mkdir -p $@/images
	mkdir -p $@/types

gen-docs:
	poetry run gen-doc biolink-model.yaml --directory target/docs --template-directory doc_templates
	cp css/extra_css.css docs/
	cp README.md docs/
	cp images/biolink-model.logo docs/



prefix-map: prefix-map/biolink-model-prefix-map.json


guidelines/%.md: docs/index.md
	cp -R guidelines/* $(dir $@)

# add more logging?
# some docs pages not being created
# usage of mkdocs.yml attributes like analytics?

###  -- PYTHON --
gen-python: $(patsubst %, target/python/%.py, $(SCHEMA_NAMES))
.PHONY: gen-python
target/python/%.py: $(SCHEMA_DIR)/%.yaml  tdir-python
# --no-mergeimports was causing an import error
#	gen-py-classes --no-mergeimports $(GEN_OPTS) $< > $@
	poetry run gen-py-classes --mergeimports $(GEN_OPTS) $< > $@

###  -- GRAPHQL --
gen-graphql:target/graphql/$(SCHEMA_NAME).graphql
.PHONY: gen-graphql
target/graphql/%.graphql: $(SCHEMA_DIR)/%.yaml tdir-graphql
	poetry run gen-graphql $(GEN_OPTS) $< > $@

###  -- JSON SCHEMA --
gen-jsonschema: target/jsonschema/$(SCHEMA_NAME).schema.json
.PHONY: gen-jsonschema
target/jsonschema/%.schema.json: $(SCHEMA_DIR)/%.yaml tdir-jsonschema
	poetry run gen-json-schema $(GEN_OPTS) --closed -t ingest $< > $@


###  -- SQL --
gen-sqlddl: target/sqlddl/$(SCHEMA_NAME).sql
.PHONY: gen-sqlddl
target/sqlddl/%.sql: $(SCHEMA_DIR)/%.yaml tdir-sqlddl
	poetry run gen-sqlddl $(GEN_OPTS) $< > $@

###  -- JSONLD Context --
gen-jsonld-context: target/jsonld-context/$(SCHEMA_NAME).context.jsonld
.PHONY: gen-jsonld-context
target/jsonld-context/%.context.jsonld: $(SCHEMA_DIR)/%.yaml tdir-jsonld-context
	poetry run gen-jsonld-context $(GEN_OPTS) $< > $@

###  -- SHEX --
# one file per module
gen-shex: $(patsubst %, target/shex/%.shex, $(SCHEMA_NAMES))
.PHONY: gen-shex
target/shex/%.shex: $(SCHEMA_DIR)/%.yaml tdir-shex
	poetry run gen-shex --no-mergeimports $(GEN_OPTS) $< > $@

###  -- CSV --
# one file per module
gen-csv: $(patsubst %, target/csv/%.csv, $(SCHEMA_NAMES))
.PHONY: gen-csv
target/csv/%.csv: $(SCHEMA_DIR)/%.yaml tdir-csv
	poetry run gen-csv $(GEN_OPTS) $< > $@

###  -- OWL --
# TODO: modularize imports. For now imports are merged.
gen-owl: target/owl/$(SCHEMA_NAME).owl.ttl
.PHONY: gen-owl
target/owl/%.owl.ttl: $(SCHEMA_DIR)/%.yaml tdir-owl
	poetry run gen-owl $(GEN_OPTS) $< > $@

###  -- RDF (direct mapping) --
# TODO: modularize imports. For now imports are merged.
gen-rdf: target/rdf/$(SCHEMA_NAME).ttl
.PHONY: gen-rdf
target/rdf/%.ttl: $(SCHEMA_DIR)/%.yaml tdir-rdf
	poetry run gen-rdf $(GEN_OPTS) $< > $@

###  -- LINKML --
# linkml (copy)
# one file per module
gen-linkml: target/linkml/$(SCHEMA_NAME).yaml
.PHONY: gen-linkml
target/linkml/%.yaml: $(SCHEMA_DIR)/%.yaml tdir-limkml
	cp $< > $@

gh-deploy:
# deploy documentation (note: requires documentation is in docs dir)
	poetry run mkdocs gh-deploy --remote-branch gh-pages --force --theme readthedocs

deploy-pypi:
# deploys package to pypi
# note: you need to have a pypi account
# properly configured .pypirc file
	twine upload dist/* --verbose

deploy-testpypi:
# deploys package to testpypi
# note: you need to have a testpypi account
# or properly configured .pypirc file
	twine upload -r testpypi dist/* --verbose

##  -- TEST/VALIDATE JSONSCHEMA

# datasets used test/validate the schema
SCHEMA_TEST_EXAMPLES := \

SCHEMA_TEST_EXAMPLES_INVALID := \


.PHONY: test-jsonschema
test-jsonschema: $(foreach example, $(SCHEMA_TEST_EXAMPLES), validate-$(example))

.PHONY: test-jsonschema_invalid
test-jsonschema_invalid: $(foreach example, $(SCHEMA_TEST_EXAMPLES_INVALID), validate-invalid-$(example))

validate-%: test/data/%.json jsonschema/allianceModel.schema.json
# util/validate_allianceModel_json.py -i $< # example of validating data using the cli
	poetry run jsonschema -i $< $(word 2, $^)

validate-invalid-%: test/data/invalid/%.json jsonschema/allianceModel.schema.json
	! poetry run jsonschema -i $< $(word 2, $^)

# ---------------------------------------
# Java
# ---------------------------------------
gen-java: $(patsubst %, target/java/%.java, $(SCHEMA_NAMES))
.PHONY: gen-java

target/java/%.java: $(SCHEMA_DIR)/%.yaml tdir-java
	poetry run gen-java $(JAVA_GEN_OPTS)  $< > $@

# ----------------------------------------
# TESTS
# ----------------------------------------
test: tests
tests: biolink-model.yaml env.lock pytest # jsonschema_test
	poetry run python -m unittest discover -p 'test_*.py'

pytest: biolink/model.py
	poetry run python $<