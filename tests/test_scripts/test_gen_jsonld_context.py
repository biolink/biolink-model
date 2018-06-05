import re
import unittest


from metamodel.generators.contextgen import cli
from tests.test_scripts.clicktestcase import ClickTestCase, metadata_filter

# This has to occur post ClickTestCase
import click

update_test_files = False

class GenContextTestCase(ClickTestCase):
    testdir = "genjsonld"
    click_ep = cli
    prog_name = "gen-jsonld-context"

    def test_help(self):
        self.do_test("--help", 'help', update_test_file=update_test_files)
        self.assertFalse(update_test_files, "Updating test files")

    def test_meta(self):
        self.do_test(self.metamodel_file, 'meta.jsonld', update_test_file=update_test_files, filtr=metadata_filter)
        self.do_test(self.metamodel_file + ' -f xsv', 'meta_error', update_test_file=update_test_files,
                     error=click.exceptions.BadParameter)
        self.assertFalse(update_test_files, "Updating test files")

    def test_biolink(self):
        self.maxDiff = None
        self.do_test(self.biolink_file, "biolink-model.jsonld", update_test_file=update_test_files,
                     filtr=metadata_filter)
        self.assertFalse(update_test_files, "Updating test files")


if __name__ == '__main__':
    unittest.main()
