import os
from contextlib import redirect_stdout
from typing import Union, TextIO, Optional, Set

import click

from metamodel.generators.yumlgen import YumlGenerator
from metamodel.metamodel import SchemaDefinition, ClassDefinition, SlotDefinition, Element, ClassDefinitionName
from metamodel.utils.builtins import builtin_names
from metamodel.utils.formatutils import camelcase, be, underscore
from metamodel.utils.generator import Generator
from metamodel.utils.namespaces import BIOENTITY
from metamodel.utils.schemasynopsis import SchemaSynopsis
from metamodel.utils.typereferences import References


class MarkdownGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.2"
    valid_formats = ["md"]
    visit_all__class_slots = False

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str='json') -> None:
        super().__init__(schema, fmt)
        self.directory: str = None
        self.gen_classes: Optional[Set[ClassDefinitionName]] = None
        self.gen_classes_neighborhood: Optional[References] = None

    def visit_schema(self, directory: str=None, classes: Set[ClassDefinitionName]=None) -> None:
        for cls in classes:
            if cls not in self.schema.classes:
                raise ValueError("Unknown class name: {cls}")
        self.gen_classes = classes
        if classes:
            self.gen_classes_neighborhood = self.neighborhood(list(classes))
        self.directory = directory
        self.synopsis = SchemaSynopsis(self.schema)
        os.makedirs(self.directory, exist_ok=True)
        with open(os.path.join(directory, 'index.md'), 'w') as ixfile:
            with redirect_stdout(ixfile):
                self.frontmatter(f"{self.schema.name.title()} schema")
                self.para(be(self.schema.description))

                self.header(3, 'Classes')
                for cls in sorted(self.schema.classes.values(), key=lambda c: c.name):
                    if not cls.is_a and not cls.mixin and self.secondary_ref(cls.name):
                        self.class_hier(cls)

                self.header(3, 'Mixins')
                for cls in sorted(self.schema.classes.values(), key=lambda c: c.name):
                    if cls.mixin and self.secondary_ref(cls.name):
                        self.class_hier(cls)

                self.header(3, 'Slots')
                for slot in sorted(self.schema.slots.values(), key=lambda s: s.name):
                    if not slot.is_a and self.secondary_ref(slot.name):
                        self.pred_hier(slot)

                self.header(3, 'Types')
                self.header(4, 'Built in')
                for builtin_name in sorted(builtin_names.keys()):
                    self.bullet(f'**{builtin_name}**')
                self.header(4, 'Defined')
                for typ in sorted(self.schema.types.values(), key=lambda t: t.name):
                    if self.secondary_ref(typ.name):
                        if typ.typeof is None:
                            typ_typ = '**string**'
                        elif typ.typeof in builtin_names:
                            typ_typ = f'**{typ.typeof}**'
                        else:
                            typ_typ = self.link(typ.typeof)
                        self.bullet(self.link(typ) +
                                    f' ({typ_typ}){self.description(typ.description)}')

    def visit_class(self, cls: ClassDefinition) -> bool:
        if self.gen_classes and cls not in self.gen_classes:
            return False
        with open(self.dir_path(cls), 'w') as clsfile:
            with redirect_stdout(clsfile):
                self.frontmatter(f"Class: {cls.name}")
                self.para(be(cls.description))

                print(f'URI: {str(BIOENTITY[camelcase(cls.name)])}')
                print()
                yg = YumlGenerator(self.schema).serialize(classes=[cls.name])\
                    .replace('[', '\\[').replace('?', '%3F').replace(' ', '%20')

                print(f'![img]({yg})')
                self.mappings(cls)

                self.header(2, 'Inheritance')
                if cls.is_a is not None:
                    self.bullet(f' is_a: {self.link(cls.is_a)}')
                for mixin in cls.mixins:
                    self.bullet(f' mixin: {self.link(mixin)}')

                self.header(2, 'Children')
                if cls.name in self.synopsis.isarefs:
                    for child in self.synopsis.isarefs[cls.name].classrefs:
                        self.bullet(f' child: {self.link(child)}')
                if cls.name in self.synopsis.mixinrefs:
                    for mixin in self.synopsis.mixinrefs[cls.name].classrefs:
                        self.bullet(f' mixin: {self.link(mixin)}')
                if cls.name in self.synopsis.classrefs:
                    self.header(2, 'Used in')
                    for cn in self.synopsis.classrefs[cls.name].classrefs:
                        self.bullet(f' class: {self.link(cls)} references: {self.link(cn)}')

                self.header(2, 'Fields')
                for sn in cls.slots:
                    slot = self.schema.slots[sn]
                    self.bullet(f'_{self.link(slot)}_')
                    if slot.description:
                        self.bullet(f'_{slot.description}_', level=1)
                    qual = '*' if slot.multivalued else ''
                    qual += ' [required]' if slot.required else ''
                    self.bullet(f'range: {self.link(slot.range) if slot.range else ""}{qual}', level=1)
                    if slot.subproperty_of:
                        self.bullet(f'edge label: {self.link(slot.subproperty_of)}', level=1)
                    for example in slot.examples:
                        self.bullet(f'Example: {self.xlink(example.value)} {example.description}', level=1)
                    if slot.is_a:
                        parent = self.schema.slots[slot.is_a]
                        if parent.domain == cls.name:
                            self.bullet('__Local__', level=1)
                        else:
                            self.bullet(f'inherited from: {self.link(parent.name)}', level=1)

        return True

    def visit_slot(self, aliased_slot_name: str, slot: SlotDefinition) -> None:
        with open(self.dir_path(slot), 'w') as slotfile:
            with redirect_stdout(slotfile):
                self.frontmatter(f"Slot: {aliased_slot_name}")
                self.para(be(slot.description))
                print(f'URI: {str(BIOENTITY[underscore(slot.name)])}')
                self.mappings(slot)

                self.header(2, 'Domain and Range')
                print(f'{self.link(slot.domain)} -> {self.link(slot.range)}')

                self.header(2, 'Inheritance')
                if slot.is_a:
                    self.bullet(f' is_a: {self.link(slot.is_a)}')

                self.header(2, 'Children')
                if slot.name in self.synopsis.isarefs:
                    for child in self.synopsis.isarefs[slot.name].slotrefs:
                        self.bullet(f' child: {self.link(child)}')

                self.header(2, 'Used in')
                if slot.name in self.synopsis.slotrefs:
                    for rc in self.synopsis.slotrefs[slot.name].classrefs:
                        self.bullet(f' usage: {self.link(rc)}')
                if aliased_slot_name == 'relation':
                    if slot.subproperty_of:
                        self.bullet(f' reifies: {self.link(slot.subproperty_of)}')

    def class_hier(self, cls: ClassDefinition, level=0) -> None:
        self.bullet(self.link(cls) + self.description(cls.description), level)
        if cls.name in self.synopsis.isarefs:
            for child in self.synopsis.isarefs[cls.name].classrefs:
                self.class_hier(self.schema.classes[child], level+1)
        
    def pred_hier(self, slot: SlotDefinition, level=0) -> None:
        self.bullet(self.link(slot) + self.description(slot.description), level)
        if slot.name in self.synopsis.isarefs:
            for child in self.synopsis.isarefs[slot.name].slotrefs:
                self.pred_hier(self.schema.slots[child], level+1)

    def dir_path(self, obj: Union[ClassDefinition, SlotDefinition]) -> str:
        return f'{self.directory}/{underscore(self.obj_name(obj))}.md'

    def mappings(self, obj: [SlotDefinition, ClassDefinition]) -> None:
        self.header(2, 'Mappings')
        for mapping in obj.mappings:
            self.bullet(self.xlink(mapping))
        if obj.subclass_of:
            self.bullet(self.xlink(obj.subclass_of))

    def primary_ref(self, cn: ClassDefinitionName) -> bool:
        return not self.gen_classes or cn in self.gen_classes

    def secondary_ref(self, en: str) -> bool:
        if not self.gen_classes:
            return True
        elif en in self.schema.classes:
            return en in self.gen_classes_neighborhood.classrefs
        elif en in self.schema.slots:
            return en in self.gen_classes_neighborhood.slotrefs
        elif en in self.schema.types:
            return en in self.gen_classes_neighborhood.typerefs
        else:
            return True

    # --
    # FORMATTING
    # --

    @staticmethod
    def anchor(id_: str) -> None:
        print(f'<a name="{id_}">', end='')

    @staticmethod
    def anchorend() -> None:
        print('</a>')

    @staticmethod
    def header(level: int, txt: str) -> None:
        print(f'{"#" * level} {txt}\n')

    @staticmethod
    def para(txt: str) -> None:
        print(f'\n{txt}\n')

    @staticmethod
    def bullet(txt: str, level=0) -> None:
        print(f'{"   " * level} * {txt}')

    @staticmethod
    def description(txt: Optional[str]) -> str:
        return f'{" - " + be(txt) if txt else ""}'

    def frontmatter(self, thingtype: str, layout='default') -> None:
        self.header(1, thingtype)
        # print(f'---\nlayout: {layout}\n---\n')

    def link(self, ref: Optional[Union[str, Element]]) -> str:
        obj = self.obj_for(ref) if isinstance(ref, str) else ref
        return ref if obj is None or not self.secondary_ref(obj.name) \
            else  f'[{self.aliased_slot_name(obj) if isinstance(obj, SlotDefinition) else obj.name}]' \
                  f'({self.obj_name(obj)}.{self.format})' + \
                  (f' *subsets: {"| ".join(obj.in_subset)}*' if obj.in_subset else '')

    def xlink(self, id_: str) -> str:
        return f'[{id_}]({self.id_to_url(id_)})'


@click.command()
@click.argument("yamlfile", type=click.File('r'))
@click.option("-d", "--dir", help="Output directory")
@click.option("-f", "--format", default='md', type=click.Choice(['md']), help="Output format")
@click.option("--classes", "-c", default=None, multiple=True, help="Class(es) to emit")
def cli(yamlfile, format, dir, classes):
    """ Generate markdown documentation of a biolink model """
    MarkdownGenerator(yamlfile, format).serialize(classes=classes, directory=dir)
