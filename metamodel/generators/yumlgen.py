"""Generate yuml 

https://yuml.me/diagram/scruffy/class/samples

"""
import os
import sys
from typing import Union, TextIO, Set, List, Optional

import click
import requests
from rdflib import Namespace

from metamodel.metamodel import ClassDefinitionName, SchemaDefinition, SlotDefinitionName, SlotDefinition, \
    ClassDefinition
from metamodel.utils.builtins import builtin_names
from metamodel.utils.formatutils import camelcase, underscore
from metamodel.utils.generator import Generator

yuml_is_a = '^-'
yuml_uses = 'uses -.->'
yuml_injected = '< -.- inject'
yuml_slot_type = ':'
yuml_inline = '++- '
yuml_ref = '- '

yuml_base = 'http://yuml.me/diagram/nofunky'
yuml_scale = ''                # ';scale:180' ';scale:80' for small
yuml_dir = ';dir:TB'           # '
yuml_class = '/class/'
YUML = Namespace(yuml_base + yuml_scale + yuml_dir + yuml_class)


class YumlGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.2"
    valid_formats = ['yuml', 'png', 'pdf', 'jpg', 'json', 'svg']
    visit_all_class_slots = False

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str='yuml') -> None:
        super().__init__(schema, fmt)
        self.referenced: Set[ClassDefinitionName] = None        # List of classes that have to be emitted
        self.generated: Set[ClassDefinitionName] = None         # List of classes that have been emitted
        self.box_generated: Set[ClassDefinitionName] = None     # Class boxes that have been emitted
        self.associations_generated: Set[ClassDefinitionName] = None    # Classes with associations generated
        self.focus_classes: Optional[Set[ClassDefinitionName]] = None   # Classes to be completely filled
        self.gen_classes: Set[ClassDefinitionName] = None           # Classes to be generated
        self.output_file_name: Optional[str] = None             # Location of output file if directory used

    def visit_schema(self, classes: Set[ClassDefinitionName]=None, directory: Optional[str] = None,
                     load_image: bool=True) -> None:
        if directory:
            os.makedirs(directory, exist_ok=True)
        for cls in classes:
            if cls not in self.schema.classes:
                raise ValueError("Unknown class name: {cls}")
        self.box_generated = set()
        self.associations_generated = set()
        self.focus_classes = classes
        if classes:
            self.gen_classes = self.neighborhood(list(classes)).classrefs.union(classes)
        else:
            self.gen_classes = self.synopsis.roots.classrefs
        self.referenced = self.gen_classes
        self.generated = set()
        yumlclassdef: List[str] = []
        while self.referenced.difference(self.generated):
            cn = sorted(list(self.referenced.difference(self.generated)), reverse=True)[0]
            self.generated.add(cn)
            assocs = self.class_associations(ClassDefinitionName(cn), cn in self.referenced)
            if assocs:
                yumlclassdef.append(assocs)

        yuml_url = str(YUML) + ', '.join(yumlclassdef) + \
                   (('.' + self.format) if self.format not in ('yuml', 'png') else '')
        file_suffix = '.png' if self.format == 'yuml' else '.' + self.format
        if directory:
            self.output_file_name = os.path.join(directory,
                                       camelcase(classes[0] if classes else self.schema.name) + file_suffix)
            if load_image:
                resp = requests.get(yuml_url, stream=True)
                if resp.ok:
                    with open(self.output_file_name, 'wb') as f:
                        for chunk in resp.iter_content(chunk_size=2048):
                            f.write(chunk)
        else:
            print(str(YUML)+', '.join(yumlclassdef), end='')

    def class_box(self, cn: ClassDefinitionName) -> str:
        """ Generate a box for the class.  Populate its interior only if (a) it hasn't previously been generated and
        (b) it appears in the gen_classes list

        @param cn:
        @param inherited:
        @return:
        """
        slot_defs: List[str] = []
        if cn not in self.box_generated and (not self.focus_classes or cn in self.focus_classes):
            cls = self.schema.classes[cn]
            for slotname in self.filtered_cls_slots(cn, all_slots=True):
                slot = self.schema.slots[slotname]
                if not slot.range or slot.range in builtin_names or slot.range in self.schema.types:
                    mod = self.prop_modifier(cls, slot)
                    slot_defs.append(underscore(self.aliased_slot_name(slot)) +
                                     mod + ':' +
                                     underscore(slot.range) + self.cardinality(slot))
            self.box_generated.add(cn)
        self.referenced.add(cn)
        return '[' + camelcase(cn) + ('|' + ';'.join(slot_defs) if slot_defs else '') + ']'

    def class_associations(self, cn: ClassDefinitionName, must_render: bool=False) -> str:
        """ Emit all associations for a focus class.  If none are specified, all classes are generated

        @param cn: Name of class to be emitted
        @param must_render: True means render even if this is a target (class is specifically requested)
        @return: YUML representation of the association
        """

        # NOTE: YUML diagrams draw in the opposite order in which they are created, so we work from bottom to top and
        # from right to left
        assocs: List[str] = []
        if cn not in self.associations_generated and (not self.focus_classes or cn in self.focus_classes):
            cls = self.schema.classes[cn]

            # Slots
            for slotname in self.filtered_cls_slots(cn, False)[::-1]:
                slot = self.schema.slots[slotname]
                if slot.range in self.schema.classes:
                    assocs.append(self.class_box(cn) + (yuml_inline if slot.inlined else yuml_ref) +
                                  self.aliased_slot_name(slot) + self.prop_modifier(cls, slot) +
                                  self.cardinality(slot) + '>' + self.class_box(slot.range))

            # Referencing slots
            if cn in self.synopsis.rangerefs:
                for slotname in sorted(self.synopsis.rangerefs[cn]):
                    slot = self.schema.slots[slotname]
                    if slot.domain in self.schema.classes and (slot.range != cls.name or must_render):
                        assocs.append(self.class_box(slot.domain) + (yuml_inline if slot.inlined else yuml_ref) +
                                      self.aliased_slot_name(slot) + self.prop_modifier(cls, slot) +
                                      self.cardinality(slot) + '>' + self.class_box(cn))

            # Mixins used in the class
            for mixin in cls.mixins:
                assocs.append(self.class_box(cn) + yuml_uses + self.class_box(mixin))

            # Classes that use the class as a mixin
            if cls.name in self.synopsis.mixinrefs:
                for mixin in sorted(self.synopsis.mixinrefs[cls.name].classrefs, reverse=True):
                    assocs.append(self.class_box(ClassDefinitionName(mixin)) + yuml_uses + self.class_box(cn))

            # Classes that inject information
            if cn in self.synopsis.applytos:
                for injector in sorted(self.synopsis.applytos[cn].classrefs, reverse=True):
                    assocs.append(self.class_box(cn) + yuml_injected + self.class_box(ClassDefinitionName(injector)))
            self.associations_generated.add(cn)

            # Children
            if cn in self.synopsis.isarefs:
                for is_a_cls in sorted(self.synopsis.isarefs[cn].classrefs, reverse=True):
                    assocs.append(self.class_box(cn) + yuml_is_a + self.class_box(ClassDefinitionName(is_a_cls)))

            # Parent
            if cls.is_a:
                assocs.append(self.class_box(cls.is_a) + yuml_is_a + self.class_box(cn))
        return ', '.join(assocs)

    @staticmethod
    def cardinality(slot: SlotDefinition) -> str:
        if slot.multivalued:
            return ' +' if slot.primary_key or slot.required else ' *'
        else:
            return '' if slot.primary_key or slot.required else ' %3F'

    def filtered_cls_slots(self, cn: ClassDefinitionName, all_slots: bool=True) \
            -> List[SlotDefinitionName]:
        """ Return the set of slots associated with the class that meet the filter criteria.  Slots will be returned
        in defining order, with class slots returned last

        @param cn: name of class to filter
        @param all_slots: True means include attributes
        @return: List of slot definitions
        """
        rval = []
        cls = self.schema.classes[cn]
        cls_slots = self.all_slots(cls, cls_slots_first=True)
        for slot in cls_slots:
            if all_slots or slot.range in self.schema.classes:
                rval.append(slot.name)

        return rval

    def prop_modifier(self, cls: ClassDefinition, slot: SlotDefinition) -> str:
        """ Return the modifiers for the slot:
            (i) - inherited
            (m) - inherited through mixin
            (a) - injected
            (pk) - primary ckey

        @param cls:
        @param slot:
        @return:
        """
        pk = '(pk)' if slot.primary_key else ''
        inherited = slot.name not in cls.slots
        mixin = inherited and slot.name in \
                [mslot.name for mslot in [self.schema.classes[m] for m in cls.mixins]]
        injected = cls.name in self.synopsis.applytos and \
                   slot.name in [aslot.name for aslot in
                                 [self.schema.classes[a] for a in sorted(self.synopsis.applytos[cls.name].classrefs)]]
        return pk + '(a)' if injected else '(m)' if mixin else '(i)' if inherited else ''


@click.command()
@click.argument("yamlfile", type=click.Path(exists=True, dir_okay=False))
@click.option("--classes", "-c", default=None, multiple=True, help="Class(es) to emit")
@click.option("--format", "-f", default='yuml', type=click.Choice(YumlGenerator.valid_formats),
              help="Output format if directory supplied")
@click.option("--directory", "-d", help="Output directory - if supplied, YUML rendering will be saved in file")
def cli(yamlfile, format, classes, directory):
    """ Generate a UML representation of a biolink model """
    print(YumlGenerator(yamlfile, format).serialize(classes=classes, directory=directory), end="")

