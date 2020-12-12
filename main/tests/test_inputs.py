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
        with captured_io(StringIO("List Comprehension\ncdu-pree\nbidaniel\n")) as (out, err):
            apiinput.book_topic()
        output = out.getvalue().strip()
        
        self.assertEqual('''Coding Clinic Topics:\n
        Recursion\n
        Unittesting\n
        List Comprehensions\n
        Lambdas\nPlease choose a topic you would like to clinic? Or leave blank to choose a 'General' topic\n
        Please provide the name of the Coding Clinician.\n
        Please provide the name of the Coding Patient.\n''', output)


    def test_topic_input_string_upper(self):
        with captured_io(StringIO("LIST COMprehension\ncdu-pree\nbidaniel\n")) as (out, err):
            apiinput.book_topic()
        output = out.getvalue().strip()

        self.assertEqual('''Coding Clinic Topics:\n
        Recursion\n
        Unittesting\n
        List Comprehensions\n
        Lambdas\nPlease choose a topic you would like to clinic? Or leave blank to choose a 'General' topic\n
        Please provide the name of the Coding Clinician.\n
        Please provide the name of the Coding Patient.\n''', output) 


    @patch("sys.stdin", StringIO("List Comprehension\ncdu-pree\nbidaniel\n"))
    def test_topic_input_string_datatype(self):
        topic_name = apiinput.book_topic()

        self.assertEqual(type(topic_name), str)


    def test_topic_input_empty_string(self):
        with captured_io(StringIO('\ncdu-pree\nbidaniel\n")')) as (out, err):
            apiinput.book_topic()
        output = out.getvalue().strip()

        self.assertEqual('''Coding Clinic Topics:\n
        Recursion\n
        Unittesting\n
        List Comprehensions\n
        Lambdas\nPlease choose a topic you would like to clinic? Or leave blank to choose a 'General' topic\n
        You have chosen a General topic\n
        Please provide the name of the Coding Clinician.\n
        Please provide the name of the Coding Patient.\n''', output)


    def test_doctor_input(self):
        with captured_io(StringIO('fmokoena\n')) as (out, err):
            apiinput.book_doctor() 
        output = out.getvalue().strip()

        self.assertEqual("Please provide the name of the Coding Clinician.\n", output)


    def test_doctor_input_upper_string(self):
        with captured_io(StringIO('fMokeona\n')) as (out, err):
            apiinput.book_doctor() 
        output = out.getvalue().strip()

        self.assertEqual("Please provide the name of the Coding Clinician.\n", output)


    def test_doctor_input_empty_string(self):
        with captured_io(StringIO('\n')) as (out, err):
            apiinput.book_doctor()
        output = out.getvalue().strip()

        self.assertEqual("""Please provide the name of the Coding Clinician.\n
    Field cannot be blank, please provide your valid username.\n
    Please provide the name of the Coding Clinician\n""", output)


    def test_doctor_input_invalid_username(self):
        with captured_io(StringIO('5685674\n')) as (out, err):
            apiinput.book_doctor()
        output = out.getvalue().strip()

        self.assertEqual("""Please provide the name of the Coding Clinician.\n
        Username Invalid, please select a valid username.\n
        Please provide the name of the Coding Clinician\n""", output)


    def test_patient_input(self):
        with captured_io(StringIO('tmoshole\n')) as (out, err):
            apiinput.book_patient()
        output = out.getvalue().strip()

        self.assertEqual("Please provide the name of the Coding Patient.\n", output)


    def test_patient_input_upper_string (self):
        with captured_io(StringIO('Tmoshole\n')) as (out, err):
            apiinput.book_patient()
        output = out.getvalue().strip()

        self.assertEqual("Please provide the name of the Coding Patient.\n", output)


    def test_patient_input_empty_string(self):
        with captured_io(StringIO('\n')) as (out, err):
            apiinput.book_patient()
        output = out.getvalue().strip()

        self.assertEqual("""Please provide the name of the Coding Patient.\n
        Username Invalid, please select a valid username.\n
        Please provide the name of the Coding Patient\n""", output)


    def test_patient_input_invalid_username(self):
        with captured_io(StringIO('5685test74\n')) as (out, err):
            apiinput.book_patient()
        output = out.getvalue().strip()

        self.assertEqual("""Please provide the name of the Coding Patient.\n
        Username Invalid, please select a valid username.\n
        Please provide the name of the Coding Patient\n""", output)


if __name__ == "__main__":
    unittest = Testing_Inputs()
    unittest