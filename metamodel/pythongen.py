#
# @dataclass
# class SchemaDefinition(Definition):
#     """
#     A collection of definitions
#     """
#     id: str = None
#     slots: Dict[str, Union[dict, SlotDefinition]] = empty_dict()
#     classes: Dict[str, Union[dict, ClassDefinition]] = empty_dict()
#     types: Dict[str, Union[dict, TypeDefinition]] = empty_dict()
#     imports: List[str] = empty_list()
#     license: Optional[str] = None
#     prefixes: Dict[str, URI] = empty_dict()
#
#     def __post_init__(self) -> None:
#         if self.id is None:
#             raise ValueError("id must be supplied")
#         for k, v in self.slots.items():
#             if not isinstance(v, SlotDefinition):
#                 self.slots[k] = SlotDefinition(**v) if v else SlotDefinition()
#         for k, v in self.classes.items():
#             self.classes[k] = ClassDefinition(**v) if v else ClassDefinition()
#         for k, v in self.types.items():
#             self.types[k] = TypeDefinition(**v) if v else TypeDefinition()
import datetime
import os
import re
from typing import Dict, Optional, Tuple

from metamodel.dc_metamodel import SchemaDefinition, SlotDefinition, ClassDefinition
from metamodel.utils.formatutils import camelcase, underscore, be

__version__ = "0.0.1"

builtins: Dict[str, str] = {
    'string': 'str',
    'integer': 'int',
    'float': 'float',
    'double': 'float',
    'boolean': 'bool',
    'time': 'str'}


def builtin_name(typ: Optional[str]) -> Optional[str]:
    return builtins.get(typ, None)


def class_name(name: str) -> str:
    return camelcase(name)


def slot_name(name: str) -> str:
    return underscore(name)


def type_name(name: str) -> str:
    return camelcase(name)


def python_name_for(name: str, schema: SchemaDefinition) -> str:
    return class_name(name) if name in schema.classes else \
           slot_name(name) if name in schema.slots else \
           type_name(name) if name in schema.types else \
           builtin_name(name) if name in builtins else name


class Generator:
    generatorname = os.path.basename(__file__)
    generatorversion = __version__

    def __init__(self, sourcefile: str, schemaname: str, schema: SchemaDefinition) -> None:
        self.sourcefile = sourcefile
        self.schemaname = schemaname
        self.schema = schema
        # TODO: this goes into the schema
        self.schema.version = "0.0.1x"
        self.gendate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    def __str__(self) -> str:
        return re.sub(r' +$', '', self.gen_schema().replace('\t', '    '))

    def gen_schema(self) -> str:
        return f'''# Auto generated from {self.sourcefile} by {self.generatorname} version: {self.generatorversion}
# Generation date: {self.gendate}
# Schema: {self.schemaname}
#
# id: {self.schema.id}
# description: {be(self.schema.description)}
# license: {be(self.schema.license)}

from typing import Optional, List, Union, Dict
from dataclasses import dataclass
from metamodel.metamodelcore import Root, empty_list, empty_dict

{self.gen_classdefs()}'''

    def gen_classdefs(self) -> str:
        return '\n'.join([self.gen_classdef(k, v) for k, v in self.schema.classes.items()])

    def gen_classdef(self, clsname: str,  cls: ClassDefinition) -> str:
        parentref = f'({camelcase(cls.is_a if cls.is_a else "Root")})'
        slotdefs = self.gen_slots(cls)
        postinits = self.gen_postinits(cls)
        if not slotdefs:
            slotdefs = 'pass'
        return f'''
@dataclass
class {camelcase(clsname)}{parentref}:
    """
    {be(cls.description)}
    """
    {slotdefs}
    {postinits}'''

    def gen_slots(self, cls: ClassDefinition) -> str:
        return '\n\t'.join([self.gen_slot(cls, slot) for slot in cls.slots])

    def gen_slot(self, cls: ClassDefinition, slotname: str) -> str:
        slot = self.schema.slots[slotname]
        if slot.alias:
            slotname = slot.alias
        range_type = builtin_name(slot.range)
        if not range_type:
            range_type = 'str' if not slot.inlined else python_name_for(slot.range, self.schema)
        slot_range, default_val = self.range_cardinality(range_type, slot, cls)
        default = f'= {default_val}' if default_val else ''
        return f'''{underscore(slotname)}: {slot_range} {default}'''

    def gen_postinits(self, cls: ClassDefinition) -> str:
        post_inits = []
        for slot in cls.slots:
            post_init = self.gen_postinit(cls, slot)
            if post_init:
                post_inits.append(post_init)
        post_inits_str = '\n\t\t'.join(post_inits)
        return f'''
    def __post_init__(self) -> None:
        {post_inits_str}
''' if post_inits else ""

    def gen_postinit(self, cls: ClassDefinition, slotname: str) -> Optional[str]:
        slot = self.schema.slots[slotname]
        if slot.alias:
            slotname = slot.alias
        range_type = builtin_name(slot.range)
        if not range_type:
            range_type = 'str' if not slot.inlined else python_name_for(slot.range, self.schema)
        if (slot.primary_key or slot.required) and cls.is_a:
            return f'''if self.{slotname} is None:
            raise ValueError(f"{slotname} must be supplied")'''
        elif slot.multivalued and slot.inlined:
            return f'''for k, v in self.{slotname}.items():
            if not isinstance(v, {range_type}):
                self.{slotname}[k] = {range_type}(name=k, **v) if v is not None else {range_type}(name=k)'''
        return ""

    @staticmethod
    def range_cardinality(range_type: str, slot: SlotDefinition, cls: ClassDefinition) -> Tuple[str, Optional[str]]:
        if slot.multivalued:
            return (f'List[{range_type}]', 'empty_list()') if not slot.inlined \
                else (f'Dict[str, Union[dict, {range_type}]]', 'empty_dict()')
        elif slot.primary_key or slot.required:
            return range_type, 'None' if cls.is_a else None
        elif range_type == 'bool':
            return 'bool', 'False'
        else:
            return f'Optional[{range_type}]', 'None'
