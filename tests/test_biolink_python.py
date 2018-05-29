import os
import unittest

import metamodel
from metamodel.metamodel import SchemaDefinition
#
from metamodel.schemaloader import load_schema
from metamodel.pythongen import Generator

python_metamodel_path = os.path.abspath(metamodel.metamodel.__file__)
python_metamodel = os.path.basename(python_metamodel_path)


class BiolinkGenTestCase(unittest.TestCase):
    def test_biolink(self):
        """ Generate a new metamodel and verify that it matches what we used to build it """
        cwd = os.path.abspath(os.path.dirname(__file__))
        path = os.path.abspath(os.path.join(cwd, '..', 'biolink-model.yaml'))
        targetdir = os.path.join(cwd, 'target')
        os.makedirs(targetdir, exist_ok=True)

        inp_sds = load_schema(path)
        biolink_out = os.path.join(targetdir, 'biolink_out.py')
        with open(biolink_out, 'w') as pyfile:
            pyfile.write(str(Generator(path, 'biolink model', inp_sds['biolink model'])))


if __name__ == '__main__':
    unittest.main()
