import turtle
from tkinter import ttk
import tkinter as tk
from datetime import timedelta
import datetime

event_sl = []

def view_calendar(slots):
    window = tk.Tk()
    window.title("The Code Clinic")
    for i in range(len(slots)):
        slot = slots[i].split(",")

        for j in range(4):
            frame = tk.Frame(master=window,relief=tk.RIDGE,borderwidth=1, bg= "teal")
            frame.grid(row=i, column=j,padx=2, pady=5)
            label = tk.Label(master=frame, text=f"{slot[j]}", bg="honeydew")
            label.pack()
    window.mainloop()


def slot_select(slots):
    global variable,tings
    tings = slots
    # print(slots)
    wind = tk.Tk()
    wind.title("The Code Clinic")
    wind.resizable(False,True)
    wind.minsize(1215,350)


    main_frame = tk.Frame(master=wind, borderwidth=0,bg='honeydew')
    
    container = tk.Canvas(master=main_frame,bg='honeydew')
    frame = tk.Frame(master=container,relief=tk.RIDGE,borderwidth=1, bg= "honeydew")
    scroll = ttk.Scrollbar(master=main_frame,orient= 'vertical', command=container.yview)
    container.configure(yscrollcommand= scroll.set)


    sloot = sloots(slots)
    print(sloot)
    for i in range(len(slots)):
        slot = slots[i].split("\n")
        for j in range(8):
            frame1 = tk.Frame(master=frame,relief=tk.RIDGE,borderwidth=1, bg= "beige")
            frame1.grid(row=0, column=j,padx=2, pady=2)
            try:
                lab = tk.Label(master=frame1, text=f"{slot[j].split(':',1)[0]}", bg="beige")
                lab.pack()
            except IndexError:
                lab1 = tk.Label(master=frame1, text= "Slots", bg="beige")

            frame1 = tk.Frame(master=frame,relief=tk.RIDGE,borderwidth=1, bg= "beige")
            frame1.grid(row=i+1, column=j,padx=2, pady=2)

            if i==0 and j < 7:
                ab2 = tk.Label(master=frame1, text=f"{slot[j].split(':',1)[1]}", bg="floral white")
                ab2.pack()
            if j < 7 and i != 0:
                label = tk.Label(master=frame1, text=f"{slot[j].split(':',1)[1]}", bg="floral white")
                label.pack()
            if j == 7:
                variable = tk.StringVar(master=frame1)
                event_sl.append(variable)
                variable.set("pick a slot")
                w = tk.OptionMenu(frame1, variable, *sloot[i-1])
                w.pack()

                lab1.pack()

    scroll.pack(side='right', fill='y') 
    frame.pack(fill='both')
    container.pack(fill='both')
    container.create_window((0,0) , window=frame)
    frame.bind('<Configure>',lambda e: container.configure(scrollregion = container.bbox("all")))
    main_frame.pack(fill="both")

    button = tk.Button(master=wind ,text='next',justify='center',command=callback)
    button.pack()

    wind.configure(bg='honeydew')
    wind.mainloop()

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

