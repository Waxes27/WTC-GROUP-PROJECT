import datetime
import view_calendar as view_calendar


def write_icalendar_file_text(text):
    """
    Write the details from the slot events to the my_calendar.isc iCal file
    """

    opened_file = open("my_calendar.ics", "a+")
    opened_file.writelines(text)
    opened_file.close()  


def v_calendar_data(username):

    text = '''BEGIN:VCALENDAR
PRODID:-//Google Inc//Google Calendar 70.9054//EN
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:''' + username + '''@student.wethinkcode.co.za
X-WR-TIMEZONE:Africa/Johannesburg
BEGIN:VTIMEZONE
TZID:Africa/Johannesburg
X-LIC-LOCATION:Africa/Johannesburg
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0200
TZNAME:SAST
DTSTART:19700101T000000
END:STANDARD
END:VTIMEZONE
'''
    return text


def convert_tel(tel_number):
    """
    This function converts the tel_number from events to the iCal format, so
    that it will be easier to read.
    """

    tel_number = tel_number.split(':')
    tel_number.pop(0)
    tel_number = ' '.join(tel_number).replace('-',' ')
    return tel_number


def convert_date(even_date):
    """
    This function converts the dates from events to the iCal format, so
    that it will be easier to read.
    """
    
    even_date.pop(1)
    even_date = ' '.join(even_date).replace('-','').split()
    even_date = ' '.join(even_date).replace(':','').split()
    if len(even_date) > 1:
        even_date.insert(1, 'T')
    even_date.append('Z')
    even_date = ''.join(even_date)
    return even_date


def extract_event(event_dict):

    """
    This function extracts the event's data, assign it to variables
    and add details to make it more meaningful to the iCal.
    """


    for dict_event in event_dict:
        start_date = dict_event['start'].get('dateTime').split("+")
        end_date = dict_event['end'].get('dateTime').split("+")
        stamp_date = str(datetime.datetime.now())
        stamp_date = stamp_date.split(".")
        organizer = dict_event['organizer'].get('email')
        event_uid = dict_event['iCalUID']
        event_attendee = dict_event['attendees']
        event_attendee_1 = event_attendee[0].get('email')
        attendee_1_response = (event_attendee[0].get('responseStatus')).upper()
        if len(event_attendee) > 1:
            event_attendee_2 = event_attendee[1].get('email')
            attendee_2_response = (event_attendee[1].get('responseStatus')).upper()
        else:
            event_attendee_2 = 'none'
            attendee_2_response = 'none'

        creation_date = dict_event['created'].split(".")
        last_mod_date = 0
        event_location = 0
        event_sequance = 0
        event_status = 0
        event_summary = dict_event['summary']
        event_transp = 0
        if 'conferenceData' in dict_event:
            conferenceData = dict_event['conferenceData']

            entryPoints = conferenceData['entryPoints']
            google_meets_link =  entryPoints[0].get('uri')
            tel_number = entryPoints[2].get('uri')
            event_pin = entryPoints[2].get('pin')
            uri_tel = entryPoints[1].get('uri')

        else:
            print ('no data')

            entryPoints = 'none'
            google_meets_link =  'none'
            tel_number = 'none'
            event_pin = 'none'
            uri_tel = 'none'



        start_date = 'DTSTART:' + convert_date(start_date)
        end_date = 'DTEND:' + convert_date(end_date)
        stamp_date = 'DSTAMP:' + convert_date(stamp_date)
        organizer = 'ORGANIZER;CN=' + organizer + ':mailto:' + organizer
        event_uid = 'UID:' + event_uid
        event_attendee_1 = 'ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-PARTICIPANT;PARTSTAT=' + \
        attendee_1_response + ';CN=' + event_attendee_1 + ';X-NUM-GUESTS=0:mailto:' + event_attendee_1
        event_attendee_2 = 'ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-PARTICIPANT;PARTSTAT=' + \
        attendee_2_response + ';CN=' + event_attendee_2 + ';X-NUM-GUESTS=0:mailto:' + event_attendee_2
        creation_date = 'CREATED:' + convert_date(creation_date)
        tel_number = convert_tel(tel_number)
        event_summary = 'SUMMARY:' + event_summary
        if entryPoints == 'none':
            event_description = 'DESCRIPTION:This event has no video call.'
        elif entryPoints[0].get('entryPointType')  == 'video':
            event_description = 'DESCRIPTION:This event has a video call.\nJoin:\
' + google_meets_link + '\n(ZA) '+ tel_number +' PIN:\
'+ event_pin +'#\nView more phone numbers: ' + uri_tel +'&hs=7'
        else: 
            event_description = 'DESCRIPTION:This event has no video call.'


        write_icalendar_file_text('BEGIN:VEVENT\n' + start_date + '\n' + end_date + '\n\
' + str(stamp_date) + '\n' + organizer + '\n' + event_uid + '\n' + event_attendee_1 + '\n\
' + event_attendee_2 + '\n' + creation_date + '\n' + event_description + '\n\
' + event_summary + '\n' + 'END:VEVENT' + '\n')

    write_icalendar_file_text('END:VCALENDAR')

def main():
    service = view_calendar.get_service()
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time

    events = view_calendar.get_events(service, now)

    username = 'vsithole'

    text = v_calendar_data(username)

    write_icalendar_file_text(text)

    extract_event(events)

if __name__ == '__main__':
    main()
    