# THIS MODULE DEALS WITH ALL INPUTS FROM USERS
import sys
import os
import datetime
import pickle
#from googleapiclient.discovery import build
#from google_auth_oauthlib.flow import InstalledAppFlow
#from google.auth.transport.requests import Request


def book_topic():
    booking_topic = input("Please provide a topic you would like to clinic?\n")
    while len(booking_topic) <= 0:
        print("Field cannot be blank, please provide a topic.\n")
        booking_topic = input("Please provide a topic you would like to clinic\n")
    if booking_topic == "Cancel":
        print("Cancelling clinic\n")
        return 0
    return booking_topic


def book_doctor():
    booking_doc = input("Please provide the name of the Coding Clinician.\n")
    while len(booking_doc) <= 0:
        print("Field cannot be blank, please provide your valid username.\n")
        booking_doc = input("Please provide the name of the Coding Clinician\n")
    return booking_doc + '@student.wethinkcode.co.za'


def book_patient():
    booking_pat = input("Please provide the name of the Coding Patient.\n")
    while len(booking_pat) <= 0:
        print("Please provide a valid username\n")
        booking_pat = input("Please provide the name of the Coding Patient\n")
    return booking_pat + '@student.wethinkcode.co.za'


book_topic()
book_doctor()
book_patient()





