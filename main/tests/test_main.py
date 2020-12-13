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
