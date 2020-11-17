import logging
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

import argparse

class JekyllMarkdownGenerator(MarkdownGenerator):
    """
    Extends biolinkml.generators.markdowngen.MarkdownGenerator to add new styles
    and override certain existing styles.
    """
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
        self.doc_root_title = f'Browse {self.schema.name.title().replace("-", " ")}'
        seen_elements = set()
        with open(os.path.join(directory, 'index.md'), 'w') as ixfile:
            with redirect_stdout(ixfile):
                self.frontmatter(**{'title': self.doc_root_title, 'has_children': 'true', 'nav_order': 2, 'layout': 'default', 'has_toc': 'false'})
                self.para(be(self.schema.description))

                self.header(2, 'Classes')
                with open(os.path.join(directory, 'classes.md'), 'w') as file:
                    file.write(f'---\nparent: {self.doc_root_title}\ntitle: Classes\nhas_children: true\nnav_order: 1\nlayout: default\n---')

                self.header(3, 'Entities')
                with open(os.path.join(directory, 'entities.md'), 'w') as file:
                    file.write(f'---\nparent: Classes\ngrand_parent: {self.doc_root_title}\ntitle: Entities\nhas_children: true\nnav_order: 1\nlayout: default\n---')
                for cls in sorted(self.schema.classes.values(), key=lambda c: c.name):
                    ancs = self.ancestors(cls)
                    if 'named thing' in ancs:
                        if not cls.is_a and not cls.mixin and self.is_secondary_ref(cls.name):
                            seen_elements.update(cls.name)
                            self.class_hier(cls)

                self.header(3, 'Associations')
                with open(os.path.join(directory, 'associations.md'), 'w') as file:
                    file.write(f'---\nparent: Classes\ngrand_parent: {self.doc_root_title}\ntitle: Associations\nhas_children: true\nnav_order: 2\nlayout: default\n---')
                for cls in sorted(self.schema.classes.values(), key=lambda c: c.name):
                    ancs = self.ancestors(cls)
                    if 'association' in ancs:
                        if not cls.is_a and not cls.mixin and self.is_secondary_ref(cls.name):
                            seen_elements.update(cls.name)
                            self.class_hier(cls)

                self.header(3, 'Class Mixins')
                with open(os.path.join(directory, 'class_mixins.md'), 'w') as file:
                    file.write(f'---\nparent: Classes\ngrand_parent: {self.doc_root_title}\ntitle: Class Mixins\nhas_children: true\nnav_order: 3\nlayout: default\n---')
                for cls in sorted(self.schema.classes.values(), key=lambda c: c.name):
                    if cls.mixin and self.is_secondary_ref(cls.name):
                        seen_elements.update(cls.name)
                        self.class_hier(cls)

                self.header(3, 'Other Classes')
                with open(os.path.join(directory, 'other_classes.md'), 'w') as file:
                    file.write(f'---\nparent: Classes\ngrand_parent: {self.doc_root_title}\ntitle: Other Classes\nhas_children: true\nnav_order: 4\nlayout: default\n---')
                for cls in sorted(self.schema.classes.values(), key=lambda c: c.name):
                    if cls.name not in seen_elements:
                        seen_elements.update(cls)
                        self.class_hier(cls)

                self.header(2, 'Slots')
                with open(os.path.join(directory, 'slots.md'), 'w') as file:
                    file.write(f'---\nparent: {self.doc_root_title}\ntitle: Slots\nhas_children: true\nnav_order: 2\nlayout: default\n---')

                self.header(3, 'Predicates')
                with open(os.path.join(directory, 'predicates.md'), 'w') as file:
                    file.write(f'---\nparent: Slots\n\ngrand_parent: {self.doc_root_title}\ntitle: Predicates\nhas_children: true\nnav_order: 1\nlayout: default\n---')
                for slot in sorted(self.schema.slots.values(), key=lambda c: c.name):
                    if not slot.alias:
                        if 'related to' in self.ancestors(slot) and not slot.mixin:
                            seen_elements.update(slot.name)
                            self.pred_hier(slot)

                self.header(3, 'Node Properties')
                with open(os.path.join(directory, 'node_properties.md'), 'w') as file:
                    file.write(f'---\nparent: Slots\ngrand_parent: {self.doc_root_title}\ntitle: Node Properties\nhas_children: true\nnav_order: 2\nlayout: default\n---')
                for slot in sorted(self.schema.slots.values(), key=lambda s: s.name):
                    ancs = self.ancestors(slot)
                    if not slot.alias:
                        if 'node property' in ancs and not slot.mixin:
                            seen_elements.update(slot.name)
                            self.pred_hier(slot)

                self.header(3, 'Edge Properties')
                with open(os.path.join(directory, 'edge_properties.md'), 'w') as file:
                    file.write(f'---\nparent: Slots\ngrand_parent: {self.doc_root_title}\ntitle: Edge Properties\nhas_children: true\nnav_order: 3\nlayout: default\n---')
                for slot in sorted(self.schema.slots.values(), key=lambda s: s.name):
                    ancs = self.ancestors(slot)
                    if not slot.alias:
                        if 'association slot' in ancs and not slot.mixin:
                            seen_elements.update(slot.name)
                            self.pred_hier(slot)

                self.header(3, 'Slot Mixins')
                with open(os.path.join(directory, 'slot_mixins.md'), 'w') as file:
                    file.write(f'---\nparent: Slots\ngrand_parent: {self.doc_root_title}\ntitle: Slot Mixins\nhas_children: true\nnav_order: 4\nlayout: default\n---')
                for slot in sorted(self.schema.slots.values(), key=lambda s: s.name):
                    if not slot.alias:
                        if slot.mixin:
                            seen_elements.update(slot.name)
                            self.pred_hier(slot)

                self.header(3, 'Other Slots')
                with open(os.path.join(directory, 'other_slots.md'), 'w') as file:
                    file.write(f'---\nparent: Slots\ngrand_parent: {self.doc_root_title}\ntitle: Other Slots\nhas_children: true\nnav_order: 5\nlayout: default\n---')
                for slot in sorted(self.schema.slots.values(), key=lambda s: s.name):
                    if not slot.alias:
                        if slot.name not in seen_elements:
                            seen_elements.update(slot)
                            self.pred_hier(slot)

                os.makedirs(os.path.join(directory, 'types'), exist_ok=True)
                with open(os.path.join(directory, 'types', 'index.md'), 'w') as file:
                    file.write(f'---\nparent: {self.doc_root_title}\ntitle: Types\nhas_children: true\nnav_order: 1\nlayout: default\n---')

                self.header(2, 'Types')
                with open(os.path.join(directory, 'types', 'built_in_types.md'), 'w') as file:
                    file.write(f'---\nparent: Types\ngrand_parent: {self.doc_root_title}\ntitle: Built-in Types\nhas_children: true\nnav_order: 1\nlayout: default\n---')
                self.header(3, 'Built in')
                for builtin_name in sorted(self.synopsis.typebases.keys()):
                    self.bullet(f'**{builtin_name}**')

                self.header(3, 'Defined')
                with open(os.path.join(directory, 'types', 'defined_types.md'), 'w') as file:
                    file.write(f'---\nparent: Types\ngrand_parent: {self.doc_root_title}\ntitle: Defined Types\nhas_children: true\nnav_order: 2\nlayout: default\n---')
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
                ancs = self.ancestors(cls)
                if 'named thing' in ancs:
                    parent = 'Entities'
                    grand_parent = 'Classes'
                elif 'association' in ancs:
                    parent = 'Associations'
                    grand_parent = 'Classes'
                elif cls.mixin:
                    parent = 'Class Mixins'
                    grand_parent = 'Classes'
                else:
                    parent = 'Other Classes'
                    grand_parent = 'Classes'
                self.frontmatter(**{'parent': parent, 'title': class_curi, 'grand_parent': grand_parent, 'layout': 'default'})
                self.element_header(cls, cls.name, class_curi, class_uri)
                for m in cls.mappings:
                    self.badges(m, 'mapping-label')

                if self.image_directory:
                    yg = YumlGenerator(self)
                    yg.serialize(classes=[cls.name], directory=self.image_directory, load_image=not self.noimages)
                    img_url = os.path.join('images', os.path.basename(yg.output_file_name))
                else:
                    yg = YumlGenerator(self)
                    img_url = yg.serialize(classes=[cls.name])

                img_url = img_url.replace(' ', '%20')
                img_url = img_url.replace('<', '%3C')
                img_url = img_url.replace('^', '%5E')
                img_url = img_url.replace('>', '%3E')
                img_url = img_url.replace('|', '%7C')
                img_url = img_url.replace('*', '%2A')
                img_url = img_url.replace('&#124;', '%7C')

                self.horizontal_line()
                print(f'![img]({img_url})')
                self.horizontal_line()
                self.mappings(cls)

                if cls.id_prefixes:
                    self.header(2, 'Identifier prefixes')
                    for p in cls.id_prefixes:
                        self.bullet(f'{p}')

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

    def visit_slot(self, aliased_slot_name: str, slot: SlotDefinition) -> None:
        if not slot.alias:
            with open(self.dir_path(slot), 'w') as slotfile:
                with redirect_stdout(slotfile):
                    slot_curie = self.namespaces.uri_or_curie_for(self.namespaces._base, underscore(slot.name))
                    slot_uri = self.namespaces.uri_for(slot_curie)
                    ancs = self.ancestors(slot)
                    if 'related to' in ancs:
                        if slot.mixin:
                            parent = 'Slot Mixins'
                        else:
                            parent = 'Predicates'
                        grand_parent = 'Slots'
                        slot_type = 'Relation'
                    elif 'node property' in ancs:
                        if slot.mixin:
                            parent = 'Slot Mixins'
                        else:
                            parent = 'Node Properties'
                        grand_parent = 'Slots'
                        slot_type = 'Slot'
                    elif 'association slot' in ancs:
                        if slot.mixin:
                            parent = 'Slot Mixins'
                        else:
                            parent = 'Edge Properties'
                        grand_parent = 'Slots'
                        slot_type = 'Slot'
                    else:
                        if slot.mixin:
                            parent = 'Slot Mixins'
                        else:
                            parent = 'Other Slots'
                        grand_parent = 'Slots'
                        slot_type = 'Slot'
                    self.frontmatter(**{'parent': parent, 'title': slot_curie, 'grand_parent': grand_parent, 'layout': 'default'})
                    simple_name = slot_curie.split(':', 1)[1]
                    self.header(1, f"{slot_type}: {simple_name}" + (f" _(deprecated)_" if slot.deprecated else ""))
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
                            self.bullet(f' reifies: {self.slot_link(slot.subproperty_of) if slot.subproperty_of in self.schema.slots else slot.subproperty_of}')
                    self.element_properties(slot)

    def visit_type(self, typ: TypeDefinition) -> None:
        with open(self.dir_path(typ), 'w') as typefile:
            with redirect_stdout(typefile):
                full_path = sfx(self.namespaces._base) + (sfx(typ.imported_from) if typ.imported_from else '')
                type_curie = self.namespaces.uri_or_curie_for(full_path, camelcase(typ.name))
                type_uri = self.namespaces.uri_for(type_curie)
                if type_curie.startswith('https://w3id.org/biolink/vocab/biolinkml:types/'):
                    ref = type_curie.split('/')[-1]
                    type_uri = f"https://biolink.github.io/biolinkml/docs/types/{ref}"
                    type_curie = f"metatype:{ref}"

                if typ.imported_from and 'biolinkml:types' in typ.imported_from:
                    parent = 'Built-in Types'
                else:
                    parent = 'Defined Types'
                self.frontmatter(**{'parent': parent, 'grand_parent': 'Types', 'title': type_curie, 'layout': 'default'})
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
            if curie.startswith('https://w3id.org/biolink/vocab/biolinkml:types/'):
                simple_name = curie.split('/')[-1]
                uri = f"https://biolink.github.io/biolinkml/docs/types/{simple_name}"
                simple_name = f"metatype:{simple_name}"
            else:
                simple_name = curie
        else:
            simple_name = curie.split(':', 1)[1]
        if isinstance(obj, TypeDefinition):
            obj_type = 'Type'
        elif isinstance(obj, ClassDefinition):
            obj_type = 'Class'
        elif isinstance(obj, SlotDefinition):
            obj_type = 'Slot'
        else:
            obj_type = 'Class'
        self.header(1, f"{obj_type}: {simple_name}" + (f" _(deprecated)_" if obj.deprecated else ""))
        self.para(be(obj.description))
        print(f'URI: [{curie}]({uri})')
        print()

    def badges(self, text, style='default-label'):
        print(text)
        print(f"{{: .{style} }}")
        print()

    def horizontal_line(self):
        print('\n---\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A generator for creating Jekyll style markdown')
    parser.add_argument('--yaml',  help='the YAML file', required=True)
    parser.add_argument('--dir', help='the destination folder', required=True)
    args = parser.parse_args()
    JekyllMarkdownGenerator(yamlfile=args.yaml, schema=args.yaml).serialize(directory=args.dir)
