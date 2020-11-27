from __future__ import print_function
import datetime
import datefinder
import pickle
import os.path
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from pprint import pprint
# from code import input_cc_
# import code.input_cc_.input_API as input_API

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

list_ = ["apillay", "bidaniel", "cdu-pree", "fmokoena", "mbjali", "ndumasi", "sigamede","nwalter", "Sigamede", "tmoshole", "vpekane", "Vsithole", "sbaloyi"]
topic_list = ["Recursion", "Unit Testing", "List Comprehensions", "Lambdas", ""]


def is_slot_avalaible(service, year, month, day, time):

    # now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    # events_result = service.events().list(calendarId='primary', timeMin=now,
    #                                     maxResults=100, singleEvents=True,
    #                                     orderBy='startTime').execute()
    # events = events_result.get('items', [])
    events = [{'attendees': [{'email': 'mbjali@student.wethinkcode.co.za',
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
    [{'attendees': [{'email': 'mbjali@student.wethinkcode.co.za',
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

    if not events:
        return True

    for i in events:           
        full_start_date = i['start'].get('dateTime').split("+")
        start_date_time = full_start_date[0].split("T")
        
        start_year = start_date_time[0].split('-')[0]
        start_month = start_date_time[0].split('-')[1]
        start_day = start_date_time[0].split('-')[2]
        start_hour = ''.join(start_date_time[1].split('-')).split(':')[0]
        start_minute = ''.join(start_date_time[1].split('-')).split(':')[1]
        start_time = start_hour + ':' + start_minute
        

        print('Year', start_year, year)
        print('Month', start_month, month)
        print('Day', start_day, day)
        print('Time', start_time, time)
        print()


        

        if start_year == year and start_month == month and start_day == day and \
            start_time == time:
            return False
    return True       



def create_doctor_event(start, summary, pat_email,duration=1):
    string_date_list = list(datefinder.find_dates(start))
    if len(string_date_list):
        start = string_date_list[0]
        end_time = start + datetime.timedelta(hours=duration)
    event = {
        'summary': summary, 
        
        'start': {
            'dateTime': start.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Africa/Johannesburg',
        },        
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Africa/Johannesburg',
        },
        'attendees': [
            {'email': pat_email},
        ]
    }
    result = service.events().insert(calendarId='primary', body=event).execute()
    print("Event created:", result.get("summary"))
    


def main():
    # username = input_API.book_doctor(list_)
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    global service

    creds = None
    username = input_API.book_doctor(list_)

    topic = input_API.book_topic(topic_list)

    if os.path.exists(f'.tokens/{username}.pickle'):
        with open(f'.tokens/{username}.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(f"{os.environ['HOME']}/.config/.clinic/credentials.json"
            , SCOPES)
            creds = flow.run_local_server(port=0)
        # with open(username  + ".pickle", "wb") as token:
        with open(f"{os.environ['HOME']}/.config/.clinic/.tokens/{username}.pickle",'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)    
    year = input("slot year: ")
    month = input("slot month: ")
    day = input("slot day: ")
    time = input("slot time: ")
    slot_time = f'{year} {month} {day} {time}'
    
    slot_duration = int(input("Enter slot duration: "))
    pat_email = input_API.book_patient(list_)




    if is_slot_avalaible(service, year, month, day, time) == True:
        print('Double booking')
    else: create_doctor_event(slot_time, topic, pat_email)



if __name__ == '__main__':
    #2020-11-27T14:30:00+02:00
    x = is_slot_avalaible([], '2020', '11', '27', '14:30')
    print(x)