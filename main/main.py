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
