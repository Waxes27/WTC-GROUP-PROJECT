import unittest
import sys
from unittest.mock import patch
from io import StringIO
import book_slot


class testing_inputs(unittest.TestCase):    
    
    def test_slot_not_available(self):

        service = ["id: 7lh0290kn852tu3u90q48dmr1s\ndate: 2020-12-11\nstart_time: 11:30\
        \nend_time: 12:30\ntopic: Docstrings\ndoctor: fmokoena\npatient: Available"]
        results = book_slot.is_slot_avalaible(service, "2020", "12", "11","11:30")
        self.assertEqual(False,results)    
        
        
    def test_slot_not_available_(self): 

        with patch('sys.stdout', new = StringIO()) as fakeout:            
            service = ["id: 7lh0290kn852tu3u90q48dmr1s\ndate: 2020-12-11\nstart_time: 11:30\
            \nend_time: 12:30\ntopic: Docstrings\ndoctor: fmokoena\npatient: Available"]
            book_slot.is_slot_avalaible(service, "2020", "12", "11", "11:30")
        self.assertEqual(fakeout.getvalue(),'Double booking')    
        
        
    def test_is_slot_available_year(self):        
        service = ["id: 7lh0290kn852tu3u90q48dmr1s\ndate: 2020-12-11\nstart_time: 11:30\
        \nend_time: 12:30\ntopic: Docstrings\ndoctor: fmokoena\npatient: Available"]
        results = book_slot.is_slot_avalaible(service, "2021", "10", "11", "11:30")
        self.assertEqual(True,results)  
        
    def test_is_slot_available_month(self):        
        
        service = ["id: 7lh0290kn852tu3u90q48dmr1s\ndate: 2020-12-11\nstart_time: 11:30\
                \nend_time: 12:30\ntopic: Docstrings\ndoctor: fmokoena\npatient: Available"]
        results = book_slot.is_slot_avalaible(service, "2020", "12", "11", "11:30")
        self.assertEqual(True,results)    
    def test_is_slot_available_day(self):        
        service = ["id: 7lh0290kn852tu3u90q48dmr1s\ndate: 2020-12-11\nstart_time: 11:30\
        \nend_time: 12:30\ntopic: Docstrings\ndoctor: fmokoena\npatient: Available"]
        results = book_slot.is_slot_avalaible(service, "2020", "12", "19", "11:30")
        self.assertEqual(True,results)    
        
    
    def test_is_slot_available_time(self):        
        service = ["id: 7lh0290kn852tu3u90q48dmr1s\ndate: 2020-12-11\nstart_time: 11:30\
        \nend_time: 12:30\ntopic: Docstrings\ndoctor: fmokoena\npatient: Available"]
        results = book_slot.is_slot_avalaible(service, "2020", "12", "11", "14:00")
        self.assertEqual(True,results)
        
        
if __name__ == "__main__":
    unittest.main()