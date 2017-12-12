# ----------------------------------------
# TOP LEVEL TARGETS
# ----------------------------------------
all: build test 
test: metatest pytests
build: biolinkmodel/datamodel.py biolinkmodel/schema.py gen-golr-views ontology/biolink.owl

# ----------------------------------------
# BUILD/COMPILATION
# ----------------------------------------

gen-golr-views:
	./bin/gen-golr-views.py -d golr-views biolink-model.yaml


biolinkmodel/datamodel.py: biolink-model.yaml
	./bin/gen-py-classes.py $< > $@

ontology/biolink.owl: biolink-model.yaml
	./bin/gen-rdf.py -o $@ $< 

ontology/%.json: ontology/%.owl
	owltools $< -o -f json $@

ontology/%.obo: ontology/%.owl
	owltools $< -o -f obo --no-check $@

ontology/%.tree: ontology/%.json
	ogr --showdefs -t tree -r $< % > $@

ontology/%.png: ontology/%.json
	ogr-tree -t png -o $@ -c subClassOf subPropertyOf -r $< % 


#biolinkmodel/schema.py: biolink-model.yaml
#	./bin/gen-mm-schema.py $< > $@

# ----------------------------------------
# JSONSCHEMA
# ----------------------------------------
jsonschema/biolink.json: biolink-model.yaml
	bin/gen-json-schema.py $< > $@

JSONSCHEMA2POJO = $(HOME)/src/jsonschema2pojo/bin/jsonschema2pojo
java: jsonschema/biolink.json
	$(JSONSCHEMA2POJO) --source jsonschema/ -T JSONSCHEMA -t java-gen

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
regen-mm:
	./bin/gen-py-classes.py meta.yaml  > $(MM)-tmp.py && python $(MM)-tmp.py && cp $(MM) $(MM)-PREV && mv $(MM)-tmp.py $(MM)

# ----------------------------------------
# UTILS
# ----------------------------------------

dir-%:
	mkdir -p $@
