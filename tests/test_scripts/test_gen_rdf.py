import os
import unittest

# This has to occur post ClickTestCase
from urllib.parse import urljoin

import click

from metamodel.generators.jsonldgen import meta_context
from metamodel.generators.rdfgen import cli
from tests.test_scripts.clicktestcase import ClickTestCase

update_test_files = False

cwd = os.path.dirname(__file__)
meta_context = urljoin('file:', os.path.join(cwd, 'output', 'gencontext', 'meta.jsonld'))


class GenRDFTestCase(ClickTestCase):
    testdir = "genrdf"
    click_ep = cli
    prog_name = "gen-rdf"
    # TODO: Need to add RDF difference or cannonical representation to do this test
    soft_compare = "Files are different, but it could be an RDF ordering issue"

    def test_help(self):
        self.do_test("--help", 'help', update_test_file=update_test_files, bypass_soft_compare=True)
        self.assertFalse(update_test_files, "Updating test files")

    def test_meta(self):
        self.maxDiff = None
        self.do_test(self.metamodel_file + f" --context {meta_context}", 'meta.ttl',
                     update_test_file=update_test_files)
        self.do_test(self.metamodel_file + f' -f xml --context {meta_context}', 'meta.xml',
                     update_test_file=update_test_files)
        self.do_test(self.metamodel_file + f' -f n3  --context {meta_context}', 'meta.n3',
                     update_test_file=update_test_files)
        self.do_test(self.metamodel_file + f' -f xsv  --context {meta_context}', 'meta_error',
                     update_test_file=update_test_files,
                     error=click.exceptions.BadParameter)
        self.assertFalse(update_test_files, "Updating test files")

    def test_biolink(self):
        self.do_test(self.biolink_file + f" --context {meta_context}", 'biolink-model.ttl',
                     update_test_file=update_test_files)
        self.do_test(self.biolink_file + f" -f n3 --context {meta_context}", 'biolink-model.n3',
                     update_test_file=update_test_files)
        self.assertFalse(update_test_files, "Updating test files")


if __name__ == '__main__':
    unittest.main()
