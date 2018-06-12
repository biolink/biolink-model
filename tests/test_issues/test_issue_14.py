import unittest

from metamodel.utils.formatutils import camelcase


class CamelCaseTestCase(unittest.TestCase):
    def test_idempotent(self):
        txt = "this is it"
        self.assertEqual(camelcase(txt), camelcase(camelcase(txt)))
        self.assertEqual("MicroRNA", camelcase("microRNA"))
        self.assertEqual("SellTheHouseNOW", camelcase("sell  the\thouseNOW"))
        self.assertEqual("X", camelcase("x"))
        self.assertEqual("X", camelcase("   x   "))


if __name__ == '__main__':
    unittest.main()
