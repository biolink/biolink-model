SRC_DIR = .
SCHEMA_DIR = $(SRC_DIR)
SOURCE_FILES = biolink-model.yaml
SCHEMA_NAMES = biolink-model

SCHEMA_NAME = biolink-model
SCHEMA_SRC = $(SCHEMA_DIR)/$(SCHEMA_NAME).yaml
TGTS = python json-schema jsonld-context python sqlddl owl shex prefix-map rdf java
ARTIFACT_TGTS = python json-schema jsonld-context python sqlddl owl shex prefix-map rdf java
JAVA_GEN_OPTS = --output_directory org/biolink/model --package org.biolink.model
DDL_GEN_OPTS = --sqla-file target/sqla-files/

all: clean gen test
artifacts: clean-artifacts gen-artifacts stage-artifacts
gen: $(patsubst %,gen-%,$(TGTS))

.PHONY: all gen clean t echo test install gh-deploy clean-artifacts clean-doc clean-artifacts gen-artifacts clean-docs .FORCE

gen-artifacts: $(patsubst %,gen-%,$(ARTIFACT_TGTS))
	cp -pr target/* .
	cp -pr target/shex/* .
	cp -pr target/owl/* .
	cp -pr jsonld-context/* .
	cp -pr python/* biolink/model.py
	cp -pr owl/* .
	cp -pr rdf/* .

clean:
	rm -rf target/*

clean-json-schema:
	rm -rf target/*
	rm -rf json-schema/*

clean-artifacts:
	rm -rf target/*
	rm -rf python/*
	rm -rf jsonld-context/*
	rm -rf json-schema/*
	rm -rf sqlddl/*
	rm -rf rdf/*
	rm -rf owl/*

docs:
	mkdir -p $@
	mkdir -p $@/images
	mkdir -p $@/types

clean-docs:
	rm -rf docs/images/*
	rm -rf docs/types/*
	rm -rf docs/
	mkdir -p docs
	mkdir -p docs/images
	mkdir -p docs/types


gen-docs:
	poetry run gen-doc biolink-model.yaml --directory target/docs --template-directory doc_templates
	cp -pr target/docs/ .
	cp css/extra_css.css docs/
	cp README.md docs/
	cp images/biolink-logo.png docs/

t:
	echo $(SCHEMA_NAMES)

echo:
	echo $(patsubst %,gen-%,$(TGTS))

install:
	poetry install

tdir-%:
	mkdir -p target/$*

###  -- PYTHON --
gen-prefix-map: target/prefix-map/$(SCHEMA_NAME)-prefix-map.json
.PHONY: gen-prefix-map
target/prefix-map/%.json: $(SCHEMA_DIR)/biolink-model.yaml  tdir-prefix-map
	poetry run gen-prefix-map $(GEN_OPTS) $< > $@

# add more logging?
# some docs pages not being created
# usage of mkdocs.yml attributes like analytics?

###  -- PYTHON --
gen-python: $(patsubst %, target/python/%.py, $(SCHEMA_NAMES))
.PHONY: gen-python
target/python/%.py: $(SCHEMA_DIR)/biolink-model.yaml  tdir-python
	poetry run gen-py-classes --mergeimports $(GEN_OPTS) $< > $@

###  -- JSON SCHEMA --
gen-json-schema: target/json-schema/$(SCHEMA_NAME).json
.PHONY: gen-json-schema
target/json-schema/%.json: $(SCHEMA_DIR)/biolink-model.yaml tdir-json-schema
	poetry run gen-json-schema $(GEN_OPTS) --closed -t ingest $< > $@

###  -- SQL --
gen-sqlddl: target/sqlddl/$(SCHEMA_NAME).sql
.PHONY: gen-sqlddl
target/sqlddl/%.sql: $(SCHEMA_DIR)/biolink-model.yaml tdir-sqlddl
	poetry run gen-sqlddl $(GEN_OPTS) $< > $@

###  -- JSONLD Context --
gen-jsonld-context: target/jsonld-context/context.jsonld
.PHONY: gen-jsonld-context
target/jsonld-context/context.jsonld: $(SCHEMA_DIR)/biolink-model.yaml tdir-jsonld-context
	poetry run gen-jsonld-context $(GEN_OPTS) $< > $@

###  -- SHEX --
# one file per module
gen-shex: $(patsubst %, target/shex/%.shex, $(SCHEMA_NAMES))
.PHONY: gen-shex
target/shex/%.shex: $(SCHEMA_DIR)/biolink-model.yaml tdir-shex
	poetry run gen-shex --no-mergeimports $(GEN_OPTS) $< > $@

###  -- CSV --
# one file per module
gen-csv: $(patsubst %, target/csv/%.csv, $(SCHEMA_NAMES))
.PHONY: gen-csv
target/csv/%.csv: $(SCHEMA_DIR)/biolink-model.yaml tdir-csv
	poetry run gen-csv $(GEN_OPTS) $< > $@

###  -- OWL --
# TODO: modularize imports. For now imports are merged.
gen-owl: target/owl/$(SCHEMA_NAME).owl.ttl
.PHONY: gen-owl
target/owl/%.owl.ttl: $(SCHEMA_DIR)/biolink-model.yaml tdir-owl
	poetry run gen-owl $(GEN_OPTS) $< > $@

###  -- RDF (direct mapping) --
# TODO: modularize imports. For now imports are merged.
gen-rdf: target/rdf/$(SCHEMA_NAME).ttl
.PHONY: gen-rdf
target/rdf/%.ttl: $(SCHEMA_DIR)/biolink-model.yaml tdir-rdf
	poetry run gen-rdf $(GEN_OPTS) $< > $@

###  -- LINKML --
# linkml (copy)
# one file per module
gen-linkml: target/linkml/$(SCHEMA_NAME).yaml
.PHONY: gen-linkml
target/linkml/%.yaml: $(SCHEMA_DIR)/biolink-model.yaml tdir-limkml
	cp $< > $@

# ~~~~~~~~~~~~~~~~~~~~
# Solr
# ~~~~~~~~~~~~~~~~~~~~
gen-golr-views: target/golr-views/$(SCHEMA_NAME).yaml
.PHONY: gen-golr-views
	poetry run gen-golr-views -d golr-views $<
target/golr-views/%.yaml: $(SCHEMA_DIR)/biolink-model.yaml tdir-golr-views
	poetry run gen-golr-views $(GEN_OPTS) $< > $@

# ~~~~~~~~~~~~~~~~~~~~
# Graphql
# ~~~~~~~~~~~~~~~~~~~~
gen-graphql: target/graphql/$(SCHEMA_NAME).yaml
.PHONY: gen-graphql
	poetry run gen-graphql -d graphql $<
target/graphql/%.graphql: $(SCHEMA_DIR)/biolink-model.yaml tdir-graphql
	poetry run gen-graphql $< > $@

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


# ---------------------------------------
# Java
# ---------------------------------------
gen-java: $(patsubst %, target/java/%.java, $(SCHEMA_NAMES))
.PHONY: gen-java
target/java/%.java: $(SCHEMA_DIR)/biolink-model.yaml tdir-java
	poetry run gen-java $(JAVA_GEN_OPTS)  $< > $@


# ----------------------------------------
# TESTS
# ----------------------------------------
test: tests

tests: biolink-model.yaml pytest # jsonschema_test
	poetry run python -m unittest discover -p 'test_*.py'

pytest: biolink/model.py
	poetry run python $<
