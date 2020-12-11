import unittest
import sys
from unittest.mock import patch
from io import StringIO
import book_slot


class testing_inputs(unittest.TestCase):

    def test_slot_not_available(self):

        service = ?
        results = book_slot.is_slot_avalaible(service, 2020, 12, 11, 12:00)
        self.assertEqual(False,results)
        
    
    def test_slot_not_available(self):

        with patch('sys.stdout', new = StringIO()) as fakeout:
        service = ?
        book_slot.is_slot_avalaible(service, 2020, 12, 11, 12:00)
        self.assertEqual(fakeout.getvalue(),'Double booking')


    def test_is_slot_available_year(self):

        service = ?
        results = book_slot.is_slot_avalaible(service, 2021, 10, 11, 12:00)
        self.assertEqual(True,results)


    def test_is_slot_available_month(self):

        service = ?
        results = book_slot.is_slot_avalaible(service, 2020, 12, 11, 12:00)
        self.assertEqual(True,results)

    
    def test_is_slot_available_day(self):

        service = ?
        results = book_slot.is_slot_avalaible(service, 2020, 12, 19, 12:00)
        self.assertEqual(True,results)


    def test_is_slot_available_time(self):

        service = ?
        results = book_slot.is_slot_avalaible(service, 2020, 12, 11, 14:00)
        self.assertEqual(True,results)


