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

#from datetime import date
# import GUI #added
#from codebase import book_slot

s = ' '
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']#removed '.readonly'

event_dict = {}

def main(username):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
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

    service = build('calendar', 'v3', credentials=creds)
    return service



def display_events(service):
    global s
    used = False
    current_date = ''
    slots = []
    guest_user = ""
    x = input("How many days do you want to view? ")

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting available slots...\n')

    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=100, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])


    
    
    if not events:
        print('No available slots found.')

    else:
        print(f"Calendar for today and the next {x} days:")
        #slots.append( "Calendar for the next 7 days:\n")
        print("Available slots :")
        #slots.append("Available slots :\n")
        #print("Dates from " + date_s[0] + " till the " + week)

        for k in events:           
            
            s = k['start'].get('dateTime').split("+")
            date_s = s[0].split("T")
            e = k['end'].get('dateTime').split("+")
            date_e = e[0].split("T")
            count = 0

            try:
        
                day_count = datetime.datetime.now()
                new_final_time = day_count + timedelta(days = int(x)) 
                week = new_final_time.strftime("%F")
                
                if date_s[0] > week:
                    break

                if current_date != date_s[0]:
                    print('\n')
                    print("Date: " + date_s[0])
                    
                    print('Start Time'.ljust(10) , 'End Time'.ljust(10), 'Topic'.ljust(10) ,'Doctor'.ljust(10) , 'Patient'.ljust(10))
                    #slots.append('Start Time'.ljust(10) + " " +'End Time'.ljust(10) + 'Topic'.ljust(10) + 'Doctor'.ljust(10) + 'Patient'.ljust(10))
                    current_date = date_s[0]

                doctor_email = k['organizer']['email']
                doctor_user = doctor_email.split('@')
                     
                if k.get("attendees") == None:
                    guest_user = "Available"
                else:
                    guest_email = k['attendees'][0]['email']
                    user_email = guest_email.split('@')
                    guest_user = user_email[0]

                print ('{:.>80}'.format('.'))
                print(date_s[1][:5].ljust(12) + date_e[1][:5].ljust(12) +k['summary'].ljust(8), doctor_user[0].ljust(12) + guest_user.ljust(10))
                slots.append("ID: " + k['id'] + "\n"+ "Date: " + date_s[0] + "\n" + 'Start Time: '+ date_s[1][:5] + "\n" + 'End Time: '+ date_e[1][:5] + "\n" + 'Topic: ' +k['summary']+ "\n" + 'Doctor: ' + doctor_user[0] + "\n" + 'Patient: ' + guest_user.ljust(10))

                

            except:
                print(KeyError)

            write_calendar_file_text(slots)
            read_calendar_file_text()

            print(" ")

        # input_API.book_topic(topic_list)
        # input_API.book_doctor(doctor_list)
        # input_API.book_patient(patient_list)
        # display_events(service)
       
    return slots, x


def write_calendar_file_text(slots):

    
    # calendar_write = open("view_calendar.txt", "wb")
    with open("view_calendar.txt", "w") as opened_file:
        for calendar_list in slots: 
            opened_file.write(calendar_list + '\n\n')

    opened_file.close()


def read_calendar_file_text():
    pass
    # #filename = 

    # with open("view_calendar.txt", "r") as opened_file:
    #     for calendar_dict in opened_file: 
    #         event_desc, content = calendar_dict.strip().split(':', 1)
    #         event_dict[event_desc] = content.strip()
            #event_dict = calendar_dict.split(',')
            #event_dict[int(key)] = val

    #print(event_dict)
    # return event_dict


def main1(username):
    service = main(username)
    slots ,x = display_events(service)
    
    return x


if __name__ == '__main__':
    main1()
