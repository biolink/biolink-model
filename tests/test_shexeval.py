import os
import sys
import unittest

from CFGraph import CFGraph
from pyshex import ShExEvaluator
from rdflib import Graph


class ShexEvalTestCase(unittest.TestCase):

    def shextest(self, rdf_file: str, shex_file: str, focus: str, cfgraph: bool=False, rdf_path: bool=False) -> None:
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        g = CFGraph() if cfgraph else Graph()
        g.load(rdf_file if rdf_path else os.path.join(base_dir, 'rdf', rdf_file), format="turtle")
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
        """ Test ShEx definition of metamodel against the metamodel with no RDF collections  """
        self.shextest("meta.ttl", "metanc.shex", "https://biolink.github.io/metamodel/ontology/meta.ttl", cfgraph=True)

    def test_meta_shexeval_collections(self):
        """ Test ShEx definition recursive collections definitions against metamodel
         (incomplete because lists are shortened) """
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        rdf_file = os.path.join(base_dir, 'source', 'meta_rdf.ttl')
        self.shextest(rdf_file, "meta.shex", "https://biolink.github.io/metamodel/ontology/meta.ttl", cfgraph=False,
                      rdf_path=True)

    @unittest.skipIf(True, "Need to find the failure issue below")
    def test_biolink_shexeval_no_collections(self):
        """ Test ShEx definition of metamodel against the biolink model w/ no RDF collections """
        self.shextest("biolink-model.ttl", "metanc.shex",
                      "https://biolink.github.io/biolink-model/ontology/biolink.ttl", cfgraph=True)

    @unittest.skipIf(True, "Need to find the failure issue below")
    def test_biolink_shexeval_collections(self):
        """ Test ShEx definition recursive collections definitions against biolink model
                 (incomplete because lists are shortened) """
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        rdf_file = os.path.join(base_dir, 'source', 'biolink-model_rdf.ttl')
        self.shextest(rdf_file, "meta.shex",
                      "https://biolink.github.io/biolink-model/ontology/biolink.ttl", cfgraph=False, rdf_path=True)


if __name__ == '__main__':
    unittest.main()
