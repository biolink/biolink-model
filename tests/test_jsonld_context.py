import unittest

from jsonasobj import load, as_json

from metamodel.contextgen import ContextGenerator
from tests.utils.GeneratorTestCase import GeneratorTestCase

update_source: bool = False


class JSONLdContextTestCase(GeneratorTestCase):
    def test_metamodel(self):
        compfile, outfile = self.gen_test('meta.yaml', 'metacontext.jsonld', ContextGenerator, update_source)

        in_json = load(compfile)
        out_json = load(outfile)
        self.assertEqual(in_json, out_json)

    def test_biolinkmodel(self):
        compfile, outfile = self.gen_test('biolink-model.yaml', 'context.jsonld', ContextGenerator, update_source)

        in_json = load(compfile)
        out_json = load(outfile)
        self.maxDiff = None
        self.assertEqual(as_json(in_json), as_json(out_json))


if __name__ == '__main__':
    unittest.main()
