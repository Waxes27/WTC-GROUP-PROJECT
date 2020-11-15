import unittest
import input_cc as input_cc
from unittest.mock import patch
from io import StringIO
# from tests.test_base import captured_io
from contextlib import contextmanager

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

    
class testing_inputs(unittest.TestCase):
  
    @patch("sys.stdin", StringIO("List Comprehension\nList Comprehension\n"))
    def test_topic_input_string(self):

        """
        Test the input is equal to the output. 
        -The user enters a topic from a list of topics and the function returns the topic.
        """
        topic_name = input_cc.book_topic()
        
        self.assertEqual(topic_name,"List Comprehension") 


    @patch("sys.stdin", StringIO("LIST COMprehension\nLIST COMprehension\n"))
    def test_topic_input_string_upper(self):
        """
        Test that the functions returns a topic from the list 
        even when user entered upper cases when selecting a topic.
        """

        topic_name = input_cc.book_topic()
        
        self.assertEqual(topic_name,"List Comprehension") 


    @patch("sys.stdin", StringIO("List Comprehension\nList Comprehension\n"))
    def test_topic_input_string_datatype(self):
        """
        Test that the input is a string and outputs a string.
        """

        topic_name = input_cc.book_topic()

        self.assertEqual(type(topic_name), str)


    def test_topic_input_empty_string(self):
        """
        Test that when the user returns an empty string it should return:
        -Field cannot be blank.\nPlease provide a topic you would like to clinic.\n
        """
        with captured_io(StringIO('\n')) as (out, err):

            topic_name = input_cc.book_topic()

        output = out.getvalue().strip()

        self.assertEqual("""Field cannot be blank.\nPlease provide a topic you would like to clinic.\n""", output)


    @patch("sys.stdin", StringIO("fmokoena\nfmokoena\n"))
    def test_doctor_input(self):
        """
        Test that when the doctor enters a user name, it returns their email address.
        input:fmokoena
        output:fmokoena@student.wethinkcode.co.za
        """
        doctor_name = input_cc.book_doctor() 

        self.assertEqual(doctor_name,"fmokoena@student.wethinkcode.co.za")


    @patch("sys.stdin", StringIO("fMokoena\nFMokoena\n"))
    def test_doctor_input_upper_string(self):
        """
        Test that when the doctor enters a username in upper cases,
        it returns their email address.
        -input:fmokoena
        -output:fmokoena@student.wethinkcode.co.za
        """

        doctor_name = input_cc.book_doctor() 

        self.assertEqual(doctor_name,"fmokoena@student.wethinkcode.co.za")


    def test_doctor_input_empty_string(self):
        """
        Test that when the user returns an empty string it should return:
        -Please provide a valid username.\n
        """
        with captured_io(StringIO('\n')) as (out, err):

            topic_name = input_cc.book_doctor()

        output = out.getvalue().strip()

        self.assertEqual("""Please provide a valid username.\n""", output)


    def test_doctor_input_invalid_username(self):
        """
        Test that if a user enters an invalid user name, the function returns:
        -Username Invalid, please enter a valid username.\n
        """
        with captured_io(StringIO('5685674\n')) as (out, err):

            topic_name = input_cc.book_doctor()

        output = out.getvalue().strip()

        self.assertEqual("""Username Invalid, please enter a valid username.\n""", output)


    @patch("sys.stdin", StringIO("tmoshole\ntmoshole\n"))
    def test_patient_input(self):
        """
        Test that when the patient enters a user name, it returns their email address.
        input:tmoshole
        output:fmokoena@student.wethinkcode.co.za
        """
        patient_name = input_cc.book_patient()

        self.assertEqual(patient_name,"tmoshole@student.wethinkcode.co.za")


    @patch("sys.stdin", StringIO("Tmoshole\nTMoshole\n"))
    def test_patient_input_upper_string (self):
        """
        Test that when the patient enters a username in upper cases,
        it returns their email address.
        -input:fmokoena
        -output:fmokoena@student.wethinkcode.co.za
        """

        patient_name = input_cc.book_patient()

        self.assertEqual(patient_name,"tmoshole@student.wethinkcode.co.za")


    def test_patient_input_empty_string(self):
        """
        Test that when the user returns an empty string it should return:
        -Please provide a valid username.\n
        """

        with captured_io(StringIO('\n')) as (out, err):

            topic_name = input_cc.book_patient()

        output = out.getvalue().strip()

        self.assertEqual("""Please provide a valid username.\n""", output)


    def test_patient_input_invalid_username(self):
        """
        Test that if a user enters an invalid user name, the function returns:
        -Username Invalid, please enter a valid username.\n
        """

        with captured_io(StringIO('5685test74\n')) as (out, err):

            topic_name = input_cc.book_patient()

        output = out.getvalue().strip()

        self.assertEqual("""Username Invalid, please enter a valid username.\n""", output)

if __name__ == "__main__":
    unittest.main()