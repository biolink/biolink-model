import unittest

# This has to occur post ClickTestCase
import click

from metamodel.generators.ontolgen import cli
from tests.test_scripts.clicktestcase import ClickTestCase

update_test_files = False


class GenRDFTestCase(ClickTestCase):
    testdir = "genrdf"
    click_ep = cli
    prog_name = "gen-rdf"

    def test_help(self):
        self.do_test("--help", 'help', update_test_file=update_test_files)
        self.assertFalse(update_test_files, "Updating test files")

    def test_meta(self):
        self.do_test(self.metamodel_file, 'meta.ttl', update_test_file=update_test_files)
        self.do_test(self.metamodel_file + ' -f xml', 'meta.xml', update_test_file=update_test_files)
        self.do_test(self.metamodel_file + ' -f json-ld', 'meta.jsonld', update_test_file=update_test_files)
        self.do_test(self.metamodel_file + ' -f xsv', 'meta_error', update_test_file=update_test_files,
                     error=click.exceptions.BadParameter)
        self.assertFalse(update_test_files, "Updating test files")

    def test_biolink(self):
        self.do_test(self.biolink_file, "biolink-model.ttl", update_test_file=update_test_files)
        self.do_test(self.biolink_file + " -f n3", "biolink-model.n3", update_test_file=update_test_files)
        self.assertFalse(update_test_files, "Updating test files")


if __name__ == '__main__':
    unittest.main()
