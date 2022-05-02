SRC_DIR = .
SCHEMA_DIR = $(SRC_DIR)
SOURCE_FILES = biolink-model.yaml
SCHEMA_NAMES = biolink-model

SCHEMA_NAME = biolink-model
SCHEMA_SRC = $(SCHEMA_DIR)/$(SCHEMA_NAME).yaml
TGTS = python json-schema jsonld-context jsonld-contextn python sqlddl owl shex shexn shexj shexjn prefix-map rdf java
ARTIFACT_TGTS = python json-schema jsonld-context jsonld-contextn python sqlddl owl shex shexn shexj shexjn prefix-map rdf java
JAVA_GEN_OPTS = --output_directory org/biolink/model --package org.biolink.model

all: clean gen test
artifacts: clean-artifacts gen-artifacts stage-artifacts
gen: $(patsubst %,gen-%,$(TGTS))

.PHONY: all gen clean t echo test install gh-deploy clean-artifacts clean-doc clean-artifacts gen-artifacts clean-docs .FORCE

gen-artifacts: $(patsubst %,gen-%,$(ARTIFACT_TGTS))
	cp -pr target/* .
	cp -pr target/shex/* .
	cp -pr target/shexj/* biolink-modeln.shexj
	cp -pr target/shexn/* biolink-modeln.shex
	cp -pr target/shexjn/* biolink-modeln.shexj
	cp -pr target/owl/* .
	cp -pr jsonld-context/* .
	cp -pr jsonld-contextn/* .
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
	rm -rf jsonld-contextn/*
	rm -rf json-schema/*
	rm -rf sqlddl/*
	rm -rf rdf/*
	rm -rf owl/*
	rm -rf shex/*
	rm -rf shexj/*
	rm -rf shexjn/*
	rm -rf prefix-map/*


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

gen-prefix-map: target/prefix-map/$(SCHEMA_NAME)-prefix-map.json
.PHONY: gen-prefix-map
target/prefix-map/%.json: $(SCHEMA_DIR)/biolink-model.yaml  tdir-prefix-map
	poetry run gen-prefix-map $< > $@

###  -- PYTHON --
gen-python: target/python/$(SCHEMA_NAME).py
.PHONY: gen-python
target/python/%.py: $(SCHEMA_DIR)/biolink-model.yaml  tdir-python
	poetry run gen-py-classes --mergeimports $< > $@

###  -- JSON SCHEMA --
gen-json-schema: target/json-schema/$(SCHEMA_NAME).json
.PHONY: gen-json-schema
target/json-schema/%.json: $(SCHEMA_DIR)/biolink-model.yaml tdir-json-schema
	poetry run gen-json-schema --closed -t ingest $< > $@

###  -- SQL --
gen-sqlddl: target/sqlddl/$(SCHEMA_NAME).sql
.PHONY: gen-sqlddl
target/sqlddl/%.sql: $(SCHEMA_DIR)/biolink-model.yaml tdir-sqlddl
	poetry run gen-sqlddl $< > $@

###  -- JSONLD Context --
gen-jsonld-context: target/jsonld-context/context.jsonld
.PHONY: gen-jsonld-context
target/jsonld-context/context.jsonld: $(SCHEMA_DIR)/biolink-model.yaml tdir-jsonld-context
	poetry run gen-jsonld-context  $< > $@

###  -- JSONLD Context N--
gen-jsonld-contextn: target/jsonld-contextn/contextn.jsonld
.PHONY: gen-jsonld-contextn
target/jsonld-contextn/contextn.jsonld: $(SCHEMA_DIR)/biolink-model.yaml tdir-jsonld-contextn
	poetry run gen-jsonld-context --metauris $< > $@


###  -- SHEX --
# one file per module
gen-shex: $(patsubst %, target/shex/%.shex, $(SCHEMA_NAMES))
.PHONY: gen-shex
target/shex/%.shex: $(SCHEMA_DIR)/biolink-model.yaml tdir-shex
	poetry run gen-shex --no-mergeimports $< > $@

gen-shexn: $(patsubst %, target/shexn/%.shexn, $(SCHEMA_NAMES))
.PHONY: gen-shexn
target/shexn/%.shexn: $(SCHEMA_DIR)/biolink-model.yaml tdir-shexn
	poetry run gen-shex --no-mergeimports --metauris $(GEN_OPTS) $< > $@

gen-shexj: $(patsubst %, target/shexj/%.shexj, $(SCHEMA_NAMES))
.PHONY: gen-shexj
target/shexj/%.shexj: $(SCHEMA_DIR)/biolink-model.yaml tdir-shexj
	poetry run gen-shex --no-mergeimports --format json $(GEN_OPTS) $< > $@

gen-shexjn: $(patsubst %, target/shexjn/%.shexjn, $(SCHEMA_NAMES))
.PHONY: gen-shexjn
target/shexjn/%.shexjn: $(SCHEMA_DIR)/biolink-model.yaml tdir-shexjn
	poetry run gen-shex --no-mergeimports --metauris --format json $(GEN_OPTS) $< > $@


###  -- CSV --
# one file per module
gen-csv: $(patsubst %, target/csv/%.csv, $(SCHEMA_NAMES))
.PHONY: gen-csv
target/csv/%.csv: $(SCHEMA_DIR)/biolink-model.yaml tdir-csv
	poetry run gen-csv $< > $@

###  -- OWL --
# TODO: modularize imports. For now imports are merged.
gen-owl: target/owl/$(SCHEMA_NAME).owl.ttl
.PHONY: gen-owl
target/owl/%.owl.ttl: $(SCHEMA_DIR)/biolink-model.yaml tdir-owl
	poetry run gen-owl $< > $@

###  -- RDF (direct mapping) --
# TODO: modularize imports. For now imports are merged.
gen-rdf: target/rdf/$(SCHEMA_NAME).ttl
.PHONY: gen-rdf
target/rdf/%.ttl: $(SCHEMA_DIR)/biolink-model.yaml tdir-rdf
	poetry run gen-rdf $< > $@

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
	poetry run gen-golr-views $< > $@

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
