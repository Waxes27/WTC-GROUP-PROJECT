from __future__ import print_function
import datetime
import datefinder
import pickle
import os.path
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


def find_event(service, calid):
    """
    finds the event a patient is searching for by the doctor's username
    returns: returns details of the event if it is available
    """
    doctor = input("Enter your doctor's username: ") + "@student.wethinkcode.co.za"
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId=calid, timeMin=now,
                                        maxResults=100, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    for i in range(len(events)):
        # print(events[i])
        if events[i]['creator']['email'] == doctor:
            if "Available" in events[i]['summary']:
                print("\nDoctor is available for booking:\n")
                print("Time: "+events[i]['start']['dateTime'][:10] + " " + events[i]['start']['dateTime'][11:16] +'\n')
                print(f"{events[i]['description']}\n")
                continue
        elif events[i]['creator']['email'] == doctor:
            if "Fully" in events[i]['summary']:
                print("Doctor is fully booked")
                continue
        return doctor
    return None


def event(service, calid,username, slot_topic, start_time, end_time, doctor, room):
    """
    updates the event that the user wants to attend
    """
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId=calid, timeMin=now,
                                        maxResults=100, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    for i in range(len(events)):
        if 'Available' in events[i]['summary']:
            if events[i]['creator']['email'] == doctor:
                try:
                    if len((events[i]['attendees'])) == 2:
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
                            'location' :  room,
                            'description' : f'Topic: {slot_topic}',
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
                            'location' :  room,
                            'description' : f'Topic: {slot_topic}',
                        }
                        return event

                except KeyError as e:
                    event = {
                            'summary': f'Available for booking(1/2) ({slot_topic})',
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
                            ],
                            'location' :  room,
                            'description' : f'Topic: {slot_topic}',
                    }
                    return event