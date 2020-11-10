from __future__ import print_function
import datetime
import datefinder
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
#SCOPES = ['https://www.googleapis.com/auth/calendar','https://www.googleapis.com/auth/calendar.events']
SCOPES = ['https://www.googleapis.com/auth/calendar']



creds = None
#service = None

# def check_creds(creds):
#     if os.path.exists('token.pickle'):
#         with open('token.pickle', 'rb') as token:
#             creds = pickle.load(token)
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open('token.pickle', 'wb') as token:
#             pickle.dump(creds, token)
#     return creds


# def create_service(creds):
#     service = build('calendar', 'v3', credentials=check_creds(creds))
#     return service

# creds = check_creds(creds)
# #print(check_creds(creds))
# #print(create_service(creds))

# def create_event(start, summary, description, duration=1):
#     global service
#     string_date_list = list(datefinder.find_dates(start))
#     if len(string_date_list):
#         start = string_date_list[0]
#         end_time = start + datetime.timedelta(hours=duration)
#     event = {
#         'summary': summary,
#         'description': description,
#         'start': {
#             'dateTime': start,
#             'timeZone': 'Africa/Johannesburg',
#         },
#         'end': {
#             'dateTime': end_time,
#             'timeZone': 'Africa/Johannesburg',
#         }
#     }
#     result = service.events().insert(calendarId='primary', body=event).execute()
    #print(f"Event created: {result[0]['items']}")


# def main():
#     check_creds(creds)
#     create_service(creds)
#     create_event("November 10 10:30", "Presentation", "A meeting where we present our project to the client", 2)


#EXAMPLE EVENT
# event = {
#   'summary': 'Google I/O 2015',
#   'location': '800 Howard St., San Francisco, CA 94103',
#   'description': 'A chance to hear more about Google\'s developer products.',
#   'start': {
#     'dateTime': '2015-05-28T09:00:00-07:00',
#     'timeZone': 'America/Los_Angeles',
#   },
#   'end': {
#     'dateTime': '2015-05-28T17:00:00-07:00',
#     'timeZone': 'America/Los_Angeles',
#   },
#   'recurrence': [
#     'RRULE:FREQ=DAILY;COUNT=2'
#   ],
#   'attendees': [
#     {'email': 'lpage@example.com'},
#     {'email': 'sbrin@example.com'},
#   ],
#   'reminders': {
#     'useDefault': False,
#     'overrides': [
#       {'method': 'email', 'minutes': 24 * 60},
#       {'method': 'popup', 'minutes': 10},
#     ],
#   },
# }


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

    # service = build('calendar', 'v3', credentials=creds)
    # #create_service(creds)
    # create_event("November 10 10:30", "Presentation", "A meeting where we present our project to the client", 2)

    service = build('calendar', 'v3', credentials=creds)

    def create_event(start, summary, description, duration=1):
        string_date_list = list(datefinder.find_dates(start))
        if len(string_date_list):
            start = string_date_list[0]
            end_time = start + datetime.timedelta(hours=duration)
        event = {
            'summary': summary,
            'description': description,
            'start': {
                'dateTime': start.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': 'Africa/Johannesburg',
            },
            'end': {
                'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': 'Africa/Johannesburg',
            }
        }
        result = service.events().insert(calendarId='primary', body=event).execute()
        print("Event created:", result.get("summary"))
    
    #event_id = '0lpcna3mkv4otlfp7l2ncfkc5i'
    calendar_id = 'primary'

    def delete_event(cal_id, event_id):
        service.events().delete(calendarId=cal_id, eventId=event_id).execute()
        print("Deleted an event")

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    event_id = ''

    events1 = []

    if not events:
        print('No upcoming events found.')
    else:
        for item in events:
            print(item)
            event_id = item['id']
            #print(f"{item['summary']}")
        print(event_id)

    create_event("november 10 09:00am", "Presentation", "A meeting with the mentors/clients, presenting our app.", 0.20)
    # delete_event(calendar_id, event_id)
#     for k in events:
#         try:
#             print(k['start'][''])
#         except:
#             KeyError
#         # start = event['start'].get('dateTime', event['start'].get('date'))
#         # try:
#         #     print(f"{start}_____{event['summary']}")
#         # except:
#         #     KeyError




if __name__ == '__main__':
    main()