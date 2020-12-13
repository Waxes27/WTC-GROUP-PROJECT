import unittest
from input_cc_.input_API import API_input
from unittest.mock import patch
from io import StringIO
from contextlib import contextmanager
import sys
from test_base import captured_io
import test_base

apiinput = API_input()


class Testing_Inputs(unittest.TestCase):    
    
    maxDiff = None    
    
    def test_topic_input_string(self):
        with captured_io(StringIO("List Comprehensions\ncdu-pree\nbidaniel\n")) as (out, err):
            apiinput.book_topic()
        output = out.getvalue().strip()        
        
        self.assertEqual('''Coding Clinic Topics:

Recursion
Unittesting 
List Comprehensions
Lambdas
Please choose a topic you would like to clinic? Or leave blank to choose a 'General' topic''', output)    


    def test_topic_input_string_upper(self):
        with captured_io(StringIO("LIST COMprehensionS\ncdu-pree\nbidaniel\n")) as (out, err):
            apiinput.book_topic()
        output = out.getvalue().strip()        
        self.assertEqual('''Coding Clinic Topics:

Recursion
Unittesting 
List Comprehensions
Lambdas
Please choose a topic you would like to clinic? Or leave blank to choose a 'General' topic''', output)     


    @patch("sys.stdin", StringIO("List Comprehensions\ncdu-pree\nbidaniel\n"))
    def test_topic_input_string_datatype(self):
        topic_name = apiinput.book_topic()        
        self.assertEqual(type(topic_name), str)    
        
        
    def test_topic_input_empty_string(self):
        with captured_io(StringIO("\ncdu-pree\nbidaniel\n")) as (out, err):
            apiinput.book_topic()
        output = out.getvalue().strip()        
        self.assertEqual('''Coding Clinic Topics:

Recursion
Unittesting 
List Comprehensions
Lambdas
Please choose a topic you would like to clinic? Or leave blank to choose a 'General' topic
You have chosen a General topic''', output)    


    def test_doctor_input(self):
        with captured_io(StringIO("cdu-pree\n")) as (out, err):
            apiinput.book_doctor() 
        output = out.getvalue()        
        self.assertEqual('Please provide the name of the Coding Clinician.\n', output)    
        
        
    def test_doctor_input_upper_string(self):
        with captured_io(StringIO("Cdu-pree\n")) as (out, err):
            apiinput.book_doctor() 
        output = out.getvalue().strip()        
        self.assertEqual('Please provide the name of the Coding Clinician.', output)    
        
        
    def test_doctor_input_empty_string(self):
        with captured_io(StringIO(" \ncdu-pree\n")) as (out, err):
            apiinput.book_doctor()
        output = out.getvalue().strip()        
        self.assertEqual('''Please provide the name of the Coding Clinician.
Username Invalid, please select a valid username.\n
Please provide the name of the Coding Clinician.''', output)   


    def test_doctor_input_invalid_username(self):
        with captured_io(StringIO("c2552f\ncdu-pree\n")) as (out, err):
            apiinput.book_doctor()
        output = out.getvalue().strip()        
        self.assertEqual('''Please provide the name of the Coding Clinician.
Username Invalid, please select a valid username.\n
Please provide the name of the Coding Clinician.''', output)    


    def test_patient_input(self):
        with captured_io(StringIO("bidaniel\n")) as (out, err):
            apiinput.book_patient()
        output = out.getvalue().strip()        
        self.assertEqual('Please provide the name of the Coding Patient.', output)    
        
        
    def test_patient_input_upper_string (self):
        with captured_io(StringIO("Bidaniel\n")) as (out, err):
            apiinput.book_patient()
        output = out.getvalue()        
        self.assertEqual('Please provide the name of the Coding Patient.\n', output)    
        
        
    def test_patient_input_empty_string(self):
        with captured_io(StringIO(" \nbidaniel\n")) as (out, err):
            apiinput.book_patient()
        output = out.getvalue().strip()        
        self.assertEqual('''Please provide the name of the Coding Patient.
Username Invalid, please select a valid username.\n
Please provide the name of the Coding Patient.''', output)    


    def test_patient_input_invalid_username(self):
        with captured_io(StringIO('5685test74\nbidaniel\n')) as (out, err):
            apiinput.book_patient()
        output = out.getvalue().strip()        
        self.assertEqual('''Please provide the name of the Coding Patient.
Username Invalid, please select a valid username.\n
Please provide the name of the Coding Patient.''', output)


if __name__ == "__main__":
    unittest = Testing_Inputs()
    unittest