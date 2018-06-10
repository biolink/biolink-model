import os
import re
import sys
import unittest
from contextlib import redirect_stdout
from io import StringIO
from typing import Union, List, Optional, Callable

# Make sure you import click from here rather than the root
import click


# Stop click from doing a sys.exit
from tests import refresh_files


class CLIExitException(Exception):
    ...


def no_click_exit(self, code=0):
    raise CLIExitException()


click.core.Context.exit = no_click_exit


def metadata_filter(s: str) -> str:
    return re.sub(r'Auto generated from.* ', '', re.sub(r'# Generation date: .*\n', '', s, re.MULTILINE), re.MULTILINE)


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
                update_test_file: bool=False, error: type(Exception)=None,
                filtr: Optional[Callable[[str], str]]=None) -> None:
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

        if testfile and (update_test_file or refresh_files):
            with open(testfile_path, 'w') as f:
                f.write(outf.getvalue())
            if refresh_files:
                print(f'{testfile_path} updated')

        if testfile:
            with open(testfile_path) as f:
                old_txt = outf.getvalue().replace('\r\n', '\n')
                if filtr:
                    old_txt = filtr(old_txt)
                new_txt = f.read().replace('\r\n', '\n')
                if filtr:
                    new_txt = filtr(new_txt)
                self.assertEqual(old_txt.strip(), new_txt.strip())
        else:
            print("Directory comparison needs to be added", file=sys.stderr)

    @staticmethod
    def clear_dir(dir: str) -> None:
        import os, shutil
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                # elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)

if __name__ == '__main__':
    unittest.main()
