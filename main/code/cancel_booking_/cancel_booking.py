#THIS MODULE IS MEANT FOR CANCELLATION OF BOOKINGS
from __future__ import print_function
import datetime
import pickle
import os.path
import googleapiclient
from . import datedict
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# import Calendar_Commands
import pprint as pprint
# import input_cc_.input_API as input_API

SCOPES_Doc = ['https://www.googleapis.com/auth/calendar','https://www.googleapis.com/auth/calendar.events']
SCOPES_Pat = ['https://www.googleapis.com/auth/calendar','https://www.googleapis.com/auth/calendar.events']

green = lambda text: '\033[92m' + text + '\033[0m'
red = lambda text: '\033[91m' + text + '\033[0m'
yellow = lambda text: '\33[33m' + text + '\033[0m'

def get_eventid(service,username):
    email = username + "@student.wethinkcode.co.za"
    doc_or_pat= input("Are you a doctor or a patient?: ").lower()
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    if "d" in doc_or_pat:
        subject = input("Please advise the subject?: ").capitalize()
        year = input('Year: ')
        time = input("slot time(7 - 16 / 07:00 - 16:00): ")
        try:
            time = datedict.times[int(time)]
        except:
            ValueError
            KeyError
            pass

        month = input("slot month (1 - 12 or 'december'): ").lower()
        try:
            for k,v in datedict.months.items():
                try:
                    if int(month):
                        month = datedict.months[int(month)][1]
                        print(month)
                except:
                    pass
        except:
            pass
        day = input("slot day: ")

        # subject = 'General'
        # year = 2020
        # time = '12:00'
        # month = 'december'
        # day = '6'

        data = service.events().list(calendarId=email,timeMin=now).execute()
        test1 = data.get('items', [])
        length = len(test1)
        # print(test1)
        for i in range(length):
            test1 = data.get('items', [])
            if test1[i]['summary'] == subject:
                date = test1[i]['start']['dateTime']
                start_date_time = date.split("T")
                start_year = start_date_time[0].split('-')[0]
                start_month = int(start_date_time[0].split('-')[1])
                start_month = datedict.months[start_month][1]

                start_day = start_date_time[0].split('-')[2]
                if len(day) == 1:
                    day = f'0{day}'

                start_hour = ''.join(start_date_time[1].split('-')).split(':')[0]
                start_minute = ''.join(start_date_time[1].split('-')).split(':')[1]
                start_time = start_hour + ':' + start_minute

                # print("WELCOME")
                # print(start_time, time)
                if int(start_year) == int(year) and start_month == month and start_day == day and start_time == time:
                    eventid = test1[i]['id']
                    return eventid, doc_or_pat
                 
    if "p" in doc_or_pat:
        subject = input("Please advise the subject?: ").capitalize()
        year = input('Year: ')
        time = input("slot time(7 - 16 / 07:00 - 16:00): ")
        try:
            time = datedict.times[int(time)]
        except:
            ValueError
            KeyError
            pass

        month = input("slot month (1 - 12 or 'december'): ").lower()
        try:
            for k,v in datedict.months.items():
                try:
                    if int(month):
                        month = datedict.months[int(month)][1]
                        print(month)
                except:
                    pass
        except:
            pass
        day = input("slot day: ")
        # subject = 'General'
        # year = 2020
        # time = '12:00'
        # month = 'december'
        # day = '6'
        data = service.events().list(calendarId='primary',timeMin=now).execute()
        test1 = data.get('items', [])
        length = len(test1)
        for i in range(length):
            test1 = data.get('items', [])
            if test1[i]['summary'] == subject:
                date = test1[i]['start']['dateTime']
                start_date_time = date.split("T")
                start_year = start_date_time[0].split('-')[0]
                start_month = int(start_date_time[0].split('-')[1])
                start_month = datedict.months[start_month][1]

                start_day = start_date_time[0].split('-')[2]
                if len(day) == 1:
                    day = f'0{day}'
                start_hour = ''.join(start_date_time[1].split('-')).split(':')[0]
                start_minute = ''.join(start_date_time[1].split('-')).split(':')[1]
                start_time = start_hour + ':' + start_minute
                attendee = test1[i]['attendees'][0]['email']
                print(attendee)

                print(start_day, day)
                if int(start_year) == int(year) and start_month == month and start_day == day and start_time == time and email == attendee:
                    eventid = test1[i]['id']
                    return eventid, doc_or_pat
    


