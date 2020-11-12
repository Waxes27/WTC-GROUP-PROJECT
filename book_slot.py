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


def create_patient_event(start, summary, doc_email, duration=1):
    """
    Creates the event on the patients calendar
    """
    string_date_list = list(datefinder.find_dates(start))
    if len(string_date_list) >= 0:
        start = string_date_list[0]
        end_time = start + datetime.timedelta(hours=duration)
    print(start)
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
            {'email': doc_email},
        ]
    }
    result = service.events().insert(calendarId='primary', body=event).execute()
    print("Event created:", result.get("summary"))


def create_doctor_event(pat_email, start, summary, duration=1):
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

username = input("Enter username: ")

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    global service

    creds = None

    if os.path.exists(username + '.pickle'):
        with open(username + '.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open(username  + ".pickle", "wb") as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    input1 = input("What would you like to do: ")
    if input1 == "exit":
        return False
    elif input1 == "book slot":
        input2 = input("doc or pat: ")
        if input2 == "pat":
            slot_time = input("Enter slot date(yyyy-month-day time): ")
            slot_duration = int(input("Enter slot duration: "))
            title = input("Enter topic: ")
            doc_email = input("Doctor email: ")
            create_patient_event(slot_time, title, doc_email, slot_duration)

        if input2 == "doc":
            slot_time = input("Enter slot date(yyyy-month-day time): ")
            slot_duration = int(input("Enter slot duration: "))
            title = input("Enter topic: ")
            pat_email = input("Patient email: ")
            create_doctor_event(pat_email, slot_time, title, slot_duration)


if __name__ == '__main__':
    main()