import os
import re
import unittest
# This has to occur post ClickTestCase
from functools import reduce
from typing import List, Tuple

import click
from rdflib import Graph, URIRef
from rdflib.collection import Collection

from metamodel.generators.contextgen import ContextGenerator
from metamodel.generators.jsonldgen import cli, meta_context, JSONLDGenerator
from metamodel.utils.namespaces import BIOENTITY
from tests.test_scripts.clicktestcase import ClickTestCase

update_test_files = False

repl: List[Tuple[str, str]] = [
    (r'"source_file_size": [0-9]+', ''),
    (r'"source_file_date": "[^"]+"', ''),
    (r'"generation_date": "[^"]+"', ''),
    (r'"source_file": "[^"]+"', '')
]


def filtr(txt: str) -> str:
    return reduce(lambda s, expr: re.sub(expr[0], expr[1], s), repl, txt)


class GenJSONLDTestCase(ClickTestCase):
    testdir = "genjsonld"
    click_ep = cli
    prog_name = "gen-jsonld"

    def test_help(self):
        self.do_test("--help", 'help', update_test_file=update_test_files)
        self.assertFalse(update_test_files, "Updating test files")

    def test_meta(self):
        self.maxDiff = None
        self.do_test(self.metamodel_file + f" --context {meta_context}", 'meta.jsonld',
                     update_test_file=update_test_files, filtr=filtr)
        self.do_test(self.metamodel_file + f' -f jsonld --context {meta_context}', 'meta.jsonld',
                     update_test_file=update_test_files, filtr=filtr)
        self.do_test(self.metamodel_file + f' -f xsv --context {meta_context}', 'meta_error',
                     update_test_file=update_test_files,
                     error=click.exceptions.BadParameter)
        self.assertFalse(update_test_files, "Updating test files")

    def check_size(self, g: Graph, g2: Graph, root: URIRef, expected_classes: int,
                   expected_slots: int, expected_types: int, model: str) -> None:
        for graph in [g, g2]:
            class_bnode = graph.value(root, BIOENTITY.classes)
            slot_bnode = graph.value(root, BIOENTITY.slots)
            type_bnode = graph.value(root, BIOENTITY.types)
            self.assertEqual(expected_classes, len(list(Collection(graph, class_bnode))),
                             f"Expected {expected_classes} classes in {model}")
            self.assertEqual(expected_slots, len(list(Collection(graph, slot_bnode))),
                             f"Expected {expected_slots} slots in {model}")
            self.assertEqual(expected_types, len(list(Collection(graph, type_bnode))),
                             f"Expected {expected_types} types in {model}")

    def test_meta_output(self):
        """ Generate a context AND a jsonld for the metamodel and make sure it parses as RDF """
        cwd = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        temp_dir = os.path.join(cwd, 'temp')
        os.makedirs(temp_dir, exist_ok=True)
        jsonld_path = os.path.join(temp_dir, 'metajson.jsonld')
        rdf_path = os.path.join(temp_dir, 'metardf.ttl')
        yaml_path = os.path.abspath(os.path.join(cwd, '..', '..', 'meta.yaml'))
        meta_context_path = os.path.join(self.testdir_path, 'metacontext.jsonld')
        meta_context_relpath = os.path.basename(meta_context_path)

        # Generate an image of the metamodel
        with open(meta_context_path, 'w') as tfile:
            tfile.write(ContextGenerator(yaml_path).serialize())
        with open(jsonld_path, 'w') as tfile:
            tfile.write(JSONLDGenerator(yaml_path).serialize(context=meta_context_relpath))
        g = Graph()
        g.load(jsonld_path, format="json-ld")
        g.serialize(rdf_path, format="ttl")
        g.bind('bioentity', BIOENTITY)
        new_ttl = g.serialize(format="turtle").decode()
        new_g = Graph()
        new_g.parse(data=new_ttl, format="turtle")
        self.check_size(g, new_g, URIRef("https://biolink.github.io/metamodel/ontology/meta.ttl"), 9, 77, 0, "meta")

    def test_biolink(self):
        self.maxDiff=None
        self.do_test(self.biolink_file, "biolink-model.jsonld", update_test_file=update_test_files, filtr=filtr)
        self.assertFalse(update_test_files, "Updating test files")

    def test_biolink_output(self):
        """ Generate a context AND a jsonld for the metamodel and make sure it parses as RDF """
        cwd = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        temp_dir = os.path.join(cwd, 'temp')
        os.makedirs(temp_dir, exist_ok=True)
        meta_context_path = os.path.join(temp_dir, 'metacontext.jsonld')
        meta_yaml_path = os.path.abspath(os.path.join(cwd, '..', '..', 'meta.yaml'))
        context_path = os.path.join(temp_dir, 'biolinkcontext.jsonld')
        jsonld_path = os.path.join(temp_dir, 'biolinkjson.jsonld')
        meta_context_relpath = os.path.basename(meta_context_path)
        rdf_path = os.path.join(temp_dir, 'biolinkrdf.ttl')
        yaml_path = os.path.abspath(os.path.join(cwd, '..', '..', 'biolink-model.yaml'))

        # Generate an image of the metamodel
        with open(meta_context_path, 'w') as tfile:
            tfile.write(ContextGenerator(meta_yaml_path).serialize())
        with open(context_path, 'w') as tfile:
            tfile.write(ContextGenerator(yaml_path).serialize())
        with open(jsonld_path, 'w') as tfile:
            tfile.write(JSONLDGenerator(yaml_path).serialize(context=meta_context_relpath))
        g = Graph()
        g.load(jsonld_path, format="json-ld")
        g.serialize(rdf_path, format="ttl")
        g.bind('bioentity', BIOENTITY)
        new_ttl = g.serialize(format="turtle").decode()
        new_g = Graph()
        new_g.parse(data=new_ttl, format="turtle")
        self.check_size(g, new_g, URIRef("https://biolink.github.io/biolink-model/ontology/biolink.ttl"),
                        145, 257, 15, "biolink-model")


if __name__ == '__main__':
    unittest.main()
