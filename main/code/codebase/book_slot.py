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


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

list_ = ["apillay", "bidaniel", "cdu-pree", "fmokoena", "mbjali", "ndumasi", "sigamede","nwalter", "Sigamede", "tmoshole", "vpekane", "Vsithole", "sbaloyi"]
topic_list = ["Recursion", "Unit Testing", "List Comprehensions", "Lambdas", ""]


green = lambda text: '\033[92m' + text + '\033[0m'
red = lambda text: '\033[91m' + text + '\033[0m'
yellow = lambda text: '\33[33m' + text + '\033[0m'


def volunteer(service, calid, start, topic, room):
    """
    opens a 30min slot for a doctor in the code clinics calendar
    """
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId=calid, timeMin=now,
                                        maxResults=100, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    
    string_date_list = list(datefinder.find_dates(start))
    if len(string_date_list):
        start = string_date_list[0]
        end_time = start + datetime.timedelta(minutes=30)
    event = {
        'summary': 'Available for booking',
        'start': {
            'dateTime': start.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Africa/Johannesburg',
        },
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Africa/Johannesburg',
        },
        'location' :  room,
        'description' : f'Topic: {topic}',
    }
    result = service.events().insert(calendarId=calid, body=event).execute()
    print(result.get("summary"))


def book_vol_slot(service, calid, doctor):
    """
    allows a patient to attend an available event on the code clinics calendar
    """
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId=calid, timeMin=now,
                                        maxResults=100, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    value = cancel_booking.get_eventID(service, calid, doctor)
    if value != None:
        event = service.events().get(calendarId=calid, eventId=value).execute()
    else:
        print("\nDoctor is unavailable/fully booked.")
        return True

    string_date_list = list(datefinder.find_dates(time_slot_input()))
    if len(string_date_list):
        start_time = string_date_list[0]
        end_time = start_time + datetime.timedelta(minutes=30)
    year = 2020
    slot_topic = 'general'.capitalize()
    username = input('username: ')

    event = update_event.event(service, calid, username,slot_topic, start_time, end_time, doctor)
    try:
        result = service.events().update(calendarId=calid, eventId=value, body=event).execute()
        print("Event updated")
    except TypeError as e:
        print(e)
        print('Cannot create booking')


def is_slot_avalaible(calid, service, slot_time):
    """
    checks if the slot the patient is booking is available/not fully booked
    """
    year = '2020'
    month = str(slot_time.split()[1])
    day = str(slot_time.split()[2])
    time = str(slot_time.split()[3])
     
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId=calid, timeMin=now,
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


        full_end_date = i['end'].get('dateTime').split("+")
        end_date_time = full_end_date[0].split("T")
        
        end_year = end_date_time[0].split('-')[0]
        end_month = end_date_time[0].split('-')[1]
        end_day = end_date_time[0].split('-')[2]
        end_hour = ''.join(end_date_time[1].split('-')).split(':')[0]
        end_minute = ''.join(end_date_time[1].split('-')).split(':')[1]
        end_time = end_hour + ':' + end_minute

        loop_start = int(''.join(start_time.split(':')))
        loop_end = int(''.join(end_time.split(':')))
        user_time = int(''.join(time.split(':')))

        for i in range(loop_start, loop_end + 1):
            if start_year == year and start_month == month and start_day == day and \
                i == user_time:
                return False
    return True      


def create_doctor_event(service,calid):
    """
    Used to create a slot for the doctor
    """
    topic = input_API.book_topic(topic_list)
    slot_time = user_time_slot_input()
    room = location()
    if is_slot_avalaible(calid,service, slot_time):
        volunteer(service,calid,slot_time,topic,room)   
    else:
        double_book_text = red('Double boooking is not allowed')
        print(double_book_text)



def validate_token():
    """
    validates the user's token
    either refreshes it if it's expired or creates one if it's not available
    """
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
    """
    creates/run a service
    """
    service = build('calendar', 'v3', credentials=creds)
    return service


def location():
    """
    Asks the doctor for the location of the coding clinic session
    return: room
    """
    rooms = {
        '4th floor' : ['4th floor open area'],
        '5th floor' : ['5th floor kitchen area']
    }
    area = input("which floor will you be using(4/5): ")

    if area == "4":
        room = rooms['4th floor']
        return room
    elif area == '5':
        room = rooms['5th floor']
        return room


def user_time_slot_input():
    """
        Prompts the user for a desired booking time slot
        Returns:

            slot_time (str): The desired year, month, day and time booking
    """

    while True:
        year = 2020
        time = input("slot time e.g [17:00]: ")
        month = input("slot month e.g [11] for November: ")
        day = input("slot day e.g [14]: ")
        if is_time_format_acceptable(time, month, day):
            slot_time = f'{year} {month} {day} {time}'
            sucessful_message = green('Time slot successfully entered.\n')
            print(sucessful_message)
            break
        else:
            warning_message = yellow('Please type in the specified format.')
            print(warning_message)
            continue
    return slot_time


def time_slot_input():
    """
        Prompts the user for event start time, day, month
        Returns:

            slot_time (str): The desired year, month, day and time booking
    """

    while True:
        print("Please enter the event's:")
        year = 2020
        time = input("Start time e.g [17:00]: ")
        month = input("Month e.g [11] for November: ")
        day = input("Day e.g [14]: ")
        if is_time_format_acceptable(time, month, day):
            slot_time = f'{year} {month} {day} {time}'
            sucessful_message = green('Time slot successfully entered.\n')
            print(sucessful_message)
            break
        else:
            warning_message = yellow('Please type in the specified format.')
            print(warning_message)
            continue
    return slot_time


def is_time_format_acceptable(time, month, day):
    """
        Verifies whether time format provided is desired

        Paramaters 
            time (str): desired user time slot
            month (str): desired user month booking
            day (str): desired user day booking
    """

    hour_time = int(time.split(':')[0])
    minute_time = int(time.split(':')[-1])
    month = int(month)
    if month not in range(1,13):
        return False
    if hour_time not in range(0,24):
        return False
    if minute_time not in range(0,59):
        return False
    return True


def main(service):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    # global service

    creds =None
    creds = validate_token()
    # service = create_service(creds)
    topic = input_API.book_topic(topic_list)
    slot_time = user_time_slot_input()
    room = location()
    pat_email = input_API.book_patient(list_)
    create_doctor_event(slot_time, topic, pat_email,service,calid)



# if __name__ == '__main__':
#     main()