def doctor_cancellation(service,eventid,doctor):
    data =  service.events().get(calendarId='primary',eventId=eventid).execute()
    if data['organizer']['email'] == doctor :
        #Checks if there no attendees
        try:
            if len(data['attendees']) == 1:
                patient1 = data['attendees'][0]['email']
                patient_time1 = data['start']['dateTime']
                print(f"""The following patient {patient1.split('@')[0]} has a meeting with you at 
{patient_time1.split('T')[-1].split('+')[0]} on the {patient_time1.split('T')[0]}""")
        except KeyError:
            try:
                del_event = service.events().delete(calendarId='primary',eventId= eventid).execute()
            except googleapiclient.errors.HttpError:
                print(yellow("No event to delete"))
                return
            
            print(green("Booking Removed"))
    return
    # else:
        # if len(data['attendees']) == 3:
        #     patient1 = data['attendees'][1]['email']
        #     patient_time1 = data['start']['dateTime']
        #     patient2 = data['attendees'][2]['email']
        #     patient_time2 = data['start']['dateTime']
        #     print(f"The following patient {patient1} has a meeting with you at {patient_time1}")
        #     print(f"The following patient {patient2} has a meeting with you at {patient_time2}")
        # elif len(data['attendees']) == 2:
        #     patient1 = data['attendees'][1]['email']
        #     patient_time1 = data['start']['dateTime']
        #     print(f"The following patient {patient1} has a meeting with you at {patient_time1}")
    

def patient_cancellation(service,eventid,patient):
    data = service.events().get(calendarId='primary',eventId=eventid).execute()
    try:

        if data['attendees'][0]['email'] != patient and data['attendees'][2]['email'] != patient:
            print("You cannot cancel a meeting you are not attending")
        elif data['attendees'][0]['email'] == '':
            print("You cannot cancel a meeting")
        elif data['attendees'][0]['email'] == patient:
            del data['attendees'][0]
            event = service.events().get(calendarId='primary', eventId=eventid).execute()
            event['attendees'][0] = None
            updated_event = service.events().update(calendarId='primary', eventId=eventid, body=event).execute()
        elif data['attendees'][1]['email'] == patient:
            del data['attendees'][1]
            event = service.events().get(calendarId='primary', eventId=eventid).execute()
            event['attendees'][1] = None
            updated_event = service.events().update(calendarId='primary', eventId=eventid, body=event).execute()
    except IndexError:
        print("The are no attendees in the event")



# def main():
    
#     doctor_cancellation(service_pat(),'4352o2h1bsr3vdn6qqefdvu79h_20201127T123000Z','ndumasi@student.wethinkcode.co.za')
# cancel =  input("Cancel event?(yes/no)")
# cancel.lower()


#Must pass in the doctor email


# def update_calendar_pat(service,eventid,new):
#     data = service.events().get(calendarId='primary',eventId=eventid).execute()
#     print(new)
#     update = service.events().update(calendarId='primary',eventId=eventid,body=new).execute()



# if cancel == 'yes' and input_API.book_doctor in doctor_list = ["apillay", "bidaniel", "cdu-pree", "fmokoena", "mbjali", "ndumasi"]:
#     deleting_event(service)

# elif cancel == "yes" and input_API.book_patient in patient_list = ["nwalter", "Sigamede", "tmoshole", "vpekane", "Vsithole", "sbaloyi"]:
#     update_metadata_calendar(service)

# main()


def get_eventID(service,calid, doctor):
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId=calid, timeMin=now,
                                        maxResults=100, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    for i in range(len(events)):
        if events[i]['creator']['email'] == doctor:
            if "Available" in events[i]['summary']:
                id = events[i]['id']
                return id
            elif "Fully" in events[i]['summary']:
                # return None
                continue


def get_eventid_vol(service,username,calid):
    email = username + "@student.wethinkcode.co.za"
    # doc_or_pat= input("Are you a doctor or a patient?: ").lower()
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    # if 'Available' in
    subject = 'Available for booking'#input("Please advise the subject?: ").capitalize()
    year = '2020'#input('Year: ')
    time = '9'#input("slot time(7 - 16 / 07:00 - 16:00): ")
    try:
        time = datedict.times[int(time)]
        if len(time) == 4:
            time = f'0{time}'
    except:
        ValueError
        KeyError
        pass
    print(time)

    month = 12#input("slot month (1 - 12 or 'december'): ").lower()
    try:
        for k,v in datedict.months.items():
            try:
                if int(month):
                    month = datedict.months[int(month)][1]
                    print(month)
            except:
                pass
    except:
        pass
    day = '8'#input("slot day: ")

    # subject = 'General'
    # year = 2020
    # time = '12:00'
    # month = 'december'
    # day = '6'

    data = service.events().list(calendarId=calid,timeMin=now).execute()
    test1 = data.get('items', [])
    length = len(test1)
    # print(test1)
    for i in range(length):
        test1 = data.get('items', [])
        if test1[i]['summary'].split()[0] in subject:
            
            date = test1[i]['start']['dateTime']
            start_date_time = date.split("T")
            start_year = start_date_time[0].split('-')[0]
            start_month = int(start_date_time[0].split('-')[1])
            start_month = datedict.months[start_month][1]

            start_day = start_date_time[0].split('-')[2]
            if len(day) == 1:
                day = f'0{day}'

            start_hour = ''.join(start_date_time[1].split('-')).split(':')[0]
            start_minute = ''.join(start_date_time[1].split('-')).split(':')[1]
            start_time = start_hour + ':' + start_minute

            # print("WELCOME")
            # print(start_time, time)
            if int(start_year) == int(year) and start_month == month and start_day == day and start_time == time:
                eventid = test1[i]['id']
                return eventid