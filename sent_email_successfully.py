import os
import threading
import time
from tkinter import *


def error_animation(error_widget):
    try:
        t = 0
        while t < 0.5 and not kill_threads.isClosing:
            error_widget.place_configure(
                y=int(error_widget.place_info()["y"]) + ((abs(error_animation.feedback_height) * 2) * 0.2))
            time.sleep(0.1)
            t += 0.1
        else:
            while t < error_animation.sleep and not kill_threads.isClosing:
                if error_animation.sleep < t:
                    return
                time.sleep(0.1)
                t += 0.1
                pass

            while error_animation.t > 0 and not kill_threads.isClosing:
                if error_animation.t < 0:
                    return
                error_widget.place_configure(
                    y=int(error_widget.place_info()["y"]) - ((abs(error_animation.feedback_height) * 2) * 0.2))
                time.sleep(0.1)
                error_animation.t -= 0.1
            error_widget.place_configure(y=error_animation.feedback_height)
            error_animation.counter = 0
    except:
        pass


def switch_window():
    os.system('python login.py')


def kill_threads():
    try:
        if error_animation.t1.is_alive():
            return
    except:
        pass
    error_animation.sleep = 0.1
    error_animation.t = -5
    root.destroy()


def return_to_login():
    try:
        if error_animation.t1.is_alive():
            return
    except:
        pass
    threading.Thread(target=switch_window).start()
    time.sleep(1.6)
    kill_threads()


def display_feedback(widget):
    try:
        if error_animation.counter > 0:
            error_animation.counter = 1
            return
        error_animation.t = 0.5
        error_animation.t1 = threading.Thread(target=error_animation, args={widget})
        error_animation.t1.start()
        error_animation.counter = 1
    except:
        pass



# ------------------------------------------------------------------------------
error_animation.sleep = 2
error_animation.t = 0.5
error_animation.counter = 0
error_animation.feedback_height = -75
kill_threads.isClosing = False

root = Tk()

width = 1440
height = 735

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = ((screen_width / 2) - (width / 2))
y = ((screen_height / 2) - (height / 2))

root.geometry(f'{width}x{height}+{int(x)}+{int(y) - 30}')
root.configure(bg="#ffffff")
root.title("EMAIL SENT SUCCESSFULLY")
canvas = Canvas(
    root,
    bg="#ffffff",
    height=735,
    width=1440,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"images/sent_email_successfully/background.png")
background = canvas.create_image(
    720.0, 367.5,
    image=background_img)

img0 = PhotoImage(file=f"images/sent_email_successfully/img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    bg="#ffffff",
    activebackground="#ffffff",
    highlightthickness=0,
    command=return_to_login,
    relief="flat")

b0.place(
    x=686, y=186,
    width=69,
    height=52)

feedback_frame = Frame(canvas)
feedback_frame.place(x=width / 2, y=error_animation.feedback_height, anchor=CENTER)

success_img = PhotoImage(file="images/account_recovery/email-verification.png")
success_lbl = Label(feedback_frame, image=success_img)
success_lbl.pack()
# success_lbl.place(x=width / 2, y=error_animation.feedback_height, anchor=CENTER)

with open('portal.txt', 'r') as f:
    username = f.read()

verification_email = Label(feedback_frame, text=username, font=("", 13, "bold"), bg="#2C6B46",
                           fg="#87BD9D")
verification_email.place(relx=0.15, rely=0.7)



error_animation.t = 0.5
error_animation.feedback_height = -78
error_animation.t1 = threading.Thread(target=error_animation, args={feedback_frame})
error_animation.t1.start()
error_animation.counter = 1

root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", kill_threads)
root.mainloop()
