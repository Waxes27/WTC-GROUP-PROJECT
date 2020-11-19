#THIS MODULE IS MEANT FOR CANCELLATION OF BOOKINGS
from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# import Calendar_Commands
import pprint as pprint
# import input_cc_.input_API as input_API

SCOPES_Doc = ['https://www.googleapis.com/auth/calendar','https://www.googleapis.com/auth/calendar.events']
SCOPES_Pat = ['https://www.googleapis.com/auth/calendar.readonly','https://www.googleapis.com/auth/calendar.events.readonly']



def service_Doc():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
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
                'main/code/codebase/credentials.json', SCOPES_Doc)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds) 
    return service


def service_pat():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
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
                'main/code/codebase/credentials.json', SCOPES_Pat)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds) 
    return service

# cancel =  input("Cancel event?(yes/no)")
# cancel.lower()

def events_on_calendar(service):
    events_cal = service.events().list(calendarId='sigamede@student.wethinkcode.co.za').execute()
    pprint.pprint(events_cal[0])    



def deleting_event(service,eventID):
    del_event = service.events().delete(calendarId='primary',eventId= eventID).execute()

def patient_cancellation(service,attendee,eventID):
    data = Calendar_Commands.get_event(service)
    if data['email'] == attendee:
        data['email'] = ''
        # del data['email']
    update = service.events().update(calendarId='primary',eventId=eventID).execute()
    return update


# if cancel == 'yes' and input_API.book_doctor in doctor_list = ["apillay", "bidaniel", "cdu-pree", "fmokoena", "mbjali", "ndumasi"]:
#     deleting_event(service)

# elif cancel == "yes" and input_API.book_patient in patient_list = ["nwalter", "Sigamede", "tmoshole", "vpekane", "Vsithole", "sbaloyi"]:
#     update_metadata_calendar(service)

if __name__ == "__main__":
    service = service_pat()
    events_on_calendar(service)
    
   