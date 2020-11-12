import sys
import os
import datetime
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import help_cc_.help_cc as help_cc
# import help_cc
# from help_cc



doctor_list = ["apillay", "bidaniel", "cdu-pree", "fmokoena", "mbjali", "ndumasi"]
patient_list = ["nwalter", "Sigamede", "tmoshole", "vpekane", "Vsithole", "sbaloyi"]
topic_list = ["Recursion", "Unit Testing", "List Comprehensions", "Lambdas", ""]


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



# def book_topic(topic_list, username, role):
#     print("\nCoding Clinic Topics:\n")
#     print(*topic_list, sep="\n")
#     booking_topic = input("Please choose a topic you would like to clinic? Or leave blank to choose a 'General' topic\n").capitalize()

#     while booking_topic not in topic_list and booking_topic != "General":
#         booking_topic = input("Please choose a valid topic from the list above:\n")

#     if len(booking_topic) <= 0:
#         print("You have chosen a General topic\n")
#         booking_topic = "General"    
#     role_username = (role, username)
#     role_username_topic = {role_username: booking_topic}
#     print('Topic booked\nDetails: ')
#     for user, topic in role_username_topic.items():
#         print(f'Username: {user[1].capitalize()}\nRole: {user[0]}\nBooked topic: {topic}')
#     return booking_topic


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
    for i in range(0,15):
        print('-', end='')
    print()
    for user, topic in role_username_topic.items():
        print(f'Email:        {user[1]}\nRole :        {user[0].capitalize()}\nBooked topic: {topic}')
    return booking_topic



#     key: username,role
#     value: topic
#     return booking_topic


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


if __name__ == "__main__":
    role = get_role()
    if role == 'doctor':
        username = book_doctor(doctor_list)
    if role == 'patient':
        username = book_patient(patient_list)
    book_topic(topic_list, username, role)