# THIS MODULE IMPLEMENTS A HELP COMMAND WITH A LIST OF ALL POSSIBLE
#import input_cc

import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from g_setup import main



# Defining of Global variables is done here
#list_of_commands = ["vcal", "mkslot", "vtslot", "ctslot","logout"]
list_of_commands = ["HELP", "MAKEBOOK" , "VIEWBOOK", "CANCELBOOK","MAKESLOT","VIEWSLOT", "CANCELSLOT", "LOGOUT"]
details_of_commands = ["Shows information about the commands", "Views and books an available time slot", "Views bookings", "Cancels booking", "Creates a time slot", "Displays all avalible time slots", "Cancels a time slot", "Logs the user out"]

# End of global variables

def run_main():
    """ 
    run_main is is the first function to start when help_cc.py starts
    """ 

    user = ""
    while user != "logout":
        user = user_input()
        if user == "help":
            do_help()

def user_input():
    """
     user_input asks whether you need assistance and type help 
     for viewing help assistance stores user input.
    """ 

    user = input("How can I assist?, please type help for assistance:")

    return user
    
def do_help():
    """ 
        The do_help prints out the list of commands that can be used in the system
    """

    i = 0
    len_of_commands =len(list_of_commands)
    print("List of available commands")
    print("--------------------------")
    while i < len_of_commands:

        print('{:10s} {:1s} {:1s}'.format(list_of_commands[i], ":", details_of_commands[i]))

        help_output = '{:10s} {:1s} {:1s}'.format(list_of_commands[i], ":", details_of_commands[i])
        i += 1

    print(" ")
    
    return help_output
     

if __name__ == "__main__":
    run_main()

    