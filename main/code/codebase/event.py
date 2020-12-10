from __future__ import print_function
import datetime
import datefinder
import pickle
import os.path
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


def event(service, calid,username, slot_topic, start_time, end_time):
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId=calid, timeMin=now,
                                        maxResults=100, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    username = input('hm: ')
    for i in range(len(events)):
        if 'Available' in events[i]['summary']:
            print(events[i]['creator'])
            try:
                if len((events[i]['attendees'])) == 2:
                    print(events[i]['attendees'])
                    event = {
                        'summary': f'Fully Booked ({slot_topic})',
                        'start': {
                            'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'Africa/Johannesburg',
                        },
                        'end': {
                            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'Africa/Johannesburg',
                        },
                        'attendees': [
                            {'email' : f"{events[i]['attendees'][0]['email']}"},
                            {'email' : f"{events[i]['attendees'][1]['email']}"},
                        ],
                        'location' :  '5th floor',
                        'description' : f'Topic : {slot_topic}',
                    }
                    return event

                if len((events[i]['attendees'])) == 1:
                    event = {
                        'summary': f'Fully Booked ({slot_topic})',
                        'start': {
                            'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'Africa/Johannesburg',
                        },
                        'end': {
                            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'Africa/Johannesburg',
                        },
                        'attendees': [
                            {'email' : f"{events[i]['attendees'][0]['email']}"},
                            {'email' : f"{username}@student.wethinkcode.co.za"},
                        ],
                        'location' :  '5th floor',
                        'description' : f'Topic : {slot_topic}',
                    }
                    return event
            except KeyError:
                # print("No attendees")
                event = {
                        'summary': f'Available for booking(1/2)',
                        #Add description (To include doctor name)
                        'start': {
                            'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'Africa/Johannesburg',
                        },
                        'end': {
                            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'Africa/Johannesburg',
                        },
                        'attendees': [
                            {'email' : f'{username}@student.wethinkcode.co.za'},
                        ]
                }
                return event