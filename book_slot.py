from __future__ import print_function
import datetime
import datefinder
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from pprint import pprint

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def get_events():
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    event1 = []

    if not events:
        print('No upcoming events found.')
    else:
        print(events[1]["summary"])
        for item in events:
            event1.append(item)
            #pprint(event1[0])
    #return event1

def create_patient_event(start, summary, description = None, duration=1):
    string_date_list = list(datefinder.find_dates(start))
    if len(string_date_list):
        start = string_date_list[0]
        end_time = start + datetime.timedelta(hours=duration)
    event = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Africa/Johannesburg',
        },
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Africa/Johannesburg',
        }
    }
    result = service.events().insert(calendarId='primary', body=event).execute()
    print("Event created:", result.get("summary"))


def create_doctor_event():
    string_date_list = list(datefinder.find_dates(start))
    if len(string_date_list):
        start = string_date_list[0]
        end_time = start + datetime.timedelta(hours=duration)
    event = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Africa/Johannesburg',
        },
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Africa/Johannesburg',
        }
    }
    result = service.events().insert(calendarId='primary', body=event).execute()
    print("Event created:", result.get("summary"))


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    global service

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)


    service = build('calendar', 'v3', credentials=creds)

    #get_events()

    # now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    # print('Getting the upcoming 10 events')
    # events_result = service.events().list(calendarId='primary', timeMin=now,
    #                                     maxResults=10, singleEvents=True,
    #                                     orderBy='startTime').execute()
    # events = events_result.get('items', [])

    # event_id = ''

    # events1 = []

    # if not events:
    #     print('No upcoming events found.')
    # else:
    #     for item in events:
    #         pprint(item)
    #         event_id = item['id']
    #         #print(f"{item['summary']}")
    #     print(event_id)

    # print("Valid commands:\nbook slot\nexit")

    input1 = input("What would you like to do: ")
    if input1 == "exit":
        return False
    elif input1 == "book slot":
        input2 = input("doc or pat: ")
        if input2 == "pat":
            slot_time = input("Enter slot date: ")
            slot_duraion = int(input("Enter slot duration: "))
            title = input("Enter topic: ")
            description = input("Enter slot description(else hit 'enter'): ")

            create_patient_event(slot_time, title, description, slot_duraion)
        elif input2 == "doc":
            title = input("Enter topic: ")
            slot_time = input("What date are you avail. on(pls include start time): ")
            description = input("Enter slot description(else hit 'enter'): ")
            slot_duraion = int(input("How long will you be available: "))



if __name__ == '__main__':
    main()