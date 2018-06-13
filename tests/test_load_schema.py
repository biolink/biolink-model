import os
import unittest

from metamodel.metamodel import SchemaDefinition
from metamodel.utils.schemaloader import load_raw_schema, SchemaLoader

schema = """
test1:
    id: "http://bioentity.io/test/test1.yaml"
    description: Simple test schema
    license: https://creativecommons.org/publicdomain/zero/1.0/

    slots:
        s:
            domain: c
            primary_key: true
            description: a slot

        {dupslot}
        
    types:
        identifier type:
          typeof: string
          description: >-
            A string that is intended to uniquely identify a thing
            May be URI in full or compact (CURIE) form
            
        {duptype}
            
    classes:
        c:
          description: A class
          slots:
            - s
            
        {dupclass}
"""

nametest = """
id: "http://bioentity.io/test/test1.yaml"
description: Simple test schema
"""


class LoadSchemaTestCase(unittest.TestCase):

    def eval_result(self, rslt: SchemaDefinition, schemaname: str) -> None:
        self.assertTrue(isinstance(rslt, SchemaDefinition))
        self.assertEqual(rslt.name, schemaname)

    def test_load_file(self):
        """ Test ability to load from string, URI or file name """
        cwd = os.path.abspath(os.path.dirname(__file__))
        filename = os.path.abspath(os.path.join(cwd, '..', 'meta.yaml'))
        self.eval_result(load_raw_schema(filename), 'metamodel')

        with open(filename) as f:
            self.eval_result(load_raw_schema(f.read()), 'metamodel')

        # TODO: Add URL test once this gets committed

    def test_name_variants(self):
        nt1 = load_raw_schema(nametest)
        self.assertEqual(nt1.name, 'http://bioentity.io/test/test1.yaml')
        nt2 = load_raw_schema(nametest + '\nname: nametest')
        self.assertEqual(nt2.name, 'nametest')

    def test_dups(self):
        """ Test  slot, type and class duplicate name checking """
        self.eval_result(load_raw_schema(schema.format(dupslot='', duptype='', dupclass='')), 'test1')
        with self.assertRaises(ValueError):
            load_raw_schema(schema.format(dupslot='s:', duptype='', dupclass=''))
        with self.assertRaises(ValueError):
            load_raw_schema(schema.format(dupslot='', duptype='identifier type:', dupclass=''))
        with self.assertRaises(ValueError):
            load_raw_schema(schema.format(dupslot='', duptype='', dupclass='c:'))

    def test_monarch(self):
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        monarch_path =  os.path.join('contrib', 'monarch.yaml')
        schema = load_raw_schema(monarch_path, base_dir=base_dir)
        schema = SchemaLoader(monarch_path, base_dir=base_dir).resolve()
        self.assertTrue(True, 'We pass by getting here')


if __name__ == '__main__':
    unittest.main()
