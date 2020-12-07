import sys
import os
import datetime
import time
import pickle
#import code.help_cc_.help_cc as help_cc
from googleapiclient.discovery import build
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
        
        
    #@property
    def history(self):
        '''
        Getter method that returns the lists as they are needed.
        '''

        print("Does this work?")
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
            print("testing2")
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
            
            
    def redo(self):
        '''
        Method that repeats the previously undone instruction from the 
        program.
        '''

        if self.__history_command + 1 < len(self.__hislist):
            self.__history_command += 1
            self.__cmdlist[
                self.__hislist[self.__history_command][1]
            ].exec(self.__hislist[self.__history_command][2])
            print("Redoing previous commands")
            return self.__hislist
        else:
            print("Nothing to redo")
            return self.__hislist    
            

            
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
        booking_topic = input("Please choose a topic you would like to clinic? Or leave blank to choose a 'General' topic\n").capitalize()
        #if booking_topic == "help".capitalize():
            #help_cc.run_main()
        if booking_topic == "undo".capitalize():
            self.__execute()
            self.undo()
            print("testing")
            self.username()
        while (booking_topic not in self.topic_list and booking_topic != "help".capitalize() 
        and booking_topic != "undo".capitalize()):
            booking_topic = input("Please choose a valid topic from the list above:\n").capitalize()
        if len(booking_topic) <= 0:
            print("You have chosen a General topic\n")
            booking_topic = "General"
            return booking_topic
        return booking_topic    
        

    def book_doctor(self):
        booking_doc = input("Please provide the name of the Coding Clinician.\n").lower()
        if booking_doc == "HELP".lower():
            #help_cc.run_main()
            self.book_doctor()
        if booking_doc == "UNDO".lower():
            self.__execute()
            self.undo()
            print("testing")
            self.book_topic()
        while len(booking_doc) <= 0:
            print("Please provide your username.\n")
            booking_doc = input("Please provide the name of the Coding Clinician\n").lower()
        while booking_doc not in self.list_ and booking_doc != "help" and booking_doc != "undo":
            print("Username Invalid, please select a valid username.\n")
            booking_doc = input("Please provide the name of the Coding Clinician\n").lower()
        return booking_doc + '@student.wethinkcode.co.za'    
        
        
    def book_patient(self):
        booking_pat = input("Please provide the name of the Coding Patient.\n")
        if booking_pat == "HELP".lower():
            #help_cc.run_main()
            self.book_patient()
        if booking_pat == "UNDO".lower():
            self.undo()
            self.__execute()
            self.book_doctor()
        while booking_pat not in self.list_ and booking_pat != "help" and booking_pat != "undo":
            print("Username Invalid, please select a valid username.")
            booking_pat = input("Please provide the name of the Coding Patient\n")
        while len(booking_pat) <= 0:
            print("Please provide a valid username\n")
            booking_pat = input("Please provide the name of the Coding Patient\n")
        return booking_pat + '@student.wethinkcode.co.za', self.__history_command + 1    
        
        
    def main(self):
        self.username()
        #self.history()
        #self.register(self.book_topic, self.book_doctor, self.book_patient)
        self.book_topic()
        self.book_doctor()
        self.book_patient()
        
        
if __name__ == "__main__":    
    apiinput = API_input()
    apiinput.main()