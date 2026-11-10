import json

import yaml


def test_ordo_prefix():
    with open("biolink-model.yaml") as schema_file:
        schema = yaml.safe_load(schema_file)

    assert schema["prefixes"]["ORDO"] == "http://www.orpha.net/ORDO/"
    assert "orphanet" not in schema["prefixes"]


def test_cob_prefix_mapping():
    expected = "http://purl.obolibrary.org/obo/COB_"
    with open("biolink-model.yaml") as schema_file:
        schema = yaml.safe_load(schema_file)
    with open("src/biolink_model/prefixmaps/biolink-model-prefix-map.json") as prefix_map_file:
        prefix_map = json.load(prefix_map_file)
    with open("project/jsonld/biolink_model.context.jsonld") as context_file:
        context = json.load(context_file)

    assert schema["prefixes"]["COB"] == expected
    assert prefix_map["COB"] == expected
    assert context["@context"]["COB"] == expected
