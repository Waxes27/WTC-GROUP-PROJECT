import sys
import os
import datetime
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import help_cc


doctor_list = ["apillay", "bidaniel", "cdu-pree", "fmokoena", "Mbjali", "Ndumasi"]
patient_list = ["nwalter", "Sigamede", "tmoshole", "vpekane", "Vsithole", "sbaloyi"]
topic_list = ["Recursion", "Unit Testing", "List Comprehensions", "Lambdas", ""]


def get_role():
    role = input('What do you wish your role to be for the code clinic?: ').lower()
    roles = ['doctor', 'patient']
    while len(role) == 0 or role not in roles:
        print('\nYou can either choose to be a \n(1) Doctor or \n(2) Patient.')
        role = input('What do you wish your role to be for the code clinic?: ').lower()
    print('Role stored successfully.\n')
    return role


def doctor_username(doctor_list):
    booking_doc = input("Please provide the name of the Coding Clinician: ").lower()
    
    while len(booking_doc) <= 0 or booking_doc not in doctor_list:
        print("Please provide a valid username.\n")
        booking_doc = input("Please provide the name of the Coding Clinician: ").lower()
    return booking_doc + '@student.wethinkcode.co.za'


def patient_username(patient_list):
    booking_pat = input("Please provide the name of the Coding Patient: ").lower()
    
    while len(booking_pat) <= 0 or booking_pat not in patient_list:
        print("\nPlease provide a valid username.")
        booking_pat = input("Please provide the name of the Coding Patient\n").lower()

    return booking_pat + '@student.wethinkcode.co.za'


def print_topics(topic_list):
    print("Coding Clinic Topics:\n")
    print(*topic_list, sep="\n")


def print_topic_booking(role_username, booking_topic):
    role_username_topic = {role_username: booking_topic}
    print('\nTopic booked!\n\nDetails: ')
    for user,topic in role_username_topic.items():
        print(f'Username: {user[0]} \nRole: {user[1].capitalize()} \nTopic: {topic}')


def get_date():
    """
        Function that returns desired date and time for a Code Clinic
        Returns:
            picked_date (str): Stores the user's desired date
            chosen_time (str): Stores the user's desired time
    """
    chosen_date = input('Book a slot in the format dd-mm-yyyy: ')
    chosen_time = input('Book a time slot in the format hh:mm: ')
    chosen_date = chosen_date.split('-')
    chosen_date = [int(i) for i in chosen_date]
    x = datetime.datetime(chosen_date[2], chosen_date[1], chosen_date[0])
    picked_date = x.strftime("%A %d %B")
    print('Timne slot created for:', chosen_time, picked_date, end='\n\n')
    return picked_date

def book_topic(topic_list, username, role):
    print_topics(topic_list)

    booking_topic = input("Please choose a topic you would like to clinic? Or leave blank to choose a 'General' topic: ").capitalize()
    
    while booking_topic not in topic_list and booking_topic != "General":
        booking_topic = input("Please choose a valid topic from the list above:\n")
    
    if len(booking_topic) <= 0:
        print("You have chosen a General topic\n")
        booking_topic = "General"    
    role_username = (username, role)
    print_topic_booking(role_username, booking_topic)

    return booking_topic


def handle_user():
    role = get_role()
    if role == 'doctor':
        username = doctor_username(doctor_list)
        get_date()
    if role == 'patient':
        username = patient_username(patient_list)
    
    book_topic(topic_list, username, role)


if __name__ == "__main__":
    handle_user()
    
