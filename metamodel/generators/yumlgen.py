"""Generate yuml 

https://yuml.me/diagram/scruffy/class/samples

"""
import os
from typing import Union, TextIO, Set, List

import click

from metamodel.metamodel import ClassDefinitionName, SchemaDefinition, SlotDefinitionName, SlotDefinition
from metamodel.utils.builtins import builtin_names
from metamodel.utils.formatutils import camelcase, underscore
from metamodel.utils.generator import Generator
from metamodel.utils.namespaces import YUML
from metamodel.utils.schemasynopsis import SchemaSynopsis

yuml_is_a = '^-'
yuml_uses = 'uses -.->'
yuml_injected = '< -.- inject'
yuml_slot_type = ':'
yuml_inline = '++- '
yuml_ref = '- '


class YumlGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.2"
    valid_formats = ['yuml']

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str='yuml') -> None:
        super().__init__(schema, fmt)
        self.synopsis: SchemaSynopsis = None
        self.referenced: Set[ClassDefinitionName] = None
        self.box_generated: Set[ClassDefinitionName] = None
        self.associations_generated: Set[ClassDefinitionName] = None

    def visit_schema(self, cls: List[ClassDefinitionName]=None):
        classes = [] if cls is None else list(cls)
        closure = self.root_closure(classes)
        self.synopsis = SchemaSynopsis(self.schema)
        self.box_generated = set()
        self.associations_generated = set()
        self.referenced = self.synopsis.roots.classrefs
        yumlclassdef: List[str] = []

        while self.referenced:
            references = self.referenced.copy()
            self.referenced.clear()
            for cn in sorted(list(references)):
                yumlclassdef.append(self.class_associations(cn))

        print(str(YUML)+', '.join(yumlclassdef))

    def class_box(self, cn: ClassDefinitionName, inherited: bool=False) -> str:
        slot_defs: List[str] = []
        if cn not in self.box_generated:
            self.referenced.add(cn)
            for slotname in self.filtered_cls_slots(cn, use_isa=inherited, use_mixins=inherited, use_applytos=True):
                slot = self.schema.slots[slotname]
                if not slot.range or slot.range in builtin_names or slot.range in self.schema.types:
                    # TODO: generalize this
                    if not slot.range:
                        slot.range = 'string'
                    slot_defs.append(underscore(self.slot_name(slot)) + ('(pk)' if slot.primary_key else '') + ':' +
                                                underscore(slot.range) + self.cardinality(slot))
            self.box_generated.add(cn)
        return '[' + camelcase(cn) + ('|' + ';'.join(slot_defs) if slot_defs else '') + ']'

    def class_associations(self, cn: ClassDefinitionName, inherited: bool=False) -> str:
        assocs: List[str] = []
        if cn not in self.associations_generated:
            cls = self.schema.classes[cn]
            if cn in self.synopsis.isarefs:
                for is_a_cls in self.synopsis.isarefs[cn].classrefs:
                    assocs.append(self.class_box(cn, inherited) + yuml_is_a + self.class_box(is_a_cls, inherited))
            for slotname in self.filtered_cls_slots(cn, use_isa=inherited, use_mixins=inherited, use_applytos=True):
                slot = self.schema.slots[slotname]
                if slot.range in self.schema.classes:
                    assocs.append(self.class_box(cn, inherited) + (yuml_inline if slot.inlined else yuml_ref) +
                                  underscore(self.slot_name(slot)) + self.cardinality(slot) + '>' +
                                             self.class_box(slot.range, inherited))
            for mixin in cls.mixins:
                assocs.append(self.class_box(cn, inherited) + yuml_uses + self.class_box(mixin, inherited))
            if cn in self.synopsis.applytos:
                for injector in self.synopsis.applytos[cn].classrefs:
                    assocs.append(self.class_box(cn, inherited) + yuml_injected + self.class_box(injector, inherited))
            self.associations_generated.add(cn)
        return ', '.join(assocs)

    @staticmethod
    def cardinality(slot: SlotDefinition) -> str:
        if slot.multivalued:
            return ' +' if slot.primary_key or slot.required else ' *'
        else:
            return '' if slot.primary_key or slot.required else ' %3F'

    def filtered_cls_slots(self, cn: ClassDefinitionName, *, use_isa: bool, use_mixins: bool, use_applytos: bool) \
            -> List[SlotDefinitionName]:
        """ Return the set of slots associated with the class that meet the filter criteria

        @param cn: name of class to filter
        @param use_isa: If true, include slots derived from the classes ancestors.  If false, only use slots that are
        directly defined in the class
        @param use_mixins: True means include slots from mixins
        @param use_applytos: True means include injected slots
        @return: List of slot definitions that mee the criteria
        """
        def slot_in(classes: Set[ClassDefinitionName]) -> bool:
            return any(slotname in self.schema.classes[cd].slots for cd in classes)

        rval = []
        cls = self.schema.classes[cn]
        cls_mixins = set() if cn not in self.synopsis.mixinrefs else self.synopsis.mixinrefs[cn]
        cls_applytos = set() if cn not in self.synopsis.applytos else self.synopsis.applytos[cn]
        cls_isas = set() if not cls.is_a else {cls.is_a}
        for slotname in cls.slots:
            if (use_isa or not slot_in(cls_isas)) \
                    and (use_mixins or not slot_in(cls_mixins)) \
                    and (use_applytos or not slot_in(cls_applytos)):
                rval.append(slotname)
        return rval


@click.command()
@click.argument("yamlfile", type=click.File('r'))
@click.option("--cls", "-c", default=None, multiple=True, help="Class(es) to emit")
@click.option("--format", "-f", default='yuml', type=click.Choice(['yuml']), help="Output format")
def cli(yamlfile, format, cls):
    print(YumlGenerator(yamlfile, format).serialize(cls=cls))


