import unittest
import sys
# import help_cc_.help_cc
# from help_cc_.help_cc import run_main
import help_cc_
from io import StringIO
from contextlib import contextmanager
# from help_cc import do_help
# import test_base

# help_cc.run_main()
@contextmanager
def captured_io(stdin):
    """Capture standard input and output, as well as standard error, and make that available for testing"""
    new_out, new_err, new_input = StringIO(), StringIO(), stdin
    old_out, old_err, old_input = sys.stdout, sys.stderr, sys.stdin
    try:
        sys.stdout, sys.stderr, sys.stdin = new_out, new_err, new_input
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr, sys.stdin = old_out, old_err, old_input


class MyTestCase(unittest.TestCase):
    def test_do_help_command(self):

        with test_base.captured_io(StringIO("help\n")) as (out, err):
            help_cc.do_help()

        output = out.getvalue().strip()

        self.assertEqual(help_cc.do_help(), """How can I assist?, please type help for assistance: List of available commands:

        with captured_io(StringIO("help\nlogout\n")) as (out, err):
            # print(help_cc)
            help_cc_.help_cc.run_main()
            self.maxDiff=None

        output = out.getvalue().strip()

        self.assertEqual("""How can I assist?, please type help for assistance: List of available commands:



vcal    : View calendar
mkslot  : Make a time slot
vtslot  : View a time slot
ctslot  : Cancel a time slot
logout  : Logging out
How can I assist?, Please type help for assistance:

Logging off...""", output)



if __name__ == "__main__":
    unittest.main()
