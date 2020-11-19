import turtle
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
    global variable
    # print(slots)
    window = tk.Tk()
    window.title("The Code Clinic")
    frame = tk.Frame(master=window,relief=tk.RIDGE,borderwidth=1, bg= "honeydew")
    sloot = sloots(slots)
    print(sloot)
    for i in range(len(slots)):
        slot = slots[i].split("\n")
        print(slot)

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
    frame.pack()
    button = tk.Button(master=window ,text='next',justify='center',command=callback)
    button.pack()
    # button.bind('<Button-1>',callback(variable))
    
    # valu = str((lb.get(tk.ACTIVE)))
    # print(valu) 
    # print(variable.get())
    window.mainloop()


def callback():
    global event_sl
    print("ello")
    for variable in event_sl:
        print(variable.get())
    # return variable

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
        
            while str(tim)[11:][:5] != sl2 :
                # print(f"this is s_l2{sl2}")
                # print(str(tim)[11:][:5] )
                slo.append(f"{str(tim)[11:][:5]} : {str(tim + timedelta(hours=0.5))[11:][:5]}")
                tim = (tim + timedelta(hours=0.5))
            slo.append('pick a slot')
            sloots.append(slo)
    return(sloots)

