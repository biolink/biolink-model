import os
import re
import sys
import textwrap
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
    return re.sub(r'(# Auto generated from ).*(\.yaml by pythongen\.py version: ).*', r'\1\2',
                  re.sub(r'(# Generation date: ).*', r'\1', s)).strip()


class ClickTestCase(unittest.TestCase):
    testdir: str = None
    click_ep = None
    prog_name: str = None
    soft_compare: Optional[str] = None
    test_base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'output'))
    metamodel_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'meta.yaml'))
    biolink_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'biolink-model.yaml'))

    @classmethod
    def setUpClass(cls):
        cls.testdir_path = os.path.join(cls.test_base_dir, cls.testdir)
        os.makedirs(cls.testdir_path, exist_ok=True)

    @staticmethod
    def closein_comparison(old_txt: str, new_txt: str) -> None:
        """ Assist with testing comparison -- zero in on the first difference in a big string

        @param old_txt:
        @param new_txt:
        """
        nt = new_txt.strip()
        ot = old_txt.strip()
        if ot != nt:
            while nt and ot and nt[:20] == ot[:20]:
                nt = nt[20:]
                ot = ot[20:]
            print(nt[:80])
            print(ot[:80])

    def do_test(self, args: Union[str, List[str]], testfile: Optional[str]="",
                update_test_file: bool=False, error: type(Exception)=None,
                filtr: Optional[Callable[[str], str]]=None, tox_wrap_fix: bool=False,
                bypass_soft_compare: bool=False) -> None:
        """ Execute a command test

        @param args: Argument string or list to command
        @param testfile: name of file to record output in.  If absent, using directory mode
        @param update_test_file: True means we need to update the test file
        @param error: If present, we expect this error
        @param filtr: Filter to remove date and app specific information from text
        @param tox_wrap_fix: tox seems to wrap redirected output at 60 columns.  If true, try wrapping the test
        file before failing
        @param bypass_soft_compare: True means not to use the class level soft compare
        """
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

        if not testfile:
            print("Directory comparison needs to be added", file=sys.stderr)
        else:
            new_txt = outf.getvalue().replace('\r\n', '\n').strip()
            if filtr:
                new_txt = filtr(new_txt)
            with open(testfile_path) as f:
                old_txt = f.read().replace('\r\n', '\n').strip()
                if filtr:
                    old_txt = filtr(old_txt)
            if old_txt != new_txt and tox_wrap_fix:
                old_txt = textwrap.fill(old_txt, 60)
                new_txt = textwrap.fill(new_txt, 60)
            compare_result = old_txt == new_txt

            # If necessary, update the test file
            if not compare_result:
                if update_test_file or refresh_files:
                    with open(testfile_path, 'w') as f:
                        f.write(outf.getvalue())
                    if refresh_files:
                        print(f'refresh_files is True: {testfile_path} updated')
                else:
                    print(f"{self.id()}: {self.soft_compare}") if self.soft_compare and not bypass_soft_compare\
                        else self.assertEqual(old_txt, new_txt)


    @staticmethod
    def clear_dir(folder: str) -> None:
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
