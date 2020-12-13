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
import time
import sys


#from datetime import date
# import GUI #added
#from codebase import book_slot

s = ' '
# calid = 'c_4pa2luaf52rfdc8f0tn05bf1qo@group.calendar.google.com'
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']#removed '.readonly'

event_dict = {"id":[], "date":[], "start_time":[], "end_time":[], "topic":[], "doctor":[], "guest_user_1":[], "guest_user_2":[], "booked":[]}
event_list = []

def main(service, calid):
    # service = get_service()
    display_events(service, calid)


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

def get_events(service, calid, now):

    events_result = service.events().list(calendarId=calid, timeMin=now,
                                        maxResults=100, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    return events

def display_events(service,calid):
    """ 
        Displays the Google calendar events within a given time period 
    """

    global s
    slots = []
    ids = []
    dates_week = []
    x = 0
    save = False
    count = 0
    guest_user = []
    topic = ''
    description = ''
    topic_desc = ''
    email_count = 0
    booked = ''
    opened = ''
    idss = []
    temp_id = []

    x = get_days()
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    
    print('Getting available slots...\n')

    events = get_events(service, calid ,now)
    #pprint(events)

    if not events:
        print('No available slots found.')

    else:
        print("Calendar for the next "+ x + " days:")
        print("------------------------------------")
        print("Available slots :")
        print("------------------------------------")
         
        for google_cal in events:  

            s = google_cal['start'].get('dateTime').split("+")
            date_s = s[0].split("T")
            e = google_cal['end'].get('dateTime').split("+")
            date_e = e[0].split("T")

            try:
                
                doctor_email = google_cal['creator']['email']
                doctor_user = doctor_email.split('@')
                    
                try:
                    while count <= 1:
                        if google_cal.get("attendees") == None or google_cal['attendees'][count]['email'] == None:
                            guest_user.append("Available")
                            guest_user.append("Available")
                        else:
                            guest_email = google_cal['attendees'][count]['email']
                            user_email = guest_email.split('@')
                            guest_user.append(user_email[0])
                            email_count += 1
                        count += 1

                    count=0
                except:
                    guest_user.append("Available")  


                if email_count == 2:
                    booked = "Fully booked"
                else:
                    booked = "Available"
                
                email_count = 0

                topic = google_cal['description'] 
                description = topic.split(': ')
                topic_desc = description[1]
                
                slots.append("id: "+google_cal['id']+ "\n"+ "date: "+date_s[0]+"\n"+'start_time: '+ date_s[1][:5]+ "\n"+ 'end_time: '+ date_e[1][:5]+ "\n"+ 'topic: '+ topic_desc+ "\n"+ 'doctor: ' + doctor_user[0]+ "\n" + 'patient 1: ' + guest_user[0].ljust(10) + '\n'+'patient 2: ' + guest_user[1].ljust(10)+  "\n" + 'Available:' + booked)
                ids.append(google_cal['id'])
                #opened = read_calendar_id(ids)
                #write_calendar_id(ids, opened)  
                #write_calendar_id(google_cal['id'], opened)  
                event_dict_loader(google_cal['id'] ,date_s[0],date_s[1][:5],date_e[1][:5],topic_desc, doctor_user[0],guest_user[0], guest_user[1], booked)
                write_calendar_file_json(event_dict)
                save = write_display_calendar(google_cal['id'] ,date_s[0],date_s[1][:5],date_e[1][:5],topic_desc, doctor_user[0],guest_user[0], guest_user[1], booked, save)
                guest_user.clear()
            except KeyError as e:
                print(e)

        write_calendar_id(ids, opened)  

        day_to = datetime.datetime.now()
        last_day = day_to + timedelta(days = int(x))
        
        while day_to != last_day:
            dates_week.append(day_to.strftime("%F"))
            day_to = day_to + timedelta(days = 1)
        
        for t in dates_week:
            print('\n')
            print("Date: " + t)
            print ('{:.>112}'.format('.'))
            print('|', 'Start Time'.ljust(9) , '|',' End Time'.ljust(10), '|',' Topic'.ljust(13) ,'|',' Doctor'.ljust(10) , '|',' Patient 1'.ljust(12),'|', ' Patient 2'.ljust(13),'|','Available:'.ljust(22) , '|')
            print ('{:.>112}'.format('.'))
            used = False

            for p in range(len(slots)):
                act = slots[p]
                act = act.split('\n')
                act.remove(act[0])

                if t == act[0].split(': ',1)[1]:
                    print("|",act[1].split(':',1)[1]," "*(10-len(act[1].split(':',1)[1]))\
                    + "|",act[2].split(':',1)[1]," "*(10-len(act[2].split(':',1)[1])) \
                    + "|",act[3].split(':')[1]," "*(13-len(act[3].split(':',1)[1])) \
                    + "|",act[4].split(':')[1]," "*(10-len(act[4].split(':',1)[1])) \
                    + "|",act[5].split(':')[1]," "*(12-len(act[5].split(':')[1]))\
                    + "|",act[6].split(':')[1]," "*(13-len(act[6].split(':')[1]))\
                    + "|",act[7].split(':')[1]," "*(21-len(act[7].split(':')[1])),'|')
                    used = True
                    print ('{:.>112}'.format('.'))
                elif used == False and p == len(slots) - 1:
                    print("| No bookings made today                                                                                       |")
                    print ('{:.>112}'.format('.'))
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

def write_calendar_id(id, opened):
    
    file_open = "id_found.txt"
    #if opened == False or os.stat(file_open).st_size == 0:
    with open("id_found.txt", "a") as opened_file:
        for ids in id:
            opened_file.write(ids + '\n')
    opened_file.close()
    #else:
    #compare_id(id)
   
    pass

def compare_id(id):

    # file_open = "id_found.txt"

    # with open(file_open, "r") as opened_file:
    #         for ids_find in file_open:
    #             contents  = ids_find.readlines(1)
    #             if contents != id:
    #                 print("Go")
    #             else:
    #                 print("Back")
    # opened_file.close()
    pass


def read_calendar_id(id):
    opened = False
    file_name = "id_found.txt"
    
    if path.exists(file_name) == False or os.stat(file_name).st_size == 0:
        return False
    else:
        with open(file_name) as opened_file:
            bio = opened_file.read()

        #print(bio)

            
            
            # if opened_file.mode = "r":

            # for ids_find in opened_file:
            #     if ids_find.readlines == id:
            #         return True
        #files = file_open.read()
        # for x in files:
        #     if ids_find == id:
        #         print("Testing")
        #         return True  
        # with open(file_open, "r") as opened_file:
        #     for ids_find in file_open:
        #         if ids_find == id:
        #             return True         
        #opened_file.close()
   


def write_display_calendar(id ,date,start_time,end_time,topic, doctor, guest_user_1, guest_user_2,booked, save):
        
    with open(f'{os.environ["HOME"]}/Documents/display_calendar.doc', "a") as opened_file:
        if save == False:
            opened_file.write("Your calendar for the next 7 days:\n")
            opened_file.write("Available slots :\n")
            opened_file.write('==========================================================================\n')

        opened_file.write("Date: " + date + '\n')
        opened_file.write("Time: " + start_time + "-" + end_time + '\n')
        opened_file.write("Topic: " + topic + " "[:15] + '\n')
        opened_file.write("People attending\n")
        opened_file.write("Doctor: " + doctor + " "[:15] + '\n')
        opened_file.write("Patient: " + guest_user_1 + " "[:15])
        opened_file.write("Patient: " + guest_user_2 + " "[:15])
        opened_file.write("\nAvailable: " +booked)
        opened_file.write('\n')
        opened_file.write('==========================================================================')
        opened_file.write('\n')
    opened_file.close()

    save = True

    return save


def get_days():

    while True:
        x = input("How many days do you want to view? ")
        if not x.isdigit():
            print("Please enter the number of days you require:")
            continue
        break        

    return x


def event_dict_loader(id, date, start_time, end_time, topic,doctor,guest_user_1, guest_user_2, booked):
    
    event_dict["id"].append(id)
    event_dict["date"].append(date)
    event_dict["start_time"].append(start_time)
    event_dict["end_time"].append(end_time)
    event_dict["topic"].append(topic)
    event_dict["doctor"].append(doctor)
    event_dict["guest_user_1"].append(guest_user_1)
    event_dict["guest_user_2"].append(guest_user_2)
    event_dict["booked"].append(booked)

    return True


def read_calendar_file_text(slots):
    pass


def write_calendar_file_json(event_dict):
     
    with open("calendar_dict.json", "w") as outfile:
        json.dump(event_dict, outfile)


if __name__ == '__main__':
    main()
    
