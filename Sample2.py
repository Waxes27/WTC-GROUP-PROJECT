from __future__ import print_function
import datetime
import os.path 
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from datetime import timedelta
import Calendar_Commands

# if user == "Doc":
SCOPES = ['https://www.googleapis.com/auth/calendar']
# elif user == "Patient":
#     SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def main():#Creating,checking for the token
    creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credebtials.json',SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open('token.pickle','wb') as token:
            pickle.dump(creds,token)
    service = build('calendar','v3',credentials=creds)
    return service

if __name__ == "__main__":
    service = main()
    Calendar_Commands.add_event(service)    