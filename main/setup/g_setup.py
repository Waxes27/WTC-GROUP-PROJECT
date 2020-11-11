import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

def main():
    CRED= None
    #CREDENTIALS_FILE = 'WTC-GROUP-PROJECT/credentials.json'
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            #CREDENTIALS_FILE = pickle.load(token)
            CRED = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not CRED or not CRED.valid:
        if CRED and CRED.expired and CRED.refresh_token:
            CRED.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '../credentials.json', SCOPES)
            CRED = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(CRED, token)

    service = build('calendar', 'v3', credentials=CRED)

    return service

if __name__ == "__main__":
    main()