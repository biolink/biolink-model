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
