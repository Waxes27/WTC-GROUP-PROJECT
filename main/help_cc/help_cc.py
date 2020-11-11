# THIS MODULE IMPLEMENTS A HELP COMMAND WITH A LIST OF ALL POSSIBLE
#import input_cc

import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# from g_setup import main



# Defining of Global variables is done here

#SCOPES = ['https://www.googleapis.com/auth/calendar']

#CREDENTIALS_FILE = 'WTC-GROUP-PROJECT/credentials.json'
CREDENTIALS_FILE = 'path_to_file/credentials.json'
list_of_commands = ["vcal", "mkslot", "vtslot", "ctslot","logout"]
details_of_commands = ["View calendar", "Make a time slot", "View a time slot", "Cancel a time time slot", "Logging out"]

#service = get_calender_service()

# End of global variables

def run_main():
    user = ""

    #user = user_input()
    while user != "logout":
        user = user_input()
        if user == "help":
            do_help()
        elif user == "vcal":
            view_calendar()

def user_input():

    user = input("How can I assist?, please type help for assistance:")

    return user
    
def do_help():

    i = 0
    len_of_commands =len(list_of_commands)
    print("List of available commands")
    print("--------------------------\n")
    while i < len_of_commands:

        print(list_of_commands[i] + "-->" + details_of_commands[i])

        i += 1
    
    print(" ")


def view_calendar():
    service = main()
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('viewing of timeslots')
    print('--------------------')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])


    if not events:
        print('No upcoming events found.')
    else:
        for item in events:
            print(item['summary'])
    # for k in events:
    #     try:
    #         print(k['start'][''])
    #     except:
    #         KeyError


if __name__ == "__main__":

    run_main()

    