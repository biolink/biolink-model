.SECONDARY:

# ----------------------------------------
# TOP LEVEL TARGETS
# ----------------------------------------
all: build test
test: pytests
build: metamodel/context.jsonld context.jsonld build_core contrib_build_monarch contrib_build_translator
build_core: metamodel/metamodel.py metamodel/docs/index.md biolinkmodel/datamodel.py docs/index.md gen-golr-views ontology/biolink.ttl json-schema/biolink-model.json java graphql/biolink-model.graphql

contrib_build_%: dir-contrib-% contrib/%/docs/index.md contrib/%/datamodel.py contrib-golr-% contrib/%/ontology.ttl contrib/%/schema.json contrib-java-% contrib/%/%.graphql
	echo


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
	gen-jsonld-context $< > $@

metamodel/context.jsonld: meta.yaml
	gen-jsonld-context $< > $@

# ~~~~~~~~~~~~~~~~~~~~
# JSONSCHEMA -> Java
# ~~~~~~~~~~~~~~~~~~~~
json-schema/%.json: dir-json-schema %.yaml
	gen-json-schema $< > $@

contrib/%/schema.json: contrib/%.yaml
	gen-json-schema $< > $@

java: dir-json-schema json-schema/biolink-model.json
	jsonschema2pojo --source $< -T JSONSCHEMA -t java

contrib-java-%: contrib/%/schema.json
	jsonschema2pojo --source $< -T JSONSCHEMA -t contrib/$*/java

# ~~~~~~~~~~~~~~~~~~~~
# DOCS
# ~~~~~~~~~~~~~~~~~~~~
docs/index.md: biolink-model.yaml
	gen-markdown --dir docs -i $<

metamodel/docs/index.md: meta.yaml
	gen-markdown --dir metamodel/docs -i $<

contrib/%/docs/index.md: contrib/%.yaml
	gen-markdown --dir contrib/$*/docs -i $<

# ~~~~~~~~~~~~~~~~~~~~
# Ontology
# ~~~~~~~~~~~~~~~~~~~~
ontology/biolink.ttl: biolink-model.yaml
	gen-owl -o $@ $<

contrib/%/ontology.ttl: contrib/%.yaml
	gen-owl -o $@ $<


# ~~~~~~~~~~~~~~~~~~~~
# Solr
# ~~~~~~~~~~~~~~~~~~~~
gen-golr-views: dir-golr-views
	gen-golr-views -d golr-views biolink-model.yaml

contrib-golr-%: contrib/%.yaml
	gen-golr-views -d contrib/$*/golr-views contrib/$*.yaml

# ~~~~~~~~~~~~~~~~~~~~
# Python
# ~~~~~~~~~~~~~~~~~~~~
metamodel/metamodel.py: meta.yaml
	gen-py-classes $< > $@

biolinkmodel/datamodel.py: biolink-model.yaml
	gen-py-classes $< > $@

contrib/%/datamodel.py: contrib/%.yaml
	gen-py-classes $< > $@

graphviz/%.png: biolink-model.yaml
	gen-graphviz  -c $* $< -o graphviz/$*


# ~~~~~~~~~~~~~~~~~~~~
# ShEx
# ~~~~~~~~~~~~~~~~~~~~

shex/biolink-model.shex: biolink-model.yaml
	gen-shex $< > $@

# ~~~~~~~~~~~~~~~~~~~~
# Graphql
# ~~~~~~~~~~~~~~~~~~~~

graphql/biolink-model.graphql: biolink-model.yaml
	gen-graphql $< > $@

proto/biolink-model.proto: biolink-model.yaml
	gen-proto $< > $@

contrib/%/%.graphql: contrib/%.yaml
	gen-graphql $< > contrib/$*/$*.graphql

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

# ----------------------------------------
# TESTS
# ----------------------------------------
pytests:
	python -m unittest


# ----------------------------------------
# CLEAN
# ----------------------------------------
clean:
	rm -rf subsets shex proto ontology json-schema java-gen graphviz graphql golr-views contrib/go contrib/monarch docs/images/* docs/*.md

# ----------------------------------------
# UTILS
# ----------------------------------------
dir-%:
	mkdir -p $*

dir-contrib-%:
	mkdir -p contrib/$*
