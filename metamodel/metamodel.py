# Auto generated from meta.yaml by pythongen.py version: 0.0.4
# Generation date: 2018-11-12 18:12
# Schema: metamodel
#
# id: https://biolink.github.io/metamodel/ontology/meta.ttl
# description: Metamodel for biolink schema
# license: https://creativecommons.org/publicdomain/zero/1.0/

import datetime
from typing import Optional, List, Union, Dict, Any
from dataclasses import dataclass
from metamodel.utils.metamodelcore import empty_list, empty_dict
from metamodel.utils.yamlutils import YAMLRoot

metamodel_version = "0.3.2"

inherited_slots: List[str] = ["description", "alt_description_text", "source", "alt_descriptions", "in_subset",
                              "exact_matches", "broader_matches", "narrower_matches", "multivalued", "domain", "range",
                              "required", "inlined", "definitional", "object_property", "subproperty_of", "inherited"]


# Type names


# Class references
class PrefixLocalName(str):
    pass


class ElementName(str):
    pass


class DefinitionName(ElementName):
    pass


class SlotDefinitionName(DefinitionName):
    pass


class ClassDefinitionName(DefinitionName):
    pass


class TypeDefinitionName(ElementName):
    pass


class SchemaDefinitionName(DefinitionName):
    pass


class SchemaDefinitionId(str):
    pass


@dataclass
class AltDescription(YAMLRoot):
    """
    Attributed description
    """
    description: Optional[str] = None
    source: Optional[str] = None


@dataclass
class Prefix(YAMLRoot):
    """
    Prefix URI map
    """
    local_name: PrefixLocalName
    prefix_uri: Optional[str] = None


@dataclass
class Example(YAMLRoot):
    """
    example of usage
    """
    value: Optional[str] = None
    description: Optional[str] = None


@dataclass
class Element(YAMLRoot):
    """
    root of all described things
    """
    name: ElementName
    singular_name: Optional[str] = None
    description: Optional[str] = None
    note: Optional[str] = None
    comment: Optional[str] = None
    examples: List[Union[dict, Example]] = empty_list()
    see_also: Optional[str] = None
    flags: List[str] = empty_list()
    aliases: List[str] = empty_list()
    mappings: List[str] = empty_list()
    id_prefixes: List[str] = empty_list()
    in_subset: List[str] = empty_list()
    from_schema: Optional[str] = None
    alt_descriptions: List[AltDescription] = empty_list()
    exact_matches: List[str] = empty_list()
    broader_matches: List[str] = empty_list()
    narrower_matches: List[str] = empty_list()
    close_matches: List[str] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        self.alt_descriptions = [v if isinstance(v, AltDescription)
                                 else AltDescription(v) for v in self.alt_descriptions]


@dataclass
class Definition(Element):
    """
    definition base class
    """
    name: DefinitionName = None
    is_a: Optional[DefinitionName] = None
    mixin: bool = False
    mixins: List[DefinitionName] = empty_list()
    abstract: bool = False
    local_names: List[str] = empty_list()
    union_of: List[DefinitionName] = empty_list()
    subclass_of: Optional[str] = None
    values_from: List[str] = empty_list()
    symmetric: bool = False

    def _fix_elements(self):
        super()._fix_elements()
        if self.is_a and not isinstance(self.is_a, DefinitionName):
            self.is_a = DefinitionName(self.is_a)
        self.mixins = [v if isinstance(v, DefinitionName)
                       else DefinitionName(v) for v in self.mixins]
        self.union_of = [v if isinstance(v, DefinitionName)
                         else DefinitionName(v) for v in self.union_of]


@dataclass
class SlotDefinition(Definition):
    """
    A property or slot
    """
    name: SlotDefinitionName = None
    multivalued: bool = False
    domain: Optional[ClassDefinitionName] = None
    range: Optional[Any] = None
    required: bool = False
    object_property: bool = False
    inlined: bool = False
    primary_key: bool = False
    identifier: bool = False
    definitional: bool = False
    alias: Optional[str] = None
    path: Optional[str] = None
    subproperty_of: Optional[SlotDefinitionName] = None
    inverse: Optional[SlotDefinitionName] = None
    is_class_field: bool = False
    role: Optional[str] = None
    inherited: bool = False
    is_a: Optional[SlotDefinitionName] = None
    mixins: List[SlotDefinitionName] = empty_list()
    union_of: List[SlotDefinitionName] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.name is None:
            raise ValueError(f"name must be supplied")
        if not isinstance(self.name, SlotDefinitionName):
            self.name = SlotDefinitionName(self.name)
        if self.domain and not isinstance(self.domain, ClassDefinitionName):
            self.domain = ClassDefinitionName(self.domain)
        if self.subproperty_of and not isinstance(self.subproperty_of, SlotDefinitionName):
            self.subproperty_of = SlotDefinitionName(self.subproperty_of)
        if self.inverse and not isinstance(self.inverse, SlotDefinitionName):
            self.inverse = SlotDefinitionName(self.inverse)
        if self.is_a and not isinstance(self.is_a, SlotDefinitionName):
            self.is_a = SlotDefinitionName(self.is_a)
        self.mixins = [v if isinstance(v, SlotDefinitionName)
                       else SlotDefinitionName(v) for v in self.mixins]
        self.union_of = [v if isinstance(v, SlotDefinitionName)
                         else SlotDefinitionName(v) for v in self.union_of]


