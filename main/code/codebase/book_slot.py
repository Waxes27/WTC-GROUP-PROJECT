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
import code.input_cc_.input_API as input_API
#from . import create_service


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

list_ = ["apillay", "bidaniel", "cdu-pree", "fmokoena", "mbjali", "ndumasi", "sigamede","nwalter", "Sigamede", "tmoshole", "vpekane", "Vsithole", "sbaloyi"]
topic_list = ["Recursion", "Unit Testing", "List Comprehensions", "Lambdas", ""]

service = ''

def create_doctor_event(start, summary, pat_email,service):
    string_date_list = list(datefinder.find_dates(start))
    if len(string_date_list):
        start = string_date_list[0]
        end_time = start + datetime.timedelta(minutes=30)
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


def validate_token():
    # username = input_API.book_doctor(list_)
    if os.path.exists(f"{os.environ['HOME']}/.config/.clinic/username.txt"):
        username_file = open(f"{os.environ['HOME']}/.config/.clinic/username.txt", 'r')
        username = username_file.readline()
        # RUN A LOGIN HERE
    else:
        print("User not found...\n")
        username = input("Username: ")
        # RUN A LOGIN HERE
        username_file = open(f"{os.environ['HOME']}/.config/.clinic/username.txt", 'w+')
        username_file.write(username)

    creds = None

    #topic = input_API.book_topic(topic_list)
    username = f'{username}@student.wethinkcode.co.za'
    if os.path.exists(f"{os.environ['HOME']}/.config/.clinic/.tokens/{username}.pickle"):
        with open(f"{os.environ['HOME']}/.config/.clinic/.tokens/{username}.pickle",'rb') as token:
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
    return creds


def create_service(creds):
    service = build('calendar', 'v3', credentials=creds)
    return service


def main(service):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    # global service

    creds =None
    creds = validate_token()
    # service = create_service(creds)

    topic = input_API.book_topic(topic_list)
    
    year = 2020
    time = input("slot time: ")
    month = input("slot month: ")
    day = input("slot day: ")
    slot_time = f'{year} {month} {day} {time}'
    pat_email = input_API.book_patient(list_)

    create_doctor_event(slot_time, topic, pat_email,service)



if __name__ == '__main__':
    main()