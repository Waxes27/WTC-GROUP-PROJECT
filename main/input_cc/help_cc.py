# THIS MODULE IMPLEMENTS A HELP COMMAND WITH A LIST OF ALL POSSIBLE
#import input_cc

import datetime
# import pickle
import os.path
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
#from g_setup import main
# print("help imported")



# Defining of Global variables is done here
#list_of_commands = ["vcal", "mkslot", "vtslot", "ctslot","logout"]
list_of_commands = ["username","HELP", "MAKEBOOK" , "VIEWBOOK", "CANCELBOOK","MAKESLOT","VIEWSLOT", "CANCELSLOT", "LOGOUT"]
details_of_commands = ["Enter in your username","Shows information about the commands", "Views and books an available time slot", "Views bookings", "Cancels booking", "Creates a time slot", "Displays all avalible time slots", "Cancels a time slot", "Logs the user out"]
topic_list = ["Recursion", "Unit Testing", "List Comprehensions", "Lambdas"]
details_of_topics = ["The repeated application of a recursive procedure or definition.","Automated code to test software written by other developers","Creating new lists from other iterables", "an anonymous function is a function that is defined without a name. "]
# End of global variables

def run_main():
    """ 
    run_main is is the first function to start when help_cc.py starts
    """ 

    do_help()


def do_help():
    """ 
        The do_help prints out the list of commands that can be used in the system
    """

    help_output = ""
    i = 0
    len_of_commands =len(list_of_commands)
    len_of_topic = len(topic_list)
    print("List of available commands")
    print("--------------------------")
    while i < len_of_commands:

        print('{:10s} {:1s} {:1s}'.format(list_of_commands[i], ":", details_of_commands[i]))
        help_output += '{:10s} {:5s} {:1s}'.format(list_of_commands[i], ":", details_of_commands[i])
        
        i += 1

    print(" ")
    j = 0
    print("Topics list commands availabe:")
    print("--------------------")

    while j < len_of_topic:

        print('{:20s} {:1s} {:1s}'.format(topic_list[j], ":", details_of_topics[j]))
        help_output += '{:20s} {:1s} {:1s}'.format(topic_list[j], ":", details_of_topics[j])
        j += 1
    
    return help_output
     

# if __name__ == "__main__":
    # run_main()