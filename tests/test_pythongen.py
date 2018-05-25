import os
import unittest

from metamodel.dc_metamodel import SchemaDefinition
#
from metamodel.metamodelcore import load_schema
from metamodel.pythongen import Generator


class PythonGenTestCase(unittest.TestCase):
    def test_metamodel(self):
        cwd = os.path.abspath(os.path.dirname(__file__))
        path = os.path.abspath(os.path.join(cwd, '..', 'meta.yaml'))

        inp_sds = load_schema(path, SchemaDefinition)
        with open(os.path.join(cwd, 'output.py'), 'w') as pyfile:
            pyfile.write(str(Generator(path, 'metamodel', inp_sds['metamodel'])))

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
