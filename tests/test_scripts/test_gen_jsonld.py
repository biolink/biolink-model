import re
import unittest

# This has to occur post ClickTestCase
from functools import reduce
from typing import List, Tuple

import click

from metamodel.generators.jsonldgen import cli, meta_context
from tests.test_scripts.clicktestcase import ClickTestCase

update_test_files = False

repl: List[Tuple[str, str]] = [
    (r'"source_file_size": [0-9]+', '"source_file_size": 199861'),
    (r'"source_file_date": "[^"]+"', '"source_file_date": "Mon Jun 11 21:34:50 2018"'),
    (r'"generation_date": "[^"]+"', '"generation_date": "2018-06-12 13:57"'),
    (r'"source_file": "[^"]+"', '"source_file": "source.yaml",')
]


def filtr(txt: str) -> str:
    return reduce(lambda s, expr: re.sub(expr[0], expr[1], s), repl, txt)


class GenJSONLDTestCase(ClickTestCase):
    testdir = "genjsonld"
    click_ep = cli
    prog_name = "gen-jsonld"

    def test_help(self):
        self.do_test("--help", 'help', update_test_file=update_test_files)
        self.assertFalse(update_test_files, "Updating test files")

    def test_meta(self):
        self.maxDiff = None
        self.do_test(self.metamodel_file + f" --context {meta_context}", 'meta.jsonld',
                     update_test_file=update_test_files, filtr=filtr)
        self.do_test(self.metamodel_file + f' -f jsonld --context {meta_context}', 'meta.jsonld',
                     update_test_file=update_test_files, filtr=filtr)
        self.do_test(self.metamodel_file + f' -f xsv --context {meta_context}', 'meta_error',
                     update_test_file=update_test_files,
                     error=click.exceptions.BadParameter)
        self.assertFalse(update_test_files, "Updating test files")

    def test_biolink(self):
        self.do_test(self.biolink_file, "biolink-model.jsonld", update_test_file=update_test_files, filtr=filtr)
        self.assertFalse(update_test_files, "Updating test files")


if __name__ == '__main__':
    unittest.main()
