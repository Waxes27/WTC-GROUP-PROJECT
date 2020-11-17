from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from datetime import timedelta # added 
#from datetime import date
# import GUI #added

s = ' '
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
                'code/codebase/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service


def display_events(service):
    global s
    used = False
    current_date = ''
    slots = []
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting available slots...\n')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=100, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    # for k in events[0]:
    #     print(k)
    # print(events[0]['summary'])
    # print(events[0]['id'])
    # print(events[0]['creator']['email'])
    # print(events[0]['start']['dateTime'])
    
    
    if not events:
        print('No available slots found.')

    else:
        print("Calendar for the next 7 days:")
        slots += "Calendar for the next 7 days:"
        print("Available slots :")
        slots += "Available slots :"
        #print("Dates from " + date_s[0] + " till the " + week)
       
        # print('{:<10s} {:>4s} {:>12s} {}'.format('Topic','Doctor','Date','Time' ))
        # slots.append('{} {} {} {} {}'.format('Topic','Doctor','Date','Time',"Slots" ))

        

        for k in events:           
            
            s = k['start'].get('dateTime').split("+")
            # print(s)
            date_s = s[0].split("T")
            e = k['end'].get('dateTime').split("+")
            date_e = e[0].split("T")
            count = 0

            try:
        
                day_count = datetime.datetime.now()
                new_final_time = day_count + timedelta(days = 7) 
                week = new_final_time.strftime("%F")
                
                
                
                if date_s[0] > week:
                    break

            
                if current_date != date_s[0]:
                    print('\n')
                    print("Date: " + date_s[0])
                    slots += "Date: " + date_s[0]
                    
                    print('Time'.ljust(10) ,'Topic'.ljust(10) ,'Doctor'.ljust(10) , 'Patient'.ljust(10))
                    slots += 'Time'.ljust(10) ,'Topic'.ljust(10) ,'Doctor'.ljust(10) , 'Patient'.ljust(10)
                    current_date = date_s[0]

                doctor_email = k['organizer']['email']
                doctor_user = doctor_email.split('@')
                     
                if k['attendees'][0]['email'] is not None:
                    guest_email = k['attendees'][0]['email']
                    guest_email = guest_email.split('@')
                    guest_user = guest_email[0]
       
                else:
                    guest_user = "Available"

                print ('{:.>80}'.format('.'))
                print(date_s[1][:5].ljust(12) + k['summary'].ljust(8), doctor_user[0].ljust(12) + guest_user.ljust(10))
                slots += date_s[1][:5].ljust(12) + k['summary'].ljust(8), doctor_user[0].ljust(12) + guest_user[0].ljust(10)
                
            except:
                KeyError
    
    return slots

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


def main1():
    service = main()
    display_events(service)
    # print(s[0])
    
    
if __name__ == '__main__':
    main1()
