# Auto generated from /Users/solbrig/git/hsolbrig/biolink-model/meta.yaml by pythongen.py version: 0.0.1
# Generation date: 2018-05-25 17:24
# Schema: metamodel
#
# id: http://bioentity.io/json-schema/meta.json
# description: Metamodel for biolink schema
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict
from dataclasses import dataclass
from metamodel.metamodelcore import Root, empty_list, empty_dict


@dataclass
class Mapping(Root):
    """
    A mapping from a local to external string
    """
    localname: str
    mappedname: str


@dataclass
class PrefixMap(Root):
    """
    ID/CURIE prefix applicable to that element
    """
    nsname: str
    uri: str


@dataclass
class Example(Root):
    """
    example of usage
    """
    value: str
    description: Optional[str] = None


@dataclass
class Element(Root):
    """
    root of all classes
    """
    name: str
    singular_name: Optional[str] = None
    description: Optional[str] = None
    note: Optional[str] = None
    examples: Dict[str, Union[dict, Example]] = empty_dict()

    def __post_init__(self) -> None:
        for k, v in self.examples.items():
            if not isinstance(v, Example):
                self.examples[k] = Example(name=k, **v) if v is not None else Example(name=k)


@dataclass
class Definition(Element):
    """
    base class
    """
    is_a: Optional[str] = None
    abstract: bool = False
    prefixes: List[str] = empty_list()
    in_subset: List[str] = empty_list()
    apply_to: Optional[str] = None
    mappings: List[str] = empty_list()


@dataclass
class SlotDefinition(Definition):
    """
    A property or slot
    """
    mixin: bool = False
    mixins: List[str] = empty_list()
    identifier: bool = False
    domain: Optional[str] = None
    inlined: bool = False
    range: Optional[str] = None
    primary_key: bool = False
    multivalued: bool = False
    alias: Optional[str] = None
    required: bool = False
    path: Optional[str] = None
    subproperty_of: Optional[str] = None


@dataclass
class SlotUsageDefinition(SlotDefinition):
    """
    A usage of slot in the context of a class
    """
    pass


@dataclass
class ClassDefinition(Definition):
    """
    A class or interface
    """
    defining_slots: Dict[str, Union[dict, SlotDefinition]] = empty_dict()
    subclass_of: Optional[str] = None
    mixin: bool = False
    mixins: List[str] = empty_list()
    slots: List[str] = empty_list()
    slot_usage: List[str] = empty_list()

    def __post_init__(self) -> None:
        for k, v in self.defining_slots.items():
            if not isinstance(v, SlotDefinition):
                self.defining_slots[k] = SlotDefinition(name=k, **v) if v is not None else SlotDefinition(name=k)


@dataclass
class TypeDefinition(Definition):
    """
    A type definition
    """
    mixins: List[str] = empty_list()
    typeof: Optional[str] = None


@dataclass
class SchemaDefinition(Definition):
    """
    A collection of definitions
    """
    id: str = None
    imports: List[str] = empty_list()
    license: Optional[str] = None
    slots: Dict[str, Union[dict, SlotDefinition]] = empty_dict()
    types: Dict[str, Union[dict, TypeDefinition]] = empty_dict()
    classes: Dict[str, Union[dict, ClassDefinition]] = empty_dict()

    def __post_init__(self) -> None:
        if self.id is None:
            raise ValueError(f"id must be supplied")
        for k, v in self.slots.items():
            if not isinstance(v, SlotDefinition):
                self.slots[k] = SlotDefinition(name=k, **v) if v is not None else SlotDefinition(name=k)
        for k, v in self.types.items():
            if not isinstance(v, TypeDefinition):
                self.types[k] = TypeDefinition(name=k, **v) if v is not None else TypeDefinition(name=k)
        for k, v in self.classes.items():
            if not isinstance(v, ClassDefinition):
                self.classes[k] = ClassDefinition(name=k, **v) if v is not None else ClassDefinition(name=k)
