# All artifacts of the build should be preserved
.SECONDARY:

# It can be fairly expensive to regenerate the various png's in the markdown.
# There are three alternatives:
#   1) make imgflags="-i"             -- generate uml images in images subdirectory (default)
#   2) make imgflags="-i --noimages"  -- assume uml images already exist and generate links to them
#   3) make imgflags=""               -- genrate uml images as inline url's
imgflags?=-i


# ----------------------------------------
# TOP LEVEL TARGETS
# ----------------------------------------
all: build tests

build: python gen-golr-views biolink-model.graphql gen-graphviz context.jsonld contextn.jsonld \
json-schema/biolink-model.json biolink-model.owl.ttl biolink-model.proto shex biolink-model.ttl \
prefix-map/biolink-model-prefix-map.json

# ----------------------------------------
# BUILD/COMPILATION
# ----------------------------------------
# ~~~~~~~~~~~~~~~~~~~~
# Python
# ~~~~~~~~~~~~~~~~~~~~

# Build the biolink model python library
python: biolink/model.py

biolink/model.py: biolink-model.yaml
	mkdir biolink 2>/dev/null || true
	export poetry_DONT_LOAD_ENV=1 && poetry run gen-py-classes $< > $@.tmp && poetry run python $@.tmp &&  mv $@.tmp $@

# ~~~~~~~~~~~~~~~~~~~~~~
# doc-gen with templates
# ~~~~~~~~~~~~~~~~~~~~~~

gendoc:
	poetry run gen-doc biolink-model.yaml --directory docs --template-directory doc_templates

# ~~~~~~~~~~~~~~~~~~~~
# Solr
# ~~~~~~~~~~~~~~~~~~~~
gen-golr-views: biolink-model.yaml dir-golr-views
	poetry run gen-golr-views -d golr-views $<


# ~~~~~~~~~~~~~~~~~~~~
# Graphql
# ~~~~~~~~~~~~~~~~~~~~
biolink-model.graphql: biolink-model.yaml
	poetry run gen-graphql $< > $@

# ~~~~~~~~~~~~~~~~~~~~
# Graphviz
# ~~~~~~~~~~~~~~~~~~~~
gen-graphviz: biolink-model.yaml dir-graphviz
	poetry run gen-graphviz  -d graphviz $< -f gv
	poetry run gen-graphviz  -d graphviz $< -f svg


# ~~~~~~~~~~~~~~~~~~~~
# Java
# ~~~~~~~~~~~~~~~~~~~~
java: json-schema/biolink-model.json dir-java
	jsonschema2pojo --source $< -T JSONSCHEMA -t java


# ~~~~~~~~~~~~~~~~~~~~
# JSON-LD CONTEXT
# ~~~~~~~~~~~~~~~~~~~~
context.jsonld: biolink-model.yaml
	touch $@
	poetry run gen-jsonld-context $< > tmp.jsonld && ( poetry run comparefiles tmp.jsonld $@ -c "^\s*\"comments\".*\n" && cp tmp.jsonld $@); rm tmp.jsonld

contextn.jsonld: biolink-model.yaml
	touch $@
	poetry run gen-jsonld-context --metauris $< > tmp.jsonld && ( poetry run comparefiles tmp.jsonld $@ -c "^\s*\"comments\".*\n" && cp tmp.jsonld $@); rm tmp.jsonld


# ~~~~~~~~~~~~~~~~~~~~
# JSON-SCHEMA
# ~~~~~~~~~~~~~~~~~~~~
json-schema: json-schema/biolink-model.json

json-schema/biolink-model.json: biolink-model.yaml dir-json-schema
	poetry run gen-json-schema $< > $@


# ~~~~~~~~~~~~~~~~~~~~
# prefix-map
# ~~~~~~~~~~~~~~~~~~~~

prefix-map: prefix-map/biolink-model-prefix-map.json

prefix-map/biolink-model-prefix-map.json: biolink-model.yaml dir-prefix-map
	poetry run gen-prefix-map $< > $@

# ~~~~~~~~~~~~~~~~~~~~
# Ontology
# ~~~~~~~~~~~~~~~~~~~~
biolink-model.owl.ttl: biolink-model.yaml
	poetry run gen-owl --no-metaclasses -o $@ $<


# ~~~~~~~~~~~~~~~~~~~~
# Proto
# ~~~~~~~~~~~~~~~~~~~~
biolink-model.proto: biolink-model.yaml
	poetry run gen-proto $< > $@

# ~~~~~~~~~~~~~~~~~~~~
# RDF
# ~~~~~~~~~~~~~~~~~~~~
biolink-model.ttl: biolink-model.yaml
	poetry run gen-rdf -f ttl --context https://w3id.org/linkml/context.jsonld $<  > $@

# ~~~~~~~~~~~~~~~~~~~~
# ShEx
# ~~~~~~~~~~~~~~~~~~~~


shex: biolink-model.shex biolink-modeln.shex biolink-model.shexj biolink-modeln.shexj

biolink-model.shex: biolink-model.yaml
	poetry run gen-shex $< > $@
biolink-modeln.shex: biolink-model.yaml
	touch $@
	poetry run gen-shex --metauris $< > $@
biolink-model.shexj: biolink-model.yaml
	touch $@
	poetry run gen-shex --format json $< > $@
biolink-modeln.shexj: biolink-model.yaml
	touch $@
	poetry run gen-shex --metauris --format json $< > $@

# ----------------------------------------
# TESTS
# ----------------------------------------
test: tests
tests: biolink-model.yaml env.lock pytest # jsonschema_test
	poetry run python -m unittest discover -p 'test_*.py'

pytest: biolink/model.py
	poetry run python $<

# jsonschema_test: json-schema/biolink-model.json
#	jsonschema $<


### gh pages ###
gh-deploy:
# deploy documentation (note: requires documentation is in docs dir)
	poetry run mkdocs gh-deploy --remote-branch gh-pages --force --theme readthedocs


# ----------------------------------------
# CLEAN
# ----------------------------------------
clean-docs:
	rm -rf docs/images/* docs/*.md

clean:
	rm -rf docs/images/* docs/*.md golr-views graphql graphviz java json
	rm -rf json-schema ontology proto rdf shex

# ----------------------------------------
# UTILS
# ----------------------------------------
dir-%:
	mkdir -p $*
