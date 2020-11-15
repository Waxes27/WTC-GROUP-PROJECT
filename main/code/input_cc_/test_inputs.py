import unittest
<<<<<<< HEAD:main/input_cc/test_inputs.py
# from . import input_cc
import input_cc
from unittest.mock import patch
from io import StringIO
# from .test_base import captured_io
from test_base import captured_io
=======
import input_cc as input_cc
from unittest.mock import patch
from io import StringIO
# from tests.test_base import captured_io
from .test_base import captured_io
>>>>>>> main:main/code/input_cc_/test_inputs.py

class testing_inputs(unittest.TestCase):
  
    @patch("sys.stdin", StringIO("list comprehension\nlist comprehension\n"))
    def test_topic_input_string(self):

        topic_name = input_cc.book_topic()
        
        self.assertEqual(topic_name,"list comprehension") 
        self.assertEqual(type(topic_name), str)


    @patch("sys.stdin", StringIO("cancel\ncancel\n"))
    def test_topic_input_cancel_output(self):

        topic_name = input_cc.book_topic()

        self.assertEqual(topic_name, 0) 


    def test_topic_input_cancel(self):
        with captured_io(StringIO('cancel\n')) as (out, err):

            topic_name = input_cc.book_topic()

        output = out.getvalue().strip()

        self.assertEqual("""Cancelling clinic\n""", output)


    def test_topic_input_empty_string(self):
        with captured_io(StringIO('\n')) as (out, err):

            topic_name = input_cc.book_topic()

        output = out.getvalue().strip()

        self.assertEqual("""Field cannot be blank.\nPlease provide a topic you would like to clinic.\n""", output)


    @patch("sys.stdin", StringIO("vsithole\nvsithole\n"))
    def test_doctor_input(self):

        doctor_name = input_cc.book_doctor() 

        self.assertEqual(doctor_name,"vsithole@student.wethinkcode.co.za")


    def test_doctor_input_empty_string(self):
        with captured_io(StringIO('\n')) as (out, err):

            topic_name = input_cc.book_doctor()

        output = out.getvalue().strip()

        self.assertEqual("""Field cannot be blank\nPlease provide a topic you would like to clinic\n""", output)


    @patch("sys.stdin", StringIO("tmoshole\ntmoshole\n"))
    def test_patient_input(self):

        patient_name = input_cc.book_patient()

        self.assertEqual(patient_name,"tmoshole@student.wethinkcode.co.za")


if __name__ == "__main__":
    unittest.main()