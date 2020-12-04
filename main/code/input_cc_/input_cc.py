<<<<<<< HEAD
=======
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
    return booking_topic.lower().capitalize()


def book_doctor():
    booking_doc = input("Please provide the name of the Coding Clinician.\n")
    while len(booking_doc) <= 0:
        print("Field cannot be blank, please provide your valid username.\n")
        booking_doc = input("Please provide the name of the Coding Clinician\n")
    return booking_doc.lower() + '@student.wethinkcode.co.za'


def book_patient():
    booking_pat = input("Please provide the name of the Coding Patient.\n")
    while len(booking_pat) <= 0:
        print("Please provide a valid username\n")
        booking_pat = input("Please provide the name of the Coding Patient\n")
    return booking_pat.lower() + '@student.wethinkcode.co.za'
>>>>>>> Playground

<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> Playground
def get_role():
=======
def get_role():
    """
        Functions that returns the role of the user for Code Clinic
    Returns:
            role (str): role of user
    """
>>>>>>> refs/remotes/origin/sbaloyi
    role = input('What do you wish your role to be for the code clinic? ').lower()
    roles = ['doctor', 'patient']
    while len(role) == 0 or role not in roles:
        print('\nYou can either choose to be a \n(1) Doctor or \n(2) Patient.')
        role = input('What do you wish your role to be for the code clinic? ').lower()
    print('Role stored successfully.')
    return role

<<<<<<< HEAD
<<<<<<< HEAD
def get_username():
=======
=======
>>>>>>> Playground

def get_username():
    """
        Functions that returns user-provided username
        Returns
            username (str): stores the username
    """
>>>>>>> refs/remotes/origin/sbaloyi
    username = input("Please enter your username: ")
    if len(username) == 0:
        username = input("Please enter your username: ")
    print(f'Welcome {username}!')
<<<<<<< HEAD
    return


def get_date():
=======
    return username


<<<<<<< HEAD:main/input_cc/input_cc.py
def get_date():
    """
        Function that returns desired date and time for a Code Clinic
        Returns:
            picked_date (str): Stores the user's desired date
            chosen_time (str): Stores the user's desired time
    """
>>>>>>> refs/remotes/origin/sbaloyi
    chosen_date = input('Book a slot in the format dd-mm-yyyy: ')
    chosen_time = input('Book a time slot in the format hh:mm: ')
    chosen_date = chosen_date.split('-')
    chosen_date = [int(i) for i in chosen_date]
    x = datetime.datetime(chosen_date[2], chosen_date[1], chosen_date[0])
    picked_date = x.strftime("%A %d %B")
    print('Timne slot created for:', chosen_time, picked_date)
<<<<<<< HEAD
    return picked_date

=======
    return picked_date, chosen_time
>>>>>>> refs/remotes/origin/sbaloyi

if __name__ == "__main__":
    import datetime
    get_role()
    get_username()
<<<<<<< HEAD
<<<<<<< HEAD
    picked_date = get_date()
=======
    get_date()





>>>>>>> refs/remotes/origin/sbaloyi
=======
    get_date()
>>>>>>> Playground
=======
def main():
    book_topic()
    book_doctor()
    book_patient()

if __name__ == "__main__":
    pass
>>>>>>> Playground:main/code/input_cc_/input_cc.py
