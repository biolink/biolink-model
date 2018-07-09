import re
import unittest

# This has to occur post ClickTestCase
import click

from metamodel.generators.contextgen import cli
from tests.test_scripts.clicktestcase import ClickTestCase

update_test_files = False


def json_metadata_filter(s: str) -> str:
    ...
    return re.sub(r'Auto generated from .*? by', 'Auto generated from ... by',
                  re.sub(r'Generation date: .*?\\n', 'Generation date: \n', s))


class GenContextTestCase(ClickTestCase):
    testdir = "gencontext"
    click_ep = cli
    prog_name = "gen-jsonld-context"

    def test_help(self):
        self.do_test("--help", 'help', update_test_file=update_test_files)
        self.assertFalse(update_test_files, "Updating test files")

    def test_meta(self):
        self.do_test(self.metamodel_file, 'meta.jsonld', update_test_file=update_test_files, filtr=json_metadata_filter)
        self.do_test(self.metamodel_file + ' -f xsv', 'meta_error', update_test_file=update_test_files,
                     error=click.exceptions.BadParameter)
        self.assertFalse(update_test_files, "Updating test files")

    def test_biolink(self):
        self.maxDiff = None
        self.do_test(self.biolink_file, "biolink-model.jsonld", update_test_file=update_test_files,
                     filtr=json_metadata_filter)
        self.assertFalse(update_test_files, "Updating test files")


if __name__ == '__main__':
    unittest.main()
