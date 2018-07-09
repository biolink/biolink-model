import unittest


from metamodel.generators.csvgen import cli
from tests import refresh_files
from tests.test_scripts.clicktestcase import ClickTestCase

# This has to occur post ClickTestCase
import click

update_test_files = False


class GenCSVTestCase(ClickTestCase):
    testdir = "gencsv"
    click_ep = cli
    prog_name = "gen-csv"

    def test_help(self):
        self.do_test("--help", 'help', update_test_file=update_test_files)
        self.assertFalse(update_test_files, "Updating test files")

    def test_meta(self):
        self.do_test(self.metamodel_file, 'meta.csv', update_test_file=update_test_files)
        self.do_test(self.metamodel_file + ' -f tsv', 'meta.tsv', update_test_file=update_test_files)
        self.do_test(self.metamodel_file + ' -f xsv', 'meta_error', update_test_file=update_test_files,
                     error=click.exceptions.BadParameter)
        self.do_test([self.metamodel_file, "-r", "schema definition"], 'meta_sd', update_test_file=update_test_files)
        self.do_test([self.metamodel_file, "-r", "schema definition", "-r", "slot definition"], 'meta_sd_sd',
                     update_test_file=update_test_files)
        self.do_test([self.metamodel_file, "-r", "nada"], 'meta_sd', error=ValueError)
        self.assertFalse(update_test_files, "Updating test files")

    def test_biolink(self):
        self.do_test(self.biolink_file + " -f csv", "biolink-model.csv", update_test_file=update_test_files)
        self.do_test(self.biolink_file + " -f tsv", "biolink-model.tsv", update_test_file=update_test_files)
        self.do_test([self.biolink_file, "-r", "anatomical entity to anatomical entity association"],
                     "biolink-model_part.csv", update_test_file=update_test_files)

        self.assertFalse(update_test_files, "Updating test files")


if __name__ == '__main__':
    unittest.main()
