import logging
import os
from contextlib import redirect_stdout
from io import StringIO
from typing import Union, TextIO, Optional, Set, List, Any, Callable, Dict

from biolinkml.generators.markdowngen import MarkdownGenerator
from biolinkml.generators.yumlgen import YumlGenerator
from biolinkml.meta import SchemaDefinition, ClassDefinition, SlotDefinition, Element, ClassDefinitionName, \
    TypeDefinition
from biolinkml.utils.formatutils import camelcase, be, underscore, sfx
import argparse


class JekyllMarkdownGenerator(MarkdownGenerator):
    """
    Extends biolinkml.generators.markdowngen.MarkdownGenerator to add new styles
    and override certain existing styles.
    """
    generatorname = os.path.basename(__file__)
    generatorversion = "0.2.0"
    valid_formats = ["md"]
    visit_all_class_slots = False

    doc_root_title = None

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], **kwargs) -> None:
        super().__init__(schema, **kwargs)

    def visit_schema(self, directory: str = None, classes: Set[ClassDefinitionName] = None, image_dir: bool = False, noimages: bool = False, **_) -> None:
        """
        Visit the schema and generate Markdown for each ClassDefinition, SlotDefinition,
        and TypeDefinition.

        Parameters
        ----------
        directory: str
            The directory to write to
        classes: Set[ClassDefinitionName]
            A set of classes to subset
        image_dir: str
            The directory to write static images
        noimages: bool
            Whether or not to generate static images

        """
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
        self.seen_elements = set()
        with open(os.path.join(directory, 'index.md'), 'w') as ixfile:
            # Create the data model index
            with redirect_stdout(ixfile):
                self.frontmatter(**{'title': self.doc_root_title, 'has_children': 'true', 'nav_order': 2, 'layout': 'default', 'has_toc': 'false'})
                self.para(be(self.schema.description))

                self.header(2, 'Classes')

                self.header(3, 'Entities')

                for cls in sorted(self.schema.classes.values(), key=lambda c: c.name):
                    ancs = self.ancestors(cls)
                    if 'named thing' in ancs:
                        if not cls.is_a and not cls.mixin and self.is_secondary_ref(cls.name):
                            self.seen_elements.add(cls.name)
                            self.class_hier(cls)

                self.header(3, 'Associations')
                for cls in sorted(self.schema.classes.values(), key=lambda c: c.name):
                    ancs = self.ancestors(cls)
                    if 'association' in ancs:
                        if not cls.is_a and not cls.mixin and self.is_secondary_ref(cls.name):
                            self.seen_elements.add(cls.name)
                            self.class_hier(cls)

                self.header(3, 'Class Mixins')
                for cls in sorted(self.schema.classes.values(), key=lambda c: c.name):
                    if cls.mixin and self.is_secondary_ref(cls.name):
                        if cls.name not in self.seen_elements:
                            self.seen_elements.add(cls.name)
                            self.class_hier(cls)

                self.header(3, 'Other Classes')
                for cls in sorted(self.schema.classes.values(), key=lambda c: c.name):
                    if cls.name not in self.seen_elements:
                        self.seen_elements.add(cls.name)
                        self.class_hier(cls)

                self.header(2, 'Slots')
                self.header(3, 'Predicates')
                for slot in sorted(self.schema.slots.values(), key=lambda c: c.name):
                    if not slot.alias:
                        if 'related to' in self.ancestors(slot) and not slot.mixin:
                            self.seen_elements.add(slot.name)
                            self.pred_hier(slot)

                self.header(3, 'Node Properties')
                for slot in sorted(self.schema.slots.values(), key=lambda s: s.name):
                    ancs = self.ancestors(slot)
                    if not slot.alias:
                        if 'node property' in ancs and not slot.mixin:
                            self.seen_elements.add(slot.name)
                            self.pred_hier(slot)

                self.header(3, 'Edge Properties')
                for slot in sorted(self.schema.slots.values(), key=lambda s: s.name):
                    ancs = self.ancestors(slot)
                    if not slot.alias:
                        if 'association slot' in ancs and not slot.mixin:
                            self.seen_elements.add(slot.name)
                            self.pred_hier(slot)

                self.header(3, 'Slot Mixins')
                for slot in sorted(self.schema.slots.values(), key=lambda s: s.name):
                    if not slot.alias:
                        if slot.mixin:
                            self.seen_elements.add(slot.name)
                            self.pred_hier(slot)

                self.header(3, 'Other Slots')
                for slot in sorted(self.schema.slots.values(), key=lambda s: s.name):
                    if not slot.alias:
                        if slot.name not in self.seen_elements:
                            self.seen_elements.add(slot.name)
                            self.pred_hier(slot)

                self.header(2, 'Types')
                self.header(3, 'Built in')
                for builtin_name in sorted(self.synopsis.typebases.keys()):
                    self.bullet(f'**{builtin_name}**')

                self.header(3, 'Defined')
                for typ in sorted(self.schema.types.values(), key=lambda t: t.name):
                    if self.is_secondary_ref(typ.name):
                        if typ.typeof:
                            typ_typ = self.type_link(typ.typeof)
                        else:
                            typ_typ = f'**{typ.base}**'

                        self.bullet(self.type_link(typ, after_link=f' ({typ_typ})', use_desc=True))

        # create parent for organizing markdown based on Class types
        with open(os.path.join(directory, 'classes.md'), 'w') as file:
            file.write(f'---\nparent: {self.doc_root_title}\ntitle: Classes\nhas_children: true\nnav_order: 1\nlayout: default\n---')
        with open(os.path.join(directory, 'entities.md'), 'w') as file:
            file.write(f'---\nparent: Classes\ngrand_parent: {self.doc_root_title}\ntitle: Entities\nhas_children: true\nnav_order: 1\nlayout: default\n---')
        with open(os.path.join(directory, 'associations.md'), 'w') as file:
            file.write(
                f'---\nparent: Classes\ngrand_parent: {self.doc_root_title}\ntitle: Associations\nhas_children: true\nnav_order: 2\nlayout: default\n---')
        with open(os.path.join(directory, 'class_mixins.md'), 'w') as file:
            file.write(
                f'---\nparent: Classes\ngrand_parent: {self.doc_root_title}\ntitle: Class Mixins\nhas_children: true\nnav_order: 3\nlayout: default\n---')
        with open(os.path.join(directory, 'other_classes.md'), 'w') as file:
            file.write(
                f'---\nparent: Classes\ngrand_parent: {self.doc_root_title}\ntitle: Other Classes\nhas_children: true\nnav_order: 4\nlayout: default\n---')

        # create parent for organizing markdown based on Slot types
        with open(os.path.join(directory, 'slots.md'), 'w') as file:
            file.write(
                f'---\nparent: {self.doc_root_title}\ntitle: Slots\nhas_children: true\nnav_order: 2\nlayout: default\n---')
        with open(os.path.join(directory, 'predicates.md'), 'w') as file:
            file.write(
                f'---\nparent: Slots\n\ngrand_parent: {self.doc_root_title}\ntitle: Predicates\nhas_children: true\nnav_order: 1\nlayout: default\n---')
        with open(os.path.join(directory, 'node_properties.md'), 'w') as file:
            file.write(
                f'---\nparent: Slots\ngrand_parent: {self.doc_root_title}\ntitle: Node Properties\nhas_children: true\nnav_order: 2\nlayout: default\n---')
        with open(os.path.join(directory, 'edge_properties.md'), 'w') as file:
            file.write(
                f'---\nparent: Slots\ngrand_parent: {self.doc_root_title}\ntitle: Edge Properties\nhas_children: true\nnav_order: 3\nlayout: default\n---')
        with open(os.path.join(directory, 'slot_mixins.md'), 'w') as file:
            file.write(
                f'---\nparent: Slots\ngrand_parent: {self.doc_root_title}\ntitle: Slot Mixins\nhas_children: true\nnav_order: 4\nlayout: default\n---')
        with open(os.path.join(directory, 'other_slots.md'), 'w') as file:
            file.write(
                f'---\nparent: Slots\ngrand_parent: {self.doc_root_title}\ntitle: Other Slots\nhas_children: true\nnav_order: 5\nlayout: default\n---')

        # create parent for organizing markdown based on Type types
        os.makedirs(os.path.join(directory, 'types'), exist_ok=True)
        with open(os.path.join(directory, 'types', 'index.md'), 'w') as file:
            file.write(
                f'---\nparent: {self.doc_root_title}\ntitle: Types\nhas_children: true\nnav_order: 3\nlayout: default\n---')
        with open(os.path.join(directory, 'types', 'built_in_types.md'), 'w') as file:
            file.write(
                f'---\nparent: Types\ngrand_parent: {self.doc_root_title}\ntitle: Built-in Types\nhas_children: true\nnav_order: 1\nlayout: default\n---')
        with open(os.path.join(directory, 'types', 'defined_types.md'), 'w') as file:
            file.write(
                f'---\nparent: Types\ngrand_parent: {self.doc_root_title}\ntitle: Defined Types\nhas_children: true\nnav_order: 2\nlayout: default\n---')

    def visit_class(self, cls: ClassDefinition) -> bool:
        """
        Visit a given class definition and write the following properties in Markdown,
        - Frontmatter
        - Mappings
        - Description
        - UML
        - Identifier prefixes
        - Parents
        - Uses Mixins
        - Children
        - Mixin for
        - Referenced by class
        - Attributes
        - Domain constraints for slots

        Parameters
        ----------
        cls: biolinkml.meta.ClassDefinition
            A ClassDefinition

        Returns
        -------
        bool

        """
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
        """
        Visit a given slot definition and write the following properties in Markdown,
        - Frontmatter
        - Mappings
        - Description
        - Domain and Range constraints
        - Parents
        - Children
        - Used by

        Parameters
        ----------
        cls: biolinkml.meta.SlotDefinition
            A SlotDefinition

        """
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
                            child_slot = self.schema.slots[child]
                            if not child_slot.alias:
                                self.bullet(f' {self.slot_link(child)}')

                    self.header(2, 'Used by')
                    if slot.name in sorted(self.synopsis.slotrefs):
                        for rc in sorted(self.synopsis.slotrefs[slot.name].classrefs):
                            self.bullet(f'{self.class_link(rc)}')
                    if aliased_slot_name == 'relation':
                        if slot.subproperty_of:
                            self.bullet(f' reifies: {self.slot_link(slot.subproperty_of) if slot.subproperty_of in self.schema.slots else slot.subproperty_of}')
                    self.element_properties(slot)

    def class_hier(self, cls: ClassDefinition, level: int = 0) -> None:
        """
        Generate a bullet list representing the hierarchy of a given class.

        Parameters
        ----------
        cls: biolinkml.meta.ClassDefinition
            A ClassDefinition
        level: int
            Markdown level corresponding to H1, H2, H3, etc.

        """
        self.bullet(self.class_link(cls, use_desc=True), level)
        if cls.name in sorted(self.synopsis.isarefs):
            for child in sorted(self.synopsis.isarefs[cls.name].classrefs):
                self.seen_elements.add(child)
                self.class_hier(self.schema.classes[child], level+1)

    def pred_hier(self, slot: SlotDefinition, level: int = 0) -> None:
        """
        Generate a bullet list representing the hierarchy of a given slot.

        Parameters
        ----------
        slot: biolinkml.meta.SlotDefinition
            A SlotDefinition
        level: int
            Markdown level corresponding to H1, H2, H3, etc.

        """
        self.bullet(self.slot_link(slot, use_desc=True), level)
        if slot.name in sorted(self.synopsis.isarefs):
            for child in sorted(self.synopsis.isarefs[slot.name].slotrefs):
                child_slot = self.schema.slots[child]
                if not child_slot.alias and not child_slot.mixin:
                    self.seen_elements.add(child)
                    self.pred_hier(child_slot, level+1)

    def visit_type(self, typ: TypeDefinition) -> None:
        """
        Visit a given type definition and write the following properties in Markdown,
        - Frontmatter
        - Description
        - Domain and Range constraints
        - Parents
        - Children
        - Used by

        Parameters
        ----------
        typ: biolinkml.meta.TypeDefinition
            A TypeDefinition

        """
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

    def frontmatter(self, **kwargs: Dict) -> None:
        """
        Write frontmatter with the given set of key-value pairs.

        Parameters
        ----------
        kwargs: Dict
            A set of key-value pairs.

        """
        print('---')
        for k,v in kwargs.items():
            print(f'{k}: {v}')
        print('---')

    def element_header(self, obj: Element, name: str, curie: str, uri: str) -> None:
        """
        Write the header for an element.

        Parameters
        ----------
        obj: biolinkml.meta.Element
            An element
        name: str
            The name of the element
        curie: str
            The CURIE of the element
        uri: str
            The URI of the element

        """
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

    def badges(self, text: str, style: str = 'default-label'):
        """
        Write a badge with the given text.

        Parameters
        ----------
        text: str
            A text string
        style: str
            The badge style

        """
        print(text)
        print(f"{{: .{style} }}")
        print()

    def horizontal_line(self):
        """
        Write a horizontal line.
        """
        print('\n---\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A generator for creating Jekyll style markdown')
    parser.add_argument('--yaml',  help='the YAML file', required=True)
    parser.add_argument('--dir', help='the destination folder', required=True)
    args = parser.parse_args()
    JekyllMarkdownGenerator(yamlfile=args.yaml, schema=args.yaml).serialize(directory=args.dir)
