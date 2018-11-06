"""Generate JSON-LD contexts

"""
import logging
import os, re
import sys
from typing import Union, TextIO, List, Optional, Dict

import click
from jsonasobj import JsonObj, as_json, as_dict
from prefixcommons import curie_util as cu

from metamodel.metamodel import SchemaDefinition, SlotDefinition, ClassDefinition, Element, Definition, \
    ClassDefinitionName, SlotDefinitionName, TypeDefinitionName
from metamodel.utils.builtins import DEFAULT_BUILTIN_TYPE_NAME, builtin_names, builtin_uri, Builtin
from metamodel.utils.formatutils import camelcase, underscore, be
from metamodel.utils.generator import Generator


class ContextGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.2"
    valid_formats = ['json']
    visit_all_class_slots = False

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str='json') -> None:
        super().__init__(schema, fmt)
        self.prefixmap = dict()
        self.slot_class_maps = dict()
        self.curi_maps: List[Dict[str, str]] = []

    def visit_schema(self):

        # Add the list of curi maps
        for curie_map in self.schema.default_curi_maps:
            self.curi_maps.append(cu.read_biocontext(curie_map))

        # Add any explicitly declared prefixes
        for prefix in self.schema.prefixes.values():
            self.prefixmap[prefix.local_name] = prefix.prefix_uri

        # Add any prefixes explicitly declared
        self.add_id_prefixes(self.schema)

        # Add the default prefix
        base_prefix = self.default_uri()
        if base_prefix:
            self.prefixmap['@vocab'] = base_prefix
            self.prefixmap['@base'] = base_prefix

    def end_schema(self) -> None:
        comments = f'''Auto generated from {self.schema.source_file} by {self.generatorname} version: {self.generatorversion}
Generation date: {self.schema.generation_date}
Schema: {self.schema.name}

id: {self.schema.id}
description: {be(self.schema.description)}
license: {be(self.schema.license)}
'''
        context = JsonObj(comments=comments)
        for k, v in self.slot_class_maps.items():
            self.prefixmap[k] = v
        context['@context'] = self.prefixmap
        print(as_json(context))

    def visit_class(self, cls: ClassDefinition) -> bool:
        class_def = {}
        cn = camelcase(cls.name)
        self.add_mappings(cls, class_def)
        if class_def:
            self.slot_class_maps[cn] = class_def

        # We don't bother to visit class slots - just all slots
        return False

    def visit_slot(self, aliased_slot_name: str, slot: SlotDefinition) -> None:
        slot_def = {}
        sn = underscore(slot.name)

        if not slot.alias:
            rng = self.grounded_slot_range(slot)
            if rng != DEFAULT_BUILTIN_TYPE_NAME:
                builtin_rng_uri = builtin_uri(rng)
                slot_def['@type'] = builtin_rng_uri \
                    if builtin_rng_uri and builtin_names.get(rng, None) not in (Builtin.uri, Builtin.anytype) else "@id"
            if slot.multivalued:
                slot_def['@container'] = '@list'
            self.add_mappings(slot, slot_def)
        if slot_def:
            self.prefixmap[sn] = slot_def

    def add_prefix(self, ncname: str) -> None:
        """ Look up ncname and add it to the prefix map if necessary

        @param ncname: name to add
        """
        if ncname not in self.prefixmap:
            uri = cu.expand_uri(ncname + ':', self.curi_maps)
            if uri and '://' in uri:
                self.prefixmap[ncname] = uri
            else:
                print(f"Unrecognized prefix: {ncname}", file=sys.stderr)
                self.prefixmap[ncname] = f"http://example.org/unknown/{ncname}/"

    def get_uri(self, ncname: str) -> Optional[str]:
        """ Get the URI associated with ncname

        @param ncname:
        """
        uri = cu.expand_uri(ncname + ':', self.curi_maps)
        return uri if uri and uri.startswith('http') else None

    def add_id_prefixes(self, element: Element) -> None:
        for id_prefix in element.id_prefixes:
            self.add_prefix(id_prefix)

    def add_mappings(self, defn: Definition, target: Dict) -> None:
        """ Process any mappings in defn, adding all of the mappings prefixes to the namespace map and
        add a link to the first mapping to the target

        @param defn: Class or Slot definition
        @param target: context target
        """
        self.add_id_prefixes(defn)
        for mapping in defn.mappings:
            if '://' in mapping:
                target['@id'] = mapping
            else:
                if ':' not in mapping or len(mapping.split(':')) != 2:
                    raise ValueError(f"Definition {defn.name} = unrecognized mapping: {mapping}")
                ns = mapping.split(':')[0]
                self.add_prefix(ns)
                target['@id'] = defn.mappings[0]


@click.command()
@click.argument("yamlfile", type=click.Path(exists=True, dir_okay=False))
@click.option("--format", "-f", default='json', type=click.Choice(ContextGenerator.valid_formats), help="Output format")
def cli(yamlfile, format):
    """ Generate jsonld @context definition from biolink model """
    print(ContextGenerator(yamlfile, format).serialize())
