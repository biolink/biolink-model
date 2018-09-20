import os
import sys
from typing import Union, TextIO, Optional, Set, List

from metamodel.utils.loadschema import load_raw_schema
from metamodel.metamodel import SchemaDefinition, SlotDefinition, SlotDefinitionName, ClassDefinition
from metamodel.utils.schemasynopsis import SchemaSynopsis
from metamodel.utils.mergeutils import merge_schemas, merge_slots


class SchemaLoader:
    def __init__(self, data: Union[str, TextIO], base_dir: Optional[str]=None) -> None:
        self.schema = load_raw_schema(data, base_dir=base_dir)
        self.loaded: Set[str] = {self.schema.name}
        self.base_dir = base_dir

    def resolve(self) -> SchemaDefinition:
        """ Return a fully resolved schema
        """

        if not isinstance(self.schema.slots, dict):
            raise ValueError(f"File: {self.schema.source_file} Slots are not a dictionary")

        if not isinstance(self.schema.classes, dict):
            raise ValueError(f"File: {self.schema.source_file} Classes are not a dictionary")

        # Process imports
        for sname in self.schema.imports:
            if sname not in self.loaded:
                self.loaded.add(sname)
                merge_schemas(self.schema, load_raw_schema(sname + '.yaml', base_dir=self.base_dir))

        # slot.domain --> class.slots
        for slot in self.schema.slots.values():
            if slot.domain in self.schema.classes and slot.name not in self.schema.classes[slot.domain].slots:
                self.schema.classes[slot.domain].slots.append(slot.name)

        # class.slots --> slot.domain
        for cls in self.schema.classes.values():
            if not isinstance(cls, ClassDefinition):
                raise ValueError(
                    f'File: {self.schema.source_file} Class "{cls} (type: {type(cls)})" definition is peculiar')
            if isinstance(cls.slots, str):
                print(f"File: {self.schema.source_file} Class: {cls.name} Slots are not an array", file=sys.stderr)
                cls.slots = [cls.slots]
            for slotname in cls.slots:
                if slotname in self.schema.slots:
                    if self.schema.slots[slotname].domain is None:
                        self.schema.slots[slotname].domain = cls.name

        # apply to --> mixins
        for cls in self.schema.classes.values():
            if cls.apply_to in self.schema.classes:
                self.schema.classes[cls.apply_to].mixins.append(cls.name)

        # Override class slots with slot usage definitions
        for cls in self.schema.classes.values():
            for slot_name, slot_usage in cls.slot_usage.items():
                # Construct a new slot
                # Follow the ancestry of the class to get the most proximal parent
                parent_slot = self.slot_definition_for(slot_name, cls)
                if not parent_slot and slot_name in self.schema.slots:
                    parent_slot = self.schema.slots[slot_name]
                # If parent slot is still not defined, it means that we introduced a NEW slot in the slot usages
                child_name = SlotDefinitionName(cls.name + ' ' + slot_name) if parent_slot else slot_name
                new_slot = SlotDefinition(name=child_name, alias=slot_name, domain=cls.name)
                merge_slots(new_slot, slot_usage)

                # Copy the parent definition.  If there is no parent definition, the slot is being defined
                # locally as a slot_usage
                if parent_slot is not None:
                    new_slot.is_a = parent_slot.name
                    merge_slots(new_slot, parent_slot)

                # Add the slot usage overrides
                merge_slots(new_slot, slot_usage)
                self.schema.slots[child_name] = new_slot

                # Add or replace the slot in the class definition
                append = True
                for i, s in enumerate(cls.slots):
                    if s == slot_name:
                        cls.slots[i] = SlotDefinitionName(child_name)
                        append = False
                        break
                if append:
                    cls.slots.append(SlotDefinitionName(child_name))

        # Update slots with parental information
        merged_slots: List[SlotDefinition] = []
        for slot in self.schema.slots.values():
            self.merge_slot(slot, merged_slots)

        # Clean up the slot range defaults
        for slot in self.schema.slots.values():
            if not slot.range:
                slot.range = 'string'

        return self.schema

    def merge_slot(self, slot: SlotDefinition, merged_slots: List[SlotDefinition]) -> None:
        if slot not in merged_slots:
            if slot.is_a:
                self.merge_slot(self.schema.slots[slot.is_a], merged_slots)
                merge_slots(slot, self.schema.slots[slot.is_a])
            merged_slots.append(slot)

    def schema_errors(self) -> List[str]:
        return SchemaSynopsis(self.schema).errors()

    def slot_definition_for(self, slotname: SlotDefinitionName, cls: ClassDefinition) -> Optional[SlotDefinition]:
        """ Find the most proximal definition for slotname in the context of cls"""
        if cls.is_a:
            for sn in self.schema.classes[cls.is_a].slots:
                slot = self.schema.slots[sn]
                if slot.alias and slotname == slot.alias or slotname == slot.name:
                    return slot
        for mixin in cls.mixins:
            for sn in self.schema.classes[mixin].slots:
                slot = self.schema.slots[sn]
                if slot.alias and slotname == slot.alias or slotname == slot.name:
                    return slot
        if cls.is_a:
            defn = self.slot_definition_for(slotname, self.schema.classes[cls.is_a])
            if defn:
                return defn
        for mixin in cls.mixins:
            defn = self.slot_definition_for(slotname, self.schema.classes[mixin])
            if defn:
                return defn
        return None
