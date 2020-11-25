from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import Calendar_Commands
import pprint as pprint
import cancel_booking
import csv

doc_list = ['sigamede@student.wethinkcode.co.za']
now = datetime.datetime.utcnow().isoformat() + 'Z'


SCOPES_Doc = ['https://www.googleapis.com/auth/calendar','https://www.googleapis.com/auth/calendar.events']
SCOPES_Pat = ['https://www.googleapis.com/auth/calendar.readonly','https://www.googleapis.com/auth/calendar.events.readonly']
def service_doc():
    """Shows basic usage of the Google Calendar API. for Doctor"""
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
                'main/code/codebase/credentials.json', SCOPES_Doc)
            creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds) 
    return service

# def main(())

print('Hello')
doc_or_pat = input("Are you a Doctor or a patient ").lower()
if doc_or_pat == 'doctor':
    service = service_doc() #Getting the scope of the doctor #Create a token for the doc
elif doc_or_pat == 'patient':
    service = Calendar_Commands.service_pat() #Getting the scope of the pat #create a read only token for pat

create_event = input("Would you like to create a event or be added to a event?(yes/no)").lower()

if create_event == 'yes' and doc_or_pat == 'doctor':
    create_Cal = input("Would you like to create the event on a new calendar(yes/no)?").lower()

    if create_Cal == 'no':    
        summary = input("Give a title for your event")
        description = input("Please give a description for your event")
        startTime = input("Please give a start Time in the following format(yyyy-mm-dd)")
        EndTime = input("Please give a endTime for the event in the following format(yyyy-mm-dd)")
        doc_email = input("Please enter your email?")
        Guestsmodify = input("Would you like your guest to modify the event?(True/False)e.g change event info")
        guestsCanInviteOthers = input("Would you like to allow guests to invite other guests(True/False)")
        notes = input("Please add any notes")
        Calendar_Commands.add_event_doc(service,summary,description,startTime,EndTime,doc_email,Guestsmodify,guestsCanInviteOthers,notes,calendar='primary')


    if create_Cal == 'yes':
        calendar =input("Please name your new caldenar")
        summary = input("Give a title for your event")
        description = input("Please give a description for your event")
        startTime = input("Please give a start Time in the following format(yyyy-mm-dd)")
        EndTime = input("Please give a endTime for the event in the following format(yyyy-mm-dd)")
        doc_email = input("Please enter your email?")
        Guestsmodify = input("Would you like your guest to modify the event?(True/False)e.g change event info")
        notes = input("Please add any notes")
        Calendar_Commands.add_event_doc(service,summary,description,startTime,EndTime,date,doc_email,Guestsmodify,calendar,guestsCanInviteOthers,notes)
      

    


if create_event == "yes" and doc_or_pat == 'patient':
    event = input("What would you like to learn(Test)?")
    for i in doc_list:
        data = service.events().list(calendarId=i,timeMin=now).execute()
        test1 = data.get('items', [])
        print(len(test1))
       
    for i2 in len(test1):
        print(test1[i2]
      
        # if test == event:
        #     print(test)
       


    
        


    