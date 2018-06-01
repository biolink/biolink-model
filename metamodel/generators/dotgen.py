"""Generate dotfiles

"""
import os
from typing import TextIO, Union, List, Optional, Set

import click
from graphviz import Digraph, FORMATS

from metamodel.utils.generator import Generator
from metamodel.utils.formatutils import underscore
from tests.target.metamodel import SchemaDefinition, ClassDefinition, SlotDefinition


class DotGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.2"
    valid_formats: Set[str] = FORMATS

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str='png') -> None:
        super().__init__(schema, fmt)
        self.classnames: List[str] = None
        self.filename: Optional[str] = None
        self.dirname: Optional[str] = None
        self.closure: List[str] = None
        self.filedot: Optional[Digraph] = None
        self.classdot: Optional[Digraph] = None
        self.cls_subj: Optional[SlotDefinition] = None
        self.cls_obj: Optional[SlotDefinition] = None
        self.visit_all_slots = True

    def visit_schema(self, classname: List[str], dirname: Optional[str], filename: Optional[str]) -> None:
        self.classnames = [] if classname is None else list(classname)
        self.closure = self.root_closure(self.classnames)
        self.filename = filename
        self.dirname = dirname
        if filename:
            self.filedot = Digraph(comment=self.schema.name)
        if dirname:
            os.makedirs(dirname, exist_ok=True)

    def end_schema(self, **kwargs) -> None:
        if self.filedot:
            self.filedot.format = self.format
            self.filedot.render(self.filename, self.dirname, view=False, cleanup=True)

    def visit_class(self, cls: ClassDefinition) -> bool:
        if self.dirname:
            self.classdot = Digraph(comment=self.schema.name)
        self.node(cls.name, cls.name)
        if cls.is_a:
            self.edge(cls.name, cls.is_a, label="is_a")
        for mixin in cls.mixins:
            self.edge(cls.name, mixin, label="uses")
        self.cls_subj = self.cls_obj = None
        return True

    def end_class(self, cls: ClassDefinition) -> None:
        if self.cls_subj and self.cls_obj:
            rnode = 'relation'
            self.edge(self.slot_name(self.cls_subj), self.slot_name(self.cls_obj), label=rnode)
            self.edge(self.slot_name(self.cls_subj), rnode, style='dotted')
            self.edge(self.slot_name(self.cls_obj), rnode, style='dotted')
        if self.classdot:
            self.classdot.format = self.format
            self.classdot.render(underscore(cls.name), self.dirname, view=False, cleanup=True)

    def visit_class_slot(self, cls: ClassDefinition, slot_name: str, slot: SlotDefinition):
        if slot_name == 'subject':
            self.cls_subj = slot
        elif slot_name == 'object':
            self.cls_obj = slot
        color = 'blue' if slot.name in cls.slots else 'black'
        style = 'dashed' if slot.alias in cls.slots else 'solid'
        self.edge(cls.name, slot_name, label=slot_name, color=color, style=style)
        srange = (slot.range if slot.range else 'Thing') + f" [{slot.subproperty_of}]" if slot.subproperty_of else ""
        self.node(slot.name, srange, color=color)

    def node(self, *args, **kwargs) -> None:
        if self.classdot:
            self.classdot.node(*args, **kwargs)
        if self.filedot:
            self.filedot.node(*args, **kwargs)

    def edge(self, *args, **kwargs) -> None:
        if self.classdot:
            self.classdot.edge(*args, **kwargs)
        if self.filedot:
            self.filedot.edge(*args, **kwargs)


@click.command()
@click.argument("yamlfile", type=click.File('r'))
@click.option("--directory", "-d", help="Output directory - if supplied, a graph per class will be generated")
@click.option("--out", "-o", help="Target file -- if supplied, one large graph will be generated")
@click.option("--classname", "-c", default=None, multiple=True, help="Class(es) to transform")
@click.option("--format", "-f", default='png', type=click.Choice(sorted(list(FORMATS))), help="Output format")
def cli(yamlfile, directory, out, classname, format):
    DotGenerator(yamlfile, format).serialize(classname=classname, dirname=directory, filename=out)

