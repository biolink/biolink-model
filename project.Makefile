## Add your own custom Makefile targets here

gen-viz-data:
	$(RUN) python src/biolink_model/scripts/generate_json.py
