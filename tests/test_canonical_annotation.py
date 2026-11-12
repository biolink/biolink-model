from pathlib import Path
import yaml
import pytest
from linkml_runtime.utils.schemaview import SchemaView


@pytest.fixture
def load_biolink_model() -> Path:
    """Load the Biolink Model YAML file from the project root."""
    # Define the relative path to biolink-model.yaml from either the root or tests subdirectory
    file_path = Path(__file__).parent.parent / "biolink-model.yaml"

    if not file_path.is_file():
        raise FileNotFoundError("biolink-model.yaml not found in the project root directory")

    return file_path


def test_predicates_have_canonical_or_inverse(load_biolink_model):
    """Ensure each predicate has either 'canonical_predicate: true' or 'inverse' annotation."""
    model = SchemaView(load_biolink_model)

    for slot in model.all_slots():
        slot_details = model.get_slot(slot)
        if "related to" in model.slot_ancestors(slot):
            if "annotations" in slot_details:
                slot_annotations = slot_details.annotations
                if slot_annotations and slot_annotations.get("canonical_predicate") is not None:
                    if slot_details.inverse:
                        raise AssertionError(f"Slot '{slot_details}' has both 'canonical_predicate: true' "
                                            f"and 'inverse' annotations")
            elif not slot_details.inverse:
                raise AssertionError(f"Slot '{slot_details}' has neither 'canonical_predicate: true' "
                                    f"nor 'inverse' annotations")


def test_protein_accepts_ncit_prefix(load_biolink_model):
    """Ensure NCIT is a valid identifier prefix for Protein."""
    model = SchemaView(load_biolink_model)
    protein = model.get_class("protein")
    assert protein is not None
    assert "NCIT" in protein.id_prefixes

def test_active_in_is_a_located_in(load_biolink_model):
    """Ensure active in is modeled as a specialization of located in."""
    model = SchemaView(load_biolink_model)

    assert model.get_slot("active in").is_a == "located in"
    assert model.get_slot("has active component").is_a == "location of"

def test_macromolecular_complex_accepts_iuphar_target_prefix(load_biolink_model):
    """Ensure GtoPdb target identifiers are valid for macromolecular complexes."""
    model = SchemaView(load_biolink_model)
    complex_class = model.get_class("macromolecular complex")

    assert complex_class is not None
    assert "IUPHARobj" in complex_class.id_prefixes
    assert (
        model.schema.prefixes["IUPHARobj"].prefix_reference
        == "https://www.guidetopharmacology.org/GRAC/ObjectDisplayForward?objectId="
    )

def test_chemical_classes_accept_comptox_after_chemical_prefixes(load_biolink_model):
    """Ensure EPA DSSTox substance IDs (COMPTOX:DTXSID...) are valid for every chemical class, ranked below the
    curated and structure-based chemical vocabularies so they are never preferred over them."""
    model = SchemaView(load_biolink_model)
    outranking = ["CHEBI", "UNII", "PUBCHEM.COMPOUND", "CHEMBL.COMPOUND", "DRUGBANK", "INCHIKEY"]

    checked = []
    for class_name in model.class_descendants("chemical entity"):
        id_prefixes = model.get_class(class_name).id_prefixes
        if not id_prefixes:
            continue
        checked.append(class_name)
        assert "COMPTOX" in id_prefixes, class_name
        comptox_rank = id_prefixes.index("COMPTOX")
        for prefix in outranking:
            if prefix in id_prefixes:
                assert id_prefixes.index(prefix) < comptox_rank, (class_name, prefix)

    assert "chemical entity" in checked
    assert "drug" in checked
