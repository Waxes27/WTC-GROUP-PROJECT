from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import Calendar_Commands
import pprint as pprint
import cancel_booking
import csv


SCOPES_Doc = ['https://www.googleapis.com/auth/calendar','https://www.googleapis.com/auth/calendar.events']
SCOPES_Pat = ['https://www.googleapis.com/auth/calendar.readonly','https://www.googleapis.com/auth/calendar.events.readonly']

print('Hello')
doc_or_pat = input("Are you a Doctor or a patient ").lower()
if doc_or_pat == 'doctor':
    service = cancel_booking.service_Doc()
elif doc_or_pat == 'patient':
    service = cancel_booking.service_pat()

Calendar_Commands.calendar_data(service)

# Calendar_Commands.add_event(service)