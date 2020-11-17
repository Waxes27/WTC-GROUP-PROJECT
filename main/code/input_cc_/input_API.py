import sys
import os
import datetime
import pickle
# import help_cc as help_cc
import code.help_cc_.help_cc as help_cc
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
<<<<<<< HEAD:main/input_cc/input_API.py
# import help_cc_.help_cc as help_cc
import help_cc
=======
>>>>>>> Playground:main/code/input_cc_/input_API.py


list_ = ["apillay", "bidaniel", "cdu-pree", "fmokoena", "mbjali", "ndumasi"]
list_ = ["nwalter", "Sigamede", "tmoshole", "vpekane", "Vsithole", "sbaloyi"]
topic_list = ["Recursion", "Unit Testing", "List Comprehensions", "Lambdas", ""]


<<<<<<< HEAD:main/input_cc/input_API.py
def get_role():
    role = input('What do you wish your role to be for the code clinic? ').lower()
    roles = ['doctor', 'patient']
    if role == "HELP".lower():
        help_cc.run_main()
    while len(role) == 0 or role not in roles:
        print('\nYou can either choose to be a \n(1) Doctor or \n(2) Patient.')
        role = input('What do you wish your role to be for the code clinic? ').lower()
    print('Role stored successfully.\n')
    return role
=======
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
>>>>>>> Playground:main/code/input_cc_/input_API.py


def book_topic(topic_list, username, role):
    print("\nCoding Clinic Topics:\n")
    print(*topic_list, sep="\n")
    booking_topic = input("Please choose a topic you would like to clinic? Or leave blank to choose a 'General' topic\n").capitalize()
    if booking_topic == "help".capitalize():
        help_cc.run_main()
    while booking_topic not in topic_list and booking_topic != "help":
        booking_topic = input("Please choose a valid topic from the list above:\n").capitalize()
    if len(booking_topic) <= 0:
        print("You have chosen a General topic\n")
        booking_topic = "General"
    
    role_username = (role, username)
    role_username_topic = {role_username: booking_topic}
    print('\nTopic booked')
    print('Details: ')
    for i in range(0,50):
        print('-', end='')
    print()
    for user, topic in role_username_topic.items():
        print(f'Email        : {user[1]}\nRole         : {user[0].capitalize()}\nBooked topic : {topic}')
    return booking_topic


<<<<<<< HEAD:main/input_cc/input_API.py

#     key: username,role
#     value: topic
#     return booking_topic


def book_doctor(doctor_list):
=======
def book_doctor(list_):
>>>>>>> Playground:main/code/input_cc_/input_API.py
    booking_doc = input("Please provide the name of the Coding Clinician.\n").lower()
    if booking_doc == "HELP".lower():
        help_cc.run_main()
        book_doctor(list_)
    while len(booking_doc) <= 0:
        print("Please provide your username.\n")
        booking_doc = input("Please provide the name of the Coding Clinician\n").lower()
    while booking_doc not in list_ and booking_doc != "help":
        print("Username Invalid, please select a valid username.\n")
        booking_doc = input("Please provide the name of the Coding Clinician\n").lower()
    return booking_doc + '@student.wethinkcode.co.za'


def book_patient(list_):
    booking_pat = input("Please provide the name of the Coding Patient.\n")
    if booking_pat == "HELP".lower():
        help_cc.run_main()
        book_patient(list_)
    while booking_pat not in list_ and booking_pat != "help":
        print("Username Invalid, please select a valid username.")
        booking_pat = input("Please provide the name of the Coding Patient\n")
    while len(booking_pat) <= 0:
        print("Please provide a valid username\n")
        booking_pat = input("Please provide the name of the Coding Patient\n")
    return booking_pat + '@student.wethinkcode.co.za'


<<<<<<< HEAD:main/input_cc/input_API.py
if __name__ == "__main__":
    role = get_role()
    if role == 'doctor':
        username = book_doctor(doctor_list)
    if role == 'patient':
        username = book_patient(patient_list)
    book_topic(topic_list, username, role)
=======
def main():
    book_topic(topic_list)
    book_doctor(list_)
    book_patient(list_)
>>>>>>> Playground:main/code/input_cc_/input_API.py
