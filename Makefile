# All artifacts of the build should be preserved
.SECONDARY:

# It can be fairly expensive to regenerate the various png's in the markdown.
# There are three alternatives:
#   1) make imgflags="-i"             -- generate uml images in images subdirectory (default)
#   2) make imgflags="-i --noimages"  -- assume uml images already exist and generate links to them
#   3) make imgflags=""               -- genrate uml images as inline url's
imgflags?=-i --noimages


# ----------------------------------------
# TOP LEVEL TARGETS
# ----------------------------------------
all: build test
test: pytests
shex: shex/meta.ttl shex/biolink-model.ttl
rdf: rdf/meta.ttl rdf/biolink-model.ttl
docs: metamodel/docs/index.md docs/index.md

build: metamodel/context.jsonld context.jsonld build_core contrib_build_monarch contrib_build_translator contrib_build_go
build_core: metamodel/docs/index.md biolinkmodel/datamodel.py docs/index.md gen-golr-views \
ontology/biolink.ttl json-schema/biolink-model.json java graphql/biolink-model.graphql proto/biolink-model.proto \
gen-graphviz rdf/meta.ttl shex/meta.ttl rdf/biolink-model.ttl shex/biolink-model.ttl

contrib_build_%: contrib-dir-% contrib/%/docs/index.md contrib/%/datamodel.py contrib-golr-% contrib/%/ontology.ttl \
contrib/%/schema.json contrib-java-% contrib/%/%.graphql contrib/%/shex
	echo

install:
	pip install -e . --upgrade


# ----------------------------------------
# BUILD/COMPILATION
# ----------------------------------------
# ~~~~~~~~~~~~~~~~~~~~
# CSV
# ~~~~~~~~~~~~~~~~~~~~
kbsync: subsets/biological_entity.csv
	cp $< ../translator-knowledge-beacon/api/types.csv

subsets/biological_entity.csv: biolink-model.yaml
	gen-csv -r 'biological entity' biolink-model.yaml > $@.tmp && mv $@.tmp $@

biolink-model.tsv: biolink-model.yaml
	gen-csv -f tsv biolink-model.yaml > $@.tmp && mv $@.tmp $@

# ~~~~~~~~~~~~~~~~~~~~
# JSON-LD CONTEXT
# ~~~~~~~~~~~~~~~~~~~~
context.jsonld: biolink-model.yaml
	gen-jsonld-context $< > tmp.jsonld && (comparefiles tmp.jsonld $@ -c "^\s*\"comments\".*\n" && cp tmp.jsonld $@); rm tmp.jsonld

metamodel/context.jsonld: meta.yaml
	gen-jsonld-context $< > tmp.jsonld && (comparefiles tmp.jsonld $@ -c "^\s*\"comments\".*\n" && cp tmp.jsonld $@); rm tmp.jsonld

# ~~~~~~~~~~~~~~~~~~~~
# JSONSCHEMA -> Java
# ~~~~~~~~~~~~~~~~~~~~
json-schema/%.json: dir-json-schema %.yaml
	gen-json-schema $*.yaml > $@

contrib/%/schema.json: contrib-dir-% contrib/%.yaml
	gen-json-schema contrib/$*.yaml > $@

java: dir-java json-schema/biolink-model.json
	jsonschema2pojo --source json-schema/biolink-model.json -T JSONSCHEMA -t java

contrib-java-%: contrib-dir-% contrib/%/schema.json
	mkdir -p contrib/$*/java
	jsonschema2pojo --source contrib/$*/schema.json -T JSONSCHEMA -t contrib/$*/java

# ~~~~~~~~~~~~~~~~~~~~
# DOCS
# ~~~~~~~~~~~~~~~~~~~~
docs/index.md: biolink-model.yaml
	gen-markdown --dir docs $(imgflags) $<

metamodel/docs/index.md: meta.yaml
	gen-markdown --dir metamodel/docs $(imgflags) $<

contrib/%/docs/index.md: contrib/%.yaml
	gen-markdown --dir contrib/$*/docs $<

# ~~~~~~~~~~~~~~~~~~~~
# Ontology
# ~~~~~~~~~~~~~~~~~~~~
ontology/biolink.ttl: dir-ontology biolink-model.yaml
	gen-owl -o $@ biolink-model.yaml

contrib/%/ontology.ttl: contrib-dir-% contrib/%.yaml
	gen-owl -o $@ contrib/$*.yaml

# ~~~~~~~~~~~~~~~~~~~~
# RDF
# ~~~~~~~~~~~~~~~~~~~~
rdf/%.ttl: dir-rdf metamodel/context.jsonld meta.yaml
	gen-rdf $*.yaml -f ttl --context metamodel/context.jsonld > rdf/$*.ttl


