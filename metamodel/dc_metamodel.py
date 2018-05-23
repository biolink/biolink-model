from typing import Optional, List, Union, Dict, NewType

from dataclasses import dataclass, field

empty_list = field(default_factory=lambda: [])
empty_dict = field(default_factory=lambda: {})

URI = NewType('URI', str)


class Builtin:
    pass


string = Builtin()
double = Builtin()
time = Builtin()


@dataclass
class Definition(object):
    """
    base class
    """
    name: str
    singular_name: Optional[str] = None
    is_a: Optional["Definition"] = None
    description: Optional[str] = None
    note: Optional[str] = None
    abstract: bool = False
    mappings: List[str] = empty_list
    id_prefixes: List[str] = empty_list
    in_subset: List[str] = empty_list
    apply_to: Optional[str] = None


@dataclass
class SlotDefinition(Definition):
    """
    A property or slot
    """
    mixin: bool = False
    mixins: List["ClassDefinition"] = empty_list
    identifier: Optional[str] = None
    domain: Optional["ClassDefinition"] = None
    range: Optional[Union["ClassDefinition", "TypeDefinition"]] = None
    multivalued: bool = False
    required: bool = False
    path: Optional[str] = None
    subproperty_of: Optional[str] = None
    examples: List["Example"] = empty_list


@dataclass
class SlotUsageDefinition(SlotDefinition):
    """
    A usage of slot in the context of a class
    """
    ...


@dataclass
class ClassDefinition(Definition):
    """
    A class or interface
    """
    defining_slots: List[SlotDefinition] = empty_list
    mixin: bool = False
    mixins: List["ClassDefinition"] = empty_list
    slots: List[SlotDefinition] = empty_list
    slot_usage: List[SlotUsageDefinition] = empty_list


@dataclass
class TypeDefinition(Definition):
    """
    A type definition
    """
    mixins: List["ClassDefinition"] = empty_list
    typeof: Optional[Builtin] = None


@dataclass
class SchemaDefinition(Definition):
    """
    A collection of definitions
    """
    id: str
    slots: List[SlotDefinition] = empty_list
    classes: List[ClassDefinition] = empty_list
    types: List[ClassDefinition] = empty_list
    imports: List[str] = empty_list
    license: Optional[str] = None
    prefixes: Dict[str, URI] = empty_dict


@dataclass
class Example:
    """
    example of usage
    """
    value: str
    description: str
