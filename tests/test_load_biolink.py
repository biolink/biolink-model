import os
import unittest

from metamodel.utils.loadschema import load_raw_schema


class LoadTranslatorInterchangeTestCase(unittest.TestCase):

    @unittest.skip
    def test_translator(self):
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

        translator_path = os.path.join('source', 'translator_interchange.yaml')
        schema = load_raw_schema(translator_path, base_dir=base_dir)
        # schema = SchemaLoader(monarch_path, base_dir=base_dir).resolve()
        self.assertTrue(True, 'We pass by getting here')


if __name__ == '__main__':
    unittest.main()
