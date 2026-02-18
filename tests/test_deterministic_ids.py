import pytest
from biolink_model.datamodel.pydanticmodel_v2 import (
    Association, GeneToDiseaseAssociation,
    AssociationIdConfig, IdStrategy,
)


@pytest.fixture(autouse=True)
def reset_strategy():
    """Reset to default strategy after each test."""
    yield
    AssociationIdConfig.strategy = IdStrategy.SPO_Q_KLAT_PKS
    AssociationIdConfig.custom_fields = []


# -- Core behavior (works with any strategy) ----------------------------------

def test_auto_generated_id():
    assoc = Association(
        subject="HGNC:1234",
        predicate="biolink:related_to",
        object="HP:0001234",
        knowledge_level="not_provided",
        agent_type="not_provided",
    )
    assert assoc.id.startswith("uuid:")


def test_deterministic_same_inputs():
    kwargs = dict(
        subject="HGNC:1234",
        predicate="biolink:related_to",
        object="HP:0001234",
        knowledge_level="not_provided",
        agent_type="not_provided",
    )
    assert Association(**kwargs).id == Association(**kwargs).id


def test_different_inputs_different_id():
    assoc1 = Association(
        subject="HGNC:1234", predicate="biolink:related_to", object="HP:0001234",
        knowledge_level="not_provided", agent_type="not_provided",
    )
    assoc2 = Association(
        subject="HGNC:9999", predicate="biolink:related_to", object="HP:0001234",
        knowledge_level="not_provided", agent_type="not_provided",
    )
    assert assoc1.id != assoc2.id


def test_explicit_id_preserved():
    assoc = Association(
        id="my:custom-id",
        subject="HGNC:1234", predicate="biolink:related_to", object="HP:0001234",
        knowledge_level="not_provided", agent_type="not_provided",
    )
    assert assoc.id == "my:custom-id"


def test_subclass_inherits_id_generation():
    g2d = GeneToDiseaseAssociation(
        subject="HGNC:1234", predicate="biolink:contributes_to", object="MONDO:0005148",
        knowledge_level="knowledge_assertion", agent_type="manual_agent",
    )
    assert g2d.id.startswith("uuid:")


def test_different_subclass_different_id():
    """Same core data in Association vs a subclass produces different IDs
    because the class name is included in the hash."""
    base_kwargs = dict(
        subject="HGNC:1234", predicate="biolink:contributes_to", object="MONDO:0005148",
        knowledge_level="not_provided", agent_type="not_provided",
    )
    assoc_id = Association(**base_kwargs).id
    g2d_id = GeneToDiseaseAssociation(**base_kwargs).id
    assert assoc_id != g2d_id


# -- Strategy-specific behavior ------------------------------------------------

def test_standard_strategy_includes_publications():
    """With SPO_Q_KLAT_PKS, different publications -> different ID."""
    AssociationIdConfig.strategy = IdStrategy.SPO_Q_KLAT_PKS
    base = dict(
        subject="HGNC:1234", predicate="biolink:related_to", object="HP:0001234",
        knowledge_level="not_provided", agent_type="not_provided",
    )
    a1 = Association(**base, publications=["PMID:12345"])
    a2 = Association(**base, publications=["PMID:99999"])
    assert a1.id != a2.id


def test_standard_strategy_ignores_evidence():
    """With SPO_Q_KLAT_PKS, different evidence -> same ID."""
    AssociationIdConfig.strategy = IdStrategy.SPO_Q_KLAT_PKS
    base = dict(
        subject="HGNC:1234", predicate="biolink:related_to", object="HP:0001234",
        knowledge_level="not_provided", agent_type="not_provided",
        publications=["PMID:12345"],
    )
    a1 = Association(**base, has_evidence=["ECO:0000304"])
    a2 = Association(**base, has_evidence=["ECO:0000501"])
    assert a1.id == a2.id


def test_all_fields_strategy():
    """With ALL_FIELDS, any field change -> different ID."""
    AssociationIdConfig.strategy = IdStrategy.ALL_FIELDS
    base = dict(
        subject="HGNC:1234", predicate="biolink:related_to", object="HP:0001234",
        knowledge_level="not_provided", agent_type="not_provided",
    )
    a1 = Association(**base, has_evidence=["ECO:0000304"])
    a2 = Association(**base, has_evidence=["ECO:0000501"])
    assert a1.id != a2.id


def test_qualifier_based_strategy_excludes_publications():
    """With QUALIFIER_BASED, different publications -> same ID."""
    AssociationIdConfig.strategy = IdStrategy.QUALIFIER_BASED
    base = dict(
        subject="HGNC:1234", predicate="biolink:related_to", object="HP:0001234",
        knowledge_level="not_provided", agent_type="not_provided",
    )
    a1 = Association(**base, publications=["PMID:12345"])
    a2 = Association(**base, publications=["PMID:99999"])
    assert a1.id == a2.id


def test_custom_strategy():
    """With CUSTOM, only specified fields matter."""
    AssociationIdConfig.strategy = IdStrategy.CUSTOM
    AssociationIdConfig.custom_fields = ["subject", "predicate", "object"]
    a1 = Association(
        subject="HGNC:1234", predicate="biolink:related_to", object="HP:0001234",
        knowledge_level="not_provided", agent_type="not_provided",
        primary_knowledge_source="infores:monarchinitiative",
    )
    a2 = Association(
        subject="HGNC:1234", predicate="biolink:related_to", object="HP:0001234",
        knowledge_level="knowledge_assertion", agent_type="manual_agent",  # different
        primary_knowledge_source="infores:other",  # different
    )
    assert a1.id == a2.id  # only SPO matters


def test_switching_strategy_changes_id():
    """Same data produces different IDs under different strategies."""
    kwargs = dict(
        subject="HGNC:1234", predicate="biolink:related_to", object="HP:0001234",
        knowledge_level="not_provided", agent_type="not_provided",
    )
    AssociationIdConfig.strategy = IdStrategy.SPO_Q_KLAT_PKS
    id_standard = Association(**kwargs).id

    AssociationIdConfig.strategy = IdStrategy.ALL_FIELDS
    id_all = Association(**kwargs).id

    # Different strategies -> (very likely) different IDs
    # because ALL_FIELDS includes more fields in the hash
    assert id_standard != id_all
