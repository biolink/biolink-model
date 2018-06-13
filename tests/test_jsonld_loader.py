import os
import unittest

from rdflib import Graph, URIRef, Literal, XSD, RDF

from metamodel.generators.jsonldgen import JSONLDGenerator, meta_context
from metamodel.utils.namespaces import BIOENTITY

context_jsonld = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'metamodel', 'context.jsonld'))

json_str = f"""{{
   "name": "metamodel",
   "description": "Metamodel for biolink schema",
   "id": "https://biolink.github.io/metamodel/ontology/meta.ttl",
   "version": "0.2.0",
   "license": "https://creativecommons.org/publicdomain/zero/1.0/",
   "metamodel_version": "0.2.0",
   "source_file": "/Users/solbrig/git/hsolbrig/biolink-model/meta.yaml",
   "source_file_size": 14901,
   "source_file_date": "Mon Jun 11 13:48:39 2018",
   "generation_date": "2018-06-12 12:23",
   "@context": "{context_jsonld}"
}}"""

json_str_2 = f"""{{
   "name": "metamodel",
   "description": "Metamodel for biolink schema",
   "id": "https://biolink.github.io/metamodel/ontology/meta.ttl",
   "version": "0.2.0",
   "license": "https://creativecommons.org/publicdomain/zero/1.0/",
   "metamodel_version": "0.2.0",
   "source_file": "/Users/solbrig/git/hsolbrig/biolink-model/meta.yaml",
   "source_file_size": 14901,
   "source_file_date": "Mon Jun 11 13:48:39 2018",
   "generation_date": "2018-06-12 12:23",
   "slots": {{
      "name": {{
         "name": "name",
         "description": "a unique key that identifies a slot, type or class in a schema",
         "domain": "element",
         "range": "string",
         "primary_key": true,
         "not_inherited": true
      }}
    }},
   "@context": "{context_jsonld}"
}}"""

ontology_id = URIRef('https://biolink.github.io/metamodel/ontology/meta.ttl')

class JSONLDLoaderTestCase(unittest.TestCase):
    def test_basics(self):
        g = Graph()
        g.parse(data=json_str, format="json-ld")

        target = [
            (ontology_id, BIOENTITY.license, Literal('https://creativecommons.org/publicdomain/zero/1.0/')),
            (ontology_id, BIOENTITY.source_file_size, Literal('14901', datatype=XSD.integer)),
             (ontology_id,
              BIOENTITY.name,
              Literal('metamodel')),
             (ontology_id,
              BIOENTITY.source_file,
              Literal('/Users/solbrig/git/hsolbrig/biolink-model/meta.yaml')),
             (ontology_id,
              BIOENTITY.metamodel_version,
              Literal('0.2.0')),
             (ontology_id,
              BIOENTITY.source_file_date,
              Literal('Mon Jun 11 13:48:39 2018')),
             (ontology_id,
              BIOENTITY.description,
              Literal('Metamodel for biolink schema')),
             (ontology_id,
              BIOENTITY.generation_date,
              Literal('2018-06-12 12:23')),
             (ontology_id,
              BIOENTITY.version,
              Literal('0.2.0'))]
        self.assertEqual(sorted(target), sorted(list(g)))

    def test_slot(self):
        cwd = os.path.abspath(os.path.dirname(__file__))
        source = os.path.abspath(os.path.join(cwd, 'source', 'test_slot.ttl'))
        target = os.path.abspath(os.path.join(cwd, 'target', 'test_slot.ttl'))
        g = Graph()
        g.parse(data=json_str_2, format="json-ld")
        g.serialize(destination=target, format="turtle")
        source_graph = Graph()
        source_graph.load(source, format="turtle")
        self.assertTrue(source_graph.isomorphic(g))

    def check_size(self, g: Graph) -> None:
        # Make sure we have 7 classes and 56 slots
        class_bnode = g.value(URIRef("https://biolink.github.io/metamodel/ontology/meta.ttl"), BIOENTITY.classes)
        slot_bnode = g.value(URIRef("https://biolink.github.io/metamodel/ontology/meta.ttl"), BIOENTITY.slots)
        self.assertEqual(7, len([c for c in g.predicate_objects(class_bnode) if c[0] != RDF.rest]))
        self.assertEqual(56, len([s for s in g.predicate_objects(slot_bnode) if s[0] != RDF.rest]))

    def test_full_meta(self):
        cwd = os.path.abspath(os.path.dirname(__file__))
        target = os.path.abspath(os.path.join(cwd, 'target', 'meta.jsonld'))
        yaml_file = os.path.abspath(os.path.join(cwd, '..', 'meta.yaml'))
        # Generate an image of the metamodel
        with open(target, 'w') as tfile:
            tfile.write(JSONLDGenerator(yaml_file).serialize(context=meta_context))

        g = Graph()
        g.load(target, format="json-ld")
        self.check_size(g)
        g.bind('bioentity', BIOENTITY)
        new_ttl = g.serialize(format="turtle").decode()
        new_g = Graph()
        new_g.parse(data=new_ttl, format="turtle")
        self.check_size(new_g)



if __name__ == '__main__':
    unittest.main()
