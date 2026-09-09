import os
import json
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen

import pytest
import yaml


def test_ontology_class_description_uses_biolink_prefix():
    schema_path = os.path.join(os.path.dirname(__file__), "..", "biolink-model.yaml")
    with open(schema_path) as schema_file:
        schema = yaml.safe_load(schema_file)

    description = schema["classes"]["ontology class"]["description"]
    assert "use biolink:BiologicalProcess as the type." in description
    assert "use bl:BiologicalProcess as the type." not in description


def _is_obsolete_in_ols(curie: str):
    query = urlencode(
        {"q": curie, "queryFields": "obo_id", "exact": "true", "rows": "1"}
    )
    url = f"https://www.ebi.ac.uk/ols4/api/search?{query}"
    try:
        with urlopen(url, timeout=10) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except (HTTPError, URLError):
        return None

    docs = payload.get("response", {}).get("docs", [])
    if not docs:
        return None

    is_obsolete = docs[0].get("is_obsolete")
    if isinstance(is_obsolete, list):
        is_obsolete = is_obsolete[0] if is_obsolete else False
    if isinstance(is_obsolete, str):
        return is_obsolete.lower() == "true"
    return bool(is_obsolete)


def test_processed_material_mappings_are_not_obsolete_in_ols():
    schema_path = os.path.join(os.path.dirname(__file__), "..", "biolink-model.yaml")
    with open(schema_path) as schema_file:
        schema = yaml.safe_load(schema_file)

    processed_material = schema["classes"]["processed material"]
    mapping_terms = []
    for key, value in processed_material.items():
        if key.endswith("_mappings"):
            mapping_terms.extend(value if isinstance(value, list) else [value])

    checked = 0
    obsolete_terms = []
    for term in mapping_terms:
        if ":" not in term:
            continue
        obsolescence = _is_obsolete_in_ols(term)
        if obsolescence is None:
            continue
        checked += 1
        if obsolescence:
            obsolete_terms.append(term)

    if checked == 0:
        pytest.skip("No processed material mapping terms were resolvable in OLS API.")
    assert not obsolete_terms, f"Obsolete mapping terms found: {sorted(obsolete_terms)}"
