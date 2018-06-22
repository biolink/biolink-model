import os
import unittest

from rdflib import Graph, URIRef

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

    def check_size(self, g: Graph) -> None:
        # Make sure we have 8 classes and 71 slots
        self.assertEqual(8, len(list(g.objects(URIRef("https://biolink.github.io/metamodel/ontology/meta.ttl"),
                                               BIOENTITY.classes))))
        self.assertEqual(71, len(list(g.objects(URIRef("https://biolink.github.io/metamodel/ontology/meta.ttl"),
                                                BIOENTITY.slots))))

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
