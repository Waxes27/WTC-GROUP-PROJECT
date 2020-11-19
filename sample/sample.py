from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import Calendar_Commands
import pprint as pprint
import csv

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar','https://www.googleapis.com/auth/calendar.events']
#auth/calendar is for authorization of the calendarID

def main():
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
                'main/code/codebase/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds) #`Creates a service object API name and version`

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    print(f"{events[0]}\n")
    eventid = events[0]['id']
    print(eventid)

    if not events:
        print('No upcoming events found.')
    for k in events:
        try:
            print(k['start'][''])
        except:
            KeyError
        # start = event['start'].get('dateTime', event['start'].get('date'))
        # try:
        #     print(f"{start}_____{event['summary']}")
        # except:
        #     KeyError

    eventid = '4jrn8456nii6smos7kaon22frc'
    #Calendar_Commands.add_calendar(service) #WORKS
    #Calendar_Commands.create_calendar(service) WORKS
    #Calendar_Commands.add_event(service) #WORKS
    #Calendar_Commands.calendar_data(service) #WORKS For Primary
    #Calendar_Commands.create_calendar(service)
    #Calendar_Commands.deleting_event(service,eventid)
    #Calendar_Commands.events_on_calendar(service)
    #Calendar_Commands.calendar_lists(service)
    #Calendar_Commands.get_event(service)
    #Calendar_Commands.deleting_event(service,eventid)
    # data = Calendar_Commands.get_event(service)
    # print(data)
    # test = service.events().get(calendarId='primary',eventId=eventid).execute()
    # print(test['id'])
    # print(test['status'])
    # id_event = test['id']
    # status = test['status']
    # with open('test.csv', 'w',newline='') as csvfile:
    #     fieldnames = ['id','status']
    #     writer = csv.DictWriter(csvfile,fieldnames=fieldnames)

    #     writer.writeheader()
    #     writer.writerow({'id':id_event,'status':status})
    # # attendee = 'gamingsiya100@gmail.com'
    # eventID = '16ll0lmrjrru142amadeh317r0'
    # Calendar_Commands.patient_cancellation(service,attendee,eventID,data)
   



if __name__ == '__main__':
    main()
    