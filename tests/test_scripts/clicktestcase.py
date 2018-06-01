import os
import unittest
from contextlib import redirect_stdout
from io import StringIO
from typing import Union, List, Optional

# Make sure you import click from here rather than the root
import click

# Stop click from doing a sys.exit
class CLIExitException(Exception):
    ...

def no_click_exit(self, code=0):
    raise CLIExitException()

click.core.Context.exit = no_click_exit


class ClickTestCase(unittest.TestCase):
    testdir: str = None
    click_ep = None
    prog_name = None
    test_base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'output'))
    metamodel_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'meta.yaml'))
    biolink_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'biolink-model.yaml'))

    @classmethod
    def setUpClass(cls):
        cls.testdir_path = os.path.join(cls.test_base_dir, cls.testdir)
        os.makedirs(cls.testdir_path, exist_ok=True)

    def do_test(self, args: Union[str, List[str]], testfile: Optional[str]="",
                update_test_file: bool=False, error: type(Exception)=None) -> None:
        testfile_path = os.path.join(self.testdir_path, testfile)

        outf = StringIO()
        arg_list = args.split() if isinstance(args, str) else args
        if error:
            with self.assertRaises(error):
                self.click_ep(arg_list, standalone_mode=False)
            return

        with redirect_stdout(outf):
            try:
                self.click_ep(arg_list, prog_name=self.prog_name, standalone_mode=False)
            except CLIExitException:
                pass

        if testfile and update_test_file:
            with open(testfile_path, 'w') as f:
                f.write(outf.getvalue())

        if testfile:
            with open(testfile_path) as f:
                self.assertEqual(outf.getvalue().replace('\r\n', '\n'), f.read().replace('\r\n', '\n'))
        else:
            print("Directory comparison needs to be added")



if __name__ == '__main__':
    unittest.main()
