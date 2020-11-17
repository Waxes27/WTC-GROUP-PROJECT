#THIS MODULE IMPORTS AND ACTS AS THE MAIN CODEBASE
import code
# import input_cc_.input_API as input_API
import code.help_cc_.help_cc as help_cc
import code.codebase.book_slot as book_slot
import os
import time
import sys


def clear():
    os.system('clear')
    


def main():
    clear()
    user_in = input('What would you like to do (type help to see list of commands)...: ').lower()
    while user_in != 'logout':
        if user_in == 'makebook':
            clear()
            try:
                book_slot.main()
            except AttributeError:
                book_slot.main()
            user_in = input("What would you like to do now...:  ").lower()

        elif user_in.lower() == 'username':
            clear()
            username = input('What is your username?: ')
            try:
                token = open(f'{username}@student.wethinkcode.co.za.pickle')
            except FileNotFoundError:
                print("User token not found")
            
            user_in = input("What would you like to do now...:  ").lower()

        elif user_in.lower() == 'clear':
            clear()
            user_in = input("What would you like to do now...:  ").lower()
            
        elif user_in == 'help':
            help_cc.run_main()
            user_in = input("\nWhat would you like to do now...:  ").lower()

        elif 'logout' in user_in:
            break

        else:
            clear()
            print(f"Invalid command '{user_in}'\n\n")
            help_cc.run_main()
            user_in = input("What would you like to do now...:  ").lower()

    clear()
    print("Logging off...")
    time.sleep(3)



if __name__ == "__main__":

    # token = open('ndumas@student.wethinkcode.co.za.pickle','r')
    main()
    #book_slot.main()
