import datetime
import os
import re
from typing import Dict, Optional, Tuple, List

from metamodel.builtins import Builtin, builtin_names
from metamodel.metamodel import SchemaDefinition, SlotDefinition, ClassDefinition, ClassDefinitionName, \
    SlotDefinitionName
from metamodel.utils.formatutils import camelcase, underscore, be, wrapped_annotation

__version__ = "0.0.1"           # Generator version

python_builtins: Dict[Builtin, str] = {
    Builtin.string: 'str',
    Builtin.integer: 'int',
    Builtin.float: 'float',
    Builtin.double: 'float',
    Builtin.boolean: 'bool',
    Builtin.time: 'datetime.time',
    Builtin.date: 'datetime.date'}


def python_class_name(name: str) -> str:
    return camelcase(name)


def python_slot_name(name: str) -> str:
    return underscore(name)


def python_type_name(name: str) -> str:
    return camelcase(name)


def python_name_for(name: str, schema: SchemaDefinition) -> str:
    return 'str' if name is None else \
           python_class_name(name) if name in schema.classes else \
           python_slot_name(name) if name in schema.slots else \
           python_type_name(name) if name in schema.types else \
           python_builtins[builtin_names[name]] if name in builtin_names else name


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
        return re.sub(r' +\n', '\n', self.gen_schema().replace('\t', '    ')).strip(' ')

    def gen_schema(self) -> str:
        return f'''# Auto generated from {self.sourcefile} by {self.generatorname} version: {self.generatorversion}
# Generation date: {self.gendate}
# Schema: {self.schemaname}
#
# id: {self.schema.id}
# description: {be(self.schema.description)}
# license: {be(self.schema.license)}

import datetime
from typing import Optional, List, Union, Dict, NewType
from dataclasses import dataclass
from metamodel.metamodelcore import Root, empty_list, empty_dict

{self.gen_references()}

{self.gen_classdefs()}'''

    def gen_references(self) -> str:
        """ Generate NewType declarations for all identifiers

        """
        rval = ["# Class references"]
        for cls in self.schema.classes.values():
            pkeys = self.primary_keys_for(cls)
            for pk in pkeys:
                keyname = camelcase(cls.name) + camelcase(pk)
                keytype = python_name_for(self.schema.slots[pk].range, self.schema)
                rval.append(f'{keyname} = NewType("{keyname}", {keytype})')
            if not pkeys:
                keyname = camelcase(cls.name) + 'Name'
                rval.append(f'{keyname} = NewType("{keyname}", str)')
        rval += [""]
        rval += ["# Type references"]
        rval += [f'{camelcase(k)} = NewType("{camelcase(k)}", {python_name_for(v.typeof, self.schema)})'
                 for k, v in self.schema.types.items()]
        return '\n'.join(rval)

    def gen_classdefs(self) -> str:
        return '\n'.join([self.gen_classdef(k, v) for k, v in self.schema.classes.items() if not v.mixin])

    def gen_classdef(self, clsname: str,  cls: ClassDefinition) -> str:
        parentref = f'({camelcase(cls.is_a if cls.is_a else "Root")})'
        slotdefs = self.gen_slots(cls)
        postinits = self.gen_postinits(cls)
        if not slotdefs:
            slotdefs = 'pass'
        wrapped_description = f'''
    """
    {wrapped_annotation(be(cls.description))}
    """''' if be(cls.description) else ''
        return f'''
@dataclass
class {camelcase(clsname)}{parentref}:{wrapped_description}
    {slotdefs}
    {postinits}'''

    def gen_slots(self, cls: ClassDefinition) -> str:
        return '\n\t'.join([self.gen_slot(cls, pk) for pk in self.primary_keys_for(cls)] +
                           [self.gen_slot(cls, slot) for slot in cls.slots if not self.schema.slots[slot].primary_key])

    def gen_slot(self, cls: ClassDefinition, slotname: str) -> str:
        slot = self.schema.slots[slotname]

        # Alias allows re-use of slot names in different contexts
        if slot.alias:
            slotname = slot.alias

        range_type = self.range_type_name(slot, cls.name)
        # Python version < 3.7 -- forward references have to be quoted
        if slot.inlined and slot.range in self.schema.classes and self.forward_reference(slot.range, cls.name):
            range_type = f'"{range_type}"'
        slot_range, default_val = self.range_cardinality(range_type, slot, cls)
        default = f'= {default_val}' if default_val else ''
        return f'''{underscore(slotname)}: {slot_range} {default}'''

    def gen_postinits(self, cls: ClassDefinition) -> str:
        post_inits = []
        for slot in cls.slots:
            post_init = self.gen_postinit(cls, slot)
            if post_init:
                post_inits.append(post_init)
        post_inits_line = '\n\t\t'.join(post_inits)
        return (f'''
    def _fix_elements(self):
        super()._fix_elements()
        {post_inits_line}''' + '\n') if post_inits else ''

    def gen_postinit(self, cls: ClassDefinition, slotname: str) -> Optional[str]:
        slot = self.schema.slots[slotname]
        if slot.alias:
            slotname = slot.alias
        slotname = python_slot_name(slotname)
        range_type = self.range_type_name(slot, cls.name)
        if (slot.primary_key or slot.required) and cls.is_a:
            return f'''if self.{slotname} is None:
            raise ValueError(f"{slotname} must be supplied")'''
        elif slot.multivalued and slot.range in self.schema.classes and slot.inlined:
            pkeys = self.primary_keys_for(self.schema.classes[slot.range])
            if pkeys:
                pkey_loader = f"{pkeys[0]}=k, "
                return f'''for k, v in self.{slotname}.items():
                if not isinstance(v, {range_type}):
                    self.{slotname}[k] = {range_type}({pkey_loader}**({{}} if v is None else v))'''
            else:
                return f'self.{slotname} = [v if isinstance(v, {range_type}) ' \
                       f'else {range_type}(**({{}} if v is None else v)) for v in self.{slotname}]'
        return ""

    def range_cardinality(self, range_type: str, slot: SlotDefinition, cls: ClassDefinition) \
            -> Tuple[str, Optional[str]]:
        if slot.multivalued:
            pkeys = self.primary_keys_for(self.schema.classes[slot.range]) if slot.range in self.schema.classes else []
            pkey = (camelcase(slot.range) + camelcase(pkeys[0])) if pkeys else 'str'
            range_signature = f"Union[dict, {range_type}]" \
                if slot.inlined and slot.range is not None and slot.range not in builtin_names else range_type
            return (f'List[{range_signature}]', 'empty_list()') if not slot.inlined or not pkeys \
                else (f'Dict[{pkey}, {range_signature}]', 'empty_dict()')
        elif slot.primary_key or slot.required:
            return range_type, 'None' if cls.is_a else None
        elif range_type == 'bool':
            return 'bool', 'False'
        else:
            return f'Optional[{range_type}]', 'None'

    def primary_keys_for(self, cls: ClassDefinition) -> List[SlotDefinitionName]:
        return [slot_name for slot_name in self.all_slots_for(cls) if self.schema.slots[slot_name].primary_key]

    def all_slots_for(self, cls: ClassDefinition) -> List[SlotDefinitionName]:
        return (self.all_slots_for(self.schema.classes[cls.is_a]) if cls.is_a else []) + cls.slots

    def range_type_name(self, slot: SlotDefinition, containing_class_name: ClassDefinitionName) -> str:
        return python_name_for(containing_class_name, self.schema) + camelcase(slot.name) if slot.primary_key else\
            'str' if slot.range is None else\
            python_name_for(slot.range, self.schema) + \
            ('Name' if slot.range not in builtin_names and
                       slot.range not in self.schema.types and not slot.inlined else '')

    def forward_reference(self, slot_range: str, owning_class: str) -> bool:
        for cname in self.schema.classes:
            if cname == owning_class:
                return True             # Occurs on or after
            elif cname == slot_range:
                return False            # Occurs before
        return True
