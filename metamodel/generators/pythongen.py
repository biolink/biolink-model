import os
import re
from typing import Optional, Tuple, List, Union, TextIO, cast

import click

from metamodel.metamodel import SchemaDefinition, SlotDefinition, ClassDefinition, ClassDefinitionName, \
    SlotDefinitionName
from metamodel.utils.builtins import builtin_names, python_builtins, DEFAULT_BUILTIN_TYPE_NAME
from metamodel.utils.formatutils import camelcase, underscore, be, wrapped_annotation, split_line
from metamodel.utils.generator import Generator


class PythonGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.4"
    valid_formats = ['py']
    visit_all_class_slots = False

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str='py') -> None:
        self.sourcefile = schema
        super().__init__(schema, fmt)
        if not self.schema.source_file and isinstance(self.sourcefile, str) and '\n' not in self.sourcefile:
            self.schema.source_file = self.sourcefile

    def gen_schema(self) -> str:
        split_descripton = '\n#              '.join(split_line(be(self.schema.description), split_len=100))
        return f'''# Auto generated from {self.schema.source_file} by {self.generatorname} version: {self.generatorversion}
# Generation date: {self.schema.generation_date}
# Schema: {self.schema.name}
#
# id: {self.schema.id}
# description: {split_descripton}
# license: {be(self.schema.license)}

import datetime
from typing import Optional, List, Union, Dict, Any
from dataclasses import dataclass
from metamodel.utils.metamodelcore import empty_list, empty_dict
from metamodel.utils.yamlutils import YAMLRoot

metamodel_version = "{self.schema.version}"

{self.gen_inherited()}


# Type names
{self.gen_typedefs()}

# Class references
{self.gen_references()}

{self.gen_classdefs()}'''

    def end_schema(self):
        print(re.sub(r' +\n', '\n', self.gen_schema().replace('\t', '    ')).strip(' '), end='')

    def gen_inherited(self) -> str:
        """ Generate the list of slot properties that are inherited across slot_usage or is_a paths """
        inherited_head = 'inherited_slots: List[str] = ['
        inherited_slots = ', '.join([f'"{underscore(slot.name)}"' for slot in self.schema.slots.values()
                                     if slot.inherited])
        is_rows = split_line(inherited_slots, 120 - len(inherited_head))
        return inherited_head + ('\n' + len(inherited_head) * ' ').join([r.strip() for r in is_rows]) + ']'

    def gen_references(self) -> str:
        """ Generate python type declarations for all identifiers (primary keys)

        """
        rval = []
        for cls in self.schema.classes.values():
            pkeys = self.primary_keys_for(cls)
            for pk in pkeys:
                pk_slot = self.schema.slots[pk]
                classname = camelcase(cls.name) + camelcase(pk)
                if cls.is_a and getattr(self.schema.classes[cls.is_a], pk, None):
                    parent = self.range_type_name(pk_slot, cls.is_a)
                else:
                    parent = self.python_name_for(pk_slot.range)
                rval.append(f'class {classname}({parent}):\n\tpass')
        return '\n\n\n'.join(rval)

    def gen_typedefs(self) -> str:
        """ Generate python type declarations for all defined types """
        rval = []
        for typ in self.schema.types.values():
            typname = self.python_name_for(typ.name)
            parent = self.python_name_for(typ.typeof)
            rval.append(f'class {typname}({parent}):\n\tpass')
        return '\n\n\n'.join(rval) + ('\n' if rval else '')

    def gen_classdefs(self) -> str:
        """ Create class definitions for all non-mixin classes in the model
            Note that apply_to classes are transformed to mixins
        """
        return '\n'.join([self.gen_classdef(k, v) for k, v in self.schema.classes.items() if not v.mixin])

    def gen_classdef(self, clsname: str,  cls: ClassDefinition) -> str:
        """ Generate python definition for class clsname """
        parentref = f'({self.python_name_for(cls.is_a) if cls.is_a else "YAMLRoot"})'
        slotdefs = self.gen_slot_variables(cls)
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

    def gen_slot_variables(self, cls: ClassDefinition) -> str:
        """ Generate python definition for class cls, generating primary keys first followed by the rest of the slots
        """
        return '\n\t'.join([self.gen_slot_variable(cls, pk) for pk in self.primary_keys_for(cls)] +
                           [self.gen_slot_variable(cls, slot)
                            for slot in cls.slots
                            if not self.schema.slots[slot].primary_key and not self.schema.slots[slot].identifier])

    def gen_slot_variable(self, cls: ClassDefinition, slotname: str) -> str:
        """ Generate a slot variable for slotname as defined in class
        """
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
        """ Generate all the typing and existence checks post initialize
        """
        post_inits = []
        if not cls.abstract:
            pkeys = self.primary_keys_for(cls)
            for pkey in pkeys:
                post_inits.append(self.gen_postinit(cls, pkey))
        for slotname in cls.slots:
            slot = self.schema.slots[slotname]
            if not (slot.primary_key or slot.identifier):
                post_inits.append(self.gen_postinit(cls, slotname))
        post_inits_line = '\n\t\t'.join([p for p in post_inits if p])
        return (f'''
    def _fix_elements(self):
        super()._fix_elements()
        {post_inits_line}''' + '\n') if post_inits_line else ''

    def gen_postinit(self, cls: ClassDefinition, slotname: str) -> Optional[str]:
        """ Generate python post init rules for slot in class
        """
        rlines: List[str] = []
        slot = self.schema.slots[slotname]
        if slot.alias:
            slotname = slot.alias
        slotname = self.python_name_for(slotname)
        range_type_name = self.range_type_name(slot, cls.name)

        # Generate existence check for required slots.  Note that inherited classes have to check post-init because
        # named variables can't be mixed in the class signature
        if slot.primary_key or slot.identifier or slot.required:
            if cls.is_a:
                rlines.append(f'if self.{slotname} is None:')
                rlines.append(f'\traise ValueError(f"{slotname} must be supplied")')
                rlines.append(f'if not isinstance(self.{slotname}, {range_type_name}):')
                rlines.append(f'\tself.{slotname} = {range_type_name}(self.{slotname})')
        elif slot.range in self.schema.classes or slot.range in self.schema.types:
            if not slot.multivalued:
                rlines.append(f'if self.{slotname} and not isinstance(self.{slotname}, {range_type_name}):')
                # Another really wierd case -- a class that has no properties
                if slot.range in self.schema.classes and not self.all_slots_for(self.schema.classes[slot.range]):
                    rlines.append(f'\tself.{slotname} = {range_type_name}()')
                else:
                    rlines.append(f'\tself.{slotname} = {range_type_name}(self.{slotname})')
            elif slot.inlined:
                slot_range_cls = self.schema.classes[slot.range]
                pkeys = self.primary_keys_for(slot_range_cls)
                if pkeys:
                    # Special situation -- if there are only two values: primary key and value,
                    # we load it is a list, not a dictionary
                    if len(self.all_slots_for(slot_range_cls)) - len(pkeys) == 1:
                        class_init = '(k, v)'
                    else:
                        pkey_name = self.python_name_for(pkeys[0])
                        class_init = f'({pkey_name}=k, **({{}} if v is None else v))'
                    rlines.append(f'for k, v in self.{slotname}.items():')
                    rlines.append(f'\tif not isinstance(v, {range_type_name}):')
                    rlines.append(f'\t\tself.{slotname}[k] = {range_type_name}{class_init}')
            else:
                rlines.append(f'self.{slotname} = [v if isinstance(v, {range_type_name})')
                indent = len(f'self.{slotname} = [') * ' '
                rlines.append(f'{indent}else {range_type_name}(v) for v in self.{slotname}]')
        return '\n\t\t'.join(rlines)

    def range_cardinality(self, range_type: str, slot: SlotDefinition, cls: ClassDefinition) \
            -> Tuple[str, Optional[str]]:
        if slot.multivalued:
            if slot.range in self.schema.classes:
                slot_range_cls = self.schema.classes[slot.range]
                pkeys = self.primary_keys_for(slot_range_cls)
                if pkeys:
                    pkey = camelcase(slot.range) + camelcase(pkeys[0])
                    non_keys = set(self.all_slots_for(slot_range_cls)).difference(set(pkeys))
                    if len(non_keys) == 1:
                        raw_range_type = self.range_type_name(self.schema.slots[non_keys.pop()], cls.name)
                    else:
                        raw_range_type = "dict"
                else:
                    raw_range_type = "dict"
            else:
                pkeys = None
                pkey = 'str'
            range_signature = f"Union[{raw_range_type}, {range_type}]" \
                if slot.inlined and slot.range is not None and slot.range not in builtin_names else range_type
            return (f'List[{range_signature}]', 'empty_list()') if not slot.inlined or not pkeys \
                else (f'Dict[{pkey}, {range_signature}]', 'empty_dict()')
        elif slot.primary_key or slot.identifier or slot.required:
            return range_type, 'None' if cls.is_a else None
        elif range_type == 'bool':
            return 'bool', 'False'
        else:
            return f'Optional[{range_type}]', 'None'

    def primary_keys_for(self, cls: ClassDefinition) -> List[SlotDefinitionName]:
        """ Return all primary keys / identifiers for cls

        @param cls: class to get keys for
        @return: List of primary keys
        """
        return [slot_name for slot_name in self.all_slots_for(cls)
                if self.schema.slots[slot_name].primary_key or self.schema.slots[slot_name].identifier]

    def all_slots_for(self, cls: ClassDefinition) -> List[SlotDefinitionName]:
        """ Return all slots for class cls """
        if not cls.is_a:
            return cls.slots
        else:
            return [sn for sn in self.all_slots_for(self.schema.classes[cls.is_a]) if sn not in cls.slot_usage] \
                   + cls.slots

    def key_name_for(self, class_name: ClassDefinitionName) -> Optional[str]:
        for slot_name in self.primary_keys_for(self.schema.classes[class_name]):
            return self.python_name_for(class_name) + camelcase(slot_name)
        return None

    def range_type_name(self, slot: SlotDefinition, containing_class_name: ClassDefinitionName) -> str:
        """ Generate the type name for the slot """
        if slot.primary_key or slot.identifier:
            return self.python_name_for(containing_class_name) + camelcase(slot.name)

        if slot.range in self.schema.classes and not slot.inlined:
            class_key = self.key_name_for(cast(ClassDefinitionName, slot.range))
            if class_key:
                return class_key
        return self.python_name_for(slot.range)

    def forward_reference(self, slot_range: str, owning_class: str) -> bool:
        """ Determine whether slot_range is a forward reference """
        for cname in self.schema.classes:
            if cname == owning_class:
                return True             # Occurs on or after
            elif cname == slot_range:
                return False            # Occurs before
        return True

    def python_name_for(self, name: str) -> str:

        def python_class_name() -> str:
            return camelcase(name)

        def python_slot_name() -> str:
            return underscore(name)

        def python_type_name() -> str:
            return camelcase(name)

        if name is None:
            name = DEFAULT_BUILTIN_TYPE_NAME
        return python_class_name() if name in self.schema.classes else \
            python_slot_name() if name in self.schema.slots else \
            python_type_name() if name in self.schema.types else \
            python_builtins[builtin_names[name]] if name in builtin_names else name


@click.command()
@click.argument("yamlfile", type=click.Path(exists=True, dir_okay=False))
@click.option("--format", "-f", default='py', type=click.Choice(PythonGenerator.valid_formats), help="Output format")
def cli(yamlfile, format):
    """ Generate python classes to represent a biolink model """
    print(PythonGenerator(yamlfile, format).serialize())
