import yaml


def test_ordo_prefix():
    with open("biolink-model.yaml") as schema_file:
        schema = yaml.safe_load(schema_file)

    assert schema["prefixes"]["ORDO"] == "http://www.orpha.net/ORDO/"
    assert "orphanet" not in schema["prefixes"]
