import os
import unittest
from typing import Callable, Tuple

from metamodel.metamodel import SchemaDefinition
from metamodel.schemaloader import load_schema


class GeneratorTestCase(unittest.TestCase):
    cwd = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    compdir = os.path.join(cwd, 'source')
    targetdir = os.path.join(cwd, 'target')
    os.makedirs(targetdir, exist_ok=True)

    def gen_test(self, yaml_file: str, output_file: str, generator: Callable[[SchemaDefinition], None],
                 update_source: bool=False) -> Tuple[str, str]:
        infile = os.path.abspath(os.path.join(self.cwd, '..', yaml_file))
        compfile = os.path.join(self.compdir, output_file)
        targetfile = os.path.join(self.targetdir, output_file)
        schemas = load_schema(infile)
        self.assertEqual(len(schemas), 1, "Multi schema files are not currently processed")
        g = generator(schema=list(schemas.values())[0])
        if update_source:
            with open(compfile, 'w') as sourcef:
                sourcef.write(g.serialize())
        with open(targetfile, 'w') as outf:
            outf.write(g.serialize())
        self.assertFalse(update_source, "update_source is True")
        return compfile, targetfile


if __name__ == '__main__':
    unittest.main()
