#THIS MODULE IMPORTS AND ACTS AS THE MAIN CODEBASE
import code
import code.help_cc_.help_cc as help_cc
import code.codebase.book_slot as book_slot
import code.view_calendar_cc.view_calendar as view_calendar
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
        # book_slot.service
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
    if os.path.exists(f"{os.environ['HOME']}/.config/.clinic/username.txt"):
        username_file = open(f"{os.environ['HOME']}/.config/.clinic/username.txt", 'r')
        username = username_file.readline()
    else:
        print("User not found...\n")
        username = input("Username: ")
        username_file = open(f"{os.environ['HOME']}/.config/.clinic/username.txt", 'w+')
        username_file.write(username)
    
    if sys.argv[-1].lower() == 'help' or len(sys.argv) < 2:
        help_cc.run_main()
        
    elif sys.argv[-1].lower() == 'makebook':
        try:
            book_slot.main()
            service = book_slot.service
        except AttributeError:
            book_slot.main()
    
    elif 'viewcal' in sys.argv[-1]:
        x = view_calendar.main1(username)
        
        # try:
        #     sys.argv[-1] = int(sys.argv[-1])
        # except ValueError:
        #     x= view_calendar.main1(username)
        # print(sys.argv)
        
        
    
    elif sys.argv[-1].lower() == 'username':
        print(f"The current user is... {username}")
        verify = input("Is this you..?\n\n If it is press ENTER else enter a new username: ")
        if len(verify) == 0: #User pressed enter
            clear()
        else:
            username = verify
            username_file = open(f"{os.environ['HOME']}/.config/.clinic/username.txt", 'w+')
            username_file.write(username)
            clear()
            print("Changing config file...")
            time.sleep(3)
            
            
    elif sys.argv[-1].lower() == 'interface':
        interface()


if __name__ == "__main__":
    main()
    # book_slot.main()
    # print(book_slot.service)

