import unittest
import main.input_cc as input_cc
from unittest.mock import patch
from io import StringIO
from tests.test_base import captured_io

class testing_inputs(unittest.TestCase):
  
    @patch("sys.stdin", StringIO("List Comprehension\nList Comprehension\n"))
    def test_topic_input_string(self):

        topic_name = input_cc.book_topic()
        
        self.assertEqual(topic_name,"List Comprehension") 


    @patch("sys.stdin", StringIO("LIST COMprehension\nLIST COMprehension\n"))
    def test_topic_input_string_upper(self):

        topic_name = input_cc.book_topic()
        
        self.assertEqual(topic_name,"List Comprehension") 


    @patch("sys.stdin", StringIO("List Comprehension\nList Comprehension\n"))
    def test_topic_input_string_datatype(self):

        topic_name = input_cc.book_topic()

        self.assertEqual(type(topic_name), str)


    def test_topic_input_empty_string(self):
        with captured_io(StringIO('\n')) as (out, err):

            topic_name = input_cc.book_topic()

        output = out.getvalue().strip()

        self.assertEqual("""Field cannot be blank.\nPlease provide a topic you would like to clinic.\n""", output)


    @patch("sys.stdin", StringIO("fmokoena\nfmokoena\n"))
    def test_doctor_input(self):

        doctor_name = input_cc.book_doctor() 

        self.assertEqual(doctor_name,"fmokoena@student.wethinkcode.co.za")


    @patch("sys.stdin", StringIO("fMokoena\nFMokoena\n"))
    def test_doctor_input_upper_string(self):

        doctor_name = input_cc.book_doctor() 

        self.assertEqual(doctor_name,"fmokoena@student.wethinkcode.co.za")


    def test_doctor_input_empty_string(self):
        with captured_io(StringIO('\n')) as (out, err):

            topic_name = input_cc.book_doctor()

        output = out.getvalue().strip()

        self.assertEqual("""Please provide a valid username.\n""", output)


    def test_doctor_input_invalid_username(self):
        with captured_io(StringIO('5685674\n')) as (out, err):

            topic_name = input_cc.book_doctor()

        output = out.getvalue().strip()

        self.assertEqual("""Username Invalid, please enter a valid username.\n""", output)


    @patch("sys.stdin", StringIO("tmoshole\ntmoshole\n"))
    def test_patient_input(self):

        patient_name = input_cc.book_patient()

        self.assertEqual(patient_name,"tmoshole@student.wethinkcode.co.za")


    @patch("sys.stdin", StringIO("Tmoshole\nTMoshole\n"))
    def test_patient_input_upper_string (self):

        patient_name = input_cc.book_patient()

        self.assertEqual(patient_name,"tmoshole@student.wethinkcode.co.za")


    def test_patient_input_empty_string(self):
        with captured_io(StringIO('\n')) as (out, err):

            topic_name = input_cc.book_patient()

        output = out.getvalue().strip()

        self.assertEqual("""Please provide a valid username.\n""", output)


    def test_patient_input_invalid_username(self):
        with captured_io(StringIO('5685test74\n')) as (out, err):

            topic_name = input_cc.book_patient()

        output = out.getvalue().strip()

        self.assertEqual("""Username Invalid, please enter a valid username.\n""", output)