#THIS MODULE IS MEANT FOR CANCELLATION OF BOOKINGS

import Calendar_Commands
import input_cc_.input_API as input_API

cancel =  input("Cancel event?(yes/no)")
cancel.lower()

def deleting_event(service,eventID):
    del_event = service.events().delete(calendarId='primary',eventId= eventID).execute()

def patient_cancellation(service,attendee,eventID):
    data = Calendar_Commands.get_event(service)
    if data['email'] == attendee:
        data['email'] = ''
    update = service.events().update(calendarId='primary',eventId=eventID).execute()
    return update


if cancel == 'yes' and input_API.book_doctor in doctor_list = ["apillay", "bidaniel", "cdu-pree", "fmokoena", "mbjali", "ndumasi"]:
    deleting_event(service)

elif cancel == "yes" and input_API.book_patient in patient_list = ["nwalter", "Sigamede", "tmoshole", "vpekane", "Vsithole", "sbaloyi"]:
    update_metadata_calendar(service)
    
   