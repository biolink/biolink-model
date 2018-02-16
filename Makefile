# ----------------------------------------
# TOP LEVEL TARGETS
# ----------------------------------------
all: build test 
test: metatest pytests
build: build_core contrib_build_monarch

build_core: docs/index.md biolinkmodel/datamodel.py biolinkmodel/schema.py gen-golr-views ontology/biolink.ttl json-schema/biolink-model.json java graphql/biolink-model.graphql

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
	./bin/gen-csv.py -r 'biological entity' biolink-model.yaml > $@.tmp && mv $@.tmp $@
biolink-model.tsv: biolink-model.yaml
	./bin/gen-csv.py -f tsv biolink-model.yaml > $@.tmp && mv $@.tmp $@

# ~~~~~~~~~~~~~~~~~~~~
# JSONSCHEMA -> Java
# ~~~~~~~~~~~~~~~~~~~~
json-schema/%.json: %.yaml
	bin/gen-json-schema.py $< > $@.tmp && mv $@.tmp $@

contrib/%/schema.json: contrib/%.yaml
	bin/gen-json-schema.py $< > $@.tmp && mv $@.tmp $@

JSONSCHEMA2POJO = $(HOME)/src/jsonschema2pojo/bin/jsonschema2pojo
java: json-schema/biolink-model.json
	$(JSONSCHEMA2POJO) --source $< -T JSONSCHEMA -t java-gen

contrib/%-java: contrib/%/schema.json
	$(JSONSCHEMA2POJO) --source $< -T JSONSCHEMA -t contrib/$*/java

# ~~~~~~~~~~~~~~~~~~~~
# DOCS
# ~~~~~~~~~~~~~~~~~~~~
docs/index.md: biolink-model.yaml
	./bin/gen-markdown.py --dir docs $< > $@
contrib/%/docs/index.md: contrib/%.yaml
	./bin/gen-markdown.py --dir contrib/$*/docs $< > $@

# ~~~~~~~~~~~~~~~~~~~~
# Ontology
# ~~~~~~~~~~~~~~~~~~~~
ontology/biolink.ttl: biolink-model.yaml
	./bin/gen-rdf.py -o $@ $< 

contrib/%/ontology.ttl: contrib/%.yaml
	./bin/gen-rdf.py -o $@ $<


# ~~~~~~~~~~~~~~~~~~~~
# Solr
# ~~~~~~~~~~~~~~~~~~~~
gen-golr-views:
	./bin/gen-golr-views.py -d golr-views biolink-model.yaml
contrib/%-golr:
	./bin/gen-golr-views.py -d contrib/$*/golr-views contrib/$*.yaml

# ~~~~~~~~~~~~~~~~~~~~
# Python
# ~~~~~~~~~~~~~~~~~~~~

biolinkmodel/datamodel.py: biolink-model.yaml
	./bin/gen-py-classes.py $< > $@

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

graphql/biolink-model.graphql: biolink-model.yaml 
	./bin/gen-graphql.py $< > $@

contrib/%/%.graphql: contrib/%.yaml 
	./bin/gen-graphql.py $< > $@

#biolinkmodel/schema.py: biolink-model.yaml
#	./bin/gen-mm-schema.py $< > $@


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
	pytest -s tests/*py

metatest: test-gen-meta test-gen-biolink-model

test-gen-%: test-pygen-% test-mmgen-%
	echo done

test-pygen-%: %.yaml
	./bin/gen-py-classes.py $< > $@ && python $@
test-mmgen-%: %.yaml
	./bin/gen-mm-schema.py $<

# ----------------------------------------
# METAMODEL
# ----------------------------------------

metamodel/jsonschema/metamodel.json: meta.yaml
	bin/gen-json-schema.py $< > $@

MM = metamodel/metamodel.py
MMS = metamodel/metaschema.py
regen-mm:
	./bin/gen-py-classes.py meta.yaml  > $(MM)-tmp.py && python $(MM)-tmp.py && cp $(MM) $(MM)-PREV && mv $(MM)-tmp.py $(MM)

#TODO: edit by hand for now
#regen-mms:
#	./bin/gen-mm-schema.py meta.yaml  > $(MMS)-tmp.py && python $(MMS)-tmp.py && cp $(MMS) $(MMS)-PREV && mv $(MMS)-tmp.py $(MMS)

# ----------------------------------------
# UTILS
# ----------------------------------------

dir-%:
	mkdir -p $@
