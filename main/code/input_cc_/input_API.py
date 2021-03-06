import sys
import os
import datetime
import pickle
# import help_cc as help_cc
# import code.help_cc_.help_cc as help_cc
# from help_cc_ import help_cc as help_cc
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


list_ = ["apillay", "bidaniel", "cdu-pree", "fmokoena", "mbjali", "ndumasi"]
list_ = ["nwalter", "Sigamede", "tmoshole", "vpekane", "Vsithole", "sbaloyi"]
topic_list = ["Recursion", "Unit Testing", "List Comprehensions", "Lambdas", "",]

green = lambda text: '\033[92m' + text + '\033[0m'
red = lambda text: '\033[91m' + text + '\033[0m'
yellow = lambda text: '\33[33m' + text + '\033[0m'


def username():
    username = input("Enter username: ")
    return username


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
        valid_topic_text = yellow("Please choose a valid topic from the list above:\n")
        booking_topic = input(valid_topic_text).capitalize()
    if len(booking_topic) <= 0:
        topic_message = green("You have chosen a General topic\n")
        print(topic_message)
        booking_topic = "General"
        return booking_topic
    return booking_topic


def book_doctor(list_):
    booking_doc = input("Please provide the name of the Coding Clinician.\n").lower()
    if booking_doc == "HELP".lower():
        help_cc.run_main()
        book_doctor(list_)
    while len(booking_doc) <= 0:
        print("Please provide your username.\n")
        booking_doc = input("Please provide the name of the Coding Clinician\n").lower()
    while booking_doc not in list_ and booking_doc != "help":
        valid_topic_text = yellow("Username Invalid, please select a valid username.\n")
        print(valid_topic_text)
        booking_doc = input("Please provide the name of the Coding Clinician\n").lower()
    return booking_doc + '@student.wethinkcode.co.za'


def book_patient(list_):
    booking_pat = input("Please provide the name of the Coding Patient.\n")
    if booking_pat == "HELP".lower():
        help_cc.run_main()
        book_patient(list_)
    while booking_pat not in list_ and booking_pat != "help":
        valid_topic_text = yellow("Username Invalid, please select a valid username.\n")
        print(valid_topic_text)
        booking_pat = input("Please provide the name of the Coding Patient\n")
    while len(booking_pat) <= 0:
        valid_topic_text = yellow("Please provide a valid username\n")
        print(valid_topic_text)
        booking_pat = input("Please provide the name of the Coding Patient\n")
    return booking_pat + '@student.wethinkcode.co.za'


def main():
    book_topic(topic_list)
    book_doctor(list_)
    book_patient(list_)

if __name__ == "__main__":
    main()