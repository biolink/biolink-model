# ----------------------------------------
# TOP LEVEL TARGETS
# ----------------------------------------
all: build test 
test: metatest pytests
build: biolinkmodel/datamodel.py biolinkmodel/schema.py gen-golr-views

# ----------------------------------------
# BUILD/COMPILATION
# ----------------------------------------

gen-golr-views:
	./bin/gen-golr-views.py -d golr-views biolink-model.yaml


biolinkmodel/datamodel.py: biolink-model.yaml
	./bin/gen-py-classes.py $< > $@

#biolinkmodel/schema.py: biolink-model.yaml
#	./bin/gen-mm-schema.py $< > $@

# ----------------------------------------
# TESTS
# ----------------------------------------

pytests:
	pytest -s tests/*py

metatest: test-gen-meta test-gen-biolink-model

test-gen-%: test-pygen-% test-mmgen-%
	echo done

test-pygen-%: %.yaml
	./bin/gen-py-classes.py $<
test-mmgen-%: %.yaml
	./bin/gen-mm-schema.py $<

# ----------------------------------------
# UTILS
# ----------------------------------------

dir-%:
	mkdir -p $@
