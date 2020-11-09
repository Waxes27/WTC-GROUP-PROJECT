from __future__ import print_function
import datetime
import pickle
import os.path
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request


SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

creds = None

if os.path.exists('token.pickle'):
    with open('token.pickle' ,'rb') as token:
        creds = pickle.load(token)


print(creds)