import unittest
import sys
import help_cc
from io import StringIO
from test_base import captured_io
from help_cc import do_help


class MyTestCase(unittest.TestCase):
    def test_do_help_command(self):
        with captured_io(StringIO("help\n")) as (out, err):
            help_cc.do_help()

        output = out.getvalue().strip()

        self.assertEqual(help_cc.do_help(), """How can I assist?, please type help for assistance: List of available commands:
--------------------------
HELP       : Shows information about the commands
MAKEBOOK   : Views and books an availble time slot
VIEWBOOK   : Views bookings
CANCELBOOK : Cancels booking
MAKESLOT   : Creates a time slot
VIEWSLOT   : Displays all avalible time slots
CANCELSLOT : Cancels a time slot
LOGOUT     : Logs the user out""", output)


if __name__ == "__main__":
    unittest.main()