@dataclass
class ClassDefinition(Definition):
    """
    A class or interface
    """
    name: ClassDefinitionName = None
    defining_slots: List[SlotDefinitionName] = empty_list()
    slots: List[SlotDefinitionName] = empty_list()
    slot_usage: Dict[SlotDefinitionName, Union[dict, SlotDefinition]] = empty_dict()
    apply_to: Optional[ClassDefinitionName] = None
    entity: bool = False
    is_a: Optional[ClassDefinitionName] = None
    mixins: List[ClassDefinitionName] = empty_list()
    union_of: List[ClassDefinitionName] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.name is None:
            raise ValueError(f"name must be supplied")
        if not isinstance(self.name, ClassDefinitionName):
            self.name = ClassDefinitionName(self.name)
        self.defining_slots = [v if isinstance(v, SlotDefinitionName)
                               else SlotDefinitionName(v) for v in self.defining_slots]
        self.slots = [v if isinstance(v, SlotDefinitionName)
                      else SlotDefinitionName(v) for v in self.slots]
        for k, v in self.slot_usage.items():
            if not isinstance(v, SlotDefinition):
                self.slot_usage[k] = SlotDefinition(name=k, **({} if v is None else v))
        if self.apply_to and not isinstance(self.apply_to, ClassDefinitionName):
            self.apply_to = ClassDefinitionName(self.apply_to)
        if self.is_a and not isinstance(self.is_a, ClassDefinitionName):
            self.is_a = ClassDefinitionName(self.is_a)
        self.mixins = [v if isinstance(v, ClassDefinitionName)
                       else ClassDefinitionName(v) for v in self.mixins]
        self.union_of = [v if isinstance(v, ClassDefinitionName)
                         else ClassDefinitionName(v) for v in self.union_of]


@dataclass
class TypeDefinition(Element):
    """
    A type definition
    """
    name: TypeDefinitionName = None
    typeof: Optional[str] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.name is None:
            raise ValueError(f"name must be supplied")
        if not isinstance(self.name, TypeDefinitionName):
            self.name = TypeDefinitionName(self.name)


@dataclass
class SchemaDefinition(Definition):
    """
    A collection of definitions
    """
    name: SchemaDefinitionName = None
    id: SchemaDefinitionId = None
    version: Optional[str] = None
    imports: List[str] = empty_list()
    license: Optional[str] = None
    prefixes: Dict[PrefixLocalName, Union[str, Prefix]] = empty_dict()
    default_prefix: Optional[str] = None
    default_type: Optional[TypeDefinitionName] = None
    default_curi_maps: List[str] = empty_list()
    types: Dict[TypeDefinitionName, Union[dict, TypeDefinition]] = empty_dict()
    slots: Dict[SlotDefinitionName, Union[dict, SlotDefinition]] = empty_dict()
    classes: Dict[ClassDefinitionName, Union[dict, ClassDefinition]] = empty_dict()
    metamodel_version: Optional[str] = None
    source_file: Optional[str] = None
    source_file_size: Optional[int] = None
    source_file_date: Optional[str] = None
    generation_date: Optional[datetime.date] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.name is None:
            raise ValueError(f"name must be supplied")
        if not isinstance(self.name, SchemaDefinitionName):
            self.name = SchemaDefinitionName(self.name)
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, SchemaDefinitionId):
            self.id = SchemaDefinitionId(self.id)
        for k, v in self.prefixes.items():
            if not isinstance(v, Prefix):
                self.prefixes[k] = Prefix(k, v)
        if self.default_type and not isinstance(self.default_type, TypeDefinitionName):
            self.default_type = TypeDefinitionName(self.default_type)
        for k, v in self.types.items():
            if not isinstance(v, TypeDefinition):
                self.types[k] = TypeDefinition(name=k, **({} if v is None else v))
        for k, v in self.slots.items():
            if not isinstance(v, SlotDefinition):
                self.slots[k] = SlotDefinition(name=k, **({} if v is None else v))
        for k, v in self.classes.items():
            if not isinstance(v, ClassDefinition):
                self.classes[k] = ClassDefinition(name=k, **({} if v is None else v))

