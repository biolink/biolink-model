from typing import Union, TextIO, Optional, Set, List

from metamodel.utils.loadschema import load_schema
from metamodel.metamodel import SchemaDefinition, SlotDefinition, SlotDefinitionName, ClassDefinition
from metamodel.utils.schemasynopsis import SchemaSynopsis
from metamodel.utils.mergeutils import merge_schemas, merge_slots


class SchemaLoader:
    def __init__(self, data: Union[str, TextIO]) -> None:
        self.schema = load_schema(data)
        self.loaded: Set[str] = {self.schema.name}

    def resolve(self) -> SchemaDefinition:
        """ Return a fully resolved schema
        """

        # Process imports
        for sname in self.schema.imports:
            if sname not in self.loaded:
                self.loaded.add(sname)
                merge_schemas(self.schema, load_schema(sname))

        # Inject slots into classes - we haven't error checked yet so we have to be cautious
        for slot in self.schema.slots.values():
            if slot.domain in self.schema.classes and slot.name not in self.schema.classes[slot.domain].slots:
                self.schema.classes[slot.domain].slots.append(slot.name)

        # Inject class extensions as reverse mixins
        for cls in self.schema.classes.values():
            if cls.apply_to in self.schema.classes:
                self.schema.classes[cls.apply_to].mixins.append(cls.name)

        # Incorporate the mixins into the referencing classes
        for cls in self.schema.classes.values():
            for mixin in cls.mixins:
                cls.slots += self.schema.classes[mixin].slots

        # Apply slot usages
        for cls in self.schema.classes.values():
            for slot_name, slot_usage in cls.slot_usage.items():
                # Construct a new slot
                child_name = SlotDefinitionName(cls.name + ' ' + slot_name)
                new_slot = SlotDefinition(name=child_name, alias=slot_name, domain=cls.name)

                # Copy the parent definition
                parent_slot = self.slot_definition_for(slot_name, cls)
                if parent_slot is not None:
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
        return self.schema

    def schema_errors(self) -> List[str]:
        return SchemaSynopsis(self.schema).errors()


    def slot_definition_for(self, slotname: SlotDefinitionName, cls: ClassDefinition) -> Optional[SlotDefinition]:
        if cls.is_a:
            parent = self.schema.classes[cls.is_a]
            if slotname in parent.slots:
                return self.schema.slots[slotname]
            else:
                for s in cls.slots:
                    if self.schema.slots[s].alias == slotname:
                        return self.schema.slots[s]
            return self.slot_definition_for(slotname, parent)
        return None
