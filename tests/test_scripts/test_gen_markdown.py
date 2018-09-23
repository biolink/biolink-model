import os
import unittest

from metamodel.generators.markdowngen import cli
from tests.test_scripts.clicktestcase import ClickTestCase

# This has to occur post ClickTestCase
from tests.utils.dirutils import make_and_clear_directory

update_test_files = False


class GenMarkdownTestCase(ClickTestCase):
    testdir = "genmarkdown"
    click_ep = cli
    prog_name = "gen-markdown"

    def test_help(self):
        self.do_test("--help", 'help', update_test_file=update_test_files)
        self.assertFalse(update_test_files, "Updating test files")

    def test_meta(self):
        outdir = os.path.join(self.testdir_path, 'meta')
        os.makedirs(outdir, exist_ok=True)
        self.do_test(self.metamodel_file + f" -d {outdir}", update_test_file=update_test_files)
        self.assertFalse(update_test_files, "Updating test files")

    def test_biolink(self):
        outdir = os.path.join(self.testdir_path, 'biolink-model')
        os.makedirs(outdir, exist_ok=True)
        self.do_test(self.biolink_file + f" -d {outdir}", update_test_file=update_test_files)
        self.assertFalse(update_test_files, "Updating test files")

    def test_issue_2(self):
        outdir = os.path.join(self.testdir_path, 'issue2')
        make_and_clear_directory(outdir)
        testfile = os.path.join(outdir, 'images', 'Example.png')
        if os.path.exists(testfile):
            os.remove(testfile)
        self.do_test(self.metamodel_file + f" -d {outdir} -c example -i ")
        self.assertTrue(os.path.exists(testfile))
        make_and_clear_directory(outdir)


if __name__ == '__main__':
    unittest.main()
