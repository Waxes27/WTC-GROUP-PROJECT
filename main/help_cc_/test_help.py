import unittest
import sys
# import help_cc_.help_cc
# from help_cc_.help_cc import run_main
help_cc = __import__('help_cc')
# import help_cc
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
        with captured_io(StringIO("help\nlogout\n")) as (out, err):
            # print(help_cc)
            help_cc.run_main()
            self.maxDiff=None

        output = out.getvalue().strip()

        self.assertEqual("""List of available commands
--------------------------
USERNAME    : Enter in your username
HELP        : Shows information about the available commands
MAKEBOOK    : Views and books an availble time slot
VIEWBOOK    : Views bookings
CANCELBOOK  : Cancels booking
MAKESLOTS   : Creates a time slot
VIEWSLOT    : Displays all available time slots
CANCELSLOTS : cancels a time slot
LOGOUT      : Logs the user out

Topics list commands available:
--------------------

Recursion               : The repeated application of a recursive procedure or definition.
Unittesting             : Automated code to test software written by other developers
List Comprehensions     : Creating new lists from other iterables
Lambdas                 : an anonymous function is a function that is defined without a name.
""", output)



if __name__ == "__main__":
    unittest.main()
