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


def user_input():
    try:
        user_in = input('What would you like to do (type help to see list of commands)...: ').lower()
    except KeyboardInterrupt:
        clear()
        user_in = user_input()
    return user_in


def interface():
    clear()
    print("Welcome to the Interface...")
    time.sleep(3)
    clear()
    user_in = user_input()
        
    while user_in != 'logout':
        if user_in == 'makebook':
            clear()
            
            try:
                book_slot.main()
            except AttributeError:
                book_slot.main()
            user_in = user_input()

        elif user_in.lower() == 'username':
            clear()
            try:
                username = input('What is your username?: ')
            except KeyboardInterrupt:
                clear()
                username = input('What is your username?: ')
            try:
                token = open(f'{username}@student.wethinkcode.co.za.pickle')
            except FileNotFoundError:
                print("User token not found")
            user_in = user_input()

        elif user_in.lower() == 'clear':
            clear()
            user_in = user_input()
            
        elif user_in == 'help':
            help_cc.run_main()
            user_in = user_input()

        elif 'logout' in user_in:
            break
        
        elif user_in == 'interface':
            clear()
            print("You are already in the interface.... Press 'Logout to log out of the system'")
            time.sleep(1.6)
            user_in = input("What would you like to do now...:  ").lower()

        else:
            clear()
            print(f"Invalid command '{user_in}'\n\n")
            help_cc.run_main()
            user_in = input("What would you like to do now...:  ").lower()

    clear()
    print("Logging off...")
    time.sleep(3)


def main():
    clear()
    
    if sys.argv[-1].lower() == 'help' or len(sys.argv) < 2:
        help_cc.run_main()
        
    elif sys.argv[-1].lower() == 'makebook':
        try:
            book_slot.main()
        except AttributeError:
            book_slot.main()
    
    elif sys.argv[-1].lower() == 'interface':
        interface()


if __name__ == "__main__":
    main()
    #book_slot.main()
