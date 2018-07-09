import unittest

# This has to occur post ClickTestCase
import click

from metamodel.generators.graphqlgen import cli
from tests.test_scripts.clicktestcase import ClickTestCase

update_test_files = False


class GenGraphqlTestCase(ClickTestCase):
    testdir = "gengraphql"
    click_ep = cli
    prog_name = "gen-graphql"

    def test_help(self):
        self.do_test("--help", 'help', update_test_file=update_test_files)

    def test_meta(self):
        self.do_test(self.metamodel_file, 'meta.graphql', update_test_file=update_test_files)
        self.do_test(self.metamodel_file + ' -f xsv', 'meta_error', update_test_file=update_test_files,
                     error=click.exceptions.BadParameter)
        self.assertFalse(update_test_files, "Updating test files")

    def test_biolink(self):
        self.maxDiff = None
        self.do_test(self.biolink_file, "biolink-model.graphql", update_test_file=update_test_files)
        self.assertFalse(update_test_files, "Updating test files")


if __name__ == '__main__':
    unittest.main()
