import subprocess
import sys
import os
import unittest
# import help_cc_
from test_base import run_unittests
from test_base import captured_io
from io import StringIO


class Test_Project(unittest.TestCase):

    maxDiff = None

    def test_main_file(self):
        import main
        output = main.main()
        self.assertEqual('''List of available commands\n
--------------------------
USERNAME    : Enter your username
HELP        : Shows information about the available commands
MAKEBOOK    : Makes a booking for a code clinic session
VIEWCAL     : Views calendar and events
LOGOUT      : Logs the user out
INTERFACE   : Access the Interface
CLEAR       : Clears the terminal screen
CANCELBOOK  : Cancels the booking

Topics list commands available:
------------------------------

Recursion               : The repeated application of a recursive procedure or definition.
Unittesting             : Automated code to test software written by other developers
List Comprehensions     : Creating new lists from other iterables
Lambdas                 : an anonymous function is a function that is defined without a name.''', output)

    
    def test_unittest_calendar_exist(self):
        import test_calendar
        self.assertTrue('test_calendar' in sys.modules, "test_calendar file should exist")

    def test_unittest_calendar_succeeds(self):
        test_result = run_unittests("test_calendar")
        self.assertTrue(test_result.wasSuccessful(), "Unit Tests must pass")


    def test_unittest_double_book_exist(self):
        import test_double_booking
        self.assertTrue('test_double_booking' in sys.modules, "test_double_booking file should exist")


    def test_unittest_double_succeeds(self):
        test_result = run_unittests("test_double_booking")
        self.assertTrue(test_result.wasSuccessful(), "Unit Tests must pass")


    def test_unittest_inputs_exist(self):
        import test_inputs
        self.assertTrue('test_inputs' in sys.modules, "test_inputs file should exist")


    def test_unittest_inputs_succeeds(self):
        test_result = run_unittests("test_inputs")
        self.assertTrue(test_result.wasSuccessful(), "Unit Tests must pass")

        
        

if __name__ == "__main__":
    unittest.main()
