from tkinter import *
import speedtest


def Speedchack():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download() / (10 ** 6), 3)) + " Mbps"
    up = str(round(sp.download() / (10 ** 6), 3)) + " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x650")
sp.config(bg="#3b4370")

lab = Label(sp, text="Internet Speed Test", font=("Time New Roman", 30, "bold"), bg="#90f090", fg="black")
lab.place(x=60, y=40, height=50, width=380)

lab = Label(sp, text="Download Speed", font=("Time New Roman", 30, "bold"), bg="#ffd700")
lab.place(x=60, y=130, height=50, width=380)

lab_down = Label(sp, text="00", font=("Time New Roman", 30, "bold"), bg="#ff8c00")
lab_down.place(x=60, y=200, height=50, width=380)

lab = Label(sp, text="Upload Speed", font=("Time New Roman", 30, "bold"), bg="#ffd700")
lab.place(x=60, y=290, height=50, width=380)

lab_up = Label(sp, text="00", font=("Time New Roman", 30, "bold"), bg="#ff8c00")
lab_up.place(x=60, y=360, height=50, width=380)

button = Button(sp, text="Check Speed", font=("Time New Roman", 30, "bold"), relief=RAISED, bg="#ff6f61", command=Speedchack)
button.place(x=60, y=460, height=50, width=380)

sp.mainloop()
