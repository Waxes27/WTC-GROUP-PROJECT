import sys
import os
import datetime
import time
import pickle
#from code.help_cc_ import help_cc
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class API_input():    
    
    
    def __init__(self):
        '''
        Class constructor that intialises the variables and lists that will be
        used in the input of the program.
        '''        
        self.__cmdlist = []
        self.__hislist = []
        self.__history_command = 0
        self.list_ = (["apillay", "bidaniel", "cdu-pree", "fmokoena", "mbjali", "ndumasi", 
    "nwalter", "sigamede", "tmoshole", "vpekane", "vsithole", "sbaloyi"])
        self.topic_list = ["Recursion", "Unit Testing", "List Comprehensions", "Lambdas", ""]
        self.list_of_commands = ["USERNAME","HELP","MAKEBOOK","VIEWCAL","LOGOUT","INTERFACE","CLEAR","CANCELBOOK"]
        self.details_of_commands = ["Enter your username","Shows information about the available commands", "Makes a booking for a code clinic session","Views calendar and events","Logs the user out","Access the Interface","Clears the terminal screen", "Cancels the booking"]
        self.topic_list = ["Recursion", "Unittesting ", "List Comprehensions", "Lambdas"]
        self.details_of_topics = ["The repeated application of a recursive procedure or definition.","Automated code to test software written by other developers","Creating new lists from other iterables", "an anonymous function is a function that is defined without a name."]

        
        
    #@property
    def history(self):
        '''
        Getter method that returns the lists as they are needed.
        '''

        return self.__hislist, self.__cmdlist    
        
        
    #@history.setter
    def __execute(self):
        '''
        Setter method that appends input to a list to ensure that they are
        recorded to be able to be undone or redone as needed.
        '''
        
        commands_bt = self.__cmdlist.append(self.book_topic)
        commands_bd = self.__cmdlist.append(self.book_doctor)
        commands_bp = self.__cmdlist.append(self.book_patient)
        if commands_bt != "" and commands_bt != "General":
            self.__hislist.append(commands_bt)
            self.__history_command += 1
        if commands_bd != "":
            self.__hislist.append(commands_bd)
            self.__history_command += 1
        if commands_bp != "":
            self.__hislist.append(commands_bp)
            self.__history_command += 1
        else:
            print(('''Input is invalid. 
            Please select valid input'''))
        return commands_bt, commands_bd, commands_bp    


    def undo(self):
        '''
        Method that pops off the last command done that was appended to the
        history list.
        '''        
        
        if self.__history_command > 0:
            self.__history_command -= 1
            self.__hislist.pop()
            print("Previous command was undone.")
            return self.__hislist
        else:
            print("Nothing to undo.")
            return self.__hislist


    def do_help(self):
        """ 
            The do_help prints out the list of commands that can be used in the system
        """

        help_output = ""
        i = 0
        len_of_commands =len(self.list_of_commands)
        len_of_topic = len(self.topic_list)
        print("List of available commands")
        print("--------------------------")
        while i < len_of_commands:

            print('{:11s} {:1s} {:1s}'.format(self.list_of_commands[i], ":", self.details_of_commands[i]))
            help_output += '{:10s} {:5s} {:1s}'.format(self.list_of_commands[i], ":", self.details_of_commands[i])
            
            i += 1
        print()
        j = 0
        print("Topics list commands available:")
        print("------------------------------\n")

        while j < len_of_topic:

            print('{:23s} {:1s} {:1s}'.format(self.topic_list[j], ":", self.details_of_topics[j]))
            help_output += '{:25s} {:1s} {:1s}'.format(self.topic_list[j], ":", self.details_of_topics[j])
            j += 1
        
        return help_output

            
    '''
    Following methods are taking input from the user to record and display the
    correct information according to the lists used in the previous methods.
    Validates input as needed to ensure more robustness.
    '''    
    
    
    def username(self):
        username = input("Enter username: ")
        return username    
        
        
    def book_topic(self):
        print("Coding Clinic Topics:\n")
        print(*self.topic_list, sep="\n")
        booking_topic = input("Please choose a topic you would like to clinic? Or leave blank to choose a 'General' topic\n").title()
        if booking_topic == "help".capitalize():
            self.do_help()
        if booking_topic == "undo".capitalize():
            self.__execute()
            self.undo()
            self.username()
        while len(booking_topic) <= 0:
            print("You have chosen a General topic\n")
            booking_topic = "General"
            return booking_topic
        while (booking_topic not in self.topic_list and booking_topic != "help".capitalize() 
        and booking_topic != "undo".capitalize()):
            print(booking_topic)
            booking_topic = input("Please choose a valid topic from the list above:\n").capitalize()
        return booking_topic    
        

    def book_doctor(self):
        booking_doc = input("Please provide the name of the Coding Clinician.\n").lower()
        if booking_doc == "HELP".lower():
            self.do_help()
            self.book_doctor()
        if booking_doc == "UNDO".lower():
            self.__execute()
            self.undo()
            print("testing")
            self.book_topic()
        while len(booking_doc) <= 0:
            print("Please provide your username.\n")
            booking_doc = input("Please provide the name of the Coding Clinician.\n").lower()
        while booking_doc not in self.list_ and booking_doc != "help" and booking_doc != "undo":
            print("Username Invalid, please select a valid username.\n")
            booking_doc = input("Please provide the name of the Coding Clinician.\n").lower()
        return booking_doc + '@student.wethinkcode.co.za'    
        
        
    def book_patient(self):
        booking_pat = input("Please provide the name of the Coding Patient.\n").lower()
        if booking_pat == "HELP".lower():
            self.do_help()
            self.book_patient()
        if booking_pat == "UNDO".lower():
            self.undo()
            self.__execute()
            self.book_doctor()
        while booking_pat not in self.list_ and booking_pat != "help" and booking_pat != "undo":
            print("Username Invalid, please select a valid username.\n")
            booking_pat = input("Please provide the name of the Coding Patient.\n")
        while len(booking_pat) <= 0:
            print("Please provide a valid username\n")
            booking_pat = input("Please provide the name of the Coding Patient.\n")
        return booking_pat + '@student.wethinkcode.co.za', self.__history_command + 1    
        
        
    def main(self):
        self.username()
        self.book_topic()
        self.book_doctor()
        self.book_patient()
        
        
if __name__ == "__main__":    
    apiinput = API_input()
    apiinput.main()