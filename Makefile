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
all: install tests build

# Build the biolink model python library
python: biolink/model.py
docs: docs/index.md
jekyll-docs: docs/Classes.md

shex: biolink-model.shex biolink-modeln.shex biolink-model.shexj biolink-modeln.shexj
json-schema: json-schema/biolink-model.json
prefix-map: prefix-map/biolink-model-prefix-map.json

build: python docs/index.md gen-golr-views biolink-model.graphql gen-graphviz java context.jsonld contextn.jsonld \
json-schema/biolink-model.json biolink-model.owl.ttl biolink-model.proto shex biolink-model.ttl \
prefix-map/biolink-model-prefix-map.json

# TODO: Get this working
build_contrib: contrib_build_monarch contrib_build_translator contrib_build_go

install: env.lock



# ---------------------------------------
# Install package into build environment
# ---------------------------------------
env.lock:
	pipenv install --dev
	cp /dev/null env.lock


# ----------------------------------------
# BUILD/COMPILATION
# ----------------------------------------
# ~~~~~~~~~~~~~~~~~~~~
# Python
# ~~~~~~~~~~~~~~~~~~~~
biolink/model.py: biolink-model.yaml env.lock
	mkdir biolink 2>/dev/null || true
	pipenv run gen-py-classes $< > $@.tmp && pipenv run python $@.tmp &&  mv $@.tmp $@


# ~~~~~~~~~~~~~~~~~~~~
# DOCS
# ~~~~~~~~~~~~~~~~~~~~
docs/index.md: biolink-model.yaml env.lock
	pipenv run gen-markdown --dir docs $(imgflags) $<

# ~~~~~~~~~~~~~~~~~~~~
# JEKYLL DOCS
# ~~~~~~~~~~~~~~~~~~~~
docs/Classes.md: biolink-model.yaml env.lock
	pipenv run python script/jekyllmarkdowngen.py --dir jekyll_docs --yaml $<


# ~~~~~~~~~~~~~~~~~~~~
# Solr
# ~~~~~~~~~~~~~~~~~~~~
gen-golr-views: biolink-model.yaml dir-golr-views env.lock
	pipenv run gen-golr-views -d golr-views $<


# ~~~~~~~~~~~~~~~~~~~~
# Graphql
# ~~~~~~~~~~~~~~~~~~~~
biolink-model.graphql: biolink-model.yaml env.lock
	pipenv run gen-graphql $< > $@


# ~~~~~~~~~~~~~~~~~~~~
# Graphviz
# ~~~~~~~~~~~~~~~~~~~~
gen-graphviz: biolink-model.yaml dir-graphviz env.lock
	pipenv run gen-graphviz  -d graphviz $< -f gv
	pipenv run gen-graphviz  -d graphviz $< -f svg


# ~~~~~~~~~~~~~~~~~~~~
# Java
# ~~~~~~~~~~~~~~~~~~~~
java: json-schema/biolink-model.json dir-java env.lock
	jsonschema2pojo --source $< -T JSONSCHEMA -t java


# ~~~~~~~~~~~~~~~~~~~~
# JSON-LD CONTEXT
# ~~~~~~~~~~~~~~~~~~~~
context.jsonld: biolink-model.yaml env.lock
	touch $@
	pipenv run gen-jsonld-context $< > tmp.jsonld && ( pipenv run comparefiles tmp.jsonld $@ -c "^\s*\"comments\".*\n" && cp tmp.jsonld $@); rm tmp.jsonld

contextn.jsonld: biolink-model.yaml env.lock
	touch $@
	pipenv run gen-jsonld-context --metauris $< > tmp.jsonld && ( pipenv run comparefiles tmp.jsonld $@ -c "^\s*\"comments\".*\n" && cp tmp.jsonld $@); rm tmp.jsonld


# ~~~~~~~~~~~~~~~~~~~~
# JSON-SCHEMA
# ~~~~~~~~~~~~~~~~~~~~
json-schema/biolink-model.json: biolink-model.yaml dir-json-schema env.lock
	pipenv run gen-json-schema $< > $@


# ~~~~~~~~~~~~~~~~~~~~
# prefix-map
# ~~~~~~~~~~~~~~~~~~~~

prefix-map/biolink-model-prefix-map.json: biolink-model.yaml dir-prefix-map env.lock
	pipenv run gen-prefix-map $< > $@

# ~~~~~~~~~~~~~~~~~~~~
# Ontology
# ~~~~~~~~~~~~~~~~~~~~
biolink-model.owl.ttl: biolink-model.yaml env.lock
	pipenv run gen-owl --no-metaclasses -o $@ $<


