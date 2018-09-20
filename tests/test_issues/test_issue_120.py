import os
import unittest

from metamodel.utils.schemaloader import SchemaLoader


class InheritedDomainTestCase(unittest.TestCase):
    def test_domain(self):
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        schema = SchemaLoader(os.path.join(base_dir, 'biolink-model.yaml')).resolve()
        slot = schema.slots['causes']
        self.assertEqual('named thing', slot.domain)
        self.assertEqual('named thing', slot.range)


if __name__ == '__main__':
    unittest.main()
