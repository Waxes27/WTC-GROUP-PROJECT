from __future__ import print_function
import datetime
import pickle
import os.path
from pprint import pprint
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from datetime import timedelta # added 
import json
import os
import sys


#from datetime import date
# import GUI #added
#from codebase import book_slot

s = ' '
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']#removed '.readonly'

event_dict = {"id":[], "date":[], "start_time":[], "end_time":[], "topic":[], "doctor":[], "patient":[]}
event_list = []

def main():
    service = get_service()
    display_events(service)


def get_service():   
    """
        Gets the service from the Google Calendar using the credentials from the User
    """

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
                f'{os.environ["HOME"]}/.config/.clinic/credentials.json', SCOPES)
                #'main/code/codebase/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    
    return service

def get_events(service, now):

    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=100, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    return events

def display_events(service):
    """ 
        Displays the Google calendar events within a given time period 
    """

    global s
    slots = []
    guest_user = ""
    dates_week = []
    x = 0

    x = get_days()
       

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting available slots...\n')

    events = get_events(service, now)
    #pprint(events)


    if not events:
        print('No available slots found.')

    else:
        print("Calendar for the next "+ x + " days:")
        print("------------------------------------")
        print("Available slots :")
        print("------------------------------------")
       
        #get_calendar(events)    
        for google_cal in events:  

            s = google_cal['start'].get('dateTime').split("+")
            date_s = s[0].split("T")
            e = google_cal['end'].get('dateTime').split("+")
            date_e = e[0].split("T")

            try:
                if google_cal['summary'] == "General" or google_cal['summary'] == "Recursion"\
                   or google_cal['summary'] == "Unittesting" or \
                    google_cal['summary'] == "List Comprehensions" or google_cal['summary'] == "Lambdas":
                
                    doctor_email = google_cal['creator']['email']
                    doctor_user = doctor_email.split('@')
                     
                    if google_cal.get("attendees") == None:
                        guest_user = "Available"
                    else:
                        guest_email = google_cal['attendees'][0]['email']
                        user_email = guest_email.split('@')
                        guest_user = user_email[0]
                
                    slots.append("id: " +google_cal['id'] + "\n" + "date: " + date_s[0] + "\n" + 'start_time: '+ date_s[1][:5] + "\n" + 'end_time: '+ date_e[1][:5] + "\n" + 'topic: ' +google_cal['summary'] + "\n" + 'doctor: ' + doctor_user[0]  + "\n" + 'patient: ' + guest_user.ljust(10))
                    
                    event_dict_loader(google_cal['id'] ,date_s[0],date_s[1][:5],date_e[1][:5],google_cal['summary'], doctor_user[0], guest_user)
                    write_calendar_file_json(event_dict)

            except KeyError as e:
                print(e)

        day_to = datetime.datetime.now()
        last_day = day_to + timedelta(days = int(x))
        
        while day_to != last_day:
            dates_week.append(day_to.strftime("%F"))
            day_to = day_to + timedelta(days = 1)
        
        for t in dates_week:
            print('\n')
            print("Date: " + t)
            print ('{:.>80}'.format('.'))
            print('|', 'Start Time'.ljust(9) , '|',' End Time'.ljust(10), '|',' Topic'.ljust(12) ,'|',' Doctor'.ljust(10) , '|',' Patient'.ljust(12),'|')
            print ('{:.>80}'.format('.'))
            used = False

            for p in range(len(slots)):
                act = slots[p]
                act = act.split('\n')
                act.remove(act[0])

                if t == act[0].split(': ',1)[1]:
                    print("|",act[1].split(':',1)[1]," "*(10-len(act[1].split(':',1)[1])) \
                    + "|",act[2].split(':',1)[1]," "*(10-len(act[2].split(':',1)[1])) \
                    + "|",act[3].split(':')[1]," "*(12-len(act[3].split(':',1)[1])) \
                    + "|",act[4].split(':')[1]," "*(10-len(act[4].split(':',1)[1])) \
                    + "|",act[5].split(':')[1],""*(10-len(act[5].split(':')[1])),'|')
                    used = True
                    print("....................................................................")
                elif used == False and p == len(slots) - 1:
                    print("| No bookings made today                                           |")
                    print("....................................................................")
                    used = True
  
    return slots, x


def write_calendar_file_text(slots):
    """
        Write the details from the slot events to the text file
    """

    with open("view_calendar.txt", "w") as opened_file:
        for calendar_list in slots: 
            opened_file.write(calendar_list + '\n')

    opened_file.close()  

def write_display_calendar(slots):
        
    with open(f'{os.environ["HOME"]}/Documents/display_calendar.txt', "a") as opened_file:
        
        opened_file.write("Your calendar for the next 7 days:\n")
        opened_file.write("Available slots :\n")
        for calendar_list in slots:
            opened_file.write(calendar_list + "\n")
            
    opened_file.close()

def get_days():

    while True:
        x = input("How many days do you want to view? ")
        if not x.isdigit():
            print("Please enter the number of days you require:")
            continue
        break        

    return x


def event_dict_loader(id, date, start_time, end_time, topic,doctor,patient):
    
    event_dict["id"].append(id)
    event_dict["date"].append(date)
    event_dict["start_time"].append(start_time)
    event_dict["end_time"].append(end_time)
    event_dict["topic"].append(topic)
    event_dict["doctor"].append(doctor)
    event_dict["patient"].append(patient)

    return True


def read_calendar_file_text(slots):
    pass


def write_calendar_file_json(event_dict):
     
    with open("calendar_dict.json", "w") as outfile:
        json.dump(event_dict, outfile)


if __name__ == '__main__':
    main()
    
