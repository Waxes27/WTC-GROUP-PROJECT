import subprocess
import sys
import os
import unittest
import help_cc_


class Test_Project(unittest.TestCase):
    def test_help(self):
        value = subprocess.getoutput('python3 -m unittest help_cc/test_help.py')
        print(value)
        # self.assertNotIn('FAILED',value,msg='some tests failed')
        

if __name__ == "__main__":
    unittest.main()