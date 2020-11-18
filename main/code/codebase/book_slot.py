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
import code.input_cc_.input_API as input_API

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

list_ = ["apillay", "bidaniel", "cdu-pree", "fmokoena", "mbjali", "ndumasi", "sigamede","nwalter", "Sigamede", "tmoshole", "vpekane", "Vsithole", "sbaloyi"]
topic_list = ["Recursion", "Unit Testing", "List Comprehensions", "Lambdas", ""]

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
<<<<<<< HEAD
<<<<<<< HEAD:main/input_cc/book_slot.py
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json'
=======
            flow = InstalledAppFlow.from_client_secrets_file('code/codebase/credentials.json'
>>>>>>> Playground:main/code/codebase/book_slot.py
=======
            flow = InstalledAppFlow.from_client_secrets_file(f"{os.environ['HOME']}/.config/.clinic/credentials.json"
>>>>>>> Playground
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

    create_doctor_event(slot_time, topic, pat_email)



if __name__ == '__main__':
    pass