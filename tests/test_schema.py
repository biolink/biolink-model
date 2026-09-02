import yaml


def test_ontology_class_description_uses_biolink_prefix():
    with open("biolink-model.yaml") as schema_file:
        schema = yaml.safe_load(schema_file)

    description = schema["classes"]["ontology class"]["description"]
    assert "use biolink:BiologicalProcess as the type." in description
    assert "use bl:BiologicalProcess as the type." not in description
