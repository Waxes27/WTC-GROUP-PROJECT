from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


EVENTS:

events.insert(params)
THIS NEEDS THE SCOPE TO FUNCTION
# event is the event to create with all the necessary details such as start and end. The only two required fields are the start and end times.
"""
This creates events
 - params
    calendarId=primary ---> this priorities the calendar of the logged in user

    If you don't know the email address of the calendar you would like to use:
        >> use  calendarList.list()

"""
events.update()
"""
is used to update update fields

EXAMPLE

event = {
  'summary': 'Google I/O 2015',
  'location': '800 Howard St., San Francisco, CA 94103',
  'description': 'A chance to hear more about Google\'s developer products.',
  'start': {
    'dateTime': '2015-05-28T09:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'end': {
    'dateTime': '2015-05-28T17:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'recurrence': [
    'RRULE:FREQ=DAILY;COUNT=2'
  ],
  'attendees': [
    {'email': 'lpage@example.com'},
    {'email': 'sbrin@example.com'},
  ],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}

event = service.events().insert(calendarId='primary', body=event).execute()
print 'Event created: %s' % (event.get('htmlLink'))
"""







Creating Recurring events

# Creating recurring events is similar to creating a regular (single) event with the event resource's recurrence field set.

"""
event = {
  'summary': 'Appointment',
  'location': 'Somewhere',
  'start': {
    'dateTime': '2011-06-03T10:00:00.000-07:00',
    'timeZone': 'America/Los_Angeles'
  },
  'end': {
    'dateTime': '2011-06-03T10:25:00.000-07:00',
    'timeZone': 'America/Los_Angeles'
  },
  'recurrence': [
    'RRULE:FREQ=WEEKLY;UNTIL=20110701T170000Z',
  ],
  'attendees': [
    {
      'email': 'attendeeEmail',
      # Other attendee's data...
    },
    # ...
  ],
}

recurring_event = service.events().insert(calendarId='primary', body=event).execute()

print recurring_event['id']
"""



Accessing instances:
"""
To see all the instances of a given recurring event you can use the events.instances() request.
"""

#The events.list() request by default only returns single events

"""
The following event fields are specific to instances:

recurringEventId — the ID of the parent recurring event this instance belongs to
originalStartTime — the time this instance starts according to the recurrence data in the parent recurring event. This can be different from the actual start time if the instance was rescheduled. It uniquely identifies the instance within the recurring event series even if the instance was moved.

"""

Modifying or deleting instances:
"""
To modify a single instance (creating an exception), client applications must first retrieve the instance and then update it by sending an authorized PUT request to the instance edit URL with updated data in the body. The URL is of the form:

https://www.googleapis.com/calendar/v3/calendars/calendarId/events/instanceId




Actual editing:

# First retrieve the instances from the API.
instances = service.events().instances(calendarId='primary', eventId='recurringEventId').execute()

# Select the instance to cancel.
instance = instances['items'][0]
instance['status'] = 'cancelled'

updated_instance = service.events().update(calendarId='primary', eventId=instance['id'], body=instance).execute()

# Print the updated date.
print updated_instance['updated']
"""















SYNCING DATA:
"""
Initial full sync
The initial full sync is the original request for all the resources of the collection you want to synchronize. You can optionally restrict the list request using request parameters if you only want to synchronize a specific subset of resources.

In the response to the list operation, you will find a field called nextSyncToken representing a sync token. You'll need to store the value of nextSyncToken. If the result set is too large and the response gets paginated, then the nextSyncToken field is present only on the very last page
"""