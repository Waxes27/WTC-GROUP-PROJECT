import os
import sys
import code
import code.help_cc_.help_cc as help_cc
import code.codebase.book_slot as book_slot
import code.view_calendar_cc.view_calendar as view_calendar
import code.cancel_booking_.cancel_booking as cancel_booking
import code.api_handler.api_handler as api_handler
import code.codebase.preset as preset
import code.codebase.event as event
import tkinter as tk
from tkinter import ttk ,messagebox
from datetime import timedelta
import subprocess
import datetime


event_sl = []
doc = False

def clear():
    os.system('clear')

def LogIn(sidebar,frame,main_frame,username,service,calid):
    for bu in main_frame.winfo_children():
        if str(bu)[:16] == ".!frame2.!button" :
            bu.destroy()
    for label in sidebar.winfo_children():
        label.destroy()
    for widget in frame.winfo_children():
        widget.destroy()

    main_frame.configure(bg="azure")
    log = tk.Label(master=sidebar, relief=tk.FLAT,justify='center', bd =1, text="LogIn", bg="azure")
    log.place(relx=0,rely=0.37,relwidth=1,relheight=0.25)
    log.config(font=("Courier", 30))

    # stuff = []
    frame0 = tk.Frame(master=frame,borderwidth=1)
    frame0.pack(fill = "both",expand=1,pady=2)
    frame1 = tk.Frame(master=frame,borderwidth=1)
    frame1.pack(fill = "both",expand=1,pady=2)
    frame2 = tk.Frame(master=frame,borderwidth=1)
    frame2.pack(fill = "both",expand=1,pady=2)

    user = tk.Label(master=frame0, relief=tk.FLAT,justify='center', bd =1, text="UserName : ", bg="azure")
    user.pack(side="left")
    user.config(font=("Helvetica", 10))
    user_in = tk.Entry(master=frame0, relief=tk.SUNKEN,bd = 1)
    user_in.pack()
    v = tk.IntVar(master = frame1)
    check1 = tk.Radiobutton(frame1, text="Doctor",variable = v,value = 1)
    check1.pack(side = "left")
    check2 = tk.Radiobutton(frame1, text="Patient",variable = v, value = 2 )
    check2.pack(side = "right")
    confirm = tk.Button(master=frame2 ,text='Login',justify='center', activebackground="silver",command= lambda:pick(service,calid,v,user_in,sidebar,frame,main_frame))
    confirm.pack(side = "right")

    if username:
        user_in.insert(tk.END,username)

def pick(service,calid,variable,user,sidebar,frame,main_frame):
    for widget in frame.winfo_children():
        if str(widget)[:30] == ".!frame2.!canvas.!frame.!label":
            widget.destroy()
                   
    if user.get():
        # print(user.get())
        slots = get_slots(service,calid)
        username = user.get()
        
        if b'Login successful' in check_output_login(username):
            if variable.get() == 1:
                doctor(slots,service,sidebar,frame,main_frame,username,True,calid)
            else:
                patient(slots,service,sidebar,frame,main_frame,username,False,calid)

        else:
            username_file = open(f"{os.environ['HOME']}/.config/.clinic/username.txt", 'w+')
            username_file.write(username)
            check_output_login(username)

            invalid =  tk.Label(master=frame, relief=tk.FLAT,justify='center', text="Please enter a valid UserName")
            invalid.pack()

def check_output_login(username):
    try:
        value = subprocess.check_output("wtc-lms login", shell=True)
    except subprocess.CalledProcessError as e:
        clear()
        value = failed_authentication(username)

    return value

def failed_authentication(username):
    conf(username)
    value = check_output_login(username)
    return value

def conf(username):
    os.system(f"""echo "---
    editor: code
    repo_path: ~/problems
    navigator_url: "https://navigator.wethinkcode.co.za"
    username: {username}@student.wethinkcode.co.za
    review_manager_url: "https://review-manager.wethinkcode.co.za"
    keycloak_url: "https://keycloak.wethinkcode.co.za"" > ~/.config/wtc/config.yml""")


