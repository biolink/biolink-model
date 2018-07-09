import os
import unittest
from typing import Tuple

from metamodel.utils.schemaloader import SchemaLoader


class GeneratorTestCase(unittest.TestCase):
    cwd = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    compdir = os.path.join(cwd, 'source')
    targetdir = os.path.join(cwd, 'target')
    os.makedirs(targetdir, exist_ok=True)

    def gen_test(self, yaml_file: str, output_file: str, generator,
                 update_source: bool=False) -> Tuple[str, str]:
        infile = os.path.abspath(os.path.join(self.cwd, '..', yaml_file))
        compfile = os.path.join(self.compdir, output_file)
        targetfile = os.path.join(self.targetdir, output_file)
        loader = SchemaLoader(infile)
        schema = loader.resolve()
        errors = loader.schema_errors()
        if errors:
            print('\n'.join(errors))
            self.assertTrue(len(errors) == 0)
        g = generator(schema)
        if update_source:
            with open(compfile, 'w') as sourcef:
                sourcef.write(g.serialize())
        with open(targetfile, 'w') as outf:
            outf.write(g.serialize())
        self.assertFalse(update_source, "update_source is True")
        return compfile, targetfile


if __name__ == '__main__':
    unittest.main()
