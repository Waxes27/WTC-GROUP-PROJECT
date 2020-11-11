<<<<<<< HEAD
# THIS MODULE DEALS WITH ALL INPUTS FROM USERS
=======
>>>>>>> Playground
import sys
import os
import datetime
import pickle
<<<<<<< HEAD
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





=======
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import help_cc


doctor_list = ["apillay", "bidaniel", "cdu-pree", "fmokoena", "Mbjali", "Ndumasi"]
patient_list = ["nwalter", "Sigamede", "tmoshole", "vpekane", "Vsithole", "sbaloyi"]
topic_list = ["Recursion", "Unit Testing", "List Comprehensions", "Lambdas", ""]


def get_role():
    role = input('What do you wish your role to be for the code clinic? ').lower()
    roles = ['doctor', 'patient']
    while len(role) == 0 or role not in roles:
        print('\nYou can either choose to be a \n(1) Doctor or \n(2) Patient.')
        role = input('What do you wish your role to be for the code clinic? ').lower()
    print('Role stored successfully.')
    return role


def book_topic(topic_list):
    print("Coding Clinic Topics:\n")
    print(*topic_list, sep="\n")
    booking_topic = input("Please choose a topic you would like to clinic? Or leave blank to choose a 'General' topic\n").capitalize()
    while booking_topic not in topic_list and booking_topic != "General":
        booking_topic = input("Please choose a valid topic from the list above:\n")
    if len(booking_topic) <= 0:
        print("You have chosen a General topic\n")
        booking_topic = "General"
        return booking_topic
    return booking_topic


def book_doctor(doctor_list):
    booking_doc = input("Please provide the name of the Coding Clinician.\n").lower()
    while len(booking_doc) <= 0:
        print("Please provide your valid username.\n")
        booking_doc = input("Please provide the name of the Coding Clinician\n").lower()
    while booking_doc not in doctor_list:
        print("Username Invalid, please select a valid username.\n")
        booking_doc = input("Please provide the name of the Coding Clinician\n").lower()
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
    role = get_role()
    book_topic(topic_list)
    if role == 'doctor':
        book_doctor(doctor_list)
    if role == 'patient':
        book_patient(patient_list)
>>>>>>> Playground
