import sys
import os
import datetime
import pickle
# import help_cc as help_cc
import code.help_cc_.help_cc as help_cc
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


doctor_list = ["apillay", "bidaniel", "cdu-pree", "fmokoena", "mbjali", "ndumasi"]
patient_list = ["nwalter", "Sigamede", "tmoshole", "vpekane", "Vsithole", "sbaloyi"]
topic_list = ["Recursion", "Unit Testing", "List Comprehensions", "Lambdas", ""]


# def username():
#     username = input("Enter username: ")
#     return username


# def get_role():
#     role = input('What do you wish your role to be for the code clinic? ').lower()
#     roles = ['doctor', 'patient']
#     if role == "HELP".lower():
#         help_cc.run_main()
#     while len(role) == 0 or role not in roles:
#         print('\nYou can either choose to be a \n(1) Doctor or \n(2) Patient.')
#         role = input('What do you wish your role to be for the code clinic? ').lower()
#     print('Role stored successfully.')
#     return role


def book_topic(topic_list):
    print("Coding Clinic Topics:\n")
    print(*topic_list, sep="\n")
    booking_topic = input("Please choose a topic you would like to clinic? Or leave blank to choose a 'General' topic\n").capitalize()
    if booking_topic == "help".capitalize():
        help_cc.run_main()
    while booking_topic not in topic_list and booking_topic != "help":
        booking_topic = input("Please choose a valid topic from the list above:\n").capitalize()
    if len(booking_topic) <= 0:
        print("You have chosen a General topic\n")
        booking_topic = "General"
        return booking_topic
    return booking_topic


def book_doctor(doctor_list):
    booking_doc = input("Please provide the name of the Coding Clinician.\n").lower()
    if booking_doc == "HELP".lower():
        help_cc.run_main()
        book_doctor(doctor_list)
    while len(booking_doc) <= 0:
        print("Please provide your valid username.\n")
        booking_doc = input("Please provide the name of the Coding Clinician\n").lower()
    while booking_doc not in doctor_list and booking_doc != "help":
        print("Username Invalid, please select a valid username.\n")
        booking_doc = input("Please provide the name of the Coding Clinician\n").lower()
    return booking_doc + '@student.wethinkcode.co.za'


def book_patient(patient_list):
    booking_pat = input("Please provide the name of the Coding Patient.\n")
    if booking_pat == "HELP".lower():
        help_cc.run_main()
        book_patient(patient_list)
    while booking_pat not in patient_list and booking_pat != "help":
        print("Username Invalid, please select a valid username.")
        booking_pat = input("Please provide the name of the Coding Patient\n")
    while len(booking_pat) <= 0:
        print("Please provide a valid username\n")
        booking_pat = input("Please provide the name of the Coding Patient\n")
    return booking_pat + '@student.wethinkcode.co.za'


def main():
    book_topic(topic_list)
    book_doctor(doctor_list)
    book_patient(patient_list)