# from __future__ import print_function
# import datetime
# import os.path 
# import pickle
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# from datetime import timedelta
import pprint
#Creating The Methods for caldenar

#Clearing The Caldendar of all events
def clear_caldendar():
    clear_cal = service.calendars().clear('CalendarName').execute()


#Deleting a caldenar in your caldenar
def delete_calendar(service):
    del_calendar = {'summary:'}
    del_cal = service.calendars().delete(calendarId='Test').execute()

#Gets all the data of a caldenar like its Id, 
def add_calendar(service):#WORKS
    add_cal = service.calendars().get(calendarId='c_gqu6bu6k64sqshbg8e6nvmgpio@group.calendar.google.com').execute()
    print(add_cal['id'])
    print(add_cal['timeZone'])
    print(add_cal['summary'])
    # print(add_cal['location'])

# #Creating a new caldenar for calendar
def create_calendar(service):
    new_caldendar = {'summary':'test',#Summary is the Name of the Calendar
                     'Description': 'Test Calendar',#Describing the Calendar
                     'timeZone': '+02:00', #What Timezone should it be
                      'id': 'sigamede@student.wethinkcoce.co.za', 
                      'kind': 'calendar#calendar',} #The ID for the Calendar(reverited by calendar_data is the email of the user
    create_cal =  service.calendars().insert(body=new_caldendar,calendarId='Test').execute()


#Deleting a calendar CHECK
def deleting_calendar(service):
    delete_calendar = service.calendars().delete(calendarId='Test').execute()

#This is updating the details of the calendar
def updating_calendar_data(service):
    update_cal ={'Summary': 'testing', #Update to new name
                 'Description': 'Test Calendar New', #New Describing the nwew update
                 'id': 'testemail@student.wethinkcode.co.za',#To which calendar to update
                 'kind': 'calendar#calendar',
                 'timeZone': '+02:00',   }
    update = service.calendars().insert(body=update_cal,calendarId='email@gmail.co.za').execute()

def update_metadata_calendar(service):
    calendar = add_calendar(service)
    calendar['Summary'] = 'New Summary'
    # calendar['id'] = 'new_email@gmail.co.za' (if we want to update the id)
    #calendar['timeZone'] = 'Africa/Johnnesburg' (if we want to update the timezone)
    #calendar['desciption'] = 'new Desciption' (if we want to update the description)
    #calendar['kind'] = 'calendar#calendar'(This shouldn't change!!)

    metadata_update = service.calendars().update(calendarId=calendar['id'], body= calendar).execute()



# #Checking for the heads,labels in the calendar e.g calendarId,timezone etc
# def labels_calendar():
#     label_cal = service.calendarList().list().execute()
#     pprint(label_cal)
def calendar_lists(service):
    page_token = None
    while True:
        calendar_list = service.calendarList().list(pageToken=page_token).execute()
        for calendar_list_entry in calendar_list['items']:
            print (calendar_list_entry['id'])
            page_token = calendar_list.get('nextPageToken')
        if not page_token:
                break


#Clearing users all events
def clear_all_events():
    clear_cal_events =  service.calendars().clear('primary').execute()

#Gets all the metadata for calendar e.g 
def calendar_data(service):
    cal_data = service.calendars().get(calendarId='primary').execute()

    print(f"Summary: {cal_data['summary']}")
    print(f"CaldenarId: {cal_data['id']}")
    print(f"Timezone: {cal_data['timeZone']}")
    print(f"Kind:Type of resource: {cal_data['kind']}")
    print(f"ConferenceProperties: {cal_data['conferenceProperties']}")
    # print(cal_data['location'])
    print(f"etag: {cal_data['etag']}")
    with open('test.csv', 'w',newline='') as csvfile:
        fieldnames = ['id','status']
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'id':cal_data['id'],'status':cal_data['summary']})

#Deleting a event on a calendar,note we 
def deleting_event(service):
    del_event = service.events().delete(calendarId='primary',eventID= '6mbqvt0rkmjvskoukjtkv8etho').execute()

#Adding a insert to calendar

