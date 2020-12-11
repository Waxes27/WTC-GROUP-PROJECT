#THIS MODULE IMPORTS AND ACTS AS THE MAIN CODEBASE
import subprocess
import code
import code.help_cc_.help_cc as help_cc
import code.codebase.book_slot as book_slot
import code.view_calendar_cc.view_calendar as view_calendar
import code.cancel_booking_.cancel_booking as cancel_booking
import code.api_handler.api_handler as api_handler
import code.codebase.preset as preset
import datetime
import json
import os
import time
import sys




def config(username):
    os.system(f"""echo "---
    editor: code
    repo_path: ~/problems
    navigator_url: "https://navigator.wethinkcode.co.za"
    username: {username}@student.wethinkcode.co.za
    review_manager_url: "https://review-manager.wethinkcode.co.za"
    keycloak_url: "https://keycloak.wethinkcode.co.za"" > ~/.config/wtc/config.yml""")


def verify_user(username):
    # os.system('wtc-lms config')
    #subprocess.check_output('wtc-lms config', shell=True)
    clear()
    if username not in subprocess.getoutput('wtc-lms config')[190:]:
        print('changing config file...')
        time.sleep(1)
        # janet()
        if username not in subprocess.getoutput('wtc-lms config')[190:]:
            print(f"User not found\n\n --->  Added new user\n\n Welcome {username}\n")
            config(username)
            # username = get_username()

    return username


def failed_authentication(username):
    # print("Authentication Failed! Please try again")

    try:
        verification = input(f'\n  >>>   {username}\n\n Is this you?\n\n >> If this ({username}) is you press ENTER\n\n >>> Otherwise enter a new username\n---> ')
    except KeyboardInterrupt:
        clear()
        value = failed_authentication(username)

    if len(verification) == 0:          # User pressed ENTER
        value = check_output_login(username)
    else:
        # username = verification

        username = verify_user(verification)

        value = check_output_login(username)
    return value


def check_output_login(username):
    # print(username)
    try:
        value = subprocess.check_output("wtc-lms login", shell=True)
    except subprocess.CalledProcessError as e:
        clear()
        value = failed_authentication(username)

    return value


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
    service = api_handler.main()
    clear()
    print("Welcome to the Interface...")
    time.sleep(3)
    clear()
    user_in = user_input()
        # book_slot.service
    while user_in != 'logout':
        
        if 'make' in user_in.lower():
            clear()
            
            try:
                book_slot.main(service)
            except AttributeError:
                book_slot.main(service)
            user_in = user_input()


        elif 'user' in user_in.lower():
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
            user_in = user_input()
        
        elif 'view' in user_in.lower():
            clear()
            if os.path.exists(f"{os.environ['HOME']}/.config/.clinic/username.txt"):
                username_file = open(f"{os.environ['HOME']}/.config/.clinic/username.txt", 'r')
                username = username_file.readline()
            else:
                print("User not found...\n")
                username = input("Username: ")
                username_file = open(f"{os.environ['HOME']}/.config/.clinic/username.txt", 'w+')
                username_file.write(username)
                clear()
            x = view_calendar.main1(username)
            user_in = user_input()

        else:
            clear()
            print(f"Invalid command '{user_in}'\n\n")
            help_cc.run_main()
            user_in = input("What would you like to do now...:  ").lower()

    clear()
    print("Logging off...")
    time.sleep(3)


def eventid_find(service):
    clear()
    slots = view_calendar.display_events(service)
    clear()
    doctor_verify = input("Are you a: \nD - Doctor\nP - Patient\n").lower()
    while doctor_verify != 'd' and doctor_verify != 'p':
        doctor_verify = input("Are you a: \nD - Doctor\nP - Patient\n").lower()


def delete_config():
    os.system(f"rm -rf {os.environ['HOME']}/.config/.clinic/username.txt")
    os.system(f"rm -rf {os.environ['HOME']}/.config/.clinic/.tokens")
    os.system(f"mkdir {os.environ['HOME']}/.config/.clinic/.tokens")

        


def main():
    calid = 'g67ktgipc1jjcg9tkqdtol6r54@group.calendar.google.com'
    service = api_handler.main()
    # book_slot.volunteer(service)
    # return
    clear()
    if 'del' in sys.argv:
        delete_config()
        return
    if os.path.exists(f"{os.environ['HOME']}/.config/.clinic/username.txt"):
        username_file = open(f"{os.environ['HOME']}/.config/.clinic/username.txt", 'r')
        username = username_file.readline()

        # username = f'{username}@student.wethinkcode.co.za'
    else:
        print("User not found...\n")
        username = input("Username: ")
        clear()
        username_file = open(f"{os.environ['HOME']}/.config/.clinic/username.txt", 'w+')
        value = check_output_login(username)

        if b'Login successful' in value:
            clear()
            print(f"Welcome {username}")
            time.sleep(1.7)
            clear()
            username_file.write(username)
        else:
            failed_authentication(username)

    if sys.argv[-1].lower() == 'help' or len(sys.argv) < 2:
        help_cc.run_main()


    elif 'make' in sys.argv[-1].lower():
        try:
            preset.load_preset()['operation']
        except:
            KeyError
            TypeError
            preset.load_preset()['operation']
            preset_ver = input("Would you like to have a preset (y/n): ").lower()

            if preset_ver == 'y':
                preset.set_preset()
                if preset.load_preset()['operation'] == True:
                    clear()
                    print("Preset set successfully\n\n")

        vol = input('Pick a role below...\n\nd - Doctor\np - Patient\n\n > ').lower()
        if 'd' in vol:
            book_slot.create_doctor_event(service, calid)
        else:
            book_slot.book_vol_slot(service,calid)
        return
        book_slot.main(service)


    elif 'view' in sys.argv[-1].lower():
        x = view_calendar.main(service)


    elif 'cancel' in sys.argv[-1].lower():
        try:
            eventid, doc_or_pat = cancel_booking.get_eventid(service,username)
        except TypeError:
            # clear()
            print('No bookings to cancel\nIf certain check for spelling mistakes and formatting')
            return

        # print(eventid)
        clear()
        if 'd' in doc_or_pat:
            cancel_booking.doctor_cancellation(service,eventid,f'{username}@student.wethinkcode.co.za')
        else:
            cancel_booking.patient_cancellation(service,eventid,f'{username}@student.wethinkcode.co.za')
        
        
        
    elif sys.argv[-1].lower() == 'username':
        print(f"The current user is... {username}")
        verify = input("Is this you..?\n\n If it is press ENTER else enter a new username: ")
        if len(verify) == 0: #User pressed enter
            clear()
            if b'Login successful' in check_output_login(username):
                print(f"Welcome {username}\n\n\n")
        else:
            username = verify
            username_file = open(f"{os.environ['HOME']}/.config/.clinic/username.txt", 'w+')
            username_file.write(username)
            clear()
            print("Changing config file...")
            time.sleep(3)


    elif sys.argv[-1].lower() == 'interface':
        interface()


    elif 'logout' in sys.argv:
        clear()
        print("Already logged out of interface....")


if __name__ == "__main__":
    main()
    # set_preset()
    # book_slot.volunteer()
    # service = api_handler.main()
    # eventid_find(service)
    # book_slot.main()
    # print(book_slot.service)


