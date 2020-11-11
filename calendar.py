from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from datetime import timedelta # added 



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
        print('{:<10s} {:>4s} {:>12s}'.format('Topic','Doctor','Date/Time' ))
        print()
        for k in events:
            s = k['start'].get('dateTime').split("+")
            date_s = s[0].split("T")
            e = k['end'].get('dateTime').split("+")
            date_e = e[0].split("T") 
            try:
                print ('{:.>80}'.format('.'))
                print('{:<10s} {:>4s} {:>12s} - {}:{}'.format(k['summary'],k['organizer']['email'],date_s[0], date_s[1][:5],date_e[1][:5] ))
        
            except:
                KeyError


# def create_event(service,summ, des, start, h):

#    d = datetime.datetime.now().date()
#    start = start.split(":")
#    start = datetime.datetime(d.year, d.month, d.day, int(start[0]),int(start[1]))
#    end = (start + timedelta(hours=h)).isoformat()
#    start = start.isoformat()

#    bodi = {"summary": summ,
#            "description": des,
#            "start": {"dateTime": start, "timeZone": '+02:00'},
#            "end": {"dateTime": end, "timeZone": '+02:00'},}

#    event_result = service.events().insert(calendarId='primary', body= bodi ).execute()
#    s = event_result['start'].get('dateTime').split("+")
#    date_s = s[0].split("T")
#    e = event_result['end'].get('dateTime').split("+")
#    date_e = e[0].split("T") 
# #    print(f"created event: {event_result['summary']}")
# #    print(f"from {date_s[1]} to {date_e[1]}")



if __name__ == '__main__':  
    service = main()
    # create_event(service, "random", "module tings", "12:00", 3)
    display_events(service)