def add_event(service): #WORKS
    reponse = ['accepted','tenative','declined','needsAction']
    status = ['confirmed','cancelled']

    # if user == "Doc": 
    #     role = "writer"
    # elif user == "patient":
    #     role = "reader"

    #htmlLink-read-only can be used to show the events.....Therefore we pull the link from waht is created for doc then use that to show what is avaiable for the patients
    #'iconUri': 'https://media.giphy.com/media/3oKIPsx2VAYAgEHC12/giphy.gif'
    event_details_body = {
        'summary': 'Titleofevent',
        'description': 'This is a event',
        'start':{'dateTime':start.strftime("%Y-%m-%dT%H:%M:%S"),'timeZone':'+02:00',},
        'end':{'dateTime':end_time.strftime("%Y-%m-%dT%H:%M:%S"),'timeZone': '+02:00',},
        'attendees':[{'email':doc_email},],
        'reminders':{'useDefault': False,'overrides':[{'method': 'email','minutes': 24*60},{'method': 'popup','minutes':10},]},
        'anyCanAddSelf': False,
        ' organizer':{'id':'sigmede@student.wethinkcode',
                    'email': 'sigamede@student.wethinkcode.co.za',
                    'displayName':'Organiser Name'},
        'guestsCanInviteOthers': False,
        'creator':{'email': 'sigamede@student.wethinkcode.co.za',
                    'id':'sigamede@student.wehinkcode.co.za',
                    'displayName':'NameofCreator'},
    #Check 'entryPoints':[{'accessCode': '1234','label': 'video','password':'1234','pin':'1234'}],
        'notes': "Doctor to add notes",
        'guestsCanModify': False,
        'guestsCanSeeOtherGuest': True
        }
    
        #Must add the Error 403 This is for Calendar ID
        #Must add the Error 400 This is for API Key
        #Error 404: The request is missing a valid API key.

        #When creating a 

    
    event = service.events().insert(calendarId='primary',body= event_details_body,maxAttendees=2,sendNotifications = True,sendUpdates = 'all').execute()

#deleting a event     
def deleting_event(service,eventid):
    del_event =service.events().delete(calendarId='sigamede@student.wethinkcode.co.za',eventId=eventid,sendNotifications=True,sendUpdates='all')
    return del_event
    # This will delete the event requested via the eventID then send Notifications to the attendees and a update 

#returning events from specified calendar
def events_on_calendar(service):
    events_cal = service.events().list(calendarId='sigamede@student.wethinkcode.co.za',summary='JHH').execute()
    pprint.pprint(events_cal)    

def get_event(service,eventid):
    get_event = service.events().get(calendarId='primary',eventId=eventid).execute()
  

def patient_cancellation(service,attendee,eventID,data):
    if data['email'] == attendee:
        data['email'] = ''
    print("Hello")
    updating = service.events().update(calendarId='primary',eventId=eventID,body=data,sendNotifications=True,sendUpdates='all').execute()
    return update






#Importing a private copy of a event: The event must allow for this to happen
def import_event(service):
    import_body = { ' '

    }    





# print created_rule['id']
# {
#     "role": "A String", # The role assigned to the scope. Possible values are:
#         # - "none" - Provides no access.
#         # - "freeBusyReader" - Provides read access to free/busy information.
#         # - "reader" - Provides read access to the calendar. Private events will appear to users with reader access, but event details will be hidden.
#         # - "writer" - Provides read and write access to the calendar. Private events will appear to users with writer access, and event details will be visible.
#         # - "owner" - Provides ownership of the calendar. This role has all of the permissions of the writer role with the additional ability to see and manipulate ACLs.
#     "id": "A String", # Identifier of the ACL rule.
#     "scope": { # The scope of the rule.
#       "type": "A String", # The type of the scope. Possible values are:
#           # - "default" - The public scope. This is the default value.
#           # - "user" - Limits the scope to a single user.
#           # - "group" - Limits the scope to a group.
#           # - "domain" - Limits the scope to a domain.  Note: The permissions granted to the "default", or public, scope apply to any user, authenticated or not.
#       "value": "A String", # The email address of a user or group, or the name of a domain, depending on the scope type. Omitted for type "default".
#     },
#     "etag": "A String", # ETag of the resource.
#     "kind": "calendar#aclRule", # Type of the resource ("calendar#aclRule").
#   }

#   sendNotifications: boolean, Whether to send notifications about the calendar sharing change. Optional. The default is True.




# def rule_patient():
#    rule = {
#     'scope': {
#         'type': 'user',
#         'value': 'attendeeemail',
#     },
#     'role': 'reader'
#     }

#     created_rule = service.acl().insert(calendarId='primary', body=rule).execute()
#     return created_rule

# def rule_doctor():
#        rule = {
#     'scope': {
#         'type': 'user',
#         'value': 'doc_email',
#     },
#     'role': 'owner'
#     }

#     created_rule = service.acl().insert(calendarId='primary', body=rule).execute()
#     return created_rule
    



#Creating permissions  for events
def doc_permissions ():
    pass





def patient_permissions():
    pass   




