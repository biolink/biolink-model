import os

import yaml


def test_ontology_class_description_uses_biolink_prefix():
    schema_path = os.path.join(os.path.dirname(__file__), "..", "biolink-model.yaml")
    with open(schema_path) as schema_file:
        schema = yaml.safe_load(schema_file)

    description = schema["classes"]["ontology class"]["description"]
    assert "use biolink:BiologicalProcess as the type." in description
    assert "use bl:BiologicalProcess as the type." not in description


def test_processed_material_uses_non_obsolete_exact_mapping():
    schema_path = os.path.join(os.path.dirname(__file__), "..", "biolink-model.yaml")
    with open(schema_path) as schema_file:
        schema = yaml.safe_load(schema_file)

    exact_mappings = schema["classes"]["processed material"]["exact_mappings"]
    assert "COB:0000026" in exact_mappings
    assert "OBI:0000047" not in exact_mappings
