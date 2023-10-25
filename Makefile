MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help
.DELETE_ON_ERROR:
.SUFFIXES:
.SECONDARY:

RUN = poetry run
# get values from about.yaml file
SCHEMA_NAME = biolink-model
SOURCE_SCHEMA_PATH = biolink-model.yaml
SOURCE_SCHEMA_DIR = ./
SRC = src
DEST = project
PYMODEL = $(SRC)/biolink
DOCDIR = docs


GEN_PARGS =
ifdef LINKML_GENERATORS_PROJECT_ARGS
GEN_PARGS = ${LINKML_GENERATORS_PROJECT_ARGS}
endif

GEN_DARGS =
ifdef LINKML_GENERATORS_MARKDOWN_ARGS
GEN_DARGS = ${LINKML_GENERATORS_MARKDOWN_ARGS}
endif


# basename of a YAML file in model/
.PHONY: all clean

# note: "help" MUST be the first target in the file,
# when the user types "make" they should get help info
help: status
	@echo ""
	@echo "make setup -- initial setup (run this first)"
	@echo "make site -- makes site locally"
	@echo "make test -- runs tests"
	@echo "make lint -- perform linting"
	@echo "make testdoc -- builds docs and runs local test server"
	@echo "make deploy -- deploys site"
	@echo "make update -- updates linkml version"
	@echo "make help -- show this help"
	@echo ""

status: check-config
	@echo "Project: $(SCHEMA_NAME)"
	@echo "Source: $(SOURCE_SCHEMA_PATH)"

install:
	poetry install

update: update-linkml


# todo: consider pinning to template
update-linkml:
	poetry add -D linkml@latest

# EXPERIMENTAL
create-data-harmonizer:
	npm init data-harmonizer $(SOURCE_SCHEMA_PATH)

all: site gen-viz-data
site: gen-project gendoc
%.yaml: gen-project
deploy: all mkd-gh-deploy

compile-sheets:
	$(RUN) sheets2linkml --gsheet-id $(SHEET_ID) $(SHEET_TABS) > $(SHEET_MODULE_PATH).tmp && mv $(SHEET_MODULE_PATH).tmp $(SHEET_MODULE_PATH)

# In future this will be done by conversion
gen-examples:
	cp src/data/examples/* $(EXAMPLEDIR)

# generates all project files

gen-project: $(PYMODEL)
	$(RUN) gen-project ${GEN_PARGS} -d $(DEST) $(SOURCE_SCHEMA_PATH) && mv $(DEST)/*.py $(PYMODEL)


test: test-schema test-python test-examples

test-schema:
	$(RUN) gen-project ${GEN_PARGS} -d tmp $(SOURCE_SCHEMA_PATH)

test-python:
	$(RUN) python -m unittest discover

lint:
	$(RUN) linkml-lint $(SOURCE_SCHEMA_PATH)

check-config:
	@(grep my-datamodel about.yaml > /dev/null && printf "\n**Project not configured**:\n\n  - Remember to edit 'about.yaml'\n\n" || exit 0)


# Test documentation locally
serve: mkd-serve

# Python datamodel
$(PYMODEL):
	mkdir -p $@

$(DOCDIR):
	mkdir -p $@

gendoc: $(DOCDIR)
	cp $(SRC)/docs/*md $(DOCDIR) ; \
	$(RUN) gen-doc ${GEN_DARGS} -d $(DOCDIR) $(SOURCE_SCHEMA_PATH)

testdoc: gendoc serve

MKDOCS = $(RUN) mkdocs
mkd-%:
	$(MKDOCS) $*

PROJECT_FOLDERS = sqlschema shex shacl protobuf prefixmap owl jsonschema jsonld graphql excel
git-init-add: git-init git-add git-commit git-status
git-init:
	git init
git-add: .cruft.json
	git add .gitignore .github .cruft.json Makefile LICENSE *.md examples utils about.yaml mkdocs.yml poetry.lock project.Makefile pyproject.toml src/testviz/schema/*yaml src/*/datamodel/*py src/data src/docs tests src/*/_version.py
	git add $(patsubst %, project/%, $(PROJECT_FOLDERS))
git-commit:
	git commit -m 'chore: initial commit' -a
git-status:
	git status


infores:
	poetry run gen-python information-resource.yaml > information_resource.py

# ~~~~~~~~~~~~~~~~~~~~
# pydantic
# ~~~~~~~~~~~~~~~~~~~~
gen-pydantic: biolink-model.yaml dir-pydantic env.lock
	poetry run gen-pydantic $< > biolink/pydanticmodel.py
	# poetry run gen-pydantic --pydantic_version 1 $< > biolink/pydanticmodel_v1.py


gen-pydantic-v2: biolink-model.yaml dir-pydantic env.lock
	poetry run gen-pydantic --pydantic_version 2 $< > biolink/pydanticmodel_v2.py
	# poetry run gen-pydantic --pydantic_version 2 $< > biolink/pydanticmodel.py


# ~~~~~~~~~~~~~~~~~~~~
# prefix-map
# ~~~~~~~~~~~~~~~~~~~~

prefix-map/biolink-model-prefix-map.json: biolink-model.yaml dir-prefix-map env.lock
	poetry run gen-prefix-map $< > $@

id-prefixes:
	poetry run gen-python prefix-map/class_prefixes.yaml > scripts/classprefixes.py
	cd scripts && poetry run python id_prefixes.py

# ----------------------------------------
# TESTS
# ----------------------------------------
test: tests
tests: unittest discover -p 'test_*.py'
	poetry run codespell
	poetry run yamllint -c .yamllint-config biolink-model.yaml
	poetry run yamllint -c .yamllint-config infores_catalog.yaml
	poetry run python scripts/verify_infores.py

spell:
	poetry run codespell

pytest: biolink/model.py
	poetry run python $<

# only necessary if setting up via cookiecutter
.cruft.json:
	echo "creating a stub for .cruft.json. IMPORTANT: setup via cruft not cookiecutter recommended!" ; \
	touch $@

clean:
	rm -rf $(DEST)
	rm -rf tmp
	rm -fr docs/*
	rm -fr $(PYMODEL)/*

include project.Makefile