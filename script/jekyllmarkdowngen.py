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

    doc_root_title = None

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], **kwargs) -> None:
        super().__init__(schema, **kwargs)

    def visit_schema(self, directory: str = None, classes: Set[ClassDefinitionName] = None, image_dir: bool = False,
                     noimages: bool = False, **_) -> None:
        self.gen_classes = classes if classes else []
        for cls in self.gen_classes:
            if cls not in self.schema.classes:
                raise ValueError("Unknown class name: {cls}")
        if self.gen_classes:
            self.gen_classes_neighborhood = self.neighborhood(list(self.gen_classes))

        self.directory = directory
        if directory:
            os.makedirs(directory, exist_ok=True)
        elif image_dir:
            raise ValueError(f"Image directory can only be used with '-d' option")
        if image_dir:
            self.image_directory = os.path.join(directory, 'images')
            if not noimages:
                os.makedirs(self.image_directory, exist_ok=True)
        self.noimages = noimages
        self.types_directory = os.path.join(directory, 'types')
        os.makedirs(self.types_directory, exist_ok=True)
        self.doc_root_title = f'Browse {self.schema.name.title()}'

        with open(os.path.join(directory, 'index.md'), 'w') as ixfile:
            with redirect_stdout(ixfile):
                self.frontmatter(**{'title': self.doc_root_title, 'has_children': 'true', 'nav_order': 2})
                self.para(be(self.schema.description))

                self.header(3, 'Classes')
                with open(os.path.join(directory, 'Classes.md'), 'w') as file:
                    file.write(f'---\nparent: {self.doc_root_title}\ntitle: Classes\nhas_children: true\nnav_order: 1\n---')
                for cls in sorted(self.schema.classes.values(), key=lambda c: c.name):
                    if not cls.is_a and not cls.mixin and self.is_secondary_ref(cls.name):
                        self.class_hier(cls)

                self.header(3, 'Mixins')
                with open(os.path.join(directory, 'Mixins.md'), 'w') as file:
                    file.write(f'---\nparent: {self.doc_root_title}\ntitle: Mixins\nhas_children: true\nnav_order: 2\n---')
                for cls in sorted(self.schema.classes.values(), key=lambda c: c.name):
                    if cls.mixin and self.is_secondary_ref(cls.name):
                        self.class_hier(cls)

                self.header(3, 'Slots')
                with open(os.path.join(directory, 'Slots.md'), 'w') as file:
                    file.write(f'---\nparent: {self.doc_root_title}\ntitle: Slots\nhas_children: true\nnav_order: 3\n---')
                for slot in sorted(self.schema.slots.values(), key=lambda s: s.name):
                    if not slot.is_a and self.is_secondary_ref(slot.name):
                        self.pred_hier(slot)

                self.header(3, 'Types')
                with open(os.path.join(directory, 'Types.md'), 'w') as file:
                    file.write(f'---\nparent: {self.doc_root_title}\ntitle: Types\nhas_children: true\nnav_order: 4\n---')
                self.header(4, 'Built in')
                for builtin_name in sorted(self.synopsis.typebases.keys()):
                    self.bullet(f'**{builtin_name}**')
                self.header(4, 'Defined')
                for typ in sorted(self.schema.types.values(), key=lambda t: t.name):
                    if self.is_secondary_ref(typ.name):
                        if typ.typeof:
                            typ_typ = self.type_link(typ.typeof)
                        else:
                            typ_typ = f'**{typ.base}**'

                        self.bullet(self.type_link(typ, after_link=f' ({typ_typ})', use_desc=True))

    def visit_class(self, cls: ClassDefinition) -> bool:
        if self.gen_classes and cls.name not in self.gen_classes:
            return False
        with open(self.dir_path(cls), 'w') as clsfile:
            with redirect_stdout(clsfile):
                class_curi = self.namespaces.uri_or_curie_for(self.namespaces._base, camelcase(cls.name))
                class_uri = self.namespaces.uri_for(class_curi)
                self.frontmatter(**{'parent': 'Mixins' if cls.mixin else 'Classes', 'title': class_curi, 'grand_parent': self.doc_root_title})
                self.element_header(cls, cls.name, class_curi, class_uri)
                for m in cls.mappings:
                    self.badges(m, 'mapping-label')

                if self.image_directory:
                    yg = YumlGenerator(self)
                    yg.serialize(classes=[cls.name], directory=self.image_directory, load_image=not self.noimages)
                    img_url = os.path.join('images', os.path.basename(yg.output_file_name))
                else:
                    yg = YumlGenerator(self)
                    img_url = yg.serialize(classes=[cls.name])\
                        .replace('[', '\\[').replace('?', '%3F').replace(' ', '%20')

                self.horizontal_line()
                print(f'![img]({img_url})')
                self.horizontal_line()
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
                self.frontmatter(**{'parent': 'Slots', 'title': slot_curie, 'grand_parent': self.doc_root_title})
                simple_name = slot_curie.split(':', 1)[1]
                self.header(1, f"Type: {simple_name}" + (f" _(deprecated)_" if slot.deprecated else ""))
                for s in slot.in_subset:
                    self.badges(s, f'{s}-subset-label')

                self.para(be(slot.description))
                print(f'URI: [{slot_curie}]({slot_uri})')

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

    def visit_type(self, typ: TypeDefinition) -> None:
        with open(self.dir_path(typ), 'w') as typefile:
            with redirect_stdout(typefile):
                full_path = sfx(self.namespaces._base) + (sfx(typ.imported_from) if typ.imported_from else '')
                type_curie = self.namespaces.uri_or_curie_for(full_path, camelcase(typ.name))
                type_uri = self.namespaces.uri_for(type_curie)
                self.frontmatter(**{'parent': 'Types', 'title': type_curie, 'grand_parent': self.doc_root_title})
                self.element_header(typ, typ.name, type_curie, type_uri)

                print("|  |  |  |")
                print("| --- | --- | --- |")
                if typ.typeof:
                    print(f"| Parent type | | {self.class_type_link(typ.typeof)} |")
                print(f"| Root (builtin) type | | **{typ.base}** |")
                if typ.repr:
                    print(f"| Representation | | {typ.repr} |")

    def frontmatter(self, **kwargs) -> None:
        print('---')
        for k,v in kwargs.items():
            print(f'{k}: {v}')
        print('---')

    def element_header(self, obj: Element, name: str, curie: str, uri: str) -> None:
        if curie.startswith('http'):
            simple_name = curie
        else:
            simple_name = curie.split(':', 1)[1]
        self.header(1, f"Type: {simple_name}" + (f" _(deprecated)_" if obj.deprecated else ""))
        self.para(be(obj.description))
        print(f'URI: [{curie}]({uri})')
        print()

    def badges(self, text, style='default-label'):
        print(text)
        print(f"{{: .{style} }}")
        print()

    def horizontal_line(self):
        print('\n---\n')


@shared_arguments(JekyllMarkdownGenerator)
@click.command()
@click.option("--dir", "-d", help="Output directory")
def cli(yamlfile, dir, img, **kwargs):
    """ Generate markdown documentation of a biolink model """
    JekyllMarkdownGenerator(yamlfile, **kwargs).serialize(directory=dir, image_dir=img, **kwargs)

if __name__ == "__main__":
    JekyllMarkdownGenerator(yamlfile='biolink-model.yaml', schema='biolink-model.yaml').serialize(directory='docs')
