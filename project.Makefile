## Add your own custom Makefile targets here

gen-viz-data:
	$(RUN) python src/testviz/scripts/generate_json.py
