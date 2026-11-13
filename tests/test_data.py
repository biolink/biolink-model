"""Validate the example data files under src/data/examples.

Files follow the convention ``ClassName-{SOMENAME}.yaml``, where ``ClassName`` is
the CamelCase form of the schema class the document is an instance of. Files in
``valid/`` must validate cleanly; files in ``invalid/`` must produce at least one
validation error.

Validation goes through ``linkml.validator``, which evaluates class ``rules:``
and so covers constraints such as the ``association`` rule requiring a numeric
p-value whenever 'statistical significance qualifier' is asserted.

When writing a fixture, omit ``category`` unless the target class relaxes it to
``required: false`` in ``slot_usage``. As of linkml 1.11.1 gen-json-schema emits
the type designator's ``enum`` at the array level rather than inside ``items``,
producing a constraint no array value can satisfy.
"""
import glob
import os

import pytest
import yaml
from linkml_runtime import SchemaView
from linkml_runtime.utils.formatutils import camelcase

from linkml.validator import validate

ROOT = os.path.join(os.path.dirname(__file__), "..")
DATA_DIR = os.path.join(ROOT, "src", "data", "examples")
SCHEMA = os.path.join(ROOT, "biolink-model.yaml")

# Map CamelCase class name -> the schema's own class name (lowercase with spaces).
# Built once at import; SchemaView over biolink-model.yaml is expensive.
_CLASS_BY_CAMEL = {camelcase(c): c for c in SchemaView(SCHEMA).all_classes()}


def _load(path):
    with open(path) as fh:
        return yaml.safe_load(fh)


def _target_class(path):
    """Resolve the schema class from the ``ClassName-{SOMENAME}.yaml`` filename."""
    prefix = os.path.basename(path).split("-")[0]
    if prefix not in _CLASS_BY_CAMEL:
        raise AssertionError(
            f"{os.path.basename(path)}: filename prefix {prefix!r} does not name a "
            f"class in the schema. Examples must be named ClassName-{{SOMENAME}}.yaml."
        )
    return _CLASS_BY_CAMEL[prefix]


def _examples(subdir):
    paths = sorted(glob.glob(os.path.join(DATA_DIR, subdir, "*.yaml")))
    return [pytest.param(p, id=os.path.basename(p)) for p in paths]


@pytest.mark.parametrize("path", _examples("valid"))
def test_valid_example(path):
    """Every file in valid/ must validate without errors."""
    report = validate(_load(path), SCHEMA, _target_class(path))
    assert not report.results, "\n".join(r.message for r in report.results)


@pytest.mark.parametrize("path", _examples("invalid"))
def test_invalid_example(path):
    """Every file in invalid/ must be rejected, otherwise it is not a negative test."""
    report = validate(_load(path), SCHEMA, _target_class(path))
    assert report.results, (
        f"{os.path.basename(path)} is in invalid/ but validated cleanly -- the "
        f"constraint it is meant to exercise is not being enforced."
    )


def test_examples_present():
    """Both fixture directories must be non-empty, so the globs cannot pass vacuously."""
    assert _examples("valid"), "no fixtures found in src/data/examples/valid"
    assert _examples("invalid"), "no fixtures found in src/data/examples/invalid"
