# All artifacts of the build should be preserved
.SECONDARY:

# It can be fairly expensive to regenerate the various png's in the markdown.
# There are three alternatives:
#   1) make imgflags="-i"             -- generate uml images in images subdirectory (default)
#   2) make imgflags="-i --noimages"  -- assume uml images already exist and generate links to them
#   3) make imgflags=""               -- generate uml images as inline url's
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
shacl: biolink-model.shacl.ttl
json-schema: json-schema/biolink-model.json
prefix-map: prefix-map/biolink-model-prefix-map.json

build: python docs/index.md gen-golr-views biolink-model.graphql gen-graphviz context.jsonld contextn.jsonld \
json-schema/biolink-model.json biolink-model.owl.ttl biolink-model.proto shex shacl biolink-model.ttl \
prefix-map/biolink-model-prefix-map.json gen-pydantic id-prefixes

# TODO: Get this working
build_contrib: contrib_build_monarch contrib_build_translator contrib_build_go

install: env.lock



# ---------------------------------------
# Install package into build environment
# ---------------------------------------
env.lock:
	poetry install
	cp /dev/null env.lock


# ----------------------------------------
# BUILD/COMPILATION
# ----------------------------------------
# ~~~~~~~~~~~~~~~~~~~~
# Python
# ~~~~~~~~~~~~~~~~~~~~
biolink/model.py: biolink-model.yaml env.lock
	mkdir biolink 2>/dev/null || true
	export PIPENV_DONT_LOAD_ENV=1 && poetry run gen-py-classes $< > $@.tmp && poetry run python $@.tmp &&  mv $@.tmp $@


# ~~~~~~~~~~~~~~~~~~~~
# DOCS
# ~~~~~~~~~~~~~~~~~~~~
docs/index.md: biolink-model.yaml env.lock
	poetry run gen-markdown --dir docs $(imgflags) $<

# ~~~~~~~~~~~~~~~~~~~~
# JEKYLL DOCS
# ~~~~~~~~~~~~~~~~~~~~
docs/Classes.md: biolink-model.yaml env.lock
	poetry run python script/jekyllmarkdowngen.py --dir jekyll_docs --yaml $<


# ~~~~~~~~~~~~~~~~~~~~
# Solr
# ~~~~~~~~~~~~~~~~~~~~
gen-golr-views: biolink-model.yaml dir-golr-views env.lock
	poetry run gen-golr-views -d golr-views $<


# ~~~~~~~~~~~~~~~~~~~~
# pydantic
# ~~~~~~~~~~~~~~~~~~~~
gen-pydantic: biolink-model.yaml dir-pydantic env.lock
	poetry run gen-pydantic $< > biolink/pydanticmodel.py


# ~~~~~~~~~~~~~~~~~~~~
# Graphql
# ~~~~~~~~~~~~~~~~~~~~
biolink-model.graphql: biolink-model.yaml env.lock
	poetry run gen-graphql $< > $@


# ~~~~~~~~~~~~~~~~~~~~
# Graphviz
# ~~~~~~~~~~~~~~~~~~~~
gen-graphviz: biolink-model.yaml dir-graphviz env.lock
	poetry run gen-graphviz  -d graphviz $< -f gv
	poetry run gen-graphviz  -d graphviz $< -f svg


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
	poetry run gen-jsonld-context $< > tmp.jsonld && ( poetry run comparefiles tmp.jsonld $@ -c "^\s*\"comments\".*\n" && cp tmp.jsonld $@); rm tmp.jsonld

contextn.jsonld: biolink-model.yaml env.lock
	touch $@
	poetry run gen-jsonld-context --metauris $< > tmp.jsonld && ( poetry run comparefiles tmp.jsonld $@ -c "^\s*\"comments\".*\n" && cp tmp.jsonld $@); rm tmp.jsonld


# ~~~~~~~~~~~~~~~~~~~~
# JSON-SCHEMA
# ~~~~~~~~~~~~~~~~~~~~
json-schema/biolink-model.json: biolink-model.yaml dir-json-schema env.lock
	poetry run gen-json-schema $< > $@


# ~~~~~~~~~~~~~~~~~~~~
# prefix-map
# ~~~~~~~~~~~~~~~~~~~~