def main_gui(service,username,calid):
    wind = tk.Tk()
    wind.title("The Code Clinic")
    wind.geometry('1000x500')

    sidebar = tk.Frame(master=wind, borderwidth=0,bg="azure")
    sidebar.place(relx=0,rely=0,relwidth=0.25,relheight=1)

    main_frame = tk.Frame(master=wind, borderwidth=2)
    main_frame.place(relx=0.25,rely=0,relwidth=0.75,relheight=1)

    container = tk.Canvas(master=main_frame)
    frame = tk.Frame(master=container)
    scrolly = ttk.Scrollbar(master=main_frame,orient= 'vertical', command=container.yview)
    scrollx = ttk.Scrollbar(master=main_frame,orient= 'horizontal', command=container.xview)
    container.configure(yscrollcommand= scrolly.set, xscrollcommand= scrollx.set)

    scrolly.pack(side='right', fill='y') 
    scrollx.pack(side='bottom', fill='x') 
    frame.pack(fill="both", expand=1, anchor="nw")
    container.pack(fill="both",expand=1)
    container.create_window((0,0) , window=frame)
    frame.bind('<Configure>',lambda e: container.configure(scrollregion = container.bbox("all")))

    LogIn(sidebar,frame,main_frame,username,service,calid)
    
    wind.mainloop()


def doctor(slots,service,sidebar,frame,main_frame,username,doc,calid):
    for bu in main_frame.winfo_children():
        if str(bu)[:16] == ".!frame2.!button" :
            bu.destroy()
    for label in sidebar.winfo_children():
        label.destroy()
    for widget in frame.winfo_children():
        widget.destroy()

    main_frame.configure(bg="red")
    labe1 = tk.Label(master=sidebar, relief=tk.SUNKEN,justify='center', bd =1, text="Doctor", bg="red")
    labe1.place(relx=0,rely=0,relwidth=1,relheight=0.15)
    labe1.config(font=("Courier", 30))
    button1 = tk.Button(master=sidebar ,text='View Calendar',justify='center', activebackground="silver",command= lambda: view_cal(slots,frame,main_frame))
    button1.place(relx=0,rely=0.15,relwidth=1,relheight=0.17)
    button2 = tk.Button(master=sidebar ,text='Make Slot',justify='center', activebackground="teal",command= lambda: make_slot(slots,frame,main_frame))
    button2.place(relx=0,rely=0.32,relwidth=1,relheight=0.17)
    button3 = tk.Button(master=sidebar ,text='Cancel Slot',justify='center', activebackground="medium purple",command= lambda: cancel_book(slots,username,service,frame,main_frame,doc))
    button3.place(relx=0,rely=0.49,relwidth=1,relheight=0.17)
    button4 = tk.Button(master=sidebar ,text='Help',justify='center',command= lambda: help_(slots,frame,main_frame))
    button4.place(relx=0,rely=0.66,relwidth=1,relheight=0.17)
    button5 = tk.Button(master=sidebar ,text='LogOut',justify='center',command= lambda: log_out(slots,sidebar,frame,main_frame,username,service,calid))
    button5.place(relx=0,rely=0.83,relwidth=1,relheight=0.17)


def patient(slots,service,sidebar,frame,main_frame,username,doc,calid):
    for bu in main_frame.winfo_children():
        if str(bu)[:16] == ".!frame2.!button" :
            bu.destroy()
    for label in sidebar.winfo_children():
        label.destroy()
    for widget in frame.winfo_children():
        widget.destroy()

    main_frame.configure(bg="blue")
    labe1 = tk.Label(master=sidebar, relief=tk.SUNKEN,justify='center', bd =1, text="Patient", bg="blue")
    labe1.place(relx=0,rely=0,relwidth=1,relheight=0.15)
    labe1.config(font=("Courier", 30))
    button1 = tk.Button(master=sidebar ,text='View Calendar',justify='center', activebackground="silver",command= lambda: view_cal(slots,frame,main_frame))
    button1.place(relx=0,rely=0.15,relwidth=1,relheight=0.17)
    button2 = tk.Button(master=sidebar ,text='Make Booking',justify='center', activebackground="teal",command= lambda: book_(slots,frame,main_frame,calid ,service, username))
    button2.place(relx=0,rely=0.32,relwidth=1,relheight=0.17)
    button3 = tk.Button(master=sidebar ,text='Cancel Booking',justify='center', activebackground="medium purple",command= lambda: cancel_book(slots,username,service,frame,main_frame,doc))
    button3.place(relx=0,rely=0.49,relwidth=1,relheight=0.17)
    button4 = tk.Button(master=sidebar ,text='Help',justify='center',command= lambda: help_(slots,frame,main_frame))
    button4.place(relx=0,rely=0.66,relwidth=1,relheight=0.17)
    button5 = tk.Button(master=sidebar ,text='LogOut',justify='center',command= lambda: log_out(slots,sidebar,frame,main_frame,username,service,calid))
    button5.place(relx=0,rely=0.83,relwidth=1,relheight=0.17)

    