contrib/%/datamodel.py: contrib-dir-% contrib/%.yaml
	gen-py-classes contrib/$*.yaml > $@

gen-graphviz: dir-graphviz biolink-model.yaml
	gen-graphviz  -d graphviz biolink-model.yaml

# ~~~~~~~~~~~~~~~~~~~~
# Solr
# ~~~~~~~~~~~~~~~~~~~~
gen-golr-views: dir-golr-views biolink-model.yaml
	gen-golr-views -d golr-views biolink-model.yaml

contrib-golr-%: contrib/%.yaml
	mkdir -p contrib/$*/golr-views
	gen-golr-views -d contrib/$*/golr-views contrib/$*.yaml

# ~~~~~~~~~~~~~~~~~~~~
# Python
# ~~~~~~~~~~~~~~~~~~~~
contrib/%/datamodel.py: contrib-dir-% contrib/%.yaml
	gen-py-classes contrib/$*.yaml > tmp.py && (comparefiles tmp.py $@ && cp tmp.py $@); rm tmp.py

# ~~~~~~~~~~~~~~~~~~~~
# ShEx
# ~~~~~~~~~~~~~~~~~~~~
shex/%.ttl: dir-shex %.yaml
	gen-shex $*.yaml -f rdf > shex/$*.ttl
	gen-shex $*.yaml -c -f rdf > shex/$*nc.ttl
	gen-shex $*.yaml -f shex > shex/$*.shex
	gen-shex $*.yaml -c -f shex > shex/$*nc.shex
	gen-shex $*.yaml -f json > shex/$*.json
	gen-shex $*.yaml -c -f json > shex/$*nc.json

contrib/%/shex:
	mkdir -p contrib/$*/shex
	gen-shex contrib/$*.yaml -f rdf > contrib/$*/shex/$*.ttl
	gen-shex contrib/$*.yaml -c -f rdf > contrib/$*/shex/$*nc.ttl
	gen-shex contrib/$*.yaml -f shex > contrib/$*/shex/$*.shex
	gen-shex contrib/$*.yaml -c -f shex > contrib/$*/shex/$*nc.shex
	gen-shex contrib/$*.yaml -f json > contrib/$*/shex/$*.json
	gen-shex contrib/$*.yaml -c -f json > contrib/$*/shex/$*nc.json


# ~~~~~~~~~~~~~~~~~~~~
# Graphql
# ~~~~~~~~~~~~~~~~~~~~

graphql/biolink-model.graphql: dir-graphql biolink-model.yaml
	gen-graphql biolink-model.yaml > $@

proto/biolink-model.proto: dir-proto biolink-model.yaml
	gen-proto biolink-model.yaml > $@

contrib/%/%.graphql: contrib-dir-% contrib/%.yaml
	gen-graphql contrib/$*.yaml > contrib/$*/$*.graphql

# ----------------------------------------
# Ontology conversion
# ----------------------------------------

ontology/%.json: ontology/%.ttl
	owltools $< -o -f json $@

ontology/%.obo: ontology/%.ttl
	owltools $< -o -f obo --no-check $@

ontology/%.omn: ontology/%.ttl
	owltools $< -o -f omn --prefix '' http://bioentity.io/vocab/ --prefix def http://purl.obolibrary.org/obo/IAO_0000115 $@

ontology/%.tree: ontology/%.json
	ogr --showdefs -t tree -r $< % > $@

ontology/%.png: ontology/%.json
	ogr-tree -t png -o $@ -r $< %

# ~~~~~~~~~~~~~~~~~~~~
# Update the metamodel - not part of the main build.  Use this method when meta.yaml has changed
# ~~~~~~~~~~~~~~~~~~~~
MM = metamodel/metamodel.py
BMM = biolinkmodel/datamodel.py

regen-mm:
	gen-py-classes meta.yaml > tmp.py && python tmp.py && (comparefiles typ.py $(MM) && cp $(MM) $(MM)-PREV && cp tmp.py $(MM)); rm tmp.py
	gen-py-classes biolink-model.yaml > tmp.py && python tmp.py && c&& (comparefiles typ.py $(BMM) && cp $(BMM) $(BMM)-PREV && cp tmp.py $(BMM)); rm tmp.py

# ----------------------------------------
# TESTS
# ----------------------------------------
pytests:
	python -m unittest discover -p 'test_*.py'


# ----------------------------------------
# CLEAN
# ----------------------------------------
clean:
	rm -rf subsets java shex proto ontology json-schema graphviz graphql golr-views contrib/go contrib/monarch contrib/translator docs/images/* docs/*.md

# ----------------------------------------
# UTILS
# ----------------------------------------
dir-%:
	mkdir -p $*

contrib-dir-%:
	mkdir -p contrib/$*