# ~~~~~~~~~~~~~~~~~~~~
# Proto
# ~~~~~~~~~~~~~~~~~~~~
biolink-model.proto: biolink-model.yaml env.lock
	pipenv run gen-proto $< > $@

# ~~~~~~~~~~~~~~~~~~~~
# RDF
# ~~~~~~~~~~~~~~~~~~~~
biolink-model.ttl: biolink-model.yaml env.lock
	pipenv run gen-rdf -f ttl --context https://w3id.org/linkml/context.jsonld $<  > $@

# ~~~~~~~~~~~~~~~~~~~~
# ShEx
# ~~~~~~~~~~~~~~~~~~~~
biolink-model.shex: biolink-model.yaml
	pipenv run gen-shex $< > $@
biolink-modeln.shex: biolink-model.yaml
	touch $@
	pipenv run gen-shex --metauris $< > $@
biolink-model.shexj: biolink-model.yaml
	touch $@
	pipenv run gen-shex --format json $< > $@
biolink-modeln.shexj: biolink-model.yaml
	touch $@
	pipenv run gen-shex --metauris --format json $< > $@


# ----------------------------------------
# Ontology conversion
# ----------------------------------------

# ontology/%.json: ontology/%.ttl
# 	owltools $< -o -f json $@

# ontology/%.obo: ontology/%.ttl
# 	owltools $< -o -f obo --no-check $@

# ontology/%.omn: ontology/%.ttl
# 	owltools $< -o -f omn --prefix '' http://w3id.org/biolink/vocab/ --prefix def http://purl.obolibrary.org/obo/IAO_0000115 $@

# ontology/%.tree: ontology/%.json
# 	ogr --showdefs -t tree -r $< % > $@

# ontology/%.png: ontology/%.json
# 	ogr-tree -t png -o $@ -r $< %


# ~~~~~~~~~~~~~~~~~~~~
# Contrib
# ~~~~~~~~~~~~~~~~~~~~
contrib_build_%: contrib-dir-% contrib/%/docs/index.md contrib/%/datamodel.py contrib-golr-% contrib/%/%.graphql \
contrib/%/%.owl contrib/%/schema.json contrib-java-% contrib/%/%.shex
	echo

contrib/%/datamodel.py: contrib-dir-% contrib/%.yaml env.lock
	pipenv run gen-py-classes contrib/$*.yaml > tmp.py && (pipenv run comparefiles tmp.py $@ && cp tmp.py $@); rm tmp.py

contrib/%/docs/index.md: contrib/%.yaml
	pipenv run gen-markdown --dir contrib/$*/docs $<

contrib/%/datamodel.py: contrib/%.yaml
	pipenv run gen-py-classes contrib/$*.yaml > $@

contrib-golr-%: contrib-dir-% contrib/%.yaml
	pipenv run gen-golr-views -d contrib/$*/golr-views contrib/$*.yaml

contrib/%/%.graphql: contrib-dir-% contrib/%.yaml
	pipenv run gen-graphql contrib/$*.yaml > contrib/$*/$*.graphql

contrib-java-%: contrib-dir-% contrib/%/schema.json
	mkdir -p contrib/$*/java
	jsonschema2pojo --source contrib/$*/schema.json -T JSONSCHEMA -t contrib/$*/java

contrib/%/schema.json: contrib-dir-% contrib/%.yaml
	pipenv run gen-json-schema contrib/$*.yaml > $@

contrib/%/%.owl: contrib/%.yaml
	pipenv run gen-owl -o $@ contrib/$*.yaml

contrib/%/%.shex: contrib-dir-% contrib/%.yaml
	pipenv run gen-shex contrib/*.yaml > $@

# ----------------------------------------
# TESTS
# ----------------------------------------
test: tests
tests: biolink-model.yaml env.lock pytest jsonschema_test
	pipenv run python -m unittest discover -p 'test_*.py'

pytest: biolink/model.py
	pipenv run python $<

jsonschema_test: json-schema/biolink-model.json
	jsonschema $<

# ----------------------------------------
# CLEAN
# ----------------------------------------
clean:
	rm -rf contrib/go contrib/monarch contrib/translator docs/images/* docs/*.md golr-views graphql graphviz java json json-schema ontology proto rdf shex
	rm -f env.lock
	pipenv --rm

# ----------------------------------------
# UTILS
# ----------------------------------------
dir-%:
	mkdir -p $*

contrib-dir-%:
	mkdir -p contrib/$*
