import unittest
import sys
from unittest.mock import patch
from io import StringIO
import book_slot
import os

class testing_inputs(unittest.TestCase):
    
    def  test_doctor_event(self):
        with patch('sys.stdout', new=StringIO("d\n' '\n15:00\n11\n6\n")) as out:
            creds = book_slot.validate_token()
            service = book_slot.create_service(creds)
            calid = 'g67ktgipc1jjcg9tkqdtol6r54@group.calendar.google.com'

            book_slot.create_doctor_event(service,calid)
            output = out.getvalue()
            self.assertEqual("""[datetime.datetime(2020, 11, 6, 15, 0)]
Available for booking""",output)


    def test_double_booking(self):
        with patch('sys.stdout', new=StringIO()) as out:
            creds = book_slot.validate_token()
            service = book_slot.create_service(creds)
            calid = 'g67ktgipc1jjcg9tkqdtol6r54@group.calendar.google.com'
            slot_time = '2020 12 15 13:30'

            results = book_slot.is_slot_avalaible(calid,service,slot_time)

            self.assertEqual(False, results)
       
    
    def test_is_slot_available(self):
        creds = book_slot.validate_token()
        service = book_slot.create_service(creds)
        calid = 'g67ktgipc1jjcg9tkqdtol6r54@group.calendar.google.com'
        slot_time = '2020 12 15 13:30'
         
        results = book_slot.is_slot_avalaible(calid,service,slot_time)

        self.assertEqual(True, results)


if __name__ == "__main__":
    unittest.main()

