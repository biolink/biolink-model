import os
from contextlib import redirect_stdout
from io import StringIO
from typing import Union, TextIO, Optional, Set, List, Any, Callable, Dict

import click
from biolinkml.generators.markdowngen import MarkdownGenerator

from biolinkml.generators.yumlgen import YumlGenerator
from biolinkml.meta import SchemaDefinition, ClassDefinition, SlotDefinition, Element, ClassDefinitionName, \
    TypeDefinition
from biolinkml.utils.formatutils import camelcase, be, underscore, sfx
from biolinkml.utils.generator import Generator, shared_arguments

from biolinkml.utils.typereferences import References

class JekyllMarkdownGenerator(MarkdownGenerator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.1.1"
    valid_formats = ["md"]
    visit_all_class_slots = False

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], **kwargs) -> None:
        super().__init__(schema, **kwargs)

    def visit_class(self, cls: ClassDefinition) -> bool:
        if self.gen_classes and cls.name not in self.gen_classes:
            return False
        with open(self.dir_path(cls), 'w') as clsfile:
            with redirect_stdout(clsfile):
                class_curi = self.namespaces.uri_or_curie_for(self.namespaces._base, camelcase(cls.name))
                class_uri = self.namespaces.uri_for(class_curi)
                print(f'---\nparent: "Browse {self.schema.name}"\ntitle: {class_curi}\n---')
                self.element_header(cls, cls.name, class_curi, class_uri)
                for m in cls.mappings:
                    self.badges(m, 'mappinglabel')

                if self.image_directory:
                    yg = YumlGenerator(self)
                    yg.serialize(classes=[cls.name], directory=self.image_directory, load_image=not self.noimages)
                    img_url = os.path.join('images', os.path.basename(yg.output_file_name))
                else:
                    yg = YumlGenerator(self)
                    img_url = yg.serialize(classes=[cls.name])\
                        .replace('[', '\\[').replace('?', '%3F').replace(' ', '%20')

                print(f'![img]({img_url})')
                self.mappings(cls)

                if cls.is_a is not None:
                    self.header(2, 'Parents')
                    self.bullet(f' is_a: {self.class_link(cls.is_a, use_desc=True)}')
                if cls.mixins:
                    self.header(2, 'Uses Mixins')
                    for mixin in cls.mixins:
                        self.bullet(f' mixin: {self.class_link(mixin, use_desc=True)}')

                if cls.name in self.synopsis.isarefs:
                    self.header(2, 'Children')
                    for child in sorted(self.synopsis.isarefs[cls.name].classrefs):
                        self.bullet(f'{self.class_link(child, use_desc=True)}')

                if cls.name in self.synopsis.mixinrefs:
                    self.header(2, 'Mixin for')
                    for mixin in sorted(self.synopsis.mixinrefs[cls.name].classrefs):
                        self.bullet(f'{self.class_link(mixin, use_desc=True, after_link="(mixin)")}')

                if cls.name in self.synopsis.classrefs:
                    self.header(2, 'Referenced by class')
                    for sn in sorted(self.synopsis.classrefs[cls.name].slotrefs):
                        slot = self.schema.slots[sn]
                        if slot.range == cls.name:
                            self.bullet(f' **{self.class_link(slot.domain)}** '
                                        f'*{self.slot_link(slot, add_subset=False)}*{self.predicate_cardinality(slot)}  '
                                        f'**{self.class_type_link(slot.range)}**')

                self.header(2, 'Attributes')
                own_slots = [slot for slot in [self.schema.slots[sn]
                                               for sn in sorted(cls.slots)] if slot.owner == cls.name]
                if own_slots:
                    self.header(3, 'Own')
                    for slot in own_slots:
                        self.slot_field(cls, slot)

                for slot_owner in sorted({slot.owner for slot in [self.schema.slots[sn] for sn in cls.slots]
                                          if slot.owner != slot.name and slot.owner != cls.name}):
                    self.header(3, "Inherited from " + slot_owner + ':')
                    for owner_slot_name in self.schema.classes[slot_owner].slots:
                        owner_slot = self.schema.slots[owner_slot_name]
                        if owner_slot.owner == slot_owner:
                            self.slot_field(cls, owner_slot)

                domain_for_slots = [slot for slot in [self.schema.slots[sn]
                                                      for sn in sorted(cls.slots)] if slot.domain == cls.name]
                if domain_for_slots:
                    self.header(3, 'Domain for slot:')
                    for slot in domain_for_slots:
                        self.slot_field(cls, slot)

                self.element_properties(cls)

        return True

    def visit_class_slot(self, cls: ClassDefinition, aliased_slot_name: str, slot: SlotDefinition) -> None:
        with open(self.dir_path(slot), 'w') as slotfile:
            with redirect_stdout(slotfile):
                slot_curie = self.namespaces.uri_or_curie_for(self.namespaces._base, underscore(slot.name))
                slot_uri = self.namespaces.uri_for(slot_curie)
                print(f'---\nparent: "Browse {self.schema.name}"\ntitle: {slot_curie}\n---')
                self.element_header(slot,aliased_slot_name, slot_curie, slot_uri)
                self.mappings(slot)
                for m in slot.mappings:
                    self.badges(m, 'mapping-label')
                for s in slot.in_subset:
                    self.badges(s, f'{s}-subset-label')

                self.header(2, 'Domain and Range')
                print(f'{self.class_link(slot.domain)} ->{self.predicate_cardinality(slot)} '
                      f'{self.class_type_link(slot.range)}')

                self.header(2, 'Parents')
                if slot.is_a:
                    self.bullet(f' is_a: {self.slot_link(slot.is_a)}')

                self.header(2, 'Children')
                if slot.name in sorted(self.synopsis.isarefs):
                    for child in sorted(self.synopsis.isarefs[slot.name].slotrefs):
                        self.bullet(f' {self.slot_link(child)}')

                self.header(2, 'Used by')
                if slot.name in sorted(self.synopsis.slotrefs):
                    for rc in sorted(self.synopsis.slotrefs[slot.name].classrefs):
                        self.bullet(f'{self.class_link(rc)}')
                if aliased_slot_name == 'relation':
                    if slot.subproperty_of:
                        self.bullet(f' reifies: {self.slot_link(slot.subproperty_of)}')
                self.element_properties(slot)

    def element_header(self, obj: Element, name: str, curie: str, uri: str) -> None:
        simple_name = curie.split(':', 1)[1]
        self.frontmatter(f"Type: {simple_name}" + (f" _(deprecated)_" if obj.deprecated else ""))
        self.para(be(obj.description))
        print(f'URI: [{curie}]({uri})')
        print()

    def badges(self, text, style='default-label'):
        print(text)
        print(f"{{: .{style} }}")
        print()


@shared_arguments(JekyllMarkdownGenerator)
@click.command()
@click.option("--dir", "-d", help="Output directory")
def cli(yamlfile, dir, img, **kwargs):
    """ Generate markdown documentation of a biolink model """
    JekyllMarkdownGenerator(yamlfile, **kwargs).serialize(directory=dir, image_dir=img, **kwargs)

if __name__ == "__main__":
    JekyllMarkdownGenerator(yamlfile='biolink-model.yaml', schema='biolink-model.yaml').serialize(directory='docs')
