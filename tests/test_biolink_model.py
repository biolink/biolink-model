import unittest

from linkml.utils.schemaloader import SchemaLoader

from biolink import BIOLINK_MODEL_YAML


class BiolinkModelTestCase(unittest.TestCase):
    def test_biolink_model(self):
        """ Make sure the biolink model is valid """
        schema = SchemaLoader(BIOLINK_MODEL_YAML)
        errors = []
        try:
            schema.resolve()
        except ValueError as e:
            errors.append(str(e))
        if not errors:
            errors = schema.synopsis.errors()
        self.assertEqual([], errors, "biolink-model.yaml - errors detected")


if __name__ == '__main__':
    unittest.main()
