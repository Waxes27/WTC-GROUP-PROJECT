<<<<<<< HEAD
<<<<<<< HEAD
#THIS MODULE IMPORTS AND ACTS AS THE MAIN CODEBASE


<<<<<<< HEAD

def get_token():

    creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        ####when user credentials exist
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
                # creds = flow.run
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service
=======
import help_cc
import input_cc

<<<<<<< HEAD
>>>>>>> refs/remotes/origin/sbaloyi
=======
>>>>>>> 4224549412079187620e793d0bfd733f67ccdf62
>>>>>>> Playground
=======
#THIS MODULE IMPORTS AND ACTS AS THE MAIN CODEBASE
>>>>>>> Playground
=======
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
>>>>>>> Playground
