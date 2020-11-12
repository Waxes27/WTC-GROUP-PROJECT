<<<<<<< HEAD
import help_cc.test_base as test_base
import help_cc.test_help

test_base.run_unittests('test_main')
=======
import subprocess
import sys
import os
import unittest


class Test_Project(unittest.TestCase):
    def test_help(self):
        value = subprocess.getoutput('python3 -m unittest help_cc/test_help.py')
        print(value)
        # self.assertNotIn('FAILED',value,msg='some tests failed')
        

if __name__ == "__main__":
    unittest.main()
>>>>>>> Playground
