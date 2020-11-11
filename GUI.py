import turtle
import tkinter as tk
from datetime import timedelta
import datetime

def GUI(slots):
    window = tk.Tk()
    window.title("The Code Clinic")
    sloot = sloots(slots)
    print(sloot)
    for i in range(len(slots)):
        slot = slots[i].split(" ")

        for j in range(5):
            frame = tk.Frame(master=window,relief=tk.RIDGE,borderwidth=1, bg= "teal")
            frame.grid(row=i, column=j,padx=2, pady=5)
            if j < 4 or i == 0:
                label = tk.Label(master=frame, text=f"{slot[j]}", bg="honeydew")
                label.pack()
            if j == 4 and i != 0:
                # label = tk.Label(master=frame, text=f"oats", bg="honeydew")
                # label.pack()
                # for y in range(len(sloot[i-1])):
                variable = tk.StringVar(master=frame)
                variable.set("pick a slot")
                w = tk.OptionMenu(frame, variable, *sloot[i-1])
                w.pack()

    window.mainloop()


def sloots(slots):
    sloots = []
    
    for i in range(len(slots)):
        if i != 0:
            slot = slots[i].split(" ")
            sl = slot[-1].split(";")
            date = slot[-2].split("-")
            # r = int(sl[1].replace(":","")) - int(sl[0].replace(":",""))
            # r = int(r/100)
            
            tim = datetime.datetime(int(date[0]),int(date[1]),int(date[2]),int(sl[0].replace(':','')[:2]),int(sl[0].replace(':','')[2:]))

            slo = []
            while str(tim)[11:][:5] != sl[1] :
                slo.append(f"{str(tim)[11:][:5]} : {str(tim + timedelta(hours=0.5))[11:][:5]}")
                tim = (tim + timedelta(hours=0.5))
            sloots.append(slo)
    return(sloots)

if __name__ == "__main__":
    GUI()