from tkinter import *
from tkinter.ttk import Progressbar
import speedtest
import threading

def set_user_agent():
    # Define a custom User-Agent string
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    # Set the custom User-Agent string
    speedtest.build_user_agent = lambda: user_agent

set_user_agent()


def Speedcheck():
    progress_bar.place(x=20, y=290, height=15, width=460)
    progress_bar.start(10)  # Start the progress bar animation
    sp_button.config(state=DISABLED)  # Disable the button while checking speed
    thread = threading.Thread(target=check_speed)  # Create a thread for speed checking
    thread.start()

def check_speed():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download() / (10 ** 6), 2))
    up = str(round(sp.upload() / (10 ** 6), 2))

    lab_down.config(text=f"{down} Mbps")
    lab_up.config(text=f"{up} Mbps")    

    download = float(down)
    upload = float(up)

    low = "#FD0101"
    average = "#01FD45"
    high = "##76FF76"

    if download < 10:
        lab_down.config(bg=low)
    elif 10 <= download >= 50:
        lab_down.config(bg=average)
    else:
        lab_down.config(bg=high)

    if upload < 10:
        lab_up.config(bg=low)
    elif 10 <= upload >= 50:
        lab_up.config(bg=average)
    else:
        lab_up.config(bg=high)


    progress_bar.stop()  
    progress_bar.place_forget()
    
    sp_button.config(state=NORMAL)  # Enable the button after speed check

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x350")
sp.config(bg="#8FFCE5")

lab = Label(sp, text="INTERNET SPEED TEST", font=("Courier New", 28, "bold"), bg="#00B6DE", fg="black")
lab.place(x=20, y=20, height=50, width=460)

lab = Label(sp, text="Download Speed", font=("Arial", 23, "bold"), bg="#FF76EE")
lab.place(x=20, y=100, height=40, width=300)

lab_down = Label(sp, text="00", font=("Arial", 20), bg="#ffe6b3")
lab_down.place(x=320, y=100, height=40, width=160)

lab = Label(sp, text="Upload Speed", font=("Arial", 23, "bold"), bg="#E2FD01")
lab.place(x=20, y=160, height=40, width=300)

lab_up = Label(sp, text="00", font=("Arial", 20), bg="#ffe6b3")
lab_up.place(x=320, y=160, height=40, width=160)

sp_button = Button(sp, text="CHECK SPEED", font=("Courier New", 28, "bold"), relief=RAISED, bg="#00B6DE", command=Speedcheck)
sp_button.place(x=20, y=220, height=50, width=460)

progress_bar = Progressbar(sp, orient=HORIZONTAL, length=460, mode='indeterminate', style='TProgressbar')
    
sp.mainloop()
