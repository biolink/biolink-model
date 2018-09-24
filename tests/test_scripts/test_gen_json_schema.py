import unittest

# This has to occur post ClickTestCase
import click

from metamodel.generators.jsonschemagen import cli
from tests.test_scripts.clicktestcase import ClickTestCase

update_test_files = False


class GenJSONSchemaTestCase(ClickTestCase):
    testdir = "genjsonschema"
    click_ep = cli
    prog_name = "gen-json-schema"

    def test_help(self):
        self.do_test("--help", 'help', update_test_file=update_test_files, tox_wrap_fix=True)
        self.assertFalse(update_test_files, "Updating test files")

    def test_meta(self):
        self.maxDiff = None
        self.do_test(self.metamodel_file, 'meta.json', update_test_file=update_test_files)
        self.do_test(self.metamodel_file + ' -f json', 'meta.json', update_test_file=update_test_files)
        self.do_test(self.metamodel_file + ' -f xsv', 'meta_error', update_test_file=update_test_files,
                     error=click.exceptions.BadParameter)
        self.do_test(self.metamodel_file + " -i", 'meta_inline.json', update_test_file=update_test_files)
        self.assertFalse(update_test_files, "Updating test files")

    def test_biolink(self):
        self.maxDiff = None
        self.do_test(self.biolink_file, "biolink-model.json", update_test_file=update_test_files)
        self.do_test(self.biolink_file + " -i", "biolink-model_inline.json", update_test_file=update_test_files)
        self.assertFalse(update_test_files, "Updating test files")


if __name__ == '__main__':
    unittest.main()
