import unittest


from metamodel.generators.yumlgen import cli
from tests.test_scripts.clicktestcase import ClickTestCase

# This has to occur post ClickTestCase
import click

update_test_files = True


class GenYUMLTestCase(ClickTestCase):
    testdir = "genyuml"
    click_ep = cli
    prog_name = "gen-yuml"

    def test_help(self):
        self.do_test("--help", 'help', update_test_file=update_test_files)
        self.assertFalse(update_test_files, "Updating test files")

    def test_meta(self):
        self.do_test(self.metamodel_file, 'meta.yuml', update_test_file=update_test_files)
        self.do_test(self.metamodel_file + ' -f yuml', 'meta.yuml', update_test_file=update_test_files)
        self.do_test(self.metamodel_file + ' -f xsv', 'meta_error', update_test_file=update_test_files,
                     error=click.exceptions.BadParameter)
        self.assertFalse(update_test_files, "Updating test files")

    def test_biolink(self):
        self.do_test(self.biolink_file, "biolink-model.yuml", update_test_file=update_test_files)
        self.do_test(self.biolink_file + " -i", "biolink-model_inline.yuml", update_test_file=update_test_files)
        self.assertFalse(update_test_files, "Updating test files")


if __name__ == '__main__':
    unittest.main()
