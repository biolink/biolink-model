import unittest

from metamodel.utils.loadschema import load_raw_schema

noidtest = """
description: Simple test schema
"""


class NoIDTest(unittest.TestCase):
    def test_no_identifiers(self):
        """ No name or id raises a NO identifier error """
        with self.assertRaises(ValueError):
            nt1 = load_raw_schema(noidtest)


if __name__ == '__main__':
    unittest.main()
