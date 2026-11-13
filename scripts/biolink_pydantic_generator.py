"""
Custom PydanticGenerator for biolink-model that adds deterministic
hash-based Association IDs to generated Pydantic classes.

Supports runtime-configurable identity strategies:
  - SPO_Q_KLAT_PKS (default): SPO + qualifiers + KL + AT + primary_knowledge_source + publications
  - QUALIFIER_BASED: SPO + qualifiers + KL + AT + primary_knowledge_source (no pubs)
  - ALL_FIELDS: every field on the class except id
  - CUSTOM: user-specified field list
"""
import sys
from dataclasses import dataclass

from linkml.generators.pydanticgen.pydanticgen import PydanticGenerator
from linkml.generators.pydanticgen.template import Import, Imports, ObjectImport
from linkml_runtime.utils.formatutils import camelcase, underscore


# Fields shared by QUALIFIER_BASED and SPO_Q_KLAT_PKS strategies
CORE_IDENTITY_FIELDS = [
    "subject",
    "predicate",
    "object",
    "negated",
    "knowledge_level",
    "agent_type",
    "primary_knowledge_source",
]

# Additional fields for the SPO_Q_KLAT_PKS "standard" strategy
STANDARD_EXTRA_FIELDS = [
    "publications",
]


def _compute_qualifier_slots(generator: PydanticGenerator) -> dict[str, list[str]]:
    """
    For every class descending from 'association', discover qualifier slots
    via the slot is_a hierarchy and combine with CORE_IDENTITY_FIELDS.
    """
    sv = generator.schemaview
    identity_map: dict[str, list[str]] = {}

    for class_name in sv.class_descendants("association", reflexive=True):
        qualifier_slots = []
        for slot_name in sv.class_slots(class_name):
            ancestors = sv.slot_ancestors(slot_name, reflexive=True)
            if "qualifier" in ancestors:
                qualifier_slots.append(underscore(slot_name))

        all_identity = sorted(set(CORE_IDENTITY_FIELDS + qualifier_slots))
        identity_map[camelcase(class_name)] = all_identity

    return identity_map


def _compute_standard_slots(qualifier_map: dict[str, list[str]]) -> dict[str, list[str]]:
    """
    Extend the qualifier-based map with STANDARD_EXTRA_FIELDS (publications)
    to produce the SPO+Q+KL+AT+pubs strategy.
    """
    return {
        class_name: sorted(set(fields + STANDARD_EXTRA_FIELDS))
        for class_name, fields in qualifier_map.items()
    }


def _build_slots_dict_code(var_name: str, slots_map: dict[str, list[str]]) -> str:
    """Generate a Python dict literal for a named slot mapping."""
    lines = [f"{var_name}: dict[str, list[str]] = {{"]
    for class_name in sorted(slots_map.keys()):
        lines.append(f'    "{class_name}": {slots_map[class_name]!r},')
    lines.append("}")
    return "\n".join(lines)


# --- Injected runtime code (becomes part of pydanticmodel_v2.py) ---

ID_STRATEGY_CODE = '''
class IdStrategy(enum.Enum):
    """Strategy for selecting which fields define Association identity."""
    SPO_Q_KLAT_PKS = "spo_q_klat_pks"      # SPO + qualifiers + KL + AT + PKS + pubs (default)
    QUALIFIER_BASED = "qualifier_based"      # SPO + qualifiers + KL + AT + PKS (no pubs)
    ALL_FIELDS = "all_fields"               # Every field except id
    CUSTOM = "custom"                       # User-specified field list


class AssociationIdConfig:
    """
    Process-level configuration for deterministic Association ID generation.

    Set once at startup before constructing any Association instances:

        AssociationIdConfig.strategy = IdStrategy.ALL_FIELDS

    For CUSTOM strategy, also set custom_fields:

        AssociationIdConfig.strategy = IdStrategy.CUSTOM
        AssociationIdConfig.custom_fields = ["subject", "predicate", "object"]
    """
    strategy: IdStrategy = IdStrategy.SPO_Q_KLAT_PKS
    custom_fields: list[str] = []
'''

DETERMINISTIC_ID_MIXIN_CODE = '''
class DeterministicIdMixin(ConfiguredBaseModel):
    """
    Mixin that auto-generates a deterministic hash-based ID for Association
    instances when no explicit ID is provided.

    The fields included in the hash depend on AssociationIdConfig.strategy.
    """

    @model_validator(mode="before")
    @classmethod
    def _generate_deterministic_id(cls, data: Any) -> Any:
        if isinstance(data, dict):
            existing_id = data.get("id")
            if existing_id is None or existing_id is ...:
                class_name = cls.__name__
                strategy = AssociationIdConfig.strategy

                if strategy == IdStrategy.ALL_FIELDS:
                    identity_fields = sorted(
                        f for f in cls.model_fields if f != "id"
                    )
                elif strategy == IdStrategy.CUSTOM:
                    identity_fields = sorted(AssociationIdConfig.custom_fields)
                elif strategy == IdStrategy.QUALIFIER_BASED:
                    identity_fields = _QUALIFIER_IDENTITY_SLOTS.get(class_name, [])
                else:  # SPO_Q_KLAT_PKS (default)
                    identity_fields = _STANDARD_IDENTITY_SLOTS.get(class_name, [])

                parts = [class_name]
                for field_name in identity_fields:
                    value = data.get(field_name)
                    parts.append(field_name)
                    parts.append(
                        json.dumps(value, sort_keys=True, default=str)
                        if value is not None else "null"
                    )
                hash_input = "|".join(parts)
                hash_value = hashlib.sha256(
                    hash_input.encode("utf-8")
                ).hexdigest()
                data["id"] = f"uuid:{hash_value}"
        return data
'''


@dataclass
class BiolinkPydanticGenerator(PydanticGenerator):
    """PydanticGenerator with deterministic Association ID injection."""

    def __post_init__(self):
        super().__post_init__()

        # Compute both slot maps from schema's slot is_a hierarchy
        qualifier_map = _compute_qualifier_slots(self)
        standard_map = _compute_standard_slots(qualifier_map)

        qualifier_slots_code = _build_slots_dict_code(
            "_QUALIFIER_IDENTITY_SLOTS", qualifier_map
        )
        standard_slots_code = _build_slots_dict_code(
            "_STANDARD_IDENTITY_SLOTS", standard_map
        )

        # Inject enum, config, lookup dicts, and mixin class
        if self.injected_classes is None:
            self.injected_classes = []
        self.injected_classes.append(ID_STRATEGY_CODE)
        self.injected_classes.append(qualifier_slots_code)
        self.injected_classes.append(standard_slots_code)
        self.injected_classes.append(DETERMINISTIC_ID_MIXIN_CODE)

        # Add required imports
        extra_imports = (
            Imports()
            + Import(module="enum")
            + Import(module="hashlib")
            + Import(module="json")
            + Import(module="pydantic",
                     objects=[ObjectImport(name="model_validator")])
        )
        if self.imports is None:
            self.imports = extra_imports
        else:
            self.imports = self.imports + extra_imports

    def after_render_template(self, template: str, sv) -> str:
        """Splice DeterministicIdMixin into Association's bases."""
        template = template.replace(
            "class Association(Entity):",
            "class Association(DeterministicIdMixin, Entity):",
        )
        return template


if __name__ == "__main__":
    gen = BiolinkPydanticGenerator(
        sys.argv[1],
        metadata_mode=None,
    )
    print(gen.serialize(), end="")
