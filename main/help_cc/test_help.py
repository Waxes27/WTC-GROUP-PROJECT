import unittest
import sys
import help_cc
from io import StringIO
from contextlib import contextmanager
# from help_cc import do_help
# import test_base


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
            help_cc.run_main()
            # help_cc.run_main()
            self.maxDiff=None

        output = out.getvalue().strip()

        self.assertEqual("""How can I assist?, please type help for assistance: List of available commands:
--------------------------
HELP     : Shows information about the commands
MKBOOK   : Views and books an availble time slot
VWBOOK   : Views bookings
CLBOOK   : Cancels booking
MKSLOT   : Creates a time slot
VWSLOT   : Displays all avalible time slots
CLSLOT   : Cancels a time slot
LOGOUT   : Logs the user out""", output)


if __name__ == "__main__":
    unittest.main()
