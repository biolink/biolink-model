import unittest

# This has to occur post ClickTestCase
import click

from metamodel.generators.shexgen import cli
from tests.test_scripts.clicktestcase import ClickTestCase

update_test_files = False


class GenShExTestCase(ClickTestCase):
    testdir = "genshex"
    click_ep = cli
    prog_name = "gen-shex"

    def test_help(self):
        self.do_test("--help", 'help', update_test_file=update_test_files)
        self.assertFalse(update_test_files, "Updating test files")

    def test_meta(self):
        self.maxDiff = None
        self.do_test(self.metamodel_file + ' -f json', 'meta.json', update_test_file=update_test_files)
        self.do_test(self.metamodel_file + ' -f rdf', 'meta.ttl', update_test_file=update_test_files)
        self.do_test(self.metamodel_file, 'meta.shex', update_test_file=update_test_files, error=NotImplementedError)
        self.do_test(self.metamodel_file + ' -f shex', 'meta.shex', update_test_file=update_test_files,
                     error=NotImplementedError)
        self.do_test(self.metamodel_file + f' -f xsv', 'meta_error',
                     update_test_file=update_test_files, error=click.exceptions.BadParameter)
        self.assertFalse(update_test_files, "Updating test files")

    # TODO: Need to add RDF difference or cannonical representation to do this test
    def test_biolink(self):
        self.do_test(self.biolink_file, "biolink-model.shex", update_test_file=update_test_files,
                     error=NotImplementedError)
        self.do_test(self.biolink_file + " -f json", "biolink-model.json", update_test_file=update_test_files)
        self.do_test(self.biolink_file + " -f rdf", "biolink-model.ttl", update_test_file=update_test_files)
        self.assertFalse(update_test_files, "Updating test files")


if __name__ == '__main__':
    unittest.main()
