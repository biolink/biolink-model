import os
import unittest

import biolinkmodel.datamodel
import metamodel.metamodel
from metamodel.generators.pythongen import PythonGenerator

from tests import refresh_files
from tests.test_scripts.clicktestcase import metadata_filter

# If true, update the output
update_master: bool = False


class PythonGenTestCase(unittest.TestCase):
    def gen_and_comp_python(self, yaml_file: str, python_file: str, master_file: str) -> None:
        """ Generate a new metamodel and verify that it matches what we used to build it """
        cwd = os.path.abspath(os.path.dirname(__file__))
        path = os.path.abspath(os.path.join(cwd, '..', yaml_file))
        targetdir = os.path.join(cwd, 'target')
        os.makedirs(targetdir, exist_ok=True)

        model_out = os.path.join(targetdir, python_file)
        master_file_name = os.path.basename(master_file)
        with open(model_out, 'w') as pyfile:
            pyfile.write(str(PythonGenerator(path).serialize()))

        if update_master or refresh_files:
            with open(os.path.join(cwd, master_file), 'w') as masterf:
                masterf.write(str(PythonGenerator(path).serialize()))
            self.assertFalse(update_master, f"{path}: Master file updated. Set: update_master to False")
            if refresh_files:
                print(f"{path} refreshed")

        with open(model_out) as newf:
            newdat = metadata_filter(newf.read())
            with open(master_file) as oldf:
                olddat = metadata_filter(oldf.read())
                self.maxDiff = None
                self.assertEqual(olddat, newdat, f'{master_file_name} does not match output -- should it be updated?')

    def test_metamodel(self):
        python_metamodel_path = os.path.abspath(metamodel.metamodel.__file__)
        self.gen_and_comp_python('meta.yaml', 'metamodel.py', python_metamodel_path)

    def test_biolinkmodel(self):
        python_biolinkmodel_path = os.path.abspath(biolinkmodel.datamodel.__file__)
        self.gen_and_comp_python('biolink-model.yaml', 'biolinkmodel.py', python_biolinkmodel_path)


if __name__ == '__main__':
    unittest.main()
