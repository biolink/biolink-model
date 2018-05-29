import os
import re
import unittest

import metamodel.metamodel

from metamodel.schemaloader import SchemaLoader
from metamodel.pythongen import Generator

import biolinkmodel.datamodel


# If true, update the output
update_master: bool = False


class PythonGenTestCase(unittest.TestCase):
    def gen_and_comp_python(self, yaml_file: str, schema_name: str, python_file: str, master_file: str) -> None:
        """ Generate a new metamodel and verify that it matches what we used to build it """
        cwd = os.path.abspath(os.path.dirname(__file__))
        path = os.path.abspath(os.path.join(cwd, '..', yaml_file))
        targetdir = os.path.join(cwd, 'target')
        os.makedirs(targetdir, exist_ok=True)

        inp_schema = SchemaLoader(path).resolve()
        model_out = os.path.join(targetdir, python_file)
        master_file_name = os.path.basename(master_file)
        with open(model_out, 'w') as pyfile:
            pyfile.write(str(Generator(path, schema_name, inp_schema)))

        if update_master:
            with open(os.path.join(cwd, master_file), 'w') as masterf:
                masterf.write(str(Generator(path, schema_name, inp_schema)))
            self.assertFalse(True, f"{path}: Master file updated. Set: update_master to False")

        with open(model_out) as newf:
            newdat = re.sub(r'# Generation date: .*\n', '', newf.read(), re.MULTILINE)
            with open(master_file) as oldf:
                olddat = re.sub(r'# Generation date: .*\n', '', oldf.read(), re.MULTILINE)
                self.assertEqual(olddat, newdat, f'{master_file_name} does not match output -- should it be updated?')

    def test_metamodel(self):
        python_metamodel_path = os.path.abspath(metamodel.metamodel.__file__)
        self.gen_and_comp_python('meta.yaml', 'metamodel', 'metamodel.py', python_metamodel_path)

    def test_biolinkmodel(self):
        python_biolinkmodel_path = os.path.abspath(biolinkmodel.datamodel.__file__)
        self.gen_and_comp_python('biolink-model.yaml', 'biolink model', 'biolinkmodel.py', python_biolinkmodel_path)


if __name__ == '__main__':
    unittest.main()
