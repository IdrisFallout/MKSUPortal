import os
import sys
import threading
import time
import webbrowser
from tkinter import *

open('portal.txt', 'w').close()
splash = Tk()

width = 606
height = 363

screen_width = splash.winfo_screenwidth()
screen_height = splash.winfo_screenheight()

x = ((screen_width / 2) - (width / 2))
y = ((screen_height / 2) - (height / 2))

splash.geometry(f'{width}x{height}+{int(x)}+{int(y) - 30}')
splash.overrideredirect(True)

splash.configure(bg="#ffffff")


def kill_splash():
    state = True
    while state:
        with open('portal.txt', 'r') as f:
            feedback = f.read()
        if feedback.split(":")[0] == 'SUCCESS':
            state = False
    else:
        splash.destroy()
        return


def switch_window():
    os.system('python login.py')


def go_to_login():
    threading.Thread(target=switch_window).start()
    kill_splash()


canvas = Canvas(splash, bg="#ffffff", height=363, width=606, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"images/login/splash-screen/background.png")
background = canvas.create_image(303.0, 181.5, image=background_img)

img0 = PhotoImage(file=f"images/login/splash-screen/img0.png")
b0 = Label(image=img0, borderwidth=0, highlightthickness=0, bd=0, activebackground="black", relief="flat")
b0.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/IdrisFallout"))

b0.place(x=469, y=334, width=121, height=16)

img1 = PhotoImage(file=f"images/login/splash-screen/img1.png")
b1 = Label(image=img1, borderwidth=0, highlightthickness=0, bd=0, activebackground="black", relief="flat")

b1.place(x=15, y=333, width=86, height=17)

splash.resizable(False, False)

# threading.Thread(target=kill_splash).start()
splash.after(3000, go_to_login)
splash.mainloop()
