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
import code.cancel_booking_.cancel_booking as cancel_booking
import code.codebase.event as update_event
#from . import create_service


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']
# SCOPES = ''

list_ = ["apillay", "bidaniel", "cdu-pree", "fmokoena", "mbjali", "ndumasi", "sigamede","nwalter", "Sigamede", "tmoshole", "vpekane", "Vsithole", "sbaloyi"]
topic_list = ["Recursion", "Unit Testing", "List Comprehensions", "Lambdas", ""]

service = ''

def volunteer(service):
    rooms = {
        '4th floor' : ['open area'],
        '5th floor' : ['kitchen']
    }
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=100, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    date = '2020-12-05 09:00'
    start_time = list(datefinder.find_dates(date))[0]
    slot_opening = 'Recursion'
    # print(string_date_list)
    # avail_time = '12:00'
    end_time = start_time + datetime.timedelta(hours=1)
    print(end_time)
    event = {
        'summary': 'Available for booking',
        'start': {
            'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Africa/Johannesburg',
        },
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Africa/Johannesburg',
        },
        'attendees': [
            # {'email' : 'mbjali@student.wethinkcode.co.za'},
            # {'email' : 'cdu-pee@student.wethinkcode.co.za'},
            
        ],
        'location' :  '5th floor',
        'description' : f'Topic : {slot_opening}'
    }
    print(events[0]['start'])
    result = service.events().insert(calendarId='primary', body=event).execute()
    print("Event created:", result.get("summary"))


def book_vol_slot(service):
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=100, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    year = 2020
    month = 12
    day = '05'
    # date = '2020-12-05 09:00'
    date = f'{year}-{month}-{day} 09:00'
    start_time = list(datefinder.find_dates(date))[0]
    end_time = start_time + datetime.timedelta(hours=1)
    slot_topic = 'recursion'.capitalize()
    doctor = 'ndumasi'
    # print(events[0])
    print()
    value = cancel_booking.get_eventid_vol(service, 'ndumasi')
    print(value)
    # for v in events[0]:
    #     print(v)
    # for v in events[0]:
    #     # print(v)
    #     if date.split()[0] in events[0]['start']['dateTime']:
    #         if slot_topic in events[0]['description']:
    #             if doctor in events[0]['creator']['email']:
    #                 print("Clinic found\n\nBooking...")
    #                 return True
    #             else:
    #                 print('No Doctor under the provided username')
    #                 return False
    #         else:
    #             print('Topic unavailable for today')
    #             return False
    #     else:
    #         print('No clinic due today')
    #         return False
    
    event = update_event.event(service, 'mbjali',slot_topic,start_time, end_time)
    try:
        result = service.events().update(calendarId='primary', eventId=value, body=event).execute()
    except TypeError:
        print('Cannot create booking')







def is_slot_avalaible(service, year, month, day, time):
    
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=100, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    

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

        if start_year == year and start_month == month and start_day == day and \
            start_time == time:
            return False
    return True      


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



# if __name__ == '__main__':
#     main()
