import os
import sys
import unittest

from CFGraph import CFGraph
from pyshex import ShExEvaluator
from rdflib import Graph


class ShexEvalTestCase(unittest.TestCase):

    def shextest(self, rdf_file: str, shex_file: str, focus: str, cfgraph: bool=False) -> None:
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        g = CFGraph() if cfgraph else Graph()
        g.load(os.path.join(base_dir, 'rdf', rdf_file), format="turtle")
        evaluator = ShExEvaluator(g,
                                  os.path.join(base_dir, 'shex', shex_file),
                                  focus,
                                  "http://w3id.org/biolink/vocab/SchemaDefinition")
        result = evaluator.evaluate(debug=False)
        for rslt in result:
            if not rslt.result:
                print(f"Error: {rslt.reason}")
        self.assertTrue(all(r.result for r in result))

    def test_meta_shexeval_no_collections(self):
        self.shextest("meta.ttl", "metanc.shex", "https://biolink.github.io/metamodel/ontology/meta.ttl", cfgraph=True)

    def test_meta_shexeval_collections(self):
        self.shextest("meta.ttl", "meta.shex", "https://biolink.github.io/metamodel/ontology/meta.ttl", cfgraph=False)

    def test_biolink_shexeval_no_collections(self):
        self.shextest("biolink-model.ttl", "metanc.shex",
                      "https://biolink.github.io/biolink-model/ontology/biolink.ttl", cfgraph=True)

    @unittest.skipIf(True, "Biolink collections tests have recursion problems")
    def test_biolink_shexeval_collections(self):
        self.shextest("biolink-model.ttl", "meta.shex",
                      "https://biolink.github.io/biolink-model/ontology/biolink.ttl", cfgraph=False)


if __name__ == '__main__':
    unittest.main()
