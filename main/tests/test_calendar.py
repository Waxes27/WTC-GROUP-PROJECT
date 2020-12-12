import unittest
from unittest.mock import patch
import sys
import os
from io import StringIO
import datetime
# from WTC-GROUP-PROJECT import main.view_calendar.view_calendar as calendar
# from main import view_calendar as calendar
from view_calendar_cc import view_calendar as view_calendar
# print(view_calendar.s)


class Test(unittest.TestCase):


    def test_calendar(self):
        with patch('sys.stdout', new=StringIO()) as out:
            view_calendar

        output = out.getvalue()
        if os.path.exists('token.pickle'):
            self.assertEqual(f"""Getting available slots...

Calendar for the next 7 days:
Available slots :


Date: {view_calendar.s[0][0:10]}
Time       Topic      Doctor     Patient   
................................................................................
05:30       sa       mbjali      ndumasi   
""",output)


if __name__ == "__main__":
    unittest.main()