prefix-map/biolink-model-prefix-map.json: biolink-model.yaml dir-prefix-map env.lock
	poetry run gen-prefix-map $< > $@

id-prefixes:
	poetry run gen-python prefix-map/class_prefixes.yaml > script/classprefixes.py
	cd script && poetry run python id_prefixes.py
# ~~~~~~~~~~~~~~~~~~~~
# Ontology
# ~~~~~~~~~~~~~~~~~~~~
biolink-model.owl.ttl: biolink-model.yaml env.lock
	poetry run gen-owl --no-metaclasses -o $@ $<


# ~~~~~~~~~~~~~~~~~~~~
# Proto
# ~~~~~~~~~~~~~~~~~~~~
biolink-model.proto: biolink-model.yaml env.lock
	poetry run gen-proto $< > $@

# ~~~~~~~~~~~~~~~~~~~~
# RDF
# ~~~~~~~~~~~~~~~~~~~~
biolink-model.ttl: biolink-model.yaml env.lock
	poetry run gen-rdf -f ttl --context https://w3id.org/linkml/context.jsonld $<  > $@

# ~~~~~~~~~~~~~~~~~~~~
# ShEx
# ~~~~~~~~~~~~~~~~~~~~
biolink-modeel.shex: biolink-model.yaml
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

# ~~~~~~~~~~~~~~~~~~~~
# SHACL
# ~~~~~~~~~~~~~~~~~~~~
biolink-model.shacl.ttl: biolink-model.yaml
	poetry run gen-shacl $< > $@

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
contrib/%/%.owl contrib/%/schema.json contrib-java-% contrib/%/%.shex contrib/%/%.shacl.ttl
	echo

contrib/%/datamodel.py: contrib-dir-% contrib/%.yaml env.lock
	poetry run gen-py-classes contrib/$*.yaml > tmp.py && (poetry run comparefiles tmp.py $@ && cp tmp.py $@); rm tmp.py

contrib/%/docs/index.md: contrib/%.yaml
	poetry run gen-markdown --dir contrib/$*/docs $<

contrib/%/datamodel.py: contrib/%.yaml
	poetry run gen-py-classes contrib/$*.yaml > $@

contrib-golr-%: contrib-dir-% contrib/%.yaml
	poetry run gen-golr-views -d contrib/$*/golr-views contrib/$*.yaml

contrib-pydantic-%: contrib-dir-% contrib/%.yaml
	poetry run gen-pydantic -d contrib/$*/pydantic contrib/$*.yaml


contrib/%/%.graphql: contrib-dir-% contrib/%.yaml
	poetry run gen-graphql contrib/$*.yaml > contrib/$*/$*.graphql

contrib-java-%: contrib-dir-% contrib/%/schema.json
	mkdir -p contrib/$*/java
	jsonschema2pojo --source contrib/$*/schema.json -T JSONSCHEMA -t contrib/$*/java

contrib/%/schema.json: contrib-dir-% contrib/%.yaml
	poetry run gen-json-schema contrib/$*.yaml > $@

contrib/%/%.owl: contrib/%.yaml
	poetry run gen-owl -o $@ contrib/$*.yaml

contrib/%/%.shex: contrib-dir-% contrib/%.yaml
	poetry run gen-shex contrib/*.yaml > $@

contrib/%/%.shacl.ttl: contrib-dir-% contrib/%.yaml
	poetry run gen-shacl contrib/*.yaml > $@

# ----------------------------------------
# TESTS
# ----------------------------------------
test: tests
tests: biolink-model.yaml env.lock pytest # jsonschema_test
	poetry run python -m unittest discover -p 'test_*.py'
	poetry run codespell
	poetry run yamllint -c .yamllint-config biolink-model.yaml
	poetry run python scripts/verify_infores.py

pytest: biolink/model.py
	poetry run python $<

# jsonschema_test: json-schema/biolink-model.json
#	jsonschema $<

# ----------------------------------------
# CLEAN
# ----------------------------------------
clean:
	rm -rf contrib/go contrib/monarch contrib/translator docs/images/* docs/*.md golr-views graphql graphviz java json json-schema ontology proto rdf shex shacl pydantic
	rm -f env.lock
	poetry --rm

# ----------------------------------------
# UTILS
# ----------------------------------------
dir-%:
	mkdir -p $*

contrib-dir-%:
	mkdir -p contrib/$*
