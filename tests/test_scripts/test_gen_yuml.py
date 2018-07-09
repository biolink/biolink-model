import os
import unittest

# This has to occur post ClickTestCase
import click

from metamodel.generators.yumlgen import cli, YumlGenerator
from tests.test_scripts.clicktestcase import ClickTestCase

update_test_files = False


class GenYUMLTestCase(ClickTestCase):
    testdir = "genyuml"
    click_ep = cli
    prog_name = "gen-yuml"

    def test_help(self):
        self.do_test("--help", 'help', update_test_file=update_test_files)
        self.assertFalse(update_test_files, "Updating test files")

    def test_meta(self):
        self.maxDiff = None
        meta_dir = os.path.join(self.testdir_path, 'meta')
        os.makedirs(meta_dir, exist_ok=True)
        self.do_test(self.metamodel_file, 'meta.yuml', update_test_file=update_test_files)
        self.do_test(self.metamodel_file + ' -f yuml', 'meta.yuml', update_test_file=update_test_files)
        self.do_test(self.metamodel_file + ' -f xsv', 'meta_error', update_test_file=update_test_files,
                     error=click.exceptions.BadParameter)
        self.do_test(self.metamodel_file + ' -c definition', 'definition.yuml', update_test_file=update_test_files)
        self.do_test(self.metamodel_file + ' -c definition -c element', 'definition_element.yuml',
                     update_test_file=update_test_files)
        self.do_test(self.metamodel_file + ' -c noclass', 'definition.yuml', update_test_file=update_test_files,
                     error=ValueError)

        self.do_test([self.metamodel_file, '-c', 'schema definition', '-d', meta_dir])
        self.do_test([self.metamodel_file, '-c', 'definition', '-d', meta_dir])
        # Directory tests
        for fmt in YumlGenerator.valid_formats:
            if fmt != 'yuml':
                self.do_test([self.metamodel_file, '-f', fmt, '-c', 'schema definition', '-d', meta_dir])
        # test create directory
        # TODO: delete the target and make sure it creates
        # self.do_test([self.metamodel_file, '-c', 'schema definition', '-d', meta_dir + 'z'])
        self.assertFalse(update_test_files, "Updating test files")

    def test_biolink(self):
        self.maxDiff = None
        self.do_test(self.biolink_file, "biolink-model.yuml", update_test_file=update_test_files)
        self.do_test([self.biolink_file, "-c", "organismal entity"], "organismal_entity.yuml",
                     update_test_file=update_test_files)
        self.assertFalse(update_test_files, "Updating test files")

    def test_occurrent(self):
        biolink_dir = os.path.join(self.testdir_path, 'biolink')
        os.makedirs(biolink_dir, exist_ok=True)
        self.do_test([self.biolink_file, '-c', 'occurrent', '-d', biolink_dir])


if __name__ == '__main__':
    unittest.main()
