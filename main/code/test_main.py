import subprocess
import sys
import os
import unittest
# import help_cc_


class Test_Project(unittest.TestCase):
    def test_help(self):
        value = subprocess.getoutput('python3 -m unittest help_cc_/test_help.py')
        self.assertNotIn('FAILED',value,msg='\n\n\n\nTEST_HELP FAILED')
    
    def test_input(self):
        value = subprocess.getoutput('python3 -m unittest input_cc/test_inputs.py')
        self.assertNotIn('FAILED',value,msg='\n\n\n\nTEST_INPUTS FAILED')
    
    def test_view_calendar(self):
        
        

if __name__ == "__main__":
    unittest.main()