def get_slots(service,calid):
    slots = []
    # calid = 'c_4pa2luaf52rfdc8f0tn05bf1qo@group.calendar.google.com'
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    events_result = service.events().list(calendarId=calid , timeMin=now,
                                        maxResults=100, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No available slots found.')
        # get_slots(service,calid)

    for google_cal in events:  

        s = google_cal['start'].get('dateTime').split("+")
        date_s = s[0].split("T")
        e = google_cal['end'].get('dateTime').split("+")
        date_e = e[0].split("T")

        try:
            # if google_cal['summary'] == "General" or google_cal['summary'] == "Recursion"\
            #     or google_cal['summary'] == "Unittesting" or \
            #     google_cal['summary'] == "List Comprehensions" or google_cal['summary'] == "Lambdas":
            
            doctor_email = google_cal['creator']['email']
            doctor_user = doctor_email.split('@')
                
            if google_cal.get("attendees") == None:
                guest_user = "Available"
            else:
                guest_email = google_cal['attendees'][0]['email']
                user_email = guest_email.split('@')
                guest_user = user_email[0]
        
            slots.append("id: " +google_cal['id'] + "\n" + "date: " + date_s[0] + "\n" + 'start_time: '+ date_s[1][:5] + "\n" + 'end_time: '+ date_e[1][:5] + "\n" + 'topic: ' +google_cal['summary'] + "\n" + 'doctor: ' + doctor_user[0]  + "\n" + 'patient: ' + guest_user.ljust(10))

        except KeyError as e:
            print(e)           

    return slots

def sloots(slots):
    sloots = []
    
    for i in range(len(slots)):
        if i != 0:
            slot = slots[i].split("\n")
            # sl1 = slot[2].replace("Start Time: ","")
            sl1 = slot[2].split(':')
            sl2 = slot[3].split(':',1)
            date = slot[1].split(':')
            date.pop(0)
            date = date[0].split('-')
            
            tim = datetime.datetime(int(date[0][:6]),int(date[1]),int(date[2]),int(sl1[1][1:]),int(sl1[2]))

            slo = []
        
            while str(tim)[11:][:5] != sl2[1][1:] and str(tim)[11:][:5] <= sl2[1][1:] :
                # print(f"this is s_l2{sl2}")
                # print(str(tim)[11:][:5] )
                slo.append(f"{str(tim)[11:][:5]} : {str(tim + timedelta(hours=0.5))[11:][:5]}")
                tim = (tim + timedelta(hours=0.5))
            slo.append('pick a slot')
            sloots.append(slo)

    return(sloots)
   

def view_cal(slots,frame,main_frame):

    for bu in main_frame.winfo_children():
        if str(bu)[:16] == ".!frame2.!button" :
            bu.destroy()
    for widget in frame.winfo_children():
        widget.destroy()

    frame.configure(bg="gray")
    week = get_dates(8)
    # sloot = sloots(slots)
    stuff = []
    for da in range(len(week)):
        used = False
        fr_= f"""
frame{da} = tk.Frame(master=frame,borderwidth=1, bg= 'white smoke')
frame{da}.pack(fill = "both",pady=2)
stuff.append(frame{da})
"""
        exec(fr_)
        make_fr = stuff[-1]
    
        can_1 = tk.Frame(master=make_fr,relief=tk.FLAT,borderwidth=0, bg= "white smoke")
        can_1.pack(fill ="both",expand=1,anchor="nw")
        la = tk.Label(master=can_1, relief=tk.RIDGE, bd =1, text=f"Date : {week[da]}", bg="silver")
        la.pack(fill = "both",pady= 2)
        can_2 = tk.Frame(master=make_fr,relief=tk.FLAT,borderwidth=0, bg= "white smoke")
        can_2.pack(fill ="both",expand=1)

        for i in range(len(slots)):
            slot = slots[i].split("\n")
            # if slot[0].split(':',1)[0] == "ID" :
            slot.remove(slot[0])


            if slot[0].split(': ',1)[1] == week[da]:
                slot.remove(slot[0])
                cal(da,can_2,slot,week,i)
                used = True

            elif used == False and i == len(slots) - 1:
                minion = tk.Frame(master=can_2,relief=tk.FLAT,borderwidth=0, bg= "white smoke")
                minion.grid(row=0, column=0, padx=5, pady=2)
               
                lab = tk.Label(master=minion, text="No bookings made today", bg="white smoke")
                lab.pack(fill = "both",expand = 1)
                used = True


def make_slot(slots,frame,main_frame):
    for bu in main_frame.winfo_children():
        if str(bu)[:16] == ".!frame2.!button" :
            bu.destroy()
    for widget in frame.winfo_children():
        widget.destroy()
    frame.configure(bg="green")

    inf_ = []
    frame0 = tk.Frame(master=frame,borderwidth=1, bg= 'honeydew')
    frame0.pack(fill = "both",pady=2)
    frame1 = tk.Frame(master=frame,borderwidth=1, bg= 'honeydew')
    frame1.pack(fill = "both",pady=2)
    frame2 = tk.Frame(master=frame,borderwidth=1, bg= 'honeydew')
    frame2.pack(fill = "both",pady=2)
    frame3 = tk.Frame(master=frame,borderwidth=1, bg= 'honeydew')
    frame3.pack(fill = "both",pady=2)
    frame4 = tk.Frame(master=frame,borderwidth=1, bg= 'honeydew')
    frame4.pack(fill = "both",pady=2)
    frame5 = tk.Frame(master=frame,borderwidth=1, bg= 'honeydew')
    frame5.pack(fill = "both",pady=2)

    top_lab = tk.Label(master = frame0, text = "Topic", bg= 'honeydew')
    top_lab.pack(side = "left")
    topic = tk.Entry(master=frame0, relief=tk.SUNKEN,bd = 1)
    topic.pack(side = "right")
    inf_.append(topic)

    dura_lab = tk.Label(master = frame1, text = "Room", bg= 'honeydew')
    dura_lab.pack(side = "left")
    dura = tk.Entry(master=frame1, relief=tk.SUNKEN,bd = 1)
    dura.pack(side = "right")
    inf_.append(dura)

    dat_lab = tk.Label(master = frame2, text = "Year", bg= 'honeydew')
    dat_lab.pack(side = "left")
    dat_= tk.Entry(master=frame2, relief=tk.SUNKEN,bd = 1)
    dat_.pack(side = "right")
    inf_.append(dat_)

    star_lab = tk.Label(master = frame3, text = "Month",bg= 'honeydew')
    star_lab.pack(side = "left")
    start_ti = tk.Entry(master=frame3, relief=tk.SUNKEN,bd = 1)
    start_ti.pack(side = "right")
    inf_.append(start_ti)

    star_lab = tk.Label(master = frame4, text = "Day",bg= 'honeydew')
    star_lab.pack(side = "left")
    start_ti = tk.Entry(master=frame4, relief=tk.SUNKEN,bd = 1)
    start_ti.pack(side = "right")
    inf_.append(start_ti)

    star_lab = tk.Label(master = frame5, text = "Time",bg= 'honeydew')
    star_lab.pack(side = "left")
    start_ti = tk.Entry(master=frame5, relief=tk.SUNKEN,bd = 1)
    start_ti.pack(side = "right")
    inf_.append(start_ti)



    button = tk.Button(master=main_frame ,text='Done',bg="honeydew",justify='center',command= lambda : birth_slot(frame,inf_))
    button.pack(fill = "both")


def birth_slot(frame , inf_):
    for widget in frame.winfo_children():
        # print(widget)
        if str(widget)[:30] == ".!frame2.!canvas.!frame.!label":
            widget.destroy()
    slot_time = ""

    field = ["Topic","Room","Year","Month","Day","Time"]
    for r in range(len(inf_)):
        if inf_[r].get():
            if r == 0:
                topic = inf_[r].get()
            elif r == 1:
                room = inf_[r].get()
            else:
                slot_time = slot_time + " " + inf_[r].get()
        else:
            invalid =  tk.Label(master=frame, relief=tk.FLAT,justify='center', text=f"Please enter a valid {field[r]}")
            invalid.pack(fill="both",expand= 1)

   
    if book_slot.is_slot_avalaible(calid,service, slot_time):
        book_slot.volunteer(service,calid,slot_time,topic,room)
    else:
        inval =  tk.Label(master=frame, relief=tk.FLAT,justify='center', text="A slot has already been made for this time")
        inval.pack(fill="both",expand= 1)

def book_(slots,frame,main_frame,calid ,service, username):

    for bu in main_frame.winfo_children():
        if str(bu)[:16] == ".!frame2.!button" :
            bu.destroy()
    for widget in frame.winfo_children():
        widget.destroy()
    frame.configure(bg="green")
    week = get_dates(8)
    sloot = sloots(slots)
    stuff = []
    for da in range(len(week)):
        used = False
        fr_= f"""
frame{da} = tk.Frame(master=frame,borderwidth=1, bg= 'honeydew')
frame{da}.pack(fill = "both",pady=2)
stuff.append(frame{da})
"""
        exec(fr_)
        make_fr = stuff[-1]
    
        can_1 = tk.Frame(master=make_fr,relief=tk.FLAT,borderwidth=0, bg= "honeydew")
        can_1.pack(fill ="both")
        la = tk.Label(master=can_1, relief=tk.RIDGE, bd =1, text=f"Date : {week[da]}", bg="teal")
        la.pack(fill = "both",pady= 2)
        can_2 = tk.Frame(master=make_fr,relief=tk.FLAT,borderwidth=0, bg= "honeydew")
        can_2.pack(fill ="both")

        for i in range(len(slots)):
            slot = slots[i].split("\n")
            # if slot[0].split(':',1)[0] == "ID" :
            slot.remove(slot[0])


            if slot[0].split(': ',1)[1] == week[da]:
                slot.remove(slot[0])
                make_bk(da,can_2,slot,week,sloot,i)
                used = True

            elif used == False and i == len(slots) - 1:
                minion = tk.Frame(master=can_2,relief=tk.FLAT,borderwidth=0, bg= "honeydew")
                minion.grid(row=0, column=0, padx=5, pady=2)
               
                lab = tk.Label(master=minion, text="No Slots Available", bg="honeydew")
                lab.pack(fill = "both",expand = 1)
                used = True


    button = tk.Button(master=main_frame ,text='Book',bg="honeydew",justify='center',command= lambda : callback(slots,calid,service,username))
    button.pack(fill = "both")

def cancel_book(slots,username,service,frame,main_frame,doc):
    for bu in main_frame.winfo_children():
        if str(bu)[:16] == ".!frame2.!button" :
            bu.destroy()
    for widget in frame.winfo_children():
        widget.destroy()

    frame.configure(bg="indigo")
    week = get_dates(8)
    # sloot = sloots(slots)
    stuff = []
    for da in range(len(week)):
        used = False
        fr_= f"""
frame{da} = tk.Frame(master=frame,borderwidth=1, bg= 'lavender')
frame{da}.pack(fill = "both",pady=2)
stuff.append(frame{da})
"""
        exec(fr_)
        make_fr = stuff[-1]
    
        can_1 = tk.Frame(master=make_fr,relief=tk.FLAT,borderwidth=0, bg= "lavender")
        can_1.pack(fill ="both",expand=1,anchor="nw")
        la = tk.Label(master=can_1, relief=tk.RIDGE, bd =1, text=f"Date : {week[da]}", bg="medium purple")
        la.pack(fill = "both",pady= 2)
        can_2 = tk.Frame(master=make_fr,relief=tk.FLAT,borderwidth=0, bg= "lavender")
        can_2.pack(fill ="both",expand=1)

        for i in range(len(slots)):
            slot = slots[i].split("\n")
            # if slot[0].split(':',1)[0] == "ID" :
            slot.remove(slot[0])


            if slot[0].split(': ',1)[1] == week[da]:
                slot.remove(slot[0])
                can_book(da,can_2,slot,week,i,slots,frame,main_frame,service,username,doc)
                used = True

            elif used == False and i == len(slots) - 1:
                minion = tk.Frame(master=can_2,relief=tk.FLAT,borderwidth=0, bg= "lavender")
                minion.grid(row=0, column=0, padx=5, pady=2)
               
                lab = tk.Label(master=minion, text="No bookings made today", bg="lavender")
                lab.pack(fill = "both",expand = 1)
                used = True


def help_(slots,frame,main_frame):
    for bu in main_frame.winfo_children():
        if str(bu)[:16] == ".!frame2.!button" :
            bu.destroy()
    for widget in frame.winfo_children():
        widget.destroy()

    text_ = tk.Text(master= frame, height = 25, width = 50) 
    h = """
Make Booking  : view and book availble time slots,

View Calendar : view Calendar events,

Cancel Booking : cancel booking,

Make Slot : create time slot,

Cancel Slot : cancel time slot
"""
    text_.insert(tk.END, h)
    text_.configure(state='disabled')
    text_.pack(fill ="both",expand = 1)


def log_out(slots,sidebar,frame,main_frame,username,service,calid):
    for bu in main_frame.winfo_children():
        if str(bu)[:16] == ".!frame2.!button" :
            bu.destroy()
    for widget in frame.winfo_children():
        widget.destroy()
    
    frame.configure(bg="#F0F0F0")
    tex = f"Are you sure you want to LogOut..."
    mess = messagebox.askyesno(title= "Log Out", message= tex,default="no")
    if mess == True:
        LogIn(sidebar,frame,main_frame,username,service,calid)


def callback(slots,calid,service,username):
    global event_sl
    for v in range(len(event_sl)):
        if event_sl[v].get() != "pick a slot":
            # print(event_sl[v].get())
            s = slots[v].split("\n")
            start_time = (s[2].split(": ",1))[1]
            end_time = (s[3].split(": ",1))[1]
            slot_topic = (s[4].split(": ",1))[1]
            doctor = (s[5].split(": ",1))[1]
            room = '5th floor kitchen area'
            event.event(service, calid,username, slot_topic, start_time, end_time, doctor, room)

    # return s,v


def get_dates(x):
    dates_week = []
    day_to = datetime.datetime.now()
    last_day = day_to + timedelta(days = int(x))
        
    while day_to != last_day:
        dates_week.append(day_to.strftime("%F"))
        day_to = day_to + timedelta(days = 1)
    
    return(dates_week)


def cal(da,can_2,slot,week,i):

    for j in range(5):
        can_2.columnconfigure(j, weight=1)
        minion = tk.Frame(master=can_2,relief=tk.RIDGE,borderwidth=1, bg= "white smoke")
        minion.grid(row=0, column=j,padx=5, pady=2, sticky="nsew")
        try:
            lab = tk.Label(master=minion, text=f"{slot[j].split(':',1)[0]}", bg="white smoke")
            lab.pack(fill = "both",pady = 2)
        except IndexError:
            lab = tk.Label(master=minion, text= "Slots", bg="white smoke")
            lab.pack(fill = "both",pady = 2)

        minion = tk.Frame(master=can_2,relief=tk.FLAT,borderwidth=1, bg= "floral white",highlightthickness=1,highlightbackground="black")
        minion.grid(row=i+1, column=j,padx=0, pady=0, sticky="nsew")

        if i==0 and j < 5:
            ab2 = tk.Label(master=minion, text=f"{slot[j].split(':',1)[1]}", bg="floral white")
            ab2.pack(anchor = "w")
        if j < 5 and i != 0:
            label = tk.Label(master=minion, text=f"{slot[j].split(':',1)[1]}", bg="floral white")
            label.pack(anchor = "w")
        

def make_bk(da,can_2,slot,week,sloot,i):
    global variable
    for j in range(6):
        can_2.columnconfigure(j, weight=1)
        minion = tk.Frame(master=can_2,relief=tk.RIDGE,borderwidth=1, bg= "honeydew")
        minion.grid(row=0, column=j,padx=5, pady=2, sticky="nsew")
        try:
            lab = tk.Label(master=minion, text=f"{slot[j].split(':',1)[0]}", bg="honeydew")
            lab.pack(fill = "both",pady = 2)
        except IndexError:
            lab = tk.Label(master=minion, text= "Slots", bg="honeydew")
            lab.pack(fill = "both",pady = 2)

        minion = tk.Frame(master=can_2,relief=tk.FLAT,borderwidth=1, bg= "floral white",highlightthickness=1,highlightbackground="black")
        minion.grid(row=i+1, column=j,padx=0, pady=0, sticky="nsew")

        if i==0 and j < 5:
            ab2 = tk.Label(master=minion, text=f"{slot[j].split(':',1)[1]}", bg="floral white")
            ab2.pack(anchor = "w")
        if j < 5 and i != 0:
            label = tk.Label(master=minion, text=f"{slot[j].split(':',1)[1]}", bg="floral white")
            label.pack(anchor = "w")
        if j == 5:
            variable = tk.StringVar(master=minion)
            event_sl.append(variable)
            variable.set("pick a slot")
            w = tk.OptionMenu(minion, variable, *sloot[i-1])
            w.pack()
    

def can_book(da,can_2,slot,week,i,slots,frame,main_frame,service,username,doc):
    for j in range(6):
        can_2.columnconfigure(j, weight=1)
        minion = tk.Frame(master=can_2,relief=tk.RIDGE,borderwidth=1, bg= "lavender")
        minion.grid(row=0, column=j,padx=5, pady=2, sticky="nsew")
        try:
            lab = tk.Label(master=minion, text=f"{slot[j].split(':',1)[0]}", bg="lavender")
            lab.pack(fill = "both",pady = 2)
        except IndexError:
            lab = tk.Label(master=minion, text= "Slots", bg="lavender")
            lab.pack(fill = "both",pady = 2)

        minion = tk.Frame(master=can_2,relief=tk.FLAT,borderwidth=1, bg= "floral white",highlightthickness=1,highlightbackground="black")
        minion.grid(row=i+1, column=j,padx=0, pady=0, sticky="nsew")

        if i==0 and j < 5:
            ab2 = tk.Label(master=minion, text=f"{slot[j].split(':',1)[1]}", bg="floral white")
            ab2.pack(anchor = "w")
        if j < 5 and i != 0:
            label = tk.Label(master=minion, text=f"{slot[j].split(':',1)[1]}", bg="floral white")
            label.pack(anchor = "w")
        if j == 5:
            w = tk.Button(master=minion ,text='Cancel',bg="lavender",justify='center',command= lambda : remove_book(slots,service,i,frame,main_frame,username,doc))
            w.pack()


def remove_book(slots,service,i,frame,main_frame,username,doc):
    tex = f"Are you sure you want to cancel the following event:\n{slots[i]}"
    mess = messagebox.askokcancel(title= "Cancel Booking", message= tex,default="cancel")
    if mess == True:
        eventid = slots[i][0]
        eventid = eventid.replace("ID: ","")
        try:
            if doc == True:
                cancel_booking.doctor_cancellation(service,eventid,f'{username}@student.wethinkcode.co.za')
            else:
                cancel_booking.patient_cancellation(service,eventid,f'{username}@student.wethinkcode.co.za')
        except :
           messagebox.showerror(title= "Cancel Booking Failed", message="Something went wrong please try again",default="cancel")

        cancel_book(slots,username,service,frame,main_frame,doc)

