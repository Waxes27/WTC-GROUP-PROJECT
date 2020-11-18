from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from datetime import timedelta # added 
import csv


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']#removed '.readonly'


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
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service


def display_events(service):
    slots = []
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting available slots...\n')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=100, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    
    if not events:
        print('No available slots found.')

    else:
        print("Available slots :\n")
        slots.append('{} {} {} {} {}'.format('Topic','Doctor','Date','Time',"Slots" ))

        for k in events:
            s = k['start'].get('dateTime').split("+")
            date_s = s[0].split("T")
            e = k['end'].get('dateTime').split("+")
            date_e = e[0].split("T") 
            try:
                slots.append('{} {} {} {}-{}'.format(k['summary'],k['organizer']['email'],date_s[0], date_s[1][:5],date_e[1][:5] ))
    
        
            except:
                KeyError
    return events


##########


def write_csv(events):
    with open('hiscsv.csv', 'w', newline='') as f:
        fieldname = ['id', 'Topic', 'Doctor', 'Patient', 'Date', 'Start', 'end']
        writer = csv.DictWriter(f,fieldnames=fieldname)
        writer.writeheader()
        for event in events:
            try:
                if event['attendees'][0]['email'] is not None:
                    guest_email = event['attendees'][0]['email']
                    guest_email = guest_email.split('@')
                    client = guest_email[0]
                else:
                    client =  'Available'
                    
            except KeyError:
                client =  'Available'

            doc = event['creator']['email'].split('@')
            doc = doc[0]
            writer.writerow({'id' : event['id'], 'Topic' : event['summary'], 'Doctor' : doc, 'Patient' : client, 'Date' : event['start']['dateTime'][:10], 'Start' : event['start']['dateTime'][11:][:5], 'end' : event['end']['dateTime'][11:][:5]})


def reader_csv():
    with open('hiscsv.csv','r') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            print(row['Topic'])


if __name__ == "__main__":
    service = main()
    events = display_events(service)
    write_csv(events)
    reader_csv()