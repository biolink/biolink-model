import os
import unittest

# This has to occur post ClickTestCase
import click

from metamodel.generators.golrgen import cli
from tests.test_scripts.clicktestcase import ClickTestCase

update_test_files = False


class GolrViewTestCase(ClickTestCase):
    testdir = "gengolr"
    click_ep = cli
    prog_name = "gen-golr-views"

    def test_help(self):
        self.do_test("--help", 'help', update_test_file=update_test_files)
        self.assertFalse(update_test_files, "Updating test files")

    def test_meta(self):
        outdir = os.path.join(self.testdir_path, 'meta')
        os.makedirs(outdir, exist_ok=True)
        self.do_test(self.metamodel_file + f" -d {outdir}", update_test_file=update_test_files)
        self.do_test(self.metamodel_file + f' -f xsv -d {outdir}', update_test_file=update_test_files,
                     error=click.exceptions.BadParameter)
        self.assertFalse(update_test_files, "Updating test files")

    def test_biolink(self):
        outdir = os.path.join(self.testdir_path, 'biolink-model')
        os.makedirs(outdir, exist_ok=True)
        self.do_test(self.biolink_file + f" -d {outdir}", update_test_file=update_test_files)
        self.assertFalse(update_test_files, "Updating test files")


if __name__ == '__main__':
    unittest.main()
