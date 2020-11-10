import sys
import os
import datetime
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


doctor_list = ["apillay", "bidaniel", "cdu-pree", "fmokoena", "Mbjali", "Ndumasi"]
patient_list = ["nwalter", "Sigamede", "tmoshole", "vpekane", "Vsithole", "sbaloyi"]
topic_list = ["Recursion", "Unit Testing", "List Comprehensions", "Lambdas", ""]

def book_topic(topic_list):
    print("Coding Clinic Topics:\n")
    print(*topic_list, sep="\n")
    booking_topic = input("Please choose a topic you would like to clinic? Or leave blank to choose a 'General' topic\n")
    while booking_topic not in topic_list and booking_topic != "General":
        booking_topic = input("Please choose a valid topic from the list above:\n") 
    if len(booking_topic) <= 0:
        print("You have chosen a General topic\n")
        booking_topic = "General"
        return booking_topic
    return booking_topic


def book_doctor(doctor_list):
    booking_doc = input("Please provide the name of the Coding Clinician.\n")
    while len(booking_doc) <= 0:
        print("Please provide your valid username.\n")
        booking_doc = input("Please provide the name of the Coding Clinician\n")
    while booking_doc not in doctor_list:
        print("Username Invalid, please select a valid username.\n")
        booking_doc = input("Please provide the name of the Coding Clinician\n")
    return booking_doc + '@student.wethinkcode.co.za'


def book_patient(patient_list):
    booking_pat = input("Please provide the name of the Coding Patient.\n")
    while booking_pat not in patient_list:
        print("Username Invalid, please select a valid username.")
        booking_pat = input("Please provide the name of the Coding Patient\n")
    while len(booking_pat) <= 0:
        print("Please provide a valid username\n")
        booking_pat = input("Please provide the name of the Coding Patient\n")
    return booking_pat + '@student.wethinkcode.co.za'

if __name__ == "__main__":
    book_topic(topic_list)
    book_doctor(doctor_list)
    book_patient(patient_list)