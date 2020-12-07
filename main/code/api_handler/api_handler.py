from __future__ import print_function
import datetime
import datefinder
import pickle
import os.path
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import time


SCOPES = ['https://www.googleapis.com/auth/calendar']

creds = None

def validate_token():
    # username = input_API.book_doctor(list_)
    if os.path.exists(f"{os.environ['HOME']}/.config/.clinic/username.txt"):
        username_file = open(f"{os.environ['HOME']}/.config/.clinic/username.txt", 'r')
        username = username_file.readline()
        # RUN A LOGIN HERE
    else:
        print("User not found...\n")
        username = input("Username: ")
        # RUN A LOGIN HERE
        username_file = open(f"{os.environ['HOME']}/.config/.clinic/username.txt", 'w+')
        username_file.write(username)

    creds = None

    #topic = input_API.book_topic(topic_list)
    username = f'{username}@student.wethinkcode.co.za'
    if os.path.exists(f"{os.environ['HOME']}/.config/.clinic/.tokens/{username}.pickle"):
        with open(f"{os.environ['HOME']}/.config/.clinic/.tokens/{username}.pickle",'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(f"{os.environ['HOME']}/.config/.clinic/credentials.json"
            , SCOPES)
            creds = flow.run_local_server(port=0)

        with open(f"{os.environ['HOME']}/.config/.clinic/.tokens/{username}.pickle",'wb') as token:
            pickle.dump(creds, token)
    # print(creds)
    return creds


def create_service(creds):
    service = build('calendar', 'v3', credentials=creds)
    return service


def main():
    # print(create_service(validate_token()))
    return create_service(validate_token())

main()