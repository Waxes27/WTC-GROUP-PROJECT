# from __future__ import print_function
# import datetime
# import os.path 
# import pickle
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# from datetime import timedelta
#Creating The Methods for caldenar

#Clearing The Caldendar of all events
def clear_caldendar():
    clear_cal = service.calendars().clear('CalendarName').execute()


#Deleting a caldenar in your caldenar
def delete_calendar(service):
    del_calendar = {'summary:'}
    del_cal = service.calendars().delete(calendarId='Test').execute()

#Gets all the data of a caldenar like its Id, 
def add_calendar(service):#WORKS
    add_cal = service.calendars().get(calendarId='primary').execute()
    print(add_cal['id'])
    print(add_cal['timeZone'])
    print(add_cal['summary'])
    print(add_cal['location'])

# #Creating a new caldenar for calendar
def create_calendar(service):
    new_caldendar = {'summary':'test',} #Summary is the Name of the Calendar
    create_cal =  service.calendars().insert(body=new_caldendar,calendarId='Test').execute()


#Deleting a calendar CHECK
def deleting_calendar(service):
    delete_calendar = service.calendars().delete(calendarId='Test').execute()

# #Checking for the heads,labels in the calendar e.g calendarId,timezone etc
# def labels_calendar():
#     label_cal = service.calendarList().list().execute()
#     pprint(label_cal)


#Clearing users all events
def clear_all_events():
    clear_cal_events =  service.calendars().clear('primary').execute()

#Gets all the metadata for calendar e.g 
def calendar_data(service):
    cal_data = service.calendars().get(calendarId='primary').execute()
    print(cal_data['summary'])
    print(cal_data['id'])
    print(cal_data['timeZone'])
    print(cal_data['kind'])
    print(cal_data['conferenceProperties'])

#Deleting a event on a calendar,note we 
def deleting_event(service):
    event_del = {}
    
    del_event = service.events().delete(calendarId='primary',eventID= '6mbqvt0rkmjvskoukjtkv8etho').execute()

#Adding a insert to calendar

def add_event(service): #WORKS
    reponse = ['accepted','tenative','declined','needsAction']
    status = ['confirmed','cancelled']

    # if user == "Doc": 
    #     role = "writer"
    # elif user == "patient":
    #     role = "reader"

    event_details_body = {
        'summary': 'Titleofevent',
        'description': 'This is a event',
        'start':{'dateTime':'2020-11-11T10:00:00-07:00','timeZone':'+02:00',},
        'end':{'dateTime':'2020-11-11T11:00:00-09:00','timeZone': '+02:00',},
        'attendees':[{'email':'sigamede@student.wethinkcode.co.za','responseStatus':'accepted'},],
        'reminders':{'useDefault': False,'overrides':[{'method': 'email','minutes': 24*60},{'method': 'popup','minutes':10},]},

        
        }

        #Must add the Error 403 This is for Calendar ID
        #Must add the Error 400 This is for API Key
        #Error 404: The request is missing a valid API key.

        #When creating a 

    
    event = service.events().insert(calendarId='primary',body= event_details_body,maxAttendees=2,sendNotifications = True,sendUpdates = 'all').execute()
    
  

def gets_permissions():
    



#Creating permissions  for events
def doc_permissions ():
    pass





def patient_permissions():
    pass   




