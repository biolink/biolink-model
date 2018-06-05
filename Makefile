# ----------------------------------------
# TOP LEVEL TARGETS
# ----------------------------------------
all: build test 
test: pytests
build: context.jsonld build_core contrib_build_monarch contrib_build_translator

build_core: metamodel/metamodel.py biolinkmodel/datamodel.py docs/index.md gen-golr-views ontology/biolink.ttl json-schema/biolink-model.json java graphql/biolink-model.graphql

contrib_build_%: contrib/%/docs/index.md contrib/%/datamodel.py contrib/%/schema.py contrib/%-golr contrib/%/ontology.ttl contrib/%/schema.json contrib/%-java contrib/%/%.graphql
	echo hi


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

# ~~~~~~~~~~~~~~~~~~~~
# JSONSCHEMA -> Java
# ~~~~~~~~~~~~~~~~~~~~
json-schema/%.json: %.yaml
	gen-json-schema $< > $@

contrib/%/schema.json: contrib/%.yaml
	gen-json-schema $< > $@

JSONSCHEMA2POJO = $(HOME)/src/jsonschema2pojo/bin/jsonschema2pojo
java: json-schema/biolink-model.json
	$(JSONSCHEMA2POJO) --source $< -T JSONSCHEMA -t java-gen

contrib/%-java: contrib/%/schema.json
	$(JSONSCHEMA2POJO) --source $< -T JSONSCHEMA -t contrib/$*/java

# ~~~~~~~~~~~~~~~~~~~~
# DOCS
# ~~~~~~~~~~~~~~~~~~~~
docs/index.md: biolink-model.yaml
	gen-markdown --dir docs $< > $@
contrib/%/docs/index.md: contrib/%.yaml
	gen-markdown --dir contrib/$*/docs $< > $@
clean-docs:
	rm docs/*.md
	rm contrib/%/docs/*.md

# ~~~~~~~~~~~~~~~~~~~~
# Ontology
# ~~~~~~~~~~~~~~~~~~~~
ontology/biolink.ttl: biolink-model.yaml
	gen-rdf -o $@ $<

contrib/%/ontology.ttl: contrib/%.yaml
	gen-rdf -o $@ $<


# ~~~~~~~~~~~~~~~~~~~~
# Solr
# ~~~~~~~~~~~~~~~~~~~~
gen-golr-views:
	gen-golr-views -d golr-views biolink-model.yaml

contrib/%-golr:
	gen-golr-views -d contrib/$*/golr-views contrib/$*.yaml

# ~~~~~~~~~~~~~~~~~~~~
# Python
# ~~~~~~~~~~~~~~~~~~~~
metamodel/metamodel.py: meta.yaml
    gen-py-classes $< > $@

biolinkmodel/datamodel.py: biolink-model.yaml
	gen-py-classes $< > $@

contrib/%/datamodel.py: contrib/%.yaml
	./bin/gen-py-classes.py $< > $@

biolinkmodel/schema.py: biolink-model.yaml
	./bin/gen-mm-schema.py $< > $@

contrib/%/schema.py: contrib/%.yaml
	./bin/gen-mm-schema.py $< > $@


# trigger manually to avoid git churn
gv: biolink-model.yaml 
	./bin/gen-graphviz.py -d graphviz $<

graphviz/%.png: biolink-model.yaml 
	./bin/gen-graphviz.py  -c $* $< -o graphviz/$*


# ~~~~~~~~~~~~~~~~~~~~
# ShEx
# ~~~~~~~~~~~~~~~~~~~~

shex/biolink-model.shex: biolink-model.yaml 
	./bin/gen-shex.py $< > $@

# ~~~~~~~~~~~~~~~~~~~~
# Graphql
# ~~~~~~~~~~~~~~~~~~~~

graphql/biolink-model.graphql: biolink-model.yaml 
	gen-graphql.py $< > $@

proto/biolink-model.proto: biolink-model.yaml 
	./bin/gen-proto.py $< > $@

contrib/%/%.graphql: contrib/%.yaml 
	./bin/gen-graphql.py $< > $@

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
