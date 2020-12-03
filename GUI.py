import turtle
from tkinter import ttk
import tkinter as tk
from datetime import timedelta
import datetime

event_sl = []

def main_gui(slots):
    wind = tk.Tk()
    wind.title("The Code Clinic")
    wind.geometry('800x500')

    sidebar = tk.Frame(master=wind, borderwidth=0,bg='red')
    sidebar.place(relx=0,rely=0,relwidth=0.25,relheight=1)

    main_frame = tk.Frame(master=wind, borderwidth=2,bg='blue')
    main_frame.place(relx=0.25,rely=0,relwidth=0.75,relheight=1)

    container = tk.Canvas(master=main_frame)
    frame = tk.Frame(master=container,relief=tk.RIDGE,borderwidth=1, bg= "green")
    scroll = ttk.Scrollbar(master=main_frame,orient= 'vertical', command=container.yview)
    container.configure(yscrollcommand= scroll.set)

    scroll.pack(side='right', fill='y') 
    frame.pack(fill='both',expand=1)
    container.pack(fill='both',expand=1)
    container.create_window((0,0) , window=frame)
    frame.bind('<Configure>',lambda e: container.configure(scrollregion = container.bbox("all")))

    button1 = tk.Button(master=sidebar ,text='View Calendar',justify='center',command=view_cal)
    button1.place(relx=0,rely=0.15,relwidth=1,relheight=0.17)
    button2 = tk.Button(master=sidebar ,text='Make Booking',justify='center',command=book_slot)
    button2.place(relx=0,rely=0.32,relwidth=1,relheight=0.17)
    button3 = tk.Button(master=sidebar ,text='Cancel Booking',justify='center',command=cancel_book)
    button3.place(relx=0,rely=0.49,relwidth=1,relheight=0.17)
    button4 = tk.Button(master=sidebar ,text='Help',justify='center',command=help_)
    button4.place(relx=0,rely=0.66,relwidth=1,relheight=0.17)
    button5 = tk.Button(master=sidebar ,text='LogOut',justify='center',command=log_out)
    button5.place(relx=0,rely=0.83,relwidth=1,relheight=0.17)

    content(slots,frame,main_frame)
    wind.mainloop()


def content(slots, frame,main_frame):
    global variable,tings
    tings = slots
    button = tk.Button(master=main_frame ,text='next',justify='center',command=callback)
    button.pack()

    sloot = sloots(slots)
    print(sloot)
    for i in range(len(slots)):
        slot = slots[i].split("\n")
        if slot[0].split(':',1)[0] == "ID":
            slot.remove(slot[0])
            print(slot)
        for j in range(7):
            frame1 = tk.Frame(master=frame,relief=tk.RIDGE,borderwidth=1, bg= "beige")
            frame1.grid(row=0, column=j,padx=2, pady=2)
            try:
                lab = tk.Label(master=frame1, text=f"{slot[j].split(':',1)[0]}", bg="beige")
                lab.pack()
            except IndexError:
                lab = tk.Label(master=frame1, text= "Slots", bg="beige")
                lab.pack()

            frame1 = tk.Frame(master=frame,relief=tk.RIDGE,borderwidth=1, bg= "beige")
            frame1.grid(row=i+1, column=j,padx=2, pady=2)

            if i==0 and j < 6:
                ab2 = tk.Label(master=frame1, text=f"{slot[j].split(':',1)[1]}", bg="floral white")
                ab2.pack()
            if j < 6 and i != 0:
                label = tk.Label(master=frame1, text=f"{slot[j].split(':',1)[1]}", bg="floral white")
                label.pack()
            if j == 6:
                variable = tk.StringVar(master=frame1)
                event_sl.append(variable)
                variable.set("pick a slot")
                w = tk.OptionMenu(frame1, variable, *sloot[i-1])
                w.pack()


   


    
def callback():
    global event_sl,tings
    
    for v in range(len(event_sl)):
        if event_sl[v].get() != "pick a slot":
            print(event_sl[v].get())
            s = tings[v].split("\n")
            print(s)
            print(v)

    # return s,v

def sloots(slots):
    sloots = []
    
    for i in range(len(slots)):
        if i != 0:
            slot = slots[i].split("\n")
            sl1 = (slot[2].replace("Start Time: ","")).split(':')
            sl2 = slot[3].replace("End Time: ","")
            date = slot[1].replace("Date: ", "")
            date = date.split('-')
           
            tim = datetime.datetime(int(date[0]),int(date[1]),int(date[2]),int(sl1[0]),int(sl1[1]))

            slo = []
        
            while str(tim)[11:][:5] != sl2 and str(tim)[11:][:5] <= sl2 :
                print(f"this is s_l2{sl2}")
                print(str(tim)[11:][:5] )
                slo.append(f"{str(tim)[11:][:5]} : {str(tim + timedelta(hours=0.5))[11:][:5]}")
                tim = (tim + timedelta(hours=0.5))
            slo.append('pick a slot')
            sloots.append(slo)
    return(sloots)

def view_cal():
    pass

def book_slot():
    pass

def cancel_book():
    pass

def help_():
    pass

def log_out():
    pass
