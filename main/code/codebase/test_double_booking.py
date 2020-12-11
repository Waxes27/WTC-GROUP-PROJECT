import unittest
import sys
from unittest.mock import patch
from io import StringIO
import book_slot.is_slot_avalaible



class testing_inputs(unittest.TestCase):

    book_slot.is_slot_avalaible.events = lambda a: [{'attendees': [{'email': 'mbjali@student.wethinkcode.co.za',
                 'organizer': True,
                 'responseStatus': 'accepted',
                 'self': True},
                {'email': 'amoller@student.wethinkcode.co.za',
                 'responseStatus': 'accepted'}],
  'conferenceData': {'conferenceId': 'kwq-prpf-gcv',
                     'conferenceSolution': {'iconUri': 'https://fonts.gstatic.com/s/i/productlogos/meet_2020q4/v6/web-512dp/logo_meet_2020q4_color_2x_web_512dp.png',
                                            'key': {'type': 'hangoutsMeet'},
                                            'name': 'Google Meet'},
                     'entryPoints': [{'entryPointType': 'video',
                                      'label': 'meet.google.com/kwq-prpf-gcv',
                                      'uri': 'https://meet.google.com/kwq-prpf-gcv'},
                                     {'entryPointType': 'more',
                                      'pin': '9847987293601',
                                      'uri': 'https://tel.meet/kwq-prpf-gcv?pin=9847987293601'},
                                     {'entryPointType': 'phone',
                                      'label': '+27 10 823 1060',
                                      'pin': '810827760',
                                      'regionCode': 'ZA',
                                      'uri': 'tel:+27-10-823-1060'}],
                     'signature': 'AGkP/s1HSfUw5mBnaE5LvMNX0R1d'},
  'created': '2020-11-25T08:17:35.000Z',
  'creator': {'email': 'mbjali@student.wethinkcode.co.za', 'self': True},
  'end': {'dateTime': '2020-11-25T14:50:00+02:00'},
  'etag': '"3212585062858000"',
  'hangoutLink': 'https://meet.google.com/kwq-prpf-gcv',
  'htmlLink': 'https://www.google.com/calendar/event?eid=MmgxNXJtczY4Z2lnZzFoaWU0ZmduZGNmYm8gbWJqYWxpQHN0dWRlbnQud2V0aGlua2NvZGUuY28uemE',
  'iCalUID': '2h15rms68gigg1hie4fgndcfbo@google.com',
  'id': '2h15rms68gigg1hie4fgndcfbo',
  'kind': 'calendar#event',
  'organizer': {'email': 'mbjali@student.wethinkcode.co.za', 'self': True},
  'reminders': {'useDefault': True},
  'sequence': 0,
  'start': {'dateTime': '2020-11-25T14:30:00+02:00'},
  'status': 'confirmed',
  'summary': 'mbjali review with amoller',
  'updated': '2020-11-25T08:22:11.429Z'},
 {'attendees': [{'email': 'mbjali@student.wethinkcode.co.za',
                 'responseStatus': 'needsAction',
                 'self': True},
                {'email': 'bidaniel@student.wethinkcode.co.za',
                 'responseStatus': 'needsAction'},
                {'email': 'ndumasi@student.wethinkcode.co.za',
                 'responseStatus': 'needsAction'},
                {'email': 'tmentor@student.wethinkcode.co.za',
                 'responseStatus': 'needsAction'},
                {'email': 'apillay@student.wethinkcode.co.za',
                 'responseStatus': 'needsAction'},
                {'email': 'fmokoena@student.wethinkcode.co.za',
                 'responseStatus': 'accepted'},
                {'email': 'dchappie@student.wethinkcode.co.za',
                 'responseStatus': 'declined'},
                {'email': 'tmoshole@student.wethinkcode.co.za',
                 'responseStatus': 'needsAction'},
                {'email': 'vsithole@student.wethinkcode.co.za',
                 'responseStatus': 'accepted'},
                {'email': 'sigamede@student.wethinkcode.co.za',
                 'responseStatus': 'accepted'},
                {'email': 'cdu-pree@student.wethinkcode.co.za',
                 'responseStatus': 'needsAction'},
                {'email': 'vpekane@student.wethinkcode.co.za',
                 'responseStatus': 'needsAction'},
                {'email': 'sbaloyi@student.wethinkcode.co.za',
                 'responseStatus': 'accepted'},
                {'email': 'nwalter@student.wethinkcode.co.za',
                 'responseStatus': 'accepted'}],
  'conferenceData': {'conferenceId': 'ysk-snxv-arc',
                     'conferenceSolution': {'iconUri': 'https://fonts.gstatic.com/s/i/productlogos/meet_2020q4/v6/web-512dp/logo_meet_2020q4_color_2x_web_512dp.png',
                                            'key': {'type': 'hangoutsMeet'},
                                            'name': 'Google Meet'},
                     'entryPoints': [{'entryPointType': 'video',
                                      'label': 'meet.google.com/ysk-snxv-arc',
                                      'uri': 'https://meet.google.com/ysk-snxv-arc'},
                                     {'entryPointType': 'more',
                                      'pin': '5026304574086',
                                      'uri': 'https://tel.meet/ysk-snxv-arc?pin=5026304574086'},
                                     {'entryPointType': 'phone',
                                      'label': '+27 10 823 0803',
                                      'pin': '740630632',
                                      'regionCode': 'ZA',
                                      'uri': 'tel:+27-10-823-0803'}],
                     'signature': 'AGkP/s2OY9K83t0JvPOu7/CBqtSi'},
  'created': '2020-11-13T09:29:06.000Z',
  'creator': {'email': 'dchappie@student.wethinkcode.co.za'},
  'end': {'dateTime': '2020-11-27T14:45:00+02:00',
          'timeZone': 'Africa/Johannesburg'},
  'etag': '"3210642574604000"',
  'hangoutLink': 'https://meet.google.com/ysk-snxv-arc',
  'htmlLink': 'https://www.google.com/calendar/event?eid=NDM1Mm8yaDFic3IzdmRuNnFxZWZkdnU3OWhfMjAyMDExMjdUMTIzMDAwWiBtYmphbGlAc3R1ZGVudC53ZXRoaW5rY29kZS5jby56YQ',
  'iCalUID': '4352o2h1bsr3vdn6qqefdvu79h@google.com',
  'id': '4352o2h1bsr3vdn6qqefdvu79h_20201127T123000Z',
  'kind': 'calendar#event',
  'organizer': {'displayName': '2020 Group Project Demos',
                'email': 'c_8o0g2bsqbqpmp47ik4slofs3s8@group.calendar.google.com'},
  'originalStartTime': {'dateTime': '2020-11-27T14:30:00+02:00',
                        'timeZone': 'Africa/Johannesburg'},
  'recurringEventId': '4352o2h1bsr3vdn6qqefdvu79h',
  'reminders': {'useDefault': True},
  'sequence': 1,
  'start': {'dateTime': '2020-11-27T14:30:00+02:00',
            'timeZone': 'Africa/Johannesburg'},
  'status': 'confirmed',
  'summary': 'JHB Team 25 && Team 26',
  'updated': '2020-11-14T02:34:47.302Z'},
 {'attendees': [{'email': 'mbjali@student.wethinkcode.co.za',
                 'responseStatus': 'needsAction',
                 'self': True},
                {'email': 'bidaniel@student.wethinkcode.co.za',
                 'responseStatus': 'needsAction'},
                {'email': 'ndumasi@student.wethinkcode.co.za',
                 'responseStatus': 'needsAction'},
                {'email': 'tmentor@student.wethinkcode.co.za',
                 'responseStatus': 'needsAction'},
                {'email': 'apillay@student.wethinkcode.co.za',
                 'responseStatus': 'needsAction'},
                {'email': 'fmokoena@student.wethinkcode.co.za',
                 'responseStatus': 'accepted'},
                {'email': 'dchappie@student.wethinkcode.co.za',
                 'responseStatus': 'declined'},
                {'email': 'tmoshole@student.wethinkcode.co.za',
                 'responseStatus': 'needsAction'},
                {'email': 'vsithole@student.wethinkcode.co.za',
                 'responseStatus': 'accepted'},
                {'email': 'sigamede@student.wethinkcode.co.za',
                 'responseStatus': 'accepted'},
                {'email': 'cdu-pree@student.wethinkcode.co.za',
                 'responseStatus': 'needsAction'},
                {'email': 'vpekane@student.wethinkcode.co.za',
                 'responseStatus': 'needsAction'},
                {'email': 'sbaloyi@student.wethinkcode.co.za',
                 'responseStatus': 'accepted'},
                {'email': 'nwalter@student.wethinkcode.co.za',
                 'responseStatus': 'accepted'}],
  'conferenceData': {'conferenceId': 'ysk-snxv-arc',
                     'conferenceSolution': {'iconUri': 'https://fonts.gstatic.com/s/i/productlogos/meet_2020q4/v6/web-512dp/logo_meet_2020q4_color_2x_web_512dp.png',
                                            'key': {'type': 'hangoutsMeet'},
                                            'name': 'Google Meet'},
                     'entryPoints': [{'entryPointType': 'video',
                                      'label': 'meet.google.com/ysk-snxv-arc',
                                      'uri': 'https://meet.google.com/ysk-snxv-arc'},
                                     {'entryPointType': 'more',
                                      'pin': '5026304574086',
                                      'uri': 'https://tel.meet/ysk-snxv-arc?pin=5026304574086'},
                                     {'entryPointType': 'phone',
                                      'label': '+27 10 823 0803',
                                      'pin': '740630632',
                                      'regionCode': 'ZA',
                                      'uri': 'tel:+27-10-823-0803'}],
                     'signature': 'AGkP/s2OY9K83t0JvPOu7/CBqtSi'},
  'created': '2020-11-13T09:29:06.000Z',
  'creator': {'email': 'dchappie@student.wethinkcode.co.za'},
  'end': {'dateTime': '2020-12-11T14:45:00+02:00',
          'timeZone': 'Africa/Johannesburg'},
  'etag': '"3210642574604000"',
  'hangoutLink': 'https://meet.google.com/ysk-snxv-arc',
  'htmlLink': 'https://www.google.com/calendar/event?eid=NDM1Mm8yaDFic3IzdmRuNnFxZWZkdnU3OWhfMjAyMDEyMTFUMTIzMDAwWiBtYmphbGlAc3R1ZGVudC53ZXRoaW5rY29kZS5jby56YQ',
  'iCalUID': '4352o2h1bsr3vdn6qqefdvu79h@google.com',
  'id': '4352o2h1bsr3vdn6qqefdvu79h_20201211T123000Z',
  'kind': 'calendar#event',
  'organizer': {'displayName': '2020 Group Project Demos',
                'email': 'c_8o0g2bsqbqpmp47ik4slofs3s8@group.calendar.google.com'},
  'originalStartTime': {'dateTime': '2020-12-11T14:30:00+02:00',
                        'timeZone': 'Africa/Johannesburg'},
  'recurringEventId': '4352o2h1bsr3vdn6qqefdvu79h',
  'reminders': {'useDefault': True},
  'sequence': 1,
  'start': {'dateTime': '2020-12-11T14:30:00+02:00',
            'timeZone': 'Africa/Johannesburg'},
  'status': 'confirmed',
  'summary': 'JHB Team 25 && Team 26',
  'updated': '2020-11-14T02:34:47.302Z'}]

    # def test_slot_not_available(self):

    #     service = ["id: 7lh0290kn852tu3u90q48dmr1s\ndate: 2020-12-11\nstart_time: 11:30\
    #         \nend_time: 12:30\ntopic: Docstrings\ndoctor: fmokoena\npatient: Available"]
    #     results = book_slot.is_slot_avalaible(service, "2020", "12", "11","11:30")
    #     self.assertEqual(False,results)
        
    
    # def test_slot_not_available_(self):

    #     with patch('sys.stdout', new = StringIO()) as fakeout:

    #         service = ["id: 7lh0290kn852tu3u90q48dmr1s\ndate: 2020-12-11\nstart_time: 11:30\
    #             \nend_time: 12:30\ntopic: Docstrings\ndoctor: fmokoena\npatient: Available"]
    #         book_slot.is_slot_avalaible(service, "2020", "12", "11", "11:30")
    #     self.assertEqual(fakeout.getvalue(),'Double booking')


    # def test_is_slot_available_year(self):

    #     service = ["id: 7lh0290kn852tu3u90q48dmr1s\ndate: 2020-12-11\nstart_time: 11:30\
    #             \nend_time: 12:30\ntopic: Docstrings\ndoctor: fmokoena\npatient: Available"]
    #     results = book_slot.is_slot_avalaible(service, "2021", "10", "11", "11:30")
    #     self.assertEqual(True,results)


    # def test_is_slot_available_month(self):

    #     service = ["id: 7lh0290kn852tu3u90q48dmr1s\ndate: 2020-12-11\nstart_time: 11:30\
    #             \nend_time: 12:30\ntopic: Docstrings\ndoctor: fmokoena\npatient: Available"]
    #     slot_time = "2020 12 11 11:30"
    #     results = book_slot.is_slot_avalaible(service, slot_time)
    #     self.assertEqual(True,results)





  #list
        #dictionary (with attendes)
    
    def test_is_slot_available_day(self):
        # 2020-11-27T14:30
        slot_time = "2020 11 27 14:30"
        results = book_slot.is_slot_avalaible([], slot_time)
        self.assertEqual(True,results)


    # def test_is_slot_available_time(self):

    #     service = ["id: 7lh0290kn852tu3u90q48dmr1s\ndate: 2020-12-11\nstart_time: 11:30\
    #             \nend_time: 12:30\ntopic: Docstrings\ndoctor: fmokoena\npatient: Available"]
    #     results = book_slot.is_slot_avalaible(service, "2020", "12", "11", "14:00")
    #     self.assertEqual(True,results)


if __name__ == "__main__":
    unittest.main()
