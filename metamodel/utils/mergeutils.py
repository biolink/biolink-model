from copy import deepcopy
from typing import Dict, Optional

import dataclasses

from metamodel.metamodel import SchemaDefinition, Element, SlotDefinition, SchemaDefinitionName


def merge_schemas(target: SchemaDefinition, mergee: SchemaDefinition) -> None:
    assert target.name is not None, "Schema name must be supplied"
    if target.id is None:
        target.id = mergee.id
    if target.license is None:
        target.license = mergee.license

    target.imports += [imp for imp in mergee.imports if imp not in target.imports]
    merge_dicts(target.classes, mergee.classes, mergee.name)
    merge_dicts(target.slots, mergee.slots)
    merge_dicts(target.types, mergee.types)


def merge_dicts(target: Dict[str, Element],
                source: Dict[str, Element],
                from_schema: Optional[SchemaDefinitionName]=None) -> None:
    for k, v in source.items():
        if k in target:
            raise ValueError("Conflicting definitions for {k} in schema {s1name} and {s2name}")
        target[k] = deepcopy(v)
    if from_schema:
        target.from_schema = from_schema


def merge_slots(target: SlotDefinition, source: SlotDefinition) -> None:
    for k, v in dataclasses.asdict(source).items():
        if k not in ('name', 'domain') and not getattr(target, k, None):
            setattr(target, k, deepcopy(